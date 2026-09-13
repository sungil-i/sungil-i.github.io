# Architecture Map

## 1. Directory Structure
- ./ (project root)
  - CLAUDE.md, README.md
  - astro.config.mjs, package.json, package-lock.json, tsconfig.json
  - generate_architecture_map.py, export_code.py
  - .github/workflows/deploy.yml
  - .tasks/ (Claude Code session task specs, not deployed)
  - chamcham_chloe/ (Drive sync tooling)
    - sync_to_drive.py
    - credentials.json (secret, gitignored)
    - local_backup/ (misc backup scripts, unrelated to this site)
  - marp_presentation/ (Marp slide decks for class)
  - xyz/ (unrelated Unity privacy-policy tooling, not part of the site)
  - public/
    - favicon.ico
  - src/
    - pages/ (Markdown routes)
      - index.md (site home)
      - YYYY/index.md (year index)
      - YYYY/[classId]/index.md (class index)
      - YYYY/[classId]/daily/MM-DD-topic.md (lecture logs)
      - YYYY/[classId]/test/*.md (assessment notes)
    - layouts/
      - MainLayout.astro, ClassLayout.astro, PostLayout.astro
    - components/
      - ThemeToggle.astro, YearSelector.astro
    - utils/
      - classEntries.ts
    - assets/
      - images/, java/, files/ (images and PDFs used by Markdown)

## 2. Module Summary
- `CLAUDE.md`: Assistant guidelines: stack, conventions, theming rules.
- `astro.config.mjs`: Astro build and GitHub Pages site config.
- `package.json`: npm scripts and dependencies.
- `generate_architecture_map.py`: Scans repo, drafts architecture map.
- `export_code.py`: Local code export utility script.
- `.github/workflows/deploy.yml`: CI pipeline to build and deploy Pages.
- `.tasks/*.md`: Per-session task specs used to drive Claude Code work.
- `chamcham_chloe/sync_to_drive.py`: Pushes sync docs to Google Drive.
- `chamcham_chloe/credentials.json`: GCP service account key (secret).
- `chamcham_chloe/local_backup/`: Unrelated backup scripts, ignore.
- `marp_presentation/class_01.*`: Marp slide deck for a class session.
- `xyz/`: Unrelated Unity privacy-policy docs; not part of this site.
- `src/pages/index.md`: Site homepage.
- `src/pages/YYYY/index.md`: List of classes for a school year.
- `src/pages/YYYY/[classId]/index.md`: One class's home page.
- `src/pages/YYYY/[classId]/daily/*.md`: Daily lecture notes.
- `src/pages/YYYY/[classId]/test/*.md`: Assessment/exam prep notes.
- `src/layouts/MainLayout.astro`: Base HTML shell, theme toggle, nav.
- `src/layouts/ClassLayout.astro`: Layout for class index pages.
- `src/layouts/PostLayout.astro`: Layout for daily/test Markdown posts.
- `src/components/ThemeToggle.astro`: Dark/light theme switch button.
- `src/components/YearSelector.astro`: Year/class dropdown navigation.
- `src/utils/classEntries.ts`: Helper to enumerate class folders/data.
- `src/assets/images/`: Images referenced from Markdown content.
- `src/assets/java/`: Java course slide images.
- `src/assets/files/`: PDFs referenced from Markdown content.
- `public/favicon.ico`: Site favicon.

## 3. Data Flow (Astro Pipeline)
- Markdown (`src/pages/`) -> layout components (`MainLayout.astro`,
  `PostLayout.astro`, etc.) -> `npm run build` -> static hosting on
  GitHub Pages.
