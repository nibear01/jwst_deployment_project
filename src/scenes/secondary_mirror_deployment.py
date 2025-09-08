"""Secondary mirror tripod boom deployment animation."""
from manim import *
from utils.animations import camera_move


def add_secondary_mirror_deploy(scene, telescope, hud=None):
    """Deploy secondary mirror on a three-strut boom (tripod)."""
    # tripod hub point in front of primary mirror (towards deep space/right)
    hub = Dot(telescope.get_center() + UP * 0.5 + RIGHT * 0.9, radius=0.03)
    hub.set_fill("#9aa0b2", 1)
    # three struts
    angle_offsets = [PI / 10, -PI / 10, 0]
    struts = VGroup()
    for a in angle_offsets:
        line = Line(hub.get_center(), hub.get_center() + (np.array([0.7, 0.0, 0]) \
                + rotate_vector(RIGHT, a) * 0.1))
        line.set_stroke("#9aa0b2", 3)
        struts.add(line)

    # secondary mirror disk
    sec = Circle(radius=0.18).set_fill("#d4d6dd", 1).set_stroke(WHITE, 0.6)
    sec.move_to(hub.get_center() + RIGHT * 1.0)

    # initial hidden tripod (stowed)
    struts.shift(LEFT * 0.4)
    sec.shift(LEFT * 0.4)

    scene.add(hub)
    scene.play(FadeIn(struts), run_time=0.7)
    scene.wait(0.1)

    # extend tripod: move struts & mirror outward to final position
    scene.play(
        *[s.animate.shift(RIGHT * 0.5) for s in struts],
        sec.animate.shift(RIGHT * 0.5),
        run_time=1.0
    )
    scene.play(FadeIn(sec), run_time=0.4)
    camera_move(scene, sec.get_center() + RIGHT * 0.2, scale=1.0, run_time=1.0)
    scene.wait(0.25)
