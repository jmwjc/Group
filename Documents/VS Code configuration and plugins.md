# VS Code configuration and plugins
#people/WuJC
#Tutorial/VSCode

# 常用配置

`settings.json`为`VS Code`的配置文件，下面为几项基本常用配置：
```json
{
// Default settings can be found from https://vscode-docs.readthedocs.io/en/stable/customization/userandworkspace/

//-------- Editor configuration --------

    // Controls the font family.
    // "editor.fontFamily": "Menlo, Monaco, 'Courier New', monospace",
    "editor.fontFamily": "Courier",

    // Controls the font size.
    "editor.fontSize": 16,

    // Controls the rendering size of tabs in characters. Accepted values: "auto", 2, 4, 6, etc. If set to "auto", the value will be guessed when a file is opened.
    "editor.tabSize": 4,

    // Controls visibility of line numbers: "off", "on", "relative", "interval".
    "editor.lineNumbers": "relative",

    // Controls if the editor will insert spaces for tabs. Accepted values:  "auto", true, false. If set to "auto", the value will be guessed when a file is opened.
    "editor.insertSpaces": true,

    "editor.wordWrap": "on",

//-------- Files configuration --------
    "files.autoSave": "onFocusChange",
    
//-------- Git configuration --------
    "git.autofetch": true,
    "git.confirmSync": false,
    "git.enableSmartCommit": true,

    // Control whether a repository in parent folders of workspaces or open files should be opened.
    "git.openRepositoryInParentFolders": "never",

    // Contorls whether to automatically detect git submodules.
    "git.detectSubmodules": false,
}
```
# 插件列表

| 插件                  | 推荐指数  | 主要功能                                  |
| ------------------- | ----- | ------------------------------------- |
| Git Graph           | ★★★★★ | 可视化Git                                |
| Data Wrangler       | ★★★★★ | 读取`xlsx`文件数据                          |
| Todo Tree           | ★★★★★ | 统计、高亮`magic comment`，如`TODO`、`FIXME`等 |
| Remote Development  | ★★★★★ | 服务器相关插件                               |
| TexLab              | ★★★★  | latex-lsp                             |
| LaTeX Workshop      | ★★★★  | LaTeX相关多功能包，与TexLab二选一安装即可            |
| LaTeX Utilities     | ★★★★★ | 包含LeTeX相关的snippets                    |
| Markdown All in One | ★★★★★ | Markdown相关多功能包                        |
| Vim                 | ★★★   | Vim功能支持                               |
| vscode-gmsh         | ★★★   | gmsh语言高亮                              |
| Julia               | ★★★   | Julia语言支持                             |
| Jupyter             | ★★★   | Jupyter集成                             |

# 使用技巧
## 配置服务器ssh公钥
1. 配置ssh config`Connect to Host...->Configure SSH Hosts...->/Users/username/.ssh/config`
```
Host hostname
	HostName server_ip
	User username
```
2. 将ssh公钥添加到远程服务器
```
ssh-copy-id user_name@server_ip
```
- 删除已存在的公钥：在`.ssh/known_hosts`文件中删除相对应公钥。
