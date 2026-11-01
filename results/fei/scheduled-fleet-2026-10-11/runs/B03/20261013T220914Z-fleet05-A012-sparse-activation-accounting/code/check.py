import exact as e
from exact import Q,fwht,inf,entropy,cross,add,scalar,Lv,vint,ck,cutoff,save
import time

def cores(n):
    return [[1 if mask>>x&1 else -1 for x in range(1<<n)] for mask in range(1<<(1<<n))]
def probs(a): return {t:x*x for t,x in enumerate(fwht(a)) if x}
def calibrated(P,n,mode):
    if mode==0:return dict(P)
    m=P.get(0,Q(0));R={0:m}
    for t in range(1,1<<n):R[t]=(1-m)/((1<<n)-1)
    return R
def delta(mu,nu):
    return add((1,scalar(2-mu*mu-nu*nu)),(1,Lv((mu+nu)**2/4)),(1,Lv((mu-nu)**2/4)),(-Q(1,2),Lv(mu*mu)),(-Q(1,2),Lv(nu*nu)))

pairs=refs=acts=0;fixtures=[];biaspairs=set()
for n,k in [(2,2),(3,1)]:
    for g in cores(n):
        Pg=probs(g);mu=fwht(g)[0];Hg=entropy(Pg.values());Ig=sum(inf(g))
        for h in cores(k):
            cutoff();pairs+=1
            Ph=probs(h);nu=fwht(h)[0];Hh=entropy(Ph.values());Ih=sum(inf(h));d=(1-mu*nu)/2
            f=[g[(x>>1)&((1<<n)-1)] if x&1 else h[x>>(n+1)] for x in range(1<<(n+k+1))]
            P=probs(f);expect={}
            for u in (0,1):
                expect[u]=((mu+nu)/2 if u==0 else (mu-nu)/2)**2
                for t,v in Pg.items():
                    if t:expect[u|(t<<1)]=v/4
                for t,v in Ph.items():
                    if t:expect[u|(t<<(n+1))]=v/4
            ck(P=={s:v for s,v in expect.items() if v})
            physical=inf(f);ck(physical[0]==d);ck(sum(physical[1:])==(Ig+Ih)/2)
            HF=entropy(P.values());tax=delta(mu,nu)
            ck(HF==add((Q(1,2),Hg),(Q(1,2),Hh),(1,tax)))
            if (mu,nu) not in biaspairs:
                biaspairs.add((mu,nu))
                if d:ck(vint(add((Q(15,2)*d,scalar(1)),(-1,tax)))[0]>0)
                else:ck(not tax)
            for mode in (0,1):
                refs+=1;Rg=calibrated(Pg,n,mode);Rh=calibrated(Ph,k,mode);R={0:expect[0],1:expect[1]}
                for u in (0,1):
                    for t,v in Rg.items():
                        if t:R[u|(t<<1)]=v/4
                    for t,v in Rh.items():
                        if t:R[u|(t<<(n+1))]=v/4
                ck(sum(R.values())==1)
                Cg=cross(Pg,Rg);Ch=cross(Ph,Rh);CF=cross(P,R)
                ck(CF==add((Q(1,2),Cg),(Q(1,2),Ch),(1,tax)))
                ck(add((1,CF),(-1,HF))==add((Q(1,2),Cg),(-Q(1,2),Hg),(Q(1,2),Ch),(-Q(1,2),Hh)))
                if len(fixtures)<4 and mu!=nu and mode==1:
                    fixtures.append({'mu':str(mu),'nu':str(nu),'d':str(d),'tax':e.vec(tax),'Q':{str(s):str(v) for s,v in R.items()}})
save('MUX_RESULTS.json',{'status':'PASS','pairs':pairs,'references':refs,'bias_pairs':len(biaspairs),'assertions_so_far':e.checks,'fixtures':fixtures})

for n in (1,2,3):
    for g in cores(n):
        Pg=probs(g);mu=fwht(g)[0];Hg=entropy(Pg.values());Rg=calibrated(Pg,n,1);Cg=cross(Pg,Rg);Ig=sum(inf(g))
        for r in (1,2):
            cutoff();acts+=1;p=Q(1,1<<r)
            f=[g[x>>r] if x&((1<<r)-1)==0 else 1 for x in range(1<<(n+r))]
            P=probs(f);R={0:(1-p*(1-mu))**2}
            for u in range(1<<r):
                if u:R[u]=p*p*(1-mu)**2
                for t,v in Rg.items():
                    if t:R[u|(t<<r)]=p*p*v
            ck(sum(R.values())==1);HF=entropy(P.values());CF=cross(P,R)
            ck(add((1,CF),(-1,HF))==add((p,Cg),(-p,Hg)))
            ck(sum(inf(f))==p*(Ig+r*(1-mu)))
            slack=add((p,Cg),(1,scalar(6*r*p*(1-mu))),(-1,CF))
            ck(not slack or vint(slack)[0]>0)
save('EXACT_RESULTS.json',{'status':'PASS','mux_cases':pairs,'mux_references':refs,'activation_review_cases':acts,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start,'arithmetic':'Fraction/FWHT/prime-log vectors/outward rational intervals','peak_memory':'not instrumented; estimate 100 MB','max_truth_table_dimension':5})
