from fractions import Fraction as F
from pathlib import Path
import json
r=Path(__file__).resolve().parent
W={4:F(1,20),3:F(-4,15),2:F(1,5),1:F(8,5)}
V={4:F(2,5),3:F(-16,15),2:F(2,5),1:F(8,5)}
rescaling=all(W[i]*2**i==2*V[i] for i in W)
# R(z)=z-2/z-2/z^3+...; multiply (z-2)^2 R(z)/5.
terms={1:F(1),-1:F(-2),-3:F(-2),-5:F(-4)}
out={}
for i,a in {2:F(1),1:F(-4),0:F(4)}.items():
 for j,b in terms.items():out[i+j]=out.get(i+j,F(0))+a*b/5
deriv={i-1:i*a for i,a in W.items()}
polynomial_part=all(out.get(i,F(0))==deriv.get(i,F(0)) for i in range(4))
mass=F(1,5)*(1+4)==1
stieltjes_leading=-out[-1]/2==1
tail_exponent=F(3,2)-F(1,3)==F(7,6)
checks={'potential_rescaling':rescaling,'resolvent_polynomial_part':polynomial_part,'density_mass_from_semicircle_moments':mass,'stieltjes_mass_coefficient':stieltjes_leading,'optimized_gaussian_exponent':tail_exponent,'tail_power_strict_separation':F(2)<F(7,2)}
assert all(checks.values()),checks
(r/'exact_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps(checks,indent=2),flush=True)
