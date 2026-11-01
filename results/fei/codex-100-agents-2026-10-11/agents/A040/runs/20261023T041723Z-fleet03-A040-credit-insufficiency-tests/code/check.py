from arithmetic import *
import arithmetic as ar

def fmt(interval): return [str(x) for x in interval]

def point(w):
    return tuple(-1 if x == (1 << w)-1 else 1 for x in range(1 << w))

def tensor(tables):
    out=(1,)
    for tab in tables:
        out=tuple(a*b for b in tab for a in out)
    return out

def ref(v,beta):
    p=law(v); n=len(v).bit_length()-1
    if n<2 or p[0]==1: return p
    return tuple(p[0] if t==0 else beta*p[t]+(1-beta)*(1-p[0])*(t==len(p)-1) for t in range(len(p)))

def tensorlaw(laws):
    out=(F(1),)
    for q in laws: out=tuple(a*b for b in q for a in out)
    return out

def ratio(q,p): return tuple(y/x if x else F(1) for x,y in zip(p,q))

def gate(v,u,epsilon):
    return tuple(epsilon if not (x&1) else v[(x>>1)&(len(v)-1)]*u[x//(2*len(v))] for x in range(2*len(v)*len(u)))

def lift(g,tables,betas):
    p=law(g); core=tensorlaw([law(v) for v in tables]); q=tensorlaw([ref(v,b) for v,b in zip(tables,betas)])
    ell=ratio(q,core)
    return tuple(x*ell[t>>1] for t,x in enumerate(p))

def children(g,Q,i):
    p=law(g); gs=[restrict(g,i,y) for y in (0,1)]; ps=[law(v) for v in gs]
    out=[[],[]]
    for t in range(len(gs[0])):
        lo=(t&((1<<i)-1))|((t>>i)<<(i+1)); hi=lo|(1<<i)
        pp=p[lo]+p[hi]; qq=Q[lo]+Q[hi]
        k=ps[0][t]/(2*pp) if pp else F(1,2)
        out[0].append(qq*k);out[1].append(qq*(1-k))
    zz=[sum(q) for q in out]
    ck(sum(zz)==1 and min(zz)>0)
    return gs,[tuple(x/z for x in q) for q,z in zip(out,zz)],zz

def local(w,ws,epsilon,sign):
    v=tuple(sign*x for x in point(w));u=tensor([point(k) for k in ws]); pu=law(u)
    qu=tensorlaw([ref(point(k),F(5,6)) for k in ws]); su=ratio(qu,pu)
    pv=law(v);lv=ratio(ref(v,F(5,6)),pv);g=gate(v,u,epsilon);p=law(g)
    B=tuple(x*lv[(t>>1)&(len(v)-1)] for t,x in enumerate(p))
    C=tuple(x*su[t//(2*len(v))] for t,x in enumerate(p))
    R=tuple(x*su[t//(2*len(v))] for t,x in enumerate(B))
    count=0; nonfair=0; failed_auxiliary=[]
    def walk(v,B,C,R,path):
        nonlocal count,nonfair
        count+=1;g=gate(v,u,epsilon);p=law(g);nn=len(v).bit_length()-1
        ck(sum(B)==sum(C)==sum(R)==1)
        ck(all(not x or min(b,c,r)>0 for x,b,c,r in zip(p,B,C,R)))
        ss=tuple(su[t//(2*len(v))] for t in range(len(p)))
        ck(R==tuple(b*s for b,s in zip(B,ss)))
        ck(C==tuple(x*s for x,s in zip(p,ss)))
        # B need not have P's spectator marginal. Only its nonempty sector
        # must remain proportional to p_u; R=B*s then normalizes exactly.
        masses=[sum(B[t] for t in range(len(B)) if t//(2*len(v))==u0) for u0 in range(len(pu))]
        total=sum(masses[1:]); variance=1-pu[0]
        for u0 in range(1,len(pu)):
            ck(masses[u0]*variance==total*pu[u0])
        for value in set(ss):
            pp=sum(x for x,s in zip(p,ss) if s==value);bb=sum(x for x,s in zip(B,ss) if s==value)
            if pp!=bb and not failed_auxiliary:
                failed_auxiliary.append({'path':path,'spectator_likelihood':str(value),'physical_group_mass':str(pp),'B_group_mass':str(bb)})
        N=lift(g,[v]+[point(k) for k in ws],[F(4,5)]+[F(5,6)]*len(ws))
        ck(sum(N)==1)
        if nn==0:return
        for j in range(nn):
            gv,BB,zb=children(g,B,1+j);_,CC,zc=children(g,C,1+j);_,RR,zr=children(g,R,1+j)
            ck(zb==zr);ck(zc==[F(1,2),F(1,2)])
            nonfair+=zb[0]!=F(1,2)
            vv=[restrict(v,j,y) for y in (0,1)]
            ck((sum(1-law(vv[y])[0] for y in (0,1))/2)<=1-law(v)[0])
            for y in (0,1):
                ck(gv[y]==gate(vv[y],u,epsilon))
                walk(vv[y],BB[y],CC[y],RR[y],path+[(j,y)])
    walk(v,B,C,R,[])
    return {'w':w,'spectators':ws,'epsilon':epsilon,'core_sign':sign,'nodes':count,'nonfair_reference_query_pairs':nonfair,'counterexample_to_discarded_auxiliary_marginal_equality':failed_auxiliary}

def priority(tables):
    h=tensor(tables)
    return tuple((1 if not(x>>1&1) else -1) if not(x&1) else h[x>>3] if (x>>2&1) else 1 for x in range(8*len(h)))

def initial(g,tables):
    p=law(g);pp=tensorlaw([law(v) for v in tables]);qq=tensorlaw([ref(v,F(7,8)) for v in tables]);ell=ratio(qq,pp)
    return tuple(x*ell[t>>3] for t,x in enumerate(p))

def rootpolicy(m,r,prefix,policy):
    tabs=[point(r)]*m;g0=priority(tabs);P0=law(g0);Q0=initial(g0,tabs)
    ck(sum(Q0)==1);A0=kl(P0,Q0);M0=sub((4*influence(g0),)*2,add(entropy(P0),A0))
    ck(M0[0]>1)
    gg,QQ,_=children(g0,Q0,2)
    terms=[(F(1,2),gg[0],QQ[0])];active=[(F(1,2),gg[1],QQ[1],tabs)]
    if prefix:
        active=[];gs,qs,_=children(gg[1],QQ[1],2)
        for y in (0,1):active.append((F(1,4),gs[y],qs[y],[restrict(tabs[0],0,y)]+tabs[1:]))
    sigma1=Z;sigma2=Z;positive1=0;positive2=0;full=[]
    for reach,g,q,ts in active:
        gs,qs,_=children(g,q,1)
        for epsidx in (0,1):
            gg=gs[epsidx];old=qs[epsidx];R=lift(gg,ts,[F(5,6)]*len(ts));ck(sum(R)==1)
            sig=sub(kl(law(gg),R),kl(law(gg),old));sigma1=add(sigma1,scale(sig,reach/2));positive1+=sig[0]>0
            if len(ts[0])<4 or law(ts[0])[0]==1:
                terms.append((reach/2,gg,R));continue
            def finish(weight,g,q,ts,depth):
                nonlocal sigma2,positive2
                stop=policy=='none' or len(ts[0])==1 or (policy=='one' and depth==1)
                if stop:
                    new=lift(g,ts,[F(4,5)]+[F(5,6)]*(len(ts)-1));ck(sum(new)==1)
                    sig=sub(kl(law(g),new),kl(law(g),q));sigma2=add(sigma2,scale(sig,weight));positive2+=sig[0]>0
                    terms.append((weight,g,new));return
                gs,qs,_=children(g,q,1)
                for y in (0,1):
                    childts=[restrict(ts[0],0,y)]+ts[1:]
                    if policy=='stop0' and y==0:
                        new=lift(gs[y],childts,[F(4,5)]+[F(5,6)]*(len(ts)-1));ck(sum(new)==1)
                        sig=sub(kl(law(gs[y]),new),kl(law(gs[y]),qs[y]));sigma2=add(sigma2,scale(sig,weight/2));positive2+=sig[0]>0
                        terms.append((weight/2,gs[y],new))
                    else:finish(weight/2,gs[y],qs[y],childts,depth+1)
            finish(reach/2,gg,R,ts,0)
    ck(sum(t[0] for t in terms)==1)
    Hf=Z;If=F(0);Kf=Z
    for weight,g,q in terms:
        p=law(g);ck(sum(q)==1 and all(not x or y>0 for x,y in zip(p,q)))
        Hf=add(Hf,scale(entropy(p),weight));If+=weight*influence(g);Kf=add(Kf,scale(kl(p,q),weight))
        full.append({'reach':str(weight),'truth':g,'P':[str(x) for x in p],'Q':[str(x) for x in q]})
    S=sub((4*If,)*2,Hf);e=sub(sub(entropy(P0),Hf),(4*(influence(g0)-If),)*2)
    net=add(add(A0,e),add(sigma1,sigma2));margin=sub(S,(max(F(0),net[0]),max(F(0),net[1])))
    margin=sub(margin,(F(1,4),)*2)
    ck(S[0]>=1-F(1,2**110));ck(sub(M0,sigma1)[0]>1);ck(sigma2[1]<F(1,16));ck(margin[0]>F(11,16))
    record={'m':m,'r':r,'prefix':prefix,'policy':policy,'root_margin':fmt(M0),'first_reset':fmt(sigma1),'second_reset':fmt(sigma2),'final_surplus':fmt(S),'remaining_after_old_quarter':fmt(margin),'full_terminal_KL':fmt(Kf),'positive_first_nodes':positive1,'positive_second_nodes':positive2,'terminals':full}
    return record

pilot='--pilot' in sys.argv
cases=[(2,(2,),1,1)] if pilot else [(w,ws,e,s) for w in (2,3) for ws in ((),(2,),(1,),(2,1)) for e in (-1,1) for s in (-1,1)]+[(4,(2,),1,1)]
locals=[local(*case) for case in cases]
roots=[rootpolicy(1,2,False,'none')] if pilot else [rootpolicy(m,r,pre,pol) for m,r in ((1,2),(2,2),(1,3)) for pre in (False,True) for pol in ('none','one','stop0','full')]
ck(5**3<2*4**3);ck(6**40<2**11*5**40);ck(8**5<2*7**5)
if not pilot:ck(sum(x['nodes'] for x in locals)==2105 and len(roots)==24)
out={'status':'PASS','checks':ar.checks,'runtime_seconds':time.perf_counter()-start,'local_cases':locals,'local_nodes':sum(x['nodes'] for x in locals),'root_policies':roots,'positive_second_reset_nodes':sum(x['positive_second_nodes'] for x in roots)}
dest=ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json');dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('local_cases','root_policies')}))
