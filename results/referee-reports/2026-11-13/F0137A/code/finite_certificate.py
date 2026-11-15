#!/usr/bin/env python3
"""Exact finite-path annealed probabilities; a toy verifier, not a T' certificate."""
import os
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json

def enumerate_paths(alpha,L,W,N):
    d=len(alpha)//2;S=sum(alpha);moves=[]
    for j in range(2*d):
        e=[0]*d;e[j%d]=1 if j<d else -1;moves.append(e)
    counts=defaultdict(lambda:[0]*(2*d)); front=F(0);bad=F(0);alive=F(0);leaves=0
    def dfs(x,n,weight):
        nonlocal front,bad,alive,leaves
        if x[0]>=L:front+=weight;leaves+=1;return
        if x[0]<=-L or any(abs(x[k])>=W for k in range(1,d)):
            bad+=weight;leaves+=1;return
        if n==N:alive+=weight;leaves+=1;return
        c=counts[x];den=S+sum(c)
        for j,e in enumerate(moves):
            prob=(alpha[j]+c[j])/den;c[j]+=1
            dfs(tuple(x[k]+e[k] for k in range(d)),n+1,weight*prob)
            c[j]-=1
    dfs((0,)*d,0,F(1))
    assert front+bad+alive==1
    return {'L':L,'W':W,'N':N,'front':str(front),'bad':str(bad),'alive':str(alive),
            'bad_upper':str(bad+alive),'bad_upper_float':float(bad+alive),'leaves':leaves}

if __name__=='__main__':
    alpha=[F(11,20),F(1,2),F(1,2),F(1,2)]
    examples=[enumerate_paths(alpha,1,1,1)]+[enumerate_paths(alpha,2,2,N) for N in (2,4,6,8)]
    assert F(examples[0]['bad'])==F(30,41)
    assert all(F(examples[i]['bad_upper'])>=F(examples[i+1]['bad_upper']) for i in range(1,len(examples)-1))
    out={'alpha':[str(x) for x in alpha],'examples':examples,
         'warning':'toy boxes are far below c0; no polynomial criterion is claimed'}
    (Path(__file__).resolve().parents[1]/'data'/'finite_certificate_checks.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
