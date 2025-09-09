from manim import *

SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"
GOLD = "#D4AF37"  # <- Add this here, since you're using GOLD in intro

def intro_scene(scene):
    stars = scene.create_starfield_parallax()
    scene.add(stars)
    
    # ImransLab logo reveal with glow effect
    logo = Text("ImransLab", font_size=72, color=GOLD)
    logo.shift(UP * 0.5)
    glow = logo.copy().set_color(YELLOW).set_opacity(0.2).scale(1.1)
    
    tagline = Text("Space Systems Engineering", font_size=28, color=SILVER)
    tagline.next_to(logo, DOWN, buff=0.3)
    
    # Animate stars moving for parallax effect
    star_animations = [star.animate.shift(LEFT * star.depth * 0.5) for star in stars]
    
    scene.play(
        LaggedStart(
            Write(glow, run_time=1.5),
            Write(logo, run_time=2),
            FadeIn(tagline, shift=UP),
            LaggedStart(*star_animations, lag_ratio=0.01),
            run_time=3
        )
    )
    scene.wait(1)
    
    # Title reveal with JWST silhouette
    title = Text("JWST: Unfolding in Space 2D Cinematic Video", font_size=56, color=GOLD)
    subtitle = Text("Deployment Sequence", font_size=32, color=WHITE)
    subtitle.next_to(title, DOWN, buff=0.4)
    
    # Create a more detailed JWST silhouette
    jwst_silhouette = scene.create_jwst_model_silhouette().scale(0.8)
    jwst_silhouette.next_to(subtitle, DOWN, buff=0.8)
    
    # Camera movement for dramatic effect
    scene.play(
        scene.camera.frame.animate.move_to(ORIGIN).scale(1.2),
        FadeOut(logo),
        FadeOut(glow),
        FadeOut(tagline),
        FadeIn(title, shift=UP),
        FadeIn(subtitle),
        run_time=2.5
    )
    scene.wait(0.5)
    
    # Animate JWST silhouette unfolding with glow
    scene.play(
        DrawBorderThenFill(jwst_silhouette),
        jwst_silhouette.animate.set_color(WHITE).set_fill(opacity=0.8),
        run_time=2.5
    )
    
    # Add a glow effect to the silhouette
    silhouette_glow = jwst_silhouette.copy().set_color(ACCENT_BLUE).set_opacity(0.3).scale(1.1)
    scene.add(silhouette_glow)
    scene.play(
        silhouette_glow.animate.scale(1.05).set_opacity(0.5),
        run_time=1.5
    )
    scene.wait(1)
    
    # Transition to main content with camera zoom
    scene.play(
        FadeOut(title),
        FadeOut(subtitle),
        FadeOut(jwst_silhouette),
        FadeOut(silhouette_glow),
        *[FadeOut(star) for star in stars],
        scene.camera.frame.animate.move_to(ORIGIN).scale(1),
        run_time=2.5
    )
