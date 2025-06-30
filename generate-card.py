from PIL import Image, ImageDraw, ImageFont
import os

def create_card(value, suit, value_font_path, suit_font_path, watermark_path, output_path):
    # Create blank white card image
    card_size = (300, 450)
    card = Image.new("RGB", card_size, color="white")
    draw = ImageDraw.Draw(card)

    # Load fonts
    value_font = ImageFont.truetype(value_font_path, size=72)
    suit_font = ImageFont.truetype(suit_font_path, size=72)

    # Determine color based on suit
    if suit in ["♥", "♦"]:
        color = "red"
    else:
        color = "black"

    # Calculate bounding boxes and sizes
    margin = 20
    value_bbox = value_font.getbbox(value)
    value_width = value_bbox[2] - value_bbox[0]
    value_height = value_bbox[3] - value_bbox[1]
    value_y_offset = value_bbox[1]
    suit_bbox = suit_font.getbbox(suit)
    suit_width = suit_bbox[2] - suit_bbox[0]
    suit_height = suit_bbox[3] - suit_bbox[1]
    suit_y_offset = suit_bbox[1]

    # Top-left: align baseline, avoid cut-off
    top_value_x = margin
    top_value_y = margin - value_y_offset  # shift down if bbox[1] is negative
    top_suit_x = top_value_x + value_width + 5
    top_suit_y = margin - suit_y_offset
    draw.text((top_value_x, top_value_y), value, fill=color, font=value_font)
    draw.text((top_suit_x, top_suit_y), suit, fill=color, font=suit_font)

    # Bottom-right: align baseline, avoid cut-off
    bottom_value_x = card_size[0] - value_width - suit_width - margin - 5
    bottom_value_y = card_size[1] - value_height - margin - value_y_offset
    bottom_suit_x = bottom_value_x + value_width + 5
    bottom_suit_y = card_size[1] - suit_height - margin - suit_y_offset
    draw.text((bottom_value_x, bottom_value_y), value, fill=color, font=value_font)
    draw.text((bottom_suit_x, bottom_suit_y), suit, fill=color, font=suit_font)

    # Add watermark
    if watermark_path:
        watermark = Image.open(watermark_path).convert("RGBA")
        watermark = watermark.resize((100, 100))
        watermark.putalpha(int(255 * 0.6))  # 60% transparency
        # Center the watermark
        wm_x = (card_size[0] - watermark.width) // 2
        wm_y = (card_size[1] - watermark.height) // 2
        card.paste(watermark, (wm_x, wm_y), watermark)

    # Save the result
    card.save(output_path)

def generate_all_cards():
    # Define suits and values in order
    suits = ["♠", "♥", "♦", "♣"]  # Spades, Hearts, Diamonds, Clubs
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # Generate all 52 cards
    card_number = 1
    for suit in suits:
        for value in values:
            # Create ordinal filename (1.png, 2.png, etc.)
            output_path = f"output/{card_number}.png"
            
            # Generate the card
            create_card(
                value=value,
                suit=suit,
                value_font_path="fonts/CalSans-Regular.ttf",
                suit_font_path="fonts/DejaVuSans.ttf",
                watermark_path="watermarks/kraken.png",
                output_path=output_path
            )
            
            print(f"Generated card {card_number}: {value}{suit} -> {output_path}")
            card_number += 1
    
    print(f"\nGenerated all {card_number - 1} cards in output/ directory")

if __name__ == "__main__":
    generate_all_cards()
    print("done")