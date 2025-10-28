---
summary: Learn how to organize and structure your documentation for larger projects.
tags: documentation, structure, organization
locale: en-us
---

# Building Documentation

As your documentation grows, proper organization becomes crucial. This guide covers best practices for structuring larger documentation projects.

## Documentation Architecture

### Directory Structure

Organize your content into logical sections:

```
src/
├── getting-started/
│   ├── intro.md
│   └── hello-world.md
├── building-apps/
│   ├── intro.md
│   └── advanced-features.md
├── reference/
│   ├── api.md
│   └── configuration.md
└── troubleshooting/
    └── common-issues.md
```

### Section Categories

Common documentation sections:

*   **Getting Started** - Introduction and quick start guides
*   **Tutorials** - Step-by-step learning paths
*   **How-To Guides** - Solutions to specific problems
*   **Reference** - Technical specifications and API docs
*   **Explanation** - Conceptual deep dives

## Table of Contents Management

### Hierarchical Structure

Use nested topics in `toc.yml`:

```yaml
# Main section
- href: getting-started/intro.md
  topics:
    # Subsections
    - href: getting-started/installation.md
    - href: getting-started/hello-world.md
    - href: getting-started/next-steps.md

# Another main section
- href: building-apps/intro.md
  topics:
    - href: building-apps/basics.md
    - href: building-apps/advanced.md
```

### Navigation Best Practices

*   Keep hierarchy shallow (max 3 levels)
*   Group related topics together
*   Use clear, descriptive names
*   Order from beginner to advanced

## Content Guidelines

### Writing Style

*   **Active voice** - "Click the button" not "The button should be clicked"
*   **Present tense** - "The system saves data" not "The system will save data"
*   **Second person** - "You can configure" not "One can configure"

### Page Structure

Each page should have:

1.  Clear title
2.  Brief introduction
3.  Prerequisites (if needed)
4.  Main content with subheadings
5.  Examples
6.  Next steps or related links

### Code Examples

Provide complete, working examples:

```python
# Good: Complete example
def calculate_total(items):
    """Calculate total price of items.
    
    Args:
        items: List of item prices
        
    Returns:
        Total sum of all items
    """
    return sum(items)

# Usage
prices = [10.99, 5.50, 3.25]
total = calculate_total(prices)
print(f"Total: ${total:.2f}")  # Output: Total: $18.74
```

## Frontmatter Standards

### Required Fields

Every page should include:

```yaml
---
summary: Brief description of the page (max 160 characters)
tags: keyword1, keyword2, keyword3
locale: en-us
---
```

### Optional Fields

You can add:

```yaml
---
summary: Page description
tags: keywords, here
locale: en-us
author: John Doe
date: 2025-01-15
category: tutorial
level: beginner
---
```

## Markdown Best Practices

### Headings

*   Use ATX-style headings (`#`)
*   One H1 per page
*   Don't skip heading levels
*   Use sentence case

```markdown
# Main Title (H1)

## Section (H2)

### Subsection (H3)

#### Detail (H4)
```

### Lists

*   Use `*` for unordered lists
*   Use `1.` for ordered lists
*   Indent with 4 spaces
*   Add blank lines before and after

### Links

*   Use relative paths for internal links
*   Use descriptive link text
*   Avoid "click here"

```markdown
Good: [Learn about configuration](../reference/configuration.md)
Bad: [Click here](../reference/configuration.md) for configuration
```

## Images and Media

### Image Guidelines

*   Store images in `src/images/` or section-specific folders
*   Use descriptive filenames
*   Optimize image size
*   Provide alt text

```markdown
![Description of the image](images/screenshot.png)
```

### Supported Formats

*   **Images**: PNG, JPG, GIF, SVG
*   **Code blocks**: Any language with syntax highlighting

## Version Control

### Commit Messages

Use clear, descriptive commit messages:

```
Good:
- Add authentication guide
- Update API reference for v2.0
- Fix typo in installation steps

Bad:
- Update
- Changes
- Fix
```

### Branching Strategy

*   `main` - Published documentation
*   `develop` - Work in progress
*   `feature/topic` - New content
*   `fix/issue` - Corrections

## Review Process

### Before Publishing

Check:

*   [ ] Spelling and grammar
*   [ ] Code examples work
*   [ ] Links are valid
*   [ ] Images load correctly
*   [ ] Frontmatter is complete
*   [ ] TOC is updated

### Peer Review

Have someone else review:

*   Technical accuracy
*   Clarity and readability
*   Completeness
*   Example quality

## Build Configuration

### config.yml Options

```yaml
build:
    title: My Documentation
    input-folder: src
    output-folder: build
    related-title: See Also
```

### Custom Styling

Modify `styles/main.css` to customize:

*   Colors and fonts
*   Layout and spacing
*   Code block styling
*   Responsive breakpoints

## Performance Optimization

### Build Performance

*   Keep individual files under 1000 lines
*   Optimize images before adding
*   Use efficient Markdown patterns

### Output Optimization

*   Minimize CSS and JavaScript
*   Compress images
*   Use relative paths

## Deployment

### Static Hosting

Deploy the `build/` folder to:

*   **GitHub Pages** - Free, version controlled
*   **Netlify** - Continuous deployment
*   **Vercel** - Fast, global CDN
*   **AWS S3** - Scalable, enterprise-ready

### Build Automation

Set up CI/CD to build automatically:

```yaml
# Example GitHub Actions workflow
name: Build Documentation

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: python build.py
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
```

## Maintenance

### Regular Tasks

*   Review and update content monthly
*   Check for broken links
*   Update dependencies
*   Archive outdated content

### Analytics

Track documentation usage:

*   Most viewed pages
*   Search queries
*   User feedback
*   Time on page

## Summary

Effective documentation requires:

*   Clear organization
*   Consistent formatting
*   Quality content
*   Regular maintenance
*   User feedback

By following these guidelines, you'll create documentation that users love! 📚
