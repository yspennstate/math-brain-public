from arithmetic import *
import arithmetic as ar

def fmt(v):return [str(x) for x in v]
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def same(a,b):overlap(a,b)
def bern(t):return add(entterm(t),entterm(1-t))
def phi(t):return entterm(t)
def Fmix(m,alpha):
    beta=1-alpha
    return add(scale(log(1/beta),1-m),scale(log(m/(alpha+beta*m)),m))
def core(r):
    return tuple((1-2*((x>>1)&1))*(1-2*((x>>2)==0 or ((x&1) and (x>>2)==3))) for x in range(2**(r+2)))
def G(v,eps):return tuple(eps if not(x&1) else v[x>>1] for x in range(2*len(v)))
def priority(v):return tuple((1-2*((x>>1)&1)) if not(x&1) else v[x>>3] if (x>>2)&1 else 1 for x in range(8*len(v)))
def reference(v,alpha):
    p=law(v)
    if sum(x>0 for x in p)==1:return p
    return tuple(p[0] if t==0 else (1-alpha)*p[t]+alpha*(1-p[0])*(t==len(p)-1) for t in range(len(p)))
def lifted(g,v,alpha,shift):
    p=law(g);pv=law(v);q=reference(v,alpha)
    out=tuple(x if not(t>>shift) else x*q[t>>shift]/pv[t>>shift] if pv[t>>shift] else F(0) for t,x in enumerate(p))
    ck(sum(out)==1 and all((x>0)==(y>0) for x,y in zip(p,out)))
    return out
def branch(g,q,j):
    ps=law(g);children=[restrict(g,j,y) for y in (0,1)];pc=[law(x) for x in children];pb=[];qb=[]
    for t in range(len(pc[0])):
        lo=t%(1<<j)+(t>>j)*(1<<(j+1));hi=lo+(1<<j)
        pb.append(ps[lo]+ps[hi]);qb.append(q[lo]+q[hi])
    qs=[];zs=[]
    for y in (0,1):
        raw=[qq*(pp/(2*p) if p else F(1,2)) for p,qq,pp in zip(pb,qb,pc[y])]
        z=sum(raw);ck(z>0);qs.append(tuple(t/z for t in raw));zs.append(z)
    ck(sum(zs)==1)
    return children,qs,zs,tuple(pb),tuple(qb)

alpha=F(1,6);kappa=scale(log(F(400,399)),F(1,2));cc=sub((F(18),)*2,scale(log(F(10)),5))
ck(400**300>2*399**300);ck(kappa[0]>F(1,600))

def grouped(r):
    d=F(1,2**r);m=d*d;n=2**(r-1)
    hv=add(add(phi((1-3*d)**2),scale(phi(9*m),n-1)),scale(phi(m),3*n))
    h0=add(phi((1-2*d)**2),scale(phi(4*m),2**r-1))
    h1=add(phi((1-4*d)**2),scale(phi(16*m),n-1))
    he=add(add(phi(1-6*d+10*m),scale(phi(10*m),n-1)),scale(phi(2*m),n))
    js=scale(sub(he,scale(add(h0,h1),F(1,2))),F(1,2))
    erasure_entropy=scale(sub(hv,he),F(1,2))
    posterior_mi=sub(bern(d/2),erasure_entropy)
    gamma=scale(sub(bern(3*d/2),scale(add(bern(d),bern(2*d)),F(1,2))),r)
    tc=sub(add(bern(d/2),scale(bern(3*d/2),r)),scale(hv,F(1,2)))
    E=scale(sub(Fmix(m,alpha),Fmix(10*m,alpha)),F(1,2))
    correction=scale(sub(add(Fmix(4*m,alpha),Fmix(16*m,alpha)),scale(Fmix(10*m,alpha),2)),F(1,4))
    sigma=add(kappa,correction)
    ck(E[0]>0 and js[0]>0 and posterior_mi[0]>0 and gamma[0]>0 and tc[0]>0) if r<=32 else None
    ck(sigma[0]>F(1,600))
    Hj=add((F(2),)*2,scale(hv,F(1,2)))
    IF=F(3,2)+(3*r+1)*d/4;HF=add((F(3),)*2,scale(hv,F(1,4)))
    A0=scale(Fmix(m,F(1,8)),F(1,4));M0=sub((4*IF,)*2,add(HF,A0))
    sig1=scale(sub(Fmix(m,alpha),Fmix(m,F(1,8))),F(1,4));sig2=scale(sigma,F(1,2))
    S=sub((2+3*r*d,)*2,scale(add(h0,h1),F(1,8)))
    root_after=sub(M0,add(sig1,sig2));lower=min(S[0],root_after[0])-F(1,4)
    if r>=8:ck(lower>=F(13,8));ck(hv[1]<F(1,2) and max(h0[1],h1[1])<F(1,2))
    return {'r':r,'H_v':fmt(hv),'H_children':[fmt(h0),fmt(h1)],'erased_H':fmt(he),'spectral_JS':fmt(js),'posterior_MI':fmt(posterior_mi),'Gamma':fmt(gamma),'total_correlation':fmt(tc),'conditional_erasure_KL':fmt(E),'outcome_KL':fmt(kappa),'sigma_local':fmt(sigma),'sigma_over_Inf_G_lower':str(sigma[0]/(d/2)),'Inf_G_j':str(d/2),'H_G':fmt(Hj),'I_G':str(1+(3*r+1)*d/2),'root_original_margin':fmt(M0),'sigma1_global':fmt(sig1),'sigma2_global':fmt(sig2),'complete_terminal_S':fmt(S),'remaining_after_old_quarter_lower':str(lower)}

def physical(r,epsilon):
    v=core(r);d=F(1,2**r);m=d*d;p=law(v);ck(p[0]==0 and p[-1]==m);ck(infl(v,0)==d);ck(influence(v)==1+(3*r+1)*d)
    f=priority(v);q0=lifted(f,v,F(1,8),3);A0=kl(law(f),q0);M0=sub((4*influence(f),)*2,add(entropy(law(f)),A0))
    bg,bq,bz,_,_=branch(f,q0,2);ck(bz==[F(1,2),F(1,2)])
    ag,aq,az,_,_=branch(bg[1],bq[1],1);ck(az==[F(1,2),F(1,2)])
    sigma1=Z;sigma2=Z;terms=[(F(1,2),bg[0],bq[0])];localrec=[]
    for e in (0,1):
        g=ag[e];ck(g==G(v,1-2*e));R=lifted(g,v,alpha,1)
        first=sub(kl(law(g),R),kl(law(g),aq[e]));sigma1=add(sigma1,scale(first,F(1,4)))
        kids,old,z,pbar,qbar=branch(g,R,1);ck(z==[F(19,40),F(21,40)])
        K=Z;fresh=Z;ls=[]
        for y in (0,1):
            vv=restrict(v,0,y);ck(kids[y]==G(vv,1-2*e));N=lifted(kids[y],vv,alpha,1)
            ck(law(vv)[-1]==(4 if y==0 else 16)*m)
            kk=kl(law(kids[y]),old[y]);nn=kl(law(kids[y]),N)
            K=add(K,scale(kk,F(1,2)));fresh=add(fresh,scale(nn,F(1,2)))
            terms.append((F(1,8),kids[y],N));ls.append({'truth':kids[y],'P':[str(x) for x in law(kids[y])],'old_Q':[str(x) for x in old[y]],'new_Q':[str(x) for x in N]})
        sig=sub(fresh,K);sigma2=add(sigma2,scale(sig,F(1,4)));ck(sig[0]>F(1,600))
        same(sig,add(kappa,scale(sub(add(Fmix(4*m,alpha),Fmix(16*m,alpha)),scale(Fmix(10*m,alpha),2)),F(1,4))))
        erasedD=kl(pbar,qbar);same(erasedD,scale(Fmix(10*m,alpha),F(1,2)))
        E=sub(kl(law(g),R),erasedD);same(E,scale(sub(Fmix(m,alpha),Fmix(10*m,alpha)),F(1,2)))
        same(erasedD,add(kappa,K));ck(E[0]>0)
        localrec.append({'epsilon':1-2*e,'reference_outcomes':[str(x) for x in z],'sigma':fmt(sig),'conditional_erasure_KL':fmt(E),'outcome_KL':fmt(kappa),'parent_truth':g,'parent_P':[str(x) for x in law(g)],'parent_Q':[str(x) for x in R],'children':ls})
    hf=Z;iff=F(0);terminal=[]
    for w,g,q in terms:
        hf=add(hf,scale(entropy(law(g)),w));iff+=w*influence(g)
        terminal.append({'reach':str(w),'truth':g,'P':[str(x) for x in law(g)],'Q':[str(x) for x in q]})
    S=sub((4*iff,)*2,hf);margin=min(S[0],sub(M0,add(sigma1,sigma2))[0])-F(1,4)
    model=grouped(r);same(M0,tuple(F(x) for x in model['root_original_margin']));same(sigma1,tuple(F(x) for x in model['sigma1_global']));same(sigma2,tuple(F(x) for x in model['sigma2_global']));same(S,tuple(F(x) for x in model['complete_terminal_S']))
    ck(margin>F(13,8))
    return {'r':r,'label_epsilon':epsilon,'sigma1':fmt(sigma1),'sigma2':fmt(sigma2),'original_margin':fmt(M0),'complete_terminal_S':fmt(S),'remaining_after_old_quarter_lower':str(margin),'local_records':localrec,'full_terminals':terminal}

pilot='--pilot' in sys.argv
rs=[3] if pilot else list(range(3,17))+[24,32,64,128]
physical_cases=[physical(3,1)] if pilot else [physical(r,1) for r in (3,4,5,6)]
groups=[grouped(r) for r in rs]
result={'status':'PASS','checks':ar.checks,'runtime_seconds':time.perf_counter()-start,'physical_policies':physical_cases,'grouped':groups,'epsilon_labels':'Each complete root policy ALREADY retains both epsilon outcomes; duplicate outer labels removed before main.','formal_verification':'not attempted'}
dest=ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json');dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'status':'PASS','checks':ar.checks,'runtime_seconds':result['runtime_seconds'],'physical_policies':len(physical_cases),'grouped_cases':len(groups)}))
