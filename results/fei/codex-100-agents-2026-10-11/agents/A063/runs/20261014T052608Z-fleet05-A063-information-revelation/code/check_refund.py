import json,time,math
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
RUN=Path(__file__).resolve().parents[1]
NLOG=64; PREC=384; checks=0
def ck(v):
    global checks
    checks+=1
    assert v
def outward(a):
    den=1<<PREC
    lo=(a[0].numerator*den)//a[0].denominator
    hi=-((-a[1].numerator*den)//a[1].denominator)
    return F(lo,den),F(hi,den)
def plus(a,b):return outward((a[0]+b[0],a[1]+b[1]))
def neg(a):return -a[1],-a[0]
def scale(a,c):return outward((a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c))
def series(z):
    total=F(0); power=z
    for j in range(NLOG):
        total+=power/F(2*j+1);power*=z*z
    err=2*power/F(2*NLOG+1)/(1-z*z)
    return 2*total,2*total+err
LN2=series(F(1,3))
ck(LN2[0]>F(2,3))
@lru_cache(maxsize=8192)
def log2(x):
    assert x>0
    if x<1:return neg(log2(1/x))
    e=x.numerator.bit_length()-x.denominator.bit_length()
    v=x/F(1<<e) if e>=0 else x*F(1<<(-e))
    if v<1:e-=1;v*=2
    if v>=2:e+=1;v/=2
    assert 1<=v<2
    if v==1:return F(e),F(e)
    l=series((v-1)/(v+1))
    return outward((F(e)+l[0]/LN2[1],F(e)+l[1]/LN2[0]))
def entropy(probs):
    out=(F(0),F(0))
    for p in probs:
        if p:out=plus(out,scale(log2(p),-p))
    return out
def raw_information(joint):
    """Raw table mass q times conditional information, no floating cancellation."""
    q=sum(sum(row) for row in joint)
    if not q:return F(0),F(0)
    rows=[sum(row) for row in joint]
    cols=[sum(row[j] for row in joint) for j in range(len(joint[0]))]
    out=(F(0),F(0))
    for i,row in enumerate(joint):
        for j,p in enumerate(row):
            if p:out=plus(out,scale(log2(p*q/(rows[i]*cols[j])),p))
    return out
def coefficients(k,r):
    delta=F(1,1<<k);p=F(1,1<<r);s=F(1,1<<(k//2));B=p*delta
    np=((1<<k)+(1<<(k//2)))//2;nm=((1<<k)-(1<<(k//2)))//2
    classes=[]
    for name,c,count in [('empty',s,1),('plus',s,np-1),('minus',-s,nm)]:
        for U,umult in [(0,1),(1,(1<<(r-1))-1)]:
            if not umult:continue
            C=p*(c-(name=='empty')-delta)
            exceptional=(name=='empty' and U==0)
            mat=[[C+int(exceptional),C],[B,B]]
            classes.append({'name':name,'U_nonempty':U,'mult':count*umult,'mat':mat,'central':exceptional})
    ck(sum(c['mult'] for c in classes)==1<<(k+r-1))
    ck(sum(c['mult']*sum(a*a for row in c['mat'] for a in row) for c in classes)==1)
    return classes
def table(mat,first):
    # Rows are spectral second bit, columns are physical first-query sign (+,-).
    if first=='z':mat=[list(row) for row in zip(*mat)]
    return [[(mat[0][j]+mat[1][j])**2/2,(mat[0][j]-mat[1][j])**2/2] for j in (0,1)]
def full_joint(mat,first):
    # Independent construction of the full 4x4 root-spectrum/outcome coupling.
    if first=='z':mat=[list(row) for row in zip(*mat)]
    out=[]
    for u in (0,1):
        for v in (0,1):
            row=[];qv=mat[0][v]**2+mat[1][v]**2
            for sigma in (1,-1):
                cv=[mat[0][j]+sigma*mat[1][j] for j in (0,1)]
                qs=sum(a*a for a in cv)
                kp=cv[v]**2/(2*qv) if qv else F(0)
                for tau in (1,-1):
                    kn=(cv[0]+tau*cv[1])**2/(2*qs) if qs else F(0)
                    row.append(mat[u][v]**2*kp*kn)
            out.append(row)
    ck(sum(sum(row) for row in out)==sum(a*a for row in mat for a in row))
    for outcome in range(4):
        sigma=1 if outcome//2==0 else -1;tau=1 if outcome%2==0 else -1
        expected=(mat[0][0]+tau*mat[0][1]+sigma*mat[1][0]+sigma*tau*mat[1][1])**2/4
        ck(sum(row[outcome] for row in out)==expected)
    return out
def exact_ci_zero(joint):
    q=sum(sum(row) for row in joint);rs=[sum(row) for row in joint];cs=[sum(row[j] for row in joint) for j in (0,1)]
    return all(joint[i][j]*q==rs[i]*cs[j] for i in (0,1) for j in (0,1))
def primitive(mat,first):
    tab=table(mat,first);q=sum(sum(row) for row in tab)
    weights=[sum(row) for row in tab];rho=[row[0]/w if w else F(0) for row,w in zip(tab,weights)]
    t=sum(row[0] for row in tab)/q
    varraw=sum(w*(a-t)**2 for w,a in zip(weights,rho))
    return q,t,varraw,tab
def block_metrics(classes):
    B=J=H=terminal=(F(0),F(0))
    childmasses=[F(0)]*4
    for cl in classes:
        m=cl['mult'];a=cl['mat'];q=sum(v*v for row in a for v in row)
        atoms=[v*v for row in a for v in row]
        physical=[]
        for si in (1,-1):
            for sj in (1,-1):
                c=a[0][0]+sj*a[0][1]+si*a[1][0]+si*sj*a[1][1]
                physical.append(c*c/4)
        H=plus(H,scale(entropy(atoms),m))
        B=plus(B,scale(plus(entropy(atoms),neg(entropy([q]))),m))
        j=(F(0),F(0));ht=(F(0),F(0))
        for idx,t in enumerate(physical):
            childmasses[idx]+=m*4*t
            if t:
                j=plus(j,scale(log2(4*t/q),t))
                ht=plus(ht,scale(log2(4*t),-t))
        J=plus(J,scale(j,m));terminal=plus(terminal,scale(ht,m))
    ck(childmasses==[F(1)]*4)
    err=plus(plus(H,neg(terminal)),neg(plus(B,J)))
    ck(err[0]<=0<=err[1])
    return B,J,H,terminal
def enc(interval):return [str(x) for x in interval]
def approx(interval):
    # Decimal display only, never a sign decision or certificate.
    return float((interval[0]+interval[1])/2)
def direct_walsh():
    k=4;r=8;n=k+r+1;N=1<<n
    vals=[]
    for x in range(N):
        data=x&15;controls=(x>>k)&255;y=(x>>(k+r))&1
        b=-1 if ((data&1)*((data>>1)&1)+((data>>2)&1)*((data>>3)&1))%2 else 1
        vals.append(1 if controls else b-2*int(y and data==0))
    ck(set(vals)<={-1,1})
    raw=vals[:];step=1
    while step<N:
        for base in range(0,N,2*step):
            for j in range(base,base+step):
                u=raw[j];v=raw[j+step];raw[j]=u+v;raw[j+step]=u-v
        step*=2
    p=F(1,256);s=F(1,4);delta=F(1,16);hist={}
    for w in range(1<<(k+r-1)):
        T=w&15;U=w>>k;orig=T+(U<<(k+1))
        c=(-1 if ((T&1)*((T>>1)&1)+((T>>2)&1)*((T>>3)&1))%2 else 1)*s
        C=p*(c-int(T==0)-delta)
        expect=[[C+int(w==0),C],[p*delta,p*delta]]
        for u in (0,1):
            for v in (0,1):ck(F(raw[orig+(v<<k)+(u<<(k+r))],N)==expect[u][v])
    for coord,expected in [(k+r,p*delta),(k,p*(1-s+delta))]:
        disagreement=sum(vals[x]!=vals[x^(1<<coord)] for x in range(N))
        ck(F(disagreement,N)==expected)
    return {'dimension':n,'truth_table_entries':N,'checked_root_coefficients':N,'selector_influence':str(p*delta),'control_influence':str(p*(1-s+delta))}
def main():
    begin=time.perf_counter();rows=[]
    for k in range(4,41,2):
        if time.perf_counter()-begin>50:raise RuntimeError('Frozen pilot timeout; do not escalate or extend silently')
        r=2*k;d=F(1,1<<(3*k));classes=coefficients(k,r)
        central=next(c for c in classes if c['central'])
        B,J,H,terminal=block_metrics(classes)
        metrics={}
        for first in ('y','z'):
            R=(F(0),F(0));noncentral=0
            for cl in classes:
                a=cl['mat'];q,t,vr,tab=primitive(a,first)
                full=full_joint(a,first)
                refund=raw_information(tab)
                fullinfo=raw_information(full)
                difference=plus(refund,neg(fullinfo));ck(difference[0]<=0<=difference[1])
                if not cl['central']:
                    ck(exact_ci_zero(tab));ck(refund==(F(0),F(0)));noncentral+=cl['mult']
                else:
                    ck(F(1,4)<=t<=F(3,4));ck(vr<=2*d*d)
                    ck(refund[0]>=0);ck(refund[1]<=16*d*d)
                    ck(not exact_ci_zero(tab))
                R=plus(R,scale(refund,cl['mult']))
            metrics[first]={'R_interval':enc(R),'display_R_over_d2':approx(scale(R,1/(d*d))),
                'noncentral_zero_refund_masks':noncentral,'strict_positive_by_nonindependence':True}
        ceiling=scale(plus(B,neg(J)),F(1,2))
        if k>=6:
            ck(ceiling[0]>=F(15,32)*d)
            ck(16*d*d<F(15,32)*d)
        rows.append({'k':k,'r':r,'d':str(d),'orders':metrics,'block_MU_ceiling_interval':enc(ceiling),
            'display_MU_ceiling_over_d':approx(scale(ceiling,1/d)),
            'terminal_entropy_interval':enc(terminal),'display_terminal_entropy':approx(terminal)})
        if k==4:
            # Save the first completed exact instance immediately.
            (RUN/'out'/'FIRST_RESULT.json').write_text(json.dumps(rows[-1],indent=2)+'\n',encoding='utf-8')
    direct=direct_walsh()
    out={'status':'PASS','exact_assertions':checks,'parameter_values':len(rows),'two_query_orders':2*len(rows),
      'runtime_seconds':time.perf_counter()-begin,'log_method':'64 rational atanh terms; dyadic reduction; explicit positive tail, outward interval division; all combined interval endpoints rounded outward to denominator 2^384',
      'direct_actual_Boolean_verification':direct,'rows':rows}
    (RUN/'out'/'CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
