import xml.etree.ElementTree as ET

def parse_xml(xml_file):
  """
  Parses an XML file and prints element names and values.

  Args:
      xml_file (str): Path to the XML file.
  """
  try:
    # Parse the XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate through all "item" elements
    for item in root.findall('item'):
      # Get element name and text content (value)
      name = item.attrib['name']
      value = item.text.strip() if item.text else ""  # Handle empty values

      # Print name and value
      print(f"Name: {name}")
      print(f"Value: {value}")
      print("-" * 20)

  except FileNotFoundError:
    print(f"Error: File '{xml_file}' not found.")

# Example usage (replace 'your_file.xml' with your actual file path)
parse_xml('Resource.xml')
