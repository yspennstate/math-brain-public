# QFORM B17 — near-extremizer rigidity for the sharp collinear branch

Run: `QFORM-B17-20260923T003650Z-r11`

Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL_QFORM_OPEN / CONTINUITY_SEPARATE / WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form conjecture is **not proved** here.  The new result classifies every sequence that can asymptotically attain the already proved `3 sqrt(2)` ceiling inside the entire collinear-heavy witness architecture: near saturation is possible **if and only if every individual physical leverage tends to zero**.  Thus no macroscopic physical coordinate can survive in a sharp sequence in this branch.

## 1. Exact source inherited from the preceding B17 theorem

Let `U_i` be iid `Unif[-1/2,1/2]`, let `a=(a_i)` be any finite real vector with

`sum_i a_i^2=1`,

and define

`F(a)=E exp[-6(sum_i a_i U_i)^2]`, `C(a)=6F(a)`.

The preceding fleet01/B17 theorem (`QFORM-COLLINEAR-FRAGMENT-SHARP-3SQRT2-v1`) proves that the exact physical branch constant for arbitrary cap-one laws is at most `C(a)`, with equality at output zero for centered unit intervals, and

`C(a)<=3sqrt(2)`.

Its proof uses the Fourier identity

`F(a)=(24pi)^(-1/2) int_R exp(-t^2/24) prod_i sinc(a_i t/2) dt`.       (1.1)

For `a_i^2<=8/9` it applies Holder with `p_0=2`, `p_i=2/a_i^2` and the Konig--Koldobsky sinc estimate

`I(p):=int_R |sinc u|^p du < sqrt(6pi/p),    p>=9/4`,                (1.2)

where strictness for every finite `p>=9/4` follows from their Proposition 7 proof.  If one coefficient has square larger than `8/9`, the same report proves

`F(a)<=H(|a_1|)`,  `H(s):=int_{-1/2}^{1/2} exp(-6s^2u^2)du`,        (1.3)

and the exact rational certificate

`H(sqrt(8/9)) < 52933/76545 < 1/sqrt(2)`.                           (1.4)

## 2. New quantitative rigidity theorem

### Theorem `QFORM-COLLINEAR-NEAR-EXTREMIZER-RIGIDITY-v1`

For every `epsilon in (0,1]` there exists an explicit source-defined number

`rho(epsilon)<1`

such that every finite `a` with `sum a_i^2=1` and `||a||_infinity>=epsilon` satisfies

`F(a) <= rho(epsilon)/sqrt(2)`,                                     (2.1)

and hence

`C(a) <= 3sqrt(2) rho(epsilon) < 3sqrt(2)`.                         (2.2)

One may take the following completely canonical `rho`.

Put

`h_*:=sqrt(2) H(sqrt(8/9)) < sqrt(2)*(52933/76545)<1`.              (2.3)

For `0<epsilon<=sqrt(8/9)`, define

`q(p):=I(p)/sqrt(6pi/p)`,
`q_epsilon:=max_{9/4<=p<=2/epsilon^2} q(p)`,                         (2.4)

and

`rho(epsilon):=max{h_*, q_epsilon^(epsilon^2/2)}`.                   (2.5)

For `epsilon>sqrt(8/9)`, take simply `rho(epsilon)=h_*` (or the sharper `sqrt(2)H(epsilon)`).

Because `q` is continuous on every compact subinterval of `(1,infinity)` and (1.2) is strict, `q_epsilon<1`; hence every displayed `rho(epsilon)` is strictly below one.

### Proof

Assume first that every `a_i^2<=8/9`.  In the Holder proof of the preceding theorem, do **not** discard the unused strict sinc slack.  With `p_i=2/a_i^2`, change of variables gives exactly

`||sinc(a_i t/2)||_{p_i}
 <= [2sqrt(3pi)]^(1/p_i) q(p_i)^(1/p_i)`.                           (2.6)

Together with `||exp(-t^2/24)||_2=(12pi)^(1/4)`, (1.1) therefore yields the sharpened identity-level estimate

`F(a) <= (1/sqrt(2)) prod_i q(p_i)^(1/p_i)`.                        (2.7)

Choose `j` with `|a_j|=||a||_infinity>=epsilon`.  Then

`p_j=2/a_j^2 in [9/4,2/epsilon^2]`,

so `q(p_j)<=q_epsilon`, while every other `q(p_i)<=1`.  Since

`1/p_j=a_j^2/2>=epsilon^2/2`,

and `0<q_epsilon<1`, (2.7) gives

`F(a) <= (1/sqrt(2)) q_epsilon^(epsilon^2/2)`.                       (2.8)

If some `a_j^2>8/9`, (1.3)--(1.4) give

`F(a)<=H(sqrt(8/9))=(1/sqrt(2))h_*`.                                (2.9)

Equations (2.8)--(2.9) prove (2.1)--(2.2).

Continuity of `q`: on a compact interval `p>=9/4`, `|sinc u|^p` is dominated by the integrable function `|sinc u|^(9/4)` away from the harmless origin, so dominated convergence applies to `I(p)`.  Compactness plus strict (1.2) gives `q_epsilon<1`. QED.

## 3. Exact characterization of every sharp sequence

Let `a^(k)` be any sequence of finite vectors with `sum_i (a_i^(k))^2=1`. Then

`boxed( C(a^(k))->3sqrt(2)  iff  ||a^(k)||_infinity->0. )`          (3.1)

Necessity is immediate from Theorem 2: if the maximum leverage failed to tend to zero, a subsequence would satisfy `||a^(k)||_infinity>=epsilon` for some fixed `epsilon>0`, and (2.2) would leave a fixed gap below `3sqrt(2)`.

For sufficiency, put

`S_k=sum_i a_i^(k) U_i`.

The summands are centered, their total variance is exactly `1/12`, and

`max_i |a_i^(k)U_i| <= ||a^(k)||_infinity/2 ->0`.

Thus the Lindeberg condition is automatic and

`S_k => G`, `G~N(0,1/12)`.

Since `x -> exp(-6x^2)` is bounded and continuous,

`F(a^(k))->E exp(-6G^2)=1/sqrt(2)`.

Hence `C(a^(k))=6F(a^(k))->3sqrt(2)`.  This proves (3.1).

The statement survives arbitrary cap-one heavy laws on the **necessary** side: the exact branch extremization from the preceding B17 theorem says their global peak is bounded by `C(a)`.  Therefore any arbitrary-law sequence in this architecture whose peaks approach `3sqrt(2)` must also have `||a||_infinity->0`.

## 4. Applying the completed fleet02/B17 theorem to exact finite target matrices

The designated partner source used here is fleet02/B17,

`yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`.

It proves: if independent `Y_1,Y_2,Y_3` have even densities nonincreasing on `[0,infinity)`, then for positive `alpha,beta,gamma`,

`Q=alpha Y_1^2+beta Y_2^2-gamma Y_3^2`

has

`||p_Q||_infinity=p_Q(0)`.                                          (4.1)

Apply (4.1) to the following **finite original-coordinate target family**.  For a fixed leverage vector `a`, let

`Y_{1,m}=m^(-1/2) sum_{k=1}^m U_{1k}`,
`Y_{2,m}=m^(-1/2) sum_{k=1}^m U_{2k}`,
`Y_3=sum_i a_i U_{3i}`,

with all physical variables independent centered unit intervals and with the three physical banks disjoint.  Each aggregate density is even decreasing, so the partner theorem gives the exact finite identity

`||p_{Q_{m,a}}||_infinity=p_{Q_{m,a}}(0)`,
`Q_{m,a}=Y_{1,m}^2+Y_{2,m}^2-Y_3^2`.                               (4.2)

The physical-to-spectral frame has two columns consisting of `m` entries `1/sqrt(m)` and the third consisting of the entries `a_i`; hence `R^T R=I_3` and

`A_{m,a}=R diag(1,1,-1)R^T`

has nonzero spectrum **exactly** `{1,1,-1}` for every finite `m`.

The standard local CLT for the two explicit uniform banks (the same local-CLT step already used and proved in the partner branch) gives

`p_{Q_{m,a}}(0) -> 6F(a)=C(a)`.                                    (4.3)

Combining the partner's exact global-mode identity (4.2) with the new rigidity bound therefore yields the actual inequality

`lim_{m->infinity} ||p_{Q_{m,a}}||_infinity
 = C(a)
 <= 3sqrt(2) rho(epsilon)`                                          (4.4)

whenever `||a||_infinity>=epsilon`.

In particular, for every fixed `epsilon>0` and every fixed leverage vector with a macroscopic coefficient at least `epsilon`, all sufficiently large finite exact target matrices in this family have a **strict global** density gap below `3sqrt(2)`.  The partner theorem is essential here for excluding a finite off-zero peak while passing from the central local limit to the global norm.

## 5. Concrete heavy-row certificate

The most heavily localized regime already has an explicit gap.  If

`||a||_infinity^2>8/9`,

then (1.4) gives

`C(a)<6*(52933/76545)=105866/25515=4.1491671565...`,

whereas

`3sqrt(2)=4.2426406871...`.

Thus any branch witness within `0.09347...` of the `3sqrt(2)` endpoint is automatically outside this one-row-dominated regime.

## 6. Consequence for sharp witnesses

This theorem is stronger than the previous statement that each finite leverage vector lies below `3sqrt(2)`.  It identifies the **only possible near-sharp mechanism** in the whole collinear-heavy architecture: a Lindeberg/diffuse cloud of physical coordinates.  No sequence retaining even one fixed-size leverage can approach the sharp branch ceiling.

Hence a full-QFORM witness larger than `3sqrt(2)`, if one exists, cannot be obtained by taking an almost-sharp collinear configuration and leaving a macroscopic coordinate in that spectral direction.  It must exploit genuinely non-collinear shared-coordinate geometry, coupled spectral tails, or another mechanism outside the exact branch proved here.

This is a supporting theorem only.  It does not prove that the unrestricted QFORM sharp constant is `3sqrt(2)` and does not settle the full continuity problem.

## 7. Corrections and provenance

Fresh control was read before the run; the active owner revision was `2026-09-22.15`, QFORM only.  The proof uses none of the refuted law-uniform pointwise oscillatory-decay, arbitrary-joint coarea, post-rotation independence, conditional-cap, finite-fragment-count, single-minor, or cross-rank-three premises.  The only external analytic input is the strict finite-`p` version of Konig--Koldobsky Proposition 7, Adv. Math. 346 (2019), DOI `10.1016/j.aim.2019.02.017`.
