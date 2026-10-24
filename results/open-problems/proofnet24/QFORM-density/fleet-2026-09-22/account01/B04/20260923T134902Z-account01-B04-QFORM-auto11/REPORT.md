SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T13:49:02Z.
attacking: entropy-bias the fourth-volume face deletion, prove an exact fractional-Hall alternative, and route every failure into one four-row packet paid by the newest account02/B04 support-defect theorem.

# account01/B04 — entropy-biased fourth-volume deletion flow

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATES / FULL_TARGET_OPEN`  
Continuity in the theorem below: **proved (`C_0`)**.  
Full unrestricted QFORM theorem: **OPEN**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

This run uses only ORIGINAL-coordinate product banks. No spectral rotation of the random variables is made. It does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, worst-fiber suprema, moments, support bounds, or a uniformly good individual minor.

## 1. Sources actually used

Fresh owner control remained QFORM-only, revision `2026-09-22.15`.

The current Claude/volume-stability source is

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its sharp fractional third-volume theorem gives, for canonical third-volume row marginals `alpha_i<=q/2`, `1<=q<3/2`,

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`,

with a continuous `C_0` density and arbitrary same-bank curvature/outside conditioning retained.

The entropy-weighted extension used in the new branch is this slot's completed theorem

- `QFORM-ENTROPY-WEIGHTED-THREE-VOLUME-v1`
- `yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T021315Z-account01-B04-QFORM-auto11/REPORT.md`.

For any probability law `w` on supported physical `3 x 3` minors, with row marginals `alpha_i` and

`G(w)=exp(sum_w log(det(M[S,T])^2/w_(S,T)))`,

it gives

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`                 (1.1)

when `max alpha_i<=q/2`, `1<=q<3/2`; again the density is `C_0`.

The newest designated account02/B04 theorem actually used below is

- `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`
- `yspennstate/math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

It says that if `Z=E3(N)>0` and no probability law on the supported physical `3 x 3` minors has every constrained-side row marginal strictly below `3/4`, then the full ambient form has a `C_0` density and

`||p_Q||inf <= 6*4^(1/6) Z^(-1/6)`.                            (1.2)

## 2. Biased deletion identity

Let `M=A[I,J]` be any original-coordinate cross block with

`E4:=e4(M^T M)>0`.

For each physical four-row set `R`, put

`d_R=det(M_R M_R^T)`,   `pi_R=d_R/E4`.                         (2.1)

For each physical triple `S`, put

`a_S=det(M_S M_S^T)`

and

`tau_S=sum_(j notin S) dist(m_j,span M_S)^2`.                  (2.2)

The Gram-height identity gives

`sum_(j notin S) d_(S union {j}) = a_S tau_S`,

hence

`sum_S a_S tau_S =4E4`.                                       (2.3)

Uniformly deleting one row from `R~pi` therefore gives the reference triple law

`mu0(S)=a_S tau_S/(4E4)`.                                     (2.4)

Now change mechanism: conditional on `R`, delete `J` according to an arbitrary kernel `kappa_R(j)`, `j in R`, and let `mu` be the law of `S=R\{J}`. Put

`K(kappa)=sum_R pi_R D_KL(kappa_R || Unif(R))`.                (2.5)

The joint law `(R,J)` under the biased deletion has KL divergence exactly `K(kappa)` from the uniform-deletion joint law. Pushing forward `(R,J)->S` and using data processing gives

`D_KL(mu||mu0) <= K(kappa)`.                                  (2.6)

Let `p(S)=a_S/E3(M)` be the canonical physical row-triple volume law. From (2.4),

`D(mu||p)
 = D(mu||mu0)+log(E3/(4E4))+E_mu log tau_S`.                   (2.7)

Lift `mu` to full `3 x 3` minors using the canonical conditional column-volume distribution. The determinant factors cancel, and its exact entropy currency is therefore

`boxed:
G(mu)=4E4 exp[-D(mu||mu0)] / tau_geo(mu),`                     (2.8)

where

`tau_geo(mu)=exp(E_mu log tau_S)`.                             (2.9)

Consequently

`boxed:
G(mu)>=4E4 exp[-K(kappa)]/tau_geo(mu).`                        (2.10)

Every deletion kernel is supported on four points, so

`D(kappa_R||Unif(R))=log4-H(kappa_R)<=log4`.

Also `tau_S<=||M||_F^2`. Hence every biased deletion kernel satisfies the coarse but dimension-free-in-the-number-of-rows estimate

`boxed:
G(mu)>=E4/||M||_F^2.`                                         (2.11)

The point is that one may now use the deletion choice to repair the row marginals while paying at most one factor four of entropy currency.

## 3. Exact fractional-Hall criterion at the q=4/3 gate

Write

`rho_i=P_pi(i in R)`,
`delta_i=P(J=i)`,
`alpha_i=P(i in S)=rho_i-delta_i`.                             (3.1)

We want `alpha_i<=2/3`, which is the convenient Fourier choice `q=4/3`. This is equivalent to requiring

`delta_i >= ell_i:=(rho_i-2/3)_+`.                             (3.2)

There exists a deletion kernel meeting (3.2) if and only if the finite fractional-Hall inequalities

`boxed:
sum_(i in U) ell_i <= P_pi(R intersects U)   for every U`     (3.3)

hold.

Proof: make a bipartite flow network with one supply node for each four-set `R`, supply `pi_R`, edges from `R` to its four rows, and row demands `ell_i`. Max-flow/min-cut gives exactly (3.3). Once all lower demands are met, allocate each remaining base supply arbitrarily along an incident edge; this only increases `delta_i` and therefore decreases `alpha_i`.

## 4. If the deletion flow fails, one physical four-row packet carries >2/3 of all E4 volume

Assume (3.3) fails. Removing from a failing `U` every index with `rho_i<=2/3` leaves the left side unchanged and can only decrease the right side, so we may assume

`rho_i>2/3` for every `i in U`.                                (4.1)

Since every sampled `R` has size four,

`sum_i rho_i=4`,                                               (4.2)

so `|U|<=5`.

Let `m=|U|` and `K=|R cap U|`. The failed Hall inequality is

`E K -(2/3)m > P(K>=1)`.                                      (4.3)

For `m=1,2,3`, the pointwise inequality

`K-(2/3)m <= 1_{K>=1}`

holds because `K<=m`; for `m=5` it also holds because `K<=4`. Therefore only

`m=4`                                                        (4.4)

can fail.

Now define

`g(K)=K-8/3-1_{K>=1}`.

For `K=0,1,2,3`, `g(K)<=-2/3`, while `g(4)=1/3`. If `p4=P(K=4)`, then

`E g(K) <= (1/3)p4-(2/3)(1-p4)=p4-2/3`.                       (4.5)

Failure (4.3) means `E g(K)>0`, hence

`p4>2/3`.                                                      (4.6)

But both `R` and `U` have four elements, so `K=4` means exactly `R=U`. Thus

`boxed:
if the q=4/3 deletion flow fails, there is a physical four-row U with
 d_U/E4 = pi(U) > 2/3.`                                       (4.7)

This is the new structural classification: the only obstruction to entropy-biased fourth-volume downshift is an actual four-row fourth-volume hub.

## 5. New theorem — fourth-volume flow/hub dichotomy

### Theorem 5.1 — `QFORM-FOURTHVOLUME-ENTROPY-FLOW-DICHOTOMY-v1`

Let `M=A[I,J]` be any original-coordinate cross block with `E4(M)>0`. Then the full ambient quadratic form has a continuous density vanishing at infinity, and one of the following two explicit certificates holds.

**Diffuse deletion-flow branch.** There is a biased fourth-volume deletion kernel whose induced triple marginals satisfy `alpha_i<=2/3`. Then by (1.1), (2.11), with `q=4/3`,

`boxed:
||p_Q||inf <= (9 sqrt(3) e/2)
              [E4(M)/||M||_F^2]^(-1/6).`                      (5.1)

**Four-row hub branch.** There is a physical four-row packet `U` with

`d_U>(2/3)E4(M)`.                                              (5.2)

Put `N=M_U,*`. It has rank four. Since it has only four physical rows, every probability law on its supported row triples has total marginal sum three across four rows, hence some row marginal is at least `3/4`; a strict `<3/4` law is impossible. Therefore the newest account02/B04 theorem (1.2) applies to this actual subblock:

`||p_Q||inf <=6*4^(1/6) E3(N)^(-1/6).`                         (5.3)

If `lambda_1,...,lambda_4>0` are the squared singular values of `N`, then

`E3(N)=d_U sum_i lambda_i^(-1)
      >=4 d_U^(3/4)`                                           (5.4)

by AM-GM. Combining (5.2)--(5.4),

`boxed:
||p_Q||inf <=6 d_U^(-1/8)
           <6[(2/3)E4(M)]^(-1/8).`                             (5.5)

Thus, without any row-marginal assumption at all,

`boxed:
||p_Q||inf <= max{
 (9 sqrt(3)e/2)[E4/||M||_F^2]^(-1/6),
 6[(2/3)E4]^(-1/8)
}.`                                                            (5.6)

This theorem removes the quantitative near-coloop hole left by `QFORM-FOURTHVOLUME-DOWNSHIFT-v1`: concentration of fourth-volume is no longer a separate unpaid endpoint.

It does **not** prove the full owner target, because the bare hypothesis of three large eigenvalues of the full symmetric matrix does not yet force an original-coordinate cross cut with target-scale `E4/||M||_F^2` or target-scale `E4`.

## 6. Explicit genuinely rotated indefinite family: biased deletion opens a gate that uniform deletion nearly closes

Let

`V=(1/2)*[[1,1,1,1],
          [1,-1,1,-1],
          [1,1,-1,-1],
          [1,-1,-1,1]]`,                                      (6.1)

so `V` is orthogonal. For `0<epsilon<1`, let `R_epsilon` have physical rows

`e1,e2,e3,e4, v_epsilon`,
`v_epsilon=e1+epsilon(e2+e3+e4)`,                              (6.2)

and put

`M_epsilon=R_epsilon V`,
`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`.                   (6.3)

Every physical cross entry is nonzero when `epsilon=1/4`; the first four rows have entries `+/-1/2`, while the fifth row is

`(7/8,3/8,3/8,3/8)`.                                          (6.4)

Put `u=epsilon^2` and `D=2+3u`. Since

`R_epsilon^T R_epsilon=I_4+v_epsilon v_epsilon^T`,

the singular values of `M_epsilon` are

`sqrt(D),1,1,1`,                                               (6.5)

and therefore

`spec(A_epsilon)={+sqrt(D),-sqrt(D), +1 x3,-1 x3,0}`.          (6.6)

So this is genuinely rotated, indefinite, and target-valid.

The five physical four-row volumes are especially simple. Index them by the omitted row. Omitting row 1 or row 5 has squared volume `1`; omitting any of rows `2,3,4` has squared volume `u`. Hence

`E4=D=2+3u`.                                                   (6.7)

The old **uniform** face deletion retains each row with probability `(3/4)rho_i`. At `u=1/16`, the three rows `2,3,4` have `rho=34/35`, so

`q_uniform=2*(3/4)*(34/35)=51/35=1.457142857...`,             (6.8)

very near the forbidden endpoint `3/2`.

Instead, on each sampled four-set delete uniformly from the retained portion of the common set

`C={2,3,4}`.                                                   (6.9)

For the two dominant four-bases there are three deletion choices; for each of the three small bases there are two. The induced triple law has:

- three triples `{1,i,j}`, `i<j in C`, each mass `1/(3D)` and row-volume `a_S=1`;
- three triples `{5,i,j}`, each mass `1/(3D)` and `a_S=1+u`;
- three triples `{1,5,i}`, each mass `u/D` and `a_S=2u`.

Its row marginals are

`alpha_1=alpha_5=(1+3u)/D`,
`alpha_2=alpha_3=alpha_4=(4/3+u)/D`.                           (6.10)

For `0<u<=1/6` the common rows dominate, so

`q_bias=2(4/3+u)/D`.                                          (6.11)

Its entropy currency can be evaluated exactly from

`G=exp(H(mu)+sum_S mu(S)log a_S)`, giving

`boxed:
G_bias(u)
 =(3D)^(2/D) (2D)^(3u/D) (1+u)^(1/D).`                       (6.12)

At `epsilon=1/4`, `u=1/16`,

`D=35/16`,
`alpha_common=67/105`,
`alpha_unique=19/35`,
`q_bias=134/105`,                                              (6.13)

and

`G_bias
 =(105/16)^(32/35)
  (35/8)^(3/35)
  (17/16)^(16/35)
 =6.51646198699383...`.                                        (6.14)

The weighted Fourier theorem therefore gives, for every admissible cap-one product law,

`boxed:
||p_(X^T A_(1/4) X)||inf
 <=11.799966755236218...,
 p in C_0(R).`                                                 (6.15)

This is an actual gate-opening effect, not a histogram calculation.

### 6.1 Comparison with the newest Claude canonical volume theorem on the same matrix

For the canonical third-volume law of the same `M_(1/4)`,

`E3=7+9u=121/16`,
`max alpha_i=84/121`,
`q_can=168/121`.                                               (6.16)

Applying the current Claude theorem from `c2414...` directly gives

`||p_Q||inf <=22.13763159356066...`.                           (6.17)

Thus the biased face law improves the current canonical third-volume certificate on the **same matrix** by the factor

`22.13763159356066 / 11.799966755236218
 =1.8760757595979767...`.                                     (6.18)

For comparison, the previous uniform-fourth-face entropy law has

`G_uniform
 =(140/17)^(51/140)
  (35/4)^(57/140)
  (35/8)^(8/35)
 =7.30482709440799...`,                                        (6.19)

but its near-endpoint `q_uniform=51/35` makes the bound

`56.58176234879258...`.                                        (6.20)

The entropy bias loses some raw determinant currency but gains a much larger Fourier-integrability margin; the net improvement over uniform deletion is a factor `4.795078115256936...`.

## 7. Designated partner theorem applied to an actual dense endpoint

Take the same dense Hadamard `V` in (6.1) as a `4 x 4` cross block and

`A_H=[[0,V],[V^T,0]]`.                                        (7.1)

Every cross coefficient is `+/-1/2`, and

`spec(A_H)={+1 x4,-1 x4}`,                                    (7.2)

so this is a genuinely rotated indefinite target-valid matrix.

Its fourth-volume law is concentrated on its unique four-row packet: `E4=1`, `pi(U)=1`, so it lies in the heavy branch (5.2). Also `E3(V)=4`. Applying the newest account02/B04 theorem (1.2) to this actual inequality gives

`boxed:
||p_(X^T A_H X)||inf
 <=6*4^(1/6)*4^(-1/6)=6,`                                     (7.3)

with a continuous `C_0` density. This is exactly the partner exit used abstractly in (5.3)--(5.5).

## 8. What changed in the proof map

Before this run, the fourth-volume downshift had a quantitative near-coloop blow-up: uniform deletion gives `alpha_i=(3/4)rho_i`, and the Fourier coefficient diverges as `rho_*->1` even before the exact coloop endpoint.

After this run, **that obstruction is paid**:

- if the fourth-volume mass can be fractionally routed by deletion, the row gate is forced all the way to `2/3` at entropy cost at most `log4`;
- if the routing fails, fractional Hall forces more than `2/3` of all fourth-volume onto one physical four-row packet, and account02/B04 plus AM-GM pays that packet without multiplying by an arbitrarily small extra singular direction.

The first genuinely unproved connection is therefore now

`QFORM-E4-SCALE-OR-LOWRANK-ROUTING-v1`:

> starting only from the full symmetric matrix having three eigenvalues of absolute value at least one, force an original-coordinate cut with either target-scale `E4(M)/||M||_F^2` or target-scale `E4(M)`, or route failure into the already-paid exact-rank-three, pair-log, ridge, grouped-hub, aggregate-square, or low-cross-rank mechanisms.

The full theorem and full-target continuity remain open; no literature-wide novelty claim is made for this supporting theorem.
