from pathlib import Path
from fractions import Fraction as F
import importlib.util,hashlib,json,time,sys
R=Path(__file__).resolve().parents[1]
PREV=R.parents[0]/'20261021T180853Z-fleet03-A095-restricted-result-extraction/code/check.py'
spec=importlib.util.spec_from_file_location('own_stage16',PREV);A=importlib.util.module_from_spec(spec);spec.loader.exec_module(A)
def add(*zs):return tuple(sum(z[i] for z in zs) for i in (0,1))
def sc(z,c):return(z[0]*c,z[1]*c) if c>=0 else(z[1]*c,z[0]*c)
def sub(z,t):return add(z,sc(t,-1))
def rnd(z):
    d=2**80
    return[str(F((z[0]*d).__floor__(),d)),str(F((z[1]*d).__ceil__(),d))]
def grouped_cost(rows):return add(*(sc(A.log2(1/q),count*p) for count,p,q in rows if count and p))
def grouped_div(rows):return add(*(sc(A.log2(p/q),count*p) for count,p,q in rows if count and p))
def case(m):
    delta=F(1,2**(m+6));W=2*delta-64*delta**2;e=2*delta;Wc=2*e-16*e*e
    N=2**(m+6);new=N-32
    rootrows=[(count,(a-delta)**2,(1-W)*a*a) for a,count in [(F(7,16),1),(-F(7,16),3),(-F(1,16),15),(F(1,16),45)]]
    # New parent masks contribute zero KL but their actual mass is retained.
    A.ck(sum(n*p for n,p,q in rootrows)+W==1);A.ck(sum(n*q for n,p,q in rootrows)+W==1)
    dr=grouped_div(rootrows)
    classes=[]
    for c,n in [(F(7,8),1),(-F(1,8),15)]:
        classes.append((n,(c+e)**2,(1-W)*c*c,F(3,4)*(1-Wc)*c*c+delta/4,'support',c))
        raw=(1-W)*4*c*c*delta*delta/(c*c+4*delta*delta)
        classes.append((n,e*e,raw,F(3,4)*e*e+delta/4,'old_zero',c))
    classes.append((new,e*e,e*e,F(3,4)*e*e+delta/4,'new',F(0)))
    Z=sum(n*raw for n,p,raw,f,kind,c in classes)
    A.ck(Z>0);A.ck(sum(n*p for n,p,raw,f,kind,c in classes)==1);A.ck(sum(n*f for n,p,raw,f,kind,c in classes)==1)
    oldrows=[(n,p,raw/Z) for n,p,raw,f,k,c in classes];freshrows=[(n,p,f) for n,p,raw,f,k,c in classes]
    A.ck(sum(n*q for n,p,q in oldrows)==1)
    co=grouped_cost(oldrows);cf=grouped_cost(freshrows);ex=sc(sub(cf,co),F(1,2));df=grouped_div(freshrows);do=grouped_div(oldrows)
    if m>=8:
        A.ck(ex[0]>F(1,10));A.ck(dr[1]<delta)
        A.ck(df[0]>F(4041,16384));A.ck(F(31*(m+1),2**(m+6))<F(1,10))
    # Direct literal Boolean cube and references only on frozen small domain.
    if m in (0,1,2):
        _,_,_,v,Q,_=A.root(4,m);vs,qs=A.transport(v,Q,4);p0=[x*x for x in A.walsh(vs[0])]
        for s,p in enumerate(p0):
            if s<32:
                c=F(7,8) if (s%16)==0 else -F(1,8)
                if s>=16:raw=(1-W)*c*c;target=(c+e)**2
                else:raw=(1-W)*4*c*c*delta*delta/(c*c+4*delta*delta);target=e*e
            else:raw=e*e;target=e*e
            A.ck(p==target);A.ck(qs[0][s]==raw/Z)
        direct=A.ce(p0,qs[0]);A.ck(max(direct[0],co[0])<=min(direct[1],co[1]))
        # Independent physical original source influence and character coefficients.
        g=[(1-2*((x%16)==0))*(1-2*((x>>4)==0)) for x in range(64)]
        A.ck(A.influence(g)==F(3,2))
        for s,a in enumerate(A.walsh(g)):A.ck(a==F(sum(z*(-1 if (s&x).bit_count()%2 else 1) for x,z in enumerate(g)),64))
    return{'m':m,'delta':str(delta),'e1':rnd(ex),'Droot':rnd(dr),'Dfresh':rnd(df),'Dinherited':rnd(do),'normalizer':str(Z),'Ustar':str(min(F(15,2),31*(m+1)*delta)),'old_cost':rnd(co),'fresh_cost':rnd(cf),'compressed_states':len(classes),'actual_child_states':str(N)}
def witness():
    # Independent direct-character transform, not A094's witness implementation.
    def law(v):return[F(sum(z*(-1 if(s&x).bit_count()%2 else 1) for x,z in enumerate(v)),len(v))**2 for s in range(len(v))]
    def model(t):
        g=[-(1-2*(x==0)) for x in range(2**t)];v=g+g;v[2**t]*=-1
        e=F(1,2**t);p=law(g);W=2*e-len(p)*e*e
        q=[(1-W)*p[s] if s<len(p) else e*e for s in range(len(v))]
        A.ck(sum(q)==1);return v,q
    v,q=model(4);vs,qs=A.transport(v,q,0);vnew,qnew=model(3);A.ck(vs[0]==vnew);p=law(vnew)
    A.ck(p==[F(49,64)]+[F(1,64)]*15)
    A.ck(qs[0]==[F(18375,33856)]+[F(1695,33856)]*7+[F(113,8464)]*8)
    A.ck(qnew==[F(63,128)]+[F(7,128)]*7+[F(1,64)]*8)
    N=12250**49*3390**7*452**8;D=11109**49*3703**7*529**8
    A.ck(N>16*D);A.ck(N*N<512*D*D)
    return{'status':'INTEGER_CERTIFICATE_PASS','N':str(N),'D':str(D),'bounds':'1/128<e3<9/1024','reference_ratios':['12250/11109','3390/3703','452/529']}
def main():
    start=time.perf_counter();pilot='pilot'in sys.argv;ms=[0,8]if pilot else[0,1,2,8,9,16,32,64]
    rows=[case(m) for m in ms];cert=witness()
    for m in range(8,129):
        A.ck(F(31*(m+1),2**(m+6))<=F(279,16384));A.ck(F(19200,31)*F(1,2**(m+6))<1)
    out={'status':'PASS','assertions':A.NCHK,'cases':len(ms),'direct_replays':sum(m in(0,1,2)for m in ms),'seconds':time.perf_counter()-start,'rows':rows,'witness':cert,'helper_sha256':hashlib.sha256(PREV.read_bytes()).hexdigest()}
    (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json'if pilot else'EXACT_RESULTS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items()if k not in['rows','witness']}))
if __name__=='__main__':main()
