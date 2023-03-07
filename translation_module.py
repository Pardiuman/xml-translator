from xml.dom import minidom
from googletrans import Translator
import os
import sys

# Reconfigure Python text encoding and decoding system to support 97.8% of text format
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding='utf-8')

# Put your xml file's name here
YOUR_XML_FILE_TO_TRANSLATE = "test_file.xml"
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
translator = Translator()

# Parse an xml file by name
xml_doc = minidom.parse(YOUR_XML_FILE_TO_TRANSLATE)

# Open/Create new file for translated XML
print("## Outputing translated XML ##")

# Remove the comment node(s)
root = None
for child in xml_doc.childNodes:
    if child.nodeType == minidom.Element.COMMENT_NODE:
        xml_doc.removeChild(child)

# We assume there is only one big root node here
root = xml_doc.childNodes[0]

# Start Translating
for i in range(len(TRANSLATING_TAG_NAME_LIST)):
    for child in root.childNodes:
        if (   
            child.nodeType != minidom.Element.TEXT_NODE and
            child.tagName == TRANSLATING_TAG_NAME_LIST[i] and
            child.hasAttribute(TRANSLATING_TAG_ATTRIBUTE_LIST[i])
            ):
            """
            TODO: There are other way(s) to improve thhe translation quality
            - Use regex to count the symbols of non regular sentence symbols and generate PURE language lines
                a. Split the line by symbols which are not ",.?!;:"
                b. Acquire the INDEXes of the splited outputs 
                c. Use the length of the splited outputs to gain the inregular symbols and save in an array
                d. Translate the Pure language lines in MANDATORY_DEST_LANGUAGE
                e. Concatenate inregular symbols with Translated Pure Language lines
            """
            # Acquire text
            input_line = child.attributes[TRANSLATING_TAG_ATTRIBUTE_LIST[i]].value
            # Capitalize text
            input_line = input_line.title()
            # Translate text
            output_line = translator.translate(
                input_line, 
                src=OPTIONAL_SOURCE_LANGUAGE,
                dest=MANDATORY_DEST_LANGUAGE,
                ).text
            # Capitalize Translated text
            output_line = output_line.title()
            # Update translated text
            child.setAttribute(
                TRANSLATING_TAG_ATTRIBUTE_LIST[i], 
                output_line
                )
            # Check translation
            print(input_line)
            print(output_line)

with open(f"{translation_folder_dir}\\{YOUR_XML_FILE_TO_TRANSLATE}", "w", encoding='utf-8') as new_xml_file:
    xml_doc.writexml(new_xml_file, encoding='utf-8')
print("## Translated XML Generated ##")