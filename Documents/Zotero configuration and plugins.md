
#Tutorial/Zotero

**Zotero**是一款开源的文献管理软件，该软件拥有丰富的插件，可与各种软件进行协同工作。

# 常用配置

- 取消勾选`Setting->General->Automatically take snapshots when creating items from web pages`
- 取消勾选`Setting->General->Automatically tag items with keywords and subject headings`
- 选择`Setting->Export->Item Format:Better BibLaTeX`，并勾选`Keep updated`
-  选择`Preference->Export->Quick Copy->Item Format->Better BibTex Quick Copy: Cite Keys`，`Citation key` format如下
```
auth.lower + year
```
# 插件列表
| 插件                                                                   | 推荐指数  | 主要功能                                  |
| -------------------------------------------------------------------- | ----- | ------------------------------------- |
| [Better BibTex](https://retorque.re/zotero-better-bibtex/index.html) | ★★★★★ | 生成`*.bib`文件，管理BibTex中的`Citation key`。 |
| [Zutilo Utility](https://github.com/wshanks/Zutilo)                  | ★★★★★ | 批量处理文献存储元素，如`tags`、附件等。               |
| [ZotFile](http://zotfile.com/)                                       | ★★★   | 提取`pdf`文件中注释。                         |
| [Mdnotes](https://github.com/argenos/zotero-mdnotes)                 | ★★★   | 根据`pdf`文件中的注释创建`md`文件。                |

# 使用技巧

- [设置webdav坚果云同步](https://help.jianguoyun.com/?p=3168)，需提前注册zotero和坚果云账户。
- Remove all tags: `Tools->Zutilo Preference->User Interface->Remove tags->Click Zutilo context menu`
- [在Obsidian中创建文献列表](https://nataliekraneiss.com/en/your-academic-reading-list-in-obsidian/)
- 设置`tags`颜色和数字可快速设置和选择`tags`
