#!/bin/bash

# Enhanced Multimedia Analysis MCP - /aiv Command Installation Script
# Version: 1.1.0

set -e

echo "🎬 Enhanced Multimedia Analysis MCP - /aiv Installation"
echo "========================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Detect OS
OS="unknown"
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
    COMMANDS_DIR="$HOME/.claude/commands"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    CLAUDE_CONFIG_DIR="$HOME/.config/Claude"
    COMMANDS_DIR="$HOME/.claude/commands"
else
    echo -e "${RED}❌ Unsupported OS: $OSTYPE${NC}"
    exit 1
fi

echo -e "${BLUE}Detected OS: $OS${NC}"
echo ""

# Function to check if Claude Desktop is installed
check_claude_installed() {
    if [ "$OS" = "macos" ]; then
        if [ ! -d "/Applications/Claude.app" ]; then
            echo -e "${YELLOW}⚠️  Warning: Claude Desktop not found in /Applications${NC}"
            echo "   Please install Claude Desktop first"
            return 1
        fi
    fi
    return 0
}

# Function to create directories
create_directories() {
    echo -e "${BLUE}📁 Creating directories...${NC}"

    mkdir -p "$COMMANDS_DIR"
    echo -e "${GREEN}✅ Created: $COMMANDS_DIR${NC}"

    if [ ! -d "$CLAUDE_CONFIG_DIR" ]; then
        mkdir -p "$CLAUDE_CONFIG_DIR"
        echo -e "${GREEN}✅ Created: $CLAUDE_CONFIG_DIR${NC}"
    fi
}

# Function to install command file
install_command() {
    echo ""
    echo -e "${BLUE}📝 Installing /aiv command...${NC}"

    SOURCE_FILE="/home/dominicanmayan/.claude/commands/aiv.md"
    DEST_FILE="$COMMANDS_DIR/aiv.md"

    if [ ! -f "$SOURCE_FILE" ]; then
        echo -e "${RED}❌ Source file not found: $SOURCE_FILE${NC}"
        exit 1
    fi

    cp "$SOURCE_FILE" "$DEST_FILE"
    echo -e "${GREEN}✅ Installed: $DEST_FILE${NC}"
}

# Function to setup environment variables (optional)
setup_environment() {
    echo ""
    echo -e "${BLUE}🔧 Environment Variable Setup (Optional)${NC}"
    echo ""
    read -p "Enable caching for better performance? (y/N): " enable_cache

    if [[ "$enable_cache" =~ ^[Yy]$ ]]; then
        # Detect shell
        SHELL_CONFIG=""
        if [ -n "$ZSH_VERSION" ]; then
            SHELL_CONFIG="$HOME/.zshrc"
        elif [ -n "$BASH_VERSION" ]; then
            SHELL_CONFIG="$HOME/.bashrc"
        else
            echo -e "${YELLOW}⚠️  Could not detect shell. Please add environment variables manually.${NC}"
            return
        fi

        echo ""
        echo -e "${BLUE}Adding environment variables to $SHELL_CONFIG${NC}"

        # Backup shell config
        cp "$SHELL_CONFIG" "${SHELL_CONFIG}.backup.$(date +%Y%m%d_%H%M%S)"

        # Add environment variables
        cat >> "$SHELL_CONFIG" << 'EOF'

# Enhanced Multimedia Analysis MCP Configuration
export VIDEO_ANALYSIS_CACHE_ENABLED=true
export VIDEO_ANALYSIS_CACHE_DIR=/tmp/video_analysis_cache
export VIDEO_ANALYSIS_CACHE_TTL=3600
export VIDEO_ANALYSIS_CHAR_LIMIT=25000

EOF

        echo -e "${GREEN}✅ Environment variables added to $SHELL_CONFIG${NC}"
        echo -e "${YELLOW}⚠️  Run 'source $SHELL_CONFIG' or restart your terminal${NC}"
    fi
}

# Function to verify installation
verify_installation() {
    echo ""
    echo -e "${BLUE}🔍 Verifying installation...${NC}"

    if [ -f "$COMMANDS_DIR/aiv.md" ]; then
        echo -e "${GREEN}✅ /aiv command file installed${NC}"
    else
        echo -e "${RED}❌ /aiv command file not found${NC}"
        return 1
    fi

    return 0
}

# Function to show next steps
show_next_steps() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              🎉 Installation Complete! 🎉                ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}📋 Next Steps:${NC}"
    echo ""
    echo -e "  1. ${YELLOW}Restart Claude Desktop:${NC}"
    if [ "$OS" = "macos" ]; then
        echo "     killall Claude && open -a Claude"
    else
        echo "     killall Claude"
        echo "     (Then reopen Claude Desktop)"
    fi
    echo ""
    echo -e "  2. ${YELLOW}Test the /aiv command:${NC}"
    echo "     /aiv sunset over mountains with dramatic clouds"
    echo ""
    echo -e "  3. ${YELLOW}Try with options:${NC}"
    echo "     /aiv product video --platform Instagram --depth deep"
    echo ""
    echo -e "  4. ${YELLOW}Read full documentation:${NC}"
    echo "     cat /home/dominicanmayan/aiv_slash_command.md"
    echo ""
    echo -e "${BLUE}💡 Quick Tips:${NC}"
    echo "  • Use --depth quick for faster results"
    echo "  • Specify --platform for optimized output"
    echo "  • Use --focus to target specific aspects"
    echo "  • Add --format json for machine-readable output"
    echo ""
    echo -e "${GREEN}Happy Analyzing! 🎬✨${NC}"
    echo ""
}

# Main installation flow
main() {
    echo -e "${BLUE}Starting installation...${NC}"
    echo ""

    # Check if Claude is installed (optional check)
    if ! check_claude_installed; then
        echo ""
        read -p "Continue anyway? (y/N): " continue_anyway
        if [[ ! "$continue_anyway" =~ ^[Yy]$ ]]; then
            echo "Installation cancelled."
            exit 1
        fi
    fi

    # Create necessary directories
    create_directories

    # Install command file
    install_command

    # Setup environment (optional)
    setup_environment

    # Verify installation
    if ! verify_installation; then
        echo -e "${RED}❌ Installation verification failed${NC}"
        exit 1
    fi

    # Show next steps
    show_next_steps
}

# Run main installation
main
