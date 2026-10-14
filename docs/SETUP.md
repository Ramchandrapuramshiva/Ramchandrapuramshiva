# 🚀 Setup, Deployment, & Regeneration Guide

Welcome to your custom GitHub Profile Portfolio! This guide explains how GitHub profile READMEs work, how to publish these files to your account, how the automated animations operate, and how you can regenerate or customize everything anytime.

---

## 📌 1. How GitHub Profile READMEs Work

GitHub has a special feature: when you create a **public repository** whose name **exactly matches** your GitHub username (`Ramchandrapuramshiva/Ramchandrapuramshiva`), GitHub will automatically render the repository's `README.md` at the very top of your public profile page!

> [!IMPORTANT]
> - Repository Name: `Ramchandrapuramshiva`
> - Visibility: **Must be Public**
> - Branch: `main`

---

## 📁 2. Workspace File Architecture

```text
c:\Users\HP\OneDrive\Desktop\Git hub\
├── README.md                          # The live profile document displayed on your GitHub profile
├── assets/
│   ├── terminal-animation.gif         # 66 KB ultra-lightweight animated terminal GIF
│   ├── terminal-animation-source.py   # Reproducible Python source script using Pillow
│   ├── typing-header.svg              # Pure vector SVG cycling typewriter header
│   └── contribution-snake-preview.svg # Local fallback preview before GitHub Actions runs
├── .github/
│   └── workflows/
│       └── snake.yml                  # GitHub Actions workflow for Platane/snk
└── docs/
    └── SETUP.md                       # This beginner-friendly deployment & maintenance guide
```

---

## ⚙️ 3. One-Time GitHub Actions Permissions Setup

To allow the automated Contribution Snake workflow to generate your snake SVGs and push them to the `output` branch:

1. Open your repository on GitHub: `https://github.com/Ramchandrapuramshiva/shiva-github-portfolio`
2. Click on **Settings** (top tab).
3. In the left sidebar, click on **Actions** ➔ **General**.
4. Scroll down to **Workflow permissions**.
5. Select: **"Read and write permissions"**.
6. Check the box: **"Allow GitHub Actions to create and approve pull requests"**.
7. Click **Save**.

---

## 🐍 4. How the Contribution Snake Works

1. The file `.github/workflows/snake.yml` is configured to run:
   - **Automatically every 24 hours** at midnight UTC.
   - **Whenever you push changes** to `main`.
   - **Manually** from the GitHub **Actions** tab whenever you want.
2. It fetches your real GitHub contribution graph using the official `Platane/snk@v3` action.
3. It packages the generated animations (`github-contribution-grid-snake-dark.svg`, light SVG, and GIF) and pushes them to a clean orphan branch named `output`.
4. Your `README.md` automatically loads the dark SVG for dark mode users and light SVG for light mode users, with `assets/contribution-snake-preview.svg` as a reliable initial fallback.

### Manually Running the Snake Workflow:
1. Go to `https://github.com/Ramchandrapuramshiva/shiva-github-portfolio/actions`.
2. Click **Generate Contribution Snake Animation** in the left menu.
3. Click the **Run workflow** dropdown on the right and click the green **Run workflow** button.
4. Wait ~45 seconds until the checkmark turns green.

---

## 🎨 5. How to Regenerate or Update the Terminal GIF

Whenever you learn a new technology or launch a new project:

1. Open `assets/terminal-animation-source.py`.
2. Edit the command outputs or add new commands in simple text lines.
3. Run the generator in your terminal:
   ```powershell
   py assets/terminal-animation-source.py
   ```
4. The script automatically updates `assets/terminal-animation.gif` with optimal palette quantization and smooth frame delays (~66 KB).
5. Commit and push the updated GIF to GitHub!

---

## 📤 6. Step-by-Step Publishing Instructions

When you are ready to publish:

### Step A: Initialize Git in your workspace folder
```powershell
git init -b main
```

### Step B: Stage and Commit the files
```powershell
git add .
git commit -m "feat: initial release of animated profile command center"
```

### Step C: Link to your GitHub repository
```powershell
git remote add origin https://github.com/Ramchandrapuramshiva/shiva-github-portfolio.git
```

### Step D: Push to GitHub
```powershell
git push -u origin main
```

---

## 🌟 7. How to Display This Directly on Your Main Profile Page (`github.com/Ramchandrapuramshiva`)

GitHub has a special feature where a README displays directly on your user profile page (`https://github.com/Ramchandrapuramshiva`) **only when the repository name matches your exact username (`Ramchandrapuramshiva`)**.

To activate this in 10 seconds:
1. Go to `https://github.com/Ramchandrapuramshiva/shiva-github-portfolio/settings`.
2. In the **Repository name** field at the top, change `shiva-github-portfolio` to `Ramchandrapuramshiva`.
3. Click **Rename**.
4. GitHub will automatically show your animated command center right at the top of your public profile page!
