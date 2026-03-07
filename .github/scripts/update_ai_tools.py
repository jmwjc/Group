import os
import requests
import re

TOPICS = [
    "physics-informed-neural-networks",
    "scientific-computing",
    "mathematics",
    "mechanics",
    "efficiency",
    "productivity-tool"
]

TRACKER_FILE = "Documents/AI Tool Tracker.md"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_top_repos(topic):
    url = f"https://api.github.com/search/repositories?q=topic:{topic}+topic:ai&sort=stars&order=desc"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("items", [])[:5] 
    else:
        print(f"Failed to fetch {topic}: {response.status_code}")
        return []

def generate_markdown_table(data):
    if not data:
        return "No new tools found this week."
    
    header = "| Name | Description | Stars | Category | Link |\n| --- | --- | --- | --- | --- |"
    rows = []
    seen = set()
    
    for item in data:
        if item['html_url'] in seen:
            continue
        seen.add(item['html_url'])
        
        name = item['name']
        desc = item['description'] or "No description provided."
        stars = item['stargazers_count']
        link = item['html_url']
        category = "Math/Mechanics" if any(t in item['topics'] for t in ["mathematics", "mechanics", "scientific-computing", "physics-informed-neural-networks"]) else "Efficiency"
        
        desc = desc.replace("|", "\\|").replace("\n", " ")
        rows.append(f"| **{name}** | {desc} | {stars:,} | {category} | [Link]({link}) |")
    
    return header + "\n" + "\n".join(rows)

def update_tracker_file(content):
    with open(TRACKER_FILE, "r") as f:
        full_content = f.read()
    
    start_marker = "<!-- START_AUTO -->"
    end_marker = "<!-- END_AUTO -->"
    
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    new_content = f"{start_marker}\n\n{content}\n\n{end_marker}"
    
    updated_full_content = pattern.sub(new_content, full_content)
    
    with open(TRACKER_FILE, "w") as f:
        f.write(updated_full_content)

if __name__ == "__main__":
    all_repos = []
    for topic in TOPICS:
        print(f"Fetching {topic}...")
        all_repos.extend(fetch_top_repos(topic))
    
    all_repos.sort(key=lambda x: x['stargazers_count'], reverse=True)
    
    markdown = generate_markdown_table(all_repos)
    update_tracker_file(markdown)
    print("Tracker updated successfully.")
