import ast,json,time
from fractions import Fraction as F
from pathlib import Path
import recentred_census as c
start=time.monotonic();results=[]
source=json.loads((c.SOURCE/'out/full_SUMMARY.json').read_text())
cases=[('NAND_case_0006',c.table(ast.literal_eval(source['cases'][6]['tree'])),48),('Hod_g3',c.hod(6),4)]
for m in (2,3):
    t=[int(sum(((x>>(2*j))&3)==3 for j in range(m))%2==0) for x in range(1<<(2*m))]
    cases.append((f'quadratic_tensor_{m}',t,None))
strict=[int(((-1 if (x&3)==3 else 1)*(-1 if x>>2==0 else 1))==1) for x in range(32)]
cases.append(('quadratic_times_PD3',strict,None))
for name,t,named in cases:
    N=len(t);n=N.bit_length()-1;den=N*N
    signed=[2*x-1 for x in t]; w=c.direct(signed);c.ck(w==c.fwht(signed));weights=[a*a for a in w]
    H=c.entnum(weights);I=sum(s.bit_count()*a for s,a in enumerate(weights));rows=[]
    for A in ([named] if named is not None else range(1,N-1)):
        ai=[i for i in range(n) if A>>i&1];ci=[i for i in range(n) if not A>>i&1]
        # Direct character sums and physical projections, not recursive formula restriction.
        mean={}
        for x in range(1<<len(ai)):
            child=[signed[c.unpack(x,ai)|c.unpack(y,ci)] for y in range(1<<len(ci))]
            wc=c.direct(child);c.ck(wc==c.fwht(child));mean=c.combine(mean,c.entnum([a*a for a in wc]))
        L=c.combine(H,mean,1,-(1<<len(ai)));B,beta,IA=c.block_stats(weights,A);J=c.combine(L,B,1,-1)
        c.ck(c.sign(J)>=0);c.ck(c.sign({p:-v for p,v in J.items()},2*beta)>=0)
        if name.startswith('quadratic_tensor'):
            m=n//2;touched=sum(bool(A&(3<<(2*j))) for j in range(m));a=A.bit_count()
            c.ck(B=={2:a*den});c.ck(beta==a*den//2);c.ck(IA==a*den//2)
            c.ck(L=={2:2*touched*den});c.ck(J==({2:(2*touched-a)*den} if 2*touched!=a else {}))
            c.ck(c.sign(c.combine(H,B,IA,-I),-2*beta*I)<0)
        if name=='quadratic_times_PD3':
            c.ck(c.sign(c.combine(H,B,IA,-I),-2*beta*I)<0)
        row={'mask':A,'I_A':str(F(IA,den)),'beta_A':str(F(beta,den)),
             'B_A_nat_coefficients':{str(p):str(F(v,den)) for p,v in B.items()},
             'J_A_nat_coefficients':{str(p):str(F(v,den)) for p,v in J.items()},
             'L_A_over_I_A_bits':c.bits_interval(L,0,IA),
             'U_A_over_I_A_bits':c.bits_interval(B,2*beta,IA),
             'channel_surrogate_minus_J_per_I_A_bits':c.signed_bits_interval({p:-v for p,v in J.items()},2*beta,IA)}
        rows.append(row)
    if named is not None:
        c.ck(c.sign(c.combine(H,L,IA,-I))>0)
    if name=='quadratic_times_PD3':
        A=3;L=c.decrement(t,A,H);B,beta,IA=c.block_stats(weights,A)
        c.ck(c.sign(c.combine(H,L,IA,-I))>0)
    result={'name':name,'n':n,'R_bits':c.bits_interval(H,0,I),'rows':rows}
    if name=='NAND_case_0006':result['tree']=source['cases'][6]['tree']
    results.append(result);c.ck(time.monotonic()-start<55)
c.dump(c.ROOT/'out/CHANNEL_REPRODUCTION.json',{'status':'PASS','helper_version':'A052-joint-channel-reproduction-v1','case_count':len(results),'assertions':c.ASSERTIONS+1,'runtime_seconds':time.monotonic()-start,'cases':results})
print(json.dumps({'status':'PASS','cases':len(results),'assertions':c.ASSERTIONS,'runtime_seconds':time.monotonic()-start}))
