from pathlib import Path
import importlib.util,json,time,sys,math,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parents[1]/'runs/20261023T063125Z-account03-A018-shared-data-collision-law/code/check_chain.py'
sp=importlib.util.spec_from_file_location('own_arrays',OLD);a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
c=a.c;F,ck,add,sc,lg=c.F,c.ck,c.add,c.sc,c.lg
ONE=lg(F(2))
def scalar(x):return sc(x,ONE)
def pack(x):return {str(p):str(v) for p,v in x.items()}
def positive(x):return c.interval(x)[0]>0
def eta(x):return c.ent((x,))
def f(p):return eta((1-p)**2)
def delta(p):return add(f(p/2),sc(-F(1,2),f(p)),sc(F(1,4),eta(p*p)),scalar(2*p-p*p/2))
def dcore(p):return sc(p*p/2,lg((2+p*p)/(1+p*p)))
def rootrefund(p):return c.refund(p*p/16,(2+p*p)/32)
def omega(p):return add(scalar(3+p/2),sc(-F(1,2),delta(p)),sc(F(1,2),dcore(p)),sc(-1,c.psi(p/4)),rootrefund(p))
def tq_density(p):
    return add(scalar(-1-p),sc(F(1,2),delta(p)),sc(-F(1,2),dcore(p)),c.psi(p/4),sc(-F(1,2),c.psi(p/2)),sc(F(1,2),add(c.refund(F(0),F(1,8)),c.refund(p*p/4,(1+p*p)/8))),sc(-1,rootrefund(p)))
def edges(tt):
    n=len(tt).bit_length()-1
    return F(sum(tt[x]!=tt[x^(1<<i)] for i in range(n) for x in range(len(tt))),len(tt))
def integer_certificate(v):
    den=math.lcm(*(x.denominator for x in v.values()));ps={p:int(x*den) for p,x in v.items()}
    left=math.prod(p**x for p,x in ps.items() if x>0);right=math.prod(p**(-x) for p,x in ps.items() if x<0)
    ck(left>right)
    return {'prime_log':pack(v),'clearing_denominator':den,'exponents':ps,'left_gt_right':True,'left_bits':left.bit_length(),'right_bits':right.bit_length()}
def run(pilot=False):
    start=time.perf_counter();rows=[];domain=diag=0;bydensity={}
    ck(545**8<2*512**8);ck(290**8<2*273**8);ck(2**8<3**9<2**16);ck(63**63>2**376)
    # Exact log certificates for all analytic endpoint constants.
    cert={'profile_chord_A_less1':integer_certificate(add(scalar(2),sc(-F(9,8),lg(F(3))))),'constant_gate_entropy_gt2':integer_certificate(add(ONE,c.psi(F(1,2)),scalar(-2))),'constant_gate_profile_less_5_4':integer_certificate(add(scalar(F(5,4)),sc(-1,c.psi(F(1,2)))))}
    for n in range(1,(2 if pilot else 3)+1):
        N=2**n
        for bits in range(1,2**N):
            p=F(bits.bit_count(),N);in_domain=p<=F(1,4)
            if not in_domain and not(n<=2 and p==F(1,2)):continue
            event=tuple((bits>>j)&1 for j in range(N));z=tuple(1-2*v for v in event);J=edges(z)
            char=tuple(1-2*(j%2) for j in range(2*N));h1=tuple(1 if event[j//2] else char[j] for j in range(2*N))
            au,aa=a.fw(char),a.fw(h1);P=c.probs(aa);Qu=c.refs(c.probs(au))[1];Q1=c.refs(P)[1]
            ck(aa==c.walsh(h1));ck(aa[0]==p and aa[1]==1-p)
            ck(edges(h1)==1-p+J/2)
            ah,Qh=c.lift(au,aa,Qu,Q1);Hp=c.ent(c.probs(ah));H1=c.ent(P);c1=c.ce(P,Q1)
            parent=tuple(v for pair in zip(char,h1) for v in pair);ck(ah==c.walsh(parent))
            ck(Hp==add(sc(F(1,2),H1),delta(p)))
            dc=add(sc(F(1,2),add(c.kl(c.probs(au),Qu),c.kl(P,Q1))),sc(-1,c.kl(c.probs(ah),Qh)))
            ck(dc==dcore(p))
            Cu,_,_=a.activation(au,Qu);CA,_,_=a.activation(aa,Q1);Croot,PF,QF=a.activation(ah,Qh,n<=2)
            ck(Croot==add(scalar(F(5,4)),sc(F(1,4),c1),sc(F(1,2),delta(p)),sc(-F(1,2),dcore(p)),c.psi(p/4),sc(-1,rootrefund(p))))
            full=tuple(v for mask in (-1,1,1,1) for h in parent for v in (1,h*mask))
            IF=edges(full);ck(4*IF==6+J/2-p/2)
            qinf=F(sum(full[x]!=full[x^2] for x in range(len(full))),len(full));ck(qinf==p/4)
            B=add(scalar(F(7,4)-p+J/2),sc(-F(1,4),c1));W=add(scalar(4*IF),sc(-1,Croot))
            ck(add(W,sc(-1,B))==omega(p))
            T=add(Croot,sc(-F(1,2),add(Cu,CA)),scalar(-p));ck(T==tq_density(p))
            if p in bydensity:ck(bydensity[p]==(omega(p),T))
            bydensity[p]=(omega(p),T)
            if in_domain:
                domain+=1;ck(positive(add(scalar(F(85,64)),sc(-1,omega(p)))))
                ck(positive(add(scalar(F(1,4)),sc(-1,T))))
                ck(c.nonneg(delta(p)));ck(c.nonneg(dcore(p)));ck(c.nonneg(rootrefund(p)))
            else:diag+=1
            # After ALL event coordinates, BOTH full references are kept, including the constant leaf.
            qfinal=Q1
            for j in range(n):qfinal=a.fold(qfinal,1)
            ck(qfinal==((1+p)/2,(1-p)/2))
            Cfu,_,_=a.activation((F(0),F(1)),qfinal);Cfc,_,_=a.activation((F(1),F(0)),qfinal)
            leaf=add(sc(1-p,Cfu),sc(p,Cfc));ck(positive(add(scalar(4),sc(-1,leaf))))
            S=sc(F(1,2),add(CA,sc(-1,leaf)))
            ck(c.nonneg(S))
            finish=add(scalar(6-F(3,2)*p),sc(-F(1,2),add(Cu,leaf)),scalar(-F(1,8)))
            ck(finish==add(W,T,S,scalar(-J/2-F(1,8))))
            if in_domain:ck(positive(add(finish,scalar(-2))))
            rows.append({'n':n,'truth_bits':bits,'p':str(p),'domain':in_domain,'J':str(J),'Omega':pack(omega(p)),'Tq':pack(T),'B_minus_all_query_bill':pack(add(B,sc(-1,S))),'complete_influence_retired_terminal_reserve':pack(finish)})
            if time.perf_counter()-start>55:raise RuntimeError('Frozen55s cap')
    if not pilot:ck(domain==40 and diag==8)
    # Tensor proof is symbolic in m and mu; no factorization of exponentially long rational numerators.
    H0=add(scalar(4),sc(-F(9,8),lg(F(3))))
    cert['H0_gt2']=integer_certificate(add(H0,scalar(-2)))
    cert['H0_lt3']=integer_certificate(add(scalar(3),sc(-1,H0)))
    ck(6-F(16384,256*8)==-2);ck(-2+F(85,64)==-F(43,64))
    result={'status':'PASS','pilot':pilot,'domain_events':domain,'diagnostics':diag,'cases':len(rows),'assertions':c.checks,'seconds':time.perf_counter()-start,'details':rows,'tensor_witness':{'k':8,'m':16384,'analytic_B_minus_S_upper':-2,'all_original_root_slack_ledger_upper':'-43/64','not_FEI_counterexample':True}}
    (R/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    (R/'out'/('PILOT_CERTIFICATES.json' if pilot else 'CERTIFICATES.json')).write_text(json.dumps(cert,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='details'}))
if __name__=='__main__':run('--pilot' in sys.argv)
