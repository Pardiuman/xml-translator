from xml.dom import minidom
from googletrans import Translator
from collections import defaultdict
import os

# Original XML file path
original_xml_file = "Resource.xml"

# List of language codes for translation (replace with desired codes)
languages = ["de"]  # English, German, French

# Create translator object
translator = Translator()


def translate_and_update(element, text_node, language_code):
    original_text = text_node.data.strip()
    translation = translator.translate(original_text, dest=language_code).text
    text_node.data = translation


def translate_batch(text_list, language_code):
    """
    Translates a list of text strings in a single request.
    """
    translations = translator.translate(text_list, dest=language_code)
    return [translation.text for translation in translations]


# Open the original XML file for reading
xml_doc = minidom.parse(original_xml_file)

# Get the root element
root = xml_doc.documentElement

# Loop through each language code
for language_code in languages:
    # Create a copy of the original XML document for each language
    translated_doc = xml_doc.cloneNode(deep=True)

    text_to_translate = []
    for item in translated_doc.getElementsByTagName("item"):
        text_node = item.firstChild  # Assuming the first child is text
        if text_node:
            text_to_translate.append(text_node.data.strip())

    # Batch translation
    translations = translate_batch(text_to_translate, language_code)

    # Update text nodes with translations
    for i, translation in enumerate(translations):
        translated_doc.getElementsByTagName("item")[i].firstChild.data = translation

    # Generate output file name with language code suffix
    output_file_path = f"{os.path.splitext(original_xml_file)[0]}_{language_code}.xml"

    # Write the translated XML data to a separate file
    with open(output_file_path, "w", encoding="utf-8") as f:
        translated_doc.writexml(f, indent="  ", encoding="utf-8")

    print(f"XML translated and written to {output_file_path} ({language_code})")
