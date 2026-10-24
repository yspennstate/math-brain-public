from exact import *
import exact, itertools
START=time.perf_counter()
pilot='--pilot' in sys.argv
RUN=Path(__file__).resolve().parents[1]
def clock(): ck(time.perf_counter()-START<55)
def canonical(v,k,r,z):
    """Fresh explicit source law; no inherited reference is an argument."""
    n=1<<r; s=F(1,1<<k); mu=1-2*s; e=F(1,n)
    g=tuple(-1 if y&((1<<k)-1)==0 else 1 for y in range(n))
    pg=spec(g); V=tuple(mu*mu if t==0 else (1-mu*mu)/(n-1) for t in range(n))
    R=tuple((1-z)*a+z*b for a,b in zip(pg,V))
    Rp=tuple((1-e/s)*a+(e/s)*mu*(t==0)+2*e/n for t,a in enumerate(R))
    p=spec(v); q=tuple(sum(p[8*t:8*t+8]) for t in range(n))
    ck(sum(pg)==sum(V)==sum(R)==sum(Rp)==sum(q)==1)
    ck(min(q)>0 and min(Rp)>0)
    if z==0:ck(Rp==q)
    Q=tuple(Rp[j>>3]*a/q[j>>3] for j,a in enumerate(p))
    ck(sum(Q)==1 and all(b>0 for a,b in zip(p,Q) if a))
    ck(all(sum(Q[8*t:8*t+8])==Rp[t] for t in range(n)))
    return Q,pg,V
def offref(pg,V,a):return tuple(((1-a)*pg[j>>3]+a*V[j>>3]) if j%8==0 else F(0) for j in range(8*len(pg)))
def positive(v):return not v or bounds(v)[0]>0
b,c,f=root_table(); p=spec(f); vv=[restrict(f,6,t) for t in (0,1)]
pon,poff=map(spec,vv); eroot=B(p,6); old=mix(marginal(p,6))
oldbill=add((1,eroot),(F(1,2),CE(pon,old)),(F(1,2),CE(poff,old)))
Q0,pg,V=canonical(vv[0],3,5,F(0));ck(Q0==pon)
grid=[F(0),F(1)] if pilot else [F(0),F(1,4),F(1,2),F(3,4),F(1)]
source=[]; rows=[]; repaired=[]
for lam in grid:
    q,_,_=canonical(vv[0],3,5,lam)
    ck(sum(1 for a,z in zip(old,q) if a and not z)==96)
    solo=add((1,const(3)),(-1,eroot),(F(-1,2),CE(pon,q)),(F(-1,2),CE(poff,old)))
    ck(bounds(solo)[0]>F(201237,10**6))
    for alpha in [F(0),F(3,4),F(1)]:
        off=offref(pg,V,alpha)
        bill=add((1,eroot),(F(1,2),CE(pon,q)),(F(1,2),CE(poff,off)))
        margin=add((1,const(3)),(-1,bill))
        reconstructed=add((1,oldbill),(F(1,2),add((1,CE(pon,q)),(-1,CE(pon,old)))),(F(1,2),add((1,CE(poff,off)),(-1,CE(poff,old)))))
        ck(reconstructed==bill)
        if alpha<=F(3,4):ck(bounds(margin)[0]>F(42173,10**6))
        if lam==alpha==1:ck(bounds(margin)[1]<-F(153188,10**6))
        source.append({'lambda':str(lam),'alpha':str(alpha),'same_margin':rec(margin)})
    clock()

# Start from the worst admitted source corner, not a renewed source bank.
qin,_,_=canonical(vv[0],3,5,F(1));qoff=offref(pg,V,F(3,4))
incoming=add((1,eroot),(F(1,2),CE(pon,qin)),(F(1,2),CE(poff,qoff)))
incomingmargin=add((1,const(3)),(-1,incoming))
for j in ([3] if pilot else [3,4,5]):
    actual=[restrict(vv[0],j,t) for t in (0,1)]
    pp=list(map(spec,actual)); r=marginal(qin,j); m=marginal(pon,j)
    ck(len(set(actual[0]))==2 and len(set(actual[1]))==1)
    ck(all((pp[0][t]+pp[1][t])/2==m[t] for t in range(len(m))))
    refund=add((1,KL(pon,qin)),(-1,KL(m,r)));ck(positive(refund))
    newB=B(pon,j)
    pre=add((1,eroot),(F(1,2),newB),(F(1,4),CE(pp[0],r)),(F(1,4),CE(pp[1],r)),(F(1,2),CE(poff,qoff)))
    ck(pre==add((1,incoming),(F(-1,2),refund)))
    for beta in grid:
        new,_,_=canonical(actual[0],2,4,beta)
        constant=tuple(F(t==0) for t in range(len(r)))
        ck(spec(actual[1])==constant)
        Eon=add((1,CE(pp[0],new)),(-1,CE(pp[0],r)))
        Eoff=add((1,CE(pp[1],constant)),(-1,CE(pp[1],r)))
        updated=add((1,pre),(F(1,4),Eon),(F(1,4),Eoff))
        direct=add((1,eroot),(F(1,2),newB),(F(1,4),CE(pp[0],new)),(F(1,2),CE(poff,qoff)))
        ck(updated==direct)
        margin=add((1,const(3)),(-1,updated))
        ck(margin==add((1,incomingmargin),(F(1,2),refund),(F(-1,4),Eon),(F(-1,4),Eoff)))
        ck(positive(margin))
        # Compare against the first-root escrow, preserving both old resets.
        T0=add((F(1,2),H(spec(b))),(F(1,2),H(spec(c))))
        rootdebit=add((1,H(p)),(-1,T0)); S4=add((1,const(3)),(-1,T0))
        ck(margin==add((1,S4),(-1,rootdebit),(-1,add((1,incoming),(-1,H(p)))),(F(1,2),refund),(F(-1,4),Eon),(F(-1,4),Eoff)))
        rows.append({'physical_on_child_query':j,'beta':str(beta),'incoming_margin':rec(incomingmargin),'conditional_KL_refund_local':rec(refund),'fresh_nonconstant_reset_local':rec(Eon),'constant_child_reset_local':rec(Eoff),'complete_original_quota_margin':rec(margin),'full_new_liability':rec(updated),'old_sibling_CE':rec(CE(poff,qoff)),'on_terminal_CE':rec(CE(pp[0],new))})
        # Spend the newly released global capacity on the retained original
        # sibling, whose alpha=1 reference failed at the earlier frontier.
        farnew=offref(pg,V,F(1))
        farprice=add((1,CE(poff,farnew)),(-1,CE(poff,qoff)))
        repaired_bill=add((1,updated),(F(1,2),farprice))
        repaired_margin=add((1,const(3)),(-1,repaired_bill))
        ck(positive(repaired_margin))
        ck(repaired_margin==add((1,incomingmargin),(F(1,2),refund),(F(-1,4),Eon),(F(-1,4),Eoff),(F(-1,2),farprice)))
        ck(repaired_bill==add((1,eroot),(F(1,2),newB),(F(1,4),CE(pp[0],new)),(F(1,2),CE(poff,farnew))))
        repaired.append({'physical_on_child_query':j,'beta':str(beta),'alpha_new':'1','far_sibling_extra_signed_cost_local':rec(farprice),'same_original_margin':rec(repaired_margin),'same_original_full_bill':rec(repaired_bill)})
    clock()

# Boundary assumptions: all omitted fixed hypotheses have explicit guards.
for n in range(0,3):
    for mask in range(1<<(1<<n)):
        v=tuple(1 if mask>>t&1 else -1 for t in range(1<<n)); pv=spec(v); rv=mix(pv)
        for j in range(n): node(v,rv,j)
ck(sum(F(1,2)*a for a in [F(1,2),F(1,2)])==F(1,2))
out={'status':'PASS','pilot':pilot,'assertions':exact.COUNT,'seconds':time.perf_counter()-START,'source_cases':len(source),'active_query_reset_cases':len(rows),'repaired_endpoint_cases':len(repaired),'source':source,'rows':rows,'repaired_endpoint':repaired,'scope':'same original quota3, worst admitted incoming source corner, one active query then prescribed canonical profile reset plus maximal-spread retained-sibling reset, arbitrary later no-reset continuation by analytic telescope'}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'assertions':out['assertions'],'seconds':out['seconds'],'source_cases':len(source),'active_query_reset_cases':len(rows),'worst_new_margin_display_only':min(x['complete_original_quota_margin']['display_only'] for x in rows),'repaired_endpoint_margin_display_only':min(x['same_original_margin']['display_only'] for x in repaired)}))
