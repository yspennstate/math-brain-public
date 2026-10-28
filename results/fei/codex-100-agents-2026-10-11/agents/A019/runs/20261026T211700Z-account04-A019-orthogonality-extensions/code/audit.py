import json,time
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
R=Path(__file__).resolve().parents[1];num=0
def ck(b):
    global num
    num+=1
    assert b,num
def spec(t):
    a=list(t);s=1
    while s<len(a):
        for x in range(0,len(a),2*s):
            for j in range(s):v,w=a[x+j],a[x+j+s];a[x+j]=v+w;a[x+j+s]=v-w
        s*=2
    return [Q(x*x,len(a)**2) for x in a]
def ev(i):return (-1 if i&7==0 else 1)*(-1 if i&25==0 else 1)
def project(p,keep):
    out=[Q(0)]*(1<<len(keep))
    for i,v in enumerate(p):out[sum(((i>>a)&1)<<j for j,a in enumerate(keep))]+=v
    return out
def restrict(t,ass):
    free=[i for i,a in enumerate(ass) if a==-1];base=sum(a<<i for i,a in enumerate(ass) if a!=-1)
    return [t[base+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))],free
def main():
    start=time.perf_counter();orig=[ev(i) for i in range(32)];op=spec(orig)
    rows=json.loads((R/'out/BLOCK_CERTIFICATES.json').read_text(encoding='utf-8'))
    for row in rows:
        tr,free=restrict(orig,row['assignment']);essential=[j for j in range(len(free)) if any(tr[x]!=tr[x^(1<<j)] for x in range(len(tr)))]
        keep=[free[j] for j in essential];t=[tr[sum(((x>>j)&1)<<i for j,i in enumerate(essential))] for x in range(1<<len(essential))]
        p=spec(t);q=project(op,keep)
        ck(keep==row['keep']);ck(t==row['truth']);ck(list(map(str,p))==row['P']);ck(list(map(str,q))==row['R'])
        influence=sum(Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(essential)))
        ck(str(influence)==row['I']);D=len(t)**2;left=2**int(4*influence*D);right=1
        for a,b in zip(p,q):
            if a:left*=b.numerator**int(a*D);right*=b.denominator**int(a*D)
        ck(str(left)==row['left']);ck(str(right)==row['right']);ck(left>=right)
    fixtures=0
    for k in (1,2):
        rho=Q(1,2**k);mu=Q(5,8);p0=rho*(1-mu)/2
        # Original ordering: q,u,padding,5 source coordinates.
        n=k+7
        def core(i):
            event=((i>>2)&(2**k-1))==0 and ev(i>>(k+2))==-1
            return 1-2*(i&1) if event else 1-2*((i>>1)&1)
        parent=[core(i) for i in range(1<<n)];q0=[x/2 for x in spec(parent)];q0[1]+=Q(1,2)
        for sa in [(-1,)*5,(0,1,-1,-1,-1),(1,-1,-1,-1,-1),(0,0,0,-1,-1)]:
            source,sfree=restrict(orig,sa);ess=[j for j in range(len(sfree)) if any(source[x]!=source[x^(1<<j)] for x in range(len(source)))]
            keep_source=[sfree[j] for j in ess];ss=[source[sum(((x>>j)&1)<<i for j,i in enumerate(ess))] for x in range(1<<len(ess))];rr=project(op,keep_source)
            for pa in [(-1,)*k,(0,)*k,(1,)+(-1,)*(k-1)]:
                kp=pa.count(-1);r=Q(1,2**kp);keep=[1]+[2+j for j,a in enumerate(pa) if a==-1]+[k+2+j for j in keep_source]
                inherited=project(q0,keep);formula=[Q(0)]*len(inherited);formula[1]=(1-2*p0)/2;formula[0]+=Q(1,2)
                for s in range(len(rr)):
                    for uv in range(2**(kp+1)):formula[uv+(s<<(kp+1))]+=rho*r*(rr[s]+(1-2*mu if not s else 0))/8
                ck(inherited==formula)
                for qb in (0,1):
                    ass=[qb,-1]+list(pa)+list(sa)
                    # Clean irrelevant source bits by fixing to0, which keeps function identical.
                    for j in sfree:
                        if j not in keep_source:ass[k+2+j]=0
                    restricted,_=restrict(parent,ass);actual=spec(restricted);nu=Q(sum(ss),len(ss));active=1 not in pa;a=r*(1-nu)/2 if active else Q(0)
                    pp=spec(ss);derived=[Q(0)]*len(actual);derived[1]=1-2*a
                    if active:
                        for s in range(len(pp)):
                            for uv in range(2**(kp+1)):derived[uv+(s<<(kp+1))]+=r*r*(pp[s]+(1-2*nu if not s else 0))/4
                    ck(actual==derived);fixtures+=1
    result={'status':'PASS','block_certificates':len(rows),'projection_fixtures':fixtures,'exact_checks':num,'seconds':time.perf_counter()-start,'independence':'Butterfly Walsh and separate original-parent construction, no import of stage.py'}
    ck(result['seconds']<60);(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
