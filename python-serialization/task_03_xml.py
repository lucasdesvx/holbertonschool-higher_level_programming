import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="unicode")


def deserialize_from_xml(filename):
    root = ET.parse(filename).getroot()
    return {element.tag: element.text or "" for element in root}
