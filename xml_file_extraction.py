import numpy as np
import xml.etree.cElementTree as ET
import pandas as pd
import csv

filename = 'TSeries-08282022-1146-002.xml'
tree = ET.ElementTree(file = filename)
treecopy = tree
root = tree.getroot()
#print(root.tag)
#print(root[2].attrib)
timestamp = root[2]
#for x in root[2]:
    #print(x.tag,x.attrib)
relativeTime = [] 
absoluteTime = []
for x in root[2].findall('Frame'):
    #print(x.attrib.get('absoluteTime'))
    #print(x.attrib.get('relativeTime'))
    relativeTime.append(x.attrib.get('relativeTime'))
    absoluteTime.append(x.attrib.get('absoluteTime'))

relativeTime = np.array(relativeTime)
absoluteTime = np.array(absoluteTime)
# exporting a list variable into the csv file
Timestamp = np.transpose(np.vstack((relativeTime,absoluteTime)))

#csv gets created in the current working directory 
#export csv file as a dataframe
pd.DataFrame(Timestamp).to_csv('Timestamp.csv')      