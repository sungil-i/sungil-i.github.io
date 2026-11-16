# 🧑‍🏫 IT Education Class Website Project Guidelines (Astro)

@architecture_map.md
@system_state.md

## 📌 Project Overview & Stack
- **Framework:** Astro SSG (v7.x; version pinned in `package.json`, Node `>=22.12.0`)
- **UI Toolkit:** Bootstrap 5.3 (Dark/Light dual theme)
- **Hosting:** GitHub Pages — https://sungil-i.github.io (CI: `.github/workflows/deploy.yml`)
- **Authentication (Planned):** SSO via `https://win.upj53.kr`
- **Purpose:** Class materials (Markdown), daily lecture logs, and performance assessment notes organized by year, semester, and classroom.

The directory tree and module inventory live in `architecture_map.md`; current status and open items live in `system_state.md` (both imported above). Do not duplicate them here.

## 🧩 Where Detailed Rules Live (`.claude/rules/`, path-scoped)
- `.claude/rules/astro-ui.md` → `src/layouts/**`, `src/components/**`: Bootstrap dual theme, `import.meta.glob` (never `Astro.glob()`), `PostLayout.astro` grid and back-link.
- `.claude/rules/markdown-content.md` → `src/pages/**/*.md(x)`: `MM-DD-subject_name.md` naming, frontmatter, 3-tier relative path depth, root-relative links.

## 🛠️ Build / Sync Commands
- `npm run dev` — local dev server
- `npm run build` — static production build (must exit 0 before finishing any task)
- `npm run preview` — preview the built `dist/`
- `python -m chamcham_chloe.sync_to_drive` — sync SSOT docs to Google Drive (`PROJECT_PREFIX="school-"`)

## 🔄 Drive Sync & Context Protocol
- Google Drive context files use the prefix in `PROJECT_PREFIX` (`school-`).
- Synchronized files: `CLAUDE.md`, `architecture_map.md`, `system_state.md`.
- Keep `CLAUDE.md` concise (<200 lines); put status in `system_state.md` and structure in `architecture_map.md`.

## 🔒 Git & Security Guardrails
- `.gitattributes`: text files use LF; binary assets (`*.png`, `*.jpg`, `*.webp`, `*.pdf`, fonts, ...) are `binary`. Never reintroduce a global `* text eol=crlf`, which corrupts images (`[NoImageMetadata]`).
- `.gitignore` isolates secrets: `.env*`, `env_backup_*.txt`, `chamcham_chloe/credentials.*`, `*.pem`, `*.key`. Never commit or print their contents.
- Do not delete local secret files without explicit sign-off; report them instead.
- Images in `src/assets/images/` must have the extension matching their real format (verify with `file`).
- Images committed before the `.gitattributes` binary protection may keep a CRLF-corrupted blob in `HEAD`; re-stage them with `git rm --cached <path> && git add <path>`.
- Verify new or updated images in `src/assets/` with `python3 scripts/verify_assets.py` (or `file`) and run `npm run build` before `git push`.
- Never rename an image extension by hand (e.g., `.webp`/`.png` -> `.jpg`) without true format re-encoding.
- Enable the shared pre-commit hook once per clone (Local Laptop and School PC): `git config core.hooksPath .githooks` (runs `scripts/verify_assets.py --staged` when `src/assets/` is staged).

## 💻 Local Override Convention (`CLAUDE.local.md`)
- Put machine-specific settings (WSL/Conda paths on Local Laptop vs School PC, personal notes) in `CLAUDE.local.md` at the repository root.
- `CLAUDE.local.md` is listed in `.gitignore`; never commit it.

## 📝 Assistant Response Tone & Manner
- Maintain the perspective of an encouraging IT educator; propose clear, well-structured, and easily digestible code for students.
- Always provide precise file paths and contextual explanations when suggesting modifications.
