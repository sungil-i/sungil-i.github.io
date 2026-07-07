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

## Requirement 05

Target file: `src/layouts/PostLayout.astro`
Reference file: `src/layouts/MainLayout.astro`

Environment: Claude REPL

Add a fixed 'TOP' (scroll-to-top) button to the bottom-right corner of the post layout, and append its specific styles inside the global `<style>` tag within the `<head>` of the main layout without modifying any existing styles.

### 1. Add an ID to the Table of Contents (TOC) in `src/layouts/PostLayout.astro`
- Locate the `<details class="toc-details mb-4 p-3 rounded border">` HTML structural element which renders the TOC (`📑 목차`).
- Add an `id="toc"` attribute to this `<details>` tag to enable smooth anchor navigation directly to the table of contents.

### 2. Append the 'TOP' Button Element to `src/layouts/PostLayout.astro`
- Add the functional scroll-to-top button inside the layout template. Ensure it navigates to the `#toc` anchor point.
- Refer to the user-provided Bootstrap template structure. Implement it cleanly as an anchor link to maintain native HTML scrolling to the TOC position:

```html
  <a href="#toc" class="btn btn-primary rounded-circle shadow-lg btn-scroll-top svelte-1teoznn" aria-label="최상단으로 이동">↑<br><span class="small" style="font-size: 0.7rem;">TOP</span></a>
```

* CONSTRAINT: Absolutely do NOT change, delete, or break any existing layout logic, markup, or conditional variables inside `src/layouts/PostLayout.astro`. Only append this functional block at an appropriate container boundary.

### 3. Safely Inject Button Styling into `src/layouts/MainLayout.astro`

* Open `src/layouts/MainLayout.astro` and find the global `<style>` tag located inside the `<head>` block.
* Append CSS rules for the `.btn-scroll-top` class to make it float permanently at the bottom-right of the viewport:

```css
.btn-scroll-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 1050;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  padding: 0;
  line-height: 1.2;
}
```

* CRITICAL CONSTRAINT: Do NOT delete, alter, or overwrite any other CSS classes, selectors, or configurations inside the `<style>` tag or the `<head>` element of `src/layouts/MainLayout.astro`. Keep all existing design completely intact.