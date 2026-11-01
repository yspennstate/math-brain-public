from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
run=Path(__file__).resolve().parents[1]
src=run/'code/check_quotient.py'; ns={'__file__':str(src)}
exec(compile(src.read_text().split('cases=rows=0')[0],str(src),'exec'),ns)
test,logadd,combine,bound,walsh,bent=[ns[k] for k in ['test','logadd','combine','bound','physical_spectrum','bent']]
started=time.perf_counter(); cases=0
for original_d in [6,8]:
    d=original_d-2; delta0=Q(1,1<<d); theta=Q(1,2); point=theta*delta0; t=Q(1,1<<(d//2))
    for r in [1,2]:
        for mask in range(1<<(1<<r)):
            q=tuple(1 if mask>>x&1 else -1 for x in range(1<<r)); qa=walsh(q); alpha=1-qa[0]
            values=tuple(q[x&((1<<r)-1)] if x>>r==0 else bent(x>>(r+1),d) for x in range(1<<(r+1+d)))
            # First remaining core coordinate is the physical dummy w.
            a=walsh(values); p=[x*x for x in a]; total={}; Ictrl=Q(0)
            for i in range(r):
                bit=1<<i; eq=sum(qa[S]**2 for S in range(1<<r) if S&bit); ei=point*eq; Ictrl+=ei
                test(sum(p[S] for S in range(len(p)) if S&bit)==ei)
                if not ei: continue
                fullD={}; ref={}; upper={}; coarse_ref={}; coarse_upper={}
                for S in range(len(p)):
                    if S&bit: continue
                    rr=p[S]+p[S|bit]; hi=p[S|bit]; key=S&((1<<(r+1))-1); U=S&((1<<r)-1)
                    ref[key]=ref.get(key,Q(0))+rr; upper[key]=upper.get(key,Q(0))+hi
                    coarse_ref[U]=coarse_ref.get(U,Q(0))+rr; coarse_upper[U]=coarse_upper.get(U,Q(0))+hi
                    if hi: logadd(fullD,hi/(ei*rr),hi)
                test(sum(ref.values())==1); test(sum(upper.values())==ei)
                def quotient(R,H):
                    result={}
                    for key,rr in R.items():
                        hi=H[key]
                        if hi: logadd(result,hi/(ei*rr),hi)
                    return result
                fineD=quotient(ref,upper); coarseD=quotient(coarse_ref,coarse_upper)
                fineLoss=combine((fullD,1),(fineD,-1)); extraLoss=combine((fineD,1),(coarseD,-1))
                beta=qa[bit]; R=1+delta0*((theta*alpha)**2+(theta*beta)**2-2*theta*alpha); expected={}
                if beta:
                    for sigma in [-1,1]:
                        c=1-2*theta*alpha*sigma*t+delta0*((theta*alpha)**2+(theta*beta)**2)
                        logadd(expected,R/c,delta0*theta*theta*beta*beta*(1+sigma*t)/2)
                test(fineLoss==expected)
                test(bound(fineLoss)[1]<=Q(256,9)*theta**4*delta0**2*beta**2)
                total=combine((total,1),(fineLoss,1))
                if q==(1,1,1,-1):
                    epsilon=(delta0/8)/(1-delta0/4); Dflag={}
                    logadd(Dflag,1/(2*epsilon),Q(1,2)); logadd(Dflag,1/(2*(1-epsilon)),Q(1,2))
                    test(extraLoss==combine((Dflag,point*beta**2)))
            test(bound(total)[1]<=Q(256,9)*theta**2*point*Ictrl)
            cases+=1
test(cases==40)
for original_d in range(6,129,2):
    delta0=Q(1,1<<(original_d-2)); epsilon=(delta0/8)/(1-delta0/4)
    test(epsilon<=delta0/7)
    test(1/(4*epsilon*(1-epsilon))>=7/(4*delta0))
out={'direct_cases':cases,'compressed_AND_cases':62,'assertions':ns['ns']['assertions'],'elapsed_seconds':time.perf_counter()-started,
     'certificate':'Fine partition retains physical dummy Fourier occupancy; old partition additionally loses exact binary flag KL with local rate >=ln(7/(4delta0))/4',
     'arithmetic':'Exact Fraction and prime-log identities; rational enclosure only for bounded fine loss'}
(run/'out/EXPOSURE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
