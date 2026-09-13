# System State

_Last updated: 2026-09-14_

## Current Stack
- Astro v6.0.8, Bootstrap 5.3 dual-theme UI, static hosting on GitHub Pages.
- Content is Markdown-only under `src/pages/`; no database, no backend API.

## Recently Completed
- CLAUDE.md rewritten for Astro v6 standards (glob data fetching, asset
  path resolution, Bootstrap theme variables, sync doc protocol).
- `YearSelector.astro` reworked to dynamically discover class folders and
  navigate via an explicit "Go" button instead of an auto-change listener.
- `PostLayout.astro` widened (col-lg-10/col-xl-10) with a collapsible
  in-page table of contents (H2-H4) for long lecture notes.
- Architecture doc set trimmed from 5 to 3 files (this file, CLAUDE.md,
  architecture_map.md); `database_schema.md`/`api_registry.md` dropped
  since this project has no database or backend API to document.
- `architecture_map.md` regenerated from `architecture_map_draft.md`
  (draft removed) with concise English one-line descriptions.

## In Progress / Planned
- SSO integration via `https://win.upj53.kr` (planned; not yet wired in).
- Plan to deprecate hardcoded `ADMIN_PASSWORD`/`USER1_PASSWORD` once SSO
  auth lands.
- See `.tasks/2026-09-14-upgrade_astro.md` (Requirement 01 done; later
  requirements in that file are unfilled templates for future sessions).

## Known Issues / Follow-ups
- `chamcham_chloe/credentials.txt` and `env_backup_school.txt` are
  untracked plaintext copies of live secrets (GCP key, admin passwords)
  and are not covered by `.gitignore` — do not `git add` them; delete or
  gitignore before committing.
- `xyz/` (Unity privacy-policy tooling) and
  `chamcham_chloe/local_backup/` contain content unrelated to this site
  and can likely be removed.

## Sync Protocol
- `chamcham_chloe/sync_to_drive.py` uploads `SYNC_FILES`
  (`architecture_map.md`, `CLAUDE.md`, `system_state.md`) to Google
  Drive as Google Docs, prefixed with `PROJECT_PREFIX` (`school-`).
