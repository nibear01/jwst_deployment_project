"""JWST Deployment Animation V2 - Cinematic Master Scene"""
from manim import *
import numpy as np
from src.scenes.outro import outro_scene
from src.scenes.intro import intro_scene
from src.scenes.sunshield import sunshield_deployment
from src.scenes.secondary_mirror import secondary_mirror_deployment
from src.scenes.primary_mirror import primary_mirror_deployment
from src.scenes.l2_explainer import l2_explainer

# Constants
GOLD = "#D4AF37"
SILVER = "#C0C0C0"
DARK_METAL = "#2F2F2F"
LIGHT_METAL = "#E6E6E6"
DEEP_BLUE = "#0B1426"
STAR_WHITE = "#FFFFFF"
NEBULA_BLUE = "#1F4A80"
NEBULA_PURPLE = "#4B0082"
ACCENT_BLUE = "#1E90FF"

class MasterScene(MovingCameraScene):
    def construct(self):
        # self.add_sound("jwst_voice.mp3", time_offset=0.0, gain=None)
        self.camera.background_color = DEEP_BLUE
        
        stars, nebula = self.create_space_background()
        self.add(stars, nebula)
        
        self.play(FadeIn(stars, nebula, run_time=3))
        intro_scene(self)   #done 

        # Main deployment sequences with smooth transitions
        sunshield_deployment(self)   #done
        self.transition_effect("Secondary Mirror Deployment")
        secondary_mirror_deployment(self) 
        self.transition_effect("Primary Mirror Deployment")
        primary_mirror_deployment(self)
        self.transition_effect("Journey to L2")
        l2_explainer(self)

        outro_scene(self)      #done

    def create_space_background(self):
        """Create a rich space background with stars and nebula"""
        stars = VGroup()
        for i in range(400): 
            brightness = np.random.uniform(0.3, 0.8)
            size = np.random.uniform(0.001, 0.01)  # Slightly larger stars
            star = Dot(
                radius=size,
                color=WHITE
            ).set_opacity(brightness)
            
            star.move_to([
                np.random.uniform(-8, 8),
                np.random.uniform(-5, 5),
                0
            ])
            stars.add(star)
        
        # Nebula cloud - more detailed
        nebula = VGroup()
        colors = [NEBULA_BLUE, NEBULA_PURPLE, "#3E309B", "#0F1955"]
        for i in range(8):
            cloud = Ellipse(
                width=np.random.uniform(4, 8),
                height=np.random.uniform(2, 4),
                color=colors[i % len(colors)],
                fill_opacity=np.random.uniform(0.05, 0.2),
                stroke_width=0
            )
            cloud.move_to([
                np.random.uniform(-6, 6),
                np.random.uniform(-3, 3),
                0
            ])
            nebula.add(cloud)
        
        return stars, nebula

    def create_jwst_model_silhouette(self):
        """Create a detailed JWST silhouette for the intro"""
        # Sunshield
        sunshield = Polygon(
            [-3, 0, 0], [0, 2.5, 0], [3, 0, 0], [0, -2.5, 0],
            color=WHITE, fill_opacity=0.8, stroke_width=2
        )
        
        # Primary mirror
        primary_mirror = Circle(radius=0.8, color=GOLD, fill_opacity=0.9)
        primary_mirror.shift(UP * 1.2)
        
        # Secondary mirror
        secondary_mirror = Circle(radius=0.2, color=SILVER, fill_opacity=0.9)
        secondary_mirror.shift(UP * 2.5)
        
        # Spacecraft bus
        bus = Rectangle(width=1, height=0.5, color=DARK_METAL, fill_opacity=0.9)
        bus.shift(DOWN * 0.8)
        
        return VGroup(sunshield, primary_mirror, secondary_mirror, bus)

    def create_starfield_parallax(self):
        """Create a starfield with parallax effect"""
        stars = VGroup()
        for i in range(150):
            depth = np.random.uniform(0.5, 2.0)  # Parallax depth factor
            size = 0.03 / depth
            brightness = 0.4 / depth
            
            star = Dot(radius=size, color=WHITE).set_opacity(brightness)
            star.move_to([
                np.random.uniform(-8, 8),
                np.random.uniform(-5, 5),
                0
            ])
            star.depth = depth
            stars.add(star)
        return stars

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

    def create_jwst_model(self):
        """Create a detailed JWST model with accurate proportions"""
        # Sunshield layers (5 layers, kite shape)
        sunshield_layers = VGroup()
        layer_colors = [LIGHT_METAL, DARK_METAL, LIGHT_METAL, DARK_METAL, LIGHT_METAL]
        
        for i in range(5):
            layer = Polygon(
                [-3 - i*0.1, 0, 0],      # Left point
                [0, 2 + i*0.1, 0],       # Top point  
                [3 + i*0.1, 0, 0],       # Right point
                [0, -2 - i*0.1, 0],      # Bottom point
                color=layer_colors[i],
                fill_opacity=0.9,
                stroke_width=2,
                stroke_color=WHITE
            )
            layer.set_z_index(-i)
            sunshield_layers.add(layer)
        
        # Primary mirror (18 segments)
        primary_mirror = self.create_primary_mirror()
        primary_mirror.shift(UP * 3.2)
        
        # Secondary mirror on tripod
        secondary_mirror = Circle(radius=0.3, color=GOLD, fill_opacity=0.9)
        boom_struts = VGroup()
        for angle in [0, 2*PI/3, 4*PI/3]:
            strut = Line(
                ORIGIN,
                0.8 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=SILVER,
                stroke_width=4
            )
            boom_struts.add(strut)
        
        secondary_system = Group(secondary_mirror, boom_struts)
        secondary_system.shift(UP * 2)
        
        # Spacecraft bus - more detailed
        bus = Rectangle(
            width=1.5, height=0.8,
            color=DARK_METAL,
            fill_opacity=0.9,
            stroke_width=3,
            stroke_color=SILVER
        ).shift(DOWN * 0.5)
        
        # Add details to bus
        bus_details = VGroup()
        for i in range(3):
            panel = Rectangle(
                width=0.3, height=0.6,
                color=LIGHT_METAL,
                fill_opacity=0.7,
                stroke_width=1
            )
            panel.move_to(bus.get_center() + RIGHT * (i * 0.4 - 0.4))
            bus_details.add(panel)
        
        # DTA tower
        dta_tower = Rectangle(
            width=0.5, height=1.2,
            color=SILVER,
            fill_opacity=0.9,
            stroke_width=2
        ).shift(UP * 0.4)
        
        # Solar panel
        solar_panel = Rectangle(
            width=0.2, height=2.5,
            color=LIGHT_METAL,
            fill_opacity=1,
            stroke_width=1
        ).next_to(bus, LEFT, buff=0).shift(UP * 0.2)

        # mirror_boom = VGroup(
        #     primary_mirror, dta_tower
        # )
        # primary_mirror.shift(UP * 0.6 + dta_tower.height / 2)
        
        # High gain antenna
        antenna = VGroup(
            Circle(radius=0.15, color=SILVER, fill_opacity=0.9),
            Rectangle(width=0.1, height=0.4, color=SILVER, fill_opacity=0.9)
        ).arrange(DOWN, buff=0).next_to(bus, RIGHT, buff=0.1).shift(UP * 0.3)
        
        return Group(sunshield_layers, primary_mirror, secondary_system, bus, bus_details, dta_tower, solar_panel, antenna)

    def create_primary_mirror(self):
        """Create the 18-segment primary mirror with larger polygons."""

        def create_hexagon(radius=0.5, color="#FFD700"):
            hexagon = RegularPolygon(6, radius=radius)
            hexagon.set_fill(color, opacity=1)
            hexagon.set_stroke(WHITE, width=1.5)
            return hexagon

        # Central hexagon
        center_hex = create_hexagon()
        all_segments = VGroup(center_hex)

        # First ring (6 hexagons)
        for i in range(6):
            angle = i * PI / 3
            hex_pos = 0.9 * np.array([np.cos(angle), np.sin(angle), 0]) 
            seg = create_hexagon().move_to(hex_pos)
            all_segments.add(seg)

        # Second ring (12 hexagons)
        wing_left = VGroup()
        wing_right = VGroup()
        for i in range(6):
            angle = i * PI / 3
            hex_pos = 1.75 * np.array([np.cos(angle), np.sin(angle), 0]) 
            seg = create_hexagon().move_to(hex_pos)
            if hex_pos[0] < 0:
                wing_left.add(seg)
            else:
                wing_right.add(seg)

        for i in range(6):
            angle = i * PI / 3 + PI / 6
            hex_pos = 1.75 * np.array([np.cos(angle), np.sin(angle), 0])
            seg = create_hexagon().move_to(hex_pos)
            if hex_pos[0] < 0:
                wing_left.add(seg)
            else:
                wing_right.add(seg)

        # Frame & highlights
        frame = SurroundingRectangle(all_segments, buff=0.2, color="#FFE65B", stroke_width=2).set_opacity(0.3)

        highlights = VGroup()
        for hex_seg in all_segments:
            dot = Dot(point=hex_seg.get_center() + 0.15*UP + 0.1*RIGHT, color=WHITE, radius=0.04)  # slightly larger
            highlights.add(dot)

        mirror_group = VGroup(all_segments, wing_left, wing_right, frame, highlights)

        return mirror_group




    


    