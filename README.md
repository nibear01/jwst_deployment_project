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

## ⚙️ Setup & Requirements

- **Python** ≥ 3.9  
- **Manim Community Edition** ≥ 0.19.0  
- **NumPy**  
- **gtts**  
- **FFmpeg** (for rendering mp4 with sound)

### 1️⃣ Create & Activate Virtual Environment

```bash
# Create a virtual environment
python -m venv venv
```


# Activate on Windows
```
venv\Scripts\activate
```

# Activate on macOS/Linux
```
source venv/bin/activate
```

# Install Requirements
```
pip install manim numpy gtts
```

# Running the Project

Render the full cinematic sequence:

```
manim -pqh main.py MasterScene
```

Flags:

-p → preview after render

-q → quality (l=low, m=medium, h=high, k=4K)

Example for high-quality render:

```
manim -pqh main.py MasterScene
```


🎬 Features

# Realistic space background with parallax starfield & nebula

## JWST model: mirrors, sunshield, bus, solar panel, antenna, etc.

## Cinematic transitions between deployment stages

## Voice narration via jwst_voice.mp3

## Modular scene structure: intro, deployments, outro


# Intro → Title and JWST silhouette with starfield

## Sunshield Deployment → 5-layer kite-shaped sunshield unfolds

## Secondary Mirror Deployment → Tripod + mirror animation

## Primary Mirror Deployment → 18 gold hexagonal mirrors unfold

## Journey to L2 → Telescope travels to orbit

## Outro → Glowing JWST logo with fade-out


# 🎵 Audio Integration

Add narration with:

```
self.add_sound("jwst_voice.mp3", time_offset=0.0)
```

Replace jwst_voice.mp3 with your own audio if needed.

# 📝 Notes

## Make sure your virtual environment is active before running Manim

## Ensure FFmpeg is installed and accessible in PATH for mp4 rendering