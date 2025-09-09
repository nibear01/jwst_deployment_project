# Project Documentation

# JWST Deployment Animation (Manim Project)

## 🌌 Overview
This project is a **cinematic visualization of the James Webb Space Telescope (JWST) deployment sequence**, built using the [Manim Community Edition](https://docs.manim.community).  

It simulates:
- **Sunshield deployment**
- **Secondary mirror deployment**
- **Primary mirror deployment**
- **Journey to L2 orbit**
- **Intro and Outro sequences with cinematic transitions**
- A **realistic starfield & nebula space background**

The animation is narrated (via `jwst_voice.mp3`) to explain how the telescope works and why it matters.

---

## 📂 Folder Structure

```
│── src/
│ ├── main.py # Master scene entry point
│ ├── scenes/ # Contains individual deployment scenes
│ │ ├── intro.py
│ │ ├── sunshield.py
│ │ ├── secondary_mirror.py
│ │ ├── primary_mirror.py
│ │ ├── l2_explainer.py
│ │ ├── outro.py
│ │
│ ├── utils/ # Helper functions and constants
│ │ ├── animations.py
│ │ ├── constants.py
│ │
│── assets/
│ ├── jwst_voice.mp3 # Narration / voice-over file
│ ├── music/ # (Optional) Background music
│ ├── images/ # Reference or textures if needed
│
│── README.md # Project documentation
│── requirements.txt # Python dependencies
```


---

## ⚙️ Requirements

- **Python** ≥ 3.9
- **Manim Community Edition** ≥ 0.19.0  
- **NumPy**  
- **gtts
- **FFmpeg** (for rendering mp4 with sound)

Install requirements with:
```bash
pip install -r requirements.txt


## ▶️ Running the Project

To render the full cinematic sequence:

manim -pqh src/main.py MasterScene


-p → preview after render

-q → quality (l=low, m=medium, h=high, k=4K)

Example for high-quality render:

manim -pqh src/main.py MasterScene


## 🎬 Features

### ✅ Realistic space background with parallax starfield & nebula
### ✅ JWST model (mirrors, sunshield, bus, solar panel, antenna, etc.)
### ✅ Cinematic transitions between deployment stages
### ✅ Voice narration with jwst_voice.mp3
### ✅ Modular scenes (intro, deployments, outro)


##📖 Scenes Explained

### Intro → Title and silhouette of JWST with starfield
### Sunshield Deployment → 5-layer kite-shaped sunshield unfolds
### Secondary Mirror Deployment → Tripod + mirror animation
### Primary Mirror Deployment → 18 gold hexagonal mirrors unfold
### Journey to L2 → Telescope shown traveling towards orbit
### Outro → Glowing JWST logo with fade-out


##🎵 Audio Integration

###The line:

self.add_sound("jwst_voice.mp3", time_offset=0.0)

adds narration at the start. Replace with your own narration if needed.

