from PIL import Image, ImageDraw

src = r"C:\Users\huiran\Documents\xwechat_files\wxid_nygnl9jqw39o22_2c7c\temp\RWTemp\2026-10\9e20f478899dc29eb19741386f9343c8\1898ddec6c5e17a917605b37586b0a58.jpg"
dst = r"C:\Users\huiran\Doubao\chats\2026-10-15\new-chat-1\personal-page\assets\avatar.png"

img = Image.open(src).convert("RGB")
w, h = img.size
print(f"Original size: {w}x{h}")

# Watermark "@Zr6Ov" is in bottom-right corner
# Cover it by sampling the background color nearby and painting over
draw = ImageDraw.Draw(img)

# Sample background color from a spot near the watermark (but not on it)
# The background is light blue polka dot
# Take a patch from the left side of the watermark area
patch = img.crop((w - 180, h - 60, w - 80, h - 20))
patch_w, patch_h = patch.size
# Tile/cover the bottom-right watermark area
for x in range(w - 120, w, patch_w):
    for y in range(h - 50, h, patch_h):
        img.paste(patch, (x, y))

# Also directly paint over the exact watermark area with sampled color
# Sample color from near the bottom right (clean area)
bg_color = img.getpixel((w - 150, h - 30))
print(f"Sampled bg color: {bg_color}")
draw.rectangle([w - 130, h - 45, w, h], fill=bg_color)

# Resize to reasonable avatar size (400x400)
img = img.resize((400, 400), Image.LANCZOS)
img.save(dst, "PNG")
print(f"Saved to: {dst}")
