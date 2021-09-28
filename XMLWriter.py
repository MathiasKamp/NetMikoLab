# this file contains methods and logic to write a dictionary to an xml file
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


# this method writes a dictionary into an xml file using dicttoxml library
def dict_to_xml_file(values, filename):
    output_file = None

    try:
        filename = filename + ".xml"
        output_file = open(filename, "w")

    except IOError as error:
        print(error)
        output_file.close()
    else:
        xml = dicttoxml(values)
        xml_str = parseString(xml)
        output_file.write(xml_str.toprettyxml())

    finally:
        if output_file is not None:
            output_file.close()
