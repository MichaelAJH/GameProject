import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem        

def log_in(name, password):
    tree = ET.parse('player_data.xml')
    root = tree.getroot()
    for player in root.iter('player'):
        if player.attrib['name'] == name:
            for ps in player.iter('password'):
                if ps.attrib['value'] == password:
                    print('Log-in successful!')
                    return True
            print('Incorrect password')
            return False
    ans = input('Nonexistent player id. Sign in? (Y/N)' )
    if ans == 'Y' or ans == 'y':
        sign_in(name, password)
    else:
        pass

def sign_in(name, password):
    tree = ET.parse('player_data.xml')
    root = tree.getroot()
    for player in root.iter('player'):
        if player.attrib['name'] == name:
            print('Existing player id. Try with a different name.')
            return False
    
    ET.SubElement(root, 'player', attrib={'name':name})
    for player in root.iter('player'):
        if player.attrib['name'] == name:
            ET.SubElement(player, 'password', attrib={'value':password})
            print('Sign-in successful')
            indent(root)
            tree.write('player_data.xml')
            return None

def remove(name, password):
    tree = ET.parse('player_data.xml')
    root = tree.getroot()
    for player in root.iter('player'):
        if player.attrib['name'] == name:
            for ps in player.iter('password'):
                if ps.attrib['value'] == password:
                    print(f'User {name} removed from log.')
                    return True
            print('Incorrect password')
            return False
