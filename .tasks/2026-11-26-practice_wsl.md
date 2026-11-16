<!--
/home/upj53/Workspace/sungil-i.github.io/.tasks/2026-11-26-practice_wsl.md

/home/upj53/Workspace/sungil-i.github.io
.tasks/2026-11-26-practice_wsl.md

# Tasks : Task file 의 'Requirement 1'

노트북 설정의 '## 8. 🚨 [하네스 엔지니어링 제약] AI 행동 통제 규약 (Harness Rules)' 에 따라 아래 '요청사항' 을 만족하도록 Task file 의 Tasks 와 Claude REPL 을 위한 지시글을 생성해주세요. 지시글은 정확한 Task file 과 Target file 함께 올바른 상대 경로를 사용해주세요.

**요청사항**

## Current Directory (absolute path): "/home/upj53/Workspace/sungil-i.github.io"
## Task file (relative path): ".tasks/2026-11-26-practice_wsl.md"

## Environment:
* Current development environment : 실습실 PC
* OS/SW: Windows 11 Pro PowerShell + WSL Bridge

## 추가 지시: 토큰 절감을 위해 마크다운 파일 내부의 Task 지시글은 영문으로 작성하고, 바로 Claude REPL 에 사용할 수 있게 Claude REPL용 지시글을 출력해주세요. 지시글을 출력할 때 상대경로를 정확하게 사용해주세요. 외부 CLI 호출이 아닌, REPL 환경 내부에서 직접 타겟팅하여 격리 연산을 수행하기 위한 최적의 형태로 지시글을 만들어주세요.

## Tasks 내용



-->


## Requirement 1

Target file: `src/assets/images/unity_gui.jpg`, `src/pages/2026/2-10/test/2_test3.md`

Environment: Windows 11 Pro PowerShell + WSL Bridge (실습실 PC)

Diagnose and resolve the Astro `[NoImageMetadata]` build failure on `unity_gui.jpg` and standardize internal root-relative markdown links in `2_test3.md`.

### 1. Diagnose and Fix Corrupted Image Metadata (`src/assets/images/unity_gui.jpg`)
- Inspect `src/assets/images/unity_gui.jpg` using CLI diagnostics (`file src/assets/images/unity_gui.jpg` and byte-size check) to verify valid image magic bytes (JPEG/PNG/WebP) and non-zero file size.
- Search all markdown files under `src/pages/` referencing `unity_gui.jpg` to confirm exact relative path resolution (`../../../../assets/images/unity_gui.jpg`).
- Check `.gitattributes` and Git tracking status (`git ls-files --eol src/assets/images/unity_gui.jpg`) to ensure WSL `core.autocrlf` did not corrupt binary line endings.
- If `unity_gui.jpg` is corrupted, empty, or misnamed (e.g., WebP/PNG saved with `.jpg` extension), convert/re-export it as a valid image or update the extension and markdown reference accordingly.

### 2. Standardize Internal Links (`src/pages/2026/2-10/test/2_test3.md`)
- Inspect `src/pages/2026/2-10/test/2_test3.md`.
- Replace hardcoded production domain URLs (`https://sungil-i.github.io/2026/2-10/daily/10-08-shooting_game_1/`) with root-relative internal paths (`/2026/2-10/daily/10-08-shooting_game_1/`).
- Verify that the target markdown file (`src/pages/2026/2-10/daily/10-08-shooting_game_1.md`) exists on disk and matches the exact slug casing.

### 3. Verify Static Production Build
- Run `npm run build` inside the WSL environment to confirm that `vite-plugin-assets` processes image metadata cleanly without `[NoImageMetadata]` errors and all static routes compile with exit code 0.


<!--
-->



## Requirement 2

Target file: `.gitattributes`, `src/assets/images/unity_gui.png`, `.github/workflows/deploy.yml`, `package.json`, `.gitignore`

Environment: Windows 11 Pro PowerShell + WSL Bridge (실습실 PC)

Resolve Git CRLF binary corruption causing `[NoImageMetadata]` on `unity_gui.png` in CI, upgrade deprecated Node.js 20 GitHub Actions in `deploy.yml`, and audit/update `package.json`, `.gitignore`, and `.gitattributes`.

### 1. Fix `.gitattributes` Binary Protection & Re-index `unity_gui.png`
- Inspect `.gitattributes` at the repository root and remove unsafe global `* text eol=crlf` rules that corrupt binary assets.
- Configure `.gitattributes` with safe line-ending rules:
  - Set `* text=auto eol=lf` as the default.
  - Explicitly enforce `text eol=lf` for code, config, shell, and markdown files (`*.astro`, `*.ts`, `*.tsx`, `*.js`, `*.mjs`, `*.cjs`, `*.json`, `*.md`, `*.mdx`, `*.css`, `*.html`, `*.yml`, `*.yaml`, `*.py`, `*.sh`).
  - Explicitly enforce `binary` (`-text -diff`) for all binary assets (`*.png`, `*.jpg`, `*.jpeg`, `*.webp`, `*.gif`, `*.ico`, `*.pdf`, `*.zip`, `*.woff`, `*.woff2`, `*.ttf`, `*.eot`).
- Verify `src/assets/images/unity_gui.png` integrity both on disk (`file src/assets/images/unity_gui.png`) and in the Git object database (`git show HEAD:src/assets/images/unity_gui.png | file -`).
- Re-stage `src/assets/images/unity_gui.png` (`git rm --cached src/assets/images/unity_gui.png && git add src/assets/images/unity_gui.png`) so Git stores the uncorrupted binary blob. If the local file itself was corrupted by previous CRLF checkout, report it immediately so a clean image can be restored.

### 2. Resolve Node.js 20 Deprecation Warning in `.github/workflows/deploy.yml`
- Inspect `.github/workflows/deploy.yml`.
- Upgrade deprecated Node.js 20 action references (`actions/checkout@v4` and `actions/setup-node@v4`) to Node.js 24-compatible major versions (`actions/checkout@v5` or `@v6`, and `actions/setup-node@v5` or `@v6`).
- Update `node-version` in the `setup-node` step from `'20'` to `'22'` (or `'24'` LTS) to match Astro v7 runtime requirements and eliminate GitHub Actions Node.js 20 deprecation warnings.

### 3. Audit and Update `.gitignore` and `package.json`
- Inspect `.gitignore` and ensure complete coverage of:
  - Astro/Node build artifacts (`dist/`, `.astro/`, `.cache/`, `node_modules/`, `npm-debug.log*`).
  - Critical environment and secret backups (`.env`, `.env.*`, `!.env.example`, `env_backup_*.txt`, `chamcham_chloe/credentials.json`, `chamcham_chloe/credentials.txt`, `*.pem`, `*.key`).
  - Python runtime caches (`__pycache__/`, `*.py[cod]`, `.venv/`, `venv/`).
  - OS/IDE/CLI artifacts (`.DS_Store`, `Thumbs.db`, `Desktop.ini`, `.vscode/*`, `!.vscode/extensions.json`, `.claude/`, `.claude_session`).
- Check `git ls-files` for any already-tracked secret backup files (`env_backup_*.txt`, `credentials.*`) and report them in the summary without deleting local files.
- Inspect `package.json`:
  - Add or update `"engines": { "node": ">=22.0.0" }` to align local and CI Node.js runtimes.
  - Verify `"build": "astro build"` and existing dependency definitions remain intact without unintended version churn.

### 4. Verification
- Run `npm run build` in WSL to verify exit code 0 and clean asset metadata extraction for `src/assets/images/unity_gui.png`.
- Run `git status` and `git diff --check` to confirm clean line-ending attributes and zero binary corruption.


<!--
-->

## Requirement 3

Target file: `CLAUDE.md`, `.claude/rules/`, `architecture_map.md`, `system_state.md`, `architecture_map_draft.md`, `.gitignore`

Environment: Windows 11 Pro PowerShell + WSL Bridge (실습실 PC)

Upgrade `CLAUDE.md` using Claude Code memory best practices (`https://code.claude.com/docs/en/memory`), update `architecture_map.md` from `architecture_map_draft.md` (then delete the draft), and synchronize `system_state.md` with all completed work.

### 1. Upgrade `CLAUDE.md` Using Claude Code Memory Architecture
- Inspect existing `CLAUDE.md`, `.gitignore`, and any existing `.claude/` directory in the repository root.
- Refactor `CLAUDE.md` into a concise, scannable, high-signal project memory file (target under 200 lines) modeled after `backend/v2` and Claude Code memory guidelines (`code.claude.com/docs/en/memory`):
  - **SSOT Memory Imports**: Add `@architecture_map.md` and `@system_state.md` imports so Claude Code automatically loads the 3-document SSOT context without duplicating directory trees or status logs inside `CLAUDE.md`.
  - **Modular Path-Scoped Rules (`.claude/rules/`)**: Extract domain-specific standards into focused rule files with YAML `paths:` frontmatter so rules load contextually without diluting root `CLAUDE.md`:
    - Create `.claude/rules/astro-ui.md` (`paths: ["src/layouts/**/*.astro", "src/components/**/*.astro"]`): Document Bootstrap 5.3 `data-bs-theme="dark|light"` dual-theme rules, semantic theme variables (`var(--bs-body-color)`, `var(--bs-body-bg)`, `bg-body-tertiary`, `text-body-secondary`), `html[data-bs-theme="dark"]` table overrides, `PostLayout.astro` wide grid (`col-lg-10 col-xl-10`), and mandatory `import.meta.glob('../pages/**/*.md', { eager: true })` (forbidding `Astro.glob()`).
    - Create `.claude/rules/markdown-content.md` (`paths: ["src/pages/**/*.md", "src/pages/**/*.mdx"]`): Document 3-tier relative path depth symmetry across public (`src/pages/YYYY/[classId]/daily/`) and private (`src/pages/upj53/[classId]/daily/`) namespaces (`../../../../assets/images/` and `../../../../layouts/PostLayout.astro`), `MM-DD-subject_name.md` naming, required frontmatter (`layout`, `title`), and root-relative internal link format (`/YYYY/[classId]/...`).
  - **Local Override Convention (`CLAUDE.local.md`)**: Document `CLAUDE.local.md` for machine-specific overrides (e.g., WSL/Conda paths across Local Laptop and School PC) and ensure `CLAUDE.local.md` is listed in `.gitignore`.
  - **Essential Core Sections in `CLAUDE.md`**: Keep Project Overview & Stack (Astro SSG, Bootstrap 5.3, GitHub Pages `https://sungil-i.github.io`, planned SSO via `https://win.upj53.kr`), Build/Sync Commands (`npm run dev`, `npm run build`, `npm run preview`, `python -m chamcham_chloe.sync_to_drive` with `PROJECT_PREFIX="school-"`), Git/Security Guardrails (`.gitattributes` binary protection, `.gitignore` secret isolation), and **preserve all existing Role and Harness Constraints** intact.

### 2. Update `architecture_map.md` from `architecture_map_draft.md` and Delete Draft
- Read `architecture_map_draft.md` and existing `architecture_map.md`.
- Update `architecture_map.md` using the directory structure and file inventory from `architecture_map_draft.md` while strictly adhering to the rules in `CLAUDE.md`:
  - Reflect newly added/updated paths (including `.claude/rules/`, `.gitattributes`, `src/assets/images/unity_gui.png`, and `src/pages/upj53/`).
  - Exclude `architecture_map_draft.md` itself and any sensitive/temporary artifacts from the tree and module list.
  - Replace any generic placeholder strings (e.g., `"역할을 요약해주세요."`) with accurate, one-line Korean role summaries consistent with `architecture_map.md`.
  - Maintain the Astro SSG data flow section (`src/pages/**/*.md` -> Layout components -> `npm run build` -> GitHub Pages).
- Delete `architecture_map_draft.md` from the repository (`rm -f architecture_map_draft.md`) once `architecture_map.md` is updated and verified.

### 3. Update `system_state.md` Based on Work Performed
- Read `system_state.md` and review the completed work in `.tasks/2026-11-26-practice_wsl.md` (Requirements 1, 2, and 3).
- Update `system_state.md` in strict compliance with `CLAUDE.md`:
  - Record completed tasks:
    - Requirement 1: Fixed `[NoImageMetadata]` build failure by renaming mislabeled `unity_gui.jpg` to `unity_gui.png` and converting hardcoded domain link to root-relative path in `src/pages/2026/2-10/test/2_test3.md`.
    - Requirement 2: Configured `.gitattributes` binary asset protection (`*.png`, `*.jpg`, etc.) and LF line-ending rules, upgraded deprecated Node.js 20 GitHub Actions in `.github/workflows/deploy.yml` to Node.js 24-compatible versions, and audited `.gitignore` and `package.json`.
    - Requirement 3: Upgraded `CLAUDE.md` with Claude Code memory imports (`@architecture_map.md`, `@system_state.md`) and path-scoped `.claude/rules/`, updated `architecture_map.md` from `architecture_map_draft.md` (and deleted the draft), and updated `system_state.md`.
  - Update runtime compatibility status (CI Node.js 22/24 alignment) and active next steps (Git commit/push verification, `python -m chamcham_chloe.sync_to_drive` Google Drive SSOT sync, and `https://win.upj53.kr` SSO roadmap).

### 4. Verification
- Confirm `architecture_map_draft.md` is completely removed (`test ! -f architecture_map_draft.md`).
- Verify that `@architecture_map.md` and `@system_state.md` imports in `CLAUDE.md` point to valid existing files at the repository root.
- Run `npm run build` in WSL to verify exit code 0 and zero regressions.

<!--
-->

## Requirement 4

Target file: `src/assets/images/2026-09-15-github_desktop_1.png`, `src/assets/images/`, `src/assets/java/`, `src/assets/files/`

Environment: Windows 11 Pro PowerShell + WSL Bridge (실습실 PC)

Diagnose and resolve the `[NoImageMetadata]` build failure on `src/assets/images/2026-09-15-github_desktop_1.png`, and perform a comprehensive integrity audit across all asset subdirectories (`images`, `java`, `files`).

### 1. Diagnose and Fix `src/assets/images/2026-09-15-github_desktop_1.png`
- Inspect `src/assets/images/2026-09-15-github_desktop_1.png` both on the local WSL filesystem (`file` and byte-size check) and inside the Git object database (`git show HEAD:src/assets/images/2026-09-15-github_desktop_1.png | file -`).
- Identify the root cause:
  - Case A: The local file is valid PNG/JPEG/WebP, but the committed Git blob in `HEAD` was corrupted by historical CRLF conversion. Re-stage the clean binary file (`git rm --cached src/assets/images/2026-09-15-github_desktop_1.png && git add src/assets/images/2026-09-15-github_desktop_1.png`).
  - Case B: The file is actually JPEG or WebP saved with a `.png` extension. Rename it to match its true format using `git mv` and update all markdown references under `src/pages/`.
  - Case C: The file itself is truncated, zero-byte, or has corrupted magic bytes on disk. Report it clearly in the final summary so 원준님 can replace it with a fresh screenshot.

### 2. Full Asset Audit Across `src/assets/images/`, `src/assets/java/`, and `src/assets/files/`
- Recursively scan every file inside `src/assets/images/`, `src/assets/java/`, and `src/assets/files/`.
- Check each file for:
  1. Zero-byte or truncated files.
  2. Extension vs. real binary format mismatch (e.g., PNG saved as `.jpg`, WebP saved as `.png`, HTML error page saved as image/PDF).
  3. Git `HEAD` blob corruption vs. local working tree file (`git show HEAD:<path> | file -`).
  4. Leftover Windows NTFS metadata artifacts (`*:Zone.Identifier`).
- For any misnamed image file found during the audit, rename it via `git mv` to match its actual format and update any referencing markdown links in `src/pages/`.
- For any Git-blob-corrupted file whose working tree copy is intact, re-stage it so Git stores the clean binary blob.
- Remove any `*:Zone.Identifier` files if present, and report a complete audit table of all checked directories and any anomalies found.

### 3. Verify Static Production Build
- Run `npm run build` in WSL to verify that Astro and `vite-plugin-assets` process all assets cleanly and exit with code 0.
- Run `git status` to summarize all staged/modified files without committing unless instructed.


<!--
-->


## Requirement 5

Target file: `CLAUDE.md`, `.claude/rules/markdown-content.md`, `.gitignore`, `.gitattributes`, `scripts/verify_assets.py`, `.githooks/pre-commit`, `architecture_map.md`, `system_state.md`

Environment: Windows 11 Pro PowerShell + WSL Bridge (실습실 PC)

Codify image binary integrity guardrails in `CLAUDE.md` and `.claude/rules/markdown-content.md`, add automated asset verification scripts and Git hooks to prevent `[NoImageMetadata]` regressions, and synchronize `architecture_map.md` and `system_state.md`.

### 1. Update `CLAUDE.md` and `.claude/rules/markdown-content.md`
- Inspect `CLAUDE.md` (keep total length concise under 200 lines per existing convention) and `.claude/rules/markdown-content.md`.
- In `CLAUDE.md` under `Git & Security Guardrails`:
  - Explicitly document that any image committed before `.gitattributes` binary protection may retain a CRLF-corrupted Git blob in `HEAD` and must be re-staged via `git rm --cached <path> && git add <path>`.
  - Require verifying new or updated images in `src/assets/` with `python3 scripts/verify_assets.py` (or `file`) and running `npm run build` before `git push`.
  - Forbid manually renaming image extensions (e.g., `.webp` or `.png` renamed to `.jpg`) without true format re-encoding.
- In `.claude/rules/markdown-content.md`:
  - Add a dedicated section on Binary Asset Hygiene covering magic-byte verification, Windows-to-WSL copy safety (waiting for screenshot write completion and excluding `*:Zone.Identifier`), and exact 4-level relative asset paths (`../../../../assets/images/`).

### 2. Harden `.gitignore` and Verify `.gitattributes`
- Inspect `.gitignore` and ensure `*:Zone.Identifier` (Windows NTFS alternate data stream metadata created during Windows-to-WSL copies) is explicitly ignored.
- Inspect `.gitattributes` to confirm `binary` (`-text -diff`) attributes cover all binary extensions present under `src/assets/` (`*.png`, `*.jpg`, `*.jpeg`, `*.webp`, `*.gif`, `*.ico`, `*.svgz`, `*.pdf`, `*.zip`, `*.woff`, `*.woff2`, `*.ttf`, `*.eot`).

### 3. Create Automated Asset Integrity Script & Pre-Commit Hook
- Create `scripts/verify_assets.py` (Python 3 standard library only, zero external dependencies):
  - Scan all files under `src/assets/` (or specific file paths passed via CLI arguments).
  - Verify non-zero file size (> 0 bytes).
  - Validate magic-byte signatures against file extensions (`.png`, `.jpg`/`.jpeg`, `.webp`, `.gif`, `.pdf`).
  - Detect and flag any leftover `*:Zone.Identifier` metadata files.
  - When run inside a Git repository, verify staged blobs (`git show :<path>`) for modified/added files under `src/assets/` so CRLF-corrupted index blobs are caught before commit.
  - Exit with code 0 when clean, or exit with code 1 with clear diagnostics on failure.
- Create `.githooks/pre-commit` (executable `chmod +x`) that runs `python3 scripts/verify_assets.py --staged` whenever files under `src/assets/` are staged, and document `git config core.hooksPath .githooks` in `CLAUDE.md` so both Local Laptop and School PC share the hook.

### 4. Synchronize `architecture_map.md` and `system_state.md`
- Update `architecture_map.md` to include `scripts/verify_assets.py` and `.githooks/pre-commit` in the directory structure and module summary.
- Update `system_state.md` to log the completion of Requirement 4 (full `src/assets/` audit and GitHub Pages green build restoration) and Requirement 5 (preventive `CLAUDE.md` guardrails and automated binary asset verification).

### 5. Verification
- Run `python3 scripts/verify_assets.py` across the entire `src/assets/` directory and verify exit code 0.
- Run `npm run build` in WSL to confirm clean static site generation with exit code 0.


<!--
-->
