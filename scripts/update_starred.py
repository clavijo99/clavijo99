import os
import re
import urllib.request
import json

USERNAME = "clavijo99"
README_PATH = "README.md"

SECTION_START = "<!-- STARRED_START -->"
SECTION_END   = "<!-- STARRED_END -->"

LANG_COLORS = {
    "Dart":       "#00B4AB",
    "Python":     "#3572A5",
    "JavaScript": "#F1E05A",
    "TypeScript": "#3178C6",
    "Kotlin":     "#A97BFF",
    "Swift":      "#F05138",
    "Java":       "#B07219",
    "Go":         "#00ADD8",
    "Rust":       "#DEA584",
    "C++":        "#F34B7D",
    "Shell":      "#89E051",
    "HTML":       "#E34C26",
    "CSS":        "#563D7C",
}

def lang_badge(lang):
    if not lang:
        return ""
    color = LANG_COLORS.get(lang, "888888").lstrip("#")
    label = lang.replace(" ", "%20").replace("+", "%2B")
    return f"![{lang}](https://img.shields.io/badge/-{label}-{color}?style=flat-square&logoColor=white)"

def fetch_json(url, token=None):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "readme-bot")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def fetch_starred(token=None):
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/starred?per_page=100&page={page}"
        batch = fetch_json(url, token)
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def build_section(repos):
    if not repos:
        return "_sin repositorios marcados con estrella aún._\n"

    lines = []
    for r in repos:
        name        = r["name"]
        full_name   = r["full_name"]
        description = (r.get("description") or "").strip()
        lang        = r.get("language")
        stars       = r.get("stargazers_count", 0)
        forks       = r.get("forks_count", 0)
        url         = r["html_url"]
        is_fork     = r.get("fork", False)
        topics      = r.get("topics", [])

        fork_tag  = " `fork`" if is_fork else ""
        desc_line = f" — {description}" if description else ""
        badge     = lang_badge(lang)
        stats     = f"⭐ {stars}"
        if forks:
            stats += f" · 🍴 {forks}"
        topic_tags = " ".join(f"`{t}`" for t in topics[:4])

        line = f"| [{name}]({url}){fork_tag} | {desc_line.lstrip(' — ')} | {badge} | {stats} |"
        if topic_tags:
            line = f"| [{name}]({url}){fork_tag} | {desc_line.lstrip(' — ')} {topic_tags} | {badge} | {stats} |"
        lines.append(line)

    header = (
        "| repositorio | descripción | lenguaje | stats |\n"
        "|-------------|-------------|----------|-------|\n"
    )
    return header + "\n".join(lines) + "\n"

def update_readme(section_content):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        rf"{re.escape(SECTION_START)}.*?{re.escape(SECTION_END)}",
        re.DOTALL
    )
    replacement = f"{SECTION_START}\n{section_content}{SECTION_END}"

    if not pattern.search(content):
        print("ERROR: marcadores <!-- STARRED_START --> / <!-- STARRED_END --> no encontrados en README.md")
        raise SystemExit(1)

    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"README actualizado con {section_content.count('|') // 4} repos.")

if __name__ == "__main__":
    token = os.environ.get("GH_TOKEN")
    repos = fetch_starred(token)
    section = build_section(repos)
    update_readme(section)