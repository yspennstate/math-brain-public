from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, json, math, sys, time

sys.set_int_max_str_digits(100000)

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
OUT.mkdir(exist_ok=True)
checks=0

def ck(test,label):
    global checks
    checks+=1
    if not test: raise AssertionError(label)

def factors(n):
    ans={};p=2
    while p*p<=n:
        while n%p==0:
            ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans

def lg(argument,weight=Q(1)):
    argument=Q(argument);form={}
    if not weight:return form
    for n,sign in [(argument.numerator,1),(argument.denominator,-1)]:
        for p,e in factors(n).items():form[p]=form.get(p,Q(0))+weight*sign*e
    return {p:a for p,a in form.items() if a}

def combine(*terms):
    form={}
    for a,term in terms:
        for p,v in term.items():form[p]=form.get(p,Q(0))+a*v
    return {p:a for p,a in form.items() if a}

def logbounds(argument):
    x=Q(argument);shift=0
    while x>=2:x/=2;shift+=1
    while x<1:x*=2;shift-=1
    def ln(q):
        z=(q-1)/(q+1)
        lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(48)),Q(0))
        tail=2*z**97/(97*(1-z*z))
        return lo,lo+tail
    a,b=ln(x);c,d=ln(Q(2))
    return Q(shift)+a/d,Q(shift)+b/c

def directbounds(args):
    lo=hi=Q(0)
    for weight,arg in args:
        a,b=logbounds(arg)
        lo+=weight*(a if weight>=0 else b)
        hi+=weight*(b if weight>=0 else a)
    return lo,hi

def kl(mu,ref):
    ck(sum(mu)==sum(ref)==1,'complete laws normalize')
    return combine(*[(p,lg(p/r)) for p,r in zip(mu,ref) if p])

def bent(x,d):
    return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(d//2))%2 else 1

def physical(d):
    n=d+2;length=1<<n
    vals=[(-1 if (x&3)==3 else 1) if x>>2==0 else bent(x>>2,d) for x in range(length)]
    w=[sum(vals[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(length)) for s in range(length)]
    p=[Q(a*a,length*length) for a in w]
    delta=Q(1,1<<d);t=Q(1,1<<(d//2));e=delta/2
    ck(sum(p)==1,'Parseval');ck(all(a>0 for a in p),'full Fourier support')
    influences=[]
    for i in range(n):
        inf=Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(length)),length)
        ck(inf==sum(a for s,a in enumerate(p) if s&(1<<i)),'physical versus spectral influence')
        ck(inf==(e if i<2 else (1+delta)/2),'predicted coordinate influence')
        influences.append(inf)
    ck(sum(influences)==Q(d,2)+(Q(d,2)+1)*delta,'single total physical budget')
    signs={1:0,-1:0}
    for core in range(1<<d):
        sigma=bent(core,d);signs[sigma]+=1
        amps=[sigma*t-delta/2,delta/2,delta/2,-delta/2]
        for gate in range(4):
            ck(Q(w[(core<<2)|gate],length)==amps[gate],'signed character amplitudes')
    ck(signs=={1:(2**d+2**(d//2))//2,-1:(2**d-2**(d//2))//2},'both bent sign counts')
    args=[(Q(1+sigma*t,2),(1-delta/2)/(1-sigma*t+delta/2)) for sigma in [1,-1]]
    D0=combine(*[(a,lg(arg)) for a,arg in args]);lo,hi=directbounds(args)
    ck(lo>Q(24,169)*delta and hi<Q(15,16)*delta,'dimension-uniform rational envelope')
    ck(hi<Q(63,128),'original strict margin')
    ck(7**128<2**63*5**128,'original integer logarithm certificate')
    rows=[]
    for query,partner in [(0,1),(1,0)]:
        indices=[s for s in range(length) if not s&(1<<query)]
        mu=[p[s|(1<<query)]/e for s in indices]
        ref=[p[s]+p[s|(1<<query)] for s in indices]
        binary_mu=[sum(m for s,m in zip(indices,mu) if (s>>partner)&1==v) for v in [0,1]]
        binary_ref=[sum(r for s,r in zip(indices,ref) if (s>>partner)&1==v) for v in [0,1]]
        ck(binary_mu==[Q(1,2),Q(1,2)] and binary_ref==[1-e,e],'complete quotient law')
        fullD=kl(mu,ref);binaryD=kl(binary_mu,binary_ref)
        ck(fullD==combine((1,binaryD),(Q(1,2),D0)),'full conditional KL identity')
        for v in [0,1]:
            cm=[m/binary_mu[v] for s,m in zip(indices,mu) if (s>>partner)&1==v]
            cr=[r/binary_ref[v] for s,r in zip(indices,ref) if (s>>partner)&1==v]
            ck(kl(cm,cr)==(D0 if v==0 else {}),'conditional core likelihood exact')
        M=combine(*[(p[s|(1<<query)],lg((p[s]+p[s|(1<<query)])/p[s|(1<<query)])) for s in indices])
        ck(M==combine((e,lg(1/e)),(-e,fullD)),'complete retained price')
        ck(all(p[s]>0 and p[s|(1<<query)]>0 for s in indices),'positive erasure')
        lower_price=1+logbounds((1-e)/e)[0]/2-hi/2
        ck(lower_price>Q(d,2)+Q(3,4),'original retained row lower bound')
        rows.append({'query':query,'e':str(e),'D0_lower':str(lo),'D0_upper':str(hi),
                     'loss_upper':str(e*hi/2),'M_over_e_lower':str(lower_price)})
    ck(delta*hi/2<Q(3,64)*influences[2],'dedicated 3/64 core fraction pays both losses')
    ck(Q(d+2)/sum(influences)<=2+Q(4,d)<=4,'original entropy/influence dimension bound')
    result={'d':d,'physical_n':n,'I':str(sum(influences)),'rows':rows,'status':'PASS'}
    (OUT/('physical_d'+str(d)+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

def naive(d):
    delta=math.ldexp(1.0,-d);t=math.ldexp(1.0,-d//2)
    return ((1+t)/2*math.log2((1-delta/2)/(1-t+delta/2))
           +(1-t)/2*math.log2((1-delta/2)/(1+t+delta/2)))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    start=time.perf_counter();rows=[];first_bad=first_zero=first_negative=first_e_zero=first_mass_zero=first_delta_zero=None
    physical_ds=[2] if args.pilot else [2,4,6,8]
    compressed_ds=range(2,82,2) if args.pilot else range(2,1082,2)
    with (OUT/('pilot_cases.jsonl' if args.pilot else 'cases.jsonl')).open('w',encoding='utf-8') as receipt:
        for d in physical_ds:
            result=physical(d);rows.append(result);receipt.write(json.dumps(result)+'\n');receipt.flush()
        for d in compressed_ds:
            delta=Q(1,1<<d);t=Q(1,1<<(d//2))
            ck(t*t==delta and 0<t<=Q(1,2),'compressed exact dyadics')
            ck((4*delta-1)*(5*delta+1)==20*delta*delta-delta-1<=0,'reserve polynomial including d2 endpoint')
            ck(Q(15,32)*delta*delta<=Q(3,64)*(1+delta)/2,'quadratic core reserve')
            ck(7*(1-t+delta/2)-5*(1-delta/2)==(2-3*t)*(1-2*t)>=0,'original likelihood bound')
            value=naive(d)
            if value<=0 and first_bad is None:first_bad=d
            if value==0 and first_zero is None:first_zero=d
            if value<0 and first_negative is None:first_negative=d
            fd=math.ldexp(1.0,-d)
            if fd/2==0 and first_e_zero is None:first_e_zero=d
            if (fd/2)**2==0 and first_mass_zero is None:first_mass_zero=d
            if fd==0 and first_delta_zero is None:first_delta_zero=d
            receipt.write(json.dumps({'d':d,'naive_D0_hex':value.hex(),'analytic_D0_positive_lower':str(Q(24,169)*delta)})+'\n');receipt.flush()
            ck(time.perf_counter()-start<55,'frozen runtime guard')
    compressed_count=len(compressed_ds)
    if first_bad is not None:
        d=first_bad;delta=Q(1,1<<d);t=Q(1,1<<(d//2))
        lo,hi=directbounds([(Q(1+sigma*t,2),(1-delta/2)/(1-sigma*t+delta/2)) for sigma in [1,-1]])
        ck(lo>0,'fixed 48-term certificate for first floating false sign')
        fail={'d':d,'naive_D0_hex':naive(d).hex(),'true_lower_exact':str(lo),'true_upper_exact':str(hi),
              'analytic_lower':str(Q(24,169)*delta),'claim_refuted':'naive binary64 evaluation preserves the positive D0 sign',
              'smallest_scope':'first even d in frozen ordered range; no claim across other formulas or floating platforms',
              'original_A073_claim_refuted':False}
        (OUT/('pilot_failure.json' if args.pilot else 'float_failure.json')).write_text(json.dumps(fail,indent=2)+'\n',encoding='utf-8')
    result={'status':'PASS','physical_cases':len(physical_ds),'compressed_cases':compressed_count,'checks':checks,
            'elapsed_seconds':time.perf_counter()-start,'first_naive_nonpositive_d':first_bad,'first_naive_zero_d':first_zero,
            'first_naive_negative_d':first_negative,'first_query_influence_underflow_d':first_e_zero,
            'first_gate_atom_mass_underflow_d':first_mass_zero,'first_delta_underflow_d':first_delta_zero,
            'new_dedicated_core_fraction':'3/64','universal_FEI_constant_improvement':0,'full_FEI':'OPEN'}
    (OUT/('pilot.json' if args.pilot else 'audit.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':main()
