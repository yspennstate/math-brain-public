"""v1.1: exact small fixtures plus all-real power-inequality certificate."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v1',R/'code/continuation_v1.py')
V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
P=V.prior;E=V.E;checks=0;start=time.perf_counter()
def ck(x):
    global checks
    checks+=1
    if not x:raise AssertionError(checks)
    if time.perf_counter()-start>60:raise TimeoutError('frozen 60 seconds')
def save(name,x):(R/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def main():
    t=tuple((-1)**(x>>1&1) if not x&1 else 2*(x>>3&1)-1 if x>>2&1 else 1 for x in range(16))
    p=P.spectral(t);ck(p==V.spectral_direct(t));ck(V.influence(t)==F(3,2))
    ck(sum(p[1:])==F(15,16));ck(p[0]==F(1,16));ck(E.entropy_vector(p)=={2:F(3)})
    inf=[sum(a for s,a in enumerate(p) if s>>i&1) for i in range(4)]
    ck(inf==[F(1,2),F(1,2),F(1,4),F(1,4)])
    ck(16**8<2*15**8);ck(5**3<2**7);ck(30<2*17);ck(60**2<2*47**2)
    upper=-F(11,4)+F(15,128)+F(4,3)+F(7,6)+F(7,8)+F(11,16)
    ck(upper==F(183,128));ck(3-1-upper==F(73,128))
    rows=[]
    for c in [F(3,4),F(25,32),F(13,16)]:
        q=V.exact_reference(c);ck(sum(q)==1)
        D=V.kliv(p,[(a,a) for a in q]);ck(D[1]<upper)
        for mode in ['fair','0','1']:
            row,data=P.query(t,2,4,q,mode)
            pcs=data[3];J=data[5];qb=[sum(v) for v in J]
            refs=[[a/qb[b] for a in J[b]] for b in (0,1)]
            tb=P.child(t,2,1);row2,data2=P.query(tb,2,3,refs[1],mode)
            pc2=data2[3];K2=data2[4];J2=data2[5];qby=[sum(a) for a in J2]
            refs2=[[a/qby[b] for a in J2[b]] for b in (0,1)]
            ck(all(a==F(1,4) for a in data2[1]))
            ck(pc2[0]==pc2[1]==(F(1,4),)*4)
            ck(all(a==F(1,2) for rowk in K2 for a in rowk));ck(not row2['outcome_KL'])
            erq=P.marg(refs[1],lambda s:P.erase(s,2))
            ck(refs2[0]==refs2[1]==[erq[z] for z in range(4)])
            D0=P.kl(pcs[0],refs[0]);D1=P.kl(pcs[1],refs[1]);DL=P.kl(pc2[0],refs2[0])
            Y=E.add(D1,E.mul(DL,F(-1)))
            if mode=='fair':
                C=E.mul(P.vec_log(1/(1-4*c/15)),F(1,2))
                ck(Y==C);ck(P.conditional(pcs[0],refs[0],4)==C)
                Q0=E.add(D0,E.mul(C,F(-1)));Q1=E.add(D1,E.mul(C,F(-1)))
                ck(E.mul(E.add(D0,D1),F(1,2))==E.add(C,E.mul(E.add(Q0,Q1),F(1,2))))
            for leaf in [P.child(t,2,0),P.child(tb,2,0),P.child(tb,2,1)]:
                ck(P.spectral(leaf)==V.spectral_direct(leaf));ck(E.entropy_vector(P.spectral(leaf))=={2:F(2)});ck(V.influence(leaf)==1)
            ck(F(1,2)*V.influence(P.child(t,2,0))+F(1,4)*V.influence(P.child(tb,2,0))+F(1,4)*V.influence(P.child(tb,2,1))==1)
            rows.append({'c':str(c),'fallback':mode,'Droot_interval':E.outward(D),'initial_outcome_KL':row['outcome_KL'],'mean_b_child_KL':row['child_KL'],'y_erasure_KL':P.serial(Y),'y_terminal_KL':P.serial(DL)})
    result={'status':'PASS','version':'1.1','rational_histories':9,'all_real_parameter_domain':'3/4 <= c <= 13/16; analytic logarithmic bound, not sampling','assertions':checks,'helper_assertions':P.CHECKS,'interval_helper_assertions':V.checks,'seconds':time.perf_counter()-start,'Droot_strict_upper':'183/128','same_owner_initial':3,'old_booking':'C=-(1/2)log2(1-4c/15); partitioned C/2+C/2, never added twice','new_energy_debit':1,'remaining_strict_lower':'73/128','histories':rows}
    save('RESULT.json',result);print(json.dumps({k:v for k,v in result.items() if k!='histories'}))
if __name__=='__main__':main()
