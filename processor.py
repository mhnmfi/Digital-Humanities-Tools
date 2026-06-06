import re

def process_digital_text(input_data):
    # Removing special characters for digital literature analysis
    clean_data = re.sub(r'[^\w\s]', '', input_data)
    return clean_data.lower()

print("Digital Humanities Processor Ready.")
