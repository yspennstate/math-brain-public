from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import xml.etree.ElementTree as ET

u,v,c = F(1,3),F(2,3),F(1,2)
assert (u/(1-u)+v/(1-v))/2 == F(5,4)
cov = ((1-u)**2+(1-v)**2)/2 - ((2-u-v)/2)**2
assert cov == (u-v)**2/4 == F(1,36)
assert 16*F(1,4)**2 == 1
assert c*32*F(1,4) == 4
assert F(10,2)>4
assert 1-c/F(3,4)==F(1,3)<F(1,2)
for a,b in product([F(51,100),F(3,5),F(7,10),F(74,100)], repeat=2):
    h0,h2=1-c/a,1-c/b
    covariance=(1+h0*h2)/2-(1+h0)*(1+h2)/4
    assert covariance == c*c/(4*a*b)>0

def compositions(total, length):
    if length==1:
        yield (total,)
    else:
        for k in range(total+1):
            for tail in compositions(total-k,length-1):
                yield (k,)+tail

checked=0
for m in range(2,7):
    for total in range(9):
        for eta in compositions(total,m):
            incoming=outgoing=0
            for j in range(m):
                nxt=(j+1)%m
                if eta[j]>0: outgoing+=1
                if eta[nxt]>0:
                    predecessor=list(eta)
                    predecessor[j]+=1
                    predecessor[nxt]-=1
                    assert sum(predecessor)==sum(eta)
                    assert predecessor[j]>0
                    incoming+=1
            assert incoming==outgoing
            checked+=1
result={'cycle_states':checked,'density_1':str(F(5,4)),'covariance_1':str(cov),'critical_density_2':4,'initial_density_2':5,'empty_probability_upper_at_critical':'1/3 (strict)','assertions':'passed'}
Path('independent_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
ns={'a':'http://www.w3.org/2005/Atom'}
tree=ET.parse('arxiv_search.xml')
for entry in tree.findall('a:entry',ns):
    print(entry.findtext('a:id',namespaces=ns), ' '.join(entry.findtext('a:title',namespaces=ns).split()))
