import numpy as np
from manim import *
SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"    

def sunshield_deployment(scene):
    """Cinematic JWST sunshield deployment sequence with camera work"""
    # Create JWST model
    jwst = scene.create_jwst_model()
    sunshield_layers, primary_mirror, secondary_system, bus, bus_details, dta_tower, solar_panel, antenna = jwst

    # --- INITIAL STATE ---
    for layer in sunshield_layers:
        layer.scale(0.15).set_opacity(0.4)
    primary_mirror.scale(0.5).set_opacity(0.8)
    secondary_system.scale(0.5).set_opacity(0.8)
    solar_panel.scale(0.6).set_opacity(0.5)

    scene.add(jwst)

    # Camera cinematic intro shot
    scene.play(
        scene.camera.frame.animate.move_to(jwst.get_center()).scale(1.25),
        run_time=3,
        rate_func=smooth
    )
    scene.wait(0.5)

    # --- SOLAR PANEL DEPLOYMENT ---
    scene.play(
        solar_panel.animate.scale(1.4).set_opacity(1),
        scene.camera.frame.animate.move_to(jwst.get_center()).scale(1.15),
        run_time=2.5,
        rate_func=smooth
    )

    # --- DTA EXTENSION WITH GLOW ---
    dta_glow = dta_tower.copy().set_color(ACCENT_BLUE).set_opacity(0.25)
    scene.add(dta_glow)
    scene.play(
        # mirror_boom.animate.stretch(2.5, 1, about_point=bus.get_top()),
        dta_tower.animate.stretch(2.3, 1, about_point=bus.get_top()),
        dta_glow.animate.stretch(2.3, 1, about_point=bus.get_top()).set_opacity(0.05),
        scene.camera.frame.animate.move_to(jwst.get_center()).scale(1.0),
        run_time=3,
        rate_func=smooth
    )
    scene.remove(dta_glow)

    # --- SUNSHIELD DEPLOYMENT ---
    deploy_anims = []
    glow_layers = VGroup()

    for i, layer in enumerate(sunshield_layers):
        layer.set_opacity(0.4)
        glow = layer.copy().set_color(ACCENT_BLUE).set_opacity(0.15)
        glow_layers.add(glow)

        deploy_anims.append(
            Succession(
                FadeIn(layer, scale=0.3),
                layer.animate.scale(4).set_opacity(0.9).shift(DOWN * 0.15 * i),
                lag_ratio=0.3
            )
        )

    scene.add(glow_layers)
    scene.play(
        LaggedStart(*deploy_anims, lag_ratio=0.25),
        glow_layers.animate.scale(4.2).set_opacity(0.05),
        scene.camera.frame.animate.move_to(jwst.get_center() + DOWN * 0.5).scale(0.9),
        run_time=5
    )
    scene.remove(glow_layers)

    # --- MID-BOOM EXTENSION (TENSIONING) ---
    scene.play(
        sunshield_layers.animate.stretch(1.25, 0, about_point=sunshield_layers.get_center()),
        scene.camera.frame.animate.move_to(jwst.get_center() + UP * 0.3).scale(0.85),
        run_time=2
    )

    # --- LAYER HIGHLIGHTING ---
    for i, layer in enumerate(sunshield_layers):
        label = Text(f"Layer {i+1}", font_size=20, color=WHITE)
        label.next_to(layer.get_corner(UR), UR, buff=0.1)

        glow = layer.copy().set_color(ACCENT_BLUE).set_opacity(0.3)
        scene.add(glow)

        scene.play(
            FadeIn(label, shift=UP*0.2),
            layer.animate.set_opacity(1).scale(1.05),
            glow.animate.scale(1.1).set_opacity(0.05),
            run_time=1
        )
        scene.play(FadeOut(label), FadeOut(glow), run_time=0.6)

    # --- CINEMATIC OUTRO SHOT ---
    final_glow = sunshield_layers.copy().set_color(ACCENT_BLUE).set_opacity(0.08)
    scene.add(final_glow)
    scene.play(
        scene.camera.frame.animate.move_to(jwst.get_center()).scale(0.9),
        run_time=3
    )
    scene.wait(2)
    scene.remove(final_glow)

