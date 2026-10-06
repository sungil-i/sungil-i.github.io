# Architecture Map

## 1. Directory Structure
- ./ (project root)
  - CLAUDE.md, README.md, architecture_map.md, system_state.md
  - astro.config.mjs, package.json, package-lock.json, tsconfig.json
  - generate_architecture_map.py, export_code.py
  - env_backup_school.txt, env_backup_local.txt (plaintext secrets; tracked in git)
  - .claudeignore, .gitignore, .vscode/
  - .github/workflows/deploy.yml
  - .tasks/ (Claude Code task specs, not deployed)
    - 2026-07-05-Astro_layout.md, 2026-09-14-upgrade_astro.md
    - 2026-10-06-refactor_at_home.md, __MEMO__.md
  - chamcham_chloe/ (Drive sync tooling)
    - sync_to_drive.py
    - credentials.json (GCP service account key, gitignored)
  - marp_presentation/
    - class_01.md, class_01.html
  - xyz/ (unrelated Unity privacy-policy tooling, not part of the site)
  - public/
    - favicon.ico, favicon.svg
  - src/
    - pages/ (Markdown routes)
      - index.md
      - 2025/index.md, 2025/3-10/index.md
      - 2026/index.md
      - 2026/2-10/ (index.md, daily/*.md, test/*.md)
      - 2026/3-10/ (index.md, daily/*.md, test/test1.md)
      - 2026/Java1/ (index.md, daily/*.md, test/*.md)
      - upj53/ (private teacher-only archive, excluded from public nav)
        - index.md
        - 2-10/index.md
        - 2-10/daily/*.md
    - layouts/
      - MainLayout.astro, ClassLayout.astro, PostLayout.astro, UpjLayout.astro
    - components/
      - ThemeToggle.astro, YearSelector.astro
    - utils/
      - classEntries.ts
    - assets/
      - images/, java/, files/

## 2. Module Summary
- `CLAUDE.md`: Assistant guidelines: stack, conventions, theming rules.
- `README.md`: Astro starter kit readme.
- `architecture_map.md`: This file; directory map and module summary.
- `system_state.md`: Rolling log of recent changes and open items.
- `astro.config.mjs`: Astro build and GitHub Pages site config.
- `package.json`: npm scripts and dependencies (Astro ^7.0.6).
- `package-lock.json`: Locked npm dependency versions.
- `tsconfig.json`: TypeScript compiler config.
- `generate_architecture_map.py`: Scans repo and writes architecture_map_draft.md.
- `export_code.py`: Exports project code into a single file.
- `env_backup_school.txt`: Plaintext .env backup (school); tracked in git, leak risk.
- `env_backup_local.txt`: Plaintext .env backup (local); tracked in git, leak risk.
- `.claudeignore`: Paths hidden from Claude Code (deps, build, env).
- `.github/workflows/deploy.yml`: CI that builds Astro and deploys to GitHub Pages.
- `.tasks/*.md`: Per-session task specs that drive Claude Code work.
- `chamcham_chloe/sync_to_drive.py`: Uploads SYNC_FILES docs to Google Drive.
- `chamcham_chloe/credentials.json`: GCP service account key (secret, gitignored).
- `marp_presentation/class_01.md`: Marp slide deck source for a Java class.
- `marp_presentation/class_01.html`: Rendered HTML of the Marp deck.
- `xyz/`: Unity privacy-policy scrapers and docs; unrelated to the site.
- `public/favicon.ico`, `public/favicon.svg`: Site favicons.
- `src/pages/index.md`: Site homepage.
- `src/pages/2025/index.md`: Class list for school year 2025.
- `src/pages/2025/3-10/index.md`: Class home for 2025 grade 3, class 10.
- `src/pages/2026/index.md`: Class list for school year 2026.
- `src/pages/2026/2-10/index.md`: Class home for 2026 grade 2, class 10.
- `src/pages/2026/2-10/daily/*.md`: Daily lecture notes (C#, OOP, Unity).
- `src/pages/2026/2-10/test/*.md`: Exam and performance assessment prep notes.
- `src/pages/2026/3-10/index.md`: Class home for 2026 grade 3, class 10.
- `src/pages/2026/3-10/daily/*.md`: Daily lecture notes (orientation, career, data).
- `src/pages/2026/3-10/test/test1.md`: Performance assessment 1 prep note.
- `src/pages/2026/Java1/index.md`: Class home for the Java Level 1 course.
- `src/pages/2026/Java1/daily/*.md`: Java course daily notes (Git, Markdown, JSP).
- `src/pages/2026/Java1/test/*.md`: Java course chapters (contents, syntax, controls).
- `src/pages/upj53/index.md`: Private archive entry; not in student nav.
- `src/pages/upj53/2-10/index.md`: Private class index; mirrors public class index.
- `src/pages/upj53/2-10/daily/*.md`: Private lecture notes at public path depth.
- `src/layouts/MainLayout.astro`: Base HTML shell, header, home class table, footer.
- `src/layouts/ClassLayout.astro`: Layout for class index pages.
- `src/layouts/PostLayout.astro`: Layout for posts; TOC, outline, back-to-class link.
- `src/layouts/UpjLayout.astro`: Private archive layout; groups by classId.
- `src/components/ThemeToggle.astro`: Dark/light switch; toggles html.dark class.
- `src/components/YearSelector.astro`: Year/class dropdown with Go button.
- `src/utils/classEntries.ts`: Lists class folders under 4-digit year dirs only.
- `src/assets/images/`: Images referenced from Markdown content.
- `src/assets/java/`: Java course slide images.
- `src/assets/files/`: PDFs referenced from Markdown content.

## 3. Data Flow (Astro Pipeline)
- Markdown (`src/pages/`) -> layout components (`MainLayout.astro`,
  `PostLayout.astro`, `UpjLayout.astro`, etc.) -> `npm run build` ->
  static hosting on GitHub Pages.
- `classEntries.ts` enumerates only 4-digit year folders under
  `src/pages/`, so `src/pages/upj53/` never reaches `YearSelector.astro`.
- `ClassLayout.astro` filters posts by URL path, so it renders identically
  for `src/pages/YYYY/[classId]/index.md` and `src/pages/upj53/[classId]/index.md`.
- Theme: `ThemeToggle.astro` toggles `html.dark`; an inline script in
  `MainLayout.astro` mirrors it to `data-bs-theme` for Bootstrap 5.3 classes.
- `PostLayout.astro` derives the back link `/segment0/segment1/` from
  `Astro.url.pathname` (no `history.back()`).
