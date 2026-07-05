# 🧑‍🏫 IT Education Class Website Project Guidelines

## 📌 Project Overview
- **Framework:** Astro
- **Deployment/Hosting:** GitHub Pages
- **URL:** https://sungil-i.github.io
- **Purpose:** Providing class materials (Markdown) and announcements organized by year, semester, and subject for students.

## 📂 Main Directory Structure & Roles
- `src/pages/`: The core routing folder where Markdown (`.md`) based class materials are located, organized by year (2025, 2026), subject (e.g., Java1), and tests.
- `src/layouts/`: Page layout components (`ClassLayout.astro`, `MainLayout.astro`, `PostLayout.astro`).
- `src/components/`: Reusable UI components (`ThemeToggle.astro`, `YearSelector.astro`).
- `src/assets/`: Images (`.png`) and reference documents (`.pdf`) used in class materials.

## 🚀 Frequently Used Commands (Astro)
- Start development server: `npm run dev`
- Production build (for GitHub Pages): `npm run build`
- Preview build output: `npm run preview`

## 📝 Development & Maintenance Guidelines
1. **Markdown-Based Routing:** When adding new daily class materials, create them under the `src/pages/YYYY/MM-DD/daily/` directory.
2. **File Naming Convention:** Strictly follow the `MM-DD-subject_name.md` format combining date and topic. (e.g., `04-20-csharp_repeat.md`)
3. **Required Frontmatter:** When creating a Markdown file, you must specify the appropriate layout setting (e.g., `layout: ../../../layouts/PostLayout.astro`) and the class `title` at the very top.
4. **Response Tone & Manner:** When writing code or suggesting modifications, always structure the code clearly and easily for students to understand, adopting the perspective of an IT educator.