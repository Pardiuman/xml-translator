# Bannerlord XML Translation Tool
A Python translation tool uses Google Translate Python API to translate XML of 1-D node list.

## How to use
#### Python googletrans Installation
First we need to install google translate library for python with:
    pip install googletrans 
For me, the above version does not work and will generate strange errors, so I did:
    pip install googletrans==3.1.0a0
This version choosing reference is found in here: <https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group>

#### Set YOUR_XML_FILE_TO_TRANSLATE to be the XML you want to translate
In this case with my test_file.xml, you can set:
    YOUR_XML_FILE_TO_TRANSLATE = "test_file.xml"

#### Fill in the Tag name(s) and corresponding attribute(s) containing the source text(s)
In test_file.xml, we want to translate:
Item.name from Chinese to English
CraftedItem.name from Chinese to English
So you need to do:
TRANSLATING_TAG_NAME_LIST = ['Item', 'CraftedItem']TRANSLATING_TAG_ATTRIBUTE_LIST = ['name', 'name']

Notice: 
If you just want to translate Item.name, then you can do:
TRANSLATING_TAG_NAME_LIST = ['Item']
TRANSLATING_TAG_ATTRIBUTE_LIST = ['name']
Or, if you are translating different tag with different attribute, you can do:
TRANSLATING_TAG_NAME_LIST = ['DiffenntTag1', 'DiffenntTag2', 'DiffenntTag3' .....]
TRANSLATING_TAG_ATTRIBUTE_LIST = ['DiffenntAttribute1', 'DiffenntAttribute2', 'DiffenntAttribute3' .....]
And obviously len(TRANSLATING_TAG_NAME_LIST) must equal to len(TRANSLATING_TAG_ATTRIBUTE_LIST)

#### Fill in the source language of the text and the destination language
In test_file.xml, I want to translate the text from Chinese to English, so you can do:
OPTIONAL_SOURCE_LANGUAGE = "zh-CN"
MANDATORY_DEST_LANGUAGE = "en"

Find language codes in any one of the following sites
https://developers.google.com/admin-sdk/directory/v1/languages
https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages

#### Run the code and get the translated XML file
Run the code by doing:
python translation_module
Then the generated/translated XML file will be under the Translation_Output Folder
