#!/usr/bin/env python3
"""Run after compiling torus_tsp_ubsan as described in LOG.md."""
import json
import subprocess
from experiment import ROOT
import numpy as np
from scipy.spatial import cKDTree
from validate import exact

def main():
    rows=[]
    for n in [3,4,6,7,9,11,13,15]:
        for seed in [73001,73002]:
            xy=np.random.default_rng(seed+n).random((n,2))
            k=min(32,n-1)
            _,nn=cKDTree(xy,boxsize=1).query(xy,k=k+1,workers=1)
            payload=f'{n} {k} 20 {seed} 1\n'
            payload+='\n'.join(f'{x:.17g} {y:.17g}' for x,y in xy)+'\n'
            payload+='\n'.join(' '.join(map(str,r)) for r in nn[:,1:])+'\n'
            answers=[]
            for executable in ['torus_tsp','torus_tsp_ubsan']:
                result=subprocess.run([str(ROOT/'code'/executable)],input=payload,text=True,
                                      stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
                assert not result.stderr
                answers.append(json.loads(result.stdout))
            optimum=exact(xy)
            assert abs(answers[0]['best']-answers[1]['best'])<1e-10
            assert answers[0]['best']>=optimum-1e-10
            rows.append({'n':n,'seed':seed,'optimal':optimum,'heuristic':answers[0]['best'],
                         'gap':answers[0]['best']-optimum,'ubsan':'pass',
                         'cap_hits':answers[0]['cap_hits']})
    (ROOT/'data'/'validation_edge_cases.json').write_text(json.dumps(rows,indent=2))
    print('Edge/UBSan cases:',len(rows),'max gap',max(r['gap'] for r in rows))

if __name__=='__main__':main()
