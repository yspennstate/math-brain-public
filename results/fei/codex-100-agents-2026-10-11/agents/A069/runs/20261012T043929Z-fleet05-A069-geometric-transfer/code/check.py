from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time,hashlib

RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parent/'20261011T224507Z-fleet05-A069-geometric-transfer'
t0=time.monotonic()
assertions=0
def ck(q):
    global assertions
    assert q
    assertions+=1
def guard():
    if time.monotonic()-t0>55:
        raise RuntimeError('frozen 55-second guard')
def fwht(values):
    v=values[:]
    step=1
    while step<len(v):
        for start in range(0,len(v),step*2):
            for k in range(step):
                u,w=v[start+k],v[start+k+step]
                v[start+k],v[start+k+step]=u+w,u-w
        step*=2
    return v
def binary(coords):
    if len(coords)==1:return coords[0]
    half=len(coords)//2
    return binary(coords[:half]),binary(coords[half:])
def ternary(start,d):
    if d==0:return start
    q=3**(d-1)
    return tuple(ternary(start+j*q,d-1) for j in range(3))
def cell(t):
    return 1<<t if isinstance(t,int) else sum(cell(c) for c in t)
def nodes(t):
    return [] if isinstance(t,int) else [(cell(t),len(t))]+[w for c in t for w in nodes(c)]
def lengths(t,N):
    ns=nodes(t)
    return [1+sum(b for c,b in ns if c&s) for s in range(1<<N)]
def word(t,s):
    if not s:return '0'
    result='1';todo=[t]
    while todo:
        v=todo.pop()
        if isinstance(v,int):continue
        mask=sum(1<<j for j,c in enumerate(v) if cell(c)&s)
        result+=format(mask-1,'0%db'%len(v))
        todo.extend(reversed([c for j,c in enumerate(v) if mask>>j&1]))
    return result
def decode(t,w):
    if w=='0':return 0
    ck(w[0]=='1')
    todo=[t];at=1;s=0
    while todo:
        v=todo.pop()
        if isinstance(v,int):s|=1<<v;continue
        b=len(v);mask=int(w[at:at+b],2)+1;at+=b
        ck(mask<1<<b)
        todo.extend(reversed([c for j,c in enumerate(v) if mask>>j&1]))
    ck(at==len(w))
    return s
def decoder_check(t,N,L):
    words=[word(t,s) for s in range(1<<N)]
    for s,w in enumerate(words):
        ck(len(w)==L[s]);ck(decode(t,w)==s)
    sw=sorted(words)
    ck(all(not y.startswith(x) for x,y in zip(sw,sw[1:])))
    ck(sum((F(1,1<<len(w)) for w in words),F())<=1)
def gamma(a,L):return F(sum(x*x*l for x,l in zip(a,L)),len(a)**2)
def spectral_I(a):return F(sum(s.bit_count()*x*x for s,x in enumerate(a)),len(a)**2)
def physical_Inf(table,i):return F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table))
def physical_I(table,N):return sum((physical_Inf(table,i) for i in range(N)),F())
def maj(t,x):
    if isinstance(t,int):return 1 if not (x>>t&1) else -1
    return 1 if sum(maj(c,x) for c in t)>0 else -1
def R(k):
    return F() if k==1 else 1-F(1,1<<k)+R(k//2)+R(k-k//2)

def base_majority():
    old=json.loads((OLD/'out/validation.json').read_text())
    ck(old['result']=='PASS')
    reused=[row for row in old['rows'] if row['depth']==2 and row['N'] in (9,10)]
    ck(len(reused)==2)
    ck(reused[0]['point_edits']==512 and reused[0]['L_base']=='17/2')
    ck(reused[1]['L_base']=='21/2')
    receipt={'source':str(OLD/'out/validation.json'),'sha256':hashlib.sha256((OLD/'out/validation.json').read_bytes()).hexdigest(),'reused':reused,'review':'A070 REPORT 20261011T230551Z accepts A069 v1 without repair'}
    (RUN/'out/REUSED_CERTIFICATES.json').write_text(json.dumps(receipt,indent=2)+'\n')
    rows=[]
    for N in [11,12]:
        guard();main=ternary(0,2);tree=(main,binary(list(range(9,N))))
        table=[maj(main,x) for x in range(1<<N)];a=fwht(table);L=lengths(tree,N)
        ck(gamma(a,L)==F(21,2));ck(spectral_I(a)==F(9,4));ck(physical_I(table,N)==F(9,4))
        rows.append({'N':N,'Gamma':'21/2','I':'9/4','method':'direct full truth-table integer FWHT and physical edges'})
    return rows

def addressing():
    rows=[];cases=0
    for a,domain in [(1,range(3,8)),(2,range(6,9)),(3,range(11,13))]:
        n=a+(1<<a)
        for N in domain:
            guard();size=1<<N
            tree=(binary(list(range(a))),binary(list(range(a,n))))
            if N>n:tree=(tree,binary(list(range(n,N))))
            L=lengths(tree,N);decoder_check(tree,N,L);ck(max(L)==2*N-1)
            table=[-1 if (x>>(a+(x&((1<<a)-1))))&1 else 1 for x in range(size)]
            coeff=fwht(table)
            Ig=1+F(a,2);expected=3+2*a+2*R(a)+(2 if N>n else 0)
            ck(gamma(coeff,L)==expected);ck(expected<=8*Ig-5)
            ck(spectral_I(coeff)==Ig);ck(physical_I(table,N)==Ig)
            for i in range(N):
                ck(physical_Inf(table,i)==(F(1,2) if i<a else F(1,1<<a) if i<n else F()))
            for s,c in enumerate(coeff):
                selector=s&((1<<a)-1);data=(s>>a)&((1<<(1<<a))-1);padding=s>>n
                if data.bit_count()==1 and padding==0:
                    j=data.bit_length()-1
                    ck(c==size//(1<<a)*(-1 if (selector&j).bit_count()%2 else 1))
                else:ck(c==0)
            edit_vertices=range(size) if a<=2 else list(range(8))+list(range(size-8,size))
            for x0 in edit_vertices:
                guard();f=table[:];f[x0]*=-1;z=fwht(f)
                for s,c in enumerate(z):ck(c==coeff[s]-2*table[x0]*(-1 if (s&x0).bit_count()%2 else 1))
                If=spectral_I(z);Lf=gamma(z,L)
                ck(If==physical_I(f,N));ck(abs(If-Ig)<=F(2*N,size))
                ck(Lf<=2*expected+F(8*(2*N-1),size));ck(Lf<=25*If)
                if N>=6:ck(Lf<=16*If)
                cases+=1
            rows.append({'a':a,'N':N,'Gamma_base':str(expected),'I_base':str(Ig),'point_edits':len(edit_vertices)})
    ck(cases==728)
    return rows,cases

def subcubes():
    N=3;size=8;cases=0
    for truthmask in range(256):
        guard();g=[-1 if truthmask>>x&1 else 1 for x in range(size)];ga=fwht(g)
        for r in [1,2]:
            for Z in combinations(range(N),r):
                Y=[i for i in range(N) if i not in Z]
                tz,ty=binary(list(Z)),binary(Y);tree=(tz,ty);L=lengths(tree,N)
                ys=nodes(ty);W=[sum(b for c,b in ys if s&c) for s in range(size)]
                Wg=F(sum(c*c*W[s] for s,c in enumerate(ga)),size*size)
                Uz=sum((b*(1-F(1,1<<c.bit_count())) for c,b in nodes(tz)),F())
                rho=F(1,1<<r);h_list=[];avg=F()
                for zstar in range(1<<r):
                    h=[];D=[]
                    for y in range(1<<len(Y)):
                        x=sum(((zstar>>j)&1)<<i for j,i in enumerate(Z))+sum(((y>>j)&1)<<i for j,i in enumerate(Y))
                        D.append(x);h.append(g[x])
                    ha=fwht(h);wy=lengths(ty,N) # global masks; evaluate by reinserting Y bits
                    Wh=F(sum(c*c*W[sum(((v>>j)&1)<<i for j,i in enumerate(Y))] for v,c in enumerate(ha)),len(h)**2)
                    avg+=rho*Wh;h_list.append((zstar,h,ha,D,Wh))
                ck(avg==Wg)
                for zstar,h,ha,D,Wh in h_list:
                    f=g[:]
                    for x in D:f[x]*=-1
                    fa=fwht(f);da=[u-v for u,v in zip(fa,ga)]
                    E=F(sum(c*c*L[s] for s,c in enumerate(da)),size*size)
                    mh=F(ha[0],len(h));expected=4*rho*(1+2*(1-rho*mh*mh)+Uz+Wh)
                    ck(E==expected);ck(E<=4*Wg+4*rho*(2*r+1));ck(rho*Wh<=Wg)
                    ck(gamma(fa,L)<=2*gamma(ga,L)+2*E)
                    for s,c in enumerate(da):
                        u=sum(((s>>i)&1)<<j for j,i in enumerate(Z));v=sum(((s>>i)&1)<<j for j,i in enumerate(Y))
                        ck(F(c,size)==-2*rho*(-1 if (u&zstar).bit_count()%2 else 1)*F(ha[v],len(h)))
                    for i in Y:ck(physical_Inf(f,i)==physical_Inf(g,i))
                    for i in Z:ck(physical_Inf(f,i)+physical_Inf(g,i)>=2*rho)
                    cases+=1
    ck(cases==4608)
    return cases

def main():
    (RUN/'out').mkdir(exist_ok=True)
    mr=base_majority();ar,ac=addressing();sc=subcubes();guard()
    result={'helper_version':'A069-stage2-exact-v1','result':'PASS','target_cases':ac+sc+2,'addressing_edit_cases':ac,'subcube_edit_cases':sc,'majority_new_bases':2,'assertions':assertions,'seconds':time.monotonic()-t0,'addressing':ar,'majority':mr,'entropy_signs':'analytic Kraft/Parseval proofs; no floating-point entropy assertions'}
    (RUN/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
