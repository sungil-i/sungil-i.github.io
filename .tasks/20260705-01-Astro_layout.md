## Requirement 1

Target file: `./src/components/YearSelector.astro`

Please refactor the component based on the following requirements:

1. **Discover Subfolders Dynamically:**
   Instead of just listing hardcoded years (e.g., 2025, 2026), dynamically search and retrieve the subfolders (class folders like `2-10`, `3-10`, `Java1`) located under `src/pages/2025` and `src/pages/2026`. (You can use `fs` module or `import.meta.glob` to read the directory structure).

2. **Update `<select>` Options:**
   Update the `<option>` tags inside the `<select>` element to display not only the years but also the specific class folders. The option values should be the full path (e.g., `/2026/Java1/`), and the display text should be formatted nicely (e.g., `2026 - Java1`).

3. **Change Trigger Mechanism (Add a Button):**
   Currently, page navigation is triggered automatically via the `addEventListener('change')` event on the `<select>` tag. This is inconvenient. 
   - Remove the `change` event listener.
   - Add a "Move" (or "이동") `<button>` next to the `<select>` tag.
   - Add a `click` event listener to this new button so that navigation (`window.location.href`) only occurs when the user explicitly clicks the button with the selected option value.
   
## Requirement 2

Target file: `./src/components/YearSelector.astro`

Please refactor the component based on the following requirements:

Fix the issue where the button `#class-move-btn` becomes too small and triggers an accidental text wrap.
- Change the button text from "이동" to "Go" for a more concise and intuitive call-to-action.
- Prevent layout breaking or unexpected wrapping by ensuring proper width (e.g., adding explicit minimal width, layout adjustments, or utilizing Bootstrap utility classes like `text-nowrap` if necessary).
- Ensure the button styling remains perfectly visible and aesthetically cohesive across both Dark Mode and Light Mode states.
- Maintain the original `id="class-move-btn"` attribute for JavaScript event listener compatibility.

## Requirement 3

Target file: `./src/layouts/PostLayout.astro`

Please refactor the component based on the following requirements:

Optimize layout container constraints and implement an internal self-contained Table of Contents (TOC) in `./src/layouts/PostLayout.astro`.
- Expand the main wrapper container width by modifying `<div class="container-fluid max-w-7xl py-5">` to support a wider content footprint (e.g., replace `max-w-7xl` with `max-w-none`, `max-w-full`, or an expanded constraint utility).
- Insert a native, collapsible `<details>` element rendering a Table of Contents (`📑 목차`) located sequentially between `📅 작성일: {frontmatter.date}` and the content `<slot />`.
- Parse headings dynamically from `Astro.props` or context within the script section, extracting levels from `H2` through `H4` exclusively.
- Do not import external packages or independent components for the TOC; implement all rendering logic seamlessly inside the target layout file.

## Requirement 4

Target file: `./src/layouts/PostLayout.astro`

Please refactor the component based on the following requirements:

1. Modify the Bootstrap grid utility classes to adjust the content width based on responsive breakpoints.
2. The layout must fill approximately 80% of the screen width on a standard 1920x1080 desktop resolution.
3. The layout must fill 100% of the screen width (full width) on mobile displays and screens around 900px wide.
4. Locate the following code block:
```html
<div class="container-fluid max-w-none py-5">
  <div class="row justify-content-center">
    <div class="col-12 col-lg-10 col-xl-10">
      <div class="mb-4">
```

5. Refactor the column classes (`col-...`):
* Remove `col-lg-10` so that it remains `col-12` (100% width) on screens around 900px (which falls under the `lg` breakpoint threshold of 992px).
* Use `col-xl-10` or `col-xxl-10` (10/12 columns = 83.3%, which perfectly achieves the visual ~80% width fill on a 1920x1080 screen).
* Ensure the final class attribute looks like `class="col-12 col-xl-10"` or incorporates `col-xxl-10` depending on the Bootstrap version used, ensuring 100% width at 900px and ~80% width at 1920px.


6. Maintain exact HTML structure, nesting, and formatting rules.
