"""Sunshield pallets release + stacked folded sunshield visual."""
from manim import *
from utils.animations import rotate_about, camera_move
from utils.constants import SUNSHIELD_COLORS, SUNSHIELD_LAYERS


def _make_layer(index, width=3.6, height=0.18):
    """Return one sunshield layer as a rounded rectangle."""
    r = RoundedRectangle(width=width, height=height, corner_radius=0.05)
    color = SUNSHIELD_COLORS[index % len(SUNSHIELD_COLORS)]
    r.set_fill(color, 1).set_stroke(width=0.6, color=WHITE, opacity=0.4)
    return r


def add_sunshield_sequence(scene, telescope, hud=None):
    """Animate pallets release and initial folded sunshield reveal.

    telescope: shared VGroup (bus, mirror_stub, sunshield_stub)
    hud: dict from setup_hud for trackers (optional)
    """
    # position telescope center-ish
    telescope.move_to(ORIGIN)

    # pallets: two small rectangles at sunward edge
    pallet_left = Rectangle(width=0.5, height=0.25).next_to(telescope, DOWN, buff=0.05)
    pallet_right = pallet_left.copy().next_to(pallet_left, RIGHT, buff=0.6)
    pallet_left.set_fill("#6b6b6b", 1).set_stroke(WHITE, 0.6)
    pallet_right.set_fill("#6b6b6b", 1).set_stroke(WHITE, 0.6)

    # create folded layers stacked beneath the telescope (collapsed)
    layers = VGroup(*[
        _make_layer(i, width=3.6 - i * 0.08, height=0.16)
        for i in range(SUNSHIELD_LAYERS)
    ])
    # stack them slightly offset and tucked under the bus
    for i, layer in enumerate(layers):
        layer.next_to(telescope, DOWN, buff=0.06 + i * 0.02)
        layer.set_opacity(0.2)

    sun = Circle(radius=0.6).set_fill(YELLOW, 1).set_stroke(width=0)
    sun.to_edge(LEFT, buff=1.0)

    scene.play(FadeIn(sun, shift=LEFT * 0.4), run_time=0.8)
    scene.play(FadeIn(telescope), FadeIn(pallet_left), FadeIn(pallet_right),
               run_time=0.8)
    scene.wait(0.3)

    # cinematic camera approach
    camera_move(scene, telescope.get_center(), scale=0.9, run_time=1.2,
                rate_func=smooth)

    # pallets release (slide away) with small bounce
    scene.play(pallet_left.animate.shift(LEFT * 2.2).scale(0.95),
               pallet_right.animate.shift(RIGHT * 2.2).scale(0.95),
               run_time=1.1, rate_func=there_and_back)
    scene.wait(0.15)

    # reveal folded layers - quick ripple
    reveal_anims = []
    for i, layer in enumerate(layers):
        reveal_anims.append(layer.animate.set_opacity(0.9).shift(DOWN * (0.08 + i * 0.02)))
    scene.play(LaggedStart(*reveal_anims, lag_ratio=0.12), run_time=1.2)
    scene.add(layers)
    scene.wait(0.25)

    # small outward fan to suggest pallet hinges free
    for layer in layers:
        scene.play(layer.animate.rotate(0.02), run_time=0.12)
    scene.wait(0.2)
