from lxml import etree

def xml_to_txt(xml_file, txt_file):
    # Parse the XML file
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Open the TXT file for writing
    with open(txt_file, 'w', encoding='utf-8') as f:
        # Recursively extract text content from XML
        extract_text(root, f)

def extract_text(element, file_handle, accumulated_text=''):
    # Append the text content of the element if it exists
    if element.text:
        accumulated_text += element.text.strip() + ' '

    # Recurse through child elements
    for child in element:
        accumulated_text = extract_text(child, file_handle, accumulated_text)
    
    # If the element has no children, write the accumulated text to the file
    if len(element) == 0 and accumulated_text.strip():
        file_handle.write(accumulated_text.strip() + '\n')
        accumulated_text = ''  # Reset accumulated text after writing

    return accumulated_text

# Example usage
if __name__ == "__main__":
    xml_file = 'FalV_modded_V2.xml'
    txt_file = 'output3.txt'
    xml_to_txt(xml_file, txt_file)