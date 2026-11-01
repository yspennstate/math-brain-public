from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json,time,hashlib
import independent_arithmetic as a
ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
@lru_cache(None)
def merge_refund(x,y,z,w):
    q=x*x+y*y+z*z+w*w
    if not q:return Q(0)
    def collision(u,v):return Q(4*u*u*v*v,u*u+v*v) if u or v else Q(0)
    first=collision(x,y)+collision(z,w)-Q(4*(x*y+z*w)**2,q)
    second=collision(x,z)+collision(y,w)-Q(4*(x*z+y*w)**2,q)
    ck(first>=0);ck(second>=0)
    return first+second
def diag_integer(w):
    N=len(w);n=(N-1).bit_length();O=[];R={}
    for i in range(n):
        diff=0
        for s in range(N):
            if not s>>i&1:diff+=max(0,w[s|1<<i]**2-w[s]**2)
        O.append(Q(diff,N*N))
    for i in range(n):
        for j in range(i+1,n):
            mask=(1<<i)|(1<<j);rows=Counter()
            for s in range(N):
                if s&mask==0:rows[w[s],w[s|1<<i],w[s|1<<j],w[s|mask]]+=1
            R[i,j]=sum(mult*merge_refund(*row) for row,mult in rows.items())/(N*N)
    return O,R,sum(O)+sum(R.values())
def direct_diag(t):
    N=len(t);w=[int(N*v) for v in a.direct_coeffs(t)]
    return diag_integer(w)[2]
def tensor(t,u):return tuple(int(t[x]==u[y]) for y in range(len(u)) for x in range(len(t)))
def sign_table(seed,m,r):
    k=(len(seed)-1).bit_length();core=k*m;N=1<<(core+1+r)
    ans=[]
    for x in range(N):
        if x>>(core+1):ans.append(1);continue
        sign=2*((x>>core)&1)-1
        for j in range(m):sign*=2*seed[(x>>(k*j))&((1<<k)-1)]-1
        ans.append(int(sign>0))
    return tuple(ans)
def polynomial(seed,m,r):
    k=(len(seed)-1).bit_length();core=k*m;N=1<<(core+1+r);p=Q(1,1<<r)
    sh=a.direct_coeffs(seed);out=[]
    for s in range(N):
        if s==0:v=1-p
        elif not s&((1<<(core+1))-1):v=-p
        elif s>>core&1:
            v=-p  # Truth-table balance sign is 2*bit-1 = -Walsh_character.
            for j in range(m):v*=sh[(s>>(k*j))&((1<<k)-1)]
        else:v=Q(0)
        ck((v*N).denominator==1);out.append(int(v*N))
    return out
def inverse_values(w):
    # Evaluate the polynomial by successive splits in descending coordinate order.
    v=list(w);bit=len(w)//2
    while bit:
        for start in range(0,len(v),2*bit):
            for offset in range(bit):
                x,y=v[start+offset],v[start+offset+bit]
                v[start+offset]=x+y;v[start+offset+bit]=x-y
        bit//=2
    return [Q(x,len(w)) for x in v]
def main():
    start=time.perf_counter();small=[]
    for z in range(16):
        t=tuple((z>>x)&1 for x in range(4));small.append((t,direct_diag(t)))
    for t,Tt in small:
        for u,Tu in small:ck(direct_diag(tensor(t,u))==Tt+Tu)
    receipts=[]
    for name,seed in [('dictator',(0,1)),('PD2',(0,1,1,1)),('PD3',(0,)+(1,)*7)]:
        for m in (1,2):
            data=json.loads((ROOT/'out'/('CASE_'+name+'_'+str(m)+'.json')).read_text());r=data['r'];p=Q(1,1<<r)
            k=(len(seed)-1).bit_length();core=k*m;t=sign_table(seed,m,r);N=len(t)
            ck(hashlib.sha256(bytes(t)).hexdigest()==data['truth_sha256'])
            w=polynomial(seed,m,r);iv=inverse_values(w);ck(iv==[2*v-1 for v in t])
            for s in (0,1,(1<<core),N-1):
                direct=sum((2*v-1)*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t));ck(w[s]==direct)
            O,R,T=diag_integer(w);ck(T==Q(data['T']))
            physicalI=sum(Q(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(data['n']))
            ck(physicalI==Q(data['I']))
            coreT=sum(O[:core])+sum(z for (i,j),z in R.items() if j<core);ck(coreT==Q(data['core_T']))
            components={'O_z':O[core],'R_z_core':sum(R[i,core] for i in range(core)),
                        'R_z_control':sum(R[core,j] for j in range(core+1,data['n'])),
                        'R_control_control':sum(z for (i,j),z in R.items() if i>core)}
            for key,value in components.items():ck(value==Q(data['components'][key]))
            children=Counter(tuple(t[x|(b<<core)] for x in range(1<<core)) for b in range(1<<(r+1)))
            ck(sum(children.values())==1<<(r+1))
            childH={};childI=Q(0)
            for child,mult in children.items():
                pr=[v*v for v in a.direct_coeffs(child)];h=a.ent(pr);inf=sum(s.bit_count()*v for s,v in enumerate(pr))
                childH=a.combine((1,childH),(Q(mult,1<<(r+1)),h));childI+=Q(mult,1<<(r+1))*inf
            rootH=a.ent([Q(v*v,N*N) for v in w])
            for ledger in data['ledger']:
                K=ledger['K'];S=a.combine((-1,childH),(K*childI,{2:Q(1)}));D=a.combine((1,rootH),(-K*physicalI,{2:Q(1)}))
                ck({str(pr):str(v) for pr,v in S.items()}==ledger['S_control_z'])
                ck({str(pr):str(v) for pr,v in D.items()}==ledger['D_root'])
                paid=a.combine((1,D),(1,S));ck({str(pr):str(v) for pr,v in paid.items()}==ledger['D_plus_S'])
                if K>=4:ck(a.bounds(a.combine((1,paid),(p,{2:Q(1)})))[1]<0)
            receipts.append({'seed':name,'m':m,'n':data['n'],'exact_T':str(T),'complete_child_assignments':1<<(r+1),'distinct_children':len(children)})
            if time.perf_counter()-start>55:raise TimeoutError('Frozen55sec cap')
    out={'tensor_products':256,'activation_cases':6,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'receipts':receipts,'distinct_variance_quartets':merge_refund.cache_info().currsize}
    (ROOT/'out/INDEPENDENT_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
