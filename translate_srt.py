import re
from googletrans import Translator

#Load the .srt file
with open("captions.srt", "r", encoding="utf-8") as f:
    content = f.read()

#Split into subtitle blocks
blocks = re.split(r"\n\s*\n", content.strip())

translator = Translator()
translated_blocks = []

#Translate each block
for block in blocks:
    lines = block.strip().split("\n")
    if len(lines) >= 3:
        number = lines[0]
        timestamp = lines[1]
        text_lines = lines[2:]
        full_text = " ".join(text_lines)
        try:
            translated_text = translator.translate(full_text, src='en', dest='uk').text
        except Exception as e:
            translated_text = "[Translation Error]"
        translated_block = "\n".join([number, timestamp, translated_text])
        translated_blocks.append(translated_block)

#Save translated file
output_text = "\n\n".join(translated_blocks)
with open("captions_ukrainian.srt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("✅ Translation complete. File saved as captions_ukrainian.srt")

