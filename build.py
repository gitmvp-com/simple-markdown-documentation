#!/usr/bin/env python3
"""
Simple Markdown Documentation Builder

Converts Markdown files to HTML using Python Markdown with extensions.
Inspired by OutSystems docs-odc build system.
"""

import os
import yaml
import markdown
import frontmatter
from pathlib import Path


def load_config():
    """Load build configuration from config.yml"""
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)


def load_toc():
    """Load table of contents from toc.yml"""
    with open('toc.yml', 'r') as f:
        return yaml.safe_load(f)


def convert_markdown_to_html(md_content, metadata):
    """Convert Markdown content to HTML using extensions"""
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',      # Tables, definition lists, etc.
            'markdown.extensions.meta',       # Metadata support
            'markdown.extensions.toc',        # Table of contents
            'markdown.extensions.fenced_code', # Code blocks
            'markdown.extensions.codehilite',  # Syntax highlighting
        ],
        extension_configs={
            'markdown.extensions.toc': {
                'permalink': True,
                'toc_depth': 3,
            },
        }
    )
    
    html_content = md.convert(md_content)
    return html_content, md.toc


def create_html_page(title, content, toc, metadata):
    """Create a complete HTML page with styling"""
    summary = metadata.get('summary', '')
    tags = metadata.get('tags', '')
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{summary}">
    <meta name="keywords" content="{tags}">
    <title>{title} - Simple Documentation</title>
    <link rel="stylesheet" href="../styles/main.css">
</head>
<body>
    <div class="container">
        <nav class="sidebar">
            <h2>Documentation</h2>
            <div class="toc">
                {toc}
            </div>
        </nav>
        <main class="content">
            {content}
        </main>
    </div>
</body>
</html>
"""


def build_docs():
    """Main build function"""
    print("🚀 Starting documentation build...\n")
    
    # Load configuration
    config = load_config()
    build_config = config.get('build', {})
    input_folder = build_config.get('input-folder', 'src')
    output_folder = build_config.get('output-folder', 'build')
    
    # Create output directory
    Path(output_folder).mkdir(exist_ok=True)
    
    # Load TOC
    toc_data = load_toc()
    
    # Process all markdown files
    src_path = Path(input_folder)
    file_count = 0
    
    for md_file in src_path.rglob('*.md'):
        print(f"📄 Processing: {md_file}")
        
        # Read markdown file with frontmatter
        with open(md_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            md_content = post.content
            metadata = post.metadata
        
        # Convert to HTML
        html_content, toc = convert_markdown_to_html(md_content, metadata)
        
        # Extract title from first heading or use filename
        lines = md_content.split('\n')
        title = "Documentation"
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break
        
        # Create output path
        relative_path = md_file.relative_to(src_path)
        output_file = Path(output_folder) / relative_path.with_suffix('.html')
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Create complete HTML page
        full_html = create_html_page(title, html_content, toc, metadata)
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        file_count += 1
    
    # Create index page
    print("\n📋 Creating index page...")
    create_index_page(output_folder, toc_data)
    
    print(f"\n✅ Build complete! Processed {file_count} files.")
    print(f"📂 Output directory: {output_folder}/")
    print(f"🌐 Open build/index.html in your browser to view the documentation.\n")


def create_index_page(output_folder, toc_data):
    """Create an index.html page based on TOC"""
    toc_html = "<ul>"
    
    def process_toc_item(item):
        html = ""
        if isinstance(item, dict):
            href = item.get('href', '')
            topics = item.get('topics', [])
            
            if href:
                # Convert .md to .html
                html_href = href.replace('.md', '.html')
                title = href.split('/')[-1].replace('.md', '').replace('-', ' ').title()
                html += f'<li><a href="{html_href}">{title}</a>'
                
                if topics:
                    html += "<ul>"
                    for topic in topics:
                        html += process_toc_item(topic)
                    html += "</ul>"
                
                html += "</li>"
        
        return html
    
    for item in toc_data:
        toc_html += process_toc_item(item)
    
    toc_html += "</ul>"
    
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Documentation</title>
    <link rel="stylesheet" href="styles/main.css">
</head>
<body>
    <div class="container">
        <header class="hero">
            <h1>📚 Simple Documentation</h1>
            <p>A minimal Markdown-based documentation system</p>
        </header>
        <main class="content">
            <h2>Table of Contents</h2>
            {toc_html}
            
            <div class="info-box">
                <h3>About This Documentation</h3>
                <p>This is an MVP documentation site built with Python Markdown. It demonstrates:</p>
                <ul>
                    <li>Markdown to HTML conversion</li>
                    <li>Frontmatter metadata support</li>
                    <li>Table of contents generation</li>
                    <li>Simple navigation structure</li>
                </ul>
            </div>
        </main>
    </div>
</body>
</html>
"""
    
    with open(Path(output_folder) / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)


if __name__ == '__main__':
    build_docs()
