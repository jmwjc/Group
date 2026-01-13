# OpenCode 使用指南
#people/WuJC
#Tutorial

本教程旨在帮助研究组同学快速配置并高效使用 OpenCode 助手，以辅助计算力学相关的科研工作。本指南基于 [OpenCode 官方文档](https://opencode.ai/docs/) 编写。

## 配置与安装

### 环境准备

在安装 OpenCode 之前，请确保你的系统满足以下条件：

- **终端环境**：建议使用支持 modern 特性的终端模拟器：
    - macOS/Linux: WezTerm, Ghostty, Kitty, Alacritty
    - Windows: 建议在 WSL2 中使用上述终端
- **API 密钥**：OpenCode 需要 LLM 供应商（如 Anthropic 或 OpenAI）的 API Key。请向导师申请或自行获取。

### 安装步骤

官方推荐使用一键安装脚本：

```bash
# 使用 curl 安装
curl -fsSL https://opencode.ai/install | bash
```

**备选安装方式**：

- **macOS (Homebrew)**：
  ```bash
  brew install anomalyco/tap/opencode
  ```
- **Node.js (npm)**：
  ```bash
  npm install -g opencode-ai
  ```
- **Windows (Scoop)**：
  ```powershell
  scoop bucket add extras
  scoop install extras/opencode
  ```

### 验证与基本配置

1. **设置 API Key**：在你的 `.zshrc` 或 `.bashrc` 中添加：
   ```bash
   export OPENCODE_API_KEY="你的API密钥"
   ```
2. **测试运行**：在终端输入 `opencode`（或简写 `oc`，如果设置了别名）。
3. **配置文件路径**：
    - **全局配置**：`~/.config/opencode/opencode.jsonc`
    - **项目配置**：在 vault 根目录下创建 `.opencode/opencode.jsonc`

## 扩展功能：MCP 与自定义 Agent

OpenCode 支持 Model Context Protocol (MCP)，可以为 AI 提供更强大的工具集（如搜索、计算、数据库操作）。

### 安装 MCP 服务

MCP 服务通常通过修改配置文件来安装：

1. **编辑配置文件**：打开全局或项目级的 `opencode.jsonc`。
2. **添加 mcp-servers**：在配置文件中定义服务及其启动命令。
   ```jsonc
   {
     "mcp-servers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/绝对路径/to/your/vault"]
       },
       "google-search": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-google-search"],
         "env": {
           "GOOGLE_API_KEY": "你的KEY",
           "GOOGLE_CX": "你的CX"
         }
       }
     }
   }
   ```
3. **重启加载**：保存后重启 OpenCode 即可识别新工具。

### 自定义 Agent 身份

你可以为特定的研究任务定义专用的 Agent，例如“公式推导专家”：

1. **定义 Agent**：在配置文件的 `agents` 字段中添加。
   ```jsonc
   {
     "agents": {
       "math_expert": {
         "name": "公式专家",
         "instructions": "你是一个计算力学专家，擅长有限元公式推导和张量分析。",
         "tools": ["read", "write", "python_interpreter"]
       }
     }
   }
   ```
2. **调用方式**：在对话中输入：
   ```
   使用 math_expert 帮我推导这个单元刚度矩阵
   ```

## 增强功能：Agent Skills 与 Obsidian 联动

Agent Skills 允许你为 OpenCode 定义可复用的专项技能。通过将复杂的 Prompt 封装为 Skill，可以极大提升处理效率。

### Agent Skills 基础配置

1. **目录结构**：技能存储在项目根目录的 `.opencode/skill/` 下。
   - 路径格式：`.opencode/skill/<技能名称>/SKILL.md`
2. **定义技能**：每个 `SKILL.md` 必须包含 YAML Frontmatter：
   ```markdown
   ---
   name: 技能名称
   description: 技能的简短描述，帮助 AI 识别何时使用
   ---
   # 技能详细指令
   在这里编写该技能的 System Prompt 和操作逻辑。
   ```
3. **验证加载**：在 OpenCode 终端输入 `/skills` 即可查看已识别的本地技能。

### 实战：自定义组会整理技能 (seminar-organizer)

为了实现组会录音文本的自动化处理，我们配置了 `seminar-organizer`：

1. **创建路径**：`.opencode/skill/seminar-organizer/SKILL.md`
2. **核心逻辑**：
   - 指令 AI 查阅 `/People` 目录，通过文件的 `name` 字段建立“中文名 -> 文件名”映射。
   - 规定任务输出格式为 `- [ ] 描述 [[文件名]]`。
   - 聚焦 FEM/Meshfree 等计算力学专业词汇的总结。
3. **使用方法**：
   ```bash
   oc "使用 seminar-organizer 处理 Seminars/2026-01-12组会记录.md"
   ```

### Obsidian 联动技能

你可以集成社区优秀的技能集，如 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)：

1. **安装**：将对应的技能 Markdown 文件下载到 `.opencode/skill/` 目录下。
2. **权限配置**：在 `opencode.jsonc` 中允许调用相关技能。
3. **典型应用**：
   ```bash
   oc "加载 obsidian-organizer 技能，帮我清理 Documents 目录下所有笔记的 Frontmatter"
   ```

## 进阶技能：Markdown 优化与 Canvas 自动化

为了进一步提升笔记质量和可视化能力，我们引入了 `obsidian-markdown` 和 `json-canvas` 专项技能。

### Markdown 标准化 (obsidian-markdown)

该技能擅长处理 Obsidian 特有的语法（如 Wikilinks、Callouts、Properties），可用于自动化修复和美化笔记。

- **修复断链**：`oc "使用 obsidian-markdown 检查并修复 Documents 目录下的所有 Wikilinks"`
- **统一 Properties**：`oc "确保 Documents 下的所有笔记都包含 title, author, tags 字段，且格式符合 AGENTS.md 规范"`
- **美美化排版**：`oc "将这篇笔记中的普通列表转换为 Callouts 以增强视觉层次感"`

### 可视化研究路线图 (json-canvas)

`json-canvas` 技能允许 AI 直接创建和编辑 `.canvas` 文件，实现研究思路的可视化。

- **自动生成路线图**：`oc "根据 Projects/P001 的目标，生成一个 research-roadmap.canvas，包含任务节点和逻辑连线"`
- **知识图谱构建**：`oc "分析 Documents/FEM 目录下的笔记，创建一个展示它们之间逻辑关系的 Canvas 面板"`
- **动态更新**：`oc "读取最近的组会任务，更新我的 2026-tasks.canvas 进度看板"`

## 高效使用技巧

### 场景一：自动化笔记整理与归档

当你有一堆零散的研究想法或会议记录需要归类时：

1. **搜索文件**：`opencode "查找 Documents 目录下最近三天创建的笔记"`
2. **规划建议**：`opencode "根据内容建议它们应该存放的子目录"`
3. **执行归档**：`opencode "将关于 FEM 的文件移动到 Documents/FEM，并按命名规范重命名"`
4. **清理标签**：`opencode "为这些文件在顶部添加作者署名和相关标签"`

### 场景二：科研项目进度追踪

利用 OpenCode 维护项目活跃度：

1. **记录日志**：`opencode "在 Projects/P001 笔记中记录：今日完成无网格法基础代码编写"`
2. **生成任务**：`opencode "为 P001 生成下周待办列表，并保存到笔记中"`
3. **自动周报**：`opencode "汇总本周所有修改过的笔记内容，生成一份科研周报大纲"`

### 场景三：文献阅读与综述辅助

1. **核心提取**：`opencode "读取并总结 Documents/Papers/某论文.md 的创新点"`
2. **关联搜索**：`opencode "在 vault 中搜索所有提到 '罚函数法' 的笔记并建立联系"`
3. **综述草拟**：`opencode "基于当前的无网格笔记，撰写一段约 500 字的研究现状综述"`

### 场景四：数值计算代码分析与优化

针对 FEM 或 Meshfree 的 Python/MATLAB 脚本：

1. **逻辑解析**：`opencode "解释这个求解器中刚度矩阵组装的算法逻辑"`
2. **性能诊断**：`opencode "找出这段代码中计算量最大、可以被 NumPy 优化的循环"`
3. **向量化重构**：`opencode "将这个双重循环改为 NumPy 的向量化矩阵运算"`
4. **自动化测试**：`opencode "为该算法模块编写单元测试，验证单单元情况下的正确性"`

## 进阶配合模式

### 探索模式 (Explore + Grep)

- 先用 `explore agent` 进行广度扫描。
- 锁定目录后，用 `grep` 进行内容精准匹配。
- 最后读取具体段落进行深度分析。

### 任务模式 (General + Task)

- 对于跨文件的复杂修改，调用 `general agent`。
- Agent 会通过 `todowrite` 分步骤执行。
- 任务完成后，自动运行 `git status` 供你确认。

## 常见问题排查

- **连接超时**：检查网络代理及 API Key 额度。
- **权限错误**：确保终端有权访问 iCloud 下的 Vault 路径。
- **命令冲突**：若 `oc` 别名失效，请检查配置文件中的 alias 设置。

## 获取支持

- 输入 `/help` 获取实时命令参考。
- 查阅 `AGENTS.md` 了解本 Vault 协作规范。
- 遇到复杂问题请咨询 WuJC。
