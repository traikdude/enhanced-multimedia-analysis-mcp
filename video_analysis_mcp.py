#!/usr/bin/env python3
"""
Enhanced Multimedia Analysis MCP Server
Version: 1.1.0
A Model Context Protocol server for professional multimedia content analysis
and AI video generation prompt engineering.
"""

import os
import sys
import json
import hashlib
import logging
from typing import Optional, List, Dict, Any, Literal
from datetime import datetime
from pydantic import BaseModel, Field

try:
    from fastmcp import FastMCP
except ImportError:
    print("Error: fastmcp not installed. Run: pip install fastmcp", file=sys.stderr)
    sys.exit(1)

# Configuration from environment variables
CHAR_LIMIT = int(os.getenv("VIDEO_ANALYSIS_CHAR_LIMIT", "25000"))
DEBUG = os.getenv("VIDEO_ANALYSIS_DEBUG", "false").lower() == "true"
LOG_LEVEL = os.getenv("VIDEO_ANALYSIS_LOG_LEVEL", "INFO")
CACHE_ENABLED = os.getenv("VIDEO_ANALYSIS_CACHE_ENABLED", "false").lower() == "true"
CACHE_DIR = os.getenv("VIDEO_ANALYSIS_CACHE_DIR", "/tmp/video_analysis_cache")
CACHE_TTL = int(os.getenv("VIDEO_ANALYSIS_CACHE_TTL", "3600"))
DEFAULT_DEPTH = os.getenv("VIDEO_ANALYSIS_DEFAULT_DEPTH", "standard")

# Logging setup
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("video_analysis_mcp")

# Initialize FastMCP server
mcp = FastMCP("Enhanced Multimedia Analysis MCP")

# ============================================================================
# HOTKEY DEFINITIONS
# ============================================================================

HOTKEY_CATEGORIES = {
    "A": "Aesthetic & Visual Style",
    "S": "Story & Narrative",
    "C": "Character & Subject",
    "K": "Cinematography",
    "P": "Platform Optimization",
    "E": "Execution & Technical"
}

HOTKEYS = {
    # A-Series: Aesthetic & Visual Style
    "A1": "Color palette and grading",
    "A2": "Lighting mood and atmosphere",
    "A3": "Visual texture and materials",
    "A4": "Composition and framing",
    "A5": "Visual style and art direction",
    "A6": "Time of day and weather",
    "A7": "Visual effects and magic",
    "A8": "Setting and environment",
    "A9": "Props and objects",
    "A10": "Visual metaphors and symbolism",
    "A11": "Contrast and visual hierarchy",
    "A12": "Pattern and repetition",
    "A13": "Scale and proportion",

    # S-Series: Story & Narrative
    "S1": "Story setup and premise",
    "S2": "Conflict and tension",
    "S3": "Character arc and transformation",
    "S4": "Pacing and timing",
    "S5": "Emotional journey",
    "S6": "Plot twists and reveals",
    "S7": "Theme and message",
    "S8": "Dialogue and interaction",
    "S9": "Subtext and implications",
    "S10": "Foreshadowing and callbacks",
    "S11": "Resolution and payoff",
    "S12": "World-building details",

    # C-Series: Character & Subject
    "C1": "Character appearance and design",
    "C2": "Facial expressions and emotions",
    "C3": "Body language and posture",
    "C4": "Costume and wardrobe",
    "C5": "Character relationships",
    "C6": "Personality traits",
    "C7": "Character motivation",
    "C8": "Character consistency across scenes",
    "C9": "Age, gender, ethnicity details",
    "C10": "Distinctive features and traits",
    "C11": "Character evolution",
    "C12": "Ensemble dynamics",

    # K-Series: Cinematography (Camera & Movement)
    "K1": "Camera angles and perspective",
    "K2": "Shot types and framing",
    "K3": "Camera movement and motion",
    "K4": "Depth of field and focus",
    "K5": "Lens choice and distortion",
    "K6": "Aspect ratio and format",
    "K7": "Blocking and staging",
    "K8": "Transition types",
    "K9": "Visual continuity",
    "K10": "POV and perspective shifts",
    "K11": "Establishing shots",
    "K12": "Close-ups and inserts",
    "K13": "Wide shots and landscapes",

    # P-Series: Platform Optimization
    "P1": "TikTok: Vertical format, hook-first",
    "P2": "Instagram: Grid-aware, aesthetic-first",
    "P3": "YouTube: Thumbnail optimization, retention",
    "P4": "Cinema: Cinematic language, theatrical",
    "P5": "Mobile viewing optimization",
    "P6": "Sound design for platform",
    "P7": "Text overlay considerations",
    "P8": "Platform-specific trends",
    "P9": "Algorithm optimization",
    "P10": "Duration sweet spots",

    # E-Series: Execution & Technical
    "E1": "Technical specifications",
    "E2": "Motion blur and shutter speed",
    "E3": "Frame rate considerations",
    "E4": "Resolution and quality",
    "E5": "CGI and VFX integration",
    "E6": "Practical effects",
    "E7": "Animation style and technique",
    "E8": "Rendering requirements",
    "E9": "Prompt structure optimization",
    "E10": "Negative prompts",
    "E11": "Seed and consistency parameters",
    "E12": "Model-specific syntax"
}

# ============================================================================
# DATA MODELS
# ============================================================================

class AnalysisRequest(BaseModel):
    """Request model for content analysis"""
    content_description: str = Field(
        description="Description of the visual content to analyze"
    )
    analysis_depth: Literal["quick", "standard", "deep", "comprehensive"] = Field(
        default="standard",
        description="Depth of analysis to perform"
    )
    target_platform: Optional[str] = Field(
        default=None,
        description="Target platform (TikTok, Instagram, YouTube, Cinema)"
    )
    focus_areas: Optional[List[str]] = Field(
        default=None,
        description="Specific areas to focus on"
    )
    hotkeys: Optional[List[str]] = Field(
        default=None,
        description="Specific hotkeys to use"
    )
    reference_style: Optional[str] = Field(
        default=None,
        description="Reference style or inspiration"
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format"
    )

# ============================================================================
# ANALYSIS ENGINE
# ============================================================================

def select_hotkeys_for_depth(depth: str, focus_areas: Optional[List[str]] = None,
                              custom_hotkeys: Optional[List[str]] = None) -> List[str]:
    """Select appropriate hotkeys based on analysis depth and focus"""

    if custom_hotkeys:
        return custom_hotkeys

    # Default hotkey sets based on depth
    depth_hotkeys = {
        "quick": ["A1", "A2", "C1", "C2", "K1", "K2"],
        "standard": ["A1", "A2", "A4", "S1", "S5", "C1", "C2", "C8", "K1", "K2", "K3", "E9"],
        "deep": ["A1", "A2", "A3", "A4", "A5", "S1", "S2", "S5", "C1", "C2", "C3", "C8",
                 "K1", "K2", "K3", "K7", "E1", "E9", "E10"],
        "comprehensive": ["A1", "A2", "A3", "A4", "A5", "A6", "A8", "S1", "S2", "S3", "S5",
                         "S7", "C1", "C2", "C3", "C4", "C5", "C8", "K1", "K2", "K3", "K4",
                         "K7", "K8", "E1", "E5", "E9", "E10", "E11"]
    }

    selected = depth_hotkeys.get(depth, depth_hotkeys["standard"])

    # Add platform-specific hotkeys
    if focus_areas:
        for area in focus_areas:
            area_lower = area.lower()
            if "character" in area_lower:
                selected.extend(["C6", "C7", "C9", "C10"])
            if "cinematography" in area_lower:
                selected.extend(["K5", "K6", "K11", "K12"])
            if "story" in area_lower:
                selected.extend(["S6", "S8", "S11"])

    return list(dict.fromkeys(selected))  # Remove duplicates while preserving order

def generate_prompt_sections(content: str, hotkeys: List[str],
                            platform: Optional[str] = None,
                            reference_style: Optional[str] = None) -> Dict[str, str]:
    """Generate prompt sections based on selected hotkeys"""

    sections = {
        "core_description": content,
        "visual_elements": [],
        "narrative_elements": [],
        "character_details": [],
        "cinematography": [],
        "platform_specs": [],
        "technical_specs": []
    }

    for hotkey in hotkeys:
        category = hotkey[0]
        description = HOTKEYS.get(hotkey, "")

        if category == "A":
            sections["visual_elements"].append(f"• {description}")
        elif category == "S":
            sections["narrative_elements"].append(f"• {description}")
        elif category == "C":
            sections["character_details"].append(f"• {description}")
        elif category == "K":
            sections["cinematography"].append(f"• {description}")
        elif category == "P":
            sections["platform_specs"].append(f"• {description}")
        elif category == "E":
            sections["technical_specs"].append(f"• {description}")

    # Add platform-specific guidance
    if platform:
        platform_guides = {
            "TikTok": "Vertical 9:16, hook in first 3 seconds, trending audio, fast-paced",
            "Instagram": "Square/vertical, aesthetic-first, grid integration, story-friendly",
            "YouTube": "16:9, thumbnail-optimized, retention hooks, SEO-friendly",
            "Cinema": "Cinematic 2.39:1, theatrical quality, story depth, artistic expression"
        }
        sections["platform_guidance"] = platform_guides.get(platform, "")

    if reference_style:
        sections["style_reference"] = reference_style

    return sections

def format_prompt_output(sections: Dict[str, str], format_type: str) -> str:
    """Format the analysis output"""

    if format_type == "json":
        return json.dumps(sections, indent=2)

    # Markdown format
    output = []
    output.append("# 🎬 AI Video Generation Prompt\n")

    output.append("## Core Vision\n")
    output.append(f"{sections['core_description']}\n")

    if sections.get("style_reference"):
        output.append("## Style Reference\n")
        output.append(f"{sections['style_reference']}\n")

    if sections["visual_elements"]:
        output.append("## Visual Elements\n")
        output.extend(sections["visual_elements"])
        output.append("")

    if sections["narrative_elements"]:
        output.append("## Narrative & Story\n")
        output.extend(sections["narrative_elements"])
        output.append("")

    if sections["character_details"]:
        output.append("## Character Details\n")
        output.extend(sections["character_details"])
        output.append("")

    if sections["cinematography"]:
        output.append("## Cinematography\n")
        output.extend(sections["cinematography"])
        output.append("")

    if sections.get("platform_guidance"):
        output.append("## Platform Optimization\n")
        output.append(f"{sections['platform_guidance']}\n")

    if sections["technical_specs"]:
        output.append("## Technical Specifications\n")
        output.extend(sections["technical_specs"])
        output.append("")

    output.append("\n---\n")
    output.append(f"*Generated by Enhanced Multimedia Analysis MCP*")
    output.append(f"*Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    result = "\n".join(output)

    # Enforce character limit
    if len(result) > CHAR_LIMIT:
        result = result[:CHAR_LIMIT] + "\n\n[Output truncated to character limit]"

    return result

# ============================================================================
# CACHING SYSTEM
# ============================================================================

def generate_cache_key(params: Dict[str, Any]) -> str:
    """Generate cache key from parameters"""
    key_string = json.dumps(params, sort_keys=True)
    return hashlib.sha256(key_string.encode()).hexdigest()

def get_cached_result(cache_key: str) -> Optional[str]:
    """Retrieve cached result if available"""
    if not CACHE_ENABLED:
        return None

    try:
        cache_file = os.path.join(CACHE_DIR, f"{cache_key}.json")
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cached = json.load(f)
                if cached.get('expires_at', 0) > datetime.now().timestamp():
                    logger.debug(f"Cache hit: {cache_key}")
                    return cached.get('result')
    except Exception as e:
        logger.warning(f"Cache read error: {e}")

    return None

def save_to_cache(cache_key: str, result: str, params: Dict[str, Any]) -> None:
    """Save result to cache"""
    if not CACHE_ENABLED:
        return

    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        cache_entry = {
            "cache_key": cache_key,
            "created_at": datetime.now().isoformat(),
            "expires_at": datetime.now().timestamp() + CACHE_TTL,
            "parameters": params,
            "result": result
        }
        cache_file = os.path.join(CACHE_DIR, f"{cache_key}.json")
        with open(cache_file, 'w') as f:
            json.dump(cache_entry, f, indent=2)
        logger.debug(f"Cached result: {cache_key}")
    except Exception as e:
        logger.warning(f"Cache write error: {e}")

# ============================================================================
# MCP TOOLS
# ============================================================================

@mcp.tool()
def video_analysis_analyze_image(
    content_description: str,
    analysis_depth: str = "standard",
    target_platform: Optional[str] = None,
    focus_areas: Optional[str] = None,
    hotkeys: Optional[str] = None,
    reference_style: Optional[str] = None,
    response_format: str = "markdown"
) -> str:
    """
    Analyze an image description and generate an optimized AI image generation prompt.

    Args:
        content_description: Description of the image content
        analysis_depth: Depth of analysis (quick, standard, deep, comprehensive)
        target_platform: Target platform (TikTok, Instagram, YouTube, Cinema)
        focus_areas: Comma-separated focus areas
        hotkeys: Comma-separated hotkey codes
        reference_style: Reference style or inspiration
        response_format: Output format (markdown, json)

    Returns:
        Formatted prompt and analysis
    """
    logger.info(f"Image analysis requested: depth={analysis_depth}")

    # Parse comma-separated inputs
    focus_list = [f.strip() for f in focus_areas.split(",")] if focus_areas else None
    hotkey_list = [h.strip() for h in hotkeys.split(",")] if hotkeys else None

    # Check cache
    cache_params = {
        "content": content_description,
        "depth": analysis_depth,
        "platform": target_platform,
        "hotkeys": hotkey_list
    }
    cache_key = generate_cache_key(cache_params)
    cached_result = get_cached_result(cache_key)
    if cached_result:
        return cached_result

    # Select hotkeys
    selected_hotkeys = select_hotkeys_for_depth(analysis_depth, focus_list, hotkey_list)

    # Generate prompt sections
    sections = generate_prompt_sections(
        content_description,
        selected_hotkeys,
        target_platform,
        reference_style
    )

    # Format output
    result = format_prompt_output(sections, response_format)

    # Cache result
    save_to_cache(cache_key, result, cache_params)

    return result

@mcp.tool()
def video_analysis_analyze_video(
    content_description: str,
    analysis_depth: str = "standard",
    target_platform: Optional[str] = None,
    focus_areas: Optional[str] = None,
    hotkeys: Optional[str] = None,
    reference_style: Optional[str] = None,
    response_format: str = "markdown"
) -> str:
    """
    Analyze a video description and generate an optimized AI video generation prompt.

    Args:
        content_description: Description of the video content
        analysis_depth: Depth of analysis (quick, standard, deep, comprehensive)
        target_platform: Target platform (TikTok, Instagram, YouTube, Cinema)
        focus_areas: Comma-separated focus areas
        hotkeys: Comma-separated hotkey codes
        reference_style: Reference style or inspiration
        response_format: Output format (markdown, json)

    Returns:
        Formatted prompt and analysis
    """
    logger.info(f"Video analysis requested: depth={analysis_depth}")

    # Parse comma-separated inputs
    focus_list = [f.strip() for f in focus_areas.split(",")] if focus_areas else None
    hotkey_list = [h.strip() for h in hotkeys.split(",")] if hotkeys else None

    # Check cache
    cache_params = {
        "content": content_description,
        "depth": analysis_depth,
        "platform": target_platform,
        "hotkeys": hotkey_list,
        "type": "video"
    }
    cache_key = generate_cache_key(cache_params)
    cached_result = get_cached_result(cache_key)
    if cached_result:
        return cached_result

    # Select hotkeys (add more story/motion hotkeys for video)
    selected_hotkeys = select_hotkeys_for_depth(analysis_depth, focus_list, hotkey_list)
    if "S4" not in selected_hotkeys:
        selected_hotkeys.append("S4")  # Pacing
    if "K3" not in selected_hotkeys:
        selected_hotkeys.append("K3")  # Camera movement

    # Generate prompt sections
    sections = generate_prompt_sections(
        content_description,
        selected_hotkeys,
        target_platform,
        reference_style
    )

    # Format output
    result = format_prompt_output(sections, response_format)

    # Cache result
    save_to_cache(cache_key, result, cache_params)

    return result

@mcp.tool()
def video_analysis_analyze_multimedia(
    content_description: str,
    analysis_depth: str = "standard",
    target_platform: Optional[str] = None,
    focus_areas: Optional[str] = None,
    hotkeys: Optional[str] = None,
    reference_style: Optional[str] = None,
    response_format: str = "markdown"
) -> str:
    """
    Analyze multimedia content (image + video hybrid) and generate optimized prompts.

    This is useful for projects that need both static images and video sequences.

    Args:
        content_description: Description of the multimedia content
        analysis_depth: Depth of analysis (quick, standard, deep, comprehensive)
        target_platform: Target platform (TikTok, Instagram, YouTube, Cinema)
        focus_areas: Comma-separated focus areas
        hotkeys: Comma-separated hotkey codes
        reference_style: Reference style or inspiration
        response_format: Output format (markdown, json)

    Returns:
        Formatted prompt and analysis for both image and video generation
    """
    logger.info(f"Multimedia analysis requested: depth={analysis_depth}")

    # Parse comma-separated inputs
    focus_list = [f.strip() for f in focus_areas.split(",")] if focus_areas else None
    hotkey_list = [h.strip() for h in hotkeys.split(",")] if hotkeys else None

    # Select comprehensive hotkeys
    selected_hotkeys = select_hotkeys_for_depth(analysis_depth, focus_list, hotkey_list)

    # Generate prompt sections
    sections = generate_prompt_sections(
        content_description,
        selected_hotkeys,
        target_platform,
        reference_style
    )

    # Format output with both image and video guidance
    result = format_prompt_output(sections, response_format)

    return result

@mcp.tool()
def video_analysis_get_hotkeys(category: Optional[str] = None) -> str:
    """
    Get available hotkeys and their descriptions.

    Args:
        category: Optional category filter (A, S, C, K, P, E)

    Returns:
        List of hotkeys with descriptions
    """
    logger.info(f"Hotkey list requested: category={category}")

    output = ["# 🎯 Available Hotkeys\n"]

    if category:
        category = category.upper()
        if category in HOTKEY_CATEGORIES:
            output.append(f"## {category}-Series: {HOTKEY_CATEGORIES[category]}\n")
            for key, desc in HOTKEYS.items():
                if key.startswith(category):
                    output.append(f"**{key}**: {desc}")
        else:
            return f"Unknown category: {category}. Valid categories: {', '.join(HOTKEY_CATEGORIES.keys())}"
    else:
        for cat, cat_name in HOTKEY_CATEGORIES.items():
            output.append(f"## {cat}-Series: {cat_name}\n")
            for key, desc in HOTKEYS.items():
                if key.startswith(cat):
                    output.append(f"**{key}**: {desc}")
            output.append("")

    return "\n".join(output)

# ============================================================================
# HEALTH CHECK
# ============================================================================

def health_check() -> bool:
    """Health check for monitoring"""
    try:
        # Check if hotkeys are loaded
        if not HOTKEYS:
            return False
        # Check cache directory if enabled
        if CACHE_ENABLED and not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return False

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run the MCP server"""
    logger.info("Starting Enhanced Multimedia Analysis MCP Server v1.1.0")
    logger.info(f"Character limit: {CHAR_LIMIT}")
    logger.info(f"Debug mode: {DEBUG}")
    logger.info(f"Cache enabled: {CACHE_ENABLED}")

    # Run health check
    if not health_check():
        logger.error("Health check failed!")
        sys.exit(1)

    logger.info("Server ready")

    # Run the MCP server
    mcp.run()

if __name__ == "__main__":
    main()
