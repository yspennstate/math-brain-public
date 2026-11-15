#!/usr/bin/env python3
"""Reproducible sequential experiment runner. No worker pool; one solver thread."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','HIGHS_THREADS'): os.environ[k]='1'
import argparse, hashlib, json, math, pathlib, resource, subprocess, sys, time, warnings, signal
ROOT=pathlib.Path(__file__).resolve().parents[1]; EXE=ROOT/'code'/'bisection'
DATA=ROOT/'data'; GRAPHS=DATA/'graphs'; GRAPHS.mkdir(exist_ok=True)
# These limits are far larger than actual working memory (~50 MB C++, ~200 MB SciPy).
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def guard():
    nice=os.getpriority(os.PRIO_PROCESS,0)
    if nice<10: raise RuntimeError(f'Need nice >=10, got {nice}')
    f=pathlib.Path.home()/'.claude/compute/compute_state.json'
    if f.exists():
        state=json.loads(f.read_text())
        if state.get('status')=='distress':
            raise RuntimeError('Compute governor requests yielding: '+str(state.get('status'))+'/'+str(state.get('mode')))

def run(args):
    # One child, with a 20% wall-clock run allowance when the human is present.
    # SIGSTOP/SIGCONT only touch this runner's own child, never other workloads.
    guard()
    proc=subprocess.Popen([str(EXE),*map(str,args)],text=True,cwd=ROOT,stdout=subprocess.PIPE)
    state={};last=0
    while proc.poll() is None:
        if time.monotonic()-last>5:
            f=pathlib.Path.home()/'.claude/compute/compute_state.json'
            state=json.loads(f.read_text()) if f.exists() else {};last=time.monotonic()
        if state.get('status')=='distress':
            proc.terminate();proc.wait();raise RuntimeError('Stopped own compute child on governor distress')
        if state.get('mode')=='throttle' or state.get('owner_active'):
            time.sleep(.02)
            if proc.poll() is None:
                try:proc.send_signal(signal.SIGSTOP)
                except ProcessLookupError:continue
                time.sleep(.08)
                try:proc.send_signal(signal.SIGCONT)
                except ProcessLookupError:pass
        else:time.sleep(.05)
    output=proc.communicate()[0]
    if proc.returncode:raise RuntimeError(f'Child failed with {proc.returncode}: {args}')
    return json.loads(output)

def make_graph(n,d,i):
    path=GRAPHS/f'd{d}_n{n}_i{i:03}.graph';seed=530000000+d*10000000+n*100+i
    if not path.exists():
        guard(); meta=run(['generate',n,d,seed,path]);path.with_suffix('.meta.json').write_text(json.dumps(meta,indent=2)+'\n')
    return path,seed

def edges_of(path):
    with path.open() as f:
        n,d=map(int,next(f).split());edges=[tuple(map(int,l.split())) for l in f]
    assert len(edges)==n*d//2 and len(set(tuple(sorted(e)) for e in edges))==len(edges)
    deg=[0]*n
    for u,v in edges: assert u!=v;deg[u]+=1;deg[v]+=1
    assert deg==[d]*n
    return n,d,edges

def validate(path,rows):
    n,d,edges=edges_of(path)
    for row in rows:
        s=row['spin'];assert len(s)==n and s.count('1')==n//2
        cut=sum(s[u]!=s[v] for u,v in edges);assert cut==row['cut'],(row,cut)
        assert cut%2==(d*n//2)%2

def milp(path,objective,seconds=15):
    import numpy as np
    from scipy.optimize import milp, Bounds, LinearConstraint
    from scipy.sparse import coo_array
    n,d,edges=edges_of(path);m=len(edges);rr=[];cc=[];vv=[];lower=[];upper=[]
    def add(cols,vals,lo,hi):
        idx=len(lower);rr.extend([idx]*len(cols));cc.extend(cols);vv.extend(vals);lower.append(lo);upper.append(hi)
    add(list(range(n)),[1]*n,n//2,n//2);add([0],[1],0,0)
    for j,(u,v) in enumerate(edges):
        y=n+j
        add([u,v,y],[1,-1,-1],-np.inf,0)
        add([u,v,y],[-1,1,-1],-np.inf,0)
        add([u,v,y],[-1,-1,1],-np.inf,0)
        add([u,v,y],[1,1,1],-np.inf,2)
    A=coo_array((vv,(rr,cc)),shape=(len(lower),n+m)).tocsc()
    c=np.zeros(n+m);c[n:]=1 if objective=='min' else -1
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='Unrecognized options detected')
        res=milp(c,integrality=np.ones(n+m),bounds=Bounds(0,1),constraints=LinearConstraint(A,lower,upper),options={'threads':1,'time_limit':seconds,'mip_rel_gap':0})
    result={'objective':objective,'status':int(res.status),'message':res.message}
    if res.x is not None:
        s=''.join(str(int(round(x))) for x in res.x[:n]);cut=sum(s[u]!=s[v] for u,v in edges)
        assert s.count('1')==n//2 and abs(cut-abs(res.fun))<1e-5
        result.update(cut=cut,spin=s,dual_bound=float(res.mip_dual_bound)*(1 if objective=='min' else -1),gap=float(res.mip_gap),nodes=int(res.mip_node_count))
    return result

def main():
    global EXE
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['small','large','deep','sa']);args=p.parse_args();guard()
    engine_source=('code/archive/bisection_initial.cpp' if args.mode=='small' else 'code/bisection_fast.cpp' if args.mode in ['deep','sa'] else 'code/bisection.cpp')
    if args.mode in ['deep','sa']:EXE=ROOT/'code/bisection_fast'
    elif args.mode=='small':EXE=ROOT/'code/bisection_initial'
    out=DATA/f'{args.mode}.jsonl';done={}
    if out.exists():
        for line in out.read_text().splitlines():
            row=json.loads(line);done[(row['d'],row['n'],row['instance'])]=row
    if args.mode=='small': plan=[(n,12) for n in [12,16,20,24]]+[(32,4),(48,2)]
    elif args.mode=='large':plan=[(n,12) for n in [64,128,256,512,1024,2048,4096]]+[(8192,8),(16384,6),(32768,4)]
    elif args.mode=='deep':plan=[(n,4) for n in [128,256,512,1024]]+[(n,3) for n in [2048,4096]]
    else:plan=[(n,3) for n in [128,512,2048,8192]]
    for n,samples in plan:
      for d in (3,4,5):
       for i in range(samples):
        if (d,n,i) in done:continue
        guard();path,seed=make_graph(n,d,i);base={'d':d,'n':n,'instance':i,'graph_seed':seed,'graph':str(path.relative_to(ROOT)),'nice':os.getpriority(os.PRIO_PROCESS,0)}
        t=time.monotonic()
        if args.mode=='small':
            if n<=24:
                result=run(['exact',path]);base['exact']=result
                if i==0 and n in [12,20]:
                    base['milp']=[milp(path,o) for o in ['min','max']]
                    for r in base['milp']:assert r['status']==0 and r['cut']==result[r['objective']]
            else:base['milp']=[milp(path,o,10) for o in ['min','max']]
            restarts,sweeps=4,2000
        elif args.mode=='large':restarts,sweeps=4,(2000 if n<=2048 else 1000)
        elif args.mode=='deep':restarts,sweeps=(12,6000) if n<=1024 else (8,4000)
        else:restarts,sweeps=4,2000
        trace=DATA/'traces'/f'{args.mode}_d{d}_n{n}_i{i:03}.jsonl';trace.parent.mkdir(exist_ok=True)
        method='sa' if args.mode=='sa' else 'eo';solver_seed=seed+{'small':0,'large':10000000000,'deep':20000000000,'sa':30000000000}[args.mode]
        summary=run(['solve',path,restarts,sweeps,solver_seed,method,trace]);rows=[json.loads(l) for l in trace.read_text().splitlines()];validate(path,rows)
        if 'exact' in base:
            assert summary['min']>=base['exact']['min'] and summary['max']<=base['exact']['max']
        for r in base.get('milp',[]):
            if r['status']==0:assert summary[r['objective']] == r['cut'],(base,r,summary)
        base.update(summary,engine_source=engine_source,engine_source_sha256=hashlib.sha256((ROOT/engine_source).read_bytes()).hexdigest(),method=method,restarts=restarts,sweeps=sweeps,solver_seed=solver_seed,trace=str(trace.relative_to(ROOT)),wall_seconds=time.monotonic()-t)
        with out.open('a') as f:f.write(json.dumps(base)+'\n');f.flush()
        print(f"{args.mode} d={d} n={n} i={i} min={summary['min']/n:.6f} max={summary['max']/n:.6f} delta={(summary['min']+summary['max'])/n-d/2:+.6f} time={base['wall_seconds']:.2f}s",flush=True)
    (DATA/f'{args.mode}_complete.json').write_text(json.dumps({'finished':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'nice':os.getpriority(os.PRIO_PROCESS,0),'maxrss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'maxrss_children':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss},indent=2)+'\n')
if __name__=='__main__':main()
