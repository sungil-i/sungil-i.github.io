<!--
/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md


## Tasks : Task file 의 'Requirement XX'

[Rule 8]에 따라 '요청사항' 을 만족하도록 Task file 의 Tasks 와 Claude REPL 을 위한 지시글을 생성해 줘. 지시글은 정확한 Task file 과 Target file 함께 올바른 상대 경로를 사용해라.

**요청사항**

## Current Directory (absolute path): `/home/upj53/classrooms/`
## Task file (relative path): `.tasks/2026-10-06-refactor_at_home.md`

## Environment:
* Current development environment : Local
* OS/SW: Ubuntu 20.04.6 LTS(bash) on Windows 11 Pro WSL

## 추가 지시: 토큰 절감을 위해 마크다운 파일 내부의 Task 지시글은 영문으로 작성해 주고, 내가 바로 Claude REPL 에 사용할 수 있게 Claude REPL용 지시글을 출력해 줘. 지시글을 출력할 때 상대경로를 틀리지 말고 적어라. 외부 CLI 호출이 아닌, REPL 환경 내부에서 직접 타겟팅하여 격리 연산을 수행하기 위한 최적의 형태로 지시글을 만들어라.

## Tasks 내용



-->


## Requirement 01

Target file: `src/layouts/MainLayout.astro`

Environment: Ubuntu 20.04.6 LTS(bash) on Windows 11 Pro WSL (Local)

Refactor `src/layouts/MainLayout.astro` to ensure full dark and light mode theme adaptability for the navigation table and footer elements.

### 1. Refactor Footer Theme Compatibility

* Locate the footer element in `src/layouts/MainLayout.astro`.
* Replace the hardcoded bg-light class with Bootstrap 5.3 theme-adaptive background bg-body-tertiary.
* Replace the legacy text-muted class with text-body-secondary to maintain proper text contrast across themes.
* Update border styling to border-secondary-subtle to prevent harsh border contrast in dark mode.

### 2. Refactor Navigation Table & Adaptive Button Styles

* Inspect `table class="table table-hover align-middle"` and its container inside `src/layouts/MainLayout.astro`.
* Ensure the table properly inherits theme variables (var(--bs-body-bg), var(--bs-body-color)) without lingering hardcoded white backgrounds.
* Define or update CSS rules for `.btn-theme-adaptive`:
* Ensure adaptive borders, backgrounds, and hover states using CSS variables or html[data-bs-theme="dark"] .btn-theme-adaptive.
* Alternatively, adopt standard Bootstrap adaptive classes (e.g., btn-outline-primary or btn-outline-secondary).
* Verify table headers (th) and data cells (td) maintain high readability and smooth hover states in both dark and light modes.

### 3. Verify Layout Build & Theme Integrity

* Run npm run build or Astro check to ensure no syntax errors or CSS scoping defects were introduced.
* Verify that toggling #theme-toggle smoothly switches colors for both the table and footer without CSS specificity conflicts or FOUC issues.


<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 01'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 02'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 03'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 04'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 05'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 06'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 07'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 08'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 09'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 10'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 11'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 12'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 13'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 14'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 15'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 16'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 17'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 18'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 19'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 20'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 21'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 22'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 23'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 24'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 25'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 26'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 27'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 28'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 29'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->







<!--
Read the task document at `/home/upj53/classrooms/.tasks/2026-10-06-refactor_at_home.md`. ONLY execute 'Requirement 30'. Do NOT execute or modify anything related to other requirements. Strictly adhere to the Role and Harness Constraints specified in `CLAUDE.md`.
-->






