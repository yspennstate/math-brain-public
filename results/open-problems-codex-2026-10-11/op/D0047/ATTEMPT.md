# D0047 mathematical attempt

Date: 2026-10-12. Verdict: PARTIAL. Virág's Question 9 is not solved here.

## 1. Exact question and concrete target

Source: Virág, *Operator limits of random matrices*, Question 9, PDF p. 25:

> Can one deduce the gap Painlevé equation from the PDE’s corresponding to the generator of the Brownian carousel SDE?

The source question does not explicitly restrict beta or specify the Painlevé equation. Its carousel has beta>0 and mean spacing 2pi. Put c=beta/4 and L=2pi. For lambda>=0,

    d alpha_t = c lambda exp(-ct) dt + 2 sin(alpha_t/2) dB_t,
    alpha_0=0.

By source Proposition 12.1, G_beta(lambda)=P(alpha_infinity=0) is the probability of no Sine_beta point in [0,lambda]. A concrete classical beta=2 target is, with r=lambda/2,

    Sigma(r)=r d/dr log G_2(2r),
    (r Sigma'')^2 + 4(r Sigma'-Sigma)(r Sigma'-Sigma+(Sigma')^2)=0.       (PV)

Beta=2 is a chosen classical subtarget, not a hypothesis attributed to Question 9. A proof of (PV) by an unrelated determinant argument does not answer the requested generator derivation.

## 2. Proved reduction: a stopped-phase and discounted-hitting identity

For s>=0 and theta in [0,L], let A solve the same SDE with lambda=s and A_0=theta. Set

    tau=inf{t>=0:A_t=L},       exp(-c infinity)=0,
    X_t=A_(t wedge tau),
    H(s,theta)=P(X_infinity=0),
    V(s,theta)=E exp(-c tau).

The coefficients are globally Lipschitz in A with bounded diffusion, so the strong solution exists for all finite times. Comparison with the identically zero solution having zero drift gives A_t>=0. The same comparison, applied after a hit of L to the constant solution L with zero drift, gives A_t>=L thereafter. These are the usual one-dimensional comparison inequalities: the diffusion difference is Lipschitz, its local time at zero vanishes, and applying Tanaka's formula to the negative part of the difference and Gronwall proves the inequality. Consequently 0<=X_t<=L.

Claim:

    H(s,theta)=1-(theta+s)/L+(s/L)V(s,theta).                          (1)
    G_beta(s)=H(s,0)=1-s/L+(s/L)V(s,0).                              (2)

Proof. The stopped equation is

    X_t=theta + cs integral_0^t exp(-cu) 1_{u<tau} du + M_t,
    M_t=integral_0^(t wedge tau) 2 sin(A_u/2) dB_u.

For every finite t this stochastic integral is square integrable. Moreover |M_t|<=L+theta+s pathwise, because X_t is bounded and the accumulated drift is between zero and s. Hence the martingale is uniformly bounded in L2, converges almost surely and in L2, and its quadratic variation has finite expectation in the limit by the Ito isometry. The drift also converges, so X_t has a limit. If tau is finite this limit is L. On tau=infinity, if the limit lay strictly inside (0,L), continuity of the diffusion coefficient would bound its square below by a positive constant at all sufficiently late times, giving infinite quadratic variation. This contradicts its almost-sure finiteness. Thus X_infinity belongs to {0,L}.

Taking expectations in the stopped equation and using bounded convergence gives

    E X_infinity=theta+s E[1-exp(-c tau)]=theta+s-s V(s,theta).

Since P(X_infinity=0)=1-E X_infinity/L, this proves (1). If theta=0, after any finite hit of L the unstopped phase never returns below L, so its terminal value cannot be zero. If there is no hit, the stopped and unstopped processes agree. The source terminal-winding identification therefore gives (2). QED.

A finite-horizon version, proved by the same expectation calculation, is

    E[1-X_T/L]
      =1-theta/L-(s/L) E[1-exp(-c(T wedge tau))],                     (3)

and it converges to H by bounded convergence. This fixes the probabilistic selection without assuming any regularity at the degenerate entrance. The payoff is a ramp on [0,L], not the indicator of avoiding L until T.

Immediate bounds are

    max(0,1-(theta+s)/L)<=H(s,theta)<=1-theta/L,
    max(0,1-s/L)<=G_beta(s)<=1.

These bounds/reductions are not new-literature claims; they are proved here from the stopped SDE.

## 3. Proved boundary case and a warning about finite-time killing

At s=0, X is a bounded martingale. Section 2 shows that it converges to 0 or L, and E X_infinity=theta. Therefore

    H(0,theta)=1-theta/L.                                           (4)

For 0<theta<L neither endpoint is reached at finite time. Here is a direct check. Until any putative endpoint hit, apply Ito to Z=log tan(A/4). Its derivatives give

    dZ=dB-(1/2) cos(A/2) dt.

The drift is bounded by 1/2. On each finite interval the Brownian motion and this drift integral are finite and continuous; Z cannot tend to plus or minus infinity there. An endpoint hit would force precisely such divergence, so it is impossible. It follows that V(0,theta)=0 and P(tau=infinity)=1 for every interior theta, whereas H(0,theta)=1-theta/L<1.

This is an exact counterexample to replacing the terminal-zero boundary data by pure finite-time survival boundary data. It is NOT a counterexample to Virág's question. No equality or inequality between those events at every positive s is asserted here beyond their definitions.

## 4. Generator and transform: what is proved and what requires regularity

For the Markov state R_t=s exp(-ct), A_t, Ito's formula on a C2 test function gives

    mathcal L=-cs partial_s + cs partial_theta
                  +(1-cos theta) partial_thetatheta.                (5)

The coefficient 1-cos theta is half the square of 2 sin(theta/2). For smooth harmonic representatives H, the backward equation is

    -cs H_s+cs H_theta+(1-cos theta)H_thetatheta=0.                   (6)

The probabilistically selected H has the stopped Markov mean-value property. Equation (6) is used below only wherever sufficient differentiability holds; no unproved differentiability of all boundary jets of physical H is assumed. Interior regularity can also be treated using standard local parabolic theory after changing from s to log s, but that theorem is not re-proved here.

For any smooth V and H=1-(theta+s)/L+(s/L)V, direct differentiation proves the operator identity

    mathcal L H=(s/L)(mathcal L V-cV).                               (7)

Thus the discounted-hitting formulation corresponds to mathcal L V=cV, with V(s,L)=1 and V(0,theta)=0 for interior theta. Conversely (7) holds algebraically even before any probabilistic regularity theorem. It exposes a particular missing object: a closed identity for the discounted hitting transform V(s,0) would close the original gap problem through (2).

For x=cot(theta/2), dx/dtheta=-(1+x^2)/2 and d2x/dtheta2=x(1+x^2)/2. Also 1-cos theta=2/(1+x^2). Substitution into (6), without dropping any drift term, gives for U(s,x)=H(s,theta(x))

    (beta/2)s U_s=(1+x^2)U_xx
           +[2x-(beta/4)s(1+x^2)]U_x.                              (8)

At beta=2 this agrees with the earlier attempts. The endpoint profile (4) becomes

    U(0,x)=1/2+arctan(x)/pi,
    U(s,-infinity)=0,    U(s,+infinity)=G_beta(s)

when those endpoint limits exist. In particular (4), not a constant-one survival profile, is the correct zero-drift profile.

## 5. Proved formal obstruction: the finite boundary-jet equations do not close

This statement concerns formal jets, NOT arbitrary globally bounded solutions.

Let c>0 and I be any open interval contained in (0,infinity). Choose an arbitrary C-infinity function g on I. Let w_n(s) stand for the formal theta derivative of order n at theta=0. Put w_0=g and define successively

    w_(n+1)=w_n'-(1/(cs)) sum_(k=2)^n binom(n,k) d_k w_(n-k+2),       (9)
    d_(2j)=(-1)^(j+1),  d_(2j+1)=0.

An empty sum is zero. Then there exists a UNIQUE sequence of smooth formal jets satisfying w_0=g and all differentiated boundary equations from (6).

Proof. The theta derivatives of D(theta)=1-cos theta satisfy D(0)=D'(0)=0 and D^(k)(0)=d_k for k>=2. Leibniz's rule applied n times to (6) at theta=0 gives exactly

    cs(w_(n+1)-w_n') + sum_(k=2)^n binom(n,k)d_k w_(n-k+2)=0.        (10)

Every index in the sum is at most n. Since cs is nonzero on I, equation (10) determines w_(n+1) uniquely from previously constructed smooth functions and their derivatives; its solution is (9). Starting at w_0=g, induction proves existence, smoothness, and uniqueness for all n. QED.

The first jets are

    w_1=g',
    w_2=g'',
    w_3=g'''-g''/(cs),
    w_4=g''''-4g'''/(cs)+g''/(cs^2)+3g''/(c^2 s^2).

Consequently any finite collection of these differentiated entrance equations is formally consistent with any chosen smooth g. It cannot, by itself, force a nontrivial differential equation on g. This does not forbid closure using the far boundary, positivity, global selection, convergence of the formal theta series, or coupled generators. Those are information absent from this lemma. No claim of convergence or of an actual global PDE solution for arbitrary g is made.

The nonzero-coefficient algebraic step is formalized in BoundaryAlgebra.lean. The induction and differentiation above are ordinary written proofs, not claimed Lean formalizations.

## 6. Hostile check of the earlier PV branch-selection claim

For every constant a, Sigma(r)=-ar is an EXACT solution of (PV): Sigma'=-a, Sigma''=0 and r Sigma'-Sigma=0, so both terms of (PV) vanish. Hence

    G_fake(2r)=exp(-ar)

has G_fake(0)=1 and Sigma/r -> -a. Taking a=1/pi gives precisely the source's mean-spacing slope G_fake'(0)=-1/(2pi). Thus (PV), normalization at zero, and intensity slope ALONE do not identify the physical solution. This disproves that proposed selection shortcut, not (PV) for the true gap. The cancellation is also kernel-checked in BoundaryAlgebra.lean.

To verify that this fake branch is different from the actual beta=2 gap, one may use the independently known determinantal identification as an EXTERNAL check. This subsection is not a carousel-to-PV derivation.

The Sine_2 kernel at density rho=1/(2pi) is

    K(x,y)=sin((x-y)/2)/(pi(x-y)),  K(x,x)=rho.

It is a positive Gram kernel, since K(x,y)=(1/(2pi)) integral_(-1/2)^(1/2) exp(iu(x-y)) du. Its two-point determinant is

    det_2=rho^2[1-(sin(z/2)/(z/2))^2]
         =rho^2 z^2/12+O(z^4),  z=x-y.

In the Fredholm series on [0,s], the n=1 term is -rho s. The n=2 term is

    (1/2) integral_[0,s]^2 det_2
      =(rho^2/24)(s^4/6)+O(s^6)
      =s^4/(576 pi^2)+O(s^6).

Here integral_[0,s]^2 (x-y)^2=s^4/6, obtained by integrating x^2-2xy+y^2. For each n>=3, the Gram-volume bound gives

    0<=det_n<=rho^(n-2) det_2(x_1,x_2).

Indeed orthogonally project the last n-2 Gram vectors away from the first two: each residual squared norm is <=rho, and their residual Gram determinant is bounded by their product. A singular first-two block follows by continuity. Integrating this inequality and summing the factorial denominators bounds the absolute sum of all n>=3 terms by O(s^5). Therefore, using this external determinantal theorem,

    G_2(s)=1-s/(2pi)+s^4/(576 pi^2)+O(s^5).                         (11)

In contrast exp(-s/(2pi)) has a nonzero positive s^2 coefficient. So the exact fake PV branch is not the physical gap. The needed extra branch data could be, for example, G_2''(0)=0; the mean intensity does not provide it. Formula (11) was not derived from the carousel and is not promoted as a solution of Question 9.

## 7. Previous one-pole Lax work: retained as a lead

The read-only 2026-09-17 reports introduce a real-line one-pole auxiliary Q and an added first-order equation, and report that compatibility yields a sigma-PV equation for its connection coefficient. They explicitly leave unproved the identification of their common Lax/PDE solution with the physical carousel H. Their local compact-x endpoint matching does not control x-infinity while the apparent pole comes from infinity as s decreases to zero. I have not re-proved their entire Lax construction and do not register its formulas as new proved claims.

This run additionally shows that a normalization argument based only on the slope is insufficient even after a sigma-PV identity is known. The linear/exponential branch must be excluded using further generator-side information.

## 8. Original remaining gap (updated by Sections 13–16)

A full affirmative answer still requires a derivation, from the probabilistically selected Brownian-carousel generator problem, of a closed nonlinear ODE for G_2 (at minimum), with all boundary/regularity/branch data justified from that same probabilistic problem. In the previous Lax route this means constructing a globally bounded common solution and proving that it equals H selected by (1)-(3), then supplying the branch data. The additional attempt in Sections 13–15 now supplies a generator-side vanishing quadratic remainder and excludes the exponential branch, while physical selection remains unproved. Neither compatibility of a formal added Lax equation nor the formal jet lemma performs that selection.

A concrete alternative is to derive the requisite closed differential identities for V(s,0)=E exp(-c tau), whose precise connection to the gap is (2). No such closure is proved here. No counterexample to the possibility of a generator derivation is proved here.

## 9. Verification obligations

- Terminal-zero versus finite-time survival: distinguished explicitly and disproved as interchangeable at the zero-drift interior boundary by the bounded Lamperti SDE.
- Optional stopping at infinite time: not used without bounds; all limits use the bounded stopped process and the uniformly L2-bounded martingale.
- Endpoint quantization: proved for the stopped process using finite quadratic variation, not assumed for arbitrary initial theta.
- PDE regularity at theta=0: not assumed for the physical probability; the jet theorem is explicitly formal.
- Arbitrary boundary trace: not asserted to extend globally; only formal differentiated PDE equations are solved.
- Painlevé normalization: r=s/2 at beta=2, with a=1/pi. The linear branch obeys the exact displayed PV equation.
- Determinantal calculation: explicitly external, used only to distinguish the physical gap from an exact fake PV solution.
- Lean: only the two finite algebraic statements are claimed checked if lean_check.txt records exit 0; no analytic/stochastic proof is claimed formalized.

Computational outputs and final Lean outcome are recorded in checks.txt and lean_check.txt. Literature coverage limitations, including API rate limits, are in LITERATURE.md.

## 10. Executed computational checks

check_math.py ran successfully. SymPy verified (7), the cotangent generator map, twelve successive jet equations, the explicit fourth jet, and the exact linear-sigma cancellation. A trace with the same entrance slope, G(2r)=exp(-ar-4r^2), gives Sigma=-ar-8r^2 and nonzero PV residual -32r^2(a^2+32ar+248r^2-8). This illustrates the formal-jet theorem; it is not a globally selected carousel solution.

A 64-node Gauss-Legendre Nystrom determinant check gave the following quartic correction ratios (G_2(s)-1+s/(2pi))/s^4: 0.000175811053493 at s=0.2, 0.000175319876437 at s=0.5, and 0.000173581504594 at s=1. The predicted limiting coefficient is 1/(576pi^2)=0.000175904832712. These are numerical consistency checks only, with no certified rounding-error enclosure. Each matrix was 64 by 64 and used negligible memory relative to the 1 GB limit. Exact algebra, rather than these floating-point values, supports the proved claims.

## 11. Final formal-verification outcome

The final `lake env lean ~/brain_workers/TRIO_1011/op/D0047/BoundaryAlgebra.lean` invocation, run from ~/lean_verify with a 3600-second subprocess timeout, returned exit code 0. Lean kernel-checked triangular_jet_step and linear_sigma_branch. The file imports only Real.Basic and the required field_simp, linarith, and ring tactics, and contains no sorry or native_decide. Earlier encoding/import failures were corrected before this successful run. The stochastic and analytic statements remain written proofs, not Lean-verified theorems.

## 12. Additional serious attempt: two routes and the chosen one

Reopened at the user's request on 2026-10-12. The two unexecuted routes were written in NEW_APPROACHES.md before pursuing either: (A) quantitative discounted first-hitting estimates; (B) adjoint propagation of the one-pole Lax residual. Route A is pursued below. Route B remains a proposal, not a proved selection argument.

The brain was asked for the gap using "Painleve V isomonodromy connection Fokker Planck Rumanov boundary selection" and "Brownian carousel discounted hitting time Girsanov small gap level repulsion". No source-specific selection theorem was returned. A follow-up recall on geometric-Brownian characteristic roots supplies only a hint for the power test function below; the calculation and stopping proof are checked independently.

## 13. New proved generator-side small-gap bound

The notation is that of Section 2, with theta=0, c=beta/4>0, L=2pi, X_t=A_(t wedge tau), and V(s,0)=E exp(-c tau). Define

    p=min(2, (1+sqrt(1+8c))/2).

Then 1<p<=2 and p(p-1)/2<=c. Indeed the positive root q=(1+sqrt(1+8c))/2 satisfies q(q-1)/2=c and q>1; if q<=2 take p=q, while if q>=2 then c>=1 and p=2 gives p(p-1)/2=1<=c. For every s>=0,

    0<=G_beta(s)-1+s/L <= (s/L)^(p+1)/(p+1).                       (12)

In particular, at beta=2 take p=(1+sqrt(5))/2. The remainder is O(s^((3+sqrt(5))/2)), hence o(s^2). This is proved directly from the carousel SDE; no determinantal identification or Painleve equation is used.

Proof of the moment estimate. The stopped first-moment equation gives

    0<=E X_t=cs integral_0^t exp(-cu)P(u<tau)du
               <=s(1-exp(-ct)).                                    (13)

For 1<p<=2, the function x^p is C1 on [0,infinity) but may not be C2 at zero. To avoid assuming Ito's formula there, use f_epsilon(x)=(x+epsilon)^p, epsilon>0, in the stopped discounted Ito formula up to T wedge tau. The terminal term is exp(-c(T wedge tau))f_epsilon(X_T). All stochastic integrands are bounded on [0,T] for fixed epsilon since 0<=X<=L; thus their expectations vanish. As epsilon decreases to zero, every term converges by dominated convergence: the first-derivative term is bounded by p(L+1)^(p-1), the potential term by c(L+1)^p, and the second-derivative term satisfies

    2p(p-1)sin^2(x/2)(x+epsilon)^(p-2)
        <=(p(p-1)/2)x^p,  0<=x<=L,

using 4sin^2(x/2)<=x^2 and p-2<=0. At x=0 the left side is zero. The starting value epsilon^p tends to zero. Therefore the exact limiting discounted Ito identity is valid for x^p and yields

    E[exp(-c(T wedge tau))X_T^p]
     =E integral_0^(T wedge tau) exp(-ct)
          [pc s exp(-ct)X_t^(p-1)
            +2p(p-1)sin^2(X_t/2)X_t^(p-2)-cX_t^p]dt.

The last two terms together are <=0 because p(p-1)/2<=c. The expression at X_t=0 is defined by its continuous zero limit. Consequently

    E[exp(-c(T wedge tau))X_T^p]
      <=pc s integral_0^T exp(-2ct)
                    E[X_t^(p-1)1_{t<tau}]dt
      <=pc s integral_0^T exp(-2ct)(E X_t)^(p-1)dt.                  (14)

The last inequality first drops the indicator (the random variable is nonnegative), then uses concavity of x^(p-1), since 0<p-1<=1. Substitute (13). As T tends to infinity, the left side tends by bounded convergence to L^p E exp(-c tau): on tau<infinity it is eventually L^p exp(-c tau), while on tau=infinity it tends to zero because X_T<=L and exp(-cT) tends to zero. The nonnegative upper integral converges monotonically, giving

    L^p V(s,0)
      <=pc s^p integral_0^infinity exp(-2ct)(1-exp(-ct))^(p-1)dt
      =p s^p integral_0^1 u(1-u)^(p-1)du
      =s^p/(p+1).                                                  (15)

For the last equality, put v=1-u and integrate v^(p-1)-v^p: the integral is 1/p-1/(p+1)=1/[p(p+1)]. Section 2 gives G_beta(s)-1+s/L=(s/L)V(s,0)>=0, so (15) proves (12). QED.

Referee points. The terminal discount is stopped at T wedge tau, not merely at T; using exp(-cT) after a finite hit would erase the hitting transform and invalidate the proof. The random variables used for concavity are X_t including its constant post-hit value L; dropping the pre-hit indicator only increases the upper bound. All constants remain independent of s and T. The nonsmooth-power step is explicitly justified by epsilon regularization, and the singular second derivative is compensated by the squared diffusion coefficient.

## 14. The exponential branch is now excluded without a determinant

For the fake branch exp(-s/L), Taylor's theorem gives

    exp(-s/L)-1+s/L = s^2/(2L^2)+O(s^3).

In contrast (12), with p>1, gives

    lim_(s downarrow 0) [G_beta(s)-1+s/L]/s^2=0.                    (16)

The functions therefore differ for all sufficiently small positive s, for every beta>0. At beta=2 this rejects precisely the linear-sigma branch recorded in Section 6, using only generator-side probabilistic information. No existence of a classical second derivative of G_beta at zero is asserted solely from the remainder bound: (16) is a Peano quadratic datum. If an analytic candidate gap is to equal the physical gap, its quadratic Taylor coefficient must be zero.

This removes the previously missing branch datum at quadratic order. The central physical/Lax selection and nonlinear closure are still unproved.

## 15. Proved local branch uniqueness, conditional on sigma-PV

This section gives a precise local selection consequence of the new generator-side datum. It does not derive sigma-PV for the physical gap.

Fix a nonzero real a. For a formal power series Sigma(r)=-ar+b r^2+O(r^3), the coefficient of r^2 in the sigma-PV residual is

    4b(b+a^2).                                                     (17)

Proof: rSigma''=2br+O(r^2), so its square contributes 4b^2 r^2; rSigma'-Sigma=br^2+O(r^3), and (Sigma')^2=a^2+O(r), so the other term contributes 4ba^2 r^2. Thus b=0 or b=-a^2 for every formal solution. QED.

There is at most one formal solution in each of these two sectors. In the b=0 sector the solution is exactly -ar. To see this, if a solution differed from -ar first at order n>=3, write its difference as d r^n+O(r^(n+1)), d nonzero. The square term of the PV residual starts at order 2n-2>n, while the product term at order n is 4a^2(n-1)d r^n, which is nonzero. This contradicts PV. Thus all higher coefficients vanish.

In the b=-a^2 sector suppose two solutions differed first at order n>=3, with difference d r^n. For either base solution,

    rSigma''=-2a^2 r+O(r^2),
    A=rSigma'-Sigma=-a^2 r^2+O(r^3),
    B=A+(Sigma')^2=a^2+O(r).

The changes are delta(rSigma'')=n(n-1)d r^(n-1)+O(r^n), delta A=(n-1)d r^n+O(r^(n+1)), and delta B=O(r^(n-1)). Therefore the first term in the residual changes at order n by -4a^2 n(n-1)d r^n. The second term changes there by 4a^2(n-1)d r^n; the contribution A delta B is only order n+1. Quadratic changes have order at least n+1 because n>=3. Thus the residual difference has coefficient

    -4a^2(n-1)^2 d                                                (18)

at r^n. This is nonzero, a contradiction. QED.

The same coefficient proves existence of a unique FORMAL series in the nonlinear sector: after the first two coefficients, at every order n>=3 the new coefficient appears linearly with the nonzero multiplier (18); choose it to cancel the residual at that order. Adding a term at order n does not alter previously canceled residual coefficients, by the same order calculation. This recursively constructs the unique formal solution. Convergence is not proved here.

Now let F(r) be an analytic candidate for G_2(2r), with F(0)=1, slope F'(0)=-a where a=1/pi, and satisfying the physical Peano quadratic datum F(r)=1-ar+o(r^2). Analyticity forces its quadratic coefficient to be zero. Since F is nonzero near zero, Sigma=rF'/F is analytic and has

    Sigma=-ar-a^2 r^2+O(r^3).

If this Sigma satisfies PV, it must lie in the unique nonlinear formal sector just proved. Thus there is AT MOST ONE analytic PV gap germ satisfying the generator-side first- and second-order data. Equality of all Taylor coefficients identifies analytic germs. No existence or analyticity of the physical gap has been inferred from the moment bound; this conclusion is explicitly conditional on an analytic PV candidate.

The first coefficients of the formal nonlinear sector are

    Sigma=-ar-a^2r^2-a^3r^3+(a^2/9-a^4)r^4
                  +(5a^3/36-a^5)r^5+O(r^6).

Integrating the formal relation F'/F=Sigma/r, with F(0)=1, gives

    F(r)=1-ar+(a^2/36)r^4+O(r^6).

The coefficient a^2/36 agrees with the independently known beta=2 quartic coefficient after s=2r, but the agreement is a consistency check rather than a derivation for G_2. Higher formal coefficients are saved in new_symbolic_checks.txt.

## 16. Limits of the new route and refined remaining gap

The power-moment method has a transparent ceiling. Its nonpositive discounted generator term requires p(p-1)/2<=c; concavity in (14) requires p<=2. Hence within this particular direct estimate p cannot exceed the value used in (12). At beta=2 it yields exponent (3+sqrt(5))/2, not the sharp exponent 4 or its coefficient. This limitation is a limitation of the chosen bound, not evidence that sharper generator-side estimates are impossible.

The new result closes the specific gap "exclude the exponential sigma-PV branch using source-side information." Together with the formal uniqueness argument it also supplies conditional uniqueness of the analytic nonlinear PV germ. What remains is the principal global selection/closure problem: prove that the physical probabilistically selected carousel H has the extra integrable constraint and yields sigma-PV, or derive equivalent closed identities for its discounted hitting transform. The new moment bound supplies no such constraint. Neither convergence of the formal nonlinear PV series nor global continuation of a compatible Lax solution is proved here. D0047 therefore remains PARTIAL.

## 17. Additional-attempt verification record

check_new_series.py passed exact symbolic checks of (17) and the leading multiplier (18) for n=3,...,10, retaining arbitrary intervening coefficients. It computed the recursively selected nonlinear sigma series through order 9 and the gap candidate through order 7; the latter is 1-ar+a^2r^4/36-a^2r^6/675+O(r^8). The all-orders proof is Section 15, rather than extrapolation from these finite checks.

check_new_moment.py checked the regularized diffusion inequality on a grid of x, epsilon and c, and numerically integrated the elementary beta integral for c=0.01,0.1,0.5,1,2,10. Those checks are consistent with the written bound, but certify no floating-point error interval. The largest quadrature discrepancy was about 2.1e-7 near a weak endpoint singularity; the exact integral evaluation in Section 13 does not depend on numerical quadrature. External Nystrom determinants at s=0.05,0.2,0.5,1 satisfied the new upper bound. At s=0.05 the determinant gap remainder was about 1.10e-9, the proved upper bound 1.22e-6, and the exponential remainder 3.16e-5, confirming numerically that the exponential candidate fails the new bound. The explicit estimates, not numerical results, prove its exclusion. Matrices were at most 64 by 64, and all checks used negligible memory relative to the 1 GB cap.

Boundary and logical checks: beta=0 is excluded because c must be positive for discounted stopping and p>1; the a=0 sector is excluded from formal uniqueness because the leading multipliers would vanish. The power estimate allows s=0 directly. For beta>=4, p=2 and the bound becomes (s/L)^3/3. No derivative bounds are inferred from Peano asymptotics. No actual PDE solution is inferred from the formal PV recurrence. Route B has not been executed and supplies no proved residual equation.

The final SelectionAlgebra.lean run returned exit code 0 from ~/lean_verify, using the required 3600-second timeout. Lean kernel-checked the quadratic-sector factorization, the nonlinear recurrence coefficient identity, and the sign of the discounted power term. The file uses specific Mathlib imports and contains no sorry or native_decide. The stochastic stopping proof and all-orders formal-series argument are written proofs; only those three finite algebraic steps are formalized. See new_lean_check.txt.
