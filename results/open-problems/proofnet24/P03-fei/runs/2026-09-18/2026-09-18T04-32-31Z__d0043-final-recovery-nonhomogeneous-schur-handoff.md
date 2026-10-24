Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / D0043 — final HARD recovery: full-window Schur complement and the non-Gaussian critical gate

**NO MOVEMENT: `k_exotic^cert: 0 -> 0`; D0043 consecutive unchanged count `4 -> 5`; HARD recovery episodes consumed `1/2 -> 2/2`. This is the final permitted D0043 recovery.**

Methods used exactly as assigned: **B1 CHANGE THE CATEGORY; B18 SAY IT IN ANOTHER LANGUAGE; B23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Source target: Bálint Virág, *Operator limits of random matrices* (ICM 2014), Conjecture 5 (Exotic edge operators), sharpened in Krishnapur--Rider--Virág (KRV), Section 13 / Conjecture 45. The source asks for general-fixed-`beta` tridiagonal-operator convergence at analytic nonregular edges, not only beta=2 eigenvalue asymptotics.

Status after this run: **PARTIAL / source not closed on the bounded 2026-09-18 primary-literature screen**. No claim of worldwide openness or publication novelty is made.

---

## 1. Continuity, repository state, and source/status gate

Canonical active claim entering this run:

`operations/claims/D0043.md`

creation commit `7578fb6bc235056f9d5b9f820d3087af9cc18c48`, blob `fa41e947fd62de7b036ea1a9a9e31c2642e1d18b`.

Newest complete own report entering this run:

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T03-40-49Z__d0043-recovery1-frozen-green-critical-window.md`

creation commit `51f34dc999ae962c669a8681e1cb7bfb7a3a8c03`, blob `5bd2f9708adb64901c9b51c9b1aa274fa20aa21f`, with exact-commit terminal marker `**End of complete run report.**` previously recovered.

I reread/recovered the current root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, current `RESULTS.md` and `QUEUE.md`, the D0043 claim, the newest own report, the D0043 intake/attempt history including `D0043-A001`, and the newest accessible P04/I0101 report for the directed audit. Large root ledgers and policy files are connector-truncated when rendered wholesale; exact target paths and relevant current entries were recovered, but I do **not** claim byte-for-byte manual rendering of every row of those large surfaces.

Retained D0043 history is preserved rather than repaid:

- `D0043-A001`: formal source scaling balance and the origin singularity warning;
- `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264`: the singular origin white-noise form is locally infinitesimally kinetic-form-small;
- `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266`: the continuum exotic form is closed/lower-bounded and has compact resolvent for every finite `k>=1` and fixed beta;
- `P03-D0043-K1-CRITICAL-HESSIAN-GATE-268`: explicit source-admissible quartic, local `s^{-2/3}` susceptibility, and failure of the regular uniform-convexity covariance mechanism;
- `P03-D0043-K1-FROZEN-GREEN-CRITICAL-WINDOW-270`: full frozen lattice quartic dispersion, correlation length of order the entire `n^(1/7)` edge window, and colored frozen Gaussian limit.

Fresh status checks on 2026-09-18:

1. Virág, arXiv:1804.06953, still presents the higher-order family as **Conjecture 5, Exotic edge operators**, and distinguishes it from beta=2 Riemann--Hilbert eigenvalue results.
2. KRV, arXiv:1306.4832, Section 13 / Conjecture 45, still gives the nonregular-edge scaling `m_n ~ n^(1/(4k+3))`, explicitly notes that uniform convexity was essential in the regular proof, and formulates the general-beta exotic operator limit conjecturally.
3. Li--Valkó--Xu, arXiv:2607.08536 (9 July 2026), supplies further ordinary Airy-beta soft-edge/operator results for Laguerre beta ensembles, not a source-matching exotic `k>=1` theorem.
4. A bounded fresh 2026 arXiv/web search for `multicritical beta ensemble`, `general beta`, `stochastic operator`, and `exotic edge` recovered no source-matching general-beta proof for `k>=1`. This is a dated bounded search miss, not a proof of worldwide openness or novelty.

---

## 2. Frozen metric and mandatory recovery state

Frozen metric:

`k_exotic^cert = largest K>=0 for which a source-matching rigorous operator-convergence theorem is known for every 0<=k<=K and every fixed beta>0 in the source setup.`

Before: `0`.
After: `0`.
Movement: **none**.

The regular `k=0` stochastic-Airy theorem remains the supported baseline. The theorem below is for one explicit `k=1` source-admissible potential and is therefore PARTIAL. It does not move the metric.

The previous report consumed recovery 1/2. This invocation executes recovery 2/2. Because the metric remains zero, **both D0043 HARD recoveries are now consumed. No third D0043 recovery is permitted.** The immutable handoff is written separately in this same run, and rotation is attempted after the mathematics and audit below.

---

## 3. Final-recovery idea before calculation

Claim 270 killed the last stationary-block version of the regular-edge proof: for the explicit `k=1` quartic, the correlation length is itself order `m_n=n^(1/7)`, so the edge window cannot be partitioned into blocks that are simultaneously long compared with correlations and short compared with macroscopic coefficient variation.

The final recovery therefore changes category completely.

> Treat the entire `n^(1/7)` window as one nonhomogeneous critical quadratic form, integrate out the hard Hessian mode, derive the resulting fourth-order continuum operator, and ask whether its Gaussian field can already have the weighted-Brownian covariance demanded by KRV.

I tried to make the Gaussian route work before invoking nonlinear terms. It fails for a precise reason: the full-window Hessian produces a nonlocal Green covariance, whereas the KRV integrated white-noise term has a covariance whose mixed derivative is diagonal. More importantly, the failure is not merely an artifact of a bad Gaussian approximation: along the exact soft direction, cubic and quartic terms survive at **order one** under the source `n^(1/7)` scaling. Thus the actual critical-window problem is inherently non-Gaussian before any eventual Gaussianization of the integrated potential.

No finite checker was written for this run. The new result is an analytic theorem with a written derivation; the protocol's exact-artifact requirement for finite claims is not triggered.

---

## 4. Explicit `k=1` model and scaling

Retain the source-admissible quartic from Claim 268:

`V_*(x) = (2/5)x^4 - (16/15)x^3 + (2/5)x^2 + (8/5)x.`

Its equilibrium density is

`rho_*(x) = (8/(5 pi))(1-x)^2 sqrt(1-x^2) 1_{[-1,1]}(x),`

so the right edge has exponent `5/2=2*1+1/2`.

For the KRV local branch, write the right-edge deficit `u` so that

`a+2b=1-u`,

and retain the exact branch expansion from Claim 268:

`s = u^3 - (7/16)u^4 + O(u^6)`.

For the source `k=1` edge scale put

`m=n^(1/7)`, `eps=m^{-1}`, `x=j/m`.

Since `s=j/n=x m^{-6}=eps^6 x`,

`u_j = eps^2 U(x) + O(eps^4)`,

with

`U(x)=x^(1/3)`.

At the precision needed below,

`a_j = -(eps^2/2) U(x) + O(eps^6)`,

`b_j = 1/2 - (eps^2/4) U(x) + O(eps^6)`,

`1-s_j = 1+O(eps^6)`.

The `O(eps^4)` correction in `u(s)` does not affect the order-`eps^4` Schur-complement operator: it can only enter multiplied by an additional derivative-scale `eps^2` or into `u^2` at order `eps^6`.

---

## 5. B1 — change category: exact real-space Hessian, then soft/hard variables

For a Jacobi matrix `T=T(a_j,b_j)`, the exact identities

`tr T^2 = sum_j a_j^2 + 2 sum_j b_j^2`,

`tr T^3 = sum_j a_j^3 + 3 sum_j b_j^2(a_j+a_{j+1})`,

and

`tr T^4 = sum_j (a_j^2+b_{j-1}^2+b_j^2)^2
          +2 sum_j b_j^2(a_j+a_{j+1})^2
          +2 sum_j b_j^2 b_{j+1}^2`

give the full Hessian of

`tr V_*(T) - sum_j c_j log b_j`, `c_j=1-s_j`.

Let `(alpha_j,beta_j)` be a Hessian perturbation. Direct differentiation gives the exact row formulas

`(H alpha)_j =
 (8/5)b_{j-1}^2 alpha_{j-1}
 +(4/5)(6a_j^2-8a_j+4b_{j-1}^2+4b_j^2+1) alpha_j
 +(8/5)b_j^2 alpha_{j+1}
 +(16/5)b_{j-1}(a_{j-1}+2a_j-2) beta_{j-1}
 +(16/5)b_j(2a_j+a_{j+1}-2) beta_j`,

and

`(H beta)_j =
 (16/5)b_j(2a_j+a_{j+1}-2) alpha_j
 +(16/5)b_j(a_j+2a_{j+1}-2) alpha_{j+1}
 +(32/5)b_{j-1}b_j beta_{j-1}
 +{(8/5)[2a_j^2+2a_j a_{j+1}-4a_j+2a_{j+1}^2-4a_{j+1}
          +2b_{j-1}^2+6b_j^2+2b_{j+1}^2+1] + c_j/b_j^2} beta_j
 +(32/5)b_jb_{j+1} beta_{j+1}`.

At the critical constant point `(a,b)=(0,1/2)`, the local zero mode is `(2,1)` and the orthogonal hard mode is `(1,-2)`. Use the orthonormal change of variables

`(alpha,beta)^T = (1/sqrt(5)) [[2,1],[1,-2]] (phi,psi)^T`.

This is the correct category for the full-window limit: `phi` is the critical soft field and `psi` is uniformly massive.

Substitute the varying branch above and Taylor-expand

`f(x±eps)=f±eps f'+eps^2 f''/2±...`.

On any compact subinterval `[delta,R]` with `delta>0`, the transformed Hessian equations, uniformly for smooth bounded jets, are

`S = -(16/5)eps psi'
     + eps^2[-(16/25)phi''+(12/25)psi'']
     + eps^3[-(4/5)U psi'-(8/15)psi''']
     + eps^4[(24/5)U^2 phi-(18/5)U^2 psi
             -(24/25)U phi''+(18/25)U psi''
             -(24/25)U' phi'-(12/25)U' psi'
             -(24/25)U'' phi-(12/25)U'' psi
             -(4/75)phi''''+(1/25)psi'''']
     +O(eps^5)`,

and

`W = 16 psi +(16/5)eps phi'
     +eps^2[4U psi+(12/25)phi''+(66/25)psi'']
     +eps^3[(4/5)U phi'+(4/5)U'phi+(8/15)phi'''
             +(22/5)U'psi]
     +O(eps^4)`,

where `S` and `W` are the soft and hard components of the Hessian output. These formulas retain the derivatives of the *varying coefficients*; simply substituting `u=u(x)` into Claim 270's frozen symbol would miss terms below.

---

## 6. B18 — Schur-complement the hard mode and derive the nonhomogeneous fourth-order operator

Solve the hard equation `W=0` recursively. Because its leading coefficient is `16`, the hard mode is uniquely slaved to the soft mode on every compact `[delta,R]`:

`psi = -(eps/5) phi'
       -(3 eps^2/100) phi''
       -eps^3[(U'/20)phi + phi'''/3000]
       +O(eps^4)`.

The first coefficient cancels the order-`eps` hard forcing; the second cancels the remaining order-`eps^2` forcing; at order `eps^3`, the `U phi'` terms cancel exactly and only the varying-basis term `U' phi` and a small third derivative remain.

Substituting this solution into `S` cancels the apparent order-`eps^2` and order-`eps^3` soft terms. The first nonzero Schur-complement term is

`S_eff = eps^4 L phi + O(eps^5)`,

where

`L phi = (1/25)phi''''
         -(4/5)[U phi'' + U' phi' + U'' phi]
         +(24/5)U^2 phi`.

Equivalently,

`boxed{ L = (1/25)D^4 -(4/5)D(U D) -(4/5)U'' +(24/5)U^2. }`

This formula contains the full derivative correction from the varying critical branch. It is **not** the naive frozen replacement

`(1/25)(D^4-20U D^2+120U^2)`;

the `U'` and `U''` terms are forced by the nonhomogeneous lattice Hessian and by eliminating the hard mode.

For the actual edge profile `U(x)=x^(1/3)`, `U''=-(2/9)x^(-5/3)`, so

`boxed{
 L = (1/25)D^4 -(4/5)D(x^(1/3)D)
     +(8/45)x^(-5/3)+(24/5)x^(2/3).
}`

For compactly supported smooth `phi` away from zero, integration by parts gives the positive quadratic form

`boxed{
 ell[phi]
 = (1/25) int |phi''|^2 dx
  +(4/5) int x^(1/3)|phi'|^2 dx
  +(8/45) int x^(-5/3)|phi|^2 dx
  +(24/5) int x^(2/3)|phi|^2 dx.
}`

Thus the nonhomogeneous continuum Hessian is coercive in the bulk and is more singular at the origin than frozen-symbol substitution suggests.

### What is proved about convergence

Let `H_m^soft` denote the discrete Schur complement after eliminating the hard coordinates on a fixed compact edge interval `[delta,R]`, with mesh `eps=m^{-1}`. The preceding exact row formulas and uniform Taylor remainder give, for every `phi in C_c^infty((delta,R))`,

`eps^{-4} H_m^soft phi_m -> L phi`

uniformly on compact subsets, where `phi_m(j)=phi(j eps)`. The associated quadratic forms converge on this core after the Riemann-sum normalization. This is a deterministic bulk consistency theorem.

I do **not** promote this to a full half-line Mosco/resolvent theorem. At `x=0`, the term `x^{-5/3}|phi|^2` forces `phi(0)=0` for ordinary `H^2` functions of finite energy, but it does not by itself determine a second fourth-order boundary condition. Because Claim 270 shows that correlations at any source cutoff `q_n=o(m_n)` are at least window-scale, the first-coordinate/cutoff boundary layer is not washed out before the bulk limit. Therefore the second boundary condition must be derived from the discrete first-coordinate structure; it cannot honestly be guessed from the bulk differential expression.

This is a new exact boundary-selection obstruction, not a defect hidden by notation.

---

## 7. B23 — the Hessian Gaussian cannot be the KRV weighted-Brownian field

Suppose, only as a quadratic approximation, that the critical soft field were governed by the Gaussian action

`(beta/2) ell[Phi]`.

The correct fluctuation amplitude follows from the discrete scaling. The Hessian is order `eps^4`, there are `m=eps^{-1}` edge sites, and the Gibbs prefactor is `n=m^7=eps^{-7}`. Hence a soft perturbation of size

`phi_j = eps^2 Phi(j eps)`

has order-one quadratic action:

`n * sum_j phi_j (H_m^soft phi)_j ~ O(1)`.

For any legitimate boundary realization `L_B` of the fourth-order bulk operator, the quadratic approximation would therefore have covariance

`Cov(Phi(x),Phi(y)) = beta^{-1} G_B(x,y)`,

where `G_B=L_B^{-1}` is its Green kernel.

The physical edge-direction fluctuation is

`eta_j = alpha_j+2 beta_j = (4 phi_j-3 psi_j)/sqrt(5)`.

Since `psi=O(eps)` relative to `phi`,

`m^2 eta_{floor(mx)} -> (4/sqrt(5)) Phi(x)`

at leading order in the quadratic theory.

Now compare covariance structures. If

`Y(x)=int_0^x Phi(t) dt`,

then the Gaussian Hessian approximation gives

`Cov(Y(x),Y(y))
 = beta^{-1} int_0^x int_0^y G_B(r,s) dr ds`

up to the harmless fixed edge-direction normalization. In the interior, its mixed distributional derivative is the **nonlocal Green kernel** `beta^{-1}G_B(x,y)`.

By contrast, KRV's conjectured `k=1` random potential contains

`(2/sqrt(beta)) t^(-1/3) b'_t`.

The integrated noise therefore has covariance

`(4/beta) int_0^{min(x,y)} t^(-2/3) dt
 = (12/beta) min(x,y)^(1/3)`.

Its mixed distributional derivative is

`(4/beta) x^(-2/3) delta(x-y)`,

supported on the diagonal.

A fourth-order elliptic Green kernel is nonzero off the diagonal on every interior subinterval, regardless of the unresolved endpoint boundary condition. Therefore:

`boxed{ the pure full-window Gaussian Hessian field cannot itself generate the KRV weighted-Brownian integrated potential. }`

This is **not** a refutation of Virág/KRV. It says the Hessian-only Laplace approximation is too crude at the critical scale. The next subsection shows why that approximation is in fact asymptotically invalid.

---

## 8. The decisive nonlinear calculation: cubic and quartic terms survive at source scale

Let

`F_s(a,b)=W(a,b)-(1-s)log b`

be the exact local Hamiltonian density for `V_*`, and let `(a(u),b(u),s(u))` be its exact critical branch. Perturb in the critical constant direction

`(delta a,delta b)=(2z,z)`.

A direct Taylor expansion using the exact quartic `W` and the branch equations gives

`F_{s(u)}(a(u)+2z,b(u)+z)-F_{s(u)}(a(u),b(u))`

`= 12 u^2 z^2 -32 u z^3 +32 z^4
   + O((|u|+|z|)^5).`

The quadratic, cubic, and quartic terms all have total critical degree four if `u` and `z` are assigned the same source amplitude.

At the `k=1` edge scale,

`u=eps^2 U`,

and the soft fluctuation amplitude found above is `phi=eps^2 Phi`. Since a pure soft vector `(delta a,delta b)=(2z,z)` has `phi=sqrt(5) z`, put

`z=eps^2 Phi/sqrt(5)`.

Then, with `n=eps^{-7}` and `m=eps^{-1}` sites,

`n sum_j [12u_j^2 z_j^2 -32u_j z_j^3 +32z_j^4]`

has a finite nonzero continuum limit:

`int [ (12/5)U^2 Phi^2
      -(32/(5 sqrt(5))) U Phi^3
      +(32/25) Phi^4 ] dx`

(up to the global beta factor and additional derivative terms from the full lattice action).

All three displayed terms are order one. In particular, the cubic and quartic interactions are **not** lower-order corrections to the quadratic Hessian theory.

At the exact critical point `u=0`, the local soft restriction starts with

`32 z^4`,

so the non-Gaussianity is already visible before any asymmetry from `U(x)` is introduced. Moreover, in the orthogonal hard coordinate defined by

`delta a=2z+w`, `delta b=z-2w`,

the critical local action has hard quadratic term `40 w^2` and no `w z^2` term. Thus minimizing the hard mode does not cancel the leading `32 z^4`; the first hard correction occurs at higher soft order.

Therefore the correct conclusion is stronger and more precise than “the Gaussian covariance is colored”:

> **At the source `n^(1/7)` scale, the critical-window Gibbs action is intrinsically non-Gaussian. The Hessian Gaussian is only the quadratic part of an order-one interacting soft-field theory. If the Virág/KRV conjecture is correct, the required weighted-Brownian integrated potential must emerge only after controlling this full nonhomogeneous nonlinear field, not from a Gaussian frozen or Schur-complement approximation.**

This explains why both the regular KRV local-mixing proof and a straightforward critical Gaussian replacement fail.

---

## 9. New claim

### `P03-D0043-K1-NONHOMOGENEOUS-SCHUR-GAUSSIAN-OBSTRUCTION-272`

**Status: PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED.**

For the explicit quartic

`V_*(x)=2/5 x^4-16/15 x^3+2/5 x^2+8/5 x`

at its one-sided `k=1` edge, with source scale `m=n^(1/7)` and `x=j/m`, the deterministic lattice Hessian admits the following full-window bulk critical reduction:

1. after the orthonormal soft/hard transform based on `(2,1)` and `(1,-2)`, the hard mode is uniformly massive on every compact interior interval and is slaved to the soft field by

   `psi=-(eps/5)phi'-(3eps^2/100)phi''-eps^3[(U'/20)phi+phi'''/3000]+O(eps^4)`;

2. with `U=x^(1/3)`, the rescaled Schur complement converges on smooth interior test functions to

   `L=(1/25)D^4-(4/5)D(x^(1/3)D)+(8/45)x^(-5/3)+(24/5)x^(2/3)`;

3. its quadratic form is positive and contains the singular derivative correction `+(8/45)x^(-5/3)`, which is absent from naive frozen-symbol substitution;

4. any Gaussian field obtained from this Hessian has a nonlocal Green covariance, so its integrated edge-direction field cannot equal the KRV weighted-Brownian integrated noise, whose mixed covariance derivative is diagonal;

5. this mismatch does not refute the source because the exact local soft action has surviving order-one cubic and quartic terms at the same `n^(1/7)` scale: `12u^2z^2-32uz^3+32z^4+...`.

The theorem is intentionally scoped to the explicit source-admissible `k=1` potential and to the deterministic bulk Hessian/nonlinear scaling gate. It is not tridiagonal convergence and does not establish a limiting nonlinear field law.

---

## 10. Failure analysis and exact remaining obligation

The D0043 program now has a coherent chain of eliminated easy obstructions and a sharply isolated hard one:

- Claim 264: the singular origin white-noise coefficient is not a local Dirichlet-form obstruction;
- Claim 266: the formal continuum exotic operator exists globally and has compact resolvent;
- Claim 268: the local Hessian susceptibility has the correct exotic blow-up, and uniform regular-edge convexity would suppress the target noise;
- Claim 270: the full frozen correlation length is the whole edge window, so stationary local-equilibrium patching has no mesoscopic scale;
- Claim 272: the correct nonhomogeneous bulk Hessian is fourth order with a singular derivative correction, its Gaussian field has the wrong covariance structure, and cubic/quartic soft interactions survive at order one.

The remaining source-matching obligation is therefore **not another Hessian lemma**. Even for the single explicit quartic `V_*`, one must:

1. derive the boundary-layer limit at the first coordinates / KRV cutoff and identify the second boundary condition for the fourth-order soft operator;
2. obtain a tight non-Gaussian full-window law for the actual tridiagonal coefficients under the degenerating convexity, including the order-one cubic/quartic soft interactions and their spatial couplings;
3. prove that the correctly centered *integrated edge-direction potential* nevertheless converges to the KRV weighted Brownian process;
4. prove the global growth/oscillation estimates needed for operator convergence;
5. only then pass from coefficient-field convergence to the source operator `S_{beta,1}`.

Nothing in this run proves that such a nonlinear Gaussianization occurs. Nothing in this run refutes Virág's conjecture. The metric therefore remains zero.

This is exactly the point at which the HARD protocol requires handoff rather than a third recovery.

---

## 11. Directed independent audit of P04 / I0101

Directed duty remains P03 -> P04. I audited the newest accessible P04 claim that had not appeared in the prior P03 audit exclusion list:

`P04-I0101-SZEGEDY-PLUS-ESCAPE-36 = PROVED / STRUCTURAL-PARTIAL`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T03-45-13Z__run-report.md`,

creation commit `41082b460cf5abc3cff8b2bd914aeae6c47b097e`, blob `bad5ea6f2c42631b0adecaef1958eed67076ab5b`. The P04 exact-commit receipt records recovery of `**End of complete run report.**`.

### Audit ID

`P03-AUDIT-P04-I0101-SZEGEDY-PLUS-ESCAPE-273 = PASS (CLAIM-SCOPED)`.

### Independent argument

Let `K=overline(G_{p,2})` on `n=(p-5)/4` localized vertices. P04 defines

`Theta_+(K)=min{t: exists A=A^T>=0, diag A=0, supp A subset E(K), tI-J+A >= 0}`.

Pairing the PSD slack with `X>=0` gives the Lagrangian

`t(1-tr X)+<J,X>-<A,X>`.

The infimum over free `t` forces `tr X=1`; the infimum over each nonnegative allowed edge weight forces `X_ij<=0` on `E(K)`. A sufficiently large `t` gives strict primal feasibility, so strong SDP duality yields

`Theta_+(K)=max{<J,X>: X>=0, tr X=1, X_ij<=0 on E(K)}`,

the stated Szegedy-plus dual.

On the constant-row face `A 1=(n-t)1`, setting `P=A/(n-t)` makes `P` symmetric stochastic and complement-supported. The primal slack kills `1`, while on `1^perp` it is `tI+(n-t)P`; hence PSD is exactly

`lambda_min(P|1^perp)>=-t/(n-t)`.

For the sign-sensitive defect, write ordered sums `P_H` over `H` edges and `N_K` over `K` edges. With `tr X=1`,

`T=<J,X>=1+P_H+N_K`,

`S=<C,X>=P_H-N_K`.

Since `N_K<=0`, let `Delta=-2N_K>=0`; then exactly

`S=T-1+Delta`.

The earlier conference-block identity used by P04 is

`C^2+UU^T=pI-3J`.

It is consistent with the full Paley conference identity: after two localized anchor columns are removed, their two constant outer products contribute `2J`, leaving the displayed `-3J` internal block identity. With `E=<UU^T,X>>=0`, state Cauchy--Schwarz gives

`S^2 <= tr(C^2 X)=p-3T-E`.

Substitution gives exactly

`T^2+T+1+E+2(T-1)Delta+Delta^2 <= p`.

Finally, at `t_p=2sqrt(p)/3`, the positive root of

`Delta^2+2(t_p-1)Delta = p-(t_p^2+t_p+1)`

is

`sqrt(p-3t_p)-(t_p-1)=sqrt(p-2sqrt(p))-2sqrt(p)/3+1`,

as claimed. Thus the algebra, dual signs, and source-scoped implication are correct.

Scope warning: this audit does **not** prove Randomstrasse Conjecture 27. It certifies only Claim 36's SDP reformulation and defect identity/reduction.

---

## 12. Mandatory D0043 HARD handoff and rotation screen

Because `k_exotic^cert` remains `0` after recovery 2/2, I wrote the separate immutable D0043 HARD handoff in this same run. It preserves Claims 264/266/268/270/272, the explicit quartic, the exact source conventions, and the boundary/nonlinear/full-window blocker. D0043 must not receive a third recovery unless explicitly reassigned.

I then performed the required successor-admission screen against the current root queue/coordinator state rather than stealing a stale row. Current `QUEUE.md` explicitly states that the listed candidates are PENDING unless separately certified and that **newly certified READY entries remain zero**. The latest accessible coordinator health report (`operations/task_health/runs/2026-09-18T035800Z/status.md`) likewise does not create a free HARD successor; it records current claims/health and one separately reserved CLOSABLE admission, not a READY unassigned HARD dispatch for P03. Historical hard-looking rows such as I0060/I0062 remain candidates, not automatic assignments.

Therefore no successor claim was fabricated. Current lawful next state is:

`D0043_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

No successor metric exists until a source is actually admitted; it is **UNMEASURED**, not zero.

---

## 13. Cumulative D0043 ledger

- `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264 = PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266 = PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-D0043-K1-CRITICAL-HESSIAN-GATE-268 = PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-D0043-K1-FROZEN-GREEN-CRITICAL-WINDOW-270 = PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-D0043-K1-NONHOMOGENEOUS-SCHUR-GAUSSIAN-OBSTRUCTION-272 = PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED`.
- Source Conjecture 5: **OPEN/PARTIAL on bounded current screen; not solved or refuted here**.
- Terminal D0043 metric: `k_exotic^cert=0`.
- HARD recoveries: `2/2 consumed`; **no third recovery**.

---

## 14. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  lane: HARD_OUTSIDE
  target: D0043
  source: Virag_ICM2014_Conjecture5_exotic_edge_operators
  canonical_claim: operations/claims/D0043.md
  metric_name: k_exotic^cert
  before: 0
  after: 0
  movement: false
  consecutive_unchanged: 5
  mathematical_status: PARTIAL
  recovery_state: FINAL_RECOVERY_2_OF_2_CONSUMED
  new_claim:
    id: P03-D0043-K1-NONHOMOGENEOUS-SCHUR-GAUSSIAN-OBSTRUCTION-272
    status: PROVED_STRUCTURAL_PARTIAL_SOURCE_ADMISSIBLE_EXAMPLE_PUBLICATION_NOVELTY_UNVERIFIED
  peer_audit:
    id: P03-AUDIT-P04-I0101-SZEGEDY-PLUS-ESCAPE-273
    verdict: PASS_CLAIM_SCOPED
    peer_claim: P04-I0101-SZEGEDY-PLUS-ESCAPE-36
    peer_report: proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T03-45-13Z__run-report.md
    peer_creation_commit: 41082b460cf5abc3cff8b2bd914aeae6c47b097e
    peer_blob: bad5ea6f2c42631b0adecaef1958eed67076ab5b
  next_state: D0043_HANDOFF_COMPLETE_ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  successor_metric: UNMEASURED
  shared_root_edits_by_P03: none
```

P26 alone may reconcile shared root ledgers. P03 edited no peer file and no shared root ledger.

---

## 15. Delivery / model-control limitations

GitHub only. No Gmail/email, Drive, public posting, paid compute, access changes, third-party contact, workflow execution, or extra schedule creation was used.

The exposed scheduler interface still has no binding model selector or reasoning-effort selector. GPT-6/maximum remains prompt-only. This run's actual harness model is GPT-5.6 Sol; reasoning effort is not authenticated and is reported as UNVERIFIED. Changing that requires a platform/runtime context that exposes authenticated model-family and reasoning-effort controls; prompt text cannot certify it.

**End of complete run report.**