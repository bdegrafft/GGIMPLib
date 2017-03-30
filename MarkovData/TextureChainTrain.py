__author__ = 'Brendan'
#!/usr/bin/env python


import random
import pprint

table={}
nonstep='\n'
s1=nonstep
s2=nonstep

f=open('C:\Users\Brendan\.gimp-2.8\plug-ins\Generative\MarkovData\Training.txt','r')
for chain in f:
    for step in chain.split():
        table.setdefault((s1,s2), []).append(step)
        s1,s2 =s2,step

pprint.pprint (table)
# s1 = nonstep
# s2 = nonstep
#
# for i in xrange(10):
#     newstep = random.choice(table[(s1, s2)])
#     print newstep;
#     s1, s2 = s2, newstep
