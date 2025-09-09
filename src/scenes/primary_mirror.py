import numpy as np      
from manim import *
SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"
GOLD = "#D4AF37"  

def primary_mirror_deployment(scene):
        """Primary mirror wing deployment with hinge rotation"""
        # Create primary mirror
        primary_mirror = scene.create_primary_mirror()
        center_segments, left_wing, right_wing = primary_mirror
        primary_mirror.move_to(UP * 3)
        
        # Fold wings initially
        left_wing.rotate(PI/3, about_point=center_segments.get_left())
        right_wing.rotate(-PI/3, about_point=center_segments.get_right())
        
        scene.add(primary_mirror)
        
        # Camera focus on primary mirror with dramatic angle
        scene.play(
            scene.camera.frame.animate.move_to(UP * 3).scale(0.5).rotate(PI/12),
            run_time=3,
            rate_func=smooth
        )
        
        # Add glow effect to wings during deployment
        left_glow = left_wing.copy().set_color(ACCENT_BLUE).set_opacity(0.3)
        right_glow = right_wing.copy().set_color(ACCENT_BLUE).set_opacity(0.3)
        scene.add(left_glow, right_glow)
        
        # Deploy left wing
        scene.play(
            Rotate(
                left_wing, 
                angle=-PI/3, 
                about_point=center_segments.get_left(),
                rate_func=smooth
            ),
            left_glow.animate.rotate(-PI/3, about_point=center_segments.get_left()).set_opacity(0.1),
            run_time=3
        )
        
        # Deploy right wing
        scene.play(
            Rotate(
                right_wing, 
                angle=PI/3, 
                about_point=center_segments.get_right(),
                rate_func=smooth
            ),
            right_glow.animate.rotate(PI/3, about_point=center_segments.get_right()).set_opacity(0.1),
            run_time=3
        )
        
        scene.remove(left_glow, right_glow)

        # Subtle overshoot and settle for a more organic feel
        scene.play(
            Rotate(
                left_wing,
                angle=0.06,
                about_point=center_segments.get_left(),
                rate_func=there_and_back
            ),
            Rotate(
                right_wing,
                angle=-0.06,
                about_point=center_segments.get_right(),
                rate_func=there_and_back
            ),
            run_time=0.7
        )

        scene.play(
            scene.camera.frame.animate.set(width=config.frame_width).move_to(ORIGIN),
            run_time=2
        )
        
        # Sweeping highlight across all segments
        all_segments = list(center_segments) + list(left_wing) + list(right_wing)
        sweep_to_yellow = [seg.animate.set_color(YELLOW) for seg in all_segments]
        scene.play(
            LaggedStart(*sweep_to_yellow, lag_ratio=0.06),
            run_time=1.4
        )
        sweep_back_to_gold = [seg.animate.set_color(GOLD) for seg in all_segments]
        scene.play(
            LaggedStart(*sweep_back_to_gold, lag_ratio=0.06),
            run_time=1.0
        )

        # Add subtle sparkle effects on a few random segments
        spark_indices = list(range(0, len(all_segments), max(1, len(all_segments)//6)))[:6]
        sparkles = VGroup()
        for idx in spark_indices:
            star = Star(n=5, color=WHITE, fill_opacity=0.9).scale(0.12)
            star.move_to(all_segments[idx].get_center())
            star.set_opacity(0)
            sparkles.add(star)
        scene.add(sparkles)
        scene.play(
            LaggedStart(
                *[AnimationGroup(FadeIn(star, scale=0.3), star.animate.scale(1.4)) for star in sparkles],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        scene.play(
            LaggedStart(*[FadeOut(star) for star in sparkles], lag_ratio=0.1),
            run_time=0.6
        )
        
        # Final confirmation with dramatic effect
        confirm_text = Text("PRIMARY MIRROR DEPLOYED", font_size=24, color=GREEN)
        confirm_text.next_to(primary_mirror, DOWN, buff=0.5)
        
        # Add a success icon
        success_icon = Star(n=5, color=GREEN, fill_opacity=0.8).scale(0.2)
        success_icon.next_to(confirm_text, LEFT, buff=0.2)
        
        # Brief focus-in on confirmation
        scene.play(
            scene.camera.frame.animate.scale(0.9).move_to(primary_mirror.get_center()),
            Write(confirm_text),
            DrawBorderThenFill(success_icon),
            run_time=1.5
        )
        scene.wait(1.5)
        scene.play(
            FadeOut(confirm_text),
            FadeOut(success_icon),
            scene.camera.frame.animate.set(width=config.frame_width).move_to(ORIGIN)
        )