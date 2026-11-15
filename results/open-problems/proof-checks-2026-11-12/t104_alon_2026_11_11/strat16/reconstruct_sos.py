"""Turn numerical candidates into exact identities and integer PSD proofs.

All acceptance decisions are delegated to verify_sos.py. Cholesky factors
are merely numerical proposals for an exact diagonally dominant residual.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse
import itertools
import json
from pathlib import Path
import numpy as np
from rank_three_target import construct
from verify_sos import reconstruct, check


def main():
    p=argparse.ArgumentParser();p.add_argument('control',type=int);args=p.parse_args()
    source=json.loads(Path('sos_candidate_'+str(args.control)+'.json').read_text())
    assert source['status']in('Solved','AlmostSolved') and not source['scalar']
    D=4*10**10;Df=10**12
    groups=[]
    for meta in source['metadata']:
        n=meta['dim'];G=[[0]*n for _ in range(n)]
        for i,j,c in meta['entries']:
            G[i][j]=G[j][i]=4*round(source['x'][c]*(D//4))
        groups.append(dict(key=meta['key'],mons=meta['mons'],n=meta['n'],dim=n,G=G))
    rr,V,R,mats,controls,gs,bounds=construct()
    actual=reconstruct(groups,D)
    residual=[[controls[args.control][i][j]-actual[i][j]-(rr(1)/100 if i==j else 0)for j in range(4)]for i in range(4)]
    positions={}
    for idx,block in enumerate(groups):
        if not block['key'].startswith('free'):continue
        mons=block['mons'];n=block['n']
        for a in range(block['dim']):
            for b in range(a,block['dim']):
                i=a%n;j=b%n
                m=tuple(x+y for x,y in zip(mons[a//n],mons[b//n]))
                positions.setdefault((min(i,j),max(i,j),m),(idx,a,b,2 if i==j and a!=b else 1))
    for i in range(4):
        for j in range(i,4):
            for m,c in residual[i][j].items():
                idx,a,b,fac=positions[i,j,m];free=groups[idx]
                correction=c*D/fac
                assert correction.denominator==1,(i,j,m,c,fac,correction)
                free['G'][a][b]+=int(correction)
                if a!=b:free['G'][b][a]+=int(correction)
    for block in groups:
        G=np.array(block['G'],dtype=float)/D
        L=np.linalg.cholesky(G-1e-5*np.eye(block['dim']))
        block['chol']=[[int(round(a*Df))for a in row]for row in L]
        block['G']=[[block['G'][i][j]for j in range(i+1)]for i in range(block['dim'])]
        block['chol']=[[block['chol'][i][j]for j in range(i+1)]for i in range(block['dim'])]
    cert=dict(schema=1,control=args.control,gram_denominator=D,factor_denominator=Df,
              margin='1/100',blocks=groups,
              discovery_seconds_NUMERICAL=source['seconds_NUMERICAL'],
              discovery_peak_bytes_NUMERICAL=source.get('peak_bytes_NUMERICAL'))
    check(cert)
    dest=Path('rational_sos_'+str(args.control)+'.json');dest.write_text(json.dumps(cert,separators=(',',':'))+'\n')
    print('PROVED (verify_sos.py): exact reconstruction accepted',dest,flush=True)

if __name__=='__main__':main()
