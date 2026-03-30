---
creation_date: 2026-03-29
---
 #people/WuJC 

# Lazygit 使用教程

## 一、什么是 Lazygit？

Lazygit 是一个用于 Git 的终端用户界面（TUI）工具，由 Jesse Duffield 开发。它将复杂的 Git 命令转化为直观的键盘操作，让你在终端中高效地完成各种 Git 操作，无需记忆繁琐的命令行参数。

**核心优势：**
- 🚀 可视化操作，告别繁琐命令
- ⌨️ 键盘驱动，效率翻倍
- 🔄 支持撤销/重做（Git 操作的"后悔药"）
- 📊 交互式变基，所见即所得

---

## 二、安装方法

### macOS / Linux (Homebrew)
```bash
brew install lazygit
```

### Ubuntu / Debian
```bash
sudo add-apt-repository ppa:lazygit-team/daily
sudo apt update
sudo apt install lazygit
```

### Arch Linux
```bash
sudo pacman -S lazygit
# 或从 AUR
yay -S lazygit
```

### Windows (Scoop / Chocolatey / Winget)
```bash
# Scoop
scoop install lazygit

# Chocolatey
choco install lazygit

# Winget
winget install jesseduffield.lazygit
```

### Go 安装（全平台）
```bash
go install github.com/jesseduffield/lazygit@latest
```

### 验证安装
```bash
lazygit --version
```

---

## 三、快速启动

在任意 Git 仓库目录下运行：
```bash
lazygit
```

**建议设置别名**（添加到 `~/.zshrc` 或 `~/.bashrc`）：
```bash
alias lg='lazygit'
```
之后只需输入 `lg` 即可启动。

---

## 四、界面布局

Lazygit 界面分为几个主要区域：

| 区域 | 位置 | 功能 |
|------|------|------|
| **状态面板** | 左上 | 显示当前分支、仓库状态 |
| **文件面板** | 左中 | 显示工作区文件变更 |
| **分支面板** | 左下 | 显示本地和远程分支 |
| **主面板** | 右侧 | 显示详细信息（diff、日志等） |
| **命令面板** | 底部 | 显示可用命令和快捷键 |

---

## 五、常用快捷键速查

### 全局快捷键
| 快捷键 | 功能 |
|--------|------|
| `?` | 查看所有快捷键帮助 |
| `q` | 退出 lazygit |
| `Tab` / 数字键 `1-5` | 切换面板 |
| `↑↓` / `j k` | 上下导航 |
| `h l` | 左右导航 |
| `z` | 撤销上一步操作 |
| `Ctrl+z` | 重做 |
| `R` | 刷新界面 |

### 文件操作（Files 面板）
| 快捷键 | 功能 |
|--------|------|
| `Space` | 暂存/取消暂存文件 |
| `a` | 暂存所有文件 |
| `u` | 取消暂存文件 |
| `Enter` | 查看文件 diff |
| `d` | 放弃文件更改 |
| `s` | 贮藏(stash)所有更改 |
| `v` | 进入行选择模式（部分暂存） |

### 提交操作（Commits 面板）
| 快捷键 | 功能 |
|--------|------|
| `c` | 创建新提交 |
| `C` | 复制提交（cherry-pick） |
| `V` | 粘贴提交 |
| `r` | 变基(rebase) |
| `i` | 交互式变基 |
| `s` | squash（压缩提交） |
| `f` | fixup（修正提交） |
| `d` | drop（删除提交） |
| `e` | edit（编辑提交） |

### 分支操作（Branches 面板）
| 快捷键 | 功能 |
|--------|------|
| `n` | 创建新分支 |
| `Space` | 切换分支 |
| `m` | 合并分支 |
| `d` | 删除分支 |
| `r` | 变基到当前分支 |
| `-` | 切换到上一个分支 |
| `w` | 创建工作树(worktree) |

### 远程操作
| 快捷键 | 功能 |
|--------|------|
| `P` | 推送 |
| `p` | 拉取 |
| `f` | 获取(fetch) |

---

## 六、核心操作流程

### 1. 日常提交代码
```
1. 进入 Git 仓库，运行 lazygit
2. 在 Files 面板，用 ↑↓ 选择文件
3. 按 Space 暂存文件（或按 a 暂存全部）
4. 按 c 创建提交
5. 输入提交信息，保存退出
6. 按 P 推送到远程
```

### 2. 部分暂存（精准控制）
```
1. 选中文件，按 Enter 查看 diff
2. 按 v 进入行选择模式
3. 用 ↑↓ 选择代码行范围
4. 按 Space 暂存选中行
5. 按 a 暂存整个代码块(hunk)
```

### 3. 交互式变基（整理提交历史）
```
1. 进入 Commits 面板
2. 按 i 进入交互式变基模式
3. 用 Ctrl+j/k 上下移动提交
4. 按 s 压缩提交、按 d 删除、按 e 编辑
5. 按 m 继续完成变基
```

### 4. 解决合并冲突
```
1. 合并后出现冲突时，冲突文件会标红
2. 选中冲突文件，按 Enter 查看
3. 用 ↑↓ 导航到冲突块
4. 按 1 保留当前版本，按 3 保留传入版本
5. 按 2 保留双方，或按 e 手动编辑
6. 解决后按 m → "continue" 继续
```

### 5. Cherry-Pick（复制提交）
```
1. 在 Commits 面板找到目标提交
2. 按 C 复制提交
3. 切换到目标分支
4. 按 V 粘贴提交
```

---

## 七、高级功能

### 工作树（Worktree）
用于多分支并行开发，避免频繁切换：
```
1. 按 4 进入工作树面板
2. 按 n 创建新工作树
3. 选择基础分支，输入目录路径
4. 按 Enter 切换到工作树目录
```

### 撤销与重做
- `z`：撤销上一次 Git 操作（基于 reflog）
- `Ctrl+z`：重做被撤销的操作
- **注意**：只能撤销 commit 和 branch 相关操作，工作区未暂存的改动无法撤销

### 与 Delta 配合（美化 diff）
在配置文件 `~/.config/lazygit/config.yml` 中添加：
```yaml
git:
  paging:
    pager: delta --dark --paging=never
```

---

## 八、配置文件

### 配置文件位置
- **Linux/macOS**: `~/.config/lazygit/config.yml`
- **Windows**: `%APPDATA%\lazygit\config.yml`

### 推荐配置示例
```yaml
gui:
  showBranchCommitGraph: true
  showFileTree: true
  theme:
    activeBorderColor:
      - green
      - bold
    inactiveBorderColor:
      - default
  timeFormat: "2006-01-02 15:04"

git:
  autoFetch: true
  autoRefresh: true
  mainBranches:
    - main
    - master

os:
  editPreset: "vscode"  # 或 "vim", "nvim", "sublime"
```

### 自定义快捷键
```yaml
keybinding:
  universal:
    quit: "q"
    return: "<esc>"
  files:
    commitChanges: "c"
    stashAllChanges: "s"
  branches:
    checkoutBranchByName: "c"
```

---

## 九、与编辑器集成

### Neovim (lazygit.nvim)
```vim
" 安装插件后配置
nnoremap <Leader>lg :LazyGit<CR>
nnoremap <Leader>lc :LazyGitConfig<CR>
nnoremap <Leader>lf :LazyGitFilterCurrentFile<CR>
```

### VS Code
安装 "Lazygit" 扩展，可在内置终端中启动。

---

## 十、实用技巧

| 技巧 | 说明 |
|------|------|
| `?` 随时求助 | 忘记快捷键时随时查看 |
| 先在测试仓库练习 | 熟悉操作后再用于生产仓库 |
| 重要操作前先 commit | 避免无法撤销的失误 |
| 配合 delta 使用 | 获得更漂亮的 diff 展示 |
| 使用 `Ctrl+r` | 快速切换到最近访问的仓库 |

---

## 参考资源

- **官方仓库**: https://github.com/jesseduffield/lazygit
- **中文快捷键文档**: `docs/keybindings/Keybindings_zh-CN.md`
- **配置文件文档**: `docs/Config.md`

---