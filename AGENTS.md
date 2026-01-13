# AGENTS.md

This is an Obsidian knowledge vault for the computational mechanics research group led by **Prof. Wu Junchao ([[WuJC]])**. It stores group documents, research notes, project tracking, and collaborates on FEM, Meshfree methods, and related computational mechanics research.

## Repository Structure

- **Documents/** - Research notes, software configurations, papers, and technical guides
- **Seminars/** - Seminar schedules, notes, and presentation materials
- **Slides/** - Presentation slides for talks and group meetings
- **People/** - Member profiles, contact information, and research interests
- **Projects/** - Active and archived research projects with progress tracking
- **Templates/** - Obsidian note templates for consistent documentation
- **.obsidian/** - Obsidian vault configuration and plugins

## No Build/Lint/Test Commands

This repository contains markdown files only. There are no:
- Build commands
- Linting commands
- Test commands
- Package managers (npm, pip, etc.)

## Writing Notes

### Title and Authorship
- First line: H1 title (e.g., `# Note Title`)
- Second line: Author tag `#people/author_name`
- Do not use numbered headings (no "1.", "2." in section titles)

### Tags and Classification
- Use specific tags for document classification:
    - `#Tutorial`: Technical guides, software configurations, and coding tutorials.
    - `#Policy`: Administrative rules, lab regulations, and workflow guidelines.
- **Hierarchical Tags**: Use nested tags to further categorize content (e.g., `#Tutorial/LaTeX`, `#Tutorial/VSCode`). This allows for better organization in the tag pane and Dataview queries.
- Tags should be placed on the third line (below the authorship tag).
- Do not create redundant tags; check the existing tag list in the `Home` dashboard.
### People Directory
- Files in the `People/` directory should include a YAML frontmatter with a `name` field for the person's Chinese name (e.g., `name: 张三`).
- When referencing people, use the filename as the link (e.g., `[[WuJC]]`) rather than the Chinese name.

### Research Conventions
- Use Chinese for group-internal documentation, English for academic/technical content
- Mathematical formulas: use `$...$` for inline and `$$...$$` for display math
- Code snippets: specify language for syntax highlighting
- Citations: follow a consistent format, e.g., `[Author2023]` or use Dataview for paper tracking

### File Naming
- **Notes**: Descriptive with spaces (e.g., "Nonlinear elasticity theory.md")
- **Projects**: Use project codes if established (e.g., "P001-meshfree-convergence.md")
- **People**: Use consistent format (e.g., "Zhang San.md" or "zhangsan-profile.md")

## Research Areas

This vault documents work in:
- Finite Element Method (FEM)
- Meshfree Methods
- Computational Mechanics
- Numerical Analysis
- Continuum Mechanics
- Material Modeling

## Obsidian Plugins Used

- **obsidian-git** - Version control and backup
- **dataview** - Data queries and indexed searches
- **tasks** - Task and deadline management
- **periodic-notes** - Daily/weekly research logs
- **quickadd** - Quick note creation
- **homepage** - Custom landing page

## Project Tracking

When documenting research projects:
1. Create project entry with clear goals and timeline
2. Link related papers, code, and notes
3. Track progress using tasks with due dates
4. Document findings and results in meeting notes
5. Archive completed projects with summary

## Git Workflow

This vault uses git for version control:
- Commit frequently with descriptive messages
- Use meaningful commit messages (e.g., "Add FEM convergence analysis notes")
- Push to remote regularly for backup
- Note: .obsidian/workspace.json changes frequently and can be noisy

## Guidelines for Agents

Agents should NOT:
- Add code files or programming libraries (unless explicitly requested)
- Set up build systems or development environments
- Create test frameworks

Agents MAY:
- Edit markdown notes and documentation
- Organize files and folders
- Add research-related documentation
- Update Obsidian configuration if explicitly asked
- Search and summarize existing notes on topics
