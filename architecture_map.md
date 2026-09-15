# Architecture Map

## 1. Directory Structure
- ./ (project root)
  - CLAUDE.md, README.md, architecture_map.md, system_state.md
  - astro.config.mjs, package.json, package-lock.json, tsconfig.json
  - generate_architecture_map.py, export_code.py
  - env_backup_school.txt, env_backup_local.txt (untracked plaintext secrets backups)
  - .github/workflows/deploy.yml
  - .tasks/ (Claude Code session task specs, not deployed)
  - chamcham_chloe/ (Drive sync tooling)
    - sync_to_drive.py
    - credentials.json (GCP service account key, gitignored)
  - marp_presentation/ (Marp slide decks for class, not part of the site)
  - xyz/ (unrelated Unity privacy-policy tooling, not part of the site)
  - public/
    - favicon.ico, favicon.svg
  - src/
    - pages/ (Markdown routes)
      - index.md (site home)
      - YYYY/index.md (year index, YYYY = 4-digit academic year, e.g. 2025, 2026)
      - YYYY/[classId]/index.md (class index)
      - YYYY/[classId]/daily/MM-DD-topic.md (lecture logs)
      - YYYY/[classId]/test/*.md (assessment notes)
      - upj53/ (private teacher-only archive, excluded from public nav)
        - index.md (archive entry, lists classes newest-first)
        - [classId]/daily/*.md (e.g. 2-10/daily/09-15-...md; mirrors public depth)
    - layouts/
      - MainLayout.astro, ClassLayout.astro, PostLayout.astro
      - UpjLayout.astro (private archive layout, wraps MainLayout)
    - components/
      - ThemeToggle.astro, YearSelector.astro
    - utils/
      - classEntries.ts
    - assets/
      - images/, java/, files/ (images and PDFs used by Markdown)

## 2. Module Summary
- `CLAUDE.md`: Assistant guidelines: stack, conventions, theming rules.
- `README.md`: Astro starter kit readme.
- `architecture_map.md`: This file; directory map and module summary.
- `system_state.md`: Rolling log of recent changes and open items.
- `astro.config.mjs`: Astro build and GitHub Pages site config.
- `package.json`, `package-lock.json`: npm scripts and dependencies.
- `tsconfig.json`: TypeScript compiler config.
- `generate_architecture_map.py`: Scans repo, drafts architecture map.
- `export_code.py`: Local code export utility script.
- `env_backup_school.txt`, `env_backup_local.txt`: Plaintext secrets backups; never commit.
- `.github/workflows/deploy.yml`: CI pipeline to build and deploy Pages.
- `.tasks/*.md`: Per-session task specs used to drive Claude Code work.
- `chamcham_chloe/sync_to_drive.py`: Pushes SYNC_FILES docs to Google Drive.
- `chamcham_chloe/credentials.json`: GCP service account key (secret).
- `marp_presentation/class_01.*`: Marp slide deck for a class session.
- `xyz/`: Unrelated Unity privacy-policy docs; not part of this site.
- `src/pages/index.md`: Site homepage.
- `src/pages/YYYY/index.md`: List of classes for a school year.
- `src/pages/YYYY/[classId]/index.md`: One class's home page.
- `src/pages/YYYY/[classId]/daily/*.md`: Daily lecture notes.
- `src/pages/YYYY/[classId]/test/*.md`: Assessment/exam prep notes.
- `src/pages/upj53/index.md`: Private archive entry, not in student nav.
- `src/pages/upj53/[classId]/daily/*.md`: Private lecture notes, public-depth.
- `src/layouts/MainLayout.astro`: Base HTML shell, theme toggle, nav.
- `src/layouts/ClassLayout.astro`: Layout for class index pages.
- `src/layouts/PostLayout.astro`: Layout for daily/test Markdown posts.
- `src/layouts/UpjLayout.astro`: Groups upj53 docs by classId, newest first.
- `src/components/ThemeToggle.astro`: Dark/light theme switch button.
- `src/components/YearSelector.astro`: Year/class dropdown navigation.
- `src/utils/classEntries.ts`: Lists class folders under 4-digit years only.
- `src/assets/images/`: Images referenced from Markdown content.
- `src/assets/java/`: Java course slide images.
- `src/assets/files/`: PDFs referenced from Markdown content.
- `public/favicon.ico`, `public/favicon.svg`: Site favicons.

## 3. Data Flow (Astro Pipeline)
- Markdown (`src/pages/`) -> layout components (`MainLayout.astro`,
  `PostLayout.astro`, `UpjLayout.astro`, etc.) -> `npm run build` ->
  static hosting on GitHub Pages.
- `classEntries.ts` enumerates only 4-digit year folders under
  `src/pages/`, so `src/pages/upj53/` (private archive) never reaches
  the public `YearSelector.astro` dropdown.
