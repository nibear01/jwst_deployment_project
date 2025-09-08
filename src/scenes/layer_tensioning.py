"""Sunshield layer-by-layer tensioning (1 -> 5) with labels and HUD updates."""
from manim import *
from utils.animations import tension_layers, camera_move
from utils.constants import SUNSHIELD_LAYERS


def add_layer_tensioning(scene, telescope, hud=None):
    """Tension the sunshield layers sequentially and update HUD layer counter."""
    # Recreate the layers in case they're not passed in (safe fallback)
    base_x = telescope.get_center()[0]
    layers = VGroup()
    for i in range(SUNSHIELD_LAYERS):
        rect = RoundedRectangle(width=3.2 - i * 0.05, height=0.16, corner_radius=0.04)
        rect.set_fill("#cfa967", 1).set_stroke(WHITE, 0.4)
        rect.next_to(telescope, DOWN, buff=0.06 + i * 0.02)
        rect.set_opacity(0.25)
        layers.add(rect)
        scene.add(rect)

    # Camera zoom to sunshield
    camera_move(scene, telescope.get_center() + DOWN * 0.8, scale=1.05, run_time=1.0)

    # Tension each layer one by one and update HUD
    for idx, layer in enumerate(layers, start=1):
        # animate tension for single layer
        scene.play(
            layer.animate.set_opacity(1).scale(1.02).shift(DOWN * 0.02),
            run_time=0.9
        )
        # update HUD tracker if available
        if hud and "layer_tracker" in hud:
            hud["layer_tracker"].set_value(idx)
        scene.wait(0.18)

    # final subtle full-shape relax
    scene.play(LaggedStart(*[l.animate.shift(UP * 0.01) for l in layers],
                           lag_ratio=0.05), run_time=1.0)
    scene.wait(0.2)
