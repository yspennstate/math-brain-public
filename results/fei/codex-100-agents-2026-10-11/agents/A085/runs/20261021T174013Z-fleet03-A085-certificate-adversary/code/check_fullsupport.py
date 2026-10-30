from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib,argparse
import check_reset as c
R=Path(__file__).resolve().parents[1]

def run(n):
    # j is bit 0; y1 is bit 1. Exactly three negative vertices: 0,1,3.
    v=[-1 if x in [0,1,3] else 1 for x in range(1<<(n+1))]
    P=c.law(v); c.ck(all(P)); q=c.marginal(P,0)
    child=[c.restrict(v,0,b) for b in [0,1]]; Pc=[c.law(w) for w in child]
    c.ck(all(sum(c.influence(w,j) for j in range(n))>0 for w in child))
    for a,b,m in zip(*Pc,q):c.ck(a+b==2*m)
    t=F(1,1<<n);qa=2*t*t;q0=1-6*t+10*t*t;p0=(1-2*t)**2;p=4*t*t;M=1<<(2*n-2)
    c.ck(q[0]==q0 and q[1]==qa and Pc[0][0]==p0 and Pc[0][1]==p)
    c.ck(all(a in [t*t,9*t*t,(1-3*t)**2] for a in P))
    c.ck(p*M==1 and p0<=2*q0 and qa<=F(1,8))
    I=sum(c.influence(v,j) for j in range(n+1))
    c.ck(I==(3*n-1)*t and c.influence(v,0)==t)
    d=qa*(1-F(1,1<<M));newq=list(q);newq[1]-=d;newq[0]+=d
    c.ck(sum(newq)==1 and all(newq))
    c.ck(sum(abs(a-b) for a,b in zip(q,newq))/2==d and 0<d<qa)
    delta=c.diff((c.S,c.S),c.mul(c.exact(p0),c.lg((q0+d)/q0)))
    c.ck(delta[0]>3*c.S//4)
    if n==2:
        c.ck((q0+d)/q0==F(31,16) and 31<32)
    else:c.ck(qa<=F(1,32) and 4*qa<=F(1,8))
    rootCE=c.ce(P,P); old=[c.ce(Pc[b],q) for b in [0,1]]; new=c.ce(Pc[0],newq)
    direct=c.diff(new,old[0]);c.ck(max(delta[0],direct[0])<=min(delta[1],direct[1]))
    c.ck(rootCE[1]<c.exact(8*I)[0])
    # Independent raw atom reset expression; all but two likelihood ratios equal one.
    for k in range(len(q)):
        if k not in [0,1]:c.ck(q[k]==newq[k])
    B=c.diff(c.ce(P,P),c.ce(q,q)); terminal=c.mul(c.exact(F(1,2)),c.add(*old))
    balance=c.diff(rootCE,c.add(B,terminal));c.ck(balance[0]<=0<=balance[1])
    # Matching-root conditional refund exactly zero, not a rounded subtraction.
    for k,m in enumerate(q):
        c.ck(P[2*k]+P[2*k+1]==m and m>0)
    # Actual all-atoms-positive matching root and both full terminal laws retained.
    c.ck(all(newq[k]>0 for k,pv in enumerate(Pc[0]) if pv))
    return {'n':n,'dimension':n+1,'negative_vertices':[0,1,3],'truth_table':v if n==2 else None,'full_root_support':True,'both_children_nonconstant':True,'q0':str(q0),'qa':str(qa),'p0':str(p0),'p':str(p),'M':M,'TV_upper':str(qa),'query_influence':str(t),'total_influence':str(I),'root_entropy_interval':c.serial(rootCE),'expected_reset_interval':c.serial(c.mul(c.exact(F(1,2)),delta)),'active_reset_interval':c.serial(delta),'refund':'exactly zero','reset_changed_atoms':[0,1],'all_other_terminals_unchanged':True,'finite_root_H_le_8I':True}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--pilot',action='store_true');args=a.parse_args()
    start=time.perf_counter();rows=[run(n) for n in ([2,3] if args.pilot else range(2,8))]
    out={'status':'PASS','assertions':c.checks,'runtime_seconds':time.perf_counter()-start,'family':'full-support three-vertex path','cases':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'log_helper_sha256':hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest()}
    (R/'out'/('FULLSUPPORT_PILOT.json' if args.pilot else 'FULLSUPPORT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
