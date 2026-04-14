# Auto-Update Projects Setup - Yashdahiya19 Repo
Status: 🚀 In Progress

## Approved Plan Steps

### 1. Setup Git & Branch ✅ **DONE**  
```
git init
git remote add origin https://github.com/Yashdahiya19/Yashdahiya19.git
git checkout -b blackboxai/auto-update-setup
git add .
git commit -m "📦 Add auto-update projects workflow (auto_update_projects.py + update-projects.yml)"
git push -u origin blackboxai/auto-update-setup
```
*Pending execution*
- Verify/add git remote: `https://github.com/Yashdahiya19/Yashdahiya19.git`
- `git checkout -b blackboxai/auto-update-setup`
- `git add .`
- `git commit -m "📦 Add auto-update projects workflow (auto_update_projects.py + update-projects.yml)"`
- `git push -u origin blackboxai/auto-update-setup`

### 2. Verify GitHub CLI & Create PR [PENDING]
- Check/install `gh`
- `gh pr create --title "📦 Add auto-update projects workflow" --body "Auto-populates README projects from GitHub API daily. See README setup instructions."`

### 3. User Actions [PENDING - MANUAL]
- Add `GH_TOKEN` secret (PAT with repo:public_repo scope) in repo Settings > Secrets > Actions
- Merge PR
- Go to Actions > 📦 Auto-Update Projects > Run workflow
- ✅ Verify README projects section updates

### 4. Completion [PENDING]
- Test workflow output
- Close task

*Updated: $(date)
