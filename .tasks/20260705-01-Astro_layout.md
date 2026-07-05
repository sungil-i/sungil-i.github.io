# Requirement 1

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