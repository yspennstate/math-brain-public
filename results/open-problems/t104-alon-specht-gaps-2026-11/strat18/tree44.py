"""Exact positive-coefficient certificates for both four-tree types."""
import json,time
from pathlib import Path
from algebra44 import variables,tree,numerator
from inherited17.memory_guard import install

def main():
    install(850_000_000);rr,*_=variables();records=[]
    for lower in (False,True):
        for left,right in (('star','star'),('star','path'),('path','path')):
            t=time.monotonic();num,den=numerator(rr,tree(rr,left,0),tree(rr,right,3),lower)
            bad=[(e,c)for e,c in num.items()if c<0]
            rec=dict(left=left,right=right,lower_endpoint=lower,terms=len(num),negative=len(bad))
            print(rec,'seconds',time.monotonic()-t,flush=True)
            if bad:print('first negative',bad[:3],flush=True)
            records.append(rec)
            assert not bad
            assert any(c>0 and e[-1]==0 for e,c in num.items())
            assert any(c>0 and e[-1]==2 for e,c in num.items())
            rec['minimum_nonzero_coefficient']=str(min(num.values()))
            rec['strict_witnesses']=[{'monomial':list(e),'coefficient':str(c)}for hp in (0,2)for e,c in [next((e,c)for e,c in sorted(num.items())if e[-1]==hp and c>0)]]
    Path('tree44_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (tree44.py): tree/tree signs at every k>=6 and infinity; lower endpoint k>=8.')

if __name__=='__main__':main()
