import xml.etree.ElementTree
import collections
import pickle

e = xml.etree.ElementTree.parse('C:\Users\Brendan\.gimp-2.8\plug-ins\Generative\FilterData\source.xml').getroot()

d={}
for command in e.findall('./command'):
    commandName='-'+command.find('name').text
    if '-fx_' in commandName: commandName='-gimp'+commandName[3:]
    if '_preview' in commandName: commandName=commandName.strip('_preview')

    d[commandName]=collections.OrderedDict()
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

with open('filtData.pickle', 'wb') as handle:
    pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
