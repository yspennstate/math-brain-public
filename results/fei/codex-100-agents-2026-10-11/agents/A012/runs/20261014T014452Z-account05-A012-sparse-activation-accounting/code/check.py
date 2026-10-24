import sys,time
from functools import lru_cache
import exact as e
from exact import Q,ck,cutoff,save,fwht,inf,entropy,cross,add,scalar,Lv,binary,vint
mode=sys.argv[1];assert mode in ('pilot','full')
shard=int(sys.argv[2]) if len(sys.argv)>2 else None
assert shard is None or (mode=='full' and 0<=shard<8)
def family(n):
    out=[]
    for mask in range(1<<(1<<n)):
        tab=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));hat=tuple(fwht(tab))
        out.append((tab,hat,inf(tab),{t:h*h for t,h in enumerate(hat) if h}))
    return out
def embed(t,private):return ((t&3)<<1)|((t>>2)<<private)
@lru_cache(maxsize=10000)
def packets(a,b):
    # Fold only the proof row; actual physical outputs are checked separately.
    d=(1-sum(x*y for x,y in zip(a,b)))/2
    folded=d>Q(1,2)
    if folded:b=tuple(-x for x in b);d=1-d
    delta=sum((x-y)**2/4 for x,y in zip(a,b));vg=1-sum(x*x for x in a);vh=1-sum(y*y for y in b)
    Bout=(vg+vh)/2;ck(Bout==2*(d-delta));ck(delta<=d and delta<=4*d*d)
    BC={};JC={}
    for x,y in zip(a,b):
        A=(x+y)**2/4;B=(x-y)**2/4;m=A+B
        BC=add((1,BC),(1,Lv(A)),(1,Lv(B)),(-1,Lv(m)))
        JC=add((1,JC),(1,Lv(m)),(-Q(1,2),Lv(x*x)),(-Q(1,2),Lv(y*y)))
    B=add((1,scalar(Bout)),(1,BC));J=add((1,scalar(Bout)),(1,JC));tax=add((1,B),(1,J))
    ck(not add((1,binary(delta)),(-1,BC)) or vint(add((1,binary(delta)),(-1,BC)))[0]>0)
    slack=add((1,scalar(4*d)),(-1,B));ck(not slack or vint(slack)[0]>0)
    slack7=add((1,scalar(7*d)),(-1,tax));ck(not slack7 or vint(slack7)[0]>0)
    # Original A095 t=2 upper bound is independently checked at rational 17/2 > 4+3/ln2.
    slack95=add((1,scalar(Q(17,2)*d)),(-1,tax));ck(not slack95 or vint(slack95)[0]>0)
    return d,delta,B,tax
def cal(P,n,kind):
    R={t:P.get(t,Q(0)) for t in range(4)};v=1-sum(R.values())
    for t in range(4,1<<n):R[t]=P.get(t,Q(0)) if kind==0 else v/((1<<n)-4)
    return R
def intwalsh(tab):
    a=list(tab);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
        h*=2
    return a
Gs=family(3);Hs=family(2 if mode=='pilot' else 3);cases=refs=0
Gmaps=[{embed(t,3):int(8*v) for t,v in enumerate(entry[1])} for entry in Gs]
Hmaps=[{embed(t,4):int(8*v) for t,v in enumerate(entry[1])} for entry in Hs]
for gi,(g,ah,ig,Pg) in enumerate(Gs):
    if shard is not None and gi//32!=shard:continue
    for hi,(h,bh,ih,Ph) in enumerate(Hs):
        cutoff();cases+=1
        d,delta,B,tax=packets(ah[:4],bh[:4])
        n=4 if mode=='pilot' else 5;N=1<<n
        f=[g[((x>>1)&3)|(((x>>3)&1)<<2)] if not x&1 else h[((x>>1)&3)|(((x>>4)&1)<<2)] for x in range(N)]
        raw=intwalsh(f);ahmap=Gmaps[gi];bhmap=Hmaps[hi]
        expected=[N*(ahmap.get(s&~1,0)+(1 if not s&1 else -1)*bhmap.get(s&~1,0)) for s in range(N)]
        ck([16*c for c in raw]==expected)
        physical=inf(f);actuald=(1-sum(ah[t]*bh[t] for t in range(4)))/2
        ck(physical[0]==actuald);ck(sum(physical[1:])==(sum(ig)+sum(ih))/2)
        if mode=='pilot' or (gi<16 and hi<16):
            P={s:Q(c*c,N*N) for s,c in enumerate(raw) if c}
            HF=entropy(P.values());Hg=entropy(Pg.values());Hh=entropy(Ph.values())
            ck(HF==add((Q(1,2),Hg),(Q(1,2),Hh),(1,tax)))
            for kind in (0,1):
                refs+=1;Rg=cal(Pg,3,kind);Rh=cal(Ph,2 if mode=='pilot' else 3,kind);R={}
                for t in range(4):
                    for u in (0,1):R[embed(t,3)|u]=(ah[t]+(-1)**u*bh[t])**2/4
                for Rc,private in [(Rg,3),(Rh,4)]:
                    for t,v in Rc.items():
                        if t>=4:
                            for u in (0,1):R[embed(t,private)|u]=v/4
                ck(sum(R.values())==1);CF=cross(P,R);Cg=cross(Pg,Rg);Ch=cross(Ph,Rh)
                ck(CF==add((Q(1,2),Cg),(Q(1,2),Ch),(1,tax)))
                ck(add((1,CF),(-1,HF))==add((Q(1,2),Cg),(-Q(1,2),Hg),(Q(1,2),Ch),(-Q(1,2),Hh)))
save('EXACT_'+mode+('' if shard is None else '_'+str(shard))+'.json',{'status':'PASS','shard':shard,'cases':cases,'references':refs,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start,'collision_parameter_fixtures':packets.cache_info().currsize,'memory_estimate_mb':100,'peak_memory':'not instrumented','max_truth_table_dimension':4 if mode=='pilot' else 5,'arithmetic':'integer FWHT / physical edges / Fraction / exact prime-log vectors / outward rational bounds'})
