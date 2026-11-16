"""NUMERICAL SDP discovery; a successful solver status is never a proof."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse
import itertools
import json
import time
import resource
import threading
import fcntl
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import clarabel
from rank_three_target import construct


def monomials(deg,n=6):
    return sorted((m for m in itertools.product(range(deg+1),repeat=n)if sum(m)<=deg),key=lambda m:(sum(m),m))


def setup(control,full=True,structure='sparse'):
    rr,V,R,mats,controls,gs,bounds=construct();target=controls[control]
    # A modest strictly positive margin helps rational rounding.
    target=[[target[i][j]-(rr(1)/100 if i==j else 0)for j in range(4)]for i in range(4)]
    exps=monomials(4);pairs=list(itertools.combinations_with_replacement(range(4),2))
    rows={(a,b,m):k for k,(a,b,m)in enumerate((a,b,m)for a,b in pairs for m in exps)}
    bvec=np.array([float(target[a][b].get(m,0))for a,b in pairs for m in exps]);n_eq=len(bvec)
    if structure=='dense':
        blocks=[('free',monomials(2),rr.one,4)]
    else:
        affine=monomials(1);quadratic=[m for m in monomials(2)if sum(m)==2]
        blocks=[('free'+str(i),affine+[m for m in quadratic if m[i]],rr.one,4)for i in range(6)]
        blocks.append(('free6',[m for m in quadratic if max(m)==1],rr.one,4))
    blocks += [(key,monomials(1),g,4 if full else 1)for key,g in gs.items()]
    vals=[];ri=[];ci=[];cobj=[];metadata=[];cones=[clarabel.ZeroConeT(n_eq)]
    prow=n_eq;col=0;cone_rhs=[]
    for key,mons,g,n in blocks:
        dim=len(mons)*n;entries=[]
        for j in range(dim):
            for i in range(j+1):
                m,a=mons[i//n],i%n;v,b=mons[j//n],j%n
                power=tuple(x+y for x,y in zip(m,v));factor=2 if a==b and i!=j else 1
                for gm,gc in g.items():
                    exp=tuple(x+y for x,y in zip(power,gm))
                    if n==4:
                        row=rows[min(a,b),max(a,b),exp]
                        ri.append(row);ci.append(col);vals.append(float(gc)*factor)
                    else:
                        for a2 in range(4):
                            ri.append(rows[a2,a2,exp]);ci.append(col);vals.append(float(gc)*factor)
                ri.append(prow);ci.append(col);vals.append(-1 if i==j else -2**.5)
                cone_rhs.append(-1e-3 if i==j else 0.0)
                cobj.append(1.0 if i==j else 0.0)
                entries.append((i,j,col));prow+=1;col+=1
        cones.append(clarabel.PSDTriangleConeT(dim));metadata.append(dict(key=key,dim=dim,mons=mons,n=n,entries=entries))
    A=sp.csc_matrix((vals,(ri,ci)),shape=(prow,col));bvec=np.r_[bvec,cone_rhs]
    return A,bvec,np.array(cobj),cones,metadata


def main():
    p=argparse.ArgumentParser();p.add_argument('--control',type=int,default=2);p.add_argument('--scalar',action='store_true');p.add_argument('--solver',default='faer');p.add_argument('--structure',default='sparse');args=p.parse_args()
    lock=Path('sos_discovery.lock').open('a')
    fcntl.flock(lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
    start=time.monotonic()
    try:
        resource.setrlimit(resource.RLIMIT_AS,(2_100_000_000,2_100_000_000))
        print('NUMERICAL address-space cap set to 2,100,000,000 bytes',flush=True)
    except (ValueError,OSError)as exc:
        print('OPEN: address-space cap unavailable',str(exc),flush=True)
    Path('sos_worker.pid').write_text(str(os.getpid())+'\n')
    def guard():
        while True:
            time.sleep(.1)
            if Path('stop_sos_'+str(os.getpid())).exists():
                print('OPEN: owned stop flag received',flush=True);os._exit(125)
            peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if int((time.monotonic()-start)*10)%200==0:
                print('NUMERICAL resource peak bytes',peak,'seconds',time.monotonic()-start,flush=True)
            if peak>1_950_000_000 or time.monotonic()-start>900:
                print('OPEN: resource guard stopping solve; peak',peak,flush=True)
                os._exit(124)
    threading.Thread(target=guard,daemon=True).start()
    A,b,c,cones,meta=setup(args.control,not args.scalar,args.structure)
    print('NUMERICAL dimensions',A.shape,'nonzeros',A.nnz,flush=True)
    settings=clarabel.DefaultSettings();settings.verbose=True;settings.max_iter=80
    settings.tol_gap_abs=1e-10;settings.tol_gap_rel=1e-10;settings.tol_feas=1e-12
    settings.max_threads=1;settings.time_limit=880;settings.direct_solve_method=args.solver
    solver=clarabel.DefaultSolver(sp.csc_matrix((len(c),len(c))),c,A,b,cones,settings)
    result=solver.solve()
    data=dict(status=str(result.status),control=args.control,scalar=args.scalar,seconds_NUMERICAL=time.monotonic()-start,
              peak_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              x=list(result.x),metadata=meta)
    Path('sos_candidate_'+str(args.control)+'.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
    print('NUMERICAL status',result.status,'seconds',data['seconds_NUMERICAL'],flush=True)

if __name__=='__main__':main()
