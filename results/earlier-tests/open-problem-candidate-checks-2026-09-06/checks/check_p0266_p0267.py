"""Symbolic checks for the scalar critical-noise and Bessel calculations (P0266 and P0267).

For du = (u - u^3) dt + sqrt(2) u^2 dW this checks the generator identities behind the inverse-square
(CIR-type) transform, the action on every power u^p, and the cubic cancellation at p = 2. For the reciprocal of a
four-dimensional Bessel process it checks the cubic drift and the diffusion coefficient, the deterministic clock
change that turns it into the scalar equation, the scalar coercivity and critical-interpolation identities, the
four-dimensional radial heat potential (1 - exp(-r^2/2S))/r^2 with its value at the origin, the Gaussian shell
primitives, the Newton shell expectation, and the finite-time hitting tail coefficient. Four deliberately wrong
variants are rejected: the transform without the Ito correction, a three-dimensional Bessel drift, a missing clock
factor, and the martingale expectation without the loss term.
Symbolic identities do not replace the optional-stopping hypotheses; the argument is in
analyses/P0266_P0267_critical_variational_questions.md.
"""
import json
import sympy as s


def main():
 u,r,S,e=s.symbols('u r S e',positive=True)
 p=s.symbols('p',real=True)
 checks=[]
 def zero(name,expr):
  assert s.simplify(expr)==0,name
  checks.append({'name':name,'pass':True})
 def nonzero(name,expr):
  assert s.simplify(expr)!=0,name
  checks.append({'name':name,'known_bad_rejected':True})
 drift=u-u**3;variance=2*u**4
 def generator(f):return s.diff(f,u)*drift+s.diff(f,u,2)*variance/2
 zero('inverse_square_CIR_drift',generator(u**-2)-(8-2*u**-2))
 zero('inverse_square_diffusion_variance',(s.diff(u**-2,u)*s.sqrt(2)*u**2)**2-8*u**-2)
 zero('all_power_generator',generator(u**p)-(p*u**p+p*(p-2)*u**(p+2)))
 zero('second_power_cubic_cancellation',generator(u**2)-2*u**2)
 z=1/(s.sqrt(2)*r)
 bessel_drift=s.diff(z,r)*s.Rational(3,2)/r+s.diff(z,r,2)/2
 zero('BES4_reciprocal_cubic_drift',bessel_drift+z**3)
 zero('BES4_reciprocal_diffusion',s.diff(z,r)+s.sqrt(2)*z**2)
 zero('deterministic_clock_drift',e*z+e*bessel_drift*e**2-((e*z)-(e*z)**3))
 zero('deterministic_clock_variance',(e*s.diff(z,r)*e)**2-2*(e*z)**4)
 zero('scalar_coercivity',u*(u-(2*u-u**3))-variance/2+u**2)
 zero('critical_interpolation',(2*s.Rational(2,3)-1)*(2+1)-1)
 potential=(1-s.exp(-r*r/(2*S)))/(r*r)
 zero('heat_potential_equation',s.diff(potential,S)-(s.diff(potential,r,2)+3*s.diff(potential,r)/r)/2)
 zero('heat_potential_at_origin',s.limit(potential,r,0)-1/(2*S))
 rho=s.symbols('rho',positive=True)
 inner_primitive=-(rho*rho/(2*S)+1)*s.exp(-rho*rho/(2*S))
 outer_primitive=-s.exp(-rho*rho/(2*S))/(2*S)
 zero('radial_Gaussian_mass_primitive',s.diff(inner_primitive,rho)-rho**3*s.exp(-rho*rho/(2*S))/(2*S*S))
 zero('radial_outer_potential_primitive',s.diff(outer_primitive,rho)-rho*s.exp(-rho*rho/(2*S))/(2*S*S))
 shell=(inner_primitive.subs(rho,r)-inner_primitive.subs(rho,0))/(r*r)-outer_primitive.subs(rho,r)
 zero('Newton_shell_expectation',shell-potential)
 zero('finite_time_hitting_tail_coefficient',1/(r*r)-potential-s.exp(-r*r/(2*S))/(r*r))
 nonzero('omitted_Ito_correction_rejected',s.diff(u**-2,u)*drift-(8-2*u**-2))
 wrong_bessel=s.diff(z,r)/r+s.diff(z,r,2)/2
 nonzero('BES3_instead_of_BES4_rejected',wrong_bessel+z**3)
 nonzero('missing_clock_factor_rejected',e*z+e*bessel_drift-((e*z)-(e*z)**3))
 nonzero('martingale_expectation_without_loss_rejected',1/(r*r)-potential)

 print(json.dumps({'checks':checks,'symbolic_identity_count':sum(x.get('pass',False) for x in checks),
  'known_bad_count':sum(x.get('known_bad_rejected',False) for x in checks)},indent=2))


if __name__=='__main__':main()
