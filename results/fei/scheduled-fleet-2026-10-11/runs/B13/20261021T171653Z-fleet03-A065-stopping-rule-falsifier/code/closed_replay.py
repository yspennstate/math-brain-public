"""Independent closed coefficient multiplicities, no large Boolean FWHT."""
import kernel as k
import tag as t
from fractions import Fraction as F
import json,time

def entropy(nums,den):
    # Dyadic coefficients nums/den, with exact multiplicity.
    exp=den.bit_length()-1;k.check(den==1<<exp)
    lo=hi=0;mass=0
    for a,count in nums:
        mass+=count*a*a
        if a:
            l,h=k.log_bounds(abs(a));weight=F(count*a*a,den*den)
            lo+=k.floor(weight*(2*exp*k.SCALE-2*h))
            hi+=k.ceil(weight*(2*exp*k.SCALE-2*l))
    k.check(mass==den*den)
    return lo,hi

def main():
 start=time.monotonic();rows=[]
 raw=json.loads((t.ROOT/'out/BENT_EXACT.json').read_text(encoding='utf-8'))
 for n in [4,6,8,10,12]:
    N=1<<n;r=1<<(n//2);plus=(N+r)//2;minus=(N-r)//2;delta=F(1,N)
    hm=entropy([(r-1,plus),(r+1,minus),(1,N)],N)
    hu=k.exact(F(n));hv=entropy([(r-2,plus),(r+2,minus)],N)
    D=k.sub(hm,k.half(k.add(hu,hv)))
    for seed in ['point2','majority3']:
        Is=F(1) if seed=='point2' else F(3,2);Hs=2
        prefix=[k.sub(k.add(D,k.exact(delta*Hs)),k.exact(delta*(1+Is)*C)) for C in t.PRICES]
        expected=[k.pos(p) for p in prefix]
        row=next(x for x in raw['cases'] if x['k']==n and x['seed']==seed)
        for p,q in zip(expected,row['Qearly']):k.check(max(p[0],q[0])<=min(p[1],q[1]))
        k.check(all(q==[0,0] for q in row['bank']))
        rows.append({'k':n,'seed':seed,'HM':hm,'Hu':hu,'Hv':hv,'Dselector':D,'prefix_debt':prefix,'terminal_entropy_mean':k.half(k.add(hu,hv)), 'query_influence':str(delta*(1+Is))})
 witness=next(x for x in rows if x['k']==10 and x['seed']=='majority3')
 eps=witness['prefix_debt'][1];k.check(F(eps[0],k.SCALE)>F(1,100000))
 # Exact partial-history realization: bent12 x0=x1=0 is bent10.
 b12=lambda x:sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,12,2))%2
 b10=lambda x:sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,10,2))%2
 for x in range(1<<10):k.check(b12(x<<2)==b10(x))
 # Both sides of majority3 split are nonconstant two-bit AND/OR profiles.
 a=bytes(int(x.bit_count()>=2) for x in range(8))
 ca,cb=k.children(a,0);k.check(len(set(ca))==len(set(cb))==2)
 # Direct independent edge counts for the small seed, including tag influence.
 k.check(sum(F(sum(x!=y for x,y in zip(*k.children(a,i))),4) for i in range(3))==F(3,2))
 out={'rows':rows,'witness_epsilon_scaled':eps,'scale':str(k.SCALE),'epsilon_greater_than':'1/100000','partial_history_probability':'1/4','assertions':k.ASSERTIONS,'seconds':time.monotonic()-start}
 (t.ROOT/'out/CLOSED_REPLAY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
 print('PASS',k.ASSERTIONS,'epsilon',[str(F(x,k.SCALE)) for x in eps], 'seconds',out['seconds'])
if __name__=='__main__':main()
