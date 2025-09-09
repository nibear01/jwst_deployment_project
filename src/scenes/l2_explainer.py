import numpy as np
from manim import *
SILVER = "#C0C0C0"
DEEP_BLUE = "#0B1426"

def l2_explainer(scene):
        # Create Sun-Earth-L2 system
        sun = Circle(radius=0.8, color=YELLOW, fill_opacity=1)
        sun.shift(LEFT * 4)
        
        # Add sun glow
        sun_glow = sun.copy().set_color("#FFD700").set_opacity(0.3).scale(1.2)
        
        earth = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        earth.shift(RIGHT * 2)
        
        l2_point = Dot(radius=0.15, color=RED)
        l2_point.shift(RIGHT * 3.5)
        
        # Labels with better styling
        sun_label = Text("Sun", font_size=28, color=YELLOW).next_to(sun, DOWN)
        earth_label = Text("Earth", font_size=24, color=BLUE).next_to(earth, DOWN)
        l2_label = Text("L2 Lagrange Point", font_size=22, color=RED).next_to(l2_point, UP)
        
        # Earth's orbit
        earth_orbit = Circle(radius=6, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        earth_orbit.move_to(sun.get_center())
        
        # Add elements with animation
        scene.play(
            DrawBorderThenFill(sun_glow),
            DrawBorderThenFill(sun),
            Write(sun_label),
            run_time=2
        )
        scene.play(
            Create(earth_orbit),
            run_time=2
        )
        scene.play(
            DrawBorderThenFill(earth),
            Write(earth_label),
            run_time=2
        )
        scene.play(
            DrawBorderThenFill(l2_point),
            Write(l2_label),
            run_time=2
        )
        
        # Distance indicator with animation
        distance_line = DashedLine(earth.get_center(), l2_point.get_center(), color=WHITE, stroke_width=2)
        distance_label = Text("1.5 million km", font_size=20, color=WHITE)
        distance_label.next_to(distance_line, UP, buff=0.1)
        
        scene.play(
            Create(distance_line),
            Write(distance_label),
            run_time=2
        )
        
        # Halo orbit with glow
        halo_orbit = Circle(radius=0.5, color=GREEN, stroke_width=3)
        halo_orbit.move_to(l2_point.get_center())
        halo_glow = halo_orbit.copy().set_color("#00FF00").set_opacity(0.3).scale(1.1)
        
        halo_label = Text("Halo Orbit", font_size=20, color=GREEN)
        halo_label.next_to(halo_orbit, RIGHT, buff=0.2)
        
        scene.play(
            Create(halo_glow),
            Create(halo_orbit),
            Write(halo_label),
            run_time=2
        )
        
        # JWST in halo orbit
        jwst_icon = Triangle(color=GOLD, fill_opacity=1).scale(0.1)
        jwst_icon.move_to(halo_orbit.point_from_proportion(0))
        
        # Add trail effect
        trail = TracedPath(jwst_icon.get_center, stroke_color=GOLD, stroke_width=2)
        
        scene.play(
            DrawBorderThenFill(jwst_icon),
            run_time=1
        )
        scene.add(trail)
        
        # Animate JWST around halo orbit
        scene.play(
            MoveAlongPath(jwst_icon, halo_orbit),
            rate_func=linear,
            run_time=6
        )
        scene.remove(trail)
        
        # Thermal explanation with better styling
        thermal_text = Text(
            "Sunshield protects telescope\nfrom Sun, Earth and Moon heat",
            font_size=24,
            color=WHITE
        )
        thermal_text.to_edge(DOWN, buff=0.5)
        
        # Add a background to the text
        text_bg = Rectangle(
            width=thermal_text.width + 0.5,
            height=thermal_text.height + 0.3,
            color=DEEP_BLUE,
            fill_opacity=0.8,
            stroke_color=GOLD,
            stroke_width=2
        )
        text_bg.move_to(thermal_text.get_center())
        
        scene.play(
            FadeIn(text_bg),
            Write(thermal_text),
            run_time=2
        )
        scene.wait(3)

    
        
        # Clean up with style
        l2_elements = Group(
            sun, sun_glow, sun_label, earth, earth_label, earth_orbit,
            l2_point, l2_label, distance_line, distance_label,
            halo_orbit, halo_glow, halo_label, jwst_icon, thermal_text, text_bg
        )

        scene.play(
            FadeOut(l2_elements),
            run_time=2.5
        )
        scene.wait(2)