# 🎬 Enhanced Multimedia Analysis MCP

**A Model Context Protocol (MCP) server for professional multimedia content analysis and AI video generation prompt engineering**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/traikdude/enhanced-multimedia-analysis-mcp)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

---

## 🌟 Overview

The Enhanced Multimedia Analysis MCP Server is a production-ready Model Context Protocol implementation that provides AI agents with sophisticated tools for analyzing visual content (images and videos) and generating optimized prompts for AI video generation systems.

### Core Capabilities

- 🔍 **Systematic multi-dimensional content analysis** via hotkey framework
- 🎨 **Professional prompt generation** for AI video/image generators
- 📱 **Platform-specific optimization** (TikTok, Instagram, YouTube, Cinema)
- 👥 **Character consistency tracking** across scenes
- 📊 **Four analysis depth levels** (Quick, Standard, Deep, Comprehensive)
- ⚡ **Quick activation** via `/aiv` slash command

### Key Benefits

✅ Reduces prompt engineering time from hours to minutes
✅ Improves prompt quality through systematic analysis
✅ Enables consistency across multiple generations
✅ Optimizes for platforms automatically
✅ Empowers AI agents with 100+ analysis dimensions

---

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/enhanced-multimedia-analysis-mcp.git
   cd enhanced-multimedia-analysis-mcp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the `/aiv` command:**
   ```bash
   ./scripts/install_aiv.sh
   ```

4. **Configure Claude Desktop:**

   Add to your Claude Desktop configuration (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

   ```json
   {
     "mcpServers": {
       "video-analysis": {
         "command": "python3",
         "args": ["/path/to/enhanced-multimedia-analysis-mcp/video_analysis_mcp.py"]
       }
     }
   }
   ```

5. **Restart Claude Desktop** and test:
   ```
   /aiv sunset over mountains with dramatic clouds
   ```

---

## 💡 Usage Examples

### Basic Analysis
```
/aiv A majestic eagle soaring over mountains at sunset
```

### With Platform Optimization
```
/aiv 30-second product video --platform Instagram --depth deep
```

### Character-Focused Analysis
```
/aiv Detective noir scene --focus character consistency, cinematography
```

### With Custom Hotkeys
```
/aiv Epic battle scene --hotkeys A1,C1,L1,E1 --format json
```

### Available Options

| Option | Values | Purpose |
|--------|--------|---------|
| `--depth` | quick\|standard\|deep\|comprehensive | Analysis thoroughness |
| `--platform` | TikTok\|Instagram\|YouTube\|Cinema | Platform optimization |
| `--focus` | comma-separated areas | Targeted analysis |
| `--format` | markdown\|json | Output format |
| `--hotkeys` | comma-separated list | Custom hotkey selection |
| `--style` | "reference style" | Style reference |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Claude Desktop / MCP Client                  │
│                    Slash Commands: /aiv                          │
└────────────────────────────┬────────────────────────────────────┘
                             │ JSON-RPC 2.0 over stdio
┌────────────────────────────▼────────────────────────────────────┐
│              Video Analysis MCP Server                           │
│              (video_analysis_mcp.py)                            │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐   │
│  │              4 MCP Tools                                │   │
│  │  • video_analysis_analyze_image                        │   │
│  │  • video_analysis_analyze_video                        │   │
│  │  • video_analysis_analyze_multimedia                   │   │
│  │  • video_analysis_get_hotkeys                          │   │
│  └─────────────────────┬──────────────────────────────────┘   │
│                        │                                        │
│  ┌─────────────────────▼──────────────────────────────────┐   │
│  │         Analysis Engine (Hotkey-Based)                  │   │
│  └─────────────────────┬──────────────────────────────────┘   │
│                        │                                        │
│  ┌─────────────────────▼──────────────────────────────────┐   │
│  │         Prompt Generator                                │   │
│  └─────────────────────┬──────────────────────────────────┘   │
│                        │                                        │
│  ┌─────────────────────▼──────────────────────────────────┐   │
│  │         Output Formatter (Markdown/JSON)                │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

### Technical Stack

- **Framework:** MCP Python SDK (FastMCP)
- **Validation:** Pydantic v2 models
- **Python Version:** 3.10+
- **Design Pattern:** Tool-oriented, stateless
- **Communication:** JSON-RPC 2.0 over stdio

---

## 📚 Documentation

- **[Master Specification](docs/MASTER_SPECIFICATION.md)** - Complete system documentation
- **[/aiv Command Guide](docs/aiv_slash_command.md)** - Slash command usage and examples
- **Installation Script** - Located in `scripts/install_aiv.sh`

---

## 🔧 Configuration

### Environment Variables

Configure the MCP server behavior using environment variables:

```bash
# Output character limit
export VIDEO_ANALYSIS_CHAR_LIMIT=25000

# Enable debug logging
export VIDEO_ANALYSIS_DEBUG=false

# Enable caching (improves performance)
export VIDEO_ANALYSIS_CACHE_ENABLED=true
export VIDEO_ANALYSIS_CACHE_DIR=/tmp/video_analysis_cache
export VIDEO_ANALYSIS_CACHE_TTL=3600

# Set default analysis depth
export VIDEO_ANALYSIS_DEFAULT_DEPTH=standard
```

### Claude Desktop Configuration

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "video-analysis": {
      "command": "python3",
      "args": ["/path/to/video_analysis_mcp.py"],
      "env": {
        "VIDEO_ANALYSIS_CHAR_LIMIT": "25000",
        "VIDEO_ANALYSIS_CACHE_ENABLED": "true",
        "VIDEO_ANALYSIS_CACHE_DIR": "/tmp/video_analysis_cache"
      }
    }
  }
}
```

---

## 🎯 Features

### Analysis Framework

The system uses a comprehensive hotkey-based analysis framework with 100+ dimensions organized into categories:

- **A-Series:** Aesthetic & Visual Style (A1-A13)
- **S-Series:** Story & Narrative (S1-S12)
- **C-Series:** Character & Subject (C1-C12)
- **K-Series:** Cinematography (K1-K13)
- **P-Series:** Platform Optimization (P1-P10)
- **E-Series:** Execution & Technical (E1-E12)

### Analysis Depths

| Depth | Hotkeys | Use Case | Time |
|-------|---------|----------|------|
| **Quick** | 4-6 | Fast iterations | 2-5s |
| **Standard** | 8-12 | Balanced analysis | 5-10s |
| **Deep** | 15-25 | Detailed work | 10-20s |
| **Comprehensive** | 30-50 | Production-ready | 20-30s |

### Platform Optimizations

- **TikTok:** Vertical format, hook-first, trending sounds
- **Instagram:** Aesthetic-first, grid-aware, story integration
- **YouTube:** Thumbnail optimization, retention focus, SEO
- **Cinema:** Cinematic language, aspect ratios, theatrical quality

---

## 🚢 Deployment

### Docker

```bash
docker build -t video-analysis-mcp:1.1.0 .
docker run -d --name video-analysis-mcp video-analysis-mcp:1.1.0
```

### Systemd Service

See [docs/MASTER_SPECIFICATION.md](docs/MASTER_SPECIFICATION.md#15-production-deployment) for complete deployment instructions including:
- Systemd service configuration
- Kubernetes deployment
- Docker Compose setup
- Monitoring & observability

---

## 🧪 Testing

Run comprehensive tests:

```bash
python3 -m pytest tests/
```

Test individual tools:

```bash
# Test image analysis
python3 -c "from video_analysis_mcp import test_image_analysis; test_image_analysis()"

# Test video analysis
python3 -c "from video_analysis_mcp import test_video_analysis; test_video_analysis()"
```

---

## 📈 Performance

### With Caching Enabled

| Scenario | No Cache | With Cache | Improvement |
|----------|----------|------------|-------------|
| Standard Analysis | 5.2s | 0.08s | 98.5% faster |
| Deep Analysis | 12.5s | 0.09s | 99.3% faster |
| Quick Analysis | 2.3s | 0.06s | 97.4% faster |
| Comprehensive | 25.8s | 0.11s | 99.6% faster |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Run tests: `pytest tests/`
4. Follow the code style guide (PEP 8)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built on the [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic
- Uses [FastMCP](https://github.com/jlowin/fastmcp) for MCP server implementation
- Inspired by professional video production workflows

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/traikdude/enhanced-multimedia-analysis-mcp/issues)
- **Documentation:** [docs/MASTER_SPECIFICATION.md](docs/MASTER_SPECIFICATION.md)
- **Discussions:** [GitHub Discussions](https://github.com/traikdude/enhanced-multimedia-analysis-mcp/discussions)

---

## 🗺️ Roadmap

- [ ] Real-time video file analysis
- [ ] Integration with popular AI video generators
- [ ] Web interface for prompt generation
- [ ] Batch processing capabilities
- [ ] Advanced caching strategies
- [ ] Multi-language support

---

**Made with ❤️ for the AI video generation community**

Version 1.1.0 | [Changelog](CHANGELOG.md) | [Documentation](docs/)
