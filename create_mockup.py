#!/usr/bin/env python3
"""
Create a PNG canvas mockup for balans.ca redesign
Based on: Sovereign Minimalism design philosophy
References: Thinking Machines (side footnotes), Designboom (orange), Polestar (typography)
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ============================================
# CANVAS SETUP
# ============================================

# Page dimensions (A4 landscape for wide layout)
WIDTH = 1920
HEIGHT = 1080
BACKGROUND = (255, 255, 255)  # White

# Create canvas
img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
draw = ImageDraw.Draw(img)

# ============================================
# DESIGN SYSTEM (from your requirements)
# ============================================

# Colors
ORANGE = (191, 54, 12)      # #BF360C - Designboom orange
BLACK = (0, 0, 0)           # Primary
SECONDARY = (51, 51, 51)     # #333333
TERTIARY = (117, 117, 117)   # #757575
LIGHT_GREY = (224, 224, 224) # #E0E0E0 - Polestar light grey
WHITE = (255, 255, 255)

# Typography scale (Polestar inspired)
TITLE_SIZE = 140      # 70pt
H1_SIZE = 60         # 30pt
H2_SIZE = 40         # 20pt
H3_SIZE = 32         # 16pt
BODY_SIZE = 32       # 16pt

# Layout dimensions
TOC_WIDTH = 300       # Left column
MAIN_WIDTH = 800      # Center column
FOOTNOTES_WIDTH = 300 # Right column
GUTTER = 80          # Spacing between columns

# Padding
PADDING_LG = 120     # Large padding
PADDING_MD = 80      # Medium padding
PADDING_SM = 40      # Small padding

# ============================================
# LOAD FONTS
# ============================================

def load_font(size, weight='regular'):
    """Load font with fallback"""
    font_paths = [
        '/Users/tytan/.agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Regular.ttf',
        '/Users/tytan/.agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf',
        '/Users/tytan/.agents/skills/canvas-design/canvas-fonts/BigShoulders-Regular.ttf',
        '/Users/tytan/.agents/skills/canvas-design/canvas-fonts/ArsenalSC-Regular.ttf',
    ]
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                if 'Bold' in path and weight == 'bold':
                    return ImageFont.truetype(path, size)
                elif 'Regular' in path:
                    return ImageFont.truetype(path, size)
            except:
                pass
    
    # Fallback to system fonts
    if weight == 'bold':
        return ImageFont.truetype("/System/Library/Fonts/Helvetica Bold.ttf", size) if os.path.exists("/System/Library/Fonts/Helvetica Bold.ttf") else ImageFont.load_default()
    return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttf", size) if os.path.exists("/System/Library/Fonts/Helvetica.ttf") else ImageFont.load_default()

# Load fonts
font_title = load_font(TITLE_SIZE, 'bold')
font_h1 = load_font(H1_SIZE, 'bold')
font_h2 = load_font(H2_SIZE, 'bold')
font_body = load_font(BODY_SIZE)
font_small = load_font(H3_SIZE)

# ============================================
# DRAW HEADER / TITLE BLOCK
# ============================================

def draw_header():
    """Full-width title header with border"""
    header_height = 200
    
    # Draw header background (full width)
    draw.rectangle([0, 0, WIDTH, header_height], fill=WHITE, outline=LIGHT_GREY, width=1)
    
    # Title
    title = "Balans"
    title_width = draw.textlength(title, font=font_title)
    title_x = (WIDTH - title_width) / 2
    title_y = 60
    draw.text((title_x, title_y), title, fill=BLACK, font=font_title)
    
    # Tagline
    tagline = "AI/ML Engineering for Government Modernization"
    tagline_width = draw.textlength(tagline, font=font_h2)
    tagline_x = (WIDTH - tagline_width) / 2
    tagline_y = 140
    draw.text((tagline_x, tagline_y), tagline, fill=ORANGE, font=font_h2)

# ============================================
# DRAW TOC (Left Column)
# ============================================

def draw_toc():
    """Table of contents in left column"""
    toc_x = PADDING_LG
    toc_y_start = 220
    toc_width = TOC_WIDTH - PADDING_MD
    
    # TOC header
    toc_header = "Table of Contents"
    draw.text((toc_x, toc_y_start), toc_header, fill=ORANGE, font=font_small)
    
    # TOC items
    toc_items = [
        "AI/ML Engineering for Government Modernization",
        "Choose Balans When",
        "Why Government Modernization Needs a New Approach",
        "What We Deliver",
        "Service Tiers",
        "Get Started"
    ]
    
    y = toc_y_start + 40
    for item in toc_items:
        # Active state for first item
        if item == toc_items[0]:
            draw.text((toc_x, y), item, fill=ORANGE, font=font_body)
            # Orange border indicator
            draw.line([toc_x - 10, y + 5, toc_x - 10, y + 35], fill=ORANGE, width=2)
        else:
            draw.text((toc_x, y), item, fill=SECONDARY, font=font_body)
        y += 40
    
    # Right border for TOC column
    draw.line([toc_x + TOC_WIDTH - 20, 220, toc_x + TOC_WIDTH - 20, HEIGHT - 200], fill=LIGHT_GREY, width=1)

# ============================================
# DRAW MAIN CONTENT (Center Column)
# ============================================

def draw_main_content():
    """Main content area with orange headings"""
    main_x = PADDING_LG + TOC_WIDTH + GUTTER
    main_y_start = 220
    main_width = MAIN_WIDTH
    
    # Section 1
    y = main_y_start
    heading = "AI/ML Engineering for Government Modernization"
    draw.text((main_x, y), heading, fill=ORANGE, font=font_h1)
    y += 70
    
    body_text = "Balans delivers sovereign, project-based data and AI solutions for public sector institutions."
    draw.text((main_x, y), body_text, fill=SECONDARY, font=font_body)
    y += 50
    
    # Section 2
    heading = "Why Government Modernization Needs a New Approach"
    draw.text((main_x, y), heading, fill=ORANGE, font=font_h1)
    y += 70
    
    body_text = "Traditional government IT modernization is sold as a platform, a subscription, a dashboard..."
    draw.text((main_x, y), body_text, fill=SECONDARY, font=font_body)
    y += 50
    
    # Section 3
    heading = "What We Deliver"
    draw.text((main_x, y), heading, fill=ORANGE, font=font_h1)
    y += 70
    
    body_text = "Fix the data, make it actionable, add on advanced capabilities..."
    draw.text((main_x, y), body_text, fill=SECONDARY, font=font_body)
    
    # Show more content below
    y += 80
    heading = "Service Tiers"
    draw.text((main_x, y), heading, fill=ORANGE, font=font_h1)
    y += 70
    
    body_text = "Every engagement is scoped before it's priced..."
    draw.text((main_x, y), body_text, fill=SECONDARY, font=font_body)

# ============================================
# DRAW FOOTNOTES (Right Column)
# ============================================

def draw_footnotes():
    """Footnotes in right column"""
    fn_x = PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH + GUTTER
    fn_y_start = 220
    fn_width = FOOTNOTES_WIDTH - PADDING_MD
    
    # Footnotes header
    fn_header = "Footnotes"
    draw.text((fn_x, fn_y_start), fn_header, fill=ORANGE, font=font_small)
    
    # Sample footnote
    y = fn_y_start + 40
    draw.text((fn_x, y), "1. Balans is a disability-owned business...", fill=TERTIARY, font=font_small)
    y += 30
    draw.text((fn_x, y), "2. Working with us helps you meet...", fill=TERTIARY, font=font_small)
    
    # Left border for footnotes column
    draw.line([fn_x - 10, 220, fn_x - 10, HEIGHT - 200], fill=LIGHT_GREY, width=1)

# ============================================
# DRAW FOOTER
# ============================================

def draw_footer():
    """Clean footer at bottom"""
    footer_y = HEIGHT - 100
    
    # Footer background
    draw.rectangle([0, footer_y, WIDTH, HEIGHT], fill=WHITE, outline=LIGHT_GREY, width=1)
    
    # Footer text
    footer_text = "© 2026 Balans | Adam, Principal"
    footer_width = draw.textlength(footer_text, font=font_small)
    footer_x = (WIDTH - footer_width) / 2
    draw.text((footer_x, footer_y + 30), footer_text, fill=TERTIARY, font=font_small)

# ============================================
# DRAW GRID GUIDES (subtle)
# ============================================

def draw_grid_guides():
    """Draw subtle grid lines to show layout"""
    # Vertical guides (solid but light)
    draw.line([PADDING_LG, 0, PADDING_LG, HEIGHT], fill=(240, 240, 240), width=1)
    draw.line([PADDING_LG + TOC_WIDTH, 0, PADDING_LG + TOC_WIDTH, HEIGHT], fill=(240, 240, 240), width=1)
    draw.line([PADDING_LG + TOC_WIDTH + GUTTER, 0, PADDING_LG + TOC_WIDTH + GUTTER, HEIGHT], fill=(240, 240, 240), width=1)
    draw.line([PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH, 0, PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH, HEIGHT], fill=(240, 240, 240), width=1)
    draw.line([PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH + GUTTER, 0, PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH + GUTTER, HEIGHT], fill=(240, 240, 240), width=1)
    draw.line([PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH + GUTTER + FOOTNOTES_WIDTH, 0, PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH + GUTTER + FOOTNOTES_WIDTH, HEIGHT], fill=(240, 240, 240), width=1)

# ============================================
# DRAW ARROW ELEMENTS (Polestar inspired)
# ============================================

def draw_arrows():
    """Add subtle arrow elements as visual accents"""
    # Arrow in main content area
    arrow_x = PADDING_LG + TOC_WIDTH + GUTTER + MAIN_WIDTH - 50
    arrow_y = 400
    
    # Draw arrow shape
    arrow_points = [
        (arrow_x, arrow_y),
        (arrow_x + 20, arrow_y),
        (arrow_x + 20, arrow_y - 10),
        (arrow_x + 30, arrow_y + 5),
        (arrow_x + 20, arrow_y + 10),
        (arrow_x + 20, arrow_y + 20),
        (arrow_x, arrow_y + 20)
    ]
    draw.polygon(arrow_points, fill=ORANGE)

# ============================================
# ASSEMBLE CANVAS
# ============================================

draw_header()
draw_toc()
draw_main_content()
draw_footnotes()
draw_footer()
draw_grid_guides()
draw_arrows()

# ============================================
# SAVE AND DISPLAY
# ============================================

output_path = '/Users/tytan/Projects/balans-ca/balans-mockup.png'
img.save(output_path)
print(f"✅ Canvas saved to: {output_path}")
print(f"Dimensions: {WIDTH}x{HEIGHT} pixels")
print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")
