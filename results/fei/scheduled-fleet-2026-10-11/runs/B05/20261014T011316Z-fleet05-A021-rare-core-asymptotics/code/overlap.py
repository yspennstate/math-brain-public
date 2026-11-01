"""Exact block-category Fourier certificates for arbitrary core bias."""
from check import Q,row,add,gap,erasure,wht,ROOT
from itertools import product
import json,time

def coefficient(pattern,widths,terms):
    return sum((sign*Q(1,1<<sum(widths[i] for i in range(len(widths)) if mask>>i&1)) for sign,mask in terms if pattern&~mask==0),Q(0))

def controller_split(widths,terms0,terms1,minority):
    out={};a_g=2*minority;variance=4*minority*(1-minority)
    for pattern in range(1<<len(widths)):
        mult=1
        for k,width in enumerate(widths):
            if pattern>>k&1:mult*=(1<<width)-1
        if not mult:continue
        x=coefficient(pattern,widths,terms0);y=coefficient(pattern,widths,terms1)
        item=row(x,y)
        if item:
            r,m=item;add(out,r,m*mult*variance)
        item=row(int(pattern==0)-a_g*x,int(pattern==0)-a_g*y)
        if item:
            r,m=item;add(out,r,m*mult)
    return out

start=time.perf_counter();cert=[];direct=0
biases=(Q(1),Q(1,2),Q(1,16),Q(1,1<<32))
for L,R,T,j,minority in product(range(1,3),range(1,3),range(1,3),range(1,4),biases):
    if time.perf_counter()-start>58:raise RuntimeError('Frozen 60-second pilot cap')
    p,q,r=Q(1,1<<L),Q(1,1<<R),Q(1,1<<T)
    eta=p*q*r;e=q+r-q*r-eta;rho=Q(1,1<<(j-1))
    widths=(L,R,T,j-1)
    terms0=((1,7),);terms1=((1,7),(1,10),(1,12),(-1,14),(-1,15))
    ledger=controller_split(widths,terms0,terms1,minority)
    d=rho*e*minority
    lo,hi=gap(ledger,d,6);assert hi<0
    cert.append({'query':'S','L':L,'R':R,'T':T,'remaining_separator':j,'core_minority':str(minority),'gamma':str(e*minority),'contrast':str(eta/e),'d':str(d),'K':6,'gap_upper_ln2':str(hi)})
    # Reconstruct actual small data/controls with a point-defect core.
    if minority==Q(1,16) and j<=2:
        core=(-1,)+(1,)*15;n=L+R+T+j-1
        plus=[];minus=[]
        for x in range(1<<n):
            W=int(x&((1<<L)-1)==0)
            U=int((x>>L)&((1<<R)-1)==0)
            V=int((x>>(L+R))&((1<<T)-1)==0)
            S=int((x>>(L+R+T))==0)
            B=W*U*V;C=int(U or V);A=B+S*(C-B)
            plus.extend(1+A*(g-1) for g in core)
            minus.extend(1+B*(g-1) for g in core)
        assert ledger==erasure(plus,minus);direct+=1

for R,T,j,minority in product(range(1,3),range(1,3),range(1,4),biases):
    if time.perf_counter()-start>58:raise RuntimeError('Frozen 60-second pilot cap')
    r=Q(1,1<<T);rho=Q(1,1<<(j-1))
    ledger=controller_split((j-1,T),((1,2),),((1,2),(1,1),(-1,3)),minority)
    d=rho*(1-r)*minority
    lo,hi=gap(ledger,d,7);assert hi<0
    cert.append({'query':'U_after_S_success','redundant_R_label':R,'total_U_width_for_local_fixture':j,'T':T,'remaining_U':j,'core_minority':str(minority),'gamma':str((1-r)*minority),'contrast':str(r/(1-r)),'d':str(d),'K':7,'gap_upper_ln2':str(hi)})

out={'status':'PASS','separator_K6_cases':96,'union_K7_cases':48,'compressed_vs_actual_Walsh_reconstructions':direct,'core_minority_profiles':[str(x) for x in biases],'minimum_gamma':min((Q(x['gamma']) for x in cert)),'seconds':time.perf_counter()-start,'arithmetic':'exact point-block Fourier categories and Fraction coefficients; same certified log helper as check.py, distinct representation for controller entropy'}
out['minimum_gamma']=str(out['minimum_gamma'])
(ROOT/'out'/'overlap_validation.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'out'/'overlap_certificates.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(out,indent=2))
