import numpy as np
from manim import *
SILVER = "#C0C0C0"
ACCENT_BLUE = "#1E90FF"

def sunshield_deployment(scene):
        """Cinematic sunshield deployment sequence"""
        # Create JWST model
        jwst = scene.create_jwst_model()
        sunshield_layers, primary_mirror, secondary_system, bus, bus_details, dta_tower, solar_panel, antenna = jwst
        
        # Initial folded state
        for layer in sunshield_layers:
            layer.scale(0.2).set_opacity(0.3)
        
        primary_mirror.scale(0.5).set_opacity(0.3)
        secondary_system.scale(0.4).set_opacity(0.3)
        solar_panel.scale(0.8).set_opacity(0.5)
        
        # Add to scene
        scene.add(jwst)
        
        # Camera focus on spacecraft with smooth movement
        scene.play(
            scene.camera.frame.animate.move_to(jwst.get_center()).scale(0.7),
            run_time=3,
            rate_func=smooth
        )
        
        # Solar panel deployment
        scene.play(
            solar_panel.animate.scale(1.2).set_opacity(1),
            run_time=2,
            rate_func=smooth
        )
        
        # DTA extension animation with glow effect
        dta_glow = dta_tower.copy().set_color(ACCENT_BLUE).set_opacity(0.3)
        scene.add(dta_glow)
        
        scene.play(
            dta_tower.animate.stretch(2.5, 1, about_point=bus.get_top()),
            dta_glow.animate.stretch(2.5, 1, about_point=bus.get_top()).set_opacity(0.1),
            run_time=3,
            rate_func=smooth
        )
        scene.remove(dta_glow)
        
        # Sunshield deployment with sequential animation
        deploy_animations = []
        for i, layer in enumerate(sunshield_layers):
            deploy_animations.append(
                layer.animate.scale(4).set_opacity(0.9).shift(DOWN * 0.2 * i)
            )
        
        # Add glow effect during deployment
        sunshield_glow = sunshield_layers.copy().set_color(ACCENT_BLUE).set_opacity(0.2)
        scene.add(sunshield_glow)
        
        scene.play(
            LaggedStart(*deploy_animations, lag_ratio=0.3),
            sunshield_glow.animate.scale(4).set_opacity(0.1),
            run_time=5
        )
        scene.remove(sunshield_glow)
        
        # Mid-boom extension (simulated)
        scene.play(
            sunshield_layers.animate.stretch(1.2, 0, about_point=sunshield_layers.get_center()),
            run_time=2.5
        )
        
        # Layer tensioning with labels and highlight effects
        for i, layer in enumerate(sunshield_layers):
            label = Text(f"Layer {i+1}", font_size=20, color=WHITE)
            label.next_to(layer.get_corner(UR), UR, buff=0.1)
            
            layer_glow = layer.copy().set_color(ACCENT_BLUE).set_opacity(0.3)
            scene.add(layer_glow)
            
            scene.play(
                layer.animate.set_opacity(1).scale(1.05),
                layer_glow.animate.scale(1.05).set_opacity(0.1),
                FadeIn(label),
                run_time=1
            )
            scene.play(
                FadeOut(label),
                FadeOut(layer_glow),
                run_time=0.5
            )
        
        # Final adjustment with camera movement
        scene.play(
            jwst.animate.shift(UP * 0.5),
            scene.camera.frame.animate.move_to(jwst.get_center() + UP * 0.5).scale(0.8),
            run_time=2
        )
        
        # Hold on deployed sunshield with subtle glow
        final_glow = sunshield_layers.copy().set_color(ACCENT_BLUE).set_opacity(0.1)
        scene.add(final_glow)
        scene.wait(2)
        scene.remove(final_glow)