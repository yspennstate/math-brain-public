# P0177: quantitative large-time classical and free mode locations

## Proved result

Let X have probability law mu, with alpha=E exp(epsilon X^2)<infinity for some epsilon>0. Write m=E X, mu_k=E[(X-m)^k]. Normalize both Brownian convolutions to noise variance t. The classical density and the free density each have a unique global maximizer at sufficiently large t, and

 M_c(t)=m-mu_3/(2t)+(mu_5-6mu_2mu_3)/(8t^2)+O_mu(t^-3),
 M_f(t)=m-3mu_3/t+(5mu_5-22mu_2mu_3)/t^2+O_mu(t^-3).

Both converge to the initial mean. Explicit O(t^-1) bounds with thresholds and constants in epsilon,alpha alone appear at the end. Free global uniqueness actually holds under finite variance at t>7(7+4sqrt(2))Var(X), without a claim of unimodality. All proofs below are complete real-variable arguments using the published Biane parametrization. No novelty assertion is made.


2026-10-11. Exact published question: Hasebe--Ueda, ALEA 15 (2018), 353--374, Problem 4.6, journal p.367 (PDF p.15). Hypothesis (4.13): alpha=integral exp(epsilon x^2) dmu(x)<infinity for some epsilon>0. The classical window is [-sqrt(t)/2,sqrt(t)/2] for t>=36 log(2 alpha)/epsilon. The free question is the sentence "How about free Brownian motion?". We interpret free mode as GLOBAL density maximum; the source Proposition 3.4 rules out eventual unimodality even with this tail assumption.

## Independent global free-mode lemma (first proof)
Center the initial variable X, so E X=0 and E X^2=v. For v=0 the two modes are exactly the mean. Suppose v>0. Use source (2.9)--(2.14), journal pp.356--357: eta_t(u) is continuous, psi_t is a real homeomorphism, and p_t(psi_t(u))=eta_t(u)/(pi t). Set F(u,R)=E[1/(R+(u-X)^2)]. When eta>0, R=eta^2 is the unique positive solution F=1/t, and R<=t.

For t>v, Jensen at u=0 gives F(0,t-v)>=1/t, hence R(0)>=t-v>0. For each fixed delta>0, F(u,delta^2)->0 as |u|->infinity by dominated convergence, so eta_t(u)<delta eventually. Thus eta has a positive attained global maximum. Write its coordinate u* and squared height R*. Then t-v<=R*<=t.

Let B=(sqrt(2)+2)sqrt(v), A=B^2+v. At a global maximizer,
E[(u*-X)^2/(R*+(u*-X)^2)]=1-R*/t<=v/t.
Chebyshev gives P(|X|<=sqrt(2v))>=1/2. If |u*|>sqrt(2v), put a=|u*|-sqrt(2v); using R*<=t gives a^2/[2(t+a^2)]<=v/t. For t>=4v this implies a^2<=2vt/(t-2v)<=4v, hence |u*|<=B.

For z>=0 the exact identity
(1-3z)/(1+z)^3-(1-6z)=z^2(15+17z+6z^2)/(1+z)^3>=0
implies, for every |u|<=B,
E[(R*-3(u-X)^2)/(R*+(u-X)^2)^3]>=R*^-2(1-6A/R*).
If t>7A, then R*>=t-v>6A. Consequently F_uu(u,R*)=-2E[(R*-3(u-X)^2)/(R*+(u-X)^2)^3]<0 throughout [-B,B]. Differentiation is valid because R*>0 and the rational derivatives are bounded functions of u-X. Each global maximizer is interior to {eta>0}; implicit differentiation gives F_u=0 there. A strictly concave differentiable F(.,R*) has at most one stationary point. All global maxima have the same R*, and all lie in [-B,B], so the global maximum is unique. Transport by psi_t proves uniqueness for p_t, without asserting unimodality.

At this maximum put q=u*-X. Stationarity says E[q/(1+q^2/R*)^2]=0. Bounded u* and R*->infinity, together with domination B+|X|, show along any convergent subsequence of u* that its limit is zero; compactness then implies u*->0. The physical mode is M_f=u*+(t/R*)E[q/(1+q^2/R*)], and dominated convergence and t/R*->1 give M_f->0.

If M3=E|X|^3<infinity, D=4(B^3+M3) bounds E|q|^3. Since 0<=1-(1+z)^-2<=2z, stationarity gives |u*|<=2D/R*. The identity E[q/(1+q^2/R*)]=u*-E[q^3/(R*+q^2)] gives
|M_f|<=2D/R*+3tD/R*^2<=16D/t=64(B^3+M3)/t
for t>7A (which implies t>=2v). Translate back to a nonzero mean m by replacing X with X-m. This is an explicit law-dependent O(1/t) estimate under the source hypothesis.

## Progress note
The next steps recorded at this intermediate stage were completed below: classical explicit bound, both expansions with rigorous remainders, numerical checks, literature search. Lean completion is separately recorded.

Operational note: the initial Lean command accidentally wrote Algebra.lean in ~/lean_verify because its working directory applied to the whole shell command. The same file has been saved in this problem folder. No outside file was deleted or modified further; subsequent commands use explicit output paths.

## Classical estimate and full expansions (independent proof)

Write Y=X-m, v=E Y^2, mu_k=E Y^k, M_k=E|Y|^k. All these moments exist under (4.13). Put delta=epsilon/2 and alpha_c=E exp(delta Y^2)<=exp(epsilon m^2)alpha. For v>0 set
T_c=36 log(2 alpha_c)/delta.
For every t>=T_c the classical mode is unique and |M_c(t)-m|<=M_3/t.

Proof. H(h,s)=E[(Y-h) exp(-s(Y-h)^2/2)], s=1/t. The density derivative has the sign of H. For z>=0,
(1-z)exp(-z/2)>=1-3z/2.
For 0<=z<=1 this follows from exp(-z/2)>=1-z/2 after multiplication by 1-z; for z>=1 use exp(-z/2)<=1, reverse the inequality after multiplication by 1-z, and note 1-z>=1-3z/2. Consequently
-H_h=E[(1-s(Y-h)^2)exp(-s(Y-h)^2/2)]>=1-(3s/2)(v+h^2).
Differentiation follows by domination with 1+s(Y-h)^2 on every compact h interval. Apply source Theorem 4.3 and the mode window recorded in Problem 4.6 to the CENTERED law of Y. For t>=T_c it is unimodal and has a mode h_t in [-sqrt(t)/2,sqrt(t)/2]. Jensen gives log(alpha_c)>=delta v, so T_c>=36v. Throughout this interval,
-H_h>=5/8-3v/(2t)>=7/12>1/2.
The differentiable density has H(h_t,s)=0. Also |H(0,s)|<=sM_3/2 from |1-exp(-z)|<=z and E Y=0. Integrating the derivative bound between 0 and h_t gives |h_t|<=2|H(0,s)|<=M_3/t. The critical point is a strict local maximum. A unimodal density with two global maximizers would be constant between them, contradicting strict negativity of H_h near h_t, so this mode is the unique global maximum. This proves the estimate already at the centered source threshold.


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

Finally the physical mode, source (2.14), is
M_f=u+E[q/(r+s q^2)]
=u+u/r-(s/r^2)E q^3+(s^2/r^3)E q^5+O(s^3)
=2u-2v u s+mu_3 s+(2v mu_3-mu_5)s^2+O(s^3).
Substituting u gives -3mu_3 s+(5mu_5-22v mu_3)s^2+O(s^3), as asserted. Translation restores m. There is no interchange with a divergent series and no analyticity assertion for unbounded laws.

For v=0, Y=0 almost surely, the classical law is N(m,t) and the free law is the semicircle of variance t centered at m, so both statements are exact for every t>0. If the initial law is symmetric around m, both densities are symmetric; the established uniqueness forces each sufficiently-large-time global mode to be exactly m. A nonzero third central moment makes the t^-1 order sharp for both models. For example P(Y=-1)=2/3, P(Y=2)=1/3 has v=2, mu_3=2 and gives leading shifts -1/t and -6/t respectively. The factor six describes the leading coefficients, not the full displacement at finite time.

## Scope and remaining gap
These are explicit quantitative estimates and asymptotics for every initial law satisfying the source hypothesis, and the free uniqueness result is stronger (finite variance suffices). No optimal time threshold, optimal bound constant, eventual free unimodality, or claim of novelty is made. The source's open-ended wording does not specify any of those sharper targets. Within the stated task of estimating large-time global mode location, the analytic proof has no remaining gap. Numerical and Lean checks below cover only their stated finite/algebraic portions and do not mechanically verify measure-theoretic analysis.


## Estimates using only the source's epsilon and alpha

Let alpha=E exp(epsilon X^2) and L=log(alpha)/epsilon. Jensen gives E X^2<=L, hence v<=L and epsilon m^2<=log(alpha). Therefore alpha_c<=alpha exp(epsilon m^2)<=alpha^2, and the classical estimate is valid at the explicit source-parameter threshold
 t>=72 log(2alpha^2)/epsilon.
For k>0, maximizing a^k exp(-epsilon a^2) over a>=0 gives
 E|X|^k<=alpha [k/(2e epsilon)]^(k/2).
The maximum occurs at a=sqrt(k/(2epsilon)); its value follows by substitution, with endpoints giving zero for k>0. Using |a-b|^3<=4(|a|^3+|b|^3) and |m|^3<=E|X|^3, set
 Q=8alpha [3/(2e epsilon)]^(3/2),
so M_3<=Q. Hence
 |M_c(t)-m|<=Q/t for t>=72 log(2alpha^2)/epsilon,
 |M_f(t)-m|<=64[(sqrt(2)+2)^3 L^(3/2)+Q]/t for t>7(7+4sqrt(2))L.
If alpha=1, exp(epsilon X^2)>=1 and expectation one force X=0 a.s.; both modes are zero for all t>0. These constants are sufficient estimates and not asserted optimal. They answer the source's estimate request with constants determined by precisely its supplied moment parameters.


## Verification artifacts

The detailed hostile-referee checklist is REFEREE.md. Reproducible computations are check_numeric.py (numerics_atomic.json), check_unbounded.py (numerics_unbounded.json), and check_concavity.py (concavity_stress.json). The last stress test has maximum root residual 5.7e-14. The formalized algebra is Algebra.lean, invoked serially through run_lean.py; final compiler result is in lean_result.txt. These checks corroborate the written proof and do not replace its analytic arguments.


Final disposition, 2026-10-11: SOLVED as quantitative estimates for the full source hypothesis. Algebra.lean passed (exit code 0). The full written proof, hostile audit and numerical checks are complete. No analytical gap remains for the stated estimates. Literature novelty is not certified; sharp constants and optimal transition times were not requested and are not claimed.
