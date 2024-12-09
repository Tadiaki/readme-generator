code-oss-dev

No description provided.

## Getting Started

To get started with the project, follow these steps:

- Clone the repository: git clone https://github.com/microsoft/vscode.git
- Navigate to the project directory: cd vscode
- Install the dependencies: npm install
- Start the development server: npm run web

## Scripts

The project includes several scripts to facilitate development and testing. Here are some of the key scripts:

- test: Runs a test script.
- test-browser: Runs a browser test script.
- test-node: Runs a node test script.
- test-extension: Runs an extension test script.
- preinstall: Runs a script before installation.
- postinstall: Runs a script after installation.
- compile: Compiles the project.
- watch: Watches for changes and recompiles as needed.
- watch-web: Watches for changes in the web client and recompiles as needed.
- watch-extensions: Watches for changes in the extensions and recompiles as needed.

## Dependencies

| Package | Version |
|---------|---------|
| @microsoft/1ds-core-js | ^3.2.13 |
| @microsoft/1ds-post-js | ^3.2.13 |
| @parcel/watcher | 2.1.0 |
| @types/semver | ^7.5.8 |
| @vscode/deviceid | ^0.1.1 |
| @vscode/iconv-lite-umd | 0.7.0 |
| @vscode/policy-watcher | ^1.1.8 |
| @vscode/proxy-agent | ^0.26.0 |
| @vscode/ripgrep | ^1.15.9 |
| @vscode/spdlog | ^0.15.0 |
| @vscode/sqlite3 | 5.1.8-vscode |
| @vscode/sudo-prompt | 9.3.1 |
| @vscode/tree-sitter-wasm | ^0.0.4 |
| @vscode/vscode-languagedetection | 1.0.21 |
| @vscode/windows-mutex | ^0.5.0 |
| @vscode/windows-process-tree | ^0.6.0 |
| @vscode/windows-registry | ^1.1.0 |
| @xterm/addon-clipboard | ^0.2.0-beta.53 |
| @xterm/addon-image | ^0.9.0-beta.70 |
| @xterm/addon-ligatures | ^0.10.0-beta.70 |
| @xterm/addon-search | ^0.16.0-beta.70 |
| @xterm/addon-serialize | ^0.14.0-beta.70 |
| @xterm/addon-unicode11 | ^0.9.0-beta.70 |
| @xterm/addon-webgl | ^0.19.0-beta.70 |
| @xterm/headless | ^5.6.0-beta.70 |
| @xterm/xterm | ^5.6.0-beta.70 |
| http-proxy-agent | ^7.0.0 |
| https-proxy-agent | ^7.0.2 |
| jschardet | 3.1.4 |
| kerberos | 2.1.1 |
| minimist | ^1.2.6 |
| native-is-elevated | 0.7.0 |
| native-keymap | ^3.3.5 |
| native-watchdog | ^1.4.1 |
| node-pty | ^1.1.0-beta22 |
| open | ^8.4.2 |
| tas-client-umd | 0.2.0 |
| v8-inspect-profiler | ^0.1.1 |
| vscode-oniguruma | 1.7.0 |
| vscode-regexpp | ^3.1.0 |
| vscode-textmate | 9.1.0 |
| yauzl | ^3.0.0 |
| yazl | ^2.4.3 |

## DevDependencies

| Package | Version |
|---------|---------|
| @playwright/test | ^1.46.1 |
| @stylistic/eslint-plugin-ts | ^2.8.0 |
| @types/cookie | ^0.3.3 |
| @types/debug | ^4.1.5 |
| @types/eslint | ^9.6.1 |
| @types/gulp-svgmin | ^1.2.1 |
| @types/http-proxy-agent | ^2.0.1 |
| @types/kerberos | ^1.1.2 |
| @types/minimist | ^1.2.1 |
| @types/mocha | ^9.1.1 |
| @types/node | 20.x |
| @types/sinon | ^10.0.2 |
| @types/sinon-test | ^2.4.2 |
| @types/trusted-types | ^1.0.6 |
| @types/vscode-notebook-renderer | ^1.72.0 |
| @types/webpack | ^5.28.5 |
| @types/wicg-file-system-access | ^2020.9.6 |
| @types/windows-foreground-love | ^0.3.0 |
| @types/winreg | ^1.2.30 |
| @types/yauzl | ^2.10.0 |
| @types/yazl | ^2.4.2 |
| @typescript-eslint/utils | ^8.8.0 |
| @vscode/gulp-electron | ^1.36.0 |
| @vscode/l10n-dev | 0.0.35 |
| @vscode/telemetry-extractor | ^1.10.2 |
| @vscode/test-cli | ^0.0.6 |
| @vscode/test-electron | ^2.4.0 |
| @vscode/test-web | ^0.0.62 |
| @vscode/v8-heap-parser | ^0.1.0 |
| @vscode/vscode-perf | ^0.0.19 |
| @webgpu/types | ^0.1.44 |
| ansi-colors | ^3.2.3 |
| asar | ^3.0.3 |
| chromium-pickle-js | ^0.2.0 |
| cookie | ^0.7.2 |
| copy-webpack-plugin | ^11.0.0 |
| css-loader | ^6.9.1 |
| cssnano | ^6.0.3 |
| debounce | ^1.0.0 |
| deemon | ^1.8.0 |
| electron | 32.2.6 |
| eslint | ^9.11.1 |
| eslint-formatter-compact | ^8.40.0 |
| eslint-plugin-header | 3.1.1 |
| eslint-plugin-jsdoc | ^50.3.1 |
| eslint-plugin-local | ^6.0.0 |
| event-stream | 3.3.4 |
| fancy-log | ^1.3.3 |
| file-loader | ^6.2.0 |
| glob | ^5.0.13 |
| gulp | ^4.0.0 |
| gulp-azure-storage | ^0.12.1 |
| gulp-bom | ^3.0.0 |
| gulp-buffer | 0.0.2 |
| gulp-filter | ^5.1.0 |
| gulp-flatmap | ^1.0.2 |
| gulp-gunzip | ^1.0.0 |
| gulp-gzip | ^1.4.2 |
| gulp-json-editor | ^2.5.0 |
| gulp-plumber | ^1.2.0 |
| gulp-rename | ^1.2.0 |
| gulp-replace | ^0.5.4 |
| gulp-sourcemaps | ^3.0.0 |
| gulp-svgmin | ^4.1.0 |
| gulp-untar | ^0.0.7 |
| husky | ^0.13.1 |
| innosetup | 6.0.5 |
| istanbul-lib-coverage | ^3.2.0 |
| istanbul-lib-instrument | ^6.0.1 |
| istanbul-lib-report | ^3.0.0 |
| istanbul-lib-source-maps | ^4.0.1 |
| istanbul-reports | ^3.1.5 |
| lazy.js | ^0.4.2 |
| merge-options | ^1.0.1 |
| mime | ^1.4.1 |
| minimatch | ^3.0.4 |
| minimist | ^1.2.6 |
| mocha | ^10.2.0 |
| mocha-junit-reporter | ^2.2.1 |
| mocha-multi-reporters | ^1.5.1 |
| npm-run-all | ^4.1.5 |
| os-browserify | ^0.3.0 |
| p-all | ^1.0.0 |
| path-browserify | ^1.0.1 |
| postcss | ^8.4.33 |
| postcss-nesting | ^12.0.2 |
| pump | ^1.0.1 |
| rcedit | ^1.1.0 |
| rimraf | ^2.2.8 |
| sinon | ^12.0.1 |
| sinon-test | ^3.1.3 |
| source-map | 0.6.1 |
| source-map-support | ^0.3.2 |
| style-loader | ^3.3.2 |
| ts-loader | ^9.5.1 |
| ts-node | ^10.9.1 |
| tsec | 0.2.7 |
| tslib | ^2.6.3 |
| typescript | ^5.8.0-dev.20241202 |
| typescript-eslint | ^8.8.0 |
| util | ^0.12.4 |
| webpack | ^5.94.0 |
| webpack-cli | ^5.1.4 |
| webpack-stream | ^7.0.0 |
| xml2js | ^0.5.0 |
| yaserver | ^0.4.0 |

## Author

Microsoft Corporation

## License

MIT

## Repository

[https://github.com/microsoft/vscode](https://github.com/microsoft/vscode)

## Bugs

[https://github.com/microsoft/vscode/issues](https://github.com/microsoft/vscode/issues)

## Homepage

No homepage provided.

## Keywords

No keywords provided.

## Engines

No engines specified.

## Funding

No funding information provided.

TERMINATE