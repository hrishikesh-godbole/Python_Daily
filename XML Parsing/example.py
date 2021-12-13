import xml.etree.ElementTree as ET
myTree = ET.parse('foodmenu.xml')
myRoot = myTree.getroot()
# print(myRoot[0].attrib)
#
# for x in myRoot[0]:
#     print(x.tag,x.attrib)
#
# for x in myRoot[0]:
#     print(x.text)


# we found the elements from xml file and read them in python file
# for x in myRoot.findall('food'):
#     name = x.find('name').text
#     price = x.find('price').text
#     description = x.find('description').text
#     calories = x.find('calories').text
#     print(name," ",price," ",description," ",calories)


# modifying description or any other elements from xml file
# for x in myRoot.iter('description'):
#     a = str(x.text) + ' Description has been added'
#     x.text = str(a)
#     x.set('updated','yes')
# myTree.write('new.xml')


# how to modify a tag
# ET.SubElement(myRoot[0],'speciality')
# for x in myRoot.iter('speciality'):
#     b = 'Multicontinental Cusine'
#     x.text = str(b)
# myTree.write('new2.xml')

#how to delete a tag
# myRoot[0].remove(myRoot[0][0])
# myTree.write('new3.xml')

#how to remove an element from its position
myRoot[0].clear()
myTree.write('new4.xml')