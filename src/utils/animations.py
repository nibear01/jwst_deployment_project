"""
JWST Animation Utilities
Helper functions for common deployment animations
"""

from manim import *
import numpy as np

def rotate_about_point(scene, mobject, hinge_point, angle, run_time=1.2):
    """Rotate a mobject about a specific hinge point"""
    scene.play(
        Rotate(mobject, angle=angle, about_point=hinge_point),
        run_time=run_time,
        rate_func=smooth
    )

def extend_boom(scene, boom, direction, distance, run_time=1.5):
    """Extend a boom mechanism along a direction vector"""
    scene.play(
        boom.animate.shift(direction * distance),
        run_time=run_time,
        rate_func=smooth
    )

def tension_layers_staggered(scene, layers, scale_factor=1.02, opacity=1.0, lag_ratio=0.2, run_time=2.5):
    """Tension multiple layers with staggered timing"""
    animations = []
    for layer in layers:
        animations.append(
            layer.animate.set_opacity(opacity).scale(scale_factor)
        )
    
    scene.play(
        LaggedStart(*animations, lag_ratio=lag_ratio),
        run_time=run_time
    )

def deploy_mirror_wing(scene, wing, center_point, angle, run_time=3.0):
    """Deploy a mirror wing with smooth hinge rotation"""
    scene.play(
        Rotate(
            wing,
            angle=angle,
            about_point=center_point,
            rate_func=smooth
        ),
        run_time=run_time
    )

def create_deployment_path(start_point, end_point, curve_factor=0.5):
    """Create a curved Bezier path for deployment animations"""
    control_point = (start_point + end_point) / 2 + UP * curve_factor
    
    path = VMobject()
    path.set_points_as_corners([start_point, control_point, end_point])
    path.make_smooth()
    
    return path

def animate_along_path(scene, mobject, path, run_time=2.0, rate_func=smooth):
    """Animate a mobject along a curved path"""
    scene.play(
        MoveAlongPath(mobject, path),
        run_time=run_time,
        rate_func=rate_func
    )

def create_expanding_circle_reveal(scene, center, max_radius, objects_to_reveal, run_time=2.0):
    """Create an expanding circle reveal effect"""
    reveal_circle = Circle(radius=0.1, color=WHITE, fill_opacity=0)
    reveal_circle.move_to(center)
    
    scene.play(
        reveal_circle.animate.scale(max_radius * 10),  # Scale to max radius
        *[FadeIn(obj) for obj in objects_to_reveal],
        run_time=run_time
    )
    
    scene.remove(reveal_circle)

def create_hud_update_animation(scene, value_tracker, new_value, display_text, run_time=1.0):
    """Animate HUD value updates"""
    scene.play(
        value_tracker.animate.set_value(new_value),
        run_time=run_time,
        rate_func=linear
    )

def parallax_star_movement(scene, stars, direction, distance, run_time=3.0):
    """Create parallax movement effect for background stars"""
    animations = []
    
    for i, star in enumerate(stars):
        # Vary movement based on star "depth" (opacity suggests distance)
        depth_factor = star.fill_opacity
        movement = direction * distance * depth_factor
        animations.append(star.animate.shift(movement))
    
    scene.play(*animations, run_time=run_time, rate_func=linear)

def create_focusing_effect(scene, blurry_objects, sharp_objects, run_time=2.0):
    """Simulate wavefront sensing and focusing"""
    # Fade out blurry, fade in sharp
    scene.play(
        *[FadeOut(obj) for obj in blurry_objects],
        *[FadeIn(obj) for obj in sharp_objects],
        run_time=run_time,
        rate_func=smooth
    )

def create_measurement_line(start_point, end_point, label_text, color=WHITE):
    """Create a measurement line with label"""
    line = Line(start_point, end_point, color=color, stroke_width=2)
    
    # Add tick marks at ends
    tick_size = 0.1
    start_tick = Line(
        start_point + UP * tick_size,
        start_point + DOWN * tick_size,
        color=color,
        stroke_width=2
    )
    end_tick = Line(
        end_point + UP * tick_size,
        end_point + DOWN * tick_size,
        color=color,
        stroke_width=2
    )
    
    # Label at midpoint
    label = Text(label_text, font_size=14, color=color)
    label.next_to(line.get_center(), UP, buff=0.1)
    
    return Group(line, start_tick, end_tick, label)

def create_pulse_animation(scene, mobject, scale_factor=1.2, run_time=0.8):
    """Create a pulsing highlight effect"""
    scene.play(
        mobject.animate.scale(scale_factor),
        run_time=run_time/2,
        rate_func=rush_into
    )
    scene.play(
        mobject.animate.scale(1/scale_factor),
        run_time=run_time/2,
        rate_func=rush_from
    )

def create_spiral_deployment(scene, objects, center_point, spiral_turns=2, run_time=3.0):
    """Deploy objects in a spiral pattern"""
    animations = []
    
    for i, obj in enumerate(objects):
        angle = i * 2 * PI / len(objects) + spiral_turns * 2 * PI
        radius = 1.5 + 0.5 * (i / len(objects))
        
        final_pos = center_point + radius * np.array([np.cos(angle), np.sin(angle), 0])
        
        # Create curved path to final position
        current_pos = obj.get_center()
        path_points = []
        
        for t in np.linspace(0, 1, 20):
            spiral_angle = t * angle
            spiral_radius = t * radius
            intermediate_pos = center_point + spiral_radius * np.array([
                np.cos(spiral_angle), np.sin(spiral_angle), 0
            ])
            path_points.append(intermediate_pos)
        
        path = VMobject()
        path.set_points_as_corners(path_points)
        path.make_smooth()
        
        animations.append(MoveAlongPath(obj, path))
    
    scene.play(
        *animations,
        run_time=run_time,
        rate_func=smooth
    )