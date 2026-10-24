from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import prod,lcm,comb
import json,hashlib,time,sys
ROOT=Path(__file__).resolve().parents[1]
VERSION='A073-exact-refund-review/1'
START=time.perf_counter();CHECKS=0

def ck(ok,detail=''):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError((CHECKS,detail))
    if time.perf_counter()-START>55:raise RuntimeError('Frozen 55-second job cap exceeded')

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def save(name,value):
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/name).write_text(json.dumps(serial(value),indent=2)+'\n',encoding='utf-8')

@lru_cache(None)
def factor(n):
    if n<1:raise ValueError('Positive factor input required')
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out

def combine(*terms):
    out={}
    for weight,form in terms:
        for prime,c in form.items():out[prime]=out.get(prime,F(0))+weight*c
    return {p:F(c) for p,c in out.items() if c}

def lg(q,weight=F(1)):
    q=F(q);weight=F(weight)
    if q<=0:raise ValueError('Positive log argument required')
    return combine((weight,factor(q.numerator)),(-weight,factor(q.denominator)))

def product_sign(form):
    if not form:return {'sign':0,'denominator':1,'exponents':{},'bit_budget':0}
    L=lcm(*(c.denominator for c in form.values()))
    exps={p:int(c*L) for p,c in form.items()}
    estimate=sum(abs(e)*p.bit_length() for p,e in exps.items())
    ck(estimate<=1000000,'product budget')
    U=prod(p**e for p,e in exps.items() if e>0)
    V=prod(p**(-e) for p,e in exps.items() if e<0)
    return {'sign':(U>V)-(U<V),'denominator':L,'exponents':exps,'bit_budget':estimate,
       'U_hex':format(U,'x'),'V_hex':format(V,'x')}

@lru_cache(None)
def reduced_ln(t,N=40):
    t=F(t);ck(1<=t<=2,'log range')
    y=(t-1)/(t+1)
    lower=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return lower,lower+tail

@lru_cache(None)
def log_bounds(x,N=40):
    x=F(x);ck(x>0);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    if x==1:return F(k),F(k)
    a,b=reduced_ln(x,N);c,d=reduced_ln(F(2),N)
    return k+a/d,k+b/c

def bounds(form,N=40):
    lo=hi=F(0)
    for p,coef in form.items():
        a,b=log_bounds(F(p),N)
        if coef<0:a,b=b,a
        lo+=coef*a;hi+=coef*b
    return lo,hi

def decimal_interval(interval,digits=30):
    a,b=interval;scale=10**digits;a*=scale;b*=scale
    low=a.numerator//a.denominator
    high=-((-b.numerator)//b.denominator)
    def string(i):return ('-' if i<0 else '')+str(abs(i)//scale)+'.'+str(abs(i)%scale).zfill(digits)
    return {'lower':string(low),'upper':string(high),'lower_rational':F(low,scale),
      'upper_rational':F(high,scale),'digits':digits,'width':F(high-low,scale)}

def spectrum(table,direct=False):
    N=len(table);n=N.bit_length()-1
    ck(N==1<<n and all(x in (-1,1) for x in table))
    W=list(table);step=1
    while step<N:
        for start in range(0,N,step*2):
            for j in range(start,start+step):W[j],W[j+step]=W[j]+W[j+step],W[j]-W[j+step]
        step*=2
    ck(sum(w*w for w in W)==N*N,'Parseval')
    inverse=W[:];step=1
    while step<N:
        for start in range(0,N,step*2):
            for j in range(start,start+step):inverse[j],inverse[j+step]=inverse[j]+inverse[j+step],inverse[j]-inverse[j+step]
        step*=2
    ck(inverse==[N*x for x in table],'signed inverse')
    if direct:
        ck(W==[sum(table[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)],'direct characters')
    p={s:F(w*w,N*N) for s,w in enumerate(W) if w}
    e=[]
    for i in range(n):
        physical=F(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N)
        ck(physical==sum(m for s,m in p.items() if s>>i&1),'physical influence')
        e.append(physical)
    return p,e,W

def edge_forms(p,n,e,save_joint=False):
    I=sum(e,F(0));M={};ID={};tail={};levels={};rows=[];joint_P={};joint_Q={}
    for i in range(n):
        bit=1<<i;r={}
        for s,mass in p.items():r[s&~bit]=r.get(s&~bit,F(0))+mass
        ck(sum(r.values())==1,'complete residual normalizer')
        rowM={};rowD={};mu={}
        for t,r_mass in r.items():
            upper=p.get(t|bit,F(0))
            if e[i]:
                joint_Q[i,t]=e[i]*r_mass/I
                if upper:
                    mu[t]=upper/e[i];joint_P[i,t]=upper/I
                    rowD=combine((1,rowD),(1,lg(mu[t]/r_mass,mu[t])))
            if upper:
                term=lg(r_mass/upper,upper);rowM=combine((1,rowM),(1,term))
                level=t.bit_count();levels[level]=combine((1,levels.get(level,{})),(1,term))
                if t.bit_count()>=2:tail=combine((1,tail),(1,term))
        if e[i]:
            ck(sum(mu.values())==1,'derivative normalizer')
            ck(rowM==combine((1,lg(1/e[i],e[i])),(-e[i],rowD)),'row rarity refund')
        else:ck(rowM==rowD=={})
        M=combine((1,M),(1,rowM));ID=combine((1,ID),(e[i],rowD))
        rows.append({'i':i,'M':rowM,'D':rowD,'mu':mu,'r':r})
    if I:
        ck(sum(joint_P.values())==sum(joint_Q.values())==1,'joint normalizers')
        direct={}
        for key,Pmass in joint_P.items():
            ck(joint_Q[key]>0,'finite KL support')
            direct=combine((1,direct),(1,lg(Pmass/joint_Q[key],I*Pmass)))
        ck(direct==ID,'joint KL direct versus conditional')
        for i in range(n):
            ck(sum(v for (j,t),v in joint_P.items() if j==i)==e[i]/I,'P coordinate marginal')
            ck(sum(v for (j,t),v in joint_Q.items() if j==i)==e[i]/I,'Q coordinate marginal')
        rarity=combine(*[(1,lg(1/x,x)) for x in e if x])
        ck(M==combine((1,rarity),(-1,ID)),'joint refund')
    else:ck(M==ID=={} and not joint_P and not joint_Q)
    result={'I':I,'M':M,'ID':ID,'rows':rows,'tail':tail,'levels':levels}
    if save_joint:result['joint']={'P':[[i,t,v] for (i,t),v in joint_P.items()],
                               'Q':[[i,t,v] for (i,t),v in joint_Q.items()]}
    return result

def named_witnesses():
    source_dir=ROOT.parents[2]/'A072/runs/20261012T004036Z-account05-A072-exact-walsh-engine/out'
    Kstar={2:F(4),5:F(5,2),3:F(-9,2)};records=[]
    for n,mask,cutoff in [(5,4194372,F(539,200)),(6,1103806792023,F(368,125))]:
        table=[1-2*((mask>>x)&1) for x in range(1<<n)]
        p,e,W=spectrum(table,True);forms=[]
        for i in range(n):
            Bi={};bit=1<<i
            for t in range(1<<n):
                if t&bit:continue
                a,b=p.get(t,F(0)),p.get(t|bit,F(0))
                if a and b:Bi=combine((1,Bi),(1,lg(a+b,a+b)),(-1,lg(a,a)),(-1,lg(b,b)))
            ck(e[i]>0,'relevant witness coordinate')
            forms.append(combine((1/e[i],Bi)))
        candidate=0
        for i in range(1,n):
            sign=product_sign(combine((1,forms[i]),(-1,forms[candidate])))
            if sign['sign']<0:candidate=i
        E= forms[candidate];comparisons=[]
        for f in forms:
            comparison=product_sign(combine((1,f),(-1,E)));ck(comparison['sign']>=0)
            comparisons.append(comparison)
        minima=[i for i,c in enumerate(comparisons) if c['sign']==0]
        older=json.loads((source_dir/f'witness_n{n}.json').read_text())
        ck(E=={int(k):F(v) for k,v in older['minimum_prime_log'].items()},'A072 exact minimum form')
        ck(minima==older['minimum_coordinates'],'A072 minimizers')
        ck(W==older['certificate']['walsh'],'A072 integer Walsh')
        lower=product_sign(combine((1,E),(-1,lg(F(2),cutoff))))
        margin=product_sign(combine((1,E),(-1,Kstar)))
        ck(lower['sign']==margin['sign']==1,'strict required signs')
        interval=bounds(E,40);rounded=decimal_interval(interval)
        ck(rounded['width']<=F(2,10**30),'thirty decimal outward enclosure')
        gap=bounds(combine((1,E),(-1,lg(2,cutoff))),8)
        ck(gap[0]>0,'single eight-term margin check')
        record={'n':n,'negative_mask':mask,'negative_assignments':[x for x in range(1<<n) if mask>>x&1],
          'walsh':W,'influences':e,'minimum_coordinates':minima,'coordinate_forms':forms,'E_prime_log':E,
          'minimizer_certificates':comparisons,'cutoff':cutoff,'cutoff_sign':lower,'Kstar_sign':margin,
          'outward_interval':interval,'thirty_decimal_interval':rounded,'cutoff_margin_eight_terms':gap,
          'precision_refinements':0,'certification_order':'Exact sign first; one N=40 display interval for explicit lead precision request'}
        save(f'witness_n{n}.json',record);records.append(record)
        print(f'n={n}, E in [{rounded["lower"]}, {rounded["upper"]}], minimum coordinates {minima}',flush=True)
    save('WITNESS_SUMMARY.json',{'version':VERSION,'cases':2,'checks':CHECKS,'runtime_seconds':time.perf_counter()-START,
       'results':[{'n':r['n'],'minimum_coordinates':r['minimum_coordinates'],'E_interval':r['thirty_decimal_interval'],
         'cutoff_margin_eight_terms':r['cutoff_margin_eight_terms']} for r in records]})

def seeds():
    return [
      ('constant_plus',[1,1]),('constant_minus',[-1,-1]),('dictator',[1,-1]),
      ('AND2',[1,1,1,-1]),('parity2',[1,-1,-1,1]),
      ('majority3',[1 if x.bit_count()<=1 else -1 for x in range(8)]),
      ('point3',[-1]+[1]*7),
      ('bent4',[(-1)**(((x&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1))) for x in range(16)]),
      ('f5',[1-2*((4194372>>x)&1) for x in range(32)]),
      ('f6',[1-2*((1103806792023>>x)&1) for x in range(64)])]

def run_refund(pilot=False):
    domain=[]
    for name,seed in seeds():
        n=len(seed).bit_length()-1
        for m in ([1,2] if n<=3 else [1]):
            for ell in [2,3]:
                for k in [1,2,3]:domain.append((name,seed,m,ell,k))
    ck(len(domain)==102)
    if pilot:domain=[domain[i] for i in [0,18,42,96,101]]
    seed_cache={};h_cache={};rows=[]
    stream=ROOT/'out'/('refund_pilot.jsonl' if pilot else 'refund_cases.jsonl')
    with stream.open('w',encoding='utf-8') as output:
        for name,seed,m,ell,k in domain:
            n=len(seed).bit_length()-1
            if name not in seed_cache:
                p,e,W=spectrum(seed);seed_cache[name]=(p,e,edge_forms(p,n,e))
            sp,se,sf=seed_cache[name]
            key=(name,m,ell);d=n*m+ell
            if key not in h_cache:
                h=[]
                for x in range(1<<d):
                    sign=(-1)**((x>>(n*m)).bit_count())
                    for b in range(m):sign*=seed[(x>>(n*b))&((1<<n)-1)]
                    h.append(sign)
                hp,he,hw=spectrum(h);hf=edge_forms(hp,d,he)
                h_cache[key]=(h,hp,he,hf)
            h,hp,he,hf=h_cache[key]
            ck(hf['I']==m*sf['I']+ell)
            ck(hf['M']==combine((m,sf['M'])) and hf['ID']==combine((m,sf['ID'])),'tensor terminal cost')
            ck(hp.get(0,F(0))==0 and all(hp.get(1<<i,F(0))==0 for i in range(d)),'exception exclusion')
            q=F(1,1<<k);root=(1-q)**2+q*q
            actual=[h[x&((1<<d)-1)] if x>>d==0 else 1 for x in range(1<<(d+k))]
            ap,ae,aw=spectrum(actual);af=edge_forms(ap,d+k,ae,save_joint=name=='f6' and m==1 and ell==2 and k==3)
            # Independent exact amplitudes of the physical activation.
            expected={0:(1-q)**2}
            for control in range(1<<k):
                if control:expected[control<<d]=q*q
                for s,mass in hp.items():expected[(control<<d)|s]=q*q*mass
            ck(ap==expected,'actual Walsh versus activated product spectrum')
            for i in range(d):
                ck(ae[i]==q*he[i],'one physical coordinate budget')
                if not he[i]:continue
                core=hf['rows'][i];activated=af['rows'][i]
                support_h=sum(core['r'][t] for t in core['mu'])
                support_F=sum(activated['r'][t] for t in activated['mu'])
                ck(support_F==q*support_h,'normalizer lost by support conditioning')
                conditioned_h=combine((1,core['D']),(1,lg(support_h)))
                conditioned_F=combine((1,activated['D']),(1,lg(support_F)))
                ck(conditioned_h==conditioned_F,'support conditioning erases rarity refund')
                for t,mu in activated['mu'].items():
                    c,tcore=t>>d,t&((1<<d)-1)
                    ck(mu==q*core['mu'][tcore],'derivative conditional control uniform')
                    ck(activated['r'][t]==q*q*core['r'][tcore],'full-support reference submass')
                    ck(mu/activated['r'][t]==core['mu'][tcore]/core['r'][tcore]/q,'literal likelihood ratio')
                ck(activated['D']==combine((1,core['D']),(1,lg(1/q))),'core row divergence retains seed')
                ck(activated['M']==combine((q,core['M'])),'core row oriented cost')
            Dc=combine((1,lg(1/(2*q),1-q)),(1,lg(q/root,q)))
            Mc=combine((1,lg(2,q*(1-q))),(1,lg(root/(q*q),q*q)))
            for i in range(d,d+k):
                ck(ae[i]==q,'control influence')
                row=af['rows'][i];ck(row['D']==Dc and row['M']==Mc,'control refund')
                ck(row['mu'][0]==q and row['r'][0]==root,'exceptional complete reference atom')
                regular=F(0)
                for t,mu in row['mu'].items():
                    if t:ck(mu/row['r'][t]==1/(2*q),'regular control likelihood');regular+=mu
                ck(regular==1-q)
            ck(af['I']==q*(hf['I']+k),'aggregate single budget')
            expectedID=combine((q*m,sf['ID']),(1,lg(1/q,q*hf['I'])),(k*q,Dc))
            expectedM=combine((q*m,sf['M']),(k,Mc))
            expectedTail=combine((q*m,sf['M']),(1,lg(2,k*q*(1-k*q))))
            ck(af['ID']==expectedID and af['M']==expectedM,'joint complete transport')
            ck(af['tail']==expectedTail,'oriented level>=2 tail')
            geell=combine(*[(1,form) for level,form in af['levels'].items() if level>=ell])
            control_tail=k*(q/F(2)+q*q*sum(comb(k-1,r) for r in range(ell,k)))
            ck(geell==combine((q*m,sf['M']),(1,lg(2,control_tail))),'exact parity-level tail')
            data={'seed':name,'n':n,'m':m,'ell':ell,'k':k,'N':d+k,'I_seed':sf['I'],'I_F':af['I'],
              'M_seed':sf['M'],'I_seed_D_seed':sf['ID'],'M_F':af['M'],'I_F_D_F':af['ID'],
              'M_ge2_F':af['tail'],'M_geell_F':geell,'D_control':Dc,'joint_normalizers':'EXACT_ONE','identities':'EXACT_PRIME_LOG_ZERO'}
            output.write(json.dumps(serial(data))+'\n');output.flush();rows.append(data)
            if 'joint' in af:save('f6_k3_full_joint_reference.json',{'seed':name,'m':m,'ell':ell,'k':k,'data':af})
            if name=='dictator' and m==1 and ell==2 and k==1:
                i=n*m;row=af['rows'][i]
                rho=sum(row['r'][t] for t in row['mu'])
                conditioned=combine((1,row['D']),(1,lg(rho)))
                ck(rho==q and row['D']==lg(2) and conditioned=={} and row['M']=={})
                save('SUPPORT_CONDITIONING_MUTATION.json',{'actual_boolean_definition':'For physical bits b0,b1,b2,b3: h=(-1)^(b0+b1+b2); F=h if b3=0 and +1 otherwise',
                  'N':4,'coordinate':i,'influence':ae[i],'P_spectrum':ap,'derivative_law':row['mu'],
                  'complete_reference':row['r'],'reference_mass_on_derivative_support':rho,
                  'D_complete':row['D'],'D_conditioned':conditioned,'actual_M':row['M'],
                  'erroneous_M_if_conditioned_D_is_substituted':combine((1,lg(1/ae[i],ae[i])),(-ae[i],conditioned)),
                  'conclusion':'Complete KL is 1 bit; conditioned KL is 0; substitution changes actual M=0 into false M=1/2 bit'})
    result={'version':VERSION,'cases':len(rows),'checks':CHECKS,'runtime_seconds':time.perf_counter()-START,
      'failures':0,'pilot':pilot,'maximum_N':max(r['N'] for r in rows),'seed_count':len(seed_cache),
      'review_scope':'Exact finite validation of complete normalized channels; universal formulas justified by independent analytic proof'}
    save('REFUND_PILOT.json' if pilot else 'REFUND_SUMMARY.json',result);print(json.dumps(result,indent=2))

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='witnesses':named_witnesses()
    elif mode in ['refund','pilot']:run_refund(mode=='pilot')
    else:raise ValueError(mode)
