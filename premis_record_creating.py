from lxml import etree

# create the root element of the PREMIS record
premis = etree.Element("{http://www.loc.gov/premis/v3}premis", nsmap={'premis': 'http://www.loc.gov/premis/v3'})

# create the object element and add it to the PREMIS record
object = etree.SubElement(premis, "{http://www.loc.gov/premis/v3}object")

# create the objectIdentifier element and add it to the object element
objectIdentifier = etree.SubElement(object, "{http://www.loc.gov/premis/v3}objectIdentifier")

# create the objectIdentifierType element and add it to the objectIdentifier element
objectIdentifierType = etree.SubElement(objectIdentifier, "{http://www.loc.gov/premis/v3}objectIdentifierType")
objectIdentifierType.text = "UUID"

# create the objectIdentifierValue element and add it to the objectIdentifier element
objectIdentifierValue = etree.SubElement(objectIdentifier, "{http://www.loc.gov/premis/v3}objectIdentifierValue")
objectIdentifierValue.text = "123e4567-e89b-12d3-a456-426655440000"

# create the objectCategory element and add it to the object element
objectCategory = etree.SubElement(object, "{http://www.loc.gov/premis/v3}objectCategory")
objectCategory.text = "file"

# create the objectType element and add it to the object element
objectType = etree.SubElement(object, "{http://www.loc.gov/premis/v3}objectType")
objectType.text = "text"

# create the objectTitle element and add it to the object element
objectTitle = etree.SubElement(object, "{http://www.loc.gov/premis/v3}objectTitle")
objectTitle.text = "Example Text File"

# write the PREMIS record to a file
with open("premis.xml", "wb") as f:
    f.write(etree.tostring(premis, pretty_print=True))
