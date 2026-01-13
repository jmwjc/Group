# Zotero 文献管理与科研协作指南
#people/WuJC
#Tutorial/Zotero

**Zotero** 是一款开源的文献管理工具，凭借其强大的插件生态和灵活的元数据处理能力，已成为计算力学研究组进行文献调研、论文写作的核心基础设施。

## 基础配置与环境优化

在开始使用前，建议进行以下基础设置以保持文献库的整洁和同步的高效。

### 核心设置 (Settings)
- **禁用自动抓取**：取消勾选 `Setting -> General -> Automatically take snapshots when creating items from web pages`（防止快照占用过多空间，建议手动保存重要的网页快照）。
- **清理自动标签**：取消勾选 `Setting -> General -> Automatically tag items with keywords and subject headings`（避免导入文献时产生大量冗余、无意义的标签）。

### 云端同步 (Sync)
- **WebDAV 同步**：推荐使用**坚果云**进行附件同步。
    - 在坚果云后台开通第三方应用密码。
    - 在 Zotero 中配置：`Settings -> Sync -> File Syncing -> 使用 WebDAV`。
    - 验证服务器：输入坚果云提供的服务器地址、账号及应用密码。

## 核心插件矩阵

插件是 Zotero 的灵魂，以下是研究组推荐的必装插件：

| 插件名称 | 推荐指数 | 核心功能 |
| :--- | :--- | :--- |
| **Better BibTeX** | ★★★★★ | LaTeX 联动的核心，管理 Citation Key 并自动导出 `.bib`。 |
| **Zutilo** | ★★★★★ | 提供强大的右键菜单，支持批量清理标签、管理附件、建立条目关联。 |
| **ZotFile** | ★★★★ | 自动重命名 PDF、提取注释，支持将附件同步至平板端阅读。 |
| **Mdnotes** | ★★★ | 将 Zotero 中的条目元数据和注释导出为 Markdown 文件。 |

## LaTeX 自动化联动流

实现“Zotero 修改，LaTeX 自动更新”的自动化流程。

### 1. 配置引文键 (Citation Key)
Citation Key 是你在 LaTeX 中使用 `\cite{...}` 的唯一标识。
- **设置路径**：`Settings -> Better BibTeX -> Citation keys`。
- **推荐格式**：`[auth:lower][year]` (例如：`smith2023`) 或 `[auth][year][shorttitle3_3]`。
- **快速拷贝**：设置 `Settings -> Export -> Quick Copy -> Better BibTeX Quick Copy: Cite Keys`。

### 2. 自动导出与同步
1. 右键点击你的**项目分类文件夹** -> `Export Collection...`。
2. **格式选择**：选择 `Better BibLaTeX`。
3. **开启自动同步**：勾选 `Keep updated`。
4. **保存位置**：将其保存至你的 LaTeX 项目根目录下（如 `references.bib`）。
5. **生效效果**：只要你在 Zotero 中更新文献信息或新增文献，该 `.bib` 文件会实时刷新。

## Obsidian 联动与管理技巧

### 文献导入标准流程
1. **新建分类**：为每个研究课题建立独立文件夹。
2. **拖入 PDF**：直接将 PDF 拖入 Zotero，软件会自动通过 DOI 识别元数据。
3. **检查核对**：检查标题、作者、期刊名是否抓取准确，尤其是大小写。
4. **清理标签**：利用 **Zutilo** 批量删除导入时自带的无用标签：
   - `Tools -> Zutilo Preferences -> User Interface -> Remove tags`。
   - 随后在文献右键菜单中选择 `Zutilo -> Remove tags`。

### 提取注释与笔记
- **提取 PDF 注释**：使用 **ZotFile** 提取 PDF 中的高亮和评论。
- **导出至 Obsidian**：
    - 使用 **Mdnotes** 将提取的注释导出为 `.md`。
    - 或参考 [在 Obsidian 中创建文献列表](https://nataliekraneiss.com/en/your-academic-reading-list-in-obsidian/) 配置 Dataview 自动索引。

### 视觉管理
- **标签颜色**：右键点击右下角的标签 -> `Assign Color`。设置颜色后，文献条目前会出现对应色块，方便快速识别论文权重或状态。
