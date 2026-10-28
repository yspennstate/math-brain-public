from pathlib import Path
from fractions import Fraction as Q
import sys,itertools,json,time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
OLD=R.parents[1]/'runs/20261014T094139Z-account05-A091-composition-referee/code'
sys.path.insert(0,str(OLD))
import check as a
import exact as e
START=time.perf_counter(); mode=sys.argv[1]; count=0; rows=[]
def watchdog():
    assert time.perf_counter()-START<55,'frozen runtime exceeded'
def H(t):return e.entropy(a.squares(t))
def mean(t):return sum(t,Q(0))/len(t)
def var(t):return 1-mean(t)**2
def wrap(K,C,g):return tuple(K[z]+C[z]*g[w] for w in range(len(g)) for z in range(len(C)))
def bent(m):return tuple((-1)**sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,m,2)) for z in range(1<<m))
def characters(t):
    return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def serialize(d):return {str(p):str(v) for p,v in d.items()}
if mode in ('pilot','transfer'):
    configs=list(itertools.product((0,1,-1),repeat=4))
    if mode=='pilot':configs=configs[:3]
    for cfg in configs:
        C=tuple(int(x==0) for x in cfg);K=cfg;c=mean(C);KC=a.coeff(K);CC=a.coeff(C)
        for mask in range(16):
            g=e.tab(mask,2);F=wrap(K,C,g);gc=a.coeff(g);mu=gc[0]
            for i in range(2):
                Bg,Dg,t=a.local(g,i);BF,DF,d=a.local(F,2+i);beta=gc[1<<i]
                S=e.add(*[(1,a.phi((k+mu*v)**2,beta*beta*v*v)) for k,v in zip(KC,CC)])
                identity=e.add((c,Bg),(-c,a.phi(mu*mu,beta*beta)),(1,S))
                e.check(BF,identity);e.check(d,c*t)
                e.check(abs(beta)<=t,True)
                # Strict analytic A<7 is proved separately; finite certificate uses its rational upper bound7.
                tax=e.add((c*beta*beta,e.logform(1/c))) if c else {}
                e.nonnegative(e.add((c,Bg),(1,tax),(1,a.const(7*d)),(-1,DF)))
                count+=1
            watchdog()
elif mode=='trees':
    for mask in range(256):
        root=e.tab(mask,3);released=Q(0);front=[(Q(1),root)]
        for depth in range(3):
            nxt=[]
            for weight,g in front:
                mu=mean(g);beta=a.coeff(g)[1];kids=[a.cut(g,0,b) for b in (0,1)]
                e.check(mean(kids[0]),mu+beta);e.check(mean(kids[1]),mu-beta)
                e.check(var(g)-(var(kids[0])+var(kids[1]))/2,beta*beta)
                released+=weight*beta*beta
                nxt.extend((weight/2,k) for k in kids);count+=1
            front=nxt
            e.check(released+sum(w*var(k) for w,k in front),var(root))
        rows.append({'mask':mask,'initial_singleton_energy':str(sum(x*x for i,x in enumerate(a.coeff(root)) if i and i.bit_count()==1)),'released':str(released)})
        watchdog()
elif mode=='sharp':
    gs=[e.tab(mask,2) for mask in range(16)]+[tuple(-1 if x==7 else 1 for x in range(8)),tuple((-1)**x.bit_count() for x in range(8))]
    for m in (4,6):
        b=bent(m);c=Q(1,1<<m);s=Q(1,1<<(m//2));C=(1,)+(0,)*((1<<m)-1);K=tuple(v-u for v,u in zip(b,C))
        for idx,g in enumerate(gs):
            mu=mean(g);F=wrap(K,C,g);fc=a.coeff(F);gc=a.coeff(g)
            for i in range((len(g)-1).bit_length()):
                B,D,d=a.local(F,m+i);Bg,_,t=a.local(g,i);beta=gc[1<<i]
                S=e.add(*[(1,a.phi((bb+(mu-1)*c)**2,beta*beta*c*c)) for bb in a.coeff(b)])
                e.check(B,e.add((c,Bg),(-c,a.phi(mu*mu,beta*beta)),(1,S)))
                e.nonnegative(e.add((1,S),(-1,a.const(c*beta*beta*(m-2)))))
                e.check(d,c*t)
            # Retain both actual exterior terminal profiles on complete internal query tree.
            term=e.add(((1+mu)/2,H(b)),((1-mu)/2,H(tuple(v-2*u for v,u in zip(b,C)))))
            total=e.add((1,H(F)),(-1,term))
            bills=[];release=Q(0);front=[(Q(1),g)]
            while len(front[0][1])>1:
                nxt=[]
                for weight,h in front:
                    _,nodeD,_=a.local(wrap(K,C,h),m)
                    bills.append((weight,nodeD));release+=weight*a.coeff(h)[1]**2
                    nxt.extend((weight/2,a.cut(h,0,v)) for v in (0,1))
                front=nxt
            e.check(e.add(*bills),total);e.check(release,var(g))
            source=tuple(g[w] if x==0 else F[w*(1<<m)+z] for w in range(len(g)) for z in range(1<<m) for x in (0,1))
            BX,DX,dX=a.local(source,0)
            e.check(dX,(1-c-mu*(s-c))/2)
            ticket=c*m*var(g)/2
            e.nonnegative(e.add((1,a.const(6*dX-ticket-dX/3)),(-1,DX)))
            rows.append({'m':m,'g_index':idx,'mu':str(mu),'variance':str(var(g)),'full_terminal_debit':serialize(total),'source_d':str(dX),'root_weighted_density_ticket':str(ticket)})
            count+=1;watchdog()
elif mode=='obstruction':
    for m in (4,6,8):
        b=bent(m);c=Q(1,1<<m);s=Q(1,1<<(m//2))
        W=tuple(1 if x==0 else b[z] for z in range(1<<m) for x in (0,1))
        fw=characters(W);e.check(fw,a.coeff(W))
        expected=((1+s)/2,(1-s)/2)+tuple(s*((-1)**sum(((j>>k)&1)*((j>>(k+1))&1) for k in range(0,m,2)))/2 for j in range(1,1<<m) for _ in range(2))
        e.check(sorted(x*x for x in fw),sorted(x*x for x in expected))
        _,DX,dX=a.local(W,0);e.check(dX,(1-s)/2)
        _,Db,db=a.local(b,0);e.check(Db,a.const(2));e.check(db,Q(1,2))
        _,_,root_exterior_influence=a.local(W,1)
        e.check(root_exterior_influence,Q(1,4));e.check(4*root_exterior_influence,Q(1))
        # Full terminals: X=0 leaves constant1; X=1 then z0 leaves two bent restrictions.
        terminal=e.add(*[(Q(1,4),H(a.cut(b,0,v))) for v in (0,1)])
        debit=e.add((1,H(W)),(-1,terminal));e.check(debit,e.add((1,DX),(1,a.const(1))))
        delta=e.add((1,debit),(-1,a.const(6*dX)))
        e.nonnegative(e.add((1,delta),(-1,a.const(Q(31,16)*s))))
        if m==4:
            explicit=e.add((1,a.const(Q(11,4))),(-Q(25,64),e.logform(Q(25))),(-Q(9,64),e.logform(Q(9))))
            e.check(delta,explicit)
            e.nonnegative(e.add((1,delta),(-1,a.const(Q(49,100)))))
            e.nonnegative(e.add((1,debit),(-1,a.const(Q(73,10)*dX))))
        lo,hi=e.interval(delta)
        rows.append({'m':m,'dX':str(dX),'actual_old_source_debit':serialize(DX),'all_terminals':serialize(terminal),'source6_deficit_interval':[str(lo),str(hi)]})
        count+=1;watchdog()
else:raise ValueError(mode)
out={'status':'PASS','mode':mode,'cases':count,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-START,'rows':rows,'formal_status':'NOT_FORMALIZED; exact rational certificates and analytic proof only'}
(R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
