"""
auto_update_projects.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fetches ALL public repos for Yashdahiya19 via GitHub API,
sorts by last-pushed date, and rewrites the projects section
between <!--START_SECTION:projects--> and <!--END_SECTION:projects-->
in README.md.

Run automatically every day by update-projects.yml workflow.
Place this file in the ROOT of your Yashdahiya19 profile repo.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import os
import requests
from datetime import datetime, timezone

# ── Configuration ─────────────────────────────────────────────────────
USERNAME    = "Yashdahiya19"
README_PATH = "README.md"
TOKEN       = os.environ.get("GH_TOKEN", "")
START_TAG   = "<!--START_SECTION:projects-->"
END_TAG     = "<!--END_SECTION:projects-->"
TOP_N_CARDS = 6          # Number of repo pin cards to show
SKIP_REPOS  = {USERNAME}  # Skip the profile repo itself

# Language → emoji mapping
LANG_EMOJI = {
    "Python":           "🐍",
    "JavaScript":       "⚡",
    "TypeScript":       "💙",
    "HTML":             "🌐",
    "CSS":              "🎨",
    "Java":             "☕",
    "C++":              "⚙️",
    "C":                "🔧",
    "C#":               "💜",
    "Go":               "🐹",
    "Rust":             "🦀",
    "Shell":            "🖥️",
    "Jupyter Notebook": "📓",
    "R":                "📊",
    "PHP":              "🐘",
    "Ruby":             "💎",
    "Swift":            "🍎",
    "Kotlin":           "🟣",
    "Dart":             "🎯",
}

# ── Fetch all repos via GitHub API (handles pagination) ───────────────
print(f"📡 Fetching repos for @{USERNAME}...")
headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
repos   = []
page    = 1

while True:
    resp = requests.get(
        f"https://api.github.com/users/{USERNAME}/repos",
        headers=headers,
        params={"per_page": 100, "page": page, "sort": "pushed", "direction": "desc"}
    )
    if resp.status_code != 200:
        print(f"❌ API Error {resp.status_code}: {resp.json().get('message', '')}")
        break
    data = resp.json()
    if not data:
        break
    repos.extend(data)
    if len(data) < 100:
        break
    page += 1

print(f"✅ Found {len(repos)} repos total.")

# ── Filter and sort ───────────────────────────────────────────────────
repos = [r for r in repos if r["name"] not in SKIP_REPOS]
repos.sort(key=lambda r: r.get("pushed_at") or "", reverse=True)

# ── Build the projects table ──────────────────────────────────────────
now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

lines = []
lines.append(f"> 🤖 **Auto-updated:** `{now_utc}` — reflects all public repos in real time\n")
lines.append("")
lines.append("| # | 📦 Repository | 📝 Description | 🛠️ Language | ⭐ Stars | 🍴 Forks | 🕐 Last Push |")
lines.append("|:---:|:---|:---|:---:|:---:|:---:|:---:|")

for i, repo in enumerate(repos, start=1):
    name       = repo["name"]
    desc       = (repo.get("description") or "—").replace("|", "\\|")[:80]
    stars      = repo.get("stargazers_count", 0)
    forks      = repo.get("forks_count", 0)
    lang       = repo.get("language") or "—"
    pushed_raw = repo.get("pushed_at") or ""
    is_fork    = repo.get("fork", False)
    url        = repo.get("html_url", "#")

    try:
        pushed_dt  = datetime.strptime(pushed_raw, "%Y-%m-%dT%H:%M:%SZ")
        pushed_str = pushed_dt.strftime("%b %d, %Y")
    except Exception:
        pushed_str = "—"

    lang_icon  = LANG_EMOJI.get(lang, "💻")
    fork_label = " *(fork)*" if is_fork else ""
    star_str   = f"⭐ {stars}" if stars > 0 else "—"
    fork_str   = f"🍴 {forks}" if forks > 0 else "—"

    lines.append(
        f"| {i} | [**{name}**]({url}){fork_label} | {desc} "
        f"| {lang_icon} `{lang}` | {star_str} | {fork_str} | `{pushed_str}` |"
    )

# ── Build top repo pin cards (exclude forks, top N by activity) ───────
lines.append("")
lines.append("### 🔥 Top Repos — Auto-picked by Latest Activity")
lines.append("")
lines.append('<div align="center">')
lines.append("")

top_repos = [r for r in repos if not r.get("fork")][:TOP_N_CARDS]

for j in range(0, len(top_repos), 2):
    pair = top_repos[j:j+2]
    for repo in pair:
        card = (
            f"https://github-readme-stats.vercel.app/api/pin/"
            f"?username={USERNAME}&repo={repo['name']}"
            f"&theme=tokyonight&hide_border=true&bg_color=050510"
            f"&title_color=c084fc&icon_color=818cf8&text_color=e2e8f0&border_radius=12"
        )
        lines.append(f'<a href="{repo["html_url"]}">')
        lines.append(f'  <img align="center" src="{card}" />')
        lines.append(f'</a>')
        lines.append("&nbsp;")
    lines.append("<br/><br/>")

lines.append("")
lines.append("</div>")

new_section = "\n".join(lines)

# ── Read README and inject new section ───────────────────────────────
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

if START_TAG not in content or END_TAG not in content:
    print(f"❌ ERROR: Could not find project section tags in {README_PATH}")
    print(f"   Add these tags to README.md:\n   {START_TAG}\n   {END_TAG}")
    exit(1)

before  = content.split(START_TAG)[0]
after   = content.split(END_TAG)[1]
updated = f"{before}{START_TAG}\n{new_section}\n{END_TAG}{after}"

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(updated)

print(f"✅ README.md updated successfully!")
print(f"   📊 {len(repos)} repos in table")
print(f"   📌 {len(top_repos)} repo cards generated")
print(f"   🕐 Timestamp: {now_utc}")
