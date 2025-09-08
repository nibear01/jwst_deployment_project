"""Helper animations & reusable widgets for scenes."""
from manim import *
import random
from utils.constants import (
    BACKGROUND_COLOR,
    BACKGROUND_SCALE,
    HUD_COLOR,
)

FRAME_WIDTH = config.frame_width * 2
FRAME_HEIGHT = config.frame_height * 2

def create_background(scene):
    """Create a large background, parallax stars, and subtle nebula.
    Background is kept centered on the camera frame to avoid cutoff
    while camera moves."""
    frame = scene.camera.frame
    bg = Rectangle(
        width=FRAME_WIDTH * BACKGROUND_SCALE,
        height=FRAME_HEIGHT * BACKGROUND_SCALE,
    )
    bg.set_fill(BACKGROUND_COLOR, 1).set_stroke(width=0)
    # Stars
    stars = VGroup()
    for _ in range(120):
        x = random.uniform(-FRAME_WIDTH * 1.6, FRAME_WIDTH * 1.6)
        y = random.uniform(-FRAME_HEIGHT * 1.6, FRAME_HEIGHT * 1.6)
        r = random.uniform(0.01, 0.035)
        dot = Dot(point=np.array([x, y, 0]), radius=r)
        dot.set_fill(WHITE, random.uniform(0.5, 1.0))
        dot.set_stroke(width=0)
        stars.add(dot)
    # Nebula (soft clouds)
    neb = VGroup()
    for s in [(-2.5, 0.5), (1.8, -0.8)]:
        neb_piece = Ellipse(width=6, height=2.6).move_to(np.array(s + (0,)))
        neb_piece.set_fill("#08203a", 0.25).set_stroke(width=0)
        neb.add(neb_piece)

    bg_group = VGroup(bg, neb, stars)
    # keep background centered to camera frame
    bg_group.add_updater(lambda m: m.move_to(scene.camera.frame.get_center()))
    scene.add(bg_group)
    return bg_group


def setup_hud(scene):
    """Create in-frame HUD elements and trackers. Returns trackers dict."""
    layer_tracker = ValueTracker(0)
    time_tracker = ValueTracker(0)

    layer_label = DecimalNumber(
        layer_tracker.get_value(),
        num_decimal_places=0,
        include_sign=False
    )
    layer_label.add_updater(
        lambda m: m.set_value(int(layer_tracker.get_value()))
    )
    layer_text = VGroup(
        Tex("Layer"), layer_label
    ).arrange(RIGHT, buff=0.2)
    layer_text.to_corner(UR).shift(LEFT * 0.4 + DOWN * 0.5)
    scene.add_fixed_in_frame_mobjects(layer_text)

    timer = DecimalNumber(time_tracker.get_value(), num_decimal_places=1)
    timer.add_updater(lambda m: m.set_value(time_tracker.get_value()))
    timer_text = VGroup(Tex("t (min)"), timer).arrange(RIGHT, buff=0.2)
    timer_text.to_corner(UL).shift(RIGHT * 0.4 + DOWN * 0.5)
    scene.add_fixed_in_frame_mobjects(timer_text)

    return {
        "layer_tracker": layer_tracker,
        "time_tracker": time_tracker,
        "layer_label": layer_label,
        "timer": timer,
    }


def rotate_about(scene, part, hinge_point, angle, run_time=1.2):
    """Rotate 'part' about 'hinge_point' by 'angle' radians."""
    scene.play(Rotate(part, angle=angle, about_point=hinge_point),
               run_time=run_time)


def boom_extend(scene, boom, direction, distance, run_time=1.2):
    """Animate boom extension along a direction vector."""
    scene.play(boom.animate.shift(direction * distance), run_time=run_time)


def tension_layers(scene, layers, run_time=2.5):
    """Staggered tensioning effect for sunshield layers."""
    anims = [
        layer.animate.set_opacity(1).scale(1.02)
        for layer in layers
    ]
    scene.play(LaggedStart(*anims, lag_ratio=0.18), run_time=run_time)


def camera_move(scene, target_point, scale=1.0, run_time=1.2, rate_func=there_and_back):
    """Move & zoom camera frame artistically."""
    frame = scene.camera.frame
    scene.play(frame.animate.move_to(target_point).scale(scale),
               run_time=run_time, rate_func=rate_func)
