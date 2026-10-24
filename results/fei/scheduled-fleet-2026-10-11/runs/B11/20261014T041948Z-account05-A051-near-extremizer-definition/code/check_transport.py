from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json,time,hashlib
import exact_tools as d
ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
@lru_cache(None)
def refund(a,b,c,e):
    q=a*a+b*b+c*c+e*e
    if not q:return F(0)
    def term(x,y,u,v):
        s=x*x+y*y;t=u*u+v*v
        return F(4*(x*y*t-u*v*s)**2,q*s*t) if s*t else F(0)
    r=term(a,b,c,e)+term(a,c,b,e)
    ci=(F(4*a*a*b*b,a*a+b*b) if a*a+b*b else F(0))+(F(4*c*c*e*e,c*c+e*e) if c*c+e*e else F(0))
    cj=(F(4*a*a*c*c,a*a+c*c) if a*a+c*c else F(0))+(F(4*b*b*e*e,b*b+e*e) if b*b+e*e else F(0))
    pair=F(4*((a*b+c*e)**2+(a*c+b*e)**2+(a*e+b*c)**2),q)
    parity=F(4*(a*e+b*c)**2,q)
    ck(r>=0);ck(pair==ci+cj+parity-r)
    ck(r<=ci+cj)
    return r
def diagnostic(table):
    N=len(table);n=(N-1).bit_length();w=d.fwht([2*v-1 for v in table]);den=N*N
    O=[];R={}
    for i in range(n):O.append(F(sum(max(w[s|1<<i]**2-w[s]**2,0) for s in range(N) if not s>>i&1),den))
    for i in range(n):
        for j in range(i+1,n):
            mask=(1<<i)|(1<<j)
            quartets=Counter((w[s],w[s|1<<i],w[s|1<<j],w[s|mask]) for s in range(N) if not s&mask)
            R[i,j]=sum(mult*refund(*q) for q,mult in quartets.items())/den
    I=F(sum(s.bit_count()*v*v for s,v in enumerate(w)),den)
    T=sum(O)+sum(R.values());ck(T>=0);ck(T<=(4*n-3)*I if n else T==0)
    return {'O':O,'R':R,'T':T,'I':I,'mu':F(w[0],N),'H':d.spectrum_table(tuple(table))[0]}
def tensor(t,u):return tuple(int((2*t[x]-1)*(2*u[y]-1)>0) for y in range(len(u)) for x in range(len(t)))
def activate(seed,m,r):
    k=(len(seed)-1).bit_length();core=k*m;N=1<<(core+1+r);table=[]
    for z in range(N):
        val=1
        if z>>(core+1)==0:
            val=2*((z>>core)&1)-1
            for j in range(m):val*=2*seed[(z>>(k*j))&((1<<k)-1)]-1
        table.append(int(val>0))
    return tuple(table)
def logs(x):return d.add([(1,d.factor(x.numerator)),(-1,d.factor(x.denominator))])
def main():
    start=time.perf_counter();small=[]
    for truth in range(16):
        t=tuple((truth>>x)&1 for x in range(4));small.append((t,diagnostic(t)))
    for t,ft in small:
        for u,fu in small:
            v=diagnostic(tensor(t,u));ck(v['T']==ft['T']+fu['T']);ck(v['I']==ft['I']+fu['I'])
    seeds=[('dictator',(0,1)),('PD2',(0,1,1,1)),('PD3',(0,)+(1,)*7)]
    for name,t in seeds:
        f=diagnostic(t);k=(len(t)-1).bit_length()
        for m in (1,2):
            r=((m+1)**4-1).bit_length();p=F(1,1<<r);core=k*m
            tab=activate(t,m,r);g=diagnostic(tab);mum=f['mu']**m
            coreO=sum(g['O'][:core]);coreR=sum(v for (i,j),v in g['R'].items() if j<core)
            zO=g['O'][core];controlO=sum(g['O'][core+1:])
            zcoreR=sum(g['R'][i,core] for i in range(core))
            zcontrolR=sum(g['R'][core,j] for j in range(core+1,core+1+r))
            controlR=sum(v for (i,j),v in g['R'].items() if i>core)
            cross=sum(v for (i,j),v in g['R'].items() if i<core and j>core)
            ck(coreO+coreR==p*m*f['T']);ck(controlO==0);ck(cross==0)
            ck(zO==p*(1-mum*mum));ck(zcoreR<=8*p*core*mum*mum)
            ck(zcontrolR<=14*r*p*p)
            exactcontrol=F(r*(r-1),2)*4*p*p/(((1-p)**2+3*p*p)*((1-p)**2+p*p))
            ck(controlR==exactcontrol);ck(controlR<=64*F(r*(r-1),2)*p*p)
            E=g['T']-p*m*f['T'];bound=p+8*p*core*mum*mum+(64*F(r*(r-1),2)+14*r)*p*p
            ck(0<=E<=bound);ck(E==zO+zcoreR+zcontrolR+controlR)
            ck(g['I']==p*(m*f['I']+1+r))
            theta=f['T']/f['I'];delta=abs(g['T']/g['I']-theta)
            error=(bound/p+(1+r)*theta)/(m*f['I']+1+r);ck(delta<=error)
            Ap=d.add([(-(1-p)**2,logs((1-p)**2)),(p*p,logs(p*p))])
            expectedH=d.add([(p*m,f['H']),(4*r*p,{2:F(1)}),(1,Ap)])
            ck(g['H']==expectedH)
            ledger=[]
            for K in (2,4,8):
                Dseed=d.add([(1,f['H']),(-K*f['I'],{2:F(1)})])
                Droot=d.add([(1,g['H']),(-K*g['I'],{2:F(1)})])
                S=d.add([(-p*m,Dseed)])
                paid=d.add([(p*((4-K)*r-K),{2:F(1)}),(1,Ap)])
                ck(d.add([(1,Droot),(1,S)])==paid)
                if K>=4:
                    ck(d.interval(d.add([(1,paid),(p,{2:F(1)})]))[1]<0)
                    ck(d.interval(d.add([(1,Droot),(-p*m,Dseed)]))[1]<0)
                if d.interval(Dseed)[0]>0:ck(d.interval(S)[1]<0)
                ledger.append({'K':K,'D_seed':d.enc(Dseed),'D_root':d.enc(Droot),'S_control_z':d.enc(S),'D_plus_S':d.enc(paid)})
            out={'seed':name,'m':m,'r':r,'n':(len(tab)-1).bit_length(),'p':str(p),'mu_m':str(mum),'seed_T':str(f['T']),'seed_I':str(f['I']),'T':str(g['T']),'I':str(g['I']),'Theta_seed':str(theta),'Theta_activated':str(g['T']/g['I']),'core_T':str(coreO+coreR),'wrapper_E':str(E),'wrapper_bound':str(bound),'relative_error_bound':str(error),'components':{'O_z':str(zO),'R_z_core':str(zcoreR),'R_z_control':str(zcontrolR),'R_control_control':str(controlR)},'ledger':ledger,'truth_sha256':hashlib.sha256(bytes(tab)).hexdigest()}
            (ROOT/'out'/('CASE_'+name+'_'+str(m)+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
            print(json.dumps({k:out[k] for k in ['seed','m','n','Theta_seed','Theta_activated','core_T','wrapper_E']}),flush=True)
            if time.perf_counter()-start>55:raise TimeoutError('Frozen55sec cap')
    out={'tensor_products':256,'activation_cases':6,'assertions':checks,'helper_assertions':d.ASSERTIONS,'elapsed_seconds':time.perf_counter()-start,'distinct_signed_quartets':refund.cache_info().currsize}
    (ROOT/'out/SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
