# 🧑‍🏫 IT Education Class Website Project Guidelines (Astro)

## 📌 Project Overview
- **Framework:** Astro v7.3.2 (`package.json`: `^7.0.6`)
- **UI Toolkit:** Bootstrap 5.3 (Dark/Light Dual Theme Support)
- **Deployment/Hosting:** GitHub Pages
- **URL:** https://sungil-i.github.io
- **Authentication (Planned):** SSO Integration via `https://win.upj53.kr`
- **Purpose:** Providing class materials (Markdown), daily lecture logs, and performance assessment notes organized by year, semester, and classroom.

## 📂 Main Directory Structure & Roles
- `src/pages/`: Core routing folder based on Markdown (`*.md`). Subdivided into `YYYY/[classId]/daily/` (lecture notes) and `YYYY/[classId]/test/` (assessments).
- `src/pages/upj53/`: Private teacher-only archive, structured as `[classId]/daily/*.md` to mirror the public `YYYY/[classId]/daily/` path depth (same relative asset paths). Excluded from the public year/class dropdown because `classEntries.ts` only enumerates 4-digit year folders.
- `src/layouts/`: Page layouts (`MainLayout.astro`, `ClassLayout.astro`, `PostLayout.astro`, `UpjLayout.astro` for the private archive).
- `src/components/`: Reusable UI components (`ThemeToggle.astro`, `YearSelector.astro`).
- `src/assets/images/`: Centralized storage for images referenced inside Markdown docs (automatically optimized during build).
- `chamcham_chloe/`: Context synchronization tools (`sync_to_drive.py`, Google Drive credentials).

## 🚀 Technical Standards & Guidelines

### 1. Data Fetching (Markdown)
- For compiler stability and build performance in Astro v7, **always use `import.meta.glob('../pages/**/*.md', { eager: true })`** instead of `Astro.glob()`.

### 2. Markdown & Asset Path Resolution
- File naming convention: Strictly adhere to `MM-DD-subject_name.md` (e.g., `04-20-csharp_repeat.md`).
- Markdown files must specify `layout` and `title` in their frontmatter.
- When embedding images inside Markdown, resolve the exact relative path pointing to `src/assets/images/` (e.g., `../../../../assets/images/sample.png`) to ensure Astro's image optimization pipeline functions properly.

### 3. UI/UX & Theming (Bootstrap 5.3)
- Theming is controlled via `data-bs-theme="dark"|"light"` on the root `<html>` element managed by `ThemeToggle.astro`.
- Avoid hardcoded background/text colors in `.markdown-body`. Use Bootstrap theme variables (`var(--bs-body-color)`, `var(--bs-body-bg)`).
- **Markdown Tables:** Ensure table headers (`th`) and rows (`td`) inherit or explicitly resolve dark mode colors using `html[data-bs-theme="dark"]` selectors to maintain high contrast.
- **Layout Width:** Main content in `PostLayout.astro` utilizes `col-lg-10 col-xl-10` to maximize screen real estate for source code blocks.

### 4. Drive Sync & Context Protocol
- Google Drive context files use the prefix specified in `PROJECT_PREFIX` (e.g., `school-`).
- Synchronized architecture files: `CLAUDE.md`, `architecture_map.md`, and `system_state.md`.

## 📝 Assistant Response Tone & Manner
- Maintain the perspective of an encouraging IT educator; propose clear, well-structured, and easily digestible code for students.
- Always provide precise file paths and contextual explanations when suggesting modifications.