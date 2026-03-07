#!/usr/bin/python3
import xml.etree.ElementTree as ET
def serialize_to_xml(dictionary, filename):
    elem=ET.Element("data")
    for key,value in dictionary.items():

        if isinstance(value,dict):
            child=serialize_to_xml(key,value)
            elem.append(child)
        else:
            child=ET.SubElement(elem,key)
            child.text=str(value)
    tree=ET.ElementTree(elem)
    tree.write(filename)

def deserialize_from_xml(filename):
    root=ET.parse(filename)
    root=root.getroot()
    return {child.tag:child.text for child in root}
