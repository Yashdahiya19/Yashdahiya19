# ⚙️ Complete Setup Guide — Yash Dahiya's GitHub Profile
# ══════════════════════════════════════════════════════════════════════

## 📁 Files to Upload

Upload ALL these files to your `Yashdahiya19` profile repo:

```
Yashdahiya19/                          ← Your profile repo
│
├── README.md                          ← Main profile page
├── auto_update_projects.py            ← Python script for auto-project update
│
└── .github/
    └── workflows/
        ├── snake.yml                  ← Contribution snake animation
        ├── metrics.yml                ← 4 advanced metrics SVG cards
        ├── waka.yml                   ← WakaTime coding stats
        └── update-projects.yml        ← Auto-update projects table
```

---

## 🔑 Secrets You Need

Go to: **Your Repo → Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | How to Get It | Used By |
|---|---|---|
| `GITHUB_TOKEN` | ✅ Auto-provided by GitHub — no setup needed | snake.yml |
| `METRICS_TOKEN` | Create PAT at github.com/settings/tokens (scopes: `repo`, `read:user`, `read:org`) | metrics.yml |
| `GH_TOKEN` | Create PAT at github.com/settings/tokens (scope: `repo`) | update-projects.yml, waka.yml |
| `WAKATIME_API_KEY` | Get from wakatime.com/api-key after signing up | waka.yml |

---

## 🚀 Step-by-Step Activation

### ✅ STEP 1 — Create Profile Repo
1. Go to **github.com/new**
2. Repository name: **`Yashdahiya19`** (must match your GitHub username exactly!)
3. Set to **Public**
4. Check **"Add a README file"**
5. Click **Create repository**

---

### ✅ STEP 2 — Upload All Files
Upload `README.md` and `auto_update_projects.py` to the repo root.
Upload the 4 `.yml` files to `.github/workflows/` folder.

---

### ✅ STEP 3 — Create Secrets (Required for advanced features)

**For METRICS_TOKEN:**
1. Go to **github.com/settings/tokens/new** (classic token)
2. Note: `METRICS_TOKEN`
3. Select scopes: ✅ `repo` (full) → ✅ `read:user` → ✅ `read:org`
4. Click Generate token → copy immediately
5. Add as `METRICS_TOKEN` in repo secrets

**For GH_TOKEN:**
1. Go to **github.com/settings/tokens/new** (classic token)
2. Note: `GH_TOKEN`
3. Select scopes: ✅ `repo` (full)
4. Generate → copy → add as `GH_TOKEN` in repo secrets

**For WAKATIME_API_KEY:**
1. Sign up free at **wakatime.com**
2. Install **WakaTime extension** in VS Code (it auto-tracks everything)
3. Copy key from **wakatime.com/api-key**
4. Add as `WAKATIME_API_KEY` in repo secrets

---

### ✅ STEP 4 — Run Workflows (First Time)

Go to **Actions tab** in your repo and run each workflow once:

| Workflow | How to Run | What You Get |
|---|---|---|
| 🐍 Snake | Actions → Generate Snake → Run workflow | Snake SVG appears on profile |
| 📈 Metrics | Actions → GitHub Metrics → Run workflow | 4 SVG cards appear in repo |
| 📦 Projects | Actions → Auto-Update Projects → Run workflow | Projects table auto-fills |
| ⏱️ WakaTime | Actions → WakaTime Stats → Run workflow | Coding breakdown appears |

After first manual run, everything is **fully automatic** — no action needed from you!

---

## ✅ Full Feature Checklist

| # | Feature | Auto-Updates | Status |
|:---:|---|:---:|:---:|
| 1 | Animated venom header banner | — | ✅ Ready |
| 2 | JetBrains Mono typing SVG (7 lines) | — | ✅ Ready |
| 3 | Profile views counter (live) | ✅ Live | ✅ Ready |
| 4 | Followers badge (live) | ✅ Live | ✅ Ready |
| 5 | Stars badge (live) | ✅ Live | ✅ Ready |
| 6 | Open-to-work badge | — | ✅ Ready |
| 7 | Focus badge (AI/ML) | — | ✅ Ready |
| 8 | LinkedIn / Gmail / GitHub / Spotify links | — | ✅ Ready |
| 9 | Coding GIF (right-aligned) | — | ✅ Ready |
| 10 | Terminal bash-style About Me | — | ✅ Ready |
| 11 | Languages badges with proficiency levels | — | ✅ Ready |
| 12 | AI/ML stack badges | — | ✅ Ready |
| 13 | Frameworks & Tools badges | — | ✅ Ready |
| 14 | GitHub Stats card | ✅ Daily | ✅ Ready |
| 15 | Top Languages donut chart | ✅ Daily | ✅ Ready |
| 16 | Streak stats | ✅ Daily | ✅ Ready |
| 17 | Activity contribution graph (full width) | ✅ Daily | ✅ Ready |
| 18 | GitHub Trophies (all ranks) | ✅ Live | ✅ Ready |
| 19 | Contribution highlights card | ✅ Live | ✅ Ready |
| 20 | Advanced metrics — Base overview SVG | ✅ Daily | ⚙️ Run metrics.yml |
| 21 | Advanced metrics — Language deep dive SVG | ✅ Daily | ⚙️ Run metrics.yml |
| 22 | Advanced metrics — Achievements SVG | ✅ Daily | ⚙️ Run metrics.yml |
| 23 | Advanced metrics — Calendar heatmap SVG | ✅ Daily | ⚙️ Run metrics.yml |
| 24 | WakaTime coding breakdown | ✅ Daily | ⚙️ Run waka.yml |
| 25 | Auto-updating projects table (ALL repos) | ✅ Daily | ⚙️ Run update-projects.yml |
| 26 | Auto-picked repo pin cards (top 6) | ✅ Daily | ⚙️ Run update-projects.yml |
| 27 | Contribution snake (light + dark) | ✅ Daily | ⚙️ Run snake.yml |
| 28 | Learning roadmap | — | ✅ Ready |
| 29 | GitHub Skyline 3D links (2025 + 2026) | — | ✅ Ready |
| 30 | Dev quote of the day | ✅ Daily | ✅ Ready |
| 31 | Random dev meme | ✅ Daily | ✅ Ready |
| 32 | Spotify coding playlist | — | ✅ Ready |
| 33 | Automation hub workflows table | — | ✅ Ready |
| 34 | Connect section (GitHub + LinkedIn + Email) | — | ✅ Ready |
| 35 | Animated footer wave | — | ✅ Ready |
| 36 | Last Updated / Made With / Since / Location badges | — | ✅ Ready |

---

## 💡 Pro Tips

- **Add descriptions to your repos** — the auto-update script pulls them into the projects table
- **Commit daily** — keeps your streak alive and snake looking impressive
- **WakaTime** is the #1 thing recruiters notice — set it up first!
- **Star your own repos** once they're mature — it helps trophies level up
- After creating a new repo, go to **Actions → Auto-Update Projects → Run workflow** to see it immediately on your profile
