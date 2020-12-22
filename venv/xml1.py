import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Felix Protich</name>
  <phone type="intl">
    +254 796854357 
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
