from typing import List, Dict, Annotated, Union
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

        


    def parse_package_json() -> Annotated[Union[Dict[str, str], str], "Dictionary with extracted fields or the original JSON string if an error occurs"]:
        """
        Parse a hardcoded package.json string to extract relevant fields.

        If parsing fails due to any exception, the original JSON string is returned.

        :return: A dictionary with extracted fields, or the original JSON string if an error occurs.
        """
        json_string = """{
  "name": "code-oss-dev",
  "version": "1.96.0",
  "distro": "259941ab128814d2a40a076eecd74b25d4a37a5b",
  "author": {
    "name": "Microsoft Corporation"
  },
  "license": "MIT",
  "main": "./out/main.js",
  "type": "module",
  "private": true,
  "scripts": {
    "test": "echo Please run any of the test scripts from the scripts folder.",
    "test-browser": "npx playwright install && node test/unit/browser/index.js",
    "test-browser-no-install": "node test/unit/browser/index.js",
    "test-node": "mocha test/unit/node/index.js --delay --ui=tdd --timeout=5000 --exit",
    "test-extension": "vscode-test",
    "preinstall": "node build/npm/preinstall.js",
    "postinstall": "node build/npm/postinstall.js",
    "compile": "node ./node_modules/gulp/bin/gulp.js compile",
    "watch": "npm-run-all -lp watch-client watch-extensions",
    "watchd": "deemon npm run watch",
    "watch-webd": "deemon npm run watch-web",
    "kill-watchd": "deemon --kill npm run watch",
    "kill-watch-webd": "deemon --kill npm run watch-web",
    "restart-watchd": "deemon --restart npm run watch",
    "restart-watch-webd": "deemon --restart npm run watch-web",
    "watch-client": "node --max-old-space-size=8192 ./node_modules/gulp/bin/gulp.js watch-client",
    "watch-clientd": "deemon npm run watch-client",
    "kill-watch-clientd": "deemon --kill npm run watch-client",
    "watch-extensions": "node --max-old-space-size=8192 ./node_modules/gulp/bin/gulp.js watch-extensions watch-extension-media",
    "watch-extensionsd": "deemon npm run watch-extensions",
    "kill-watch-extensionsd": "deemon --kill npm run watch-extensions",
    "precommit": "node build/hygiene.js",
    "gulp": "node --max-old-space-size=8192 ./node_modules/gulp/bin/gulp.js",
    "electron": "node build/lib/electron",
    "7z": "7z",
    "update-grammars": "node build/npm/update-all-grammars.mjs",
    "update-localization-extension": "node build/npm/update-localization-extension.js",
    "smoketest": "node build/lib/preLaunch.js && cd test/smoke && npm run compile && node test/index.js",
    "smoketest-no-compile": "cd test/smoke && node test/index.js",
    "download-builtin-extensions": "node build/lib/builtInExtensions.js",
    "download-builtin-extensions-cg": "node build/lib/builtInExtensionsCG.js",
    "monaco-compile-check": "tsc -p src/tsconfig.monaco.json --noEmit",
    "tsec-compile-check": "node node_modules/tsec/bin/tsec -p src/tsconfig.tsec.json",
    "vscode-dts-compile-check": "tsc -p src/tsconfig.vscode-dts.json && tsc -p src/tsconfig.vscode-proposed-dts.json",
    "valid-layers-check": "node build/lib/layersChecker.js",
    "update-distro": "node build/npm/update-distro.mjs",
    "web": "echo 'npm run web' is replaced by './scripts/code-server' or './scripts/code-web'",
    "compile-cli": "gulp compile-cli",
    "compile-web": "node ./node_modules/gulp/bin/gulp.js compile-web",
    "watch-web": "node ./node_modules/gulp/bin/gulp.js watch-web",
    "watch-cli": "node ./node_modules/gulp/bin/gulp.js watch-cli",
    "eslint": "node build/eslint",
    "stylelint": "node build/stylelint",
    "playwright-install": "npm exec playwright install",
    "compile-build": "node ./node_modules/gulp/bin/gulp.js compile-build",
    "compile-extensions-build": "node ./node_modules/gulp/bin/gulp.js compile-extensions-build",
    "minify-vscode": "node ./node_modules/gulp/bin/gulp.js minify-vscode",
    "minify-vscode-reh": "node ./node_modules/gulp/bin/gulp.js minify-vscode-reh",
    "minify-vscode-reh-web": "node ./node_modules/gulp/bin/gulp.js minify-vscode-reh-web",
    "hygiene": "node ./node_modules/gulp/bin/gulp.js hygiene",
    "core-ci": "node ./node_modules/gulp/bin/gulp.js core-ci",
    "core-ci-pr": "node ./node_modules/gulp/bin/gulp.js core-ci-pr",
    "extensions-ci": "node ./node_modules/gulp/bin/gulp.js extensions-ci",
    "extensions-ci-pr": "node ./node_modules/gulp/bin/gulp.js extensions-ci-pr",
    "perf": "node scripts/code-perf.js",
    "update-build-ts-version": "npm install typescript@next && tsc -p ./build/tsconfig.build.json"
  },
  "dependencies": {
    "@microsoft/1ds-core-js": "^3.2.13",
    "@microsoft/1ds-post-js": "^3.2.13",
    "@parcel/watcher": "2.1.0",
    "@types/semver": "^7.5.8",
    "@vscode/deviceid": "^0.1.1",
    "@vscode/iconv-lite-umd": "0.7.0",
    "@vscode/policy-watcher": "^1.1.8",
    "@vscode/proxy-agent": "^0.26.0",
    "@vscode/ripgrep": "^1.15.9",
    "@vscode/spdlog": "^0.15.0",
    "@vscode/sqlite3": "5.1.8-vscode",
    "@vscode/sudo-prompt": "9.3.1",
    "@vscode/tree-sitter-wasm": "^0.0.4",
    "@vscode/vscode-languagedetection": "1.0.21",
    "@vscode/windows-mutex": "^0.5.0",
    "@vscode/windows-process-tree": "^0.6.0",
    "@vscode/windows-registry": "^1.1.0",
    "@xterm/addon-clipboard": "^0.2.0-beta.53",
    "@xterm/addon-image": "^0.9.0-beta.70",
    "@xterm/addon-ligatures": "^0.10.0-beta.70",
    "@xterm/addon-search": "^0.16.0-beta.70",
    "@xterm/addon-serialize": "^0.14.0-beta.70",
    "@xterm/addon-unicode11": "^0.9.0-beta.70",
    "@xterm/addon-webgl": "^0.19.0-beta.70",
    "@xterm/headless": "^5.6.0-beta.70",
    "@xterm/xterm": "^5.6.0-beta.70",
    "http-proxy-agent": "^7.0.0",
    "https-proxy-agent": "^7.0.2",
    "jschardet": "3.1.4",
    "kerberos": "2.1.1",
    "minimist": "^1.2.6",
    "native-is-elevated": "0.7.0",
    "native-keymap": "^3.3.5",
    "native-watchdog": "^1.4.1",
    "node-pty": "^1.1.0-beta22",
    "open": "^8.4.2",
    "tas-client-umd": "0.2.0",
    "v8-inspect-profiler": "^0.1.1",
    "vscode-oniguruma": "1.7.0",
    "vscode-regexpp": "^3.1.0",
    "vscode-textmate": "9.1.0",
    "yauzl": "^3.0.0",
    "yazl": "^2.4.3"
  },
  "devDependencies": {
    "@playwright/test": "^1.46.1",
    "@stylistic/eslint-plugin-ts": "^2.8.0",
    "@types/cookie": "^0.3.3",
    "@types/debug": "^4.1.5",
    "@types/eslint": "^9.6.1",
    "@types/gulp-svgmin": "^1.2.1",
    "@types/http-proxy-agent": "^2.0.1",
    "@types/kerberos": "^1.1.2",
    "@types/minimist": "^1.2.1",
    "@types/mocha": "^9.1.1",
    "@types/node": "20.x",
    "@types/sinon": "^10.0.2",
    "@types/sinon-test": "^2.4.2",
    "@types/trusted-types": "^1.0.6",
    "@types/vscode-notebook-renderer": "^1.72.0",
    "@types/webpack": "^5.28.5",
    "@types/wicg-file-system-access": "^2020.9.6",
    "@types/windows-foreground-love": "^0.3.0",
    "@types/winreg": "^1.2.30",
    "@types/yauzl": "^2.10.0",
    "@types/yazl": "^2.4.2",
    "@typescript-eslint/utils": "^8.8.0",
    "@vscode/gulp-electron": "^1.36.0",
    "@vscode/l10n-dev": "0.0.35",
    "@vscode/telemetry-extractor": "^1.10.2",
    "@vscode/test-cli": "^0.0.6",
    "@vscode/test-electron": "^2.4.0",
    "@vscode/test-web": "^0.0.62",
    "@vscode/v8-heap-parser": "^0.1.0",
    "@vscode/vscode-perf": "^0.0.19",
    "@webgpu/types": "^0.1.44",
    "ansi-colors": "^3.2.3",
    "asar": "^3.0.3",
    "chromium-pickle-js": "^0.2.0",
    "cookie": "^0.7.2",
    "copy-webpack-plugin": "^11.0.0",
    "css-loader": "^6.9.1",
    "cssnano": "^6.0.3",
    "debounce": "^1.0.0",
    "deemon": "^1.8.0",
    "electron": "32.2.6",
    "eslint": "^9.11.1",
    "eslint-formatter-compact": "^8.40.0",
    "eslint-plugin-header": "3.1.1",
    "eslint-plugin-jsdoc": "^50.3.1",
    "eslint-plugin-local": "^6.0.0",
    "event-stream": "3.3.4",
    "fancy-log": "^1.3.3",
    "file-loader": "^6.2.0",
    "glob": "^5.0.13",
    "gulp": "^4.0.0",
    "gulp-azure-storage": "^0.12.1",
    "gulp-bom": "^3.0.0",
    "gulp-buffer": "0.0.2",
    "gulp-filter": "^5.1.0",
    "gulp-flatmap": "^1.0.2",
    "gulp-gunzip": "^1.0.0",
    "gulp-gzip": "^1.4.2",
    "gulp-json-editor": "^2.5.0",
    "gulp-plumber": "^1.2.0",
    "gulp-rename": "^1.2.0",
    "gulp-replace": "^0.5.4",
    "gulp-sourcemaps": "^3.0.0",
    "gulp-svgmin": "^4.1.0",
    "gulp-untar": "^0.0.7",
    "husky": "^0.13.1",
    "innosetup": "6.0.5",
    "istanbul-lib-coverage": "^3.2.0",
    "istanbul-lib-instrument": "^6.0.1",
    "istanbul-lib-report": "^3.0.0",
    "istanbul-lib-source-maps": "^4.0.1",
    "istanbul-reports": "^3.1.5",
    "lazy.js": "^0.4.2",
    "merge-options": "^1.0.1",
    "mime": "^1.4.1",
    "minimatch": "^3.0.4",
    "minimist": "^1.2.6",
    "mocha": "^10.2.0",
    "mocha-junit-reporter": "^2.2.1",
    "mocha-multi-reporters": "^1.5.1",
    "npm-run-all": "^4.1.5",
    "os-browserify": "^0.3.0",
    "p-all": "^1.0.0",
    "path-browserify": "^1.0.1",
    "postcss": "^8.4.33",
    "postcss-nesting": "^12.0.2",
    "pump": "^1.0.1",
    "rcedit": "^1.1.0",
    "rimraf": "^2.2.8",
    "sinon": "^12.0.1",
    "sinon-test": "^3.1.3",
    "source-map": "0.6.1",
    "source-map-support": "^0.3.2",
    "style-loader": "^3.3.2",
    "ts-loader": "^9.5.1",
    "ts-node": "^10.9.1",
    "tsec": "0.2.7",
    "tslib": "^2.6.3",
    "typescript": "^5.8.0-dev.20241202",
    "typescript-eslint": "^8.8.0",
    "util": "^0.12.4",
    "webpack": "^5.94.0",
    "webpack-cli": "^5.1.4",
    "webpack-stream": "^7.0.0",
    "xml2js": "^0.5.0",
    "yaserver": "^0.4.0"
  },
  "overrides": {
    "node-gyp-build": "4.8.1",
    "kerberos@2.1.1": {
      "node-addon-api": "7.1.0"
    },
    "@parcel/watcher@2.1.0": {
      "node-addon-api": "7.1.0"
    }
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/microsoft/vscode.git"
  },
  "bugs": {
    "url": "https://github.com/microsoft/vscode/issues"
  },
  "optionalDependencies": {
    "windows-foreground-love": "0.5.0"
  }
}"""

        try:
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
        except Exception as e:
            print(f"Error occurred: {e}")
            return json_string
        
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