# Plan: Automated AI Tool Tracking

## TL;DR

> **Quick Summary**: Set up a GitHub Actions workflow that runs weekly to fetch popular AI tools (focused on efficiency, math, and mechanics) and updates an Obsidian tracker file.
> 
> **Deliverables**:
> - `.github/workflows/track-ai-tools.yml`: Scheduled workflow.
> - `.github/scripts/update_ai_tools.py`: Python script for data fetching and processing.
> - `Documents/AI Tool Tracker.md`: The generated/updated tracker file.
> 
> **Estimated Effort**: Short
> **Parallel Execution**: NO - sequential implementation.
> **Critical Path**: Script Development → Workflow Configuration → Verification.

---

## Context

### Original Request
"I want to automatically track the most popular AI tools, how can I make it"

### Interview Summary
**Key Discussions**:
- **Location**: `Documents/AI Tool Tracker.md`
- **Fields**: Name, links, descriptions, star counts, categories.
- **Automation**: GitHub Actions (weekly updates).
- **Focus**: Efficiency, Mathematics, and Mechanics-related AI.

### Research Findings
- **GitHub API**: The most robust way to find "Mathematics" and "Mechanics" AI projects via topics (e.g., `physics-informed-neural-networks`, `scientific-computing`).

---

## Work Objectives

### Core Objective
Implement an automated system to curate and update a list of AI tools relevant to the research group's focus areas.

### Concrete Deliverables
- `.github/workflows/track-ai-tools.yml`
- `.github/scripts/update_ai_tools.py`
- `Documents/AI Tool Tracker.md`

### Definition of Done
- [ ] Workflow runs successfully on GitHub.
- [ ] `Documents/AI Tool Tracker.md` contains accurate, categorized tool information.
- [ ] Existing content in the tracker file is preserved.

### Must Have
- Automated weekly run.
- Category-based sorting (Efficiency, Math, Mechanics).
- Inclusion of star counts and descriptions.

### Must NOT Have (Guardrails)
- Duplication of entries (must deduplicate before writing).
- Overwriting of manual notes (use marker comments).

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: NO
- **User wants tests**: NO
- **QA approach**: Manual verification of file output and Action logs.

### Manual QA Procedure
- **GitHub Actions**:
  - Manually trigger the workflow.
  - Check "Actions" tab for success logs.
- **File Verification**:
  - Open `Documents/AI Tool Tracker.md`.
  - Verify that categories are present and links work.

---

## Execution Strategy

### Parallel Execution Waves
Sequential.

---

## TODOs

- [ ] 1. Initialize Project Structure
  **What to do**:
  - Create `.github/scripts/` directory.
  - Create initial `Documents/AI Tool Tracker.md` if it doesn't exist.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`git-master`]
  **Parallelization**: Sequential.

- [ ] 2. Develop Python Fetching Script
  **What to do**:
  - Write `.github/scripts/update_ai_tools.py`.
  - Implement GitHub Search API calls for specific topics (`physics-informed-neural-networks`, `scientific-computing`, `mathematics`, `mechanics`, `efficiency`).
  - Implement markdown table generation.
  - Implement logic to read `Documents/AI Tool Tracker.md` and insert content between markers.
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: [`python`]
  **Parallelization**: Sequential.

- [ ] 3. Configure GitHub Actions Workflow
  **What to do**:
  - Create `.github/workflows/track-ai-tools.yml`.
  - Set schedule to weekly (e.g., `0 0 * * 1`).
  - Add `workflow_dispatch` for manual triggers.
  - Configure permissions to write to repository.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`git-master`]
  **Parallelization**: Sequential.

- [ ] 4. Final Verification
  **What to do**:
  - Run the workflow manually.
  - Inspect `Documents/AI Tool Tracker.md`.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`git-master`]
  **Parallelization**: Sequential.

---

## Commit Strategy
- `feat(automation): add AI tool tracking script and workflow`

---

## Success Criteria
- [ ] Workflow passes.
- [ ] Tracker file updated with latest tools.
