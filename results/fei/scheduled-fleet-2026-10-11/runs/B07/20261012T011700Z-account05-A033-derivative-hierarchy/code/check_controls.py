from pathlib import Path
from fractions import Fraction as F
import json,time,math
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1;assert x
def fwht(v):
    a=v[:];h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return a
def anf(v,n):
    a=v[:]
    for i in range(n):
        for s in range(1<<n):
            if s>>i&1:a[s]^=a[s^(1<<i)]
    return a
def deg(v):return max((s.bit_count() for s,b in enumerate(v) if b),default=-1)
def prodpow(items):
    z=1
    for w,c in items:
        if w:z*=w**(w*c)
    return z
point=[-1]+[1]*7
a=fwht(point);ck(a==[6]+[-2]*7)
ck(sorted(x*x for x in a)==[4]*7+[36])
point_P=anf([int(x<0) for x in point],3);ck(deg(point_P)==3)
for i in range(3):
    dp=anf([int(point[x]!=point[x^(1<<i)]) for x in range(8)],3)
    ck(deg(dp)==2)
    ck(sum(x*x for s,x in enumerate(a) if s>>i&1)==16)
ck(3**9<2**16) # kappa(2)*I-H = 2-(9/8)log2(3)>0.
ck(3**9>2**14) # H(point defect)<3I, without rounded logs.
ck(3**3>2**4) # H(data|selector)<3I_data; kappa(2)<4.
psi=[]
for N in (4,16,64):
    amp=F(1,math.isqrt(N));ck(N*amp**2==1)
    ck(amp**2==F(1,N) and amp**2 not in (0,1))
    ck(N*amp==math.isqrt(N))
    psi.append({'N':N,'amplitude_exact':str(amp),'H_exact_bits':N.bit_length()-1,'I_exact':1,'all_plus_value':math.isqrt(N),'nonzero_square_convolution_at_pair':str(2*amp**2),'fails_kappa2':N>=16,'pivotal_square_exact':str(amp**2)})
stars=[]
for m in range(1,5):
    r=2*m;M=1<<m;N=1<<r;L=4*N
    for kind in ('paired','complete_graph'):
        for c in (0,1):
            Q=[]
            for x in range(N):
                if kind=='paired':q=sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))%2
                else:q=sum(((x>>i)&1)*((x>>j)&1) for i in range(r) for j in range(i+1,r))%2
                Q.append(q^c)
            b=[1-2*q for q in Q];ba=fwht(b);ck(all(abs(z)==M for z in ba))
            beta=F(sum(b),N);ck(abs(beta)==F(1,M))
            f=[1]*(2*N)
            # physical selector is least significant, data index is x>>1.
            for z in range(2*N):f[z]=1-2*((z&1)*Q[z>>1])
            wa=fwht(f);den=(2*N)**2;ws=[z*z for z in wa]
            scaled=[F(w*L,den) for w in ws];ck(all(w.denominator==1 for w in scaled));w=[int(z) for z in scaled]
            ck(sorted(w)==sorted([(M+1)**2,(M-1)**2]+[1]*(2*(N-1))))
            IX=F(sum(s.bit_count()*wt for s,wt in enumerate(w) if False),L)
            # data contribution uses all bits except selector.
            IX=F(sum((s>>1).bit_count()*wt for s,wt in enumerate(w)),L)
            Is=F(sum(wt for s,wt in enumerate(w) if s&1),L)
            ck(IX==F(m,2));ck(Is==(1-beta)/2)
            mz=[sum(w[s] for s in range(2*N) if s&1==z) for z in (0,1)]
            fullprod=prodpow([(wt,1) for wt in w]);margprod=prodpow([(wt,1) for wt in mz])
            # L H(data|selector)=log2(margprod/fullprod), bound 3*m/2.
            ck(margprod**2<=fullprod**2*(1<<(3*m*L)))
            # ordinary full H<=3I including beta negative.
            J=sum(s.bit_count()*wt for s,wt in enumerate(w))
            ck(L**L<=fullprod*(1<<(3*J)))
            fp=anf([int(z<0) for z in f],r+1)
            ck(deg(fp)==3)
            for i in range(r+1):
                di=anf([int(f[x]!=f[x^(1<<i)]) for x in range(2*N)],r+1);ck(deg(di)==2)
            stars.append({'m':m,'quadratic':kind,'constant':c,'beta':str(beta),'I_X':str(IX),'I_selector':str(Is),'conditional_bound':'exact integer-product PASS','full_H_bound':'exact integer-product PASS'})
formula=[]
for m in range(1,41):
    M=1<<m;N=M*M;beta=F(1,M)
    ck(F((M+1)**2+(M-1)**2+2*(N-1),4*N)==1)
    v=(1-beta**2)/2;ck(v<=F(1,2))
    if m>=2:ck(m+1<=F(3*m,2));ck(m+2<=F(3,2)*(m+1-beta))
    formula.append({'m':m,'beta':str(beta),'tail_mass':str(v),'I_X':str(F(m,2))})
tensor_cases=0
for m in (1,2):
    for n in range(4):
        size=1<<n
        for mask in range(1<<size):
            g=[1-2*((mask>>x)&1) for x in range(size)];ga=fwht(g);gw=[a*a for a in ga];ck(sum(gw)==size*size)
            # Exact tensor spectral law verified by separate direct transform.
            r=2*m;N=1<<r
            q=[sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))%2 for x in range(N)]
            star=[1-2*((z&1)*q[z>>1]) for z in range(2*N)];sa=fwht(star)
            mixed=[u*v for u in star for v in g];ma=fwht(mixed)
            ck(ma==[u*v for u in sa for v in ga]);tensor_cases+=1
out={'result':'PASS','helper_version':'phase-controls-star-v1','assertions':checks,'runtime_seconds':time.perf_counter()-t0,'direct_star_cases':len(stars),'formula_cases':len(formula),'tensor_cases':tensor_cases,'psi_controls':psi,'point_defect':{'phase_degree':3,'directional_degree':2,'H':'4-(9/8)log2(3)','I':'3/4','H_over_I':'16/3-(3/2)log2(3)','kappa2_margin':'2-(9/8)log2(3)','exact_margin_certificate':'3^9<2^16'},'stars':stars,'formula':formula}
(R/'out').mkdir(exist_ok=True)
(R/'out/validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('stars','formula')},indent=2))
