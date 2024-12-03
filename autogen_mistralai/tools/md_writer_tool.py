from typing import List, Dict, Annotated
import json


class MarkdownHelper:
    """
    A helper class to generate README content with proper Markdown syntax.
    """

    @staticmethod
    def header(text: Annotated[str, "The header text"], level: Annotated[int, "The header level (1-6)"] = 1) -> Annotated[str, "A formatted header string"]:
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
    def paragraph(text: Annotated[str, "The paragraph text"]) -> Annotated[str, "A formatted paragraph string"]:
        """
        Generates a Markdown paragraph.
        
        :param text: The paragraph text.
        :return: A formatted paragraph string.
        """
        return f"{text}\n"
    
    @staticmethod
    def list(items: Annotated[List[str], "A list of items to include"], ordered: Annotated[bool, "True for ordered list, False for unordered"] = False) -> Annotated[str, "A formatted list string"]:
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
    def code_block(code: Annotated[str, "The code string"], language: Annotated[str, "The programming language for syntax highlighting"] = "") -> Annotated[str, "A formatted code block string"]:
        """
        Generates a Markdown code block.
        
        :param code: The code string.
        :param language: The programming language for syntax highlighting.
        :return: A formatted code block string.
        """
        return f"```{language}\n{code}\n```\n"
    
    @staticmethod
    def link(text: Annotated[str, "The link text"], url: Annotated[str, "The URL"]) -> Annotated[str, "A formatted link string"]:
        """
        Generates a Markdown link.
        
        :param text: The link text.
        :param url: The URL.
        :return: A formatted link string.
        """
        return f"[{text}]({url})"
      
    @staticmethod
    def image(alt_text: Annotated[str, "The alternative text for the image"], url: Annotated[str, "The URL of the image"]) -> Annotated[str, "A formatted image string"]:
        """
        Generates a Markdown image.
        
        :param alt_text: The alternative text for the image.
        :param url: The URL of the image.
        :return: A formatted image string.
        """
        return f"![{alt_text}]({url})\n"
    
    @staticmethod
    def table(headers: Annotated[List[str], "A list of header titles"], rows: Annotated[List[List[str]], "A list of lists representing rows"]) -> Annotated[str, "A formatted table string"]:
        """
        Generates a Markdown table.
        
        :param headers: A list of header titles.
        :param rows: A list of lists, where each sublist represents a row.
        :return: A formatted table string.
        """
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "| " + " | ".join("---" for _ in headers) + " |"
        rows_lines = "\n".join("| " + " | ".join(row) + " |" for row in rows)
        return f"{header_line}\n{separator_line}\n{rows_lines}\n\n"
    
    @staticmethod
    def blockquote(text: Annotated[str, "The blockquote text"]) -> Annotated[str, "A formatted blockquote string"]:
        """
        Generates a Markdown blockquote.
        
        :param text: The blockquote text.
        :return: A formatted blockquote string.
        """
        return f"> {text}\n"
    
    @staticmethod
    def horizontal_rule() -> Annotated[str, "A horizontal rule string"]:
        """
        Generates a Markdown horizontal rule.
        
        :return: A horizontal rule string.
        """
        return "---\n"

        


    def parse_package_json() -> Annotated[Dict[str, str], "Dictionary with extracted fields from a hardcoded package.json"] :
        """
        Parse a hardcoded package.json string to extract relevant fields.

        :return: A dictionary with extracted fields.
        """
        json_string = """{
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
    
        data = json.loads(json_string) 
        return {
            "name": data.get("name", "Unknown Project"),
            "version": data.get("version", "Unknown Version"),
            "description": data.get("description", "No description provided."),
            "scripts": data.get("scripts", {}),
            "author": data.get("author", "Unknown Author"),
            "license": data.get("license", "No license specified."),
            "repository": data.get("repository", {}),
            "bugs": data.get("bugs", {}),
            "homepage": data.get("homepage", ""),
            "keywords": data.get("keywords", []),
            "dependencies": data.get("dependencies", {}),
            "devDependencies": data.get("devDependencies", {}),
            "engines": data.get("engines", {}),
            "funding": data.get("funding", {})
        }
        
    def write_to_file(
    file_path: Annotated[str, "The path to the file where content will be written"], 
    content: Annotated[str, "The content to write to the file"], 
    mode: Annotated[str, "The file mode, e.g., 'w' for write, 'a' for append"] = 'a'
) -> Annotated[None, "This function does not return any value"]:
        """
        Writes content to a specified file.
        
        :param file_path: The path to the file where content will be written.
        :param content: The content to write to the file.
        :param mode: The file mode, e.g., 'w' for write, 'a' for append.
        :return: None
        """
        
        with open(file_path, mode) as file:
            file.write(content)