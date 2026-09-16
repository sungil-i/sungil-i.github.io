# System State

_Last updated: 2026-09-16_

## Current Stack
- Astro v7.3.2 (`package.json` pins `^7.0.6`), Bootstrap 5.3 dual-theme UI,
  static hosting on GitHub Pages.
- Content is Markdown-only under `src/pages/`; no database, no backend API.

## Recently Completed
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
- SSO integration via `https://win.upj53.kr` (planned; not yet wired in).
- Plan to deprecate hardcoded `ADMIN_PASSWORD`/`USER1_PASSWORD` once SSO
  auth lands.
- See `.tasks/2026-09-14-upgrade_astro.md` (Requirements 01-04 done;
  later requirements in that file are unfilled templates for future
  sessions).

## Known Issues / Follow-ups
- **CRITICAL — live secret leak:** `env_backup_school.txt` and
  `env_backup_local.txt` are plaintext copies of `.env` (contain
  `AUTH_SECRET_KEY`, `ADMIN_PASSWORD`, `USER1_PASSWORD`, the GCP Drive
  folder ID). Neither is in `.gitignore`, and both are already **tracked
  and committed** (commits `78a1780`, `50d7dc8`) on `master`, which is
  up to date with `origin/master` — i.e. these secrets are already
  pushed to the remote. A prior note here claimed they were "untracked";
  verified 2026-09-16 that this was wrong. Recommended remediation
  (not yet done — needs explicit sign-off since it touches shared
  history): rotate `AUTH_SECRET_KEY`/`ADMIN_PASSWORD`/`USER1_PASSWORD`
  and the GCP service-account key, `git rm --cached` both files, add
  them to `.gitignore`, and scrub them from git history (e.g.
  `git filter-repo` or BFG) since a new commit alone leaves them in
  history.
- `chamcham_chloe/credentials.json` and `chamcham_chloe/credentials.txt`
  both still exist on disk (duplicate copies of the same GCP key). A
  prior note here claimed `credentials.txt` "no longer exists"; verified
  2026-09-16 that it does. Both are correctly covered by
  `chamcham_chloe/.gitignore` and are not tracked, so this is lower risk
  than the `env_backup_*` issue above, but the duplicate should probably
  be removed.
- `chamcham_chloe/__pycache__/sync_to_drive.cpython-311.pyc` is tracked
  in git (compiled bytecode cache; should be `git rm --cached` and
  ignored, not a secret but repo clutter).
- `xyz/` (Unity privacy-policy tooling) contains content unrelated to
  this site and can likely be removed.

## Sync Protocol
- `chamcham_chloe/sync_to_drive.py` uploads `SYNC_FILES`
  (`architecture_map.md`, `CLAUDE.md`, `system_state.md`) to Google
  Drive as Google Docs, prefixed with `PROJECT_PREFIX` (`school-`).
