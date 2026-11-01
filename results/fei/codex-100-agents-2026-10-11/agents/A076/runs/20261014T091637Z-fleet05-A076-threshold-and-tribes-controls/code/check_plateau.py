exec(compile((__import__('pathlib').Path(__file__).parent/'arithmetic.py').read_text(),str(__import__('pathlib').Path(__file__).parent/'arithmetic.py'),'exec'))
import sys
pilot='--pilot' in sys.argv
def cn(q):return {} if not q else {F(2):F(q)}
def carrier(s,k):return -1 if sum(((s>>(2*j))&1)*((s>>(2*j+1))&1) for j in range(k//2))%2 else 1
def form(h,v,alive=True):return tuple(h[s]*(v[x] if alive and s==0 else 1) for s in range(len(h)) for x in range(len(v)))
def prof(d,q,mu):
    ep=F(1,1<<d);M=1<<q;b=F(1,1<<(q//2));rho=1-mu;w=M*ep;t=ep*rho/b
    # L evaluated by nonzero old row entropy with the exact scale removed.
    npos=(M+(1<<(q//2)))//2
    row=plus((phi((b-ep*rho)**2),F(npos)),(phi((-b-ep*rho)**2),F(M-npos)))
    mass=1-2*ep*rho+M*ep*ep*rho*rho
    minusL=plus((row,F(1)),(cn(q*mass),F(-1)))
    j=plus((minusL,F(1)),(phi(rho*rho),ep*(1-w)),(phi(mu*mu),-ep))
    r=d*ep*(1-mu*mu);kk=ep*(2*(d-q)*rho+(d-(2*d-q)*w)*rho*rho)
    return r,kk,j
roots=queries=0
h=tuple(carrier(s>>1,4) for s in range(32));ep=F(1,32)
for n in range(3 if pilot else 4):
    for label in range(1<<(1<<n)):
        v=tuple(1-2*((label>>i)&1) for i in range(1<<n));f=form(h,v);mu=F(sum(v),len(v))
        r,kk,j=prof(5,4,mu)
        equal_expr(plus((H(f),F(1)),(H(v),-ep),(cn(4+r+kk),F(-1)),(j,F(-1))))
        eq(I(f),2+5*ep*(1-mu)+ep*I(v));leq(H(f),5*I(f))
        u=plus((cn(6+25*ep*(1-mu)-r-kk),F(1)),(j,F(-1)))
        leq(plus((u,F(-1))),-F(55,32));leq(j,120*ep);leq(plus((j,F(-1))),120*ep)
        for i in range(n):
            vv=[child(v,i,c) for c in [0,1]];ff=[child(f,i,c) for c in [0,1]]
            pcs=[prof(5,4,F(sum(t),len(t))) for t in vv];a=coeff(v)[1<<i];d=inf(v,i)
            release=r-sum(t[0] for t in pcs)/2;kdrop=kk-sum(t[1] for t in pcs)/2
            eq(release,5*ep*a*a);eq(kdrop,-2*ep*a*a)
            dhf=plus((H(f),F(1)),(H(ff[0]),F(-1,2)),(H(ff[1]),F(-1,2)))
            dhv=plus((H(v),F(1)),(H(vv[0]),F(-1,2)),(H(vv[1]),F(-1,2)))
            jd=plus((j,F(1)),(pcs[0][2],F(-1,2)),(pcs[1][2],F(-1,2)))
            equal_expr(plus((dhf,F(1)),(dhv,-ep),(cn(release+kdrop),F(-1)),(jd,F(-1))))
            leq(jd,60*ep*d);leq(plus((jd,F(-1))),60*ep*d)
            leq(plus((dhf,F(1)),(dhv,-ep)),release+60*ep*d)
            eq(inf(f,i),ep*d)
            queries+=1
        roots+=1;coeff.cache_clear()
mixed=None
if not pilot:
    h=tuple(carrier(s,6) for s in range(64));v=tuple([-1]+[1]*15);froot=form(h,v)
    rootmu=F(sum(v),len(v));rroot=6*F(1,64)*(1-rootmu*rootmu)
    leafH={};leafI=F(0);leafR=F(0);inputleaf={};inputcost={};nodecost={};totalrelease=F(0);pp=F(0);ps=F(0);nodes=[];weight=F(1)
    for step,kind in enumerate(['private','private','shared','private']):
        dshared=len(h).bit_length()-1;n=len(v).bit_length()-1;ep=F(1,len(h));mu=F(sum(v),len(v));f=form(h,v);r=dshared*ep*(1-mu*mu)
        quarter=None;admission=None
        if kind=='private':
            vv=[child(v,0,c) for c in [0,1]];hh=[h,h];ff=[child(f,0,c) for c in [0,1]]
            rs=[dshared*ep*(1-F(sum(t),len(t))**2) for t in vv]
            dhv=plus((H(v),F(1)),(H(vv[0]),F(-1,2)),(H(vv[1]),F(-1,2)))
            ic=plus((dhv,ep));queryinf=inf(f,0);pp+=weight*queryinf
            g=form(h,tuple([-1]+[1]*((1<<(n-1))-1)))
            quarter=plus((B(g,0),F(1,4)));admission=plus((B(f,0),F(1)),(quarter,F(-1)))
            leq(plus((admission,F(-1))),F(0));leq(admission,4*inf(f,n-1))
            eq(len(set(g))==2,True);eq(len(set(h))==2,True)
        else:
            hh=[child(h,0,c) for c in [0,1]];vv=[v,v];ff=[child(f,n,c) for c in [0,1]]
            eq(ff[0],form(hh[0],v));eq(ff[1],form(hh[1],v,False))
            rs=[(dshared-1)*2*ep*(1-mu*mu),F(0)];ic={};queryinf=inf(f,n);ps+=weight*queryinf
            # Physical source bank release, not a newly granted descendant reserve.
            eq(r-sum(rs)/2,ep*(1-mu*mu))
            nonzero=[a for a in coeff(hh[0]) if a];eq(len(nonzero),16);eq(set(a*a for a in nonzero),{F(1,16)})
        dhf=plus((H(f),F(1)),(H(ff[0]),F(-1,2)),(H(ff[1]),F(-1,2)))
        release=r-sum(rs)/2;eq(release>=0,True)
        if kind=='private':leq(plus((dhf,F(1)),(ic,F(-1))),60*queryinf+release)
        else:leq(dhf,6*queryinf)
        eq(all(len(set(t))==2 for t in ff),True)
        nodecost=plus((nodecost,F(1)),(dhf,weight));inputcost=plus((inputcost,F(1)),(ic,weight));totalrelease+=weight*release
        leafH=plus((leafH,F(1)),(H(ff[1]),weight/2));leafI+=weight*I(ff[1])/2;leafR+=weight*rs[1]/2
        if kind=='private':inputleaf=plus((inputleaf,F(1)),(H(vv[1]),weight*ep/2))
        nodes.append(dict(step=step,kind=kind,weight=str(weight),actual_query_influence=str(queryinf),incoming_R=str(r),
             R_children=[str(x) for x in rs],weighted_R_release=str(weight*release),full_entropy_bill=[[str(a),str(c)] for a,c in dhf.items()],
             inherited_quarter_core_B=None if quarter is None else [[str(a),str(c)] for a,c in quarter.items()],
             admission_B=None if admission is None else [[str(a),str(c)] for a,c in admission.items()],
             both_children_nonconstant=True))
        h,v=hh[0],vv[0];weight/=2
    f=form(h,v);ep=F(1,len(h));mu=F(sum(v),len(v));r=(len(h).bit_length()-1)*ep*(1-mu*mu)
    leafH=plus((leafH,F(1)),(H(f),weight));leafI+=weight*I(f);leafR+=weight*r;inputleaf=plus((inputleaf,F(1)),(H(v),weight*ep))
    eq(rroot,totalrelease+leafR);equal_expr(plus((H(froot),F(1)),(nodecost,F(-1)),(leafH,F(-1))))
    eq(I(froot),pp+ps+leafI)
    equal_expr(plus((H(tuple([-1]+[1]*15)),F(1,64)),(inputleaf,F(-1)),(inputcost,F(-1))))
    leq(plus((nodecost,F(1)),(inputcost,F(-1))),60*pp+6*ps+totalrelease)
    mixed=dict(status='PASS',history='x1=0,x2=0,s1=0,x3 with all other siblings retained',nodes=nodes,
        original_selector='z unqueried at every node and terminal',R_root=str(rroot),R_released=str(totalrelease),R_terminal=str(leafR),
        P_private=str(pp),P_shared=str(ps),terminal_I=str(leafI),
        terminal_H=[[str(a),str(c)] for a,c in leafH.items()],
        inherited_input_entropy_cost=[[str(a),str(c)] for a,c in inputcost.items()],
        complete_full_entropy_cost=[[str(a),str(c)] for a,c in nodecost.items()])
    (ROOT/'out/MIXED_HISTORY.json').write_text(json.dumps(mixed,indent=2)+'\n')
result=dict(status='PASS',mode='PILOT' if pilot else 'FULL',roots=roots,private_queries=queries,mixed_history_checked=mixed is not None,
    exact_assertions=checks,elapsed_seconds=time.perf_counter()-start)
(ROOT/('out/PLATEAU_PILOT.json' if pilot else 'out/PLATEAU_FULL.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
