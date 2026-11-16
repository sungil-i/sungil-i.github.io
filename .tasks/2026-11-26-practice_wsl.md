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
Read the task document at ``. ONLY execute 'Requirement 1' (1 ~ 3). Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
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



