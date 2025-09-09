from manim import *
import numpy as np

SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"
GOLD = "#D4AF37"  # <- Add this here, since you're using GOLD in intro

def intro_scene(scene):
    stars = scene.create_starfield_parallax()
    scene.add(stars)
    
    # Line-art logo
    svg_logo = SVGMobject("assets/logo.svg")
    svg_logo.set_fill(opacity=0).set_stroke(color=GOLD, width=6)
    svg_logo.scale(1.2).shift(UP * 0.5)

    # Collect drawable subpaths and sort them
    parts = [m.copy().set_fill(opacity=0).set_stroke(GOLD, width=6)
             for m in svg_logo.family_members_with_points()
             if len(m.get_points()) > 0]
    parts.sort(key=lambda p: (np.round(p.get_center()[0], 2), np.round(p.get_center()[1], 2)))
    parts_group = VGroup(*parts)

    # Soft glow behind the strokes
    glow = parts_group.copy().set_stroke(GOLD, width=14, opacity=0.18)
    scene.add(glow)

    name = Text("ImransLab", font_size=48, color=GOLD)
    name.next_to(parts_group, DOWN, buff=0.3)

    tagline = Text("Learn Anything and Everything", font_size=28, color=SILVER)
    tagline.next_to(name, DOWN, buff=0.2)
    
    # Animate stars moving
    star_animations = [star.animate.shift(LEFT * star.depth * 0.5) for star in stars]
    
    # Draw each subpath sequentially 
    scene.play(
        AnimationGroup(
            Succession(*[Create(p) for p in parts]),
            LaggedStart(*star_animations, lag_ratio=0.01),
            lag_ratio=0
        ),
        run_time=2.6
    )
    scene.play(FadeIn(name, shift=UP), FadeIn(tagline, shift=UP * 0.25))
    scene.wait(1)
    
    # Title reveal with JWST silhouette
    title_line1 = Text("JWST: Unfolding in Space", font_size=56, color=GOLD)
    title_line2 = Text("2D Cinematic Video", font_size=56, color=GOLD)
    title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.2)
    title.move_to(ORIGIN)
    subtitle = Text("Deployment Sequence", font_size=32, color=WHITE)
    subtitle.next_to(title, DOWN, buff=0.4)
    
    # Camera movement for dramatic effect
    scene.play(
        scene.camera.frame.animate.move_to(ORIGIN).scale(1.2),
        FadeOut(parts_group),  # updated
        FadeOut(glow),         # updated
        FadeOut(name),
        FadeOut(tagline),
        FadeIn(title, shift=UP),
        FadeIn(subtitle),
        run_time=2.5
    )
    scene.play(
        FadeOut(title, shift=UP),
        FadeOut(subtitle),
        run_time=2.5
    )
    scene.wait(0.5)
