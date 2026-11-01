"""Independent exact edge audit; all 4-state partitions on 2 physical controls."""
import itertools,time,json,hashlib,sys
from fractions import Fraction as Q
import check as c
reps={sum(f):f for f in itertools.product((-1,1),repeat=4)}
def root(labels,u,v):
    return tuple(1 if labels[z&3]==0 else -1 if labels[z&3]==1 else u[(z>>2)&3] if labels[z&3]==2 else v[z>>4] for z in range(64))
def run(pilot):
    start=time.monotonic();cases=checks=0;minimum=None
    for li,labels in enumerate(itertools.product(range(4),repeat=4)):
        cs=[tuple(int(x==j) for x in labels) for j in (2,3)]
        qs=[Q(sum(f),4) for f in cs];ic=[sum(c.inf(f,i) for i in range(2)) for f in cs]
        for q,i in zip(qs,ic):
            iso=c.add(c.scale(c.phi(q),-2),((2,i),) if i else ())
            assert not iso or c.log_bounds(iso)[0]>=0
            checks+=1
        for u,v in itertools.product(reps.values(),repeat=2):
            f=root(labels,u,v);mu=c.walsh(u)[0];nu=c.walsh(v)[0];V=(1-mu*mu,1-nu*nu)
            ctrl=sum(c.inf(f,i) for i in range(2));edgeweighted=sum(a*b for a,b in zip(V,ic))
            assert edgeweighted<=4*ctrl;checks+=1
            # Do not add event accounts: count each physical control edge once.
            direct=Q(0)
            means=(Q(1),Q(-1),mu,nu)
            for i in range(2):
                for z in range(4):
                    a=labels[z];b=labels[z^(1<<i)]
                    direct+=Q(0) if a==b else (1-means[a]*means[b])/8
            assert direct==ctrl;checks+=1
            reserve=c.add(*(c.scale(c.phi(q),vv) for q,vv in zip(qs,V)))
            slack=c.add(((2,2*ctrl),) if ctrl else (),c.scale(reserve,-1))
            assert not slack or c.log_bounds(slack)[0]>=0;checks+=1
            cases+=1
        if time.monotonic()-start>(55 if pilot else 180):raise RuntimeError('frozen runtime reached')
        if pilot and li==7:break
    out={'status':'PASS','Boolean_cases':cases,'exact_assertions':checks,'controllers':8 if pilot else 256,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(c.Path(__file__).read_bytes()).hexdigest(),'scope':'Selector reserve and exclusive control edges only; no entropy/terminal payment asserted'}
    (c.ROOT/'out'/('CONTROLLER_PILOT.json' if pilot else 'CONTROLLER_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
if __name__=='__main__':run(sys.argv[1]=='pilot')
