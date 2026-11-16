# System State

_Last updated: 2026-11-26_

## Current Stack
- Astro v7.x (`package.json` pins `^7.4.8`, `engines.node >=22.12.0`),
  Bootstrap 5.3 dual-theme UI, static hosting on GitHub Pages.
- CI (`.github/workflows/deploy.yml`): Node.js 22, `actions/checkout@v5`,
  `actions/setup-node@v5` (Node 24-compatible majors).
- Content is Markdown-only under `src/pages/`; no database, no backend API.

## Recently Completed
- Requirement 4 (`.tasks/2026-11-26-practice_wsl.md`): full `src/assets/`
  audit (images, java, files) and GitHub Pages green build restoration.
- Requirement 5 (`.tasks/2026-11-26-practice_wsl.md`): preventive guardrails.
  `CLAUDE.md` and `.claude/rules/markdown-content.md` now cover CRLF-blob
  re-staging, Binary Asset Hygiene, and the no-manual-extension-rename rule;
  `.gitignore` ignores `*:Zone.Identifier`; `.gitattributes` adds `*.svgz`;
  new `scripts/verify_assets.py` and `.githooks/pre-commit` (enable with
  `git config core.hooksPath .githooks`) block corrupted assets.
- `.tasks/2026-11-26-practice_wsl.md` (2026-11-26):
  - Req 1: Fixed the `[NoImageMetadata]` build failure by renaming the
    mislabeled `unity_gui.jpg` (really a PNG) to `unity_gui.png` and updating
    both markdown references; converted the hardcoded domain link in
    `src/pages/2026/2-10/test/2_test3.md` to a root-relative path.
  - Req 2: Replaced `* text eol=crlf` in `.gitattributes` with LF rules plus
    `binary` protection for images/fonts/pdf/zip; re-staged `unity_gui.png`
    (the committed blob had lost its `\r` bytes); upgraded deploy.yml actions
    to checkout@v5 / setup-node@v5; `.gitignore` now ignores
    `chamcham_chloe/credentials.txt`; `package.json` audited (unchanged).
  - Req 3: Rewrote `CLAUDE.md` (<200 lines) with `@architecture_map.md` /
    `@system_state.md` imports, path-scoped `.claude/rules/astro-ui.md` and
    `.claude/rules/markdown-content.md`, and the `CLAUDE.local.md` override
    convention (gitignored); refreshed `architecture_map.md` from
    `architecture_map_draft.md` (draft deleted); updated this file.
- Theme refactor (`.tasks/2026-10-06-refactor_at_home.md`, Req 01-02):
  `MainLayout.astro` footer uses `bg-body-tertiary`/`text-body-secondary`/
  `border-secondary-subtle`; `.btn-theme-adaptive` and the home class table
  use theme CSS variables; an inline `<head>` script syncs `data-bs-theme`
  with the `html.dark` class (ThemeToggle only toggles the class).
  `PostLayout.astro` back links now point to `/YYYY/[classId]/` (derived
  from `Astro.url.pathname`) instead of `history.back()`, with
  `text-body-secondary` / `btn-outline-secondary`. Build passes (48 pages).
- Doc sync pass (2026-10-06): `architecture_map.md` rewritten from
  `architecture_map_draft.md` (English, descriptions <=100 bytes; draft
  deleted); `credentials.txt` no longer exists on disk.
- Upgraded Astro from v6.0.8 to v7.3.2 (`.tasks/2026-09-14-upgrade_astro.md`);
  `CLAUDE.md`/`architecture_map.md` version references updated to match.
- Fixed Requirement 04 (3-tier path-depth symmetry): `src/pages/upj53/2-10/index.md`
  had no frontmatter at all (guaranteed "Layout undefined"); gave it the same
  `../../../layouts/ClassLayout.astro` + `classId` frontmatter as the public
  class index. Removed 6 empty `![](../../../../assets/images/)` refs in
  `src/pages/upj53/2-10/daily/09-15-github_desktop_n_unity.md` that were
  causing a Vite `[UNRESOLVED_IMPORT]` build failure. `npm run build` now
  completes cleanly (46 pages) and both `/2026/2-10/` and `/upj53/2-10/`
  render.
- CLAUDE.md rewritten for Astro v6 standards (glob data fetching, asset
  path resolution, Bootstrap theme variables, sync doc protocol).
- `YearSelector.astro` reworked to dynamically discover class folders and
  navigate via an explicit "Go" button instead of an auto-change listener.
- `PostLayout.astro` widened (col-lg-10/col-xl-10) with a collapsible
  in-page table of contents (H2-H4) for long lecture notes.
- Architecture doc set trimmed from 5 to 3 files (this file, CLAUDE.md,
  architecture_map.md); `database_schema.md`/`api_registry.md` dropped
  since this project has no database or backend API to document.
- Added a private teacher-only archive under `src/pages/upj53/`
  (Requirement 02): `UpjLayout.astro` groups its Markdown docs, and
  `classEntries.ts` enumerates only 4-digit year folders so `upj53` never
  appears in the public `YearSelector.astro` dropdown.
- Realigned the private archive to match public path depth (Requirement
  03): posts now live at `src/pages/upj53/[classId]/daily/*.md`, same
  depth as `src/pages/YYYY/[classId]/daily/`, so `layout`/image relative
  paths stay identical when copying content between them; `UpjLayout.astro`
  groups by `classId` and sorts by `date` (falling back to filename).
- Doc sync pass (2026-09-16): regenerated `architecture_map.md` from
  `generate_architecture_map.py`'s `architecture_map_draft.md` output
  (draft deleted after merge), reconciled it against the actual repo/git
  state, and corrected two stale claims below that no longer matched
  reality.

## In Progress / Planned
- Verify and commit/push the Requirement 1-3 changes (Git status review first).
- Run `python -m chamcham_chloe.sync_to_drive` to sync the SSOT docs to Google Drive.
- SSO integration via `https://win.upj53.kr` (planned; not yet wired in).
- Plan to deprecate hardcoded `ADMIN_PASSWORD`/`USER1_PASSWORD` once SSO
  auth lands.

## Known Issues / Follow-ups
- **CRITICAL - secrets remain in git history:** `env_backup_*.txt`
  (`AUTH_SECRET_KEY`, `ADMIN_PASSWORD`, `USER1_PASSWORD`, GCP Drive folder ID)
  were committed (`78a1780`, `50d7dc8`) and pushed. They are no longer
  tracked (`git ls-files` clean, verified 2026-11-26; ignored since
  `09f2dd9`), but history still holds them. Recommended (needs explicit
  sign-off): rotate the secrets and GCP key, then scrub history with
  `git filter-repo` or BFG. Local copies were left in place.
- `chamcham_chloe/credentials.json` (GCP key) is gitignored and untracked;
  `credentials.txt` exists locally but is gitignored and untracked (2026-11-26).
- `xyz/` (Unity privacy-policy tooling) contains content unrelated to
  this site and can likely be removed.

## Sync Protocol
- `chamcham_chloe/sync_to_drive.py` uploads `SYNC_FILES`
  (`architecture_map.md`, `CLAUDE.md`, `system_state.md`) to Google
  Drive as Google Docs, prefixed with `PROJECT_PREFIX` (`school-`).
