# Simple Markdown Documentation

A minimal viable product (MVP) documentation site inspired by OutSystems docs-odc. This project provides a simple Markdown-based documentation system with Python Markdown conversion.

## Features

- ✅ Markdown-based documentation with frontmatter metadata
- ✅ Python Markdown converter with extensions
- ✅ Table of Contents (TOC) configuration
- ✅ Markdown linting configuration
- ✅ EditorConfig for consistent formatting
- ✅ Simple HTML output generation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/gitmvp-com/simple-markdown-documentation.git
cd simple-markdown-documentation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Build Documentation

Convert all Markdown files to HTML:

```bash
python build.py
```

This will:
- Read all `.md` files from the `src/` directory
- Convert them to HTML using Python Markdown
- Generate output in the `build/` directory
- Create an index page based on `toc.yml`

#### Preview Documentation

After building, you can preview the documentation by opening the generated HTML files in your browser:

```bash
# On macOS
open build/index.html

# On Linux
xdg-open build/index.html

# On Windows
start build/index.html
```

## Project Structure

```
simple-markdown-documentation/
├── src/                    # Source Markdown files
│   ├── getting-started/
│   │   ├── intro.md
│   │   └── hello-world.md
│   └── building-apps/
│       └── intro.md
├── build/                  # Generated HTML output
├── styles/                 # CSS stylesheets
│   └── main.css
├── build.py               # Python build script
├── requirements.txt       # Python dependencies
├── toc.yml               # Table of contents configuration
├── config.yml            # Build configuration
├── .markdownlint.json    # Markdown linting rules
├── .editorconfig         # Editor configuration
└── README.md             # This file
```

## Writing Documentation

All documentation should be written in Markdown (check [here](https://daringfireball.net/projects/markdown/syntax) for the basic syntax).

### Markdown Extensions

The following Markdown extensions are available:

- **markdown.extensions.extra** - Meta-extension adding support for definition lists, tables, etc.
- **markdown.extensions.meta** - Read metadata from frontmatter
- **markdown.extensions.toc** - Automatic bookmarks in headings
- **markdown.extensions.fenced_code** - Code blocks with syntax highlighting

### Frontmatter

Each Markdown file should include frontmatter metadata:

```markdown
---
summary: Brief description of the page
tags: tag1, tag2, tag3
locale: en-us
---

# Page Title

Content goes here...
```

## Editor Configuration

Before editing any Markdown document, configure your editor with:

- When tab is pressed, insert **4 spaces** instead of a Tab character
- Use soft-wrapping to avoid carriage returns inside paragraphs

The `.editorconfig` file will configure most editors automatically.

## Markdown Linting

This project uses markdownlint for consistent Markdown formatting. The rules are defined in `.markdownlint.json`.

Key rules:
- Use ATX-style headings (`#` instead of underlines)
- Use asterisk (`*`) for unordered lists
- Indent lists with 4 spaces
- Use backticks for code fences

## Configuration

### toc.yml

Defines the documentation structure and navigation:

```yaml
- href: getting-started/intro.md
  topics:
    - href: getting-started/hello-world.md
```

### config.yml

Build configuration:

```yaml
build:
  title: Simple Documentation
  input-folder: src
  output-folder: build
```

## License

MIT License - Feel free to use this project as a starting point for your own documentation.

## Acknowledgments

Inspired by [OutSystems docs-odc](https://github.com/OutSystems/docs-odc) repository.
