"""Stream nonisomorphic regular graphs and exhaust edges/complement matchings.
Numerical rankings are exploratory; certify.py independently proves strict failures.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse, subprocess, json, time, resource
from pathlib import Path
import numpy as np
import networkx as nx
ROOT=Path(__file__).resolve().parents[1]
GENG=ROOT/'code/vendor/nauty2_9_3/geng'

def matchings(adj,vertices=None):
    vs=tuple(range(len(adj))) if vertices is None else vertices
    if not vs:
        yield ();return
    u=vs[0]
    for i in range(1,len(vs)):
        v=vs[i]
        if not adj[u,v]:
            for tail in matchings(adj,vs[1:i]+vs[i+1:]):yield ((u,v),)+tail

def matrix(adj,extra=()):
    a=adj.copy()
    for u,v in extra:a[u,v]+=1;a[v,u]+=1
    d=a.sum(axis=1)
    return np.diag(d)-a,d

def gap(adj,extra=()):
    l,d=matrix(adj,extra);return float(np.linalg.eigvalsh(l/np.sqrt(d[:,None]*d[None,:]))[1])

def matching_search(a,vec,mu):
    n=len(a);d=int(a[0].sum()); rows=[]; mats=[]; count=0; best=-1; bests=[]
    hmax=-1; hchoices=[]
    # For a matching, the normalization penalty sum f(v)^2 is constant.
    def consume():
        nonlocal best,bests,hmax,hchoices,count
        if not rows:return
        vals=1-np.linalg.eigvalsh(np.asarray(mats,dtype=float)/(d+1))[:,-2]
        for m,g in zip(rows,vals):
            count+=1; g=float(g)
            if g>best+1e-10:best=g;bests=[m]
            elif abs(g-best)<1e-10:bests.append(m)
            score=sum((vec[u]-vec[v])**2 for u,v in m)
            if score>hmax+1e-10:hmax=score;hchoices=[(m,g)]
            elif abs(score-hmax)<1e-10:hchoices.append((m,g))
        rows.clear();mats.clear()
    for m in matchings(a):
        b=a.copy()
        for u,v in m:b[u,v]=b[v,u]=1
        rows.append(m);mats.append(b)
        if len(rows)==2048:consume()
    consume()
    if not count:return {'count':0}
    return {'count':count,'gap_best':best,'best':bests,'heuristic_score':float(hmax),'heuristic':hchoices,
            'strong_failure':max(g for _,g in hchoices)<best-1e-9}

def run(n,d,do_matching):
    out=ROOT/'data'/f'search_d{d}_n{n}.jsonl'
    outg=ROOT/'data'/f'graphs_d{d}_n{n}.g6'
    start=time.monotonic();counts={'graphs':0,'simple_gap':0,'multiple_gap':0,'edge_candidates':0,'matching_candidates':0,'naive_strong_failures':0,'corrected_strong_failures':0,'matching_strong_failures':0,'matching_multiple_not_compared':0}
    proc=subprocess.Popen([str(GENG),'-cq',f'-d{d}',f'-D{d}',str(n)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    with out.open('w') as f,outg.open('wb') as gf:
      for idx,line in enumerate(proc.stdout):
        gf.write(line);g=nx.from_graph6_bytes(line.strip());a=nx.to_numpy_array(g,dtype=float)
        w,v=np.linalg.eigh(np.diag(a.sum(axis=1))-a);mu=float(w[1]/d);vec=v[:,1]
        simple=w[2]-w[1]>1e-8;counts['graphs']+=1;counts['simple_gap' if simple else 'multiple_gap']+=1
        edges=[(u,v) for u in range(n) for v in range(u+1,n) if not a[u,v]]
        vals=[gap(a,[e]) for e in edges];counts['edge_candidates']+=len(edges)
        rec={'id':idx,'n':n,'d':d,'g6':line.decode().strip(),'mu':mu,'eigenvalues_L':w.tolist(),'simple':bool(simple),'edges':edges,'edge_gaps':vals}
        if edges:
          best=max(vals);bestes=[e for e,x in zip(edges,vals) if abs(x-best)<1e-9];rec['best_edge_gap']=best;rec['best_edges']=bestes
          if simple:
            for name in ('naive','corrected'):
              scores=[(vec[u]-vec[v])**2-(mu*(vec[u]**2+vec[v]**2) if name=='corrected' else 0) for u,v in edges]
              top=max(scores);hs=[e for e,x in zip(edges,scores) if abs(x-top)<1e-9]
              hvals=[x for e,x in zip(edges,vals) if e in hs]
              fail=max(hvals)<best-1e-9
              rec[name]={'scores':scores,'choices':hs,'strong_failure':fail,'any_choice_loses':min(hvals)<best-1e-9}
              counts[name+'_strong_failures']+=int(fail)
        if do_matching:
          m=matching_search(a,vec,mu);rec['matching']=m;counts['matching_candidates']+=m['count']
          if not simple:
            if m['count']:m['strong_failure']=None;counts['matching_multiple_not_compared']+=1
          elif m['count']:counts['matching_strong_failures']+=int(m['strong_failure'])
        f.write(json.dumps(rec,separators=(',',':'))+'\n');f.flush()
        if (idx+1)%100==0:print(n,d,idx+1,'elapsed',round(time.monotonic()-start,1),flush=True)
    proc.wait();err=proc.stderr.read().decode()
    if proc.returncode:raise RuntimeError(err)
    counts.update(n=n,d=d,matching_exhausted=do_matching,elapsed_seconds=time.monotonic()-start,nice=os.getpriority(os.PRIO_PROCESS,0),peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (ROOT/'data'/f'summary_d{d}_n{n}.json').write_text(json.dumps(counts,indent=2)+'\n');print(counts,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,required=True);p.add_argument('--d',type=int,required=True);p.add_argument('--matching',action='store_true');args=p.parse_args();run(args.n,args.d,args.matching)
