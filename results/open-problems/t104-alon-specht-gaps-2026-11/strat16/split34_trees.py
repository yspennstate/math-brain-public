"""Exact positive coefficient checks: four-vertex trees plus triangle corners."""
import json
import itertools
from pathlib import Path
from split34_algebra import variables,tree_data,triangle,numerator


def main():
    rr,x,y,z,a,b,h=variables();records=[]
    for name,edges in [('star',[(0,1),(0,2),(0,3)]),('path',[(0,1),(1,2),(2,3)])]:
        block=tree_data(rr,edges,(x,y,z),4)
        for corner in ('balanced','path'):
            num,den=numerator(rr,block,triangle(rr,corner))
            bad=[m for m,c in num.items()if c<0]
            print(name,corner,'terms',len(num),'negative',len(bad),flush=True)
            assert not bad
            assert any(c>0 and m[-1]==0 for m,c in num.items())
            assert any(c>0 and m[-1]==2 for m,c in num.items())
            records.append(dict(tree=name,triangle=corner,terms=len(num),negative=0))
    Path('split34_trees_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (split34_trees.py): T*>0 on both four-tree types and both triangle corners, k>=5 and infinity.')

if __name__=='__main__':main()
