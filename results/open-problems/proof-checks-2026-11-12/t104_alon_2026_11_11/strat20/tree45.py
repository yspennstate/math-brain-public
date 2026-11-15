"""Exact positive-coefficient signs and padding for all six tree pairs."""
import json
from pathlib import Path
from algebra45 import *
from inherited19.inherited18.inherited17.memory_guard import install

def main():
    install(850_000_000);rr,*_=variables();records=[]
    for left in FOUR:
        for right in FIVE:
            p,den=numerator(rr,left,right)
            bad=[(e,c)for e,c in p.items()if c<0]
            rec=dict(left=left,right=right,terms=len(p),negative=len(bad),minimum_coefficient=str(min(p.values())))
            if bad:print('first failure',bad[:1],flush=True)
            assert not bad
            rec['strict_witnesses']={str(j):next(e for e,c in sorted(p.items())if e[-1]==j and c>0)for j in (0,2)}
            A0,A1,A2=padding_coefficients(rr,p)
            for q in (14*A2-A1,A1-QQ(2,7)*A0):assert q and all(c>=0 for c in q.values())
            rec['padding_derivative_terms']=[len(14*A2-A1),len(A1-QQ(2,7)*A0)]
            print(rec,flush=True);records.append(rec)
    Path('tree45_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (tree45.py): all six positive-flux four/five-tree pairs strict at every k>=7 and infinity, k=7 hardest.')
if __name__=='__main__':main()
