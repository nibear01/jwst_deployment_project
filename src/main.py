"""Master entry point. Run: manim -pqh main.py MasterScene"""
from manim import *
from scenes.sunshield_deployment import add_sunshield_sequence
from scenes.dta_midboom import add_dta_and_midbooms
from scenes.layer_tensioning import add_layer_tensioning
from scenes.secondary_mirror_deployment import add_secondary_mirror_deploy
from scenes.primary_mirror_deployment import add_primary_mirror_deploy
from scenes.l2_explainer import add_l2_explainer
from utils.animations import create_background, setup_hud
from utils.constants import SUNSHIELD_LAYERS, PRIMARY_SEGMENTS


class MasterScene(Scene):
    """Master stitching scene that runs each scene function sequentially."""
    def construct(self):
        # Create cinematic background and HUD
        create_background(self)
        hud_trackers = setup_hud(self)

        # Build a reusable 'telescope' placeholder group so scenes remain connected.
        telescope = self._create_telescope_stub()
        self.add(telescope)

        # Sequence: sunshield pallets + DTA, mid-booms, tensioning,
        # secondary boom, primary mirror wing(s), L2 explainer.
        add_sunshield_sequence(self, telescope, hud_trackers)
        add_dta_and_midbooms(self, telescope, hud_trackers)
        add_layer_tensioning(self, telescope, hud_trackers)
        add_secondary_mirror_deploy(self, telescope, hud_trackers)
        add_primary_mirror_deploy(self, telescope, hud_trackers)
        add_l2_explainer(self, hud_trackers)

        # Final hold for review
        self.wait(2)

    def _create_telescope_stub(self):
        """Create a compact telescope/bus + mirror placeholder shared across scenes."""
        bus = RoundedRectangle(width=2.0, height=1.0, corner_radius=0.1)
        bus.set_fill("#2b2d42", 1).set_stroke(WHITE, 1.2)
        mirror_stub = Circle(radius=0.5).next_to(bus, UP, buff=0.05)
        mirror_stub.set_fill("#3b3f5c", 1).set_stroke(WHITE, 0.8)
        sunshield_stub = Rectangle(width=3.6, height=0.2).next_to(bus, DOWN, buff=0.06)
        sunshield_stub.set_fill("#111217", 1).set_stroke(WHITE, 0.6)
        vg = VGroup(bus, mirror_stub, sunshield_stub)
        vg.move_to(ORIGIN)
        return vg
