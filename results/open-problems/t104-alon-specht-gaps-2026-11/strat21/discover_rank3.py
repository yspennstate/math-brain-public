"""NUMERICAL sparse SOS discovery. Its output requires exact replay."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,time,itertools
from pathlib import Path
import numpy as np
from scipy import sparse
import clarabel
from sympy.polys.domains import QQ
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'inherited20/inherited19/inherited18/inherited17/inherited16'))
from rank_three_target import construct
sys.path.insert(0,str(BASE/'inherited20/inherited19/inherited18/inherited17'))
from memory_guard import install,peak_bytes

def target(margin=QQ(1,5),gamma=4):
    rr,V,R,mats,controls,gs,bounds=construct();T=5*rr.gens[0]
    M=[[controls[2][i][j]+(2*gamma-2)*T*(R[i][j]-R[i][4]-R[4][j]+R[4][4])-2*margin*T*T*(1+int(i==j))for j in range(4)]for i in range(4)]
    return rr,M,gs

def problem():
    old=json.loads((BASE/'inherited20/inherited19/inherited18/inherited17/inherited16/rational_sos_2.json').read_text())
    rr,M,gs=target();blocks=[dict(key=b['key'],mons=b['mons'],n=(1 if b['key'].startswith('box') else b['n']),dim=(len(b['mons']) if b['key'].startswith('box') else b['dim'])) for b in old['blocks'] if not b['key'].startswith('free') or b['key']=='free0']
    rowkeys=set((i,j,e)for i in range(4)for j in range(i,4)for e in M[i][j]);maps=[];offset=0
    for b in blocks:
        g=rr.one if b['key'].startswith('free')else gs[b['key']];mp=[]
        for v in range(b['dim']):
            for u in range(v+1):
                mon=tuple(x+y for x,y in zip(b['mons'][u//b['n']],b['mons'][v//b['n']]))
                i,j=sorted((u%b['n'],v%b['n']));factor=2 if i==j and u!=v else 1
                coords=[(i,j)]if b['n']==4 else [(i,i)for i in range(4)]
                entries=[]
                for a,c in coords:
                    for e,co in g.items():
                        key=(a,c,tuple(x+y for x,y in zip(mon,e)));rowkeys.add(key);entries.append((key,co*factor))
                mp.append(entries)
        maps.append(mp)
    rowkeys=sorted(rowkeys);ids={v:i for i,v in enumerate(rowkeys)};bvec=np.array([float(M[i][j].get(e,0))for i,j,e in rowkeys]);rows=[];cols=[];vals=[];trace=np.zeros(len(rowkeys));col=0
    for b,mp in zip(blocks,maps):
        v=0
        for j in range(b['dim']):
            for i in range(j+1):
                for key,c in mp[v]:
                    rows.append(ids[key]);cols.append(col);vals.append(float(c)/(1 if i==j else np.sqrt(2)))
                    if i==j:trace[ids[key]]+=float(c)
                col+=1;v+=1
    A=sparse.csc_matrix((vals,(rows,cols)),shape=(len(rowkeys),col))
    # Dual of max delta with all Gram blocks >=delta I.
    std=sparse.vstack([sparse.csc_matrix(trace.reshape(1,-1)),-A.T],format='csc');rhs=np.zeros(1+col);rhs[0]=1
    settings=clarabel.DefaultSettings();settings.verbose=True;settings.max_threads=1;settings.max_iter=150;settings.tol_gap_abs=1e-8;settings.tol_feas=1e-8;settings.tol_gap_rel=1e-8
    settings.chordal_decomposition_enable=False
    print('NUMERICAL',len(rowkeys),'equalities',col,'cone entries','peak',peak_bytes(),flush=True)
    solver=clarabel.DefaultSolver(sparse.csc_matrix((len(rowkeys),len(rowkeys))),bvec,std,rhs,[clarabel.ZeroConeT(1)]+[clarabel.PSDTriangleConeT(b['dim'])for b in blocks],settings)
    sol=solver.solve();print('NUMERICAL status',sol.status,'peak',peak_bytes(),flush=True)
    if str(sol.status) not in ('Solved','AlmostSolved'):return
    delta=-sol.z[0];print('NUMERICAL Gram margin',delta,flush=True)
    zs=np.array(sol.z[1:]);G=[];pos=0
    for block in blocks:
        dim=block['dim'];g=np.zeros((dim,dim))
        for j in range(dim):
            for i in range(j+1):
                g[i,j]=g[j,i]=zs[pos]/(1 if i==j else np.sqrt(2));pos+=1
        g+=delta*np.eye(dim);G.append(g)
    np.savez(BASE/'rank3_discovery.npz',*[g for g in G])
    (BASE/'rank3_discovery_meta.json').write_text(json.dumps(dict(status=str(sol.status),delta=delta,margin='1/5',gamma=4,peak_bytes_NUMERICAL=peak_bytes(),blocks=blocks),indent=2)+'\n')
if __name__=='__main__':install(850_000_000);problem()
