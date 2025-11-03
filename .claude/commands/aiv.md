---
description: Activate Enhanced Multimedia Analysis MCP for instant AI video/image generation prompts
---

# 🎬 Enhanced Multimedia Analysis Activated

You are now operating in **Enhanced Multimedia Analysis Mode** using the MCP video analysis tools.

## Your Task

Analyze the user's visual content description and generate a professional AI video/image generation prompt using the systematic hotkey-based analysis framework.

## Process

1. **Parse the user's input** and extract:
   - Core visual description
   - Any options provided (depth, platform, focus, format, hotkeys, style)

2. **Determine content type**:
   - Image description → use `video_analysis_analyze_image`
   - Video description → use `video_analysis_analyze_video`
   - Both image and video → use `video_analysis_analyze_multimedia`

3. **Extract options from input**:
   - `--depth [quick|standard|deep|comprehensive]` (default: standard)
   - `--platform [TikTok|Instagram|YouTube|Cinema]`
   - `--focus [comma-separated areas]`
   - `--format [markdown|json]` (default: markdown)
   - `--hotkeys [comma-separated list]`
   - `--style "reference style"`

4. **Call the appropriate MCP tool** with parameters:
   ```python
   {
     "content_description": "[extracted description]",
     "analysis_depth": "[extracted or default]",
     "target_platform": "[if specified]",
     "focus_areas": "[if specified]",
     "hotkeys": "[if specified]",
     "reference_style": "[if specified]",
     "response_format": "[extracted or default]"
   }
   ```

5. **Return the optimized prompt** directly to the user

## Option Parsing Examples

**Input:** `/aiv sunset over mountains --depth quick`
- description: "sunset over mountains"
- depth: "quick"

**Input:** `/aiv product video --platform Instagram --focus camera movement, color grading`
- description: "product video"
- platform: "Instagram"
- focus_areas: ["camera movement", "color grading"]

**Input:** `/aiv character scene --hotkeys K1,K2,C1 --format json`
- description: "character scene"
- hotkeys: ["K1", "K2", "C1"]
- format: "json"

## Default Behavior

If no options specified:
- Use `analysis_depth: "standard"`
- Use `response_format: "markdown"`
- Let the MCP determine appropriate hotkeys

## Image-to-Video Detection

If input contains both image and video descriptions (keywords: "IMAGE:", "VIDEO:", "image" + "video"), use `video_analysis_analyze_multimedia`:

**Example:**
```
/aiv IMAGE: watercolor painting of garden VIDEO: gentle breeze, petals falling
```

Parse as:
```python
{
  "image_description": "watercolor painting of garden",
  "video_description": "gentle breeze, petals falling"
}
```

## Output

Present ONLY the final AI generation prompt to the user. Do not show:
- Your analysis process
- Tool selection reasoning
- Intermediate steps

Unless the user specifically asks to see your analysis.

---

**Now execute the analysis based on the user's input after /aiv**
