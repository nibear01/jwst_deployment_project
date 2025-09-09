"""
JWST Project Constants
Colors, dimensions, and configuration constants
"""

from manim import *
import numpy as np

# Color Palette
GOLD = "#D4AF37"
SILVER = "#C0C0C0"
DARK_METAL = "#2F2F2F"
LIGHT_METAL = "#E6E6E6"
DEEP_BLUE = "#0B1426"
STAR_WHITE = "#FFFFFF"
KAPTON_GOLD = "#FFD700"
INSTRUMENT_BLUE = "#4169E1"

# JWST Component Colors
MIRROR_GOLD = GOLD
SUNSHIELD_LIGHT = LIGHT_METAL
SUNSHIELD_DARK = DARK_METAL
SUPPORT_STRUCTURE = SILVER
INSTRUMENT_COLOR = INSTRUMENT_BLUE

# Sunshield Layer Colors (alternating)
SUNSHIELD_LAYER_COLORS = [
    LIGHT_METAL,
    DARK_METAL,
    LIGHT_METAL,
    DARK_METAL,
    LIGHT_METAL
]

# Component Dimensions (in Manim units)
SUNSHIELD_BASE_WIDTH = 6.0
SUNSHIELD_BASE_HEIGHT = 4.0
PRIMARY_MIRROR_RADIUS = 2.0
SECONDARY_MIRROR_RADIUS = 0.3
MIRROR_SEGMENT_RADIUS = 0.25

# Deployment Timeline (in days after launch)
DEPLOYMENT_TIMELINE = {
    "launch": 0,
    "solar_array": 0.5,
    "antenna_deploy": 1,
    "sunshield_pallets": 3,
    "dta_extension": 6,
    "mid_boom_extension": 8,
    "sunshield_tensioning": 10,
    "secondary_mirror": 12,
    "primary_mirror_wings": 14,
    "mirror_alignment": 120,
    "instrument_cooldown": 150,
    "first_light": 180
}

# Animation Timing (in seconds)
SCENE_DURATIONS = {
    "intro": 10,
    "sunshield_deployment": 45,
    "secondary_mirror": 25,
    "primary_mirror": 30,
    "l2_explainer": 35,
    "outro": 10
}

# Camera Settings
CAMERA_ZOOM_LEVELS = {
    "wide": 1.5,
    "medium": 1.0,
    "close": 0.6,
    "detail": 0.4
}

# Text Sizes
FONT_SIZES = {
    "title": 36,
    "scene_title": 32,
    "subtitle": 24,
    "body": 20,
    "label": 16,
    "small_label": 12,
    "hud": 18
}

# Mirror Segment Layout
PRIMARY_MIRROR_LAYOUT = {
    "center_segments": 1,
    "inner_ring_segments": 6,
    "outer_ring_segments": 12,
    "total_segments": 19  # Actually 18 for JWST
}

# L2 Orbital Parameters
L2_PARAMETERS = {
    "distance_from_earth_km": 1500000,
    "halo_orbit_radius_km": 800000,
    "orbital_period_days": 180
}

# Instrument Names and Colors
INSTRUMENTS = {
    "NIRCam": {"color": RED, "position": "primary_focus_1"},
    "NIRSpec": {"color": BLUE, "position": "primary_focus_2"}, 
    "MIRI": {"color": GREEN, "position": "primary_focus_3"},
    "FGS_NIRISS": {"color": PURPLE, "position": "primary_focus_4"}
}

# Deployment Sequence Order
DEPLOYMENT_SEQUENCE = [
    "sunshield_pallet_release",
    "dta_extension", 
    "mid_boom_deployment",
    "sunshield_layer_tensioning",
    "secondary_mirror_deployment",
    "primary_mirror_wing_deployment",
    "l2_transit_and_insertion"
]

# Animation Rate Functions
RATE_FUNCTIONS = {
    "smooth_deployment": smooth,
    "mechanical": linear,
    "spring": lambda t: 1 - np.exp(-5*t) * np.cos(10*t),
    "tension": rush_into,
    "settle": rush_from
}

# Star Field Settings
STAR_FIELD = {
    "count": 80,
    "min_radius": 0.02,
    "max_radius": 0.08,
    "min_opacity": 0.3,
    "max_opacity": 0.9,
    "field_width": 16,
    "field_height": 10
}

# HUD Elements
HUD_CONFIG = {
    "time_position": "UL",
    "status_position": "UR", 
    "progress_position": "LL",
    "info_position": "LR",
    "margin": 0.3
}