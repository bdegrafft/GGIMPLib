import xml.etree.ElementTree
import collections
import pickle

e = xml.etree.ElementTree.parse('C:\Users\Brendan\.gimp-2.8\plug-ins\Generative\FilterData\source.xml').getroot()

d={}
for command in e.findall('./command'):
    commandName='-'+command.find('name').text
    if '-fx_' in commandName: commandName='-gimp'+commandName[3:]
    if '_preview' in commandName: commandName=commandName.strip('_preview')
    commandID=int(command.get('id'))
    d[commandName]=collections.OrderedDict()
    d[commandName]['tags']=[]
    if commandID in range(1,22):
        d[commandName]['tags'].append('Arrays')
    if commandID in range(23,49):
        d[commandName]['tags'].append('Artistic')
    if commandID in range(50,58):
        d[commandName]['tags'].append('Basics')
    if commandID in range(59,76):
        d[commandName]['tags'].append('Black and White')
    if commandID in range(77,116):
        d[commandName]['tags'].append('Colors')
    if commandID in range(117,131):
        d[commandName]['tags'].append('Contors')
    if commandID in range(132,158):
        d[commandName]['tags'].append('Deformation')
    if commandID in range(159,179):
        d[commandName]['tags'].append('Degradation')
    if commandID in range(180,201):
        d[commandName]['tags'].append('Details')
    if commandID in range(202,213):
        d[commandName]['tags'].append('Film Emulation')
    if commandID in range(214,226):
        d[commandName]['tags'].append('Frames')
    if commandID in range(227,236):
        d[commandName]['tags'].append('Lights and Shadows')
    if commandID in range(237,267):
        d[commandName]['tags'].append('Patterns')
    if commandID in range(268,303):
        d[commandName]['tags'].append('Rendering')
    if commandID in range(304,332):
        d[commandName]['tags'].append('Repair')
    for params in command.findall('./parameters/'):
        paramType=params.tag
        for param in params.findall('./*'):
            if param.tag == 'name':
                paramName=param.text
                d[commandName][paramName]={'type':paramType}
                if paramType=='choice':
                    d[commandName][paramName].setdefault('options',[])
            elif param.tag!='option':
                try:
                    d[commandName][paramName][param.tag]=param.text
                except:
                    pass
            else:
                d[commandName][paramName]['options'].append(param.text)
    if d[commandName]=={}:
        del d[commandName]


def getFilters(tags,d):
    '''Returns a list of filters with the given tags'''
    possibilities=[]
    for tag in tags:
        for f in d:
            if tag in d[f]['tags']:
                if f not in possibilities:
                    possibilities.append(f)
            elif f in possibilities:
                possibilities.remove(f)
    return possibilities
with open('filtData.pickle', 'wb') as handle:
    pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)


print(getFilters(['Artistic'],d))
with open(r'C:\Users\Brendan\.gimp-2.8\plug-ins\filtData.pickle', 'rb') as handle:
    filtData = pickle.load(handle)
print(getFilters(['Artistic'],filtData))
