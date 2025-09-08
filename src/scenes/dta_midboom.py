"""Deployable Tower Assembly (DTA) extension + mid-boom extension sequence."""
from manim import *
from utils.animations import boom_extend, camera_move


def add_dta_and_midbooms(scene, telescope, hud=None):
    """Extend DTA tower and show mid-booms starting to deploy.

    telescope: shared VGroup previously created.
    """
    # create a DTA tower as a narrow rectangle above the bus
    bus = telescope[0] if len(telescope) > 0 else Rectangle(width=2, height=1)
    dta = Rectangle(width=0.22, height=0.6).next_to(bus, UP, buff=0.02)
    dta.set_fill("#8b8f9a", 1).set_stroke(WHITE, 0.6)
    midboom_left = Line(start=ORIGIN, end=LEFT * 1.2).next_to(dta, LEFT, buff=0.02)
    midboom_right = Line(start=ORIGIN, end=RIGHT * 1.2).next_to(dta, RIGHT, buff=0.02)
    midboom_left.set_stroke("#bdbdbd", 3)
    midboom_right.set_stroke("#bdbdbd", 3)

    # attach to scene near telescope
    dta.move_to(telescope.get_center() + UP * 0.9)
    midboom_left.move_to(dta.get_center() + LEFT * 0.8)
    midboom_right.move_to(dta.get_center() + RIGHT * 0.8)

    scene.play(FadeIn(dta, shift=UP * 0.4), run_time=0.9)
    scene.wait(0.12)

    # DTA extend (animate upward a bit)
    boom_extend(scene, dta, UP, 0.7, run_time=1.1)
    scene.wait(0.1)

    # mid-booms slide-out with small bending ease
    scene.play(
        midboom_left.animate.shift(LEFT * 0.6).scale(1.0),
        midboom_right.animate.shift(RIGHT * 0.6).scale(1.0),
        run_time=1.1,
        rate_func=there_and_back
    )
    scene.add(midboom_left, midboom_right)
    camera_move(scene, dta.get_center() + RIGHT * 0.6, scale=0.95, run_time=1.2)
    scene.wait(0.2)
