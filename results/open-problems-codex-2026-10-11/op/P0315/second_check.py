import sympy as S,mpmath as mp,pathlib,json
b,r,z=S.symbols('b r z',nonzero=True);I=S.I
a=1+2/b;d=a*(4/b-1);e=-a*(4/b+1)
F=1+a*(z-z**-1)/(I*r)+d*(z+z**-1)/r**2+e*(z**2+z**-2)/r**2
D=lambda f:I*z*S.diff(f,z)
co=(z+z**-1)/2;si=(z-z**-1)/(2*I)
res=S.diff(F,r)+D(F)-(4/b*D(D((1-co)*F))+2*D(si*F))/r
zs=[(4/b-2)*d-(2/b-1)*e,(16/b-2)*e-(8/b+2)*d,-(18/b+3)*e]
target=sum(v*(z**(j+1)+z**(-j-1)) for j,v in enumerate(zs))/r**3
assert S.factor(res-target)==0
mp.mp.dps=50
rows=[];worst=mp.mpf('-inf')
for bv in ['0.01','0.1','0.25','0.3333333333333333333333333','0.4','0.49','0.7','0.99']:
 beta=mp.mpf(bv);p=beta/2 if beta<=mp.mpf(1)/3 else (1-beta)/4
 kap=4*p*(1-beta-2*p)/beta
 assert p>0 and 2*p<=beta and beta+2*p<1 and 0<kap<2
 slack_min=mp.inf
 for j in range(65):
  th=2*mp.pi*j/64
  for k in range(65):
   ph=2*mp.pi*k/64
   actual=p*((p-1)+p*mp.cos(th-ph)-beta/2*(mp.cos(th)+mp.cos(ph)))
   upper=-p*(1-beta-2*p)
   slack_min=min(slack_min,upper-actual)
 assert slack_min>=-mp.mpf('1e-45')
 av=1+2/beta;dv=av*(4/beta-1);ev=-av*(4/beta+1)
 R=max(1,8*av,mp.sqrt(8*(abs(dv)+abs(ev))))
 minF=min(1+2*av*mp.sin(2*mp.pi*j/1000)/R+2*(dv*mp.cos(2*mp.pi*j/1000)+ev*mp.cos(4*mp.pi*j/1000))/R**2 for j in range(1001))
 assert minF>=mp.mpf('0.5')
 rows.append({'beta':str(beta),'p':str(p),'kappa':str(kap),'previous_QV_exponent':str(beta/2),'minimum_generator_slack':str(slack_min),'R':str(R),'minimum_parametrix_bracket_at_R':str(minF)})
pathlib.Path('second_checks.json').write_text(json.dumps({'exact_residual_identity':'symbolically verified in Laurent polynomials','residual_coefficients':[str(S.factor(v)) for v in zs],'generator_grid':rows,'angular_pairs_per_beta':4225},indent=2),encoding='utf8')
print('Exact Fokker-Planck residual identity passed; 33800 generator checks and positivity grids passed.')
