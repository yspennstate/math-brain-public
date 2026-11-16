"""Exact positive coefficients and inverse-padding derivatives for all six pairs."""
import json
from pathlib import Path
from algebra35 import variables,numerator,padding_coefficients,TREES
from inherited18.inherited17.memory_guard import install

def main():
    install(850_000_000);rr,*_=variables();records=[]
    for corner in ('balanced','path'):
        for name in TREES:
            rec={'triangle':corner,'five_tree':name}
            for lower in (False,True):
                p,den=numerator(rr,corner,name,lower)
                assert p and all(c>0 for c in p.values()),(corner,name,lower)
                witnesses={str(j):next((e for e,c in sorted(p.items()) if e[-1]==j and c>0),None) for j in (0,2)}
                assert all(witnesses.values())
                rec['lower' if lower else 'isolates']={'terms':len(p),'minimum_nonzero_coefficient':str(min(p.values())),'strict_witnesses':witnesses}
                if not lower:
                    A0,A1,A2=padding_coefficients(rr,p)
                    derivative=[12*A2-A1,A1-A0/3]
                    assert all(q and all(c>=0 for c in q.values()) for q in derivative)
                    rec['negative_inverse_padding_derivative_endpoint_terms']=[len(q) for q in derivative]
            records.append(rec);print(rec,flush=True)
    Path('tree35_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (tree35.py): six connected triangle/five-tree pairs are strict, k>=6 and infinity; k=6 hardest. Maximal-lower-trace endpoints strict as well.')

if __name__=='__main__':main()
