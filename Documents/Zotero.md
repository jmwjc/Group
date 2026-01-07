---
creation_date: 2025-12-22
---
#People/WuJC  #People/HOCHOYIN  

## 插件
# [Better BibTex](https://retorque.re/zotero-better-bibtex/)
- Citation key format: 
>[auth:lower][year]
- Set quick copy:
>Preference->Export->Quick Copy->Item Format->Better BibTex Quick Copy: Cite Keys

# [Zutilo](https://github.com/wshanks/Zutilo)
- Create relation between files.
[**Zotero->ZotFile->Mdnotes->Obsidian->Dataview Workflow**](https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536)
- Remove all tags
>Tools->Zutilo Preference->User Interface->Remove tags->Click Zutilo context menu

# [ZotFile](http://zotfile.com/)
- Extract annotations from pdf.
- Push the pdfs to ipad, and recollect them after annotating. 

# [Mdnotes](https://github.com/argenos/zotero-mdnotes)
- Create md from annotations extracted by ZotFile

# 使用教程
#### 文献导入Zotero
- 打开zotero
- 新建分类
- 把文献PDF汇入（拉入）zotero (当拖入PDF时会发现软件会自动生成讯息页面)
- 检查PDF档案与文献讯息是否一致？
- 如果没有讯息的文献 ，新增项目 -> 期刊文章 -> 补充讯息内容
#### 配置引文键 (Citation Key)
Citation Key 是你在 LaTeX 中引用文献的唯一标识（例如 `\cite{smith2020}` 中的 `smith2020`）。
1. 在 Zotero 中，打开 "编辑" -> "设置" -> "导出" -> "条目格式" -> 选择 [Better BibTex](https://retorque.re/zotero-better-bibtex/)
2. 在设置中，打开[Better BibTex](https://retorque.re/zotero-better-bibtex/) -> 设置你喜欢的格式。
  - **推荐格式：** `[auth][year]` (作者+年份，如 Smith2023) 或 `[auth:lower][year]` (小写作者+年份)。
#### 导出参考文献库 (.bib 文件)
1. 右键点击你想要使用的**分类文件夹** -> **导出文献库**
2. **格式选择：** 选择 **Better BibLaTeX** (推荐) 或  [Better BibTex](https://retorque.re/zotero-better-bibtex/)。
3. **关键设置（打钩）：**
   - **Keep updated (保持更新)：** _这是联动的灵魂_。当你修改 Zotero 里的条目时，导出的 `.bib` 文件会自动同步更新。
4. 保存文件，命名为 `references.bib`（或你喜欢的名字）。

#### 使用 VS Code + LaTeX Workshop (本地编辑器)

1. 将 Zotero 导出的 `references.bib` 文件保存在你的 LaTeX 项目根目录下。
2. 由于你在第三步勾选了 "Keep updated"，每当你在 Zotero 中新增文献或修改信息，本地的 `references.bib` 文件会自动刷新。
3. 在 VS Code 中配置 LaTeX Workshop 插件，使其能够读取该文件实现自动补全。
4. 写作时输入 `\cite{`，VS Code 会即时显示所有文献供选择。