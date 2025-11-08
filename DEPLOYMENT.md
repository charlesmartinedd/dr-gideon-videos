# GitHub Pages Deployment Guide

## Enable GitHub Pages

1. Visit: https://github.com/charlesmartinedd/dr-gideon-videos/settings/pages

2. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: master
   - **Folder**: / (root)

3. Click **Save**

4. Wait 1-2 minutes for deployment

5. Your landing page will be live at:
   **https://charlesmartinedd.github.io/dr-gideon-videos/**

## Adding Marketing Video

When the marketing video is ready:

1. Add the video file to the repository:
   ```bash
   cp /path/to/marketing-video.mp4 ./Marketing_Video.mp4
   ```

2. Update `index.html` - replace the placeholder section with:
   ```html
   <!-- Marketing Video -->
   <div id="marketing-video" class="video-content">
       <video controls>
           <source src="Marketing_Video.mp4" type="video/mp4">
           Your browser does not support the video tag.
       </video>
   </div>
   ```

3. Enable the Marketing Video button by removing `disabled`:
   ```html
   <button class="tab-button" onclick="showVideo('marketing')" id="marketingBtn">Marketing Video</button>
   ```

4. Commit and push:
   ```bash
   git add .
   git commit -m "Add marketing video"
   git push
   ```

## Current Features

- ✅ The Right Path branding (purple color scheme, logo)
- ✅ Two-tab navigation (ACSA Video active, Marketing Video placeholder)
- ✅ Video at 80% screen width
- ✅ No scrolling, clean single-page design
- ✅ Responsive for mobile devices
- ✅ Video plays directly from file (no external hosting)
- ✅ Auto-pause when switching tabs

## Landing Page URL

Once GitHub Pages is enabled, share:
**https://charlesmartinedd.github.io/dr-gideon-videos/**
