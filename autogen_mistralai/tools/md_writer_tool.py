from typing import Annotated

class MarkdownHelper:
    """
    A helper class to generate README content with proper Markdown syntax.
    """
    
    @staticmethod
    def header(text, level=1):
        """
        Generates a Markdown header.
        
        :param text: The header text.
        :param level: The header level (1-6).
        :return: A formatted header string.
        """
        if level < 1 or level > 6:
            raise ValueError("Header level must be between 1 and 6.")
        return f"{'#' * level} {text}\n"
    
    @staticmethod
    def paragraph(text):
        """
        Generates a Markdown paragraph.
        
        :param text: The paragraph text.
        :return: A formatted paragraph string.
        """
        return f"{text}\n"
    
    @staticmethod
    def list(items, ordered=False):
        """
        Generates a Markdown list.
        
        :param items: A list of items to include.
        :param ordered: True for an ordered list, False for unordered.
        :return: A formatted list string.
        """
        if ordered:
            return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items)) + "\n"
        else:
            return "\n".join(f"- {item}" for item in items) + "\n"
    
    @staticmethod
    def code_block(code, language=""):
        """
        Generates a Markdown code block.
        
        :param code: The code string.
        :param language: The programming language for syntax highlighting.
        :return: A formatted code block string.
        """
        return f"```{language}\n{code}\n```\n"
    
    @staticmethod
    def link(text, url):
        """
        Generates a Markdown link.
        
        :param text: The link text.
        :param url: The URL.
        :return: A formatted link string.
        """
        return f"[{text}]({url})"
      
    @staticmethod
    def image(alt_text, url):
        """
        Generates a Markdown image.
        
        :param alt_text: The alternative text for the image.
        :param url: The URL of the image.
        :return: A formatted image string.
        """
        return f"![{alt_text}]({url})\n"
    
    @staticmethod
    def table(headers, rows):
        """
        Generates a Markdown table.
        
        :param headers: A list of header titles.
        :param rows: A list of lists, where each sublist represents a row.
        :return: A formatted table string.
        """
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "| " + " | ".join("---" for _ in headers) + " |"
        rows_lines = "\n".join("| " + " | ".join(row) + " |" for row in rows)
        return f"{header_line}\n{separator_line}\n{rows_lines}\n"
    
    @staticmethod
    def blockquote(text):
        """
        Generates a Markdown blockquote.
        
        :param text: The blockquote text.
        :return: A formatted blockquote string.
        """
        return f"> {text}\n"
    
    @staticmethod
    def horizontal_rule():
        """
        Generates a Markdown horizontal rule.
        
        :return: A horizontal rule string.
        """
        return "---\n"
    
    @staticmethod
    def annotation_wrapper() -> Annotated[str, "A json string for a package.json file from a project"]:
        """
        Wraps a string with an annotation.
        
        :return: project1 wrapped in an annotation.
        """
        return """{
    "name": "awesome-project",
    "version": "1.0.0",
    "description": "A mock package.json file for generating a README.md using an LLM.",
    "main": "index.js",
    "scripts": {
        "start": "node index.js",
        "test": "jest",
        "build": "webpack --mode production",
        "lint": "eslint .",
        "format": "prettier --write ."
    },
    "keywords": ["markdown", "readme", "generator", "example"],
    "author": "Jane Doe <jane.doe@example.com>",
    "license": "MIT",
    "repository": {
        "type": "git",
        "url": "https://github.com/janedoe/awesome-project.git"
    },
    "bugs": {
        "url": "https://github.com/janedoe/awesome-project/issues"
    },
    "homepage": "https://github.com/janedoe/awesome-project#readme",
    "dependencies": {
        "express": "^4.18.2",
        "cors": "^2.8.5"
    },
    "devDependencies": {
        "jest": "^29.6.2",
        "webpack": "^5.88.2",
        "eslint": "^8.47.0",
        "prettier": "^3.0.3"
    },
    "engines": {
        "node": ">=14.0.0",
        "npm": ">=6.0.0"
    },
    "funding": {
        "type": "individual",
        "url": "https://github.com/sponsors/janedoe"
    }
    }"""