#!/usr/bin/env python3
"""Verify binary integrity of files under src/assets/ (stdlib only).

Usage:
  python3 scripts/verify_assets.py            # scan all of src/assets/
  python3 scripts/verify_assets.py PATH...    # scan specific files
  python3 scripts/verify_assets.py --staged   # also check staged (index) blobs

Exit code 0 = clean, 1 = problems found.
"""
import subprocess
import sys
from pathlib import Path

ASSET_DIR = "src/assets"

# extension -> accepted magic-byte checks
SIGNATURES = {
    ".png": [lambda b: b.startswith(b"\x89PNG\r\n\x1a\n")],
    ".jpg": [lambda b: b.startswith(b"\xff\xd8\xff")],
    ".jpeg": [lambda b: b.startswith(b"\xff\xd8\xff")],
    ".gif": [lambda b: b.startswith((b"GIF87a", b"GIF89a"))],
    ".webp": [lambda b: b[:4] == b"RIFF" and b[8:12] == b"WEBP"],
    ".pdf": [lambda b: b.startswith(b"%PDF-")],
}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True)


def check_bytes(label, data, ext):
    """Return a list of problems for the given content."""
    if len(data) == 0:
        return [f"{label}: zero-byte file"]
    checks = SIGNATURES.get(ext)
    if checks and not any(c(data) for c in checks):
        return [f"{label}: magic bytes do not match '{ext}' (head={data[:8]!r})"]
    # PNG signature contains \r\n; a CRLF-corrupted blob has \r\r\n instead.
    if ext == ".png" and data[:8] != b"\x89PNG\r\n\x1a\n":
        return [f"{label}: PNG signature corrupted (CRLF conversion?)"]
    return []


def staged_assets():
    out = git("diff", "--cached", "--name-only", "--diff-filter=AM", "-z", "--", ASSET_DIR)
    return [p for p in out.stdout.decode().split("\0") if p]


def main(argv):
    staged = "--staged" in argv
    paths = [a for a in argv if not a.startswith("--")]
    problems = []

    if paths:
        files = [Path(p) for p in paths]
    else:
        files = [p for p in Path(ASSET_DIR).rglob("*") if p.is_file()]

    for f in sorted(files):
        if "Zone.Identifier" in f.name:
            problems.append(f"{f}: leftover Windows Zone.Identifier metadata file")
            continue
        if not f.exists():
            problems.append(f"{f}: file not found")
            continue
        problems += check_bytes(str(f), f.read_bytes(), f.suffix.lower())

    if staged:
        for p in staged_assets():
            if "Zone.Identifier" in p:
                problems.append(f"{p}: staged Zone.Identifier file")
                continue
            blob = git("show", f":{p}")
            if blob.returncode != 0:
                continue
            problems += check_bytes(f"{p} (staged blob)", blob.stdout, Path(p).suffix.lower())

    if problems:
        print("Asset verification FAILED:", file=sys.stderr)
        for line in problems:
            print(f"  - {line}", file=sys.stderr)
        print("Fix: re-export a real image; if only the Git blob is bad, run "
              "'git rm --cached <path> && git add <path>'.", file=sys.stderr)
        return 1
    print(f"Asset verification OK ({len(files)} file(s) checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
