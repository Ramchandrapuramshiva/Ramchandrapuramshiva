"""
terminal-animation-source.py
Generates an optimized, high-fidelity animated GIF simulating a developer terminal command center
for Shiva Ramchandrapuram's GitHub profile.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH = 840
HEIGHT = 460
BG_COLOR = (13, 17, 23)        # GitHub Dark canvas
HEADER_BG = (22, 27, 34)       # GitHub Dark secondary
BORDER_COLOR = (48, 54, 61)    # GitHub Dark border
TEXT_COLOR = (230, 237, 243)   # GitHub primary text
MUTED_COLOR = (139, 148, 158)  # GitHub muted text
ACCENT_GREEN = (63, 185, 80)   # Green terminal accent (#3fb950)
ACCENT_BLUE = (88, 166, 255)   # Cyan / Blue accent (#58a6ff)
ACCENT_PURPLE = (210, 168, 255)# Purple accent (#d2a8ff)
ACCENT_YELLOW = (227, 179, 65) # Yellow accent (#e3b341)
ACCENT_ORANGE = (255, 166, 87) # Orange accent (#ffa657)

# Fonts
FONT_PATH = "C:/Windows/Fonts/consola.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/consolab.ttf"

font_regular = ImageFont.truetype(FONT_PATH, 15)
font_bold = ImageFont.truetype(FONT_BOLD_PATH, 15)
font_small = ImageFont.truetype(FONT_PATH, 13)
font_title = ImageFont.truetype(FONT_BOLD_PATH, 13)


def draw_window_frame(draw):
    # Rounded container outline
    draw.rounded_rectangle([0, 0, WIDTH - 1, HEIGHT - 1], radius=10, fill=BG_COLOR, outline=BORDER_COLOR, width=1)
    # Header bar
    draw.rounded_rectangle([0, 0, WIDTH - 1, 38], radius=10, fill=HEADER_BG)
    draw.rectangle([0, 28, WIDTH - 1, 38], fill=HEADER_BG)
    draw.line([(0, 38), (WIDTH - 1, 38)], fill=BORDER_COLOR, width=1)
    
    # macOS / Linux terminal window controls
    # Red
    draw.ellipse([16, 13, 28, 25], fill=(255, 95, 86))
    # Yellow
    draw.ellipse([36, 13, 48, 25], fill=(255, 189, 46))
    # Green
    draw.ellipse([56, 13, 68, 25], fill=(39, 201, 63))
    
    # Terminal Title centered
    title = "shiva@dev-box: ~ (zsh) — 840x460"
    bbox = font_title.getbbox(title)
    w = bbox[2] - bbox[0]
    draw.text(((WIDTH - w) // 2, 11), title, font=font_title, fill=MUTED_COLOR)


def render_content(lines_data, cursor_on=False):
    """
    lines_data: list of lines, where each line is a list of segments: [(text, font, color), ...]
    """
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw)
    
    start_y = 52
    line_height = 23
    
    for row_idx, line in enumerate(lines_data):
        curr_x = 24
        curr_y = start_y + (row_idx * line_height)
        if curr_y > HEIGHT - 30:
            break
        for seg in line:
            text, f, color = seg
            draw.text((curr_x, curr_y), text, font=f, fill=color)
            bbox = f.getbbox(text)
            seg_w = bbox[2] - bbox[0]
            curr_x += seg_w
            
    if cursor_on:
        # Draw block cursor at the end of the last line
        last_row = len(lines_data) - 1
        if last_row >= 0:
            last_line = lines_data[last_row]
            end_x = 24
            for seg in last_line:
                text, f, _ = seg
                bbox = f.getbbox(text)
                end_x += (bbox[2] - bbox[0])
            curr_y = start_y + (last_row * line_height)
            draw.rectangle([end_x + 2, curr_y + 2, end_x + 10, curr_y + 18], fill=ACCENT_GREEN)
            
    return img


def build_animation():
    print("Building terminal frames...")
    
    frames = []
    durations = [] # in milliseconds
    
    # Terminal script scenario:
    # 1. Prompt appears: shiva@dev-box:~$ 
    # 2. Types: whoami
    # 3. Output: Shiva Ramchandrapuram - AI Engineer in progress & Full-Stack Developer
    # 4. Prompt appears
    # 5. Types: cat focus_areas.json
    # 6. Output: Generative AI & LLM Apps, Intelligent Agents, Scalable Web Platforms
    # 7. Prompt appears
    # 8. Types: ls -l ./featured-projects
    # 9. Output: CineStream, MediLens AI, V1 Voice Assistant, Portfolio
    # 10. Prompt appears: types status
    # 11. Output: Active & Ready to collaborate.
    
    prompt_prefix = [
        ("shiva@dev-box", font_bold, ACCENT_BLUE),
        (":", font_regular, MUTED_COLOR),
        ("~", font_regular, ACCENT_PURPLE),
        ("$ ", font_bold, ACCENT_GREEN)
    ]
    
    # Frame 0: Initial prompt empty with cursor
    base_lines = [prompt_prefix.copy()]
    frames.append(render_content(base_lines, cursor_on=True))
    durations.append(400)
    frames.append(render_content(base_lines, cursor_on=False))
    durations.append(250)
    
    # Type command 1: "whoami"
    cmd1 = "whoami"
    for i in range(1, len(cmd1) + 1):
        line = prompt_prefix.copy() + [(cmd1[:i], font_bold, TEXT_COLOR)]
        frames.append(render_content([line], cursor_on=True))
        durations.append(80)
        
    # Pause after typing
    line = prompt_prefix.copy() + [(cmd1, font_bold, TEXT_COLOR)]
    frames.append(render_content([line], cursor_on=False))
    durations.append(300)
    
    # Output of whoami
    lines_after_cmd1 = [
        prompt_prefix.copy() + [(cmd1, font_bold, TEXT_COLOR)],
        [(" > ", font_bold, ACCENT_GREEN), ("Shiva Ramchandrapuram", font_bold, ACCENT_BLUE), (" - AI Engineer & Full-Stack Developer", font_regular, TEXT_COLOR)],
        [("   ", font_regular, TEXT_COLOR), ("Role: ", font_regular, MUTED_COLOR), ("Building GenAI Apps | LLM Agents | Production Web Systems", font_regular, TEXT_COLOR)],
    ]
    frames.append(render_content(lines_after_cmd1, cursor_on=False))
    durations.append(900)
    
    # Command 2: cat tech_stack.cfg
    cmd2 = "cat tech_stack.cfg"
    # Show prompt 2
    for i in range(1, len(cmd2) + 1):
        curr_lines = lines_after_cmd1 + [
            prompt_prefix.copy() + [(cmd2[:i], font_bold, TEXT_COLOR)]
        ]
        frames.append(render_content(curr_lines, cursor_on=True))
        durations.append(50)
        
    curr_lines = lines_after_cmd1 + [prompt_prefix.copy() + [(cmd2, font_bold, TEXT_COLOR)]]
    frames.append(render_content(curr_lines, cursor_on=False))
    durations.append(250)
    
    # Output of cmd2
    lines_after_cmd2 = curr_lines + [
        [("   [Core Stack]   ", font_bold, ACCENT_BLUE), ("Python * JavaScript * TypeScript * React * Node.js", font_regular, TEXT_COLOR)],
        [("   [AI & Agents]  ", font_bold, ACCENT_PURPLE), ("Gemini LLMs * LangChain * Prompt Eng * Automation", font_regular, TEXT_COLOR)],
        [("   [Ecosystem]    ", font_bold, ACCENT_YELLOW), ("Git * GitHub Actions * Tailwind CSS * Supabase * REST", font_regular, TEXT_COLOR)],
    ]
    frames.append(render_content(lines_after_cmd2, cursor_on=False))
    durations.append(1000)
    
    # Command 3: ls -1 ./featured-projects
    cmd3 = "ls -1 ./featured-projects"
    for i in range(1, len(cmd3) + 1):
        curr_lines = lines_after_cmd2 + [
            prompt_prefix.copy() + [(cmd3[:i], font_bold, TEXT_COLOR)]
        ]
        frames.append(render_content(curr_lines, cursor_on=True))
        durations.append(45)
        
    curr_lines = lines_after_cmd2 + [prompt_prefix.copy() + [(cmd3, font_bold, TEXT_COLOR)]]
    frames.append(render_content(curr_lines, cursor_on=False))
    durations.append(250)
    
    # Output of cmd3
    lines_after_cmd3 = curr_lines + [
        [("   + ", font_bold, ACCENT_GREEN), ("cinestream/          ", font_bold, ACCENT_BLUE), ("Movie Discovery Platform (React+Vite) ", font_regular, MUTED_COLOR), ("[LIVE]", font_bold, ACCENT_GREEN)],
        [("   + ", font_bold, ACCENT_GREEN), ("medilens-ai/         ", font_bold, ACCENT_PURPLE), ("AI Prescription & Report Assistant  ", font_regular, MUTED_COLOR), ("[LIVE]", font_bold, ACCENT_GREEN)],
        [("   + ", font_bold, ACCENT_YELLOW), ("v1-voice-assistant/  ", font_bold, ACCENT_YELLOW), ("Intelligent Conversational Voice AI ", font_regular, MUTED_COLOR), ("[DEV]", font_bold, ACCENT_YELLOW)],
        [("   + ", font_bold, ACCENT_GREEN), ("personal-portfolio/  ", font_bold, ACCENT_ORANGE), ("Modern Responsive Portfolio Platform", font_regular, MUTED_COLOR), ("[LIVE]", font_bold, ACCENT_GREEN)],
    ]
    frames.append(render_content(lines_after_cmd3, cursor_on=False))
    durations.append(1200)
    
    # Command 4: echo $CURRENT_STATUS
    cmd4 = "echo $CURRENT_STATUS"
    for i in range(1, len(cmd4) + 1):
        curr_lines = lines_after_cmd3 + [
            prompt_prefix.copy() + [(cmd4[:i], font_bold, TEXT_COLOR)]
        ]
        frames.append(render_content(curr_lines, cursor_on=True))
        durations.append(50)
        
    curr_lines = lines_after_cmd3 + [prompt_prefix.copy() + [(cmd4, font_bold, TEXT_COLOR)]]
    frames.append(render_content(curr_lines, cursor_on=False))
    durations.append(250)
    
    # Final output
    final_lines = curr_lines + [
        [(" > ", font_bold, ACCENT_GREEN), ('"Active: Engineering next-gen AI agents & full-stack apps."', font_bold, ACCENT_GREEN)],
        prompt_prefix.copy()
    ]
    
    # Add lingering final frames with blinking cursor
    for _ in range(3):
        frames.append(render_content(final_lines, cursor_on=True))
        durations.append(500)
        frames.append(render_content(final_lines, cursor_on=False))
        durations.append(500)
        
    print(f"Generated {len(frames)} frames. Quantizing and saving animated GIF...")
    
    os.makedirs("assets", exist_ok=True)
    out_path = "assets/terminal-animation.gif"
    
    # Quantize frames to a single optimized 256-color palette to minimize file size
    quantized_frames = []
    # Create master palette from final rich frame
    master_palette = frames[-1].convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
    
    for f in frames:
        q_frame = f.quantize(palette=master_palette, dither=0)
        quantized_frames.append(q_frame)
        
    quantized_frames[0].save(
        out_path,
        save_all=True,
        append_images=quantized_frames[1:],
        duration=durations,
        loop=0,
        optimize=True
    )
    
    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"SUCCESS: Saved animated GIF to {out_path} ({file_size_kb:.1f} KB)")


if __name__ == "__main__":
    build_animation()
