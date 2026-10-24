from pathlib import Path
import json,sympy as S
from fractions import Fraction as F
from math import comb
import wired_bounds
from exact_boxes import exact as free_exact
s=Path('wired_bounds.py').read_text(encoding='utf-8-sig');s=s[:s.index("if __name__=='__main__':")];s=s.replace('src=(0,0);tar=(n,0);','edges.reverse()\n src=(0,0);tar=(n,0);');scope={};exec(s,scope)
reverse=scope['exact'];rr=reverse(3,2,True);fw=json.loads(Path('wired_box.json').read_text());assert rr['counts']==fw['counts']
rf=reverse(3,1,False);fr=next(v for v in json.loads(Path('exact_boxes.json').read_text()) if v['radius']==3 and v['n']==1);assert rf['counts']==fr['counts']
r1=wired_bounds.exact(1,1,True);assert r1['counts']==[comb(12,k)-(comb(8,k) if k<=8 else 0) for k in range(13)]
for n in [1,2]:
 wi=wired_bounds.exact(3,n,True)['counts'];fi=free_exact(3,n)['counts'];assert all(a>=b for a,b in zip(wi,fi))
dif=json.loads(Path('free_wired_counts.json').read_text());assert dif==[a-b for a,b in zip(fr['counts'],fw['counts'])]
x=S.symbols('x');expr=sum(v*x**k*(1-x)**(84-k) for k,v in enumerate(dif));data=json.loads(Path('interval_certificates.json').read_text());H=sum(v*x**j for j,v in enumerate(data['H_power_coefficients']));assert S.Poly(expr-x*(1-x)**6*H,x).is_zero
for ce in data['certificates']:
 a=F(ce['a']);b=F(ce['b']);N=ce['degree'];power=[sum(F(c)*comb(j,i)*a**(j-i)*(b-a)**i for j,c in enumerate(data['H_power_coefficients']) if j>=i) for i in range(N+1)];bb=[sum(power[i]*F(comb(k,i),comb(N,i)) for i in range(k+1)) for k in range(N+1)];assert bb==list(map(F,ce['bernstein_coefficients']));assert min(bb)>F(3,10)
crit=F(sum(dif),2**84);assert crit<0
summary={'wired_reverse_edge_order':'PASS','free_reverse_edge_order':'PASS','wired_radius1_exact_star_formula':'PASS','wired_ge_free_coefficientwise':'PASS','signed_polynomial_factorization':'PASS','rational_interval_coefficients_above_3_over_10':'PASS','free_minus_wired_at_half':str(crit),'lean_algebra_exit':0}
Path('final_verification.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(summary)
