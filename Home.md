# 🗄️ 计算力学研究组知识库

欢迎使用本课题组知识库。本页面作为全局导航枢纽，帮助您快速追踪研究进展和管理任务。

---

## 🔔 组会待办汇总

```tasks
not done
path includes Seminars
short mode
limit 10
```

---

## ✅ 组会完成汇总

```tasks
done
path includes Seminars
short mode
limit 10
```

---

## 📖 管理规范

```dataview
LIST FROM "Documents" AND #Policy
```

---

## 🛠️ 技术指南

```dataview
LIST FROM "Documents" AND #Tutorial
```

---

## 🏗️ 成员与项目

- [[People/|👥 成员列表]]
- [[Projects/|📂 活跃项目]]
- [[AGENTS.md|🤖 协作规范]]

---

## 📅 近期组会进展

```dataview
TABLE
FROM "Seminars"
WHERE file.name != "Seminar"
SORT file.name DESC
LIMIT 5
```

---

## 🏷️ 常用领域标签
#Policy #Tutorial #Tutorial/LaTeX #Tutorial/VSCode #Tutorial/Zotero

---
> [!tip] 提示
> - 按 `Ctrl/Cmd + Shift + F` 使用 Omnisearch 搜索笔记
> - 使用 `oc` 指令让 AI 协助你整理知识
