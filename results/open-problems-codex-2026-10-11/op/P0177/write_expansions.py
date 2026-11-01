import pathlib
text=r'''
## Classical estimate and full expansions (independent proof)

Write Y=X-m, v=E Y^2, mu_k=E Y^k, M_k=E|Y|^k. All these moments exist under (4.13). Put delta=epsilon/2 and alpha_c=E exp(delta Y^2)<=exp(epsilon m^2)alpha. For v>0 set
T_c=max{36 log(2 alpha_c)/delta, 6v, 2M_3/sqrt(v)}.
For every t>=T_c the classical mode is unique and |M_c(t)-m|<=M_3/t.

Proof. H(h,s)=E[(Y-h) exp(-s(Y-h)^2/2)], s=1/t. The density derivative has the sign of H. For z>=0,
(1-z)exp(-z/2)>=1-3z/2.
For 0<=z<=1 this follows from exp(-z/2)>=1-z/2 after multiplication by 1-z; for z>=1 use exp(-z/2)<=1, reverse the inequality after multiplication by 1-z, and note 1-z>=1-3z/2. Consequently for |h|<=sqrt(v),
-H_h=E[(1-s(Y-h)^2)exp(-s(Y-h)^2/2)]>=1-(3s/2)(v+h^2)>=1/2
when t>=6v. Differentiation is justified by Gaussian damping, or dominated convergence using the finite second moment on this compact h interval. Also |H(0,s)|<=sM_3/2 from |1-exp(-z)|<=z. At the stated threshold, this is at most sqrt(v)/4. Integrating H_h<=-1/2 proves H(-sqrt(v),s)>0>H(sqrt(v),s), with exactly one zero h_t inside the interval and |h_t|<=2|H(0,s)|<=M_3/t. This zero is a strict local maximum. The source Theorem 4.3, applied to centered Y at its stated threshold, gives unimodality. Its smooth density and the strict local maximum make h_t its unique global maximum: a unimodal function with two global maximizers would be constant between them, contradicting H_h<0 near h_t. This proves the bound without an implicit-function theorem.

As t tends to infinity,
M_c(t)=m-mu_3/(2t)+(mu_5-6v mu_3)/(8t^2)+O_mu(t^-3).
To prove the remainder, for s>=0 Taylor's theorem gives
exp(-sq^2/2)=1-sq^2/2+s^2q^4/8+rho,
|rho|<=s^3|q|^6/48.
Use q=Y-h_t. The bound h_t=O(s) makes E|q|^7 uniformly bounded. Thus H=0 becomes
0=-h_t-(s/2)(mu_3-3v h_t-h_t^3)+(s^2/8)(mu_5-5mu_4 h_t+10mu_3 h_t^2-10v h_t^3-h_t^5)+O(s^3).
First this yields h_t=-mu_3 s/2+O(s^2). Substitution then yields the displayed second coefficient and O(s^3) remainder. Only a finite seventh moment is used in this expansion once the global mode is identified.

For the free global mode,
M_f(t)=m-3mu_3/t+(5mu_5-22v mu_3)/t^2+O_mu(t^-3).
Here is a complete coefficient and remainder derivation, requiring only M_7<infinity in addition to the preceding finite-variance global lemma. Center to m=0. Let u=u_t, R=R_t be the unique global maximizing coordinate and squared height, s=1/t, r=R/t. We already proved u=O(s) and 1-vs<=r<=1, so r>=1/2 for large t. For q=u-Y, the defining equations are
E[(r+s q^2)^-1]=1, E[q(r+s q^2)^-2]=0.
All E|q|^k, k<=7, are uniformly bounded as s decreases to zero. For every z>=0,
(1+z)^-1=1-z+z^2+rho_1, |rho_1|<=z^3,
(1+z)^-2=1-2z+3z^2+rho_2, |rho_2|<=4z^3.
The first identity has exact remainder -z^3/(1+z); the second bound follows from the third derivative -24/(1+z)^5 and Taylor's integral remainder. Therefore integration with z=s q^2/r is justified with O(s^3) errors (M_6 in the first equation and M_7 in the second and spatial map).

The first equation multiplied by r is
r=1-(s/r)E q^2+(s^2/r^2)E q^4+O(s^3).
Now E q^2=v+u^2=v+O(s^2), E q^4=mu_4+O(s), so initially r=1-vs+O(s^2), then
r=1-vs+(mu_4-v^2)s^2+O(s^3).
In particular 1/r=1+vs+O(s^2), 1/r^2=1+2vs+O(s^2).

Multiplying the second equation by r^2 yields
0=u-(2s/r)E q^3+(3s^2/r^2)E q^5+O(s^3).
Exactly E q^3=u^3+3vu-mu_3 and E q^5=u^5+10vu^3-10mu_3u^2+5mu_4u-mu_5. Hence
0=u+2mu_3 s+2v mu_3 s^2-6v u s-3mu_5 s^2+O(s^3).
It follows first u=-2mu_3 s+O(s^2), then
u=-2mu_3 s+(3mu_5-14v mu_3)s^2+O(s^3).
(The symbol on the left is u; no new variable is introduced.)

Finally the physical mode, source (2.14), is
M_f=u+E[q/(r+s q^2)]
=u+u/r-(s/r^2)E q^3+(s^2/r^3)E q^5+O(s^3)
=2u-2v u s+mu_3 s+(2v mu_3-mu_5)s^2+O(s^3).
Substituting u gives -3mu_3 s+(5mu_5-22v mu_3)s^2+O(s^3), as asserted. Translation restores m. There is no interchange with a divergent series and no analyticity assertion for unbounded laws.

For v=0, Y=0 almost surely, the classical law is N(m,t) and the free law is the semicircle of variance t centered at m, so both statements are exact for every t>0. If the initial law is symmetric around m, both densities are symmetric; the established uniqueness forces each sufficiently-large-time global mode to be exactly m. A nonzero third central moment makes the t^-1 order sharp for both models. For example P(Y=-1)=2/3, P(Y=2)=1/3 has v=2, mu_3=2 and gives leading shifts -1/t and -6/t respectively. The factor six describes the leading coefficients, not the full displacement at finite time.

## Scope and remaining gap
These are explicit quantitative estimates and asymptotics for every initial law satisfying the source hypothesis, and the free uniqueness result is stronger (finite variance suffices). No optimal time threshold, optimal bound constant, eventual free unimodality, or claim of novelty is made. The source's open-ended wording does not specify any of those sharper targets. Within the stated task of estimating large-time global mode location, the analytic proof has no remaining gap. Numerical and Lean checks below cover only their stated finite/algebraic portions and do not mechanically verify measure-theoretic analysis.
'''
with open('ATTEMPT.md','a',encoding='utf8') as f:f.write(text)
print('full expansions saved')
