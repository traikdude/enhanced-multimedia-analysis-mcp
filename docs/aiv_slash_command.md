# /aiv - AI Video Analysis Slash Command

**Command:** `/aiv`
**Full Name:** AI Video Analysis Activator
**Purpose:** Quick activation of Enhanced Multimedia Analysis MCP

---

## 🎯 What This Command Does

When you type `/aiv` followed by your visual content description, Claude will automatically:

1. Activate the Enhanced Multimedia Analysis MCP tools
2. Determine the appropriate analysis type (image/video/multimedia)
3. Execute systematic analysis using the hotkey framework
4. Generate a professional AI video/image generation prompt
5. Return only the optimized prompt (no intermediate analysis shown)

---

## 📝 Usage Syntax

### Basic Usage
```
/aiv [your visual content description]
```

### With Options
```
/aiv [description] --depth [quick|standard|deep|comprehensive]
```

```
/aiv [description] --platform [TikTok|Instagram|YouTube|Cinema]
```

```
/aiv [description] --focus [camera movement, color grading, character consistency]
```

---

## 💡 Examples

### Example 1: Simple Image
```
/aiv A majestic eagle soaring over snow-capped mountains at sunset, dramatic golden hour lighting, wings spread wide
```

**Result:** Detailed image generation prompt optimized for Midjourney/DALL-E

---

### Example 2: Video with Platform
```
/aiv 30-second coffee commercial. Steam rises from cup. Camera orbits slowly. Warm cozy morning atmosphere. --platform Instagram
```

**Result:** Video generation prompt optimized for Instagram Reels (vertical, 30s)

---

### Example 3: Character-Focused
```
/aiv Detective noir short film. Main character in 5 different city scenes. Needs consistent trench coat and fedora. --focus character consistency, cinematography
```

**Result:** Prompt with detailed CHARACTER CONSISTENCY guidelines

---

### Example 4: Quick Analysis
```
/aiv Futuristic cityscape at night with neon lights --depth quick
```

**Result:** Fast prompt generation with essential details only

---

## ⚙️ Command Options

### Depth Levels
- `--depth quick` - 2-3 seconds, essential analysis only
- `--depth standard` - 5-7 seconds, balanced (DEFAULT)
- `--depth deep` - 10-15 seconds, high-quality production
- `--depth comprehensive` - 20-30 seconds, maximum detail

### Platform Optimization
- `--platform TikTok` - 9:16 vertical, 15-60s, fast-paced
- `--platform Instagram` - 9:16 vertical, 15-90s, dynamic
- `--platform YouTube` - 16:9 horizontal, variable length, SEO-optimized
- `--platform Cinema` - Cinematic aspect ratio, artistic approach

### Focus Areas (comma-separated)
- `--focus camera movement`
- `--focus color grading`
- `--focus character consistency`
- `--focus cinematography`
- `--focus composition`
- `--focus lighting`
- `--focus pacing`
- `--focus narrative structure`

### Output Format
- `--format markdown` - Human-readable (DEFAULT)
- `--format json` - Machine-readable

### Custom Hotkeys
- `--hotkeys K1,K2,C1,P1` - Use specific analysis dimensions

---

## 🎬 Workflow Examples

### Workflow 1: Rapid Prototyping
```
/aiv [concept 1] --depth quick
/aiv [concept 2] --depth quick
/aiv [concept 3] --depth quick
[Review results, pick best]
/aiv [winning concept] --depth deep
```

### Workflow 2: Multi-Platform Content
```
/aiv [description] --platform TikTok
/aiv [same description] --platform Instagram
/aiv [same description] --platform YouTube
[Get optimized prompts for each platform]
```

### Workflow 3: Character-Driven Story
```
/aiv [scene 1] --focus character consistency --hotkeys K1,K2,K3
[Get character guidelines]
/aiv [scene 2] [using same character specs]
/aiv [scene 3] [using same character specs]
[Maintain visual consistency across all scenes]
```

---

## 🔧 Advanced Usage

### Combining Multiple Options
```
/aiv 15-second product reveal video with dynamic camera work and premium aesthetic --platform Instagram --depth deep --focus camera movement, color grading, lighting --format json
```

### Image-to-Video Animation
```
/aiv IMAGE: watercolor painting of Japanese garden with koi pond VIDEO: gentle breeze, petals falling, koi swimming, camera pans right --depth standard
```

### Style Reference
```
/aiv Portrait photograph, dramatic lighting, contemplative expression --style "Annie Leibovitz editorial style" --depth deep
```

---

## 📋 Behind the Scenes

When you use `/aiv`, the command:

1. **Parses your input** and extracts options
2. **Determines content type**:
   - Image only → calls `video_analysis_analyze_image`
   - Video description → calls `video_analysis_analyze_video`
   - Both specified → calls `video_analysis_analyze_multimedia`
3. **Selects appropriate hotkeys** based on depth and focus areas
4. **Executes analysis** using the 100+ dimension framework
5. **Generates prompt** with all relevant sections
6. **Formats output** according to your preference

---

## 🎯 Tips for Best Results

### Be Descriptive
```
❌ Bad: /aiv dog
✅ Good: /aiv Golden retriever puppy playing in autumn leaves, warm afternoon light, joyful expression
```

### Specify Platform for Videos
```
✅ /aiv [video description] --platform TikTok
```

### Use Focus for Targeted Analysis
```
✅ /aiv [description] --focus camera movement, color grading
[Faster processing, targeted results]
```

### Start Quick, Then Go Deep
```
1. /aiv [concept] --depth quick      # Get direction
2. /aiv [refined] --depth standard   # Refine details
3. /aiv [final] --depth deep         # Production ready
```

---

## 🆘 Troubleshooting

### "Command not recognized"
- Ensure MCP server is configured and running
- Check Claude Desktop configuration file
- Restart Claude Desktop

### "No output generated"
- Check your description is detailed enough
- Try adding more specific visual details
- Use `--depth standard` explicitly

### "Output too long"
- Use `--depth quick` or `--depth standard`
- Specify fewer `--focus` areas
- Use `--format json` for more compact output

---

## 🚀 Installation

### Step 1: Create Command File

Create this file at:
- **macOS/Linux:** `~/.claude/commands/aiv.md`
- **Windows:** `%USERPROFILE%\.claude\commands\aiv.md`

### Step 2: Add Command Definition

```markdown
---
description: Activate Enhanced Multimedia Analysis MCP for AI video/image generation prompts
---

You are now using the Enhanced Multimedia Analysis MCP system. Analyze the user's visual content description and generate a professional AI video/image generation prompt.

Use the video_analysis MCP tools:
- For images: video_analysis_analyze_image
- For videos: video_analysis_analyze_video
- For both: video_analysis_analyze_multimedia

Parse any options provided:
- --depth [level]
- --platform [name]
- --focus [areas]
- --format [type]
- --hotkeys [list]

Execute systematic analysis and return ONLY the final optimized prompt.
```

### Step 3: Restart Claude

```bash
killall Claude
# Then reopen
```

### Step 4: Test

```
/aiv A sunset over mountains with dramatic clouds
```

You should get a detailed prompt!

---

## 📚 Related Documentation

- **Full MCP Reference:** ENHANCED_MULTIMEDIA_ANALYSIS_MCP_MASTER.md
- **Tool Specifications:** Section 3 of master document
- **Hotkey System:** Section 5 of master document
- **Deployment Guide:** Section 6 of master document

---

## ✨ Quick Reference Card

```
COMMAND: /aiv

BASIC:
/aiv [description]

OPTIONS:
--depth quick|standard|deep|comprehensive
--platform TikTok|Instagram|YouTube|Cinema
--focus [area1, area2, area3]
--format markdown|json
--hotkeys [H1,H2,H3]
--style "reference style"

EXAMPLES:
/aiv sunset over mountains
/aiv product video --platform Instagram --depth deep
/aiv character scene --focus character consistency
/aiv quick concept --depth quick --format json
```

---

**Ready to create amazing AI generation prompts with a single command!** 🎬✨
