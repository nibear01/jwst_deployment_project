"""Minimal scene to test Primary Mirror deployment"""
from manim import *
import numpy as np
from src.scenes.primary_mirror import primary_mirror_deployment

# Constants used below
GOLD = "#D4AF37"
SILVER = "#C0C0C0"
DEEP_BLUE = "#0B1426"
ACCENT_BLUE = "#1E90FF"

class PrimaryMirrorTest(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DEEP_BLUE
        self.transition_effect("Primary Mirror Deployment")
        primary_mirror_deployment(self)

    def transition_effect(self, next_scene_title):
        """Smooth transition between scenes with title card"""
        # Create a expanding ripple transition
        transition_circle = Circle(radius=0.1, color=ACCENT_BLUE, fill_opacity=0.8)
        transition_circle.move_to(ORIGIN)
        
        # Add glow effect
        glow_circle = transition_circle.copy().set_opacity(0.3).scale(1.2)
        
        self.play(
            Create(glow_circle),
            Create(transition_circle),
            run_time=0.5
        )
        
        self.play(
            transition_circle.animate.scale(25).set_opacity(0),
            glow_circle.animate.scale(30).set_opacity(0),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Show next scene title with style
        title = Text(next_scene_title, font_size=42, color=GOLD)
        subtitle = Text("James Webb Space Telescope", font_size=24, color=SILVER)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.move_to(ORIGIN)
        
        # Add a background rectangle
        title_bg = Rectangle(
            width=title.width + 0.5,
            height=title.height + subtitle.height + 0.5,
            color=DEEP_BLUE,
            fill_opacity=0.8,
            stroke_color=GOLD,
            stroke_width=2
        )
        title_bg.move_to(title_group.get_center())
        
        self.play(
            FadeIn(title_bg),
            Write(title),
            Write(subtitle),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            FadeOut(title_bg),
            FadeOut(title),
            FadeOut(subtitle),
            run_time=1
        )


    def create_primary_mirror(self):
        """Create the 18-segment primary mirror"""
        def create_hexagon(radius=0.25):
            return RegularPolygon(6, radius=radius, color=GOLD, 
                                fill_opacity=0.95, stroke_color=WHITE, stroke_width=1.5)
        
        # Central hexagon
        center_hex = create_hexagon()
        hexagons = VGroup(center_hex)
        
        # First ring (6 hexagons)
        for i in range(6):
            angle = i * PI / 3
            hex_pos = 0.43 * np.array([np.cos(angle), np.sin(angle), 0])
            hex_seg = create_hexagon().move_to(hex_pos)
            hexagons.add(hex_seg)
        
        # Second ring (12 hexagons) - wings
        wing_left = VGroup()
        wing_right = VGroup()
        
        for i in range(6):
            angle = i * PI / 3
            hex_pos = 0.86 * np.array([np.cos(angle), np.sin(angle), 0])
            hex_seg = create_hexagon().move_to(hex_pos)
            if hex_pos[0] < 0:
                wing_left.add(hex_seg)
            else:
                wing_right.add(hex_seg)
        
        # Additional outer hexagons
        for i in range(6):
            angle = i * PI / 3 + PI/6
            hex_pos = 0.86 * np.array([np.cos(angle), np.sin(angle), 0])
            hex_seg = create_hexagon().move_to(hex_pos)
            if hex_pos[0] < 0:
                wing_left.add(hex_seg)
            else:
                wing_right.add(hex_seg)
        
        return Group(hexagons, wing_left, wing_right)


    


    