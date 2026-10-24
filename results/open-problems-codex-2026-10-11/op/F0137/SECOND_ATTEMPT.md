# Second serious attempt: repeated visits and the auxiliary walk

Research date: 2026-10-11. Original full proofs and source corrections remain in ATTEMPT.md. The unresolved question is a spatial stretched-exponential regeneration-range bound for the complete walk, including paths with repeated departures.

## Two approaches not previously pursued

1. **Green-function-weighted Kalikow auxiliary walk.** Rather than requiring positive drift after each possible finite history (which fails), average all revisits through the killed Green function. For a finite domain U, the auxiliary transition at x is E[G_U(0,x) omega(x,x+e)]/E[G_U(0,x)]. A uniform positive auxiliary drift would imply Kalikow's condition and the needed spatial bound by the established criterion. The Dirichlet integration-by-parts proof of the source's stronger condition uses this construction; the new attempt will derive and examine its exact two-site version, including parameters outside the known sufficient condition. This is the more promising immediately testable route because it sums repeated visits exactly, rather than ignoring them.

2. **Annealed time reversal of finite paths and loop-erased currents.** Derive the exact ratio of a path's annealed likelihood and its reversed likelihood. Interior visit denominators cancel, leaving directed-edge rising-factorial ratios and endpoint factors. Try to use this cancellation on loop-erased slab-crossing paths. The issue to test is whether repeatedly traversed edges wash out the directional likelihood ratio, preventing any uniform exponential tilt. This route differs from the original comparison of self-avoiding paths with a homogeneous walk; it retains every loop before comparing directions. It will be pursued only far enough to establish what the exact finite identity does and does not offer if the first route stalls.

Neither route's desired final implication is assumed. Conditional negative drift is not itself a disproof of the averaged Kalikow condition, and failure of Kalikow's condition would not refute (T′).

## Exact summation of repeated visits in a two-site domain

Fix d≥2. Write p=alpha_1, q=alpha_{1+d}, A=sum_i alpha_i and delta=p-q. Let U={0,z}, z=-e_1, and kill the walk on leaving U. Set

    u=omega(0,z), v=omega(z,0).

These variables are independent with Beta(q,A-q) and Beta(p,A-p) laws. The only way to return to 0 before exit is the two-step loop through z, of quenched probability uv. Hence

    G_U(0,0)=sum_{n≥0}(uv)^n=1/(1-uv),
    G_U(0,z)=u/(1-uv).                                      (S1)

Dirichlet coordinates are strictly between zero and one almost surely, so both quenched quantities are finite. Define

    M_n=E[(uv)^n]=(q)_n(p)_n/(A)_n^2.

The already proved gamma-ratio asymptotic gives M_n~C n^{-kappa_x}, with kappa_x=2A-p-q and C>0. Tonelli gives E G_U(0,0)=sum_n M_n. It is finite exactly when kappa_x>1. In that case E G_U(0,z)≤E G_U(0,0) is finite as well, so the auxiliary transition probabilities are well-defined at both vertices.

The auxiliary projected drift at 0 is therefore

    Dhat_U(0)·e_1
      = [sum_{n≥0} M_n (delta-n)/(A+n)]/[sum_{n≥0} M_n].     (S2)

Proof of the numerator. Expand G in (S1). Since |omega(0,+e_1)-omega(0,-e_1)|≤1 and E G<∞, exchanging the sum and expectation is legitimate by absolute integrability. Weighting row 0 by u^n changes its Dirichlet parameters by adding n to its backward coordinate. The weighted forward and backward means are therefore p/(A+n) and (q+n)/(A+n). Weighting the independent neighboring row by v^n contributes the other factor of M_n. Their difference gives (S2). This is an average over every possible number of loops, not merely a selected history.

For any transverse coordinate whose two weights agree, the corresponding auxiliary drift is zero: the same weighting changes neither of that pair's weights, and their common normalization is A+n.

## A rational obstruction to the unrestricted Kalikow reduction

Choose, for each d≥2,

    alpha_1=2/5, alpha_{1+d}=3/10,
    alpha_i=2/[25(d-1)] for all other indices i.

Thus A=43/50, delta=1/10, the largest opposite-pair weight is p+q=7/10, and kappa=kappa_x=51/50>1. The walk is directionally transient in every direction ell with ell_1>0 by the source's transience theorem. The source sufficient statistic is only 1/10, so its >1 criterion does not apply.

The first three terms of the numerator in (S2) are exactly

    n=0:  5/43,
    n=1: -4500/57319,
    n=2: -3325000/58637337.

Their sum is -1110205/58637337<0. Every later term is strictly negative, since n≥1 implies delta-n<0. Consequently the full numerator is strictly negative, its denominator is finite and strictly positive, and

    Dhat_U(0)=c e_1 for some c<0.                            (S3)

This rules out any condition requiring positive auxiliary drift uniformly over finite connected domains containing 0 in a direction ell with d_alpha·ell>0: such a direction has ell_1>0, and the single domain U already gives Dhat_U(0)·ell=c ell_1<0. The auxiliary-row definition has been checked in Tournier, arXiv:0801.2875, PDF p.14: it is exactly the Green-weighted row used here, for finite U and a starting point with integrable Green function. The uniform positive auxiliary-drift version of Kalikow's condition therefore fails in every direction relevant to the conjecture. It is **not** failure of (T′), which is strictly a different condition. For d≥3 these same parameters even satisfy the known nonzero-speed theorem, since kappa>1 and d_alpha≠0.

The finite certificate is exact; no numerical approximation to an infinite hypergeometric series is required. The strict inequalities delta∈(0,1), kappa_x>1, and a negative three-term sum persist under sufficiently small perturbations. Thus the example is not confined to an equality or nonintegrable endpoint. In the perturbed parameter family the e_1-projected auxiliary drift remains negative; transverse symmetry is needed for the stronger assertion about every positive-drift direction.

## Can summing the whole trap residence repair the sign?

A possible repair is to ignore the negative auxiliary drift at one site and instead sum the drift over the entire two-site residence, defining a jump to the exit position. This also needs checking: a positive original drift does not ensure positive mean exit displacement from a backward-facing local set.

Let H be the first exit time from U. For kappa_x>1, E H<∞ by the exact pair-exit moment result in ATTEMPT.md. The conditional mean increment in environment omega at a site x is d_omega(x)=sum_i omega(x,x+e_i)e_i. Since increments are bounded and H is integrable, bounded stopping followed by dominated convergence gives

    E[X_H·e_1]
      = E[G_U(0,0) d_omega(0)·e_1
           +G_U(0,z) d_omega(z)·e_1].                     (S4)

To spell out the limit: for H∧N, the expected sum of actual increments equals the expected sum of their conditional means. The latter is dominated in absolute value by H; the exit or in-domain position has e_1 coordinate in {-2,-1,0,1}, so the former is bounded by 2 and tends to X_H·e_1. Each occupation term is absolutely integrable because both Green functions have finite means.

Expand (S4) using (S1). At 0, the n-th term is the numerator term of (S2). At z, the factor u^{n+1} changes row 0's backward-weight expectation by (q+n)/(A+n), while v^n changes the neighboring projected mean drift to (delta+n)/(A+n). Thus

    E[X_H·e_1]
      =sum_{n≥0} M_n { (delta-n)/(A+n)
                      +(q+n)(delta+n)/(A+n)^2 }
      =sum_{n≥0} M_n [delta(A+q)+n B]/(A+n)^2,
    B=2delta+q-A.                                         (S5)

The equality of the braces and final numerator follows by expansion: the n² terms cancel. All exchanges are justified as above, so this does not subtract two uncontrolled infinities.

Consider a second explicit family, again in every d≥2:

    p=41/100, q=39/100,
    alpha_i=3/[40(d-1)] for all other directions.

Then A=19/20, delta=1/50>0, kappa_x=kappa=11/10>1 and B=-13/25. For these parameters delta(A+q)+B=-1233/2500<0, so every grouped term in (S5) for n≥1 is negative. The first three grouped terms are exactly

    268/9025,
   -67404/2933125,
   -2713886596/255255203125.

Their sum equals -999842196/255255203125<0 (approximately -0.00391703). The remaining terms are negative, so

    E[X_H·e_1] ≤ -999842196/255255203125 < 0.                (S6)

The same example already has negative auxiliary numerator after two terms: 2/95-4018/45125=-3068/45125<0. Transverse symmetry makes the entire expected exit displacement a negative multiple of e_1. Thus even replacing the whole residence in this deterministic pair by its exit jump does not give a positive annealed mean increment in the positive original-drift direction. This is a counterexample to that particular proposed repair, not to a general adaptive contraction or regeneration construction.

For clarity, the transverse exit means vanish by an exact symmetry, not by treating the projected walk as a fresh one-dimensional walk. For each j≥2, reflecting the j-th coordinate leaves U and the starting point fixed and swaps two equal Dirichlet parameters. It therefore preserves the annealed killed-path law while changing the sign of X_H·e_j. This coordinate is bounded at the first exit, so its expectation exists and equals its own negative, hence is zero.

### Stronger common example with A>1 and two-term certificates

To check that neither failure is an artifact of total Dirichlet weight A≤1, choose

    alpha_1=49/100, alpha_{1+d}=12/25,
    alpha_i=3/[100(d-1)] for every other direction.

Then the transverse total is 3/50, A=103/100>1, delta=1/100>0, and the strongest pair has weight 97/100, larger than every transverse pair. Thus kappa=kappa_x=109/100>1, d_alpha=(1/100)e_1, and M_1=2352/10609. At 0 the first two numerator terms of (S2) sum to

    1/103 - (2352/10609)(99/203)
      = -211939/2153627 < 0.                               (S9)

Every subsequent term is negative because delta<1. Therefore the auxiliary projected drift is negative. For the whole exit jump, C=delta(A+q)=151/10000 and B=2delta+q-A=-53/100. Since C+B=-5149/10000<0, every grouped term for n≥1 in (S5) is negative. Its first two terms sum to

    151/10609 - (2352/10609)(5149/41209)
      = -5887889/437186281 < 0.                             (S10)

Consequently E[X_H·e_1]≤-5887889/437186281<0, and E H<∞. This single explicitly directionally transient family defeats both uniform auxiliary drift and the proposed deterministic-pair exit-jump positivity, with only two terms needed for each rigorous upper certificate. The inequalities are strict. For d≥3 the known velocity theorem still gives nonzero asymptotic speed. This coexistence shows precisely why the local failures cannot be interpreted as a counterexample to the full conjecture.

The sign obstruction also survives the discounted Green-function convention used in Tournier's proof. If G_{U,rho}(0,x)=E_0^omega sum_{n<H} rho^n 1_{X_n=x}, then 0≤G_{U,rho}≤G_U and G_{U,rho}→G_U as rho↑1. Since E G_U<∞, dominated convergence makes both the auxiliary numerator and denominator converge to those above. The limiting denominator is positive and the limiting numerator is strictly negative; hence the discounted auxiliary projected drift is negative for all rho sufficiently close to 1. No difference between regularized and unregularized definitions repairs the example.

### A local acceleration does not change the auxiliary sign

Another natural repair, suggested by the Dirichlet acceleration literature, is to change holding times before applying an auxiliary-drift argument. Here the sign obstruction is invariant under that repair as well, for the usual continuous-time occupation-weighted generator.

Let gamma(omega,x) be any strictly positive finite rate multiplier, and use rates gamma(omega,x)omega(x,x+e) on the killed finite domain U. Conditional on the environment, its jump chain is the same discrete walk. Its expected total occupation time at 0 is G_U(0,0)/gamma(omega,0), since each visit has conditional mean holding time 1/gamma(omega,0). Write D_gamma=E[G_U(0,0)/gamma(omega,0)]. If 0<D_gamma<∞, the standard occupation-weighted auxiliary rate is

    lambda_hat(0,e)
      =E[(G_U(0,0)/gamma(omega,0))
             gamma(omega,0)omega(0,e)]/D_gamma
      =E[G_U(0,0)omega(0,e)]/D_gamma.

Therefore its e_1 drift is the same strictly negative numerator as in (S9), divided by D_gamma>0. This calculation holds even if gamma depends on the rest of the environment; independence is not used in the cancellation. If D_gamma is infinite the auxiliary rate construction is not defined in this form, and no sign or criterion is assigned to it. Thus a legitimate positive finite local acceleration cannot turn this particular auxiliary drift positive. Acceleration may still help through other arguments, such as existence of an invariant measure; those arguments are not refuted.

## Second route: exact time-reversal identity and its obstruction

Let pi=(x_0,...,x_N) be any finite nearest-neighbor path with distinct endpoints u=x_0 and v=x_N. Let n_{x,i} and N_x be its departure counts as in ATTEMPT.md. Write pi^R for the reversed path, started at v. Let bar(i) denote the opposite direction. The iid translation-invariant Dirichlet law has

    P_u(pi)/P_v(pi^R)
      = [(A+N_v)/(A+N_u-1)]
           product_{x,i} (alpha_i)_{n_{x,i}}/
                           (alpha_bar(i))_{n_{x,i}}.        (S7)

All factors are positive. For equal endpoints the prefactor is instead 1.

Proof. The reversed traversal uses the reversed edge (x+e_i,x) as many times as the original uses (x,x+e_i). Its Dirichlet numerator factor is therefore (alpha_bar(i))_{n_{x,i}}, and multiplication over all directed edges gives the displayed numerator ratio. Original departure counts minus arrival counts equal 1 at u, -1 at v, and zero at every other vertex, simply by telescoping the path's visit indicators. Reversal changes its departure counts to those arrival counts. Thus its denominator at u is (A)_{N_u-1}, at v is (A)_{N_v+1}, and elsewhere is unchanged. Dividing reversed by original denominators gives exactly (A+N_v)/(A+N_u-1). If u=v every vertex has equal arrival/departure counts, so there is no endpoint change. This derives (S7) directly from the finite-cylinder formula; it does not invoke a separate theorem about stationary reversed environments.

Group the factors in (S7) by an undirected edge in the e_1 direction. If its forward/backward counts are k_+,k_-, its factor is

    (p)_{k_+}(q)_{k_-}/[(q)_{k_+}(p)_{k_-}].

For k_+=n+1,k_-=n, this factor is (p+n)/(q+n), which approaches 1 with n even if p>q.

To remove the possibility that endpoint factors alone cause this degeneration, construct an explicit family. Starting at 0, for each k=0,...,L-1 make n complete loops k e_1→(k+1)e_1→k e_1, then advance to (k+1)e_1. The path ends at L e_1. Every axial edge has counts n+1 forward and n backward. The start has N_0=n+1, the endpoint has N_{Le_1}=n, and each interior vertex has N_x=2n+1. Hence the endpoint factor in (S7) is 1, and

    P_0(pi_{L,n})/P_{Le_1}(pi_{L,n}^R)
      =[(p+n)/(q+n)]^L.                                    (S8)

Taking n=L gives a ratio tending to exp(p-q) as L→∞, since L log(1+(p-q)/(q+L))→p-q. In particular, its logarithm divided by L tends to zero. There is no fixed c>0 such that every forward-displacing finite path has reversal likelihood ratio at least exp(cL).

This defeats a uniform **individual-path** exponential tilting proof based solely on annealed reversal. It does not bound the sum of path probabilities, which is what the conjecture needs. The exhibited loop-heavy paths have very small cylinder probabilities; their existence is not a lower bound of subexponential order on a wrong-exit event. A more sophisticated summation over currents or loop erasure remains a possible direction, but no such estimate has been proved here.

## Hostile-referee audit and remaining gap

1. The Green-weighted row is not replaced by a fresh-site mean. All repeated loops are summed exactly. Independence is used between the two site rows, never between occupation and a site's outgoing probabilities.
2. For both explicit families kappa_x>1, so the auxiliary denominator and every occupation integral used are finite. An infinite denominator is not assigned an arbitrary drift. This is why the example is not a zero-integrability artifact.
3. Infinite series are handled by a finite **negative upper certificate** and the proved negative sign of every remaining term. Numerical truncation without a tail estimate is not used.
4. The second compressed-jump calculation uses E H<∞ before optional stopping and exchanging occupation sums. No cancellation of undefined infinite expectations occurs.
5. The quantities in (S3) and (S6) are auxiliary drift and a two-site exit displacement. Neither is the asymptotic velocity, a slab-exit probability at scale L, or a regeneration range. Negative signs do not furnish a F0137 counterexample.
6. The construction extends to every d≥2 with explicit transverse weights and fixed A. The statement about every admissible direction uses transverse symmetry; under arbitrary perturbations only the e_1 statement is retained.
7. Reversed path likelihood is evaluated under the same Dirichlet parameter vector at its actual starting endpoint. Formula (S7) is not the law of a reversed stationary environment. Endpoints, departure counts, and the equal-endpoint exception are accounted for explicitly.
8. The likelihood-ratio obstruction has exactly canceled endpoint factors. It therefore reflects heavily traversed edges, not a bookkeeping oversight.
9. Exact Fraction computation in auxiliary_walk.py checks the rational certificates, equality of the two expansions in (S5), four arbitrary looped-path reversal identities, and four saturated path identities. The probabilities are finite path cylinders; none is estimated by a rare-event Monte Carlo run.

The main gap remains a bound on the total probability of repeated-visit backward spatial excursions, or on the full regeneration range. The first route fails as a **universal** reduction because actual Dirichlet examples violate its needed auxiliary-drift premise. Its simple deterministic-pair compression repair also fails. The second route yields an exact identity but no uniform pathwise spatial tilt; controlling the aggregate of loop histories would require an additional argument. No full (T)gamma/(T′) proof or counterexample is claimed.

## Final disposition

The two new routes were pursued through exact auxiliary-drift summation, whole-pair exit compensation, discounting, local acceleration, and finite-path reversal. Five additional auxiliary claims were saved. Exact rational checks passed, and both sequential Lean checks passed: the expanded current file contains nine kernel-checked finite algebraic lemmas. auxiliary_lean_expanded_result.json records the final input hash and scope. The probability and path-counting arguments are written proofs, not Lean formalizations.

Final verdict: **PARTIAL**. The original spatial repeated-visit gap is not closed. The explicit examples refute proposed proof premises, not the F0137 conjecture. No full proof or counterexample to (T)gamma/(T prime) is claimed.
