import numpy as np
from manim import *
SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"

def secondary_mirror_deployment(scene):
        """Secondary mirror deployment with tripod extension"""
        # Create just the secondary system
        secondary_mirror = Circle(radius=0.3, color=GOLD, fill_opacity=0.9)
        
        # Tripod struts (initially retracted)
        boom_struts = VGroup()
        for i, angle in enumerate([0, 2*PI/3, 4*PI/3]):
            strut = Line(
                ORIGIN,
                0.2 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=SILVER,
                stroke_width=4
            )
            boom_struts.add(strut)
        
        secondary_system = Group(secondary_mirror, boom_struts)
        secondary_system.move_to(UP * 2)
        
        scene.add(secondary_system)
        
        # Camera focus on secondary mirror with smooth zoom
        scene.play(
            scene.camera.frame.animate.move_to(UP * 2).scale(0.4),
            run_time=2.5,
            rate_func=smooth
        )
        
        # Add glow effect during deployment
        mirror_glow = secondary_mirror.copy().set_color(YELLOW).set_opacity(0.3)
        scene.add(mirror_glow)
        
        # Deploy tripod with sequential animation
        for i, strut in enumerate(boom_struts):
            angle = i * 2*PI/3
            final_end = 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
            
            strut_glow = strut.copy().set_color(ACCENT_BLUE).set_opacity(0.5)
            scene.add(strut_glow)
            
            scene.play(
                strut.animate.put_start_and_end_on(ORIGIN, final_end),
                strut_glow.animate.put_start_and_end_on(ORIGIN, final_end),
                run_time=1.5,
                rate_func=smooth
            )
            scene.remove(strut_glow)
        
        # Final adjustment with emphasis
        scene.play(
            secondary_mirror.animate.scale(1.2),
            mirror_glow.animate.scale(1.2).set_opacity(0.2),
            run_time=1.5
        )
        scene.remove(mirror_glow)
        
        # Add deployment confirmation with style
        confirm_text = Text("SECONDARY MIRROR DEPLOYED", font_size=24, color=GREEN)
        confirm_text.next_to(secondary_system, DOWN, buff=0.5)