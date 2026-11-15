"""Large disjoint MUX: (1-AND_L) g_k + AND_L parity_(2^L k)."""
import math,json
import numpy as np
from pathlib import Path
from experiment import data,zeta,KS,TS,TH
LN2=math.log(2)
def calculate(L,g):
    mu,up,p,pc=data(g);mu=mu[0];up=up[0];p=p[0];k=len(g).bit_length()-1
    q=2.**-L;b=1-q;m=(1<<L)*k
    Ig=float(sum(mu*pc));I=b*Ig+q*m+L*q
    row={'name':f'MUX_L{L}_k{k}_m{m}','L':L,'k':k,'m':m,'g_tt':hex(sum(int(a<0)<<i for i,a in enumerate(g))),'I':I,'Var':1.,'n':L+k+m}
    # Spectral support grouped by y, together with individual g subsets.
    groups=[]
    for y in range(L+1):
        C=math.comb(L,y);a=b*b if y==0 else q*q
        for X in range(1,len(g)):
            if mu[X]==0:continue
            ps=(b if y==0 else q*2**y)*p[X]
            us=(b if y==0 else q*2**-y)*up[X]
            groups.append((C*a*mu[X],int(pc[X])+y,ps,us,'g',X,y))
        groups.append((C*q*q,m+y,q*2**y,q*2**-y,'h',0,y))
    row['P']=sum(w*-math.log2(ps) for w,s,ps,us,kind,X,y in groups)
    row['A']=sum(w*-math.log2(us) for w,s,ps,us,kind,X,y in groups)
    row['H']=sum(w*-math.log2((b*b if y==0 else q*q)*mu[X] if kind=='g' else q*q) for w,s,ps,us,kind,X,y in groups)
    for K in KS:row[f'Sp{K}']=sum(w*-math.log2(ps) for w,s,ps,us,kind,X,y in groups if -math.log2(ps)>K*s+1e-12)
    for t in TS:
        F=zeta(mu[None,:],1-t)[0];cost=0.;mom={th:0. for th in TH}
        total=0.
        for y in range(L+1):
            C=math.comb(L,y);a=b*b+q*q*((2-t)**L-1) if y==0 else q*q*(2-t)**(L-y)
            for X in range(1,len(g)):
                tau=C*t**(int(pc[X])+y)*a*F[X]
                if tau==0:continue
                ps=(b if y==0 else q*2**y)*p[X]
                cost+=tau*-math.log2(ps);total+=tau
                for th in TH:mom[th]+=tau*ps**-th
            tau=C*t**y*q*q*(2-t)**(L-y)*(1-(1-t)**m)
            ps=q*2**y;cost+=tau*-math.log2(ps);total+=tau
            for th in TH:mom[th]+=tau*ps**-th
            if y:
                tau=C*t**y*q*q*(2-t)**(L-y)*(F[0]+(1-t)**m)
                ps=q*2**(y-1);cost+=tau*-math.log2(ps);total+=tau
                for th in TH:mom[th]+=tau*ps**-th
        row[f'T{t:g}']=cost
        for th in TH:row[f'taumom_t{t:g}_th{th:g}']=math.log2(1-total+mom[th])
    row['ref_product']=sum(math.log2(1+b*up[1<<j])-b*up[1<<j]*math.log2(b*up[1<<j]) for j in range(k) if up[1<<j]>0)+(m+L)*(math.log2(1+q)-q*math.log2(q))
    logZ=np.logaddexp(math.log((b*b+q*q*(3**L-1))*sum(mu*2.**pc)),2*math.log(q)+L*math.log(3)+m*LN2)
    row['markov_logZ']=float(logZ/LN2);row['ref_markov_normalized']=row['A']+row['markov_logZ']
    for r in (.25,.5,.75):row[f'ref_tau{r:g}']=0.
    row['ref_mixture3']=row['ref_mixture_uniform']=0.
    for w,s,ps,us,kind,X,y in groups:
        lt=[]
        for r in (.25,.5,.75):
            if kind=='h':logtau=2*math.log(q)+(m+y)*math.log(r)+(L-y)*math.log(2-r)
            else:
                a=b*b+q*q*((2-r)**L-1) if y==0 else q*q*(2-r)**(L-y)
                logtau=s*math.log(r)+math.log(a)+math.log(zeta(mu[None,:],1-r)[0,X])
            row[f'ref_tau{r:g}']-=w*logtau/LN2;lt.append(logtau)
        row['ref_mixture3']-=w*(float(np.logaddexp.reduce(lt))-math.log(3))/LN2
        if kind=='h':
            integ=0.;beta=1/(m+y+1)
            for j in range(L-y+1):
                if j:beta*=j/(m+y+j+1)
                integ+=math.comb(L-y,j)*beta
            pi=q*q*integ
        else:
            pi=0.
            for U in range(len(g)):
                if U&X!=X or mu[U]==0:continue
                for v in range(y,L+1):
                    mass=(b*b if v==0 else q*q)*mu[U]*math.comb(L-y,v-y)
                    d=int(pc[U])+v
                    pi+=mass/((d+1)*math.comb(d,s))
        row['ref_mixture_uniform']-=w*math.log2(pi)
    for theta in (1.,.5,.25):
        for c in (2.,4.,8.):
            W=sum(w*c**-s*us**-theta for w,s,ps,us,kind,X,y in groups)
            row[f'W_K_c{c:g}_th{theta:g}']=math.log2(W)/I
    # Raw counts: t=1/2, with both spectral-degree cutoffs and no cutoff.
    for theta in TH:
        logH=(1-theta)*math.log(q)+L*math.log1p(.5/2**(1+theta))+m*math.log(1.5)
        row[f'raw_lower_th{theta:g}']=logH/LN2
        d=1+.5/2**(1+theta)
        gQ=sum(.5**int(pc[X])*up[X]*p[X]**-theta for X in range(1,len(g)) if up[X]>0)
        other=1+(b**(1-theta)+q**(1-theta)*(d**L-1))*gQ+2**(1+theta)*q**(1-theta)*(d**L-1)
        # Subtract the H-empty contribution already accounted for in 'other'.
        hcoef=q**(1-theta)*d**L
        rawlog=float(np.logaddexp(math.log(other),math.log(hcoef)+m*math.log(1.5)+math.log1p(-math.exp(-m*math.log(1.5)))))
        row[f'raw_th{theta:g}']=rawlog/LN2
        for factor in (2,4):
            M=int(math.ceil(factor*I));raw=0.
            for y in range(L+1):
                C=math.comb(L,y)
                hup=sum(math.comb(L-y,v-y)*q*q for v in range(y,L+1) if m+v<=M)
                gups=np.zeros(len(g))
                for X in range(len(g)):
                    for U in range(len(g)):
                        if U&X!=X or mu[U]==0:continue
                        gups[X]+=mu[U]*sum(math.comb(L-y,v-y)*(b*b if v==0 else q*q) for v in range(y,L+1) if int(pc[U])+v<=M)
                for X in range(1,len(g)):
                    if gups[X]==0:continue
                    ps=(b if y==0 else q*2**y)*p[X]
                    raw+=C*.5**(y+int(pc[X]))*gups[X]*ps**-theta
                if y:
                    raw+=C*.5**y*(gups[0]+hup)*(q*2**(y-1))**-theta
                else:raw+=gups[0]+hup
                if hup>0:raw+=C*.5**y*math.expm1(m*math.log(1.5))*hup*(q*2**y)**-theta
            row[f'raw_M{factor}I_th{theta:g}']=math.log2(raw)
    return row

def main():
    result=[];rng=np.random.default_rng(13013013)
    for k in (3,5,7):
        g=np.ones(1<<k,dtype=np.int8);g[rng.choice(1<<k,1<<(k-1),replace=False)]=-1
        for L in (1,2,4,8,12,16):
            row=calculate(L,g);result.append(row);Path('mux.json').write_text(json.dumps(result,indent=2));print(row['name'],'P/I',row['P']/row['I'],'product/I',row['ref_product']/row['I'],flush=True)
if __name__=='__main__':main()
