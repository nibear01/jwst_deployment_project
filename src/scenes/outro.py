import numpy as np
from manim import *
SILVER = "#C0C0C0"
LIGHT_METAL = "#E6E6E6"
DEEP_BLUE = "#0B1426"

def outro_scene(scene):
        """Cinematic outro with credits and zoom effect"""
        # Create starfield for background
        stars = scene.create_starfield_parallax()
        scene.add(stars)
        
        # Credits with better styling
        credits = VGroup(
            Text("JWST Deployment Animation", font_size=42, color=GOLD),
            Text("Created with Manim CE", font_size=28, color=WHITE),
            Text("ImransLab - Space Systems Engineering", font_size=24, color=SILVER),
            Text("V2.0 - Enhanced Cinematic Edition", font_size=20, color=LIGHT_METAL)
        )
        
        credits.arrange(DOWN, buff=0.5)
        
        # Add a background to credits
        credits_bg = Rectangle(
            width=credits.width + 1,
            height=credits.height + 0.8,
            color=DEEP_BLUE,
            fill_opacity=0.9,
            stroke_color=GOLD,
            stroke_width=3
        )
        credits_bg.move_to(credits.get_center())
        
        # Animate credits with star movement
        scene.play(
            FadeIn(credits_bg),
            FadeIn(credits, shift=UP),
            *[star.animate.shift(RIGHT * star.depth * 0.5) for star in stars],
            run_time=4
        )
        scene.wait(2)
        
        # Final logo with zoom effect
        final_logo = Text("ImransLab", font_size=64, color=GOLD)
        final_logo.move_to(ORIGIN)
        
        # Add glow to logo
        logo_glow = final_logo.copy().set_color(YELLOW).set_opacity(0.5).scale(1.1)
        
        scene.play(
            FadeOut(credits),
            FadeOut(credits_bg),
            FadeIn(logo_glow),
            FadeIn(final_logo, scale=1.5),
            run_time=2.5
        )
        scene.wait(1.5)
        
        # Zoom in effect on the logo
        scene.play(
            final_logo.animate.scale(1.8),
            logo_glow.animate.scale(1.9).set_opacity(0.2),
            scene.camera.frame.animate.move_to(ORIGIN).scale(0.7),
            run_time=3
        )
        scene.wait(2)
        
        # End with fade to black
        scene.play(
            FadeOut(final_logo),
            FadeOut(logo_glow),
            *[FadeOut(star) for star in stars],
            run_time=4
        )