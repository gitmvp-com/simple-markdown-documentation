---
summary: Learn how to create your first documentation page with Simple Documentation.
tags: tutorial, getting started, hello world
locale: en-us
---

# Create Your First Documentation Page

This tutorial will guide you through creating your first documentation page from scratch.

## Prerequisites

Before you begin, make sure you have:

*   Completed the [Getting Started](intro.md) guide
*   Installed all dependencies
*   A text editor ready

## Step 1: Create a Markdown File

Create a new file in the `src/` directory. For this example, let's create `src/my-first-page.md`:

```markdown
---
summary: My very first documentation page
tags: tutorial, example
locale: en-us
---

# Hello, Documentation!

This is my first documentation page.

## Why Documentation Matters

Good documentation helps users:

*   Understand your project
*   Get started quickly
*   Find solutions to problems
*   Contribute effectively

## Example Code

Here's a simple Python example:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Documentation"))
```

## Next Steps

Explore more features of Simple Documentation!
```

## Step 2: Add Frontmatter

Notice the frontmatter at the top of the file:

```yaml
---
summary: My very first documentation page
tags: tutorial, example
locale: en-us
---
```

Frontmatter provides metadata about your page:

*   `summary` - Brief description for SEO and previews
*   `tags` - Keywords for categorization
*   `locale` - Language code

## Step 3: Write Content

Use standard Markdown syntax for your content:

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Lists

Unordered lists:

```markdown
*   Item 1
*   Item 2
*   Item 3
```

Ordered lists:

```markdown
1.  First item
1.  Second item
1.  Third item
```

### Links

```markdown
[Link text](url)
[Another page](intro.md)
```

### Code Blocks

Inline code: `` `code` ``

Code blocks:

````markdown
```python
def hello():
    print("Hello!")
```
````

### Tables

```markdown
| Column 1 | Column 2 |
| -------- | -------- |
| Data 1   | Data 2   |
| Data 3   | Data 4   |
```

Example:

| Feature | Supported |
| ------- | --------- |
| Markdown | ✅ Yes |
| HTML | ✅ Yes |
| LaTeX | ❌ No |

## Step 4: Add to Table of Contents

Edit `toc.yml` to include your new page:

```yaml
- href: getting-started/intro.md
  topics:
    - href: getting-started/hello-world.md
    - href: my-first-page.md  # Add this line
```

## Step 5: Build and Preview

Build the documentation:

```bash
python build.py
```

You should see output like:

```
🚀 Starting documentation build...

📄 Processing: src/getting-started/intro.md
📄 Processing: src/getting-started/hello-world.md
📄 Processing: src/my-first-page.md

📋 Creating index page...

✅ Build complete! Processed 3 files.
📂 Output directory: build/
🌐 Open build/index.html in your browser to view the documentation.
```

Open the generated HTML:

```bash
open build/my-first-page.html
```

## Tips for Great Documentation

### Be Clear and Concise

*   Use simple language
*   Break complex topics into smaller sections
*   Provide examples

### Use Visual Hierarchy

*   Use headings to organize content
*   Use lists for multiple items
*   Use code blocks for technical content

### Include Examples

*   Show, don't just tell
*   Use realistic examples
*   Explain what the code does

### Keep It Updated

*   Review documentation regularly
*   Update when features change
*   Remove outdated information

## Common Markdown Patterns

### Info Box (using blockquote)

> **Note:** This is an important piece of information that readers should pay attention to.

### Warning

> ⚠️ **Warning:** Be careful with this operation as it cannot be undone.

### Tip

> 💡 **Tip:** Here's a helpful suggestion to make your work easier.

## Troubleshooting

### Build Fails

If the build fails, check:

*   All `.md` files have valid frontmatter
*   No syntax errors in `toc.yml`
*   Python dependencies are installed

### Page Not Showing

If your page isn't appearing:

*   Verify it's listed in `toc.yml`
*   Check the file path is correct
*   Rebuild with `python build.py`

### Formatting Issues

If formatting looks wrong:

*   Check Markdown syntax
*   Ensure proper spacing around headers
*   Use 4 spaces for indentation

## Next Steps

Now that you've created your first page, you can:

*   Create more pages and organize them into sections
*   Customize the CSS in `styles/main.css`
*   Add images and other media
*   Deploy your documentation to the web

## Summary

You've learned how to:

*   ✅ Create a Markdown file with frontmatter
*   ✅ Write content using Markdown syntax
*   ✅ Add your page to the table of contents
*   ✅ Build and preview your documentation

Happy documenting! 📝
