import numpy as np
from manim import *

SILVER = "#C0C0C0"
DEEP_BLUE = "#0B1426"

def l2_explainer(scene):
    # --- Background stars (twinkling) ---
    stars = VGroup(*[
        Dot(
            point=[np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0],
            radius=np.random.uniform(0.01, 0.03),
            color=WHITE
        )
        for _ in range(70)
    ])
    scene.add(stars)

    # Stars twinkle updater
    def twinkle(dot, dt):
        dot.set_opacity(0.3 + 0.7*np.abs(np.sin(scene.time*2*np.pi*np.random.uniform(0.5, 1.5))))
    for star in stars:
        star.add_updater(twinkle)

    # --- Sun ---
    sun = Circle(radius=0.8, color=ORANGE, fill_opacity=1).shift(LEFT * 4)
    
    # Sun glow
    sun_glow = Circle(radius=1.2, color=ORANGE, fill_opacity=0.5)
    sun_glow.move_to(sun.get_center())
    
    # Glow updater (pulsating)
    def pulse_sun(mob, dt):
        mob.set_opacity(0.4 + 0.3*np.abs(np.sin(scene.time*2*np.pi)))
        mob.scale(1 + 0.01*np.sin(scene.time*2*np.pi))
    sun_glow.add_updater(pulse_sun)

    # Sun rays
    rays = VGroup(*[
        Line(ORIGIN, UP*1.5, color=YELLOW, stroke_width=2).rotate(angle)
        for angle in np.linspace(0, 2*np.pi, 18)
    ])
    rays.move_to(sun.get_center())
    rays.add_updater(lambda mob, dt: mob.rotate(0.01))

    # Sun label
    sun_label = Text("Sun", font_size=28, color=ORANGE).next_to(sun, DOWN)

    # Animate Sun
    scene.play(DrawBorderThenFill(sun), Create(sun_glow), Create(rays), Write(sun_label), run_time=2)

    # --- Earth ---
    earth_orbit = Circle(radius=6, color=WHITE, stroke_width=2, stroke_opacity=0.5).move_to(sun.get_center())
    scene.play(Create(earth_orbit), run_time=2)

    earth = Circle(radius=0.3, color=BLUE, fill_opacity=1)
    earth_label = Text("Earth", font_size=24, color=BLUE).next_to(earth, DOWN)

    def orbit_earth(mob, dt):
        mob.rotate_about_origin(dt * 0.2)
    earth.add_updater(orbit_earth)
    earth_label.add_updater(lambda mob, dt: mob.next_to(earth, DOWN))

    scene.add(earth, earth_label)

    # --- L2 point ---
    l2_point = Dot(radius=0.15, color=RED).shift(RIGHT * 3.5)
    l2_label = Text("L2 Lagrange Point", font_size=22, color=RED).next_to(l2_point, UP)
    scene.play(DrawBorderThenFill(l2_point), Write(l2_label), run_time=2)

    # Distance indicator
    distance_line = DashedLine(earth.get_center(), l2_point.get_center(), color=WHITE, stroke_width=2)
    distance_label = Text("1.5 million km", font_size=20, color=WHITE).next_to(distance_line, UP, buff=0.1)
    scene.play(Create(distance_line), Write(distance_label), run_time=2)

    # --- Halo orbit ---
    halo_orbit = Circle(radius=0.5, color=GREEN, stroke_width=3).move_to(l2_point.get_center())
    halo_glow = halo_orbit.copy().set_color("#00FF00").set_opacity(0.4).scale(1.1)
    halo_glow.add_updater(lambda mob, dt: mob.set_opacity(0.3 + 0.3*np.abs(np.sin(scene.time*2*np.pi))))
    halo_label = Text("Halo Orbit", font_size=20, color=GREEN).next_to(halo_orbit, RIGHT, buff=0.2)
    scene.play(Create(halo_orbit), Create(halo_glow), Write(halo_label), run_time=2)

    # --- JWST ---
    jwst_icon = Triangle(color=GOLD, fill_opacity=1).scale(0.1).move_to(halo_orbit.point_from_proportion(0))
    trail = TracedPath(jwst_icon.get_center, stroke_color=GOLD, stroke_width=2)
    scene.add(trail)
    scene.play(DrawBorderThenFill(jwst_icon), run_time=1)
    scene.play(MoveAlongPath(jwst_icon, halo_orbit), rate_func=linear, run_time=6)
    scene.remove(trail)

    # --- Thermal explanation ---
    thermal_text = Text(
        "Sunshield protects telescope\nfrom Sun, Earth and Moon heat",
        font_size=24, color=WHITE
    ).to_edge(DOWN, buff=0.5)

    text_bg = Rectangle(
        width=thermal_text.width + 0.5,
        height=thermal_text.height + 0.3,
        color=DEEP_BLUE,
        fill_opacity=0.8,
        stroke_color=GOLD,
        stroke_width=2
    ).move_to(thermal_text.get_center())

    scene.play(FadeIn(text_bg), Write(thermal_text), run_time=2)
    scene.wait(3)

    # --- Clean up ---
    l2_elements = Group(
        sun, sun_glow, rays, sun_label,
        earth, earth_label, earth_orbit,
        l2_point, l2_label, distance_line, distance_label,
        halo_orbit, halo_glow, halo_label, jwst_icon,
        thermal_text, text_bg, stars
    )
    scene.play(FadeOut(l2_elements), run_time=2.5)
    scene.wait(2)
