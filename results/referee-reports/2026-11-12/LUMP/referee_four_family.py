"""Simple independent four-state family suggested by the random search.

Weights 02=12=1, 03=13=t, 00=11=t^2-1, 33=t^6.
Merge 2 and 3. Both exact formulas and occupation certificates are checked.
"""
import json
from fractions import Fraction as F
from referee_core import exact_chain,lump,display

out=[]
for t in [2,4,16,64,256,4096,1000000]:
    w=[[F(0)]*4 for _ in range(4)]
    for i,j,wt in [(0,2,1),(1,2,1),(0,3,t),(1,3,t)]:
        w[i][j]=w[j][i]=F(wt)
    w[0][0]=w[1][1]=F(t*t-1)
    w[3][3]=F(t**6)
    a=exact_chain(w);b=exact_chain(lump(w,[0,1,2,2]))
    total=F(t**6+2*t*t+4*t+2)
    # Ground at state 3. Let A=H(0,3)=H(1,3), C=H(2,3).
    A=F(t*t+t+1,t);C=F((t+1)**2,t)
    mu=(2*t*(t+1)*A+2*C)/total
    original=C-mu
    induced=2*t-F(2*t*t*(t+1),total)
    assert a['tmix']==original and b['tmix']==induced
    ratio=induced/original
    assert ratio == F(2*t*(t**6+t*t+3*t+2),(t+1)*(t**6+t**5+4*t+2))
    row={'t':t,'tmix':display(original),'lumped':display(induced),'ratio':display(ratio)}
    out.append(row)
with open('referee_four_family.json','w') as f:json.dump(out,f,indent=2)
print('W02=W12=1; W03=W13=t; W00=W11=t^2-1; W33=t^6; all others zero; merge {2,3}.')
for row in out:
    print('t=%d tmix=%.15g lumped=%.15g ratio=%.15g' %
          (row['t'],row['tmix']['decimal'],row['lumped']['decimal'],row['ratio']['decimal']))
print('Best exact ratio:',out[-1]['ratio']['exact'])
