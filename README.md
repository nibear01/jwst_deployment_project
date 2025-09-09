# JWST Deployment Animation (Manim Project)

## 🌌 Overview

This project is a **cinematic visualization of the James Webb Space Telescope (JWST) deployment sequence**, built using the [Manim Community Edition](https://docs.manim.community). It accurately simulates the complex deployment process of JWST with technical precision while maintaining visual appeal and educational value.

The animation features:
- **Sunshield deployment** with 5 distinct layers
- **Secondary mirror deployment** with tripod structure
- **Primary mirror deployment** with 18 hexagonal segments
- **Journey to L2 orbit** with scientific explanation
- **Cinematic intro and outro sequences** with professional transitions
- **Realistic starfield & nebula space background**
- **Voice narration** explaining the deployment process and significance

---

## 👥 Team Members & Contributions

### Nasemul Haque
**Role:** Introduction and Outro Animation
- Created cinematic intro and outro sequences
- Implemented SVG logo animation with glowing effects
- Designed stylish text animations
- Developed dynamic starfield background

### Naved Abrar Nibir
**Role:** Sunshield Deployment Animation
- Implemented the multi-layered kite-shaped sunshield deployment
- Created realistic folding and unfolding animations with proper rotation points

### Bushra Jahan
**Role:** L2 Explainer Scene
- Developed the Sun-Earth L2 Lagrange point explanation
- Implemented Earth's orbit animation around the Sun

### Saifur Rahman
**Role:** Primary Mirror Enhancement
- Enhanced primary mirror deployment animation with overshoot and settle effects
- Added sweeping highlights and sparkle effects across segments
- Improved camera transitions and visual polish

### Rakib Hasan
**Role:** Project Management & Documentation
- Created project documentation and presentation materials
- Coordinated task division among team members
- Ensured project deadlines were met

---

## 📂 Project Structure

```
│── src/
│   ├── main.py                 # Master scene entry point
│   ├── scenes/                 # Individual deployment scenes
│   │   ├── intro.py           # Introduction sequence
│   │   ├── sunshield.py       # Sunshield deployment animation
│   │   ├── secondary_mirror.py # Secondary mirror deployment
│   │   ├── primary_mirror.py  # Primary mirror deployment
│   │   ├── l2_explainer.py    # L2 point explanation
│   │   ├── outro.py           # Outro sequence
│   │
│   ├── utils/                 # Helper functions and constants
│   │   ├── animations.py      # Custom animation functions
│   │   ├── constants.py       # Project constants and configurations
│   │
│── assets/
│   ├── jwst_voice.mp3         # Narration / voice-over file
│   ├── music/                 # Background music (optional)
│   ├── images/                # Reference images and textures
│
│── output/                    # Rendered animation files
│── README.md                  # Project documentation
│── requirements.txt           # Python dependencies
│── PROMPTS.md                 # AI reference prompts used
│── presentation.pptx          # Project presentation
```

---

## ⚙️ Setup & Installation

### Prerequisites
- **Python** ≥ 3.9
- **FFmpeg** (for audio/video processing)
- **Manim Community Edition** ≥ 0.19.0
- **NumPy**
- **gTTS** (for text-to-speech, if needed)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jwst-animation
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify FFmpeg installation**
   ```bash
   ffmpeg -version
   ```

---

## 🚀 How to Run

### Render the complete animation:
```bash
manim -pqh src/main.py MasterScene
```

### Render specific scenes:
```bash
manim -pqh src/scenes/sunshield.py SunshieldDeployment
```

### Command flags:
- `-p` → Preview after rendering
- `-q` → Quality setting (l=low, m=medium, h=high, k=4K)
- `-h` → High quality render

---

## 🎬 Animation Features

### Scene Breakdown:
1. **Intro Sequence** - Title reveal with JWST silhouette against starfield
2. **Sunshield Deployment** - 5-layer kite-shaped sunshield unfolding
3. **Secondary Mirror Deployment** - Tripod structure extension with mirror
4. **Primary Mirror Deployment** - 18 gold hexagonal mirrors unfolding
5. **L2 Journey & Explanation** - Telescope traveling to orbit with scientific explanation
6. **Outro Sequence** - Glowing JWST logo with credits fade-out

### Technical Highlights:
- Realistic space background with parallax starfield & nebula
- Accurate JWST model components: mirrors, sunshield, bus, solar panel, antenna
- Cinematic transitions between deployment stages
- Voice narration synchronized with visual elements
- Modular scene structure for easy maintenance and extensions

---

## 🎵 Audio Integration

The animation includes voice narration that can be added with:

```python
self.add_sound("assets/jwst_voice.mp3", time_offset=0.0)
```

Replace `jwst_voice.mp3` with your custom audio file if needed. Audio should be placed in the `assets/` directory.

---

## 🎨 Visual Design

### Color Scheme:
- Mirrors: Gold (#D4AF37)
- Sunshield: Alternating light/dark metallics
- Space Background: Deep blues with star highlights
- Text: White with high contrast

### Animation Techniques:
- MovingCameraScene camera movements (pan/zoom)
- Bezier/parametric paths with MoveAlongPath
- ValueTracker with updaters for HUD elements
- Hinge rotations with precise about_points
- Parallax layers for depth effect
- Reveals and transitions (FadeIn, FadeOut, Transform, LaggedStart)

---

## 📝 Notes & Best Practices

1. Ensure your virtual environment is active before running Manim
2. Verify FFmpeg is installed and accessible in PATH for MP4 rendering
3. For customizations, modify parameters in `utils/constants.py`
4. Reference images and technical specs are available in `assets/images/`
5. Maintain the project structure for consistency across team members

---

## 🔗 References

- JWST Deployment & Operations Video: https://youtu.be/aICaAEXDJQQ
- NASA JWST Technical Documentation
- Lagrange Points Explanatory Materials
- Manim Community Documentation: https://docs.manim.community

---

## 📄 License

This project is created for educational purposes as part of a team assignment. All JWST design and technical details are based on publicly available NASA resources.

---

## 👏 Acknowledgments

Special thanks to:
- NASA for making JWST technical details publicly available
- The Manim community for excellent documentation and support
- Our instructors for guidance and feedback throughout the project

For questions or contributions, please contact the team members listed above.
