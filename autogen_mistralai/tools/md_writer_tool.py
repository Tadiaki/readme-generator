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

        


    def provide_package_json_string() -> Annotated[str, "string from a hardcoded package.json"] :
        """
        Returns the annotated package.json content as a string.

        """
        return  """{
  "name": "taskpro-manager",
  "version": "2.3.1",
  "description": "TaskPro Manager is a robust task management and productivity app with real-time collaboration and cloud sync.",
  "main": "dist/server.js",
  "scripts": {
    "start": "node dist/server.js",
    "dev": "nodemon src/server.js",
    "test": "jest --verbose --coverage",
    "build": "webpack --config webpack.config.js --mode production",
    "clean": "rimraf dist && rimraf build",
    "lint": "eslint . --ext .js,.jsx,.ts,.tsx",
    "format": "prettier --write \"src/**/*.{js,jsx,ts,tsx}\"",
    "serve": "http-server dist -p 8080",
    "prepare": "husky install",
    "precommit": "lint-staged",
    "analyze": "webpack-bundle-analyzer build/stats.json"
  },
  "keywords": [
    "task management",
    "productivity",
    "collaboration",
    "cloud sync",
    "web app"
  ],
  "author": {
    "name": "Sophie Martinez",
    "email": "sophie@taskpro.com",
    "url": "https://www.taskpro.com/team/sophie"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/taskpro-inc/taskpro-manager.git"
  },
  "bugs": {
    "url": "https://github.com/taskpro-inc/taskpro-manager/issues",
    "email": "support@taskpro.com"
  },
  "homepage": "https://www.taskpro.com",
  "dependencies": {
    "express": "^4.18.2",
    "dotenv": "^16.0.3",
    "mongoose": "^7.5.0",
    "socket.io": "^4.7.2",
    "jsonwebtoken": "^9.1.1",
    "bcrypt": "^5.1.0",
    "cors": "^2.8.5",
    "uuid": "^9.0.0",
    "dayjs": "^1.11.9"
  },
  "devDependencies": {
    "jest": "^29.6.2",
    "webpack": "^5.88.2",
    "webpack-cli": "^5.1.1",
    "eslint": "^8.47.0",
    "eslint-plugin-react": "^7.32.2",
    "prettier": "^3.0.3",
    "nodemon": "^3.0.1",
    "http-server": "^14.1.1",
    "husky": "^8.0.3",
    "lint-staged": "^13.3.0",
    "rimraf": "^5.0.0",
    "sass": "^1.66.1",
    "typescript": "^5.4.2",
    "webpack-bundle-analyzer": "^4.9.0"
  },
  "peerDependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "optionalDependencies": {
    "fsevents": "^2.4.2"
  },
  "engines": {
    "node": ">=16.0.0",
    "npm": ">=8.0.0"
  },
  "funding": {
    "type": "corporate",
    "url": "https://www.taskpro.com/support-us"
  },
  "config": {
    "port": 8080,
    "env": "production"
  },
  "private": false,
  "os": ["linux", "darwin", "win32"],
  "cpu": ["x64", "arm64"],
  "bin": {
    "taskpro-cli": "./bin/taskpro-cli.js"
  },
  "workspaces": ["packages/api", "packages/frontend", "packages/shared"],
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    },
    "./utils": {
      "import": "./dist/utils.mjs",
      "require": "./dist/utils.cjs"
    }
  },
  "types": "./dist/index.d.ts",
  "files": ["dist", "src", "bin", "README.md"],
  "readme": "README.md"
}
"""  
    

        
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