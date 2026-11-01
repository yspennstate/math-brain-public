import audit as a
from exact import Q,check
import exact as e
from pathlib import Path
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter()
def main():
    pilot='--pilot' in sys.argv;source='--source' in sys.argv
    lo=int(sys.argv[sys.argv.index('--start')+1]) if '--start' in sys.argv else 0
    hi=int(sys.argv[sys.argv.index('--end')+1]) if '--end' in sys.argv else (2 if pilot else 81)
    count=0
    if source:
        cores=[e.tab(m,n) for n in (0,1,2) for m in range(1<<(1<<n))]
        opss=[[('c',0),('c',1),('c',3)],[('c',0),('d',0),('c',1),('c',3)],[('c',0),('d',1),('c',1),('c',3)],[('c',0),('d',1),('c',1),('d',0),('c',3)]]
        for u in cores[lo:hi]:
            for v in cores:
                for o in (0,1):
                    c=a.controller(1,1,o)
                    for ops in opss:a.tree(c,(u,v),(0,1,3),ops);count+=1
            a.coeff.cache_clear();a.spec.cache_clear()
            assert time.perf_counter()-START<180
    else:
        maps=list(itertools.product(range(3),repeat=4))
        cores=[e.tab(m,1) for m in range(4)]
        for ww in maps[lo:hi]:
            for us in itertools.product(cores,repeat=3):
                for r in (1,2,3):
                    c=tuple(1 if x%(1<<r)==0 else (0 if ww[x>>r]==0 else ww[x>>r]+1) for x in range(1<<(r+2)))
                    ids=(1,)+tuple(range(4,r+5))
                    a.local(c,us,ids,'c',1);count+=1
            a.coeff.cache_clear();a.spec.cache_clear()
            assert time.perf_counter()-START<(55 if pilot else 180)
    out={'status':'PASS','source_review':source,'pilot':pilot,'slice':[lo,hi],'cases':count,'stats':a.STATS,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-START}
    name=('SOURCE' if source else 'GENERAL')+('_PILOT' if pilot else f'_{lo}_{hi}')+'.json'
    (R/'out'/name).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
