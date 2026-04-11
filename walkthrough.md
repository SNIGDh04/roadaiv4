# 🚀 Beginner's Guide: GitHub & Deployment for ROADAI

This guide provides a total beginner's step-by-step path to getting your project online. I have already prepared the "Clean Export" folder for you.

---

## Part 1: Setting up GitHub

### 1. Create a GitHub Account
If you don't have one, go to [github.com](https://github.com/) and sign up.

### 2. Configure Git on your Machine
Open your terminal and run these two commands (replace with your info):
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### 3. Create a New Repository
1. Log in to GitHub.
2. Click the **+** icon in the top right corner and select **New repository**.
3. **Repository name**: `roadai-enterprise` (or anything you like).
4. Choose **Public** or **Private**.
5. **Do NOT** check any boxes like "Add a README" or ".gitignore" (I have already made these for you).
6. Click **Create repository**.

---

## Part 2: Pushing the Code to GitHub

Now, move into the folder I created and connect it to your new GitHub page.

1. **Open your terminal** and navigate to the clean folder:
   ```bash
   cd RoadAI_GitHub_Upload
   ```

2. **Link to your GitHub**: 
   (Copy the URL from your new GitHub repo page—it looks like `https://github.com/your-username/roadai-enterprise.git`)
   ```bash
   git remote add origin https://github.com/your-username/roadai-enterprise.git
   ```

3. **Rename your branch**:
   ```bash
   git branch -M main
   ```

4. **Upload (Push) the code**:
   ```bash
   git push -u origin main
   ```
   > [!NOTE]
   > If prompted for a password, GitHub now requires a **Personal Access Token (PAT)**. [Follow this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create one if you don't have it.

---

## Part 3: Deploying the Frontend (Vercel)

Vercel will host your **Dashboard UI**.

1. Go to [Vercel.com](https://vercel.com/) and sign up with your GitHub account.
2. Click **Add New** -> **Project**.
3. Find your `roadai-enterprise` repository and click **Import**.
4. **Build Settings**:
   - Vercel should detect the `vercel.json` I created.
   - If asked for "Root Directory," set it to `./` (the root).
5. Click **Deploy**.
6. Once finished, Vercel will give you a link (e.g., `roadai-xyz.vercel.app`). **Save this link.**

---

## Part 4: Deploying the Backend (Render)

Render will host your **FastAPI Engine** and run the **AI Models**.

1. Go to [Render.com](https://render.com/) and sign up with GitHub.
2. Click **New +** -> **Web Service**.
3. Connect your GitHub and select the `roadai-enterprise` repo.
4. **Configuration**:
   - **Environment**: Select `Docker` (Render will find the `Dockerfile` I made).
   - **Plan**: Select the best free/basic tier available.
5. **Environment Variables**:
   - Click "Advanced" and add `ROADAI_SECRET` with a random string.
6. Click **Create Web Service**.
7. Once it's "Live," Render will give you a URL (e.g., `https://roadai-backend.onrender.com`). **Copy this URL.**

---

## Part 5: Connecting them Together

Now that both are online, you need to tell the Frontend where the Backend is.

1. Open your local copy of `vercel.json` in the `git_export` folder.
2. Replace the placeholder URL in the `rewrites` section with your actual **Render** URL:
   ```json
   {
     "source": "/api/(.*)",
     "destination": "https://YOUR-RENDER-BACKEND-URL.onrender.com/api/$1"
   }
   ```
3. **Save, Commit, and Push again**:
   ```bash
   git add vercel.json
   git commit -m "Update backend URL"
   git push origin main
   ```
4. Vercel will automatically detect the change and redeploy your dashboard!

---

### 🎉 Congratulations!
Your ROADAI Enterprise platform is now live and accessible from anywhere in the world!
