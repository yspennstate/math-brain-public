from pathlib import Path
helper=Path(__file__).resolve().parents[2]/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(helper.read_text(encoding='utf-8').split("rows=[];candidates=0;sets=0;wins=")[0],str(helper),'exec'))
original_lg=lg
from rigorous_log import lg
log_cases=0
for numerator in range(1,17):
    for denominator in range(1,9):
        x=F(numerator,denominator);lo,hi=lg(x);oldlo,oldhi=original_lg(x)
        ck(lo<=oldhi and oldlo<=hi);log_cases+=1
cases=0;obstruction_cases=0;actual_inputs=0
for a in range(1,65):
    for b in range(3*a,3*a+33):
        n=a+b;rho=2**a*F(3,4)**b;q=F(19,20)**b
        ck(rho<=q);ck(b*q<=10);ck(b*b*q<=400)
        ck(2**(b+1)>=F(16*b*b,9));ck(lg(n)[1]<=F(b+1,2))
        # Direct binomial sum verifies the differentiated moment, independently.
        moment=sum((F(math.comb(b,l)*(b-2*l)**2,2**b*b*2**l) for l in range(b+1)),F(0))
        ck(moment==F(b+8,9)*F(3,4)**b);ck((b+8)*lg(n)[1]*rho<=249);cases+=1
for a in range(3,257):
    singleton=(1-F(1,2**(a-2)))**2;I=1+F(a-1,2**(a-2))
    ck(singleton>=F(1,4));ck(I<=2);ck(singleton/I>=F(1,8));ck(F(4*(a-1),2**(a-1))<=2);obstruction_cases+=1
    if a<=10:
        signs=[(-1 if x&1 else 1)*(1-2*int(x>>1==(1<<(a-1))-1)) for x in range(1<<a)]
        fh=walsh(signs);p=[F(x*x,2**(2*a)) for x in fh]
        ck(p[0]==0);ck(p[1]==singleton);ck(sum(S.bit_count()*z for S,z in enumerate(p))==I);ck(CE(p,p)[1]<=3)
        for i in range(a):ck(any(signs[x]!=signs[x^(1<<i)] for x in range(1<<a)))
        actual_inputs+=len(signs)
source=json.loads((R/'out/check.json').read_text(encoding='utf-8'))
row=next(z for z in source['references'] if z['a']==3 and z['b']==9 and z['H_edge_mask']==0)
original={tuple(map(int,key.split(','))):F(val) for key,val in row['complete_profile_masses'].items()}
projected={S:sum((math.comb(9,l)*original[(S,l)] for l in range(10)),F(0)) for S in range(1,8)}
sectorZ=sum(projected.values());qx=[F(0)]+[projected[S]/sectorZ for S in range(1,8)]
ck(sum(qx)==1);ck(qx[1]==qx[2]==qx[4]);ck(qx[1]<=F(1,3))
signs=[(-1 if x&1 else 1)*(1-2*int(x>>1==3)) for x in range(8)]
p=[F(z*z,64) for z in walsh(signs)];terminal=CE(p,qx);ck(terminal[0]/2>=lg(3)[1]/8)
out={'sector_scalar_cases':cases,'log_cross_checks':log_cases,'all_relevant_obstruction_scalar_cases':obstruction_cases,'actual_core_Boolean_inputs':actual_inputs,'inherited_nonempty_source':[str(z) for z in qx[1:]],'original_projected_sector_F_normalizer':str(sectorZ),'actual_terminal_CE_over_I':outward((terminal[0]/2,terminal[1]/2)),'assertions':assertions,'elapsed_seconds':time.monotonic()-start}
(R/'out/scalar.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
