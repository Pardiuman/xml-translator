from xml.dom import minidom
from googletrans import Translator
from collections import defaultdict
import os
import sys

# Reconfigure Python text encoding and decoding system to support 97.8% of text format
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding='utf-8')

# Put your xml file's name here
YOUR_XML_FILE_TO_TRANSLATE = "resource-test.xml"
# Tag names containing texts to be translated
TRANSLATING_TAG_NAME_LIST = ['Item', 'CraftedItem']
# Attributes of previously defined tag names to be translated
TRANSLATING_TAG_ATTRIBUTE_LIST = ['name', 'name']
"""
Find language codes in any one of the following sites
https://developers.google.com/admin-sdk/directory/v1/languages
https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
"""
OPTIONAL_SOURCE_LANGUAGE = "zh-CN" # -> The language of your XML BEFORE translation
MANDATORY_DEST_LANGUAGE = "en" # -> The language of your XML AFTER translation

if (len(TRANSLATING_TAG_NAME_LIST) != len(TRANSLATING_TAG_ATTRIBUTE_LIST)):
    print("ERROR: TRANSLATING_TAG_NAME_LIST and TRANSLATING_TAG_ATTRIBUTE_LIST inputs are not of same length!")
    exit()

# Make a relative sub folder for translation output
translation_folder_name = 'Translation_Output'
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
translation_folder_dir =  script_dir + '\\' + translation_folder_name
if (not os.path.exists(translation_folder_dir)):
    os.mkdir(translation_folder_name)
    print(translation_folder_name + " folder is created!")
else:
    print(translation_folder_name + " folder is already created!")

# Create translator instance
# translator = Translator()

# Parse an xml file by name
xml_doc = minidom.parse(YOUR_XML_FILE_TO_TRANSLATE)

# Open/Create new file for translated XML
print("## Outputing translated XML ##")
print(xml_doc)

# Remove the comment node(s)
root = None
for child in xml_doc.childNodes:
    if child.nodeType == minidom.Element.COMMENT_NODE:
        xml_doc.removeChild(child)

# We assume there is only one big root node here
root = xml_doc.childNodes[0]



# for item in root.getElementsByTagName("item"):
#   # Get element name and text content (value)
#   name = item.getAttribute("name")  # Use getAttribute for element names
#   value = item.firstChild.data.strip() if item.firstChild else ""  # Handle empty values

#   # Print name and value
#   print(f"Name: {name.upper()}")  # Convert name to uppercase
#   print(f"Value: {value}")
#   print("-" * 20)





data = defaultdict(str)  # Default value for missing keys is an empty string

# Loop through all "item" elements
for item in root.getElementsByTagName("item"):
  # Get element name and text content (value)
  name = item.getAttribute("name")
  value = item.firstChild.data.strip() if item.firstChild else ""

  # Add data to the map
  data[name] = value

# Print the map contents (optional)
# for key, value in data.items():
#   print(f"Name: {key}")
#   print(f"Value: {value}")
#   print("-" * 20)



######################### to translate and put in array  #######

# translated_values = []

# # Create a translator object
# translator = Translator()

# # Loop through the map and translate values
# for value in data.values():
#   # Translate the value (replace 'en' with your target language code)
#   translation = translator.translate(value, dest='de').text
#   print(translation)
#   translated_values.append(translation)

# # Print the translated values (optional)
# for value in translated_values:
#   print(value)
######################################################################


translated_data = {}  # Create an empty dictionary

# Create a translator object
translator = Translator()

# Loop through the map and translate values
for original_name, value in data.items():
  # Translate the value (replace 'en' with your target language code)
  translation = translator.translate(value, dest='de').text

  # Add key-value pair to the dictionary
  translated_data[original_name] = translation

# Print the translated data (optional)
for key, value in translated_data.items():
  print(f"Original: {key}")
  print(f"Translated: {value}")
  print("-" * 20)









for item in root.getElementsByTagName("item"):
  # Get the element name (attribute)
  name = item.getAttribute("name")

  # Find the corresponding translated value (check if key exists)
  translated_value = translated_data.get(name)  # Use get() to avoid KeyError

  # Update text node if translated value exists
  if translated_value:
    text_node = item.firstChild  # Assuming the first child is text
    if text_node:
      text_node.data = translated_value

# Write the updated XML data to a new file
translated_file_path = "translated.xml"
with open(translated_file_path, "w", encoding="utf-8") as f:
  xml_doc.writexml(f, indent="  ", encoding="utf-8")

print(f"XML updated with translated values (written to {translated_file_path}).")

