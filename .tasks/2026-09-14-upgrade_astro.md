<!--
/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md
-->


## Requirement 01: Architecture Document Curation and Google Drive Sync Integration

### Context
- Framework: Astro v6.0.8 (Static Site Generation hosted on GitHub Pages)
- Current Working Directory: `/home/upj53/Workspace/sungil-i.github.io/`
- OS/SW: Ubuntu 20.04.6 LTS on Windows 11 Pro WSL

### Target Files
- `.tasks/2026-09-14-upgrade_astro.md`
- `.env`
- `CLAUDE.md`
- `chamcham_chloe/sync_to_drive.py`

### Tasks

#### Task 1: Document Curation & Scope Definition
- Retain only the 3 relevant architecture documents for Astro SSG:
  - `CLAUDE.md` (Core instructions, tech stack, and theme rules)
  - `architecture_map.md` (Directory hierarchy and layout map)
  - `system_state.md` (Operational state and task backlog)
- Explicitly exclude `database_schema.md` (no database in static markdown architecture) and `api_registry.md` (no backend endpoints on GitHub Pages).

#### Task 2: Refactor `chamcham_chloe/sync_to_drive.py`
- Target: `chamcham_chloe/sync_to_drive.py`
- Read `PROJECT_PREFIX` from `.env` (defaulting to `"school-"`).
- Update `target_docs` list to target only:
  - `CLAUDE.md`
  - `architecture_map.md`
  - `system_state.md`
- Prepend `PROJECT_PREFIX` to Google Drive target file names (e.g., `school-CLAUDE.md`).
- Ensure robust path resolution relative to project root without hardcoded machine paths where possible.

#### Task 3: Improve Environment Configuration
- Target: `.env`
- Add `AUTH_SERVER_URL="https://win.upj53.kr"` to configure planned SSO endpoint.
- Update `COOKIE_DOMAIN` comments for root domain sharing (`.upj53.kr`).
- Document deprecation of hardcoded credentials (`ADMIN_PASSWORD`, `USER1_PASSWORD`) when authenticating via external SSO.

#### Task 4: Upgrade `CLAUDE.md`
- Target: `CLAUDE.md`
- Update content to reflect Astro v6.0.8 standards:
  - Markdown layout and relative asset path rules (`src/assets/images/`).
  - Bootstrap 5.3 `data-bs-theme` dual-theme compatibility.
  - Mandatory use of `import.meta.glob('../pages/**/*.md', { eager: true })`.
  - Prefix convention (`PROJECT_PREFIX="school-"`) for sync operations.


<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 01'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->



## Requirement 02

Target file: `src/components/YearSelector.astro`, `src/utils/classEntries.ts`, `src/layouts/UpjLayout.astro`, `src/pages/upj53/index.md`

Environment: Ubuntu 20.04.6 LTS(bash) on Windows 11 Pro WSL (Local)

Design and implement a private archive section under `src/pages/upj53` that is strictly excluded from public student navigation and displays topic folders and documents in reverse chronological order.

### 1. Guard Public Navigation (`YearSelector.astro` & `classEntries.ts`)
- Review `src/components/YearSelector.astro` and `src/utils/classEntries.ts`.
- Ensure directory enumeration logic filters folder names strictly by 4-digit academic year pattern (`/^\d{4}$/`).
- Explicitly exclude `upj53` and non-year folders from appearing in the student-facing Year/Class dropdown list.

### 2. Create Archive Layout (`src/layouts/UpjLayout.astro`)
- Create a dedicated layout component `src/layouts/UpjLayout.astro` wrapping `MainLayout.astro`.
- Collect all markdown files under the private folder using `import.meta.glob('../pages/upj53/**/*.md', { eager: true })`.
- Parse relative paths to group markdown posts by sub-topic directory (e.g., `2026-csharp`, `2025-java-1`).
- Sort topic groups in reverse alphabetical order (`b.localeCompare(a)`) so the newest subject appears at the top.
- Inside each topic, sort posts in reverse alphabetical order by filename.
- Render the grouped posts using Bootstrap 5.3 list groups and badges with complete `data-bs-theme="dark|light"` compatibility.

### 3. Create Private Index Entry (`src/pages/upj53/index.md`)
- Create `src/pages/upj53/index.md` configured with `layout: ../../layouts/UpjLayout.astro` and frontmatter metadata (`title: "교사 전용 아카이브"`).
- Provide a clear container slot for introductory notes or personal announcements.

### 4. Verification Fixture
- Add a sample document `src/pages/upj53/2026-csharp/01-csharp-intro.md` with appropriate frontmatter (`layout: ../../../layouts/PostLayout.astro`, `title: "C# 커리큘럼 계획"`).
- Ensure Vite/Astro build (`npm run build`) compiles cleanly without broken route references.



<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 02'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->



## Requirement 03

Target file: `src/layouts/UpjLayout.astro`, `src/pages/upj53/`

Environment: Ubuntu 20.04.6 LTS(bash) on Windows 11 Pro WSL (Local)

Align the directory depth of private teacher archive files under `src/pages/upj53` to match public class paths (`src/pages/YYYY/[classId]/daily/`) so relative asset paths (`../../../../assets/images/`) remain identical when copying content.

### 1. Refactor Private Folder Structure (`src/pages/upj53/`)
- Reorganize subdirectories under `src/pages/upj53/` so all markdown files sit exactly 3 directory levels below `src/pages/`.
- Adopt the structure `src/pages/upj53/[classId]/daily/*.md` (e.g., `src/pages/upj53/2-10/daily/09-15-github_desktop_n_unity.md`) or `src/pages/upj53/YYYY-[classId]/daily/*.md`.
- Ensure all private markdown posts use:
  - `layout: ../../../../layouts/PostLayout.astro`
  - Image paths: `../../../../assets/images/[image_name].png`
- Clean up or migrate shallower legacy sample files (e.g., `src/pages/upj53/2026-csharp/01-csharp-intro.md`).

### 2. Update Archive Layout (`src/layouts/UpjLayout.astro`)
- Keep `import.meta.glob('../pages/upj53/**/*.md', { eager: true })` to collect all private posts.
- Filter out the entry point `src/pages/upj53/index.md`.
- Dynamically extract category/class group names from relative file paths (e.g., `2-10/daily` or `2026-2-10/daily`).
- Sort groups in reverse alphabetical order (`b.localeCompare(a)`).
- Within each group, sort posts in reverse chronological order (by date frontmatter or filename descending).
- Render grouped lists using Bootstrap 5.3 list-groups with complete dark/light theme compatibility (`data-bs-theme`).

### 3. Verification & Build Integrity
- Ensure `src/pages/upj53/2-10/daily/09-15-github_desktop_n_unity.md` exists with frontmatter (`title`, `layout`) and a sample image reference pointing to `../../../../assets/images/`.
- Run `npm run build` to confirm no broken layout imports, route conflicts, or Vite bundling errors.



<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 03'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->



## Requirement 04

Target file: `src/pages/2026/2-10/index.md`, `src/pages/upj53/2-10/index.md`, `src/pages/upj53/index.md`, `src/layouts/ClassLayout.astro`, `src/layouts/UpjLayout.astro`, `src/pages/upj53/2-10/daily/09-15-github_desktop_n_unity.md`

Environment: Ubuntu 20.04.6 LTS(bash) on Windows 11 Pro WSL (Local)

Enforce strict 3-tier relative path depth symmetry across public (`src/pages/YYYY/`) and private (`src/pages/upj53/`) namespaces to resolve Layout undefined and Vite ImageNotFound compilation errors.

### 1. Enforce Tier 2 Class Index Layout Symmetry (`src/pages/2026/2-10/index.md` & `src/pages/upj53/2-10/index.md`)
- Inspect the frontmatter of `src/pages/2026/2-10/index.md` and `src/pages/upj53/2-10/index.md`.
- Ensure the `layout` property in both files points strictly to `../../../layouts/ClassLayout.astro` (exactly 3 parent hops: `[classId]` -> `YYYY|upj53` -> `pages` -> `layouts`).
- Correct the regression where class index files erroneously used 4 parent hops (`../../../../layouts/ClassLayout.astro`), which traverses outside `src/` and causes Astro's runtime exception `Unable to render Layout because it is undefined!`.
- Inspect `src/pages/2026/index.md` and `src/pages/upj53/index.md` (Tier 1: depth 1) to verify they strictly use 2 parent hops (`../../layouts/...`, `../../assets/images/...`).
- Verify `src/layouts/ClassLayout.astro` imports `MainLayout.astro` properly and contains no syntax errors.

### 2. Enforce Tier 3 Daily Post Depth Symmetry & Resolve Image Asset Paths
- Ensure absolute directory depth parity between public and private daily notes:
  - Public path: `src/pages/YYYY/[classId]/daily/*.md` (depth = 3 subdirectories below `src/pages/`).
  - Private path: `src/pages/upj53/[classId]/daily/*.md` (depth = 3 subdirectories below `src/pages/`).
- Audit and relocate any misplaced private markdown files:
  - Verify if `09-15-github_desktop_n_unity.md` is located directly under `src/pages/upj53/2-10/` (missing `daily/`) or legacy paths (e.g., `src/pages/upj53/2026/2-10/`).
  - If misplaced, move it strictly to `src/pages/upj53/2-10/daily/09-15-github_desktop_n_unity.md`.
- Verify asset path resolution for Tier 3 posts:
  - Confirm image references use exactly 4 parent hops: `../../../../assets/images/2026-09-15-github_desktop_1.png`.
  - Confirm post layout references use exactly 4 parent hops: `layout: ../../../../layouts/PostLayout.astro`.
  - Check case-sensitive file existence of `src/assets/images/2026-09-15-github_desktop_1.png` on the WSL filesystem.

### 3. Verify Cross-Namespace Zero-Edit Portability
- Verify that moving or copying a daily post from `src/pages/upj53/2-10/daily/` to `src/pages/2026/2-10/daily/` (or vice-versa) requires zero changes to image paths (`../../../../assets/images/`) or layout references (`../../../../layouts/PostLayout.astro`).
- Check `src/layouts/UpjLayout.astro` glob parsing (`import.meta.glob('../pages/upj53/**/*.md', { eager: true })`) to ensure no orphan markdown files outside the 3-tier structure trigger eager Vite compilation errors.

### 4. Build & Dev Server Integrity Check
- Execute `npm run build` or Vite build check to verify that:
  - `src/pages/2026/2-10/index.md` and `src/pages/upj53/2-10/index.md` render without `Layout undefined` errors.
  - Accessing `http://localhost:4321/upj53/` compiles cleanly without Vite `ImageNotFound` exceptions.
  - No broken asset links or layout reference errors remain across both public and private namespaces.



<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 04'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 05'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 06'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 07'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 08'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 09'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 10'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 11'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 12'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 13'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 14'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 15'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 16'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 17'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 18'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 19'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 20'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 21'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 22'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 23'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 24'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 25'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 26'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 27'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 28'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 29'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 30'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 31'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 32'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 33'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 34'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 35'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 36'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 37'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 38'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 39'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 40'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 41'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 42'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 43'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 44'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 45'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 46'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 47'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 48'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 49'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 50'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 51'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 52'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 53'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 54'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 55'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 56'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 57'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 58'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 59'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 60'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 61'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 62'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 63'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 64'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 65'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 66'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 67'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 68'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 69'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 70'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 71'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 72'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 73'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 74'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 75'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 76'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 77'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 78'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 79'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 80'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 81'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 82'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 83'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 84'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 85'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 86'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 87'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 88'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 89'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 90'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 91'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 92'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 93'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 94'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 95'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 96'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 97'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 98'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 99'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-09-14-upgrade_astro.md`. ONLY execute 'Requirement 100'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->






