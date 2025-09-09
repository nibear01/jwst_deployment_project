import numpy as np
from manim import *
SILVER = "#C0C0C0"
LIGHT_METAL = "#E6E6E6"
DEEP_BLUE = "#0B1426"
GOLD = "#D4AF37"  # match intro.py

def outro_scene(scene):
        """Cinematic outro with credits and zoom effect"""
        # Create starfield for background
        stars = scene.create_starfield_parallax()
        scene.add(stars)
        
        # Credits with better styling (unchanged)
        credits = VGroup(
            Text("JWST Deployment Animation", font_size=42, color=GOLD),
            Text("Created with Manim CE", font_size=28, color=WHITE),
            Text("ImransLab - Learn Anything and Everything", font_size=24, color=SILVER),
            Text("V2.0 - Enhanced Cinematic Edition", font_size=20, color=LIGHT_METAL)
        )
        credits.arrange(DOWN, buff=0.5)
        credits_bg = Rectangle(
            width=credits.width + 1,
            height=credits.height + 0.8,
            color=DEEP_BLUE,
            fill_opacity=0.9,
            stroke_color=GOLD,
            stroke_width=3
        ).move_to(credits.get_center())
        
        scene.play(
            FadeIn(credits_bg),
            FadeIn(credits, shift=UP),
            *[star.animate.shift(RIGHT * star.depth * 0.5) for star in stars],
            run_time=4
        )
        scene.wait(2)
        
        # Replace text logo with SVG logo line-art (like intro.py)
        scene.play(FadeOut(credits), FadeOut(credits_bg), run_time=1.0)
        svg_logo = SVGMobject("assets/logo.svg")
        svg_logo.set_fill(opacity=0).set_stroke(color=GOLD, width=6)
        svg_logo.scale(1.2).shift(UP * 0.3)

        parts = [m.copy().set_fill(opacity=0).set_stroke(GOLD, width=6)
                 for m in svg_logo.family_members_with_points()
                 if len(m.get_points()) > 0]
        parts.sort(key=lambda p: (np.round(p.get_center()[0], 2),
                                  np.round(p.get_center()[1], 2)))
        parts_group = VGroup(*parts)
        glow = parts_group.copy().set_stroke(GOLD, width=14, opacity=0.18)
        scene.add(glow)

        name = Text("ImransLab", font_size=48, color=GOLD).next_to(parts_group, DOWN, buff=0.3)
        tagline = Text("Learn Anything and Everything", font_size=28, color=SILVER).next_to(name, DOWN, buff=0.2)

        star_animations = [star.animate.shift(RIGHT * star.depth * 0.5) for star in stars]
        scene.play(
            AnimationGroup(
                Succession(*[Create(p) for p in parts]),
                LaggedStart(*star_animations, lag_ratio=0.01),
                lag_ratio=0
            ),
            run_time=2.6
        )
        scene.play(FadeIn(name, shift=UP), FadeIn(tagline, shift=UP * 0.25))
        scene.play(glow.animate.set_stroke(opacity=0.28).scale(1.02), run_time=1.2)

        # Fade to black
        scene.play(
            FadeOut(parts_group),
            FadeOut(glow),
            FadeOut(name),
            FadeOut(tagline),
            *[FadeOut(star) for star in stars],
            run_time=2.5
        )