---
summary: Get started with Simple Documentation - learn how to write, build, and publish your Markdown-based documentation.
tags: getting started, documentation, markdown
locale: en-us
---

# Getting Started

Welcome to **Simple Documentation** - a minimal viable product (MVP) for creating beautiful documentation from Markdown files.

## What is Simple Documentation?

Simple Documentation is a lightweight, Python-based documentation system that converts Markdown files into clean, accessible HTML pages. It's inspired by enterprise documentation systems but focuses on simplicity and ease of use.

## Key Features

*   **Markdown-based** - Write your documentation in plain Markdown
*   **Python Markdown converter** - Uses Python Markdown with popular extensions
*   **Frontmatter support** - Add metadata to your pages with YAML frontmatter
*   **Table of Contents** - Automatically generate navigation from your TOC configuration
*   **Clean HTML output** - Beautiful, responsive design out of the box
*   **No database required** - All content is file-based

## Quick Start

### Prerequisites

Before you begin, make sure you have:

*   Python 3.8 or higher installed
*   pip package manager
*   A text editor (VS Code, Sublime Text, etc.)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/gitmvp-com/simple-markdown-documentation.git
    cd simple-markdown-documentation
    ```

2.  Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Build the documentation:

    ```bash
    python build.py
    ```

4.  Open the generated documentation in your browser:

    ```bash
    open build/index.html
    ```

## Project Structure

Here's how the project is organized:

```
simple-markdown-documentation/
├── src/                    # Your Markdown source files
│   ├── getting-started/
│   └── building-apps/
├── build/                  # Generated HTML output
├── styles/                 # CSS stylesheets
├── build.py               # Build script
├── requirements.txt       # Python dependencies
├── toc.yml               # Table of contents
└── config.yml            # Configuration
```

## How It Works

1.  **Write** your documentation in Markdown files inside the `src/` directory
2.  **Configure** the table of contents in `toc.yml`
3.  **Build** by running `python build.py`
4.  **Deploy** the `build/` folder to any static web host

## Next Steps

Now that you have Simple Documentation set up, check out:

*   [Create your first documentation page](hello-world.md)
*   [Learn about Markdown extensions](#markdown-extensions)
*   [Configure your documentation](#configuration)

## Markdown Extensions

Simple Documentation uses Python Markdown with several extensions:

### Extra

Adds support for:

*   Definition lists
*   Tables
*   Fenced code blocks
*   Footnotes

### Meta

Read metadata from frontmatter:

```markdown
---
summary: Page description
tags: tag1, tag2
---
```

### TOC

Automatic table of contents generation with permalinks.

### CodeHilite

Syntax highlighting for code blocks.

## Configuration

### config.yml

Configure build settings:

```yaml
build:
    title: Simple Documentation
    input-folder: src
    output-folder: build
```

### toc.yml

Define your documentation structure:

```yaml
- href: getting-started/intro.md
  topics:
    - href: getting-started/hello-world.md
```

## Editor Setup

For the best experience, configure your editor:

*   **4 spaces** for indentation (not tabs)
*   **Soft wrapping** enabled
*   **UTF-8** encoding

The included `.editorconfig` file will configure most modern editors automatically.

## Support

This is an MVP project created as a learning example. Feel free to:

*   Fork the repository
*   Submit issues
*   Contribute improvements
*   Use it as a starting point for your own documentation
