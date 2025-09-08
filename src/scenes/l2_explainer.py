"""L2 explainer: Sun, Earth, L2 dot, halo orbit, and JWST icon animating."""
from manim import *
from utils.animations import camera_move


def add_l2_explainer(scene, hud=None):
    """Show Sun, Earth, L2 dot, halo orbit, label ~1.5M km."""
    # positions (scale is illustrative)
    sun = Circle(radius=0.9).set_fill(YELLOW, 1).set_stroke(width=0)
    earth = Circle(radius=0.28).set_fill("#2f6fba", 1).set_stroke(WHITE, 0.6)
    sun.to_edge(LEFT, buff=1.0)
    earth.move_to(sun.get_center() + RIGHT * 3.6 + DOWN * 0.1)

    # L2 point beyond Earth on same Sun-Earth line
    l2 = Dot(earth.get_center() + RIGHT * 1.6, radius=0.06)
    l2_label = Tex("L2").next_to(l2, UP, buff=0.12)
    dist_label = Tex(r"$\sim 1.5$M km").next_to(l2, DOWN, buff=0.12)

    # halo orbit (small ellipse about L2)
    halo = Ellipse(width=0.9, height=0.6).move_to(l2.get_center())
    halo.set_stroke(WHITE, 1.0, opacity=0.6).set_fill(opacity=0)

    # JWST icon (small triangle) moving on halo
    jwst_icon = Triangle().scale(0.08)
    jwst_icon.set_fill("#ffffff", 1).set_stroke(width=0)
    jwst_icon.move_to(halo.point_from_proportion(0.0))

    scene.play(FadeIn(sun), FadeIn(earth), run_time=0.9)
    scene.play(FadeIn(l2), Write(l2_label), Write(dist_label), run_time=0.6)
    scene.play(Create(halo), run_time=0.8)
    camera_move(scene, l2.get_center(), scale=0.9, run_time=1.0)

    # move jwst icon along halo orbit for 2 cycles
    scene.play(MoveAlongPath(jwst_icon, halo, run_time=3.0, rate_func=linear))
    scene.play(MoveAlongPath(jwst_icon, halo, run_time=3.0, rate_func=linear))
    # thermal rationale bullet
    note = Tex("Sun/Earth on same side → passive cooling & stable\n"
               "communications via sunshield orientation").scale(0.45)
    note.to_corner(DL).shift(RIGHT * 0.2 + UP * 0.1)
    scene.add_fixed_in_frame_mobjects(note)
    scene.wait(0.4)
