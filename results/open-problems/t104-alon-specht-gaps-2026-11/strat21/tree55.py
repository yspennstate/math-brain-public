"""Positive rational coefficient certificates for six unordered tree pairs."""
import json,itertools
from pathlib import Path
from algebra55 import *
from inherited20.inherited19.inherited18.inherited17.memory_guard import install

def coefficients(rr,p):return [rr.from_dict({e[:-1]+(0,):c for e,c in p.items()if e[-1]==j})for j in (0,1,2)]
def main():
    install(850_000_000);rr,*_=variables();records=[]
    for left,right in itertools.combinations_with_replacement(FIVE,2):
        p,den=numerator(rr,left,right)
        bad=[(e,c)for e,c in p.items()if c<0]
        rec=dict(left=left,right=right,terms=len(p),negative=len(bad),minimum_coefficient=str(min(p.values())))
        print(rec,'first',bad[:1],flush=True);assert not bad
        rec['strict_witnesses']={str(j):next(e for e,c in sorted(p.items())if e[-1]==j and c>0)for j in (0,2)}
        A0,A1,A2=coefficients(rr,p)
        qs=(16*A2-A1,A1-A0/4)
        rec['padding_derivative_terms']=[len(q)for q in qs]
        rec['padding_negative_coefficients']=[sum(c<0 for c in q.values())for q in qs]
        print('padding',rec['padding_negative_coefficients'],flush=True)
        assert all(q and all(c>=0 for c in q.values())for q in qs)
        records.append(rec)
    Path('tree55_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (tree55.py): six unordered tree pairs strict for all k>=8 and infinity, k=8 hardest.')
if __name__=='__main__':main()
