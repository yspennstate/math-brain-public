"""Exact finite regression checks. A closed/failing compute gate returns 3, never PASS."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
import time

ROOT=Path(__file__).resolve().parent
STATE=Path('~/.claude/compute/compute_state.json')

def gate():
    now=time.time()
    try:
        st=STATE.stat()
        raw=json.loads(STATE.read_text(encoding='utf-8-sig'))
        age=now-st.st_mtime
        allowed=(-2<=age<=60 and raw.get('status') in {'ok','normal','healthy'} and raw.get('mode')!='throttle')
        return {'path':str(STATE),'observed_unix':now,'mtime_age_seconds':round(age,3),'ts':raw.get('ts'),'status':raw.get('status'),'mode':raw.get('mode'),'reasons':raw.get('reasons'),'cpu_pct':raw.get('cpu_pct'),'mem_avail_mb':raw.get('mem_avail_mb'),'commit_used_pct':raw.get('commit_used_pct'),'allowed':allowed}
    except (OSError,ValueError) as e:
        return {'path':str(STATE),'observed_unix':now,'allowed':False,'error':str(e)}

def run():
    start=time.monotonic()
    receipt={'command':'python -B -X utf8 ~/brain_workers/w396/local_checks.py','status':'NOT_RUN','formal_check':False,'assertions':0,'populations':0,'graph_masks_completed':0,'gate':gate()}
    def save():
        receipt['elapsed_seconds']=round(time.monotonic()-start,4)
        (ROOT/'FINITE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    if not receipt['gate']['allowed']:
        receipt['status']='DEFERRED_COMPUTE_GATE'
        save()
        print(json.dumps(receipt),flush=True)
        return 3
    stats={'prefix_ratio_checks':0,'maximal_bound_checks':0,'total_variation_checks':0}
    edges=list(combinations(range(4),2))
    def check(condition):
        receipt['assertions']+=1
        if not condition:
            raise AssertionError('Exact check failed')
    for mask in range(64):
        if mask%8==0:
            receipt['gate']=gate()
            if not receipt['gate']['allowed'] or time.monotonic()-start>20:
                receipt['status']='DEFERRED_COMPUTE_GATE' if not receipt['gate']['allowed'] else 'DEFERRED_20_SECOND_BUDGET'
                receipt.update(stats)
                save()
                print(json.dumps(receipt),flush=True)
                return 3
        adj={v:[] for v in range(4)}
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                adj[u].append(v); adj[v].append(u)
        for profile in range(4):
            weight={e:([F(1,2),F(2,3),F(1)][profile] if profile<3 else F(i+2,9)) for i,e in enumerate(edges)}
            def q(u,v): return weight[tuple(sorted((u,v)))]
            for kind in ['fixed1','fixed2','fixed3','chordal']:
                n=int(kind[-1]) if kind!='chordal' else None
                leaves=[]
                def dfs(path,w):
                    v=path[-1]
                    if (n is not None and len(path)-1==n) or (n is None and v==3):
                        leaves.append((tuple(path),w)); return
                    for u in adj[v]:
                        if u not in path: dfs(path+[u],w*q(v,u))
                dfs([0],F(1))
                if not leaves: continue
                receipt['populations']+=1
                z=sum((w for _,w in leaves),F(0))
                horizon=max(len(p)-1 for p,_ in leaves)
                candidates=[1,2,3] if n is not None else [1,2]
                obstacles=[frozenset(v for i,v in enumerate(candidates) if a>>i&1) for a in range(1<<len(candidates))]
                roots={a:sum((w for p,w in leaves if not a.intersection(p)),F(0))/z for a in obstacles}
                @lru_cache(None)
                def count(v,excluded,remaining):
                    if v in excluded:return F(0)
                    if n is None and v==3:return F(1)
                    if n is not None and remaining==0:return F(1)
                    return sum((q(v,u)*count(u,excluded|{v},remaining-1) for u in adj[v] if u not in excluded and u!=v),F(0))
                groups=[]; values=[]
                for k in range(horizon+1):
                    gs={}
                    for i,(p,w) in enumerate(leaves):
                        key=(p[:min(k,len(p)-1)+1],k>=len(p)-1)
                        gs.setdefault(key,[]).append(i)
                    groups.append(gs)
                    vals={}
                    for key,idxs in gs.items():
                        prefix,complete=key
                        mass=sum((leaves[i][1] for i in idxs),F(0))
                        for a in obstacles:
                            direct=sum((leaves[i][1] for i in idxs if not a.intersection(leaves[i][0])),F(0))/mass
                            if complete: predicted=F(not a.intersection(prefix))
                            elif a.intersection(prefix):predicted=F(0)
                            else:
                                past=frozenset(prefix[:-1]); remaining=(n-(len(prefix)-1)) if n is not None else -1
                                denom=count(prefix[-1],past,remaining)
                                check(denom>0)
                                predicted=count(prefix[-1],past|a,remaining)/denom
                            check(direct==predicted)
                            stats['prefix_ratio_checks']+=1
                            vals[(key,a)]=predicted
                    values.append(vals)
                for a in obstacles:
                    for b in obstacles:
                        if not a<=b:continue
                        d0=roots[a]-roots[b]
                        for lam in [F(1,3),F(2,3),F(1)]:
                            cross=F(0)
                            for p,w in leaves:
                                maximum=F(0)
                                for k in range(horizon+1):
                                    key=(p[:min(k,len(p)-1)+1],k>=len(p)-1)
                                    maximum=max(maximum,values[k][(key,a)]-values[k][(key,b)])
                                if maximum>=lam:cross+=w/z
                            check(cross<=d0/lam)
                            stats['maximal_bound_checks']+=1
                        if roots[b]>0:
                            tv=sum((abs((w/z/roots[a] if not a.intersection(p) else F(0))-(w/z/roots[b] if not b.intersection(p) else F(0))) for p,w in leaves),F(0))/2
                            check(tv==1-roots[b]/roots[a])
                            stats['total_variation_checks']+=1
                count.cache_clear()
        receipt['graph_masks_completed']=mask+1
        receipt.update(stats)
        save()
    receipt['status']='PASS_EXACT_FINITE_REGRESSION_ONLY'
    save()
    print(json.dumps(receipt),flush=True)
    return 0

if __name__=='__main__':
    raise SystemExit(run())
