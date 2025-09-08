"""Primary mirror segments and wing hinge animation (18 hex segments)."""
from manim import *
from utils.animations import rotate_about, camera_move
from utils.constants import GOLD


def _hexagon(radius=0.18):
    h = RegularPolygon(n=6)
    h.set_fill(GOLD, 1).set_stroke("#6b4f1d", 1)
    h.scale(radius)
    return h


def add_primary_mirror_deploy(scene, telescope, hud=None):
    """Create 18 hex segments, organize into center + left + right groups,
    and hinge the side wings outward."""
    center = VGroup()
    left_wing = VGroup()
    right_wing = VGroup()

    base_center = telescope.get_center() + UP * 0.6
    # create 6 center discs in small ring
    for i in range(6):
        h = _hexagon(0.8)
        ang = TAU * i / 6
        pos = base_center + np.array([np.cos(ang), np.sin(ang), 0]) * 0.28
        h.move_to(pos)
        center.add(h)
        scene.add(h)

    # left wing (6 hexes)
    for i in range(6):
        h = _hexagon(0.75)
        ang = PI * 0.9 + i * 0.12
        pos = base_center + np.array([np.cos(ang), np.sin(ang), 0]) * 0.7 + LEFT * 0.4
        h.move_to(pos)
        left_wing.add(h)
        scene.add(h)

    # right wing (6 hexes)
    for i in range(6):
        h = _hexagon(0.75)
        ang = -0.1 + i * 0.12
        pos = base_center + np.array([np.cos(ang), np.sin(ang), 0]) * 0.7 + RIGHT * 0.4
        h.move_to(pos)
        right_wing.add(h)
        scene.add(h)

    # groupings
    primary_group = VGroup(center, left_wing, right_wing)
    scene.play(FadeIn(primary_group), run_time=0.8)
    camera_move(scene, primary_group.get_center(), scale=0.85, run_time=1.0)

    # hinge points (edge of center cluster)
    left_hinge = center.get_center() + LEFT * 0.15
    right_hinge = center.get_center() + RIGHT * 0.15

    # fold-out wings: rotate about hinge points
    rotate_about(scene, left_wing, left_hinge, angle=PI / 3, run_time=1.4)
    rotate_about(scene, right_wing, right_hinge, angle=-PI / 3, run_time=1.4)
    scene.wait(0.25)
