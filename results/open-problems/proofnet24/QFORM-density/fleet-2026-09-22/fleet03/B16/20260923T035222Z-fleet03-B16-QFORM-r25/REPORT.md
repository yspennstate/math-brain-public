SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T03:52:22Z.
attacking: the near-coloop/two-source leakage obstruction by converting the projection-product Fourier gate into an exact volume-sampling basis law and quantifying the surviving approximate two-coordinate cocircuit.

# fleet03/B16 r25 — balanced volume sampling and an approximate two-coordinate cocircuit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW STRUCTURAL/ANALYTIC THEOREM / STRICTER EXACT-RANK-THREE REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the balanced-basis paid branch; not proved for the full target.

## 1. Source boundary and inherited state

The unrestricted owner target remains open: for arbitrary independent original-coordinate inputs with probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one dimension-free bound for the density of `X^T A X`, or give a valid counterexample. No Gaussian, moment, support, log-concavity, connected-support, or spectral-coordinate-independence assumption is used here.


The immediate B16 predecessor is

`yspennstate/math-open-problems@3185d21d594f9e06450da809ca97fab2132285a4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T031836Z-fleet03-B16-QFORM-r24/REPORT.md`.

Its theorem `QFORM-DUPLICATED-SLICE-FRESNEL-v1` works in exact rank three

`A=R Lambda R^T`, `R^T R=I_3`, `D:=|det Lambda|>=1`,

at a physical row `r_i=sqrt(c)e`, `0<c<1`. For residual rows write

`r_j=s_j e+w_j`, `w_j perpendicular e`, `h_j=||w_j||^2`, `a:=1-c`.

Parseval gives

`sum_(j!=i) s_j^2=a`,
`sum_(j!=i) w_jw_j^T=I_2`,
`sum_(j!=i) s_jw_j=0`.                                            (1.1)

The r24 duplicated leverage is

`delta_j=h_j+s_j^2/(2a)`.                                        (1.2)

If every `delta_j<=1/2`, r24 gives a continuous density and the explicit determinant-homogeneous bound

`||p_Q||_infinity
 <=3 e^(5/6)[2ca]^(-1/6)D^(-1/3)`.                              (1.3)

The first unpaid r24 state occurs when the duplicated gate fails, after the other paid exits have removed large transverse rows.

The completed Fourier input used below is fleet01/B18 `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical source

`yspennstate/math-open-problems@8c04ccbc1f032d1a82ad505223f08e3c344bde74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

For a rank-three coefficient frame, any probability law `w` on nonsingular physical bases whose coordinate marginals are all at most `1/2` yields a continuous density with

`||p_Q||_infinity <=3e (D Z_w)^(-1/3)`,                           (1.4)

where

`Z_w=exp(H(w)+sum_S w_S log det(R_S)^2)`.                         (1.5)

This theorem works at the original product characteristic function and therefore keeps product provenance through the nonlinear quadratic integration.

## 2. Exact volume-sampling identities around one physical row

For every three-element physical basis `S`, set

`v_S=det(R_S)^2`.                                                  (2.1)

Because `R^T R=I_3`, Cauchy--Binet gives

`sum_S v_S=1`,                                                     (2.2)

so `v` is a probability law on bases. The next identities are exact.

### Lemma 2.1 — one-row inclusion ledger

For `j!=i`, under the basis law `v`,

`P_v(i in S)=c`,                                                   (2.3)

`P_v(i,j in S)=c h_j`,                                            (2.4)

`P_v(j in S)=s_j^2+h_j`,                                         (2.5)

and therefore

`P_v(j in S | i in S)=h_j`,                                      (2.6)

`P_v(j in S | i notin S)=h_j+s_j^2/a=:q_j`.                      (2.7)

#### Proof

Choose a deterministic orthonormal coefficient basis with first axis `e`. If a basis contains `i,j,k`, then

`det(r_i,r_j,r_k)^2
 =c det(w_j,w_k)^2`.

Summing over `j<k` and using the two-dimensional Cauchy--Binet identity for `sum w_jw_j^T=I_2` gives (2.3). Fixing `j` and summing over `k` gives

`sum_k det(w_j,w_k)^2=||w_j||^2=h_j`,

which proves (2.4). Equation (2.5) is the standard one-point inclusion identity for volume sampling, equivalently the diagonal of the rank-three projection `RR^T`; here it is simply `||r_j||^2=s_j^2+h_j`. Subtract (2.4) from (2.5) and divide by `a=1-c` to obtain (2.7). QED.

## 3. New theorem: the duplicated Fourier gate is exactly a balanced basis law

Define the **balanced inclusion/exclusion basis law** around coordinate `i` by

`w_S = v_S/(2c)` if `i in S`,

`w_S = v_S/(2a)` if `i notin S`.                                 (3.1)

The two pieces each have total mass `1/2` by (2.3).

### Theorem 3.1 — `QFORM-BALANCED-VOLUME-BASIS-v1`

For the law (3.1),

`alpha_i:=P_w(i in S)=1/2`,                                      (3.2)

and for every `j!=i`,

`boxed: alpha_j=h_j+s_j^2/(2a)=delta_j.`                         (3.3)

Moreover its determinant-entropy score is exactly

`boxed: Z_w=2 sqrt(ca).}`                                        (3.4)

Consequently, if every duplicated leverage satisfies `delta_j<=1/2`, then for arbitrary independent cap-one original-coordinate inputs and arbitrary affine terms,

`boxed:
 ||p_Q||_infinity
 <=3e [2 sqrt(c(1-c)) D]^(-1/3).`                                (3.5)

The density has a continuous `C_0` representative.

#### Proof

Equation (3.2) is immediate. Using Lemma 2.1,

`alpha_j
 =(1/2)P_v(j in S|i in S)
 +(1/2)P_v(j in S|i notin S)
 =(1/2)h_j+(1/2)(h_j+s_j^2/a)
 =delta_j`,

which is (3.3).

For the score, on the `i in S` half of the law, `v_S/w_S=2c`, while on the `i notin S` half, `v_S/w_S=2a`. Hence

`log Z_w
 =sum_S w_S log(v_S/w_S)
 =(1/2)log(2c)+(1/2)log(2a)
 =log(2sqrt(ca))`.                                                (3.6)

If all `alpha_j<=1/2`, the completed capped-basis Fresnel theorem applies directly and gives (3.5) and continuity. QED.

### Interpretation

The r24 five-dimensional duplicated-slice gate was not an accidental analytic inequality. It is exactly the coordinate-marginal feasibility condition for balancing the physical volume-sampling law so that the chosen hub is included half the time and excluded half the time. This identifies what a failure of the duplicated gate means in the Pluecker/basis geometry rather than only in the leakage coordinates.

The r24 direct duplicated-slice constant (1.3) is slightly sharper numerically than (3.5); the point of Theorem 3.1 is the exact basis-law interpretation and the structural information obtained when the gate fails.

## 4. Main new structural theorem: gate failure forces an approximate two-coordinate cocircuit

Assume `delta_j>1/2` for some residual coordinate `j`. Put

`q_j=h_j+s_j^2/a`.                                                (4.1)

Then (3.3) says

`delta_j=(h_j+q_j)/2>1/2`,

so

`boxed: q_j>1-h_j.}`                                              (4.2)

The next identities quantify the resulting basis concentration.

### Theorem 4.1 — `QFORM-DUPLICATED-GATE-COCIRCUIT-v1`

Under `delta_j>1/2`, the natural volume-sampling basis law satisfies

`P_v(i,j both in S)=c h_j`,                                       (4.3)

`P_v(i,j both notin S)=a(1-q_j)<a h_j`,                           (4.4)

and therefore

`boxed:
 P_v(|S intersect {i,j}|=1)>1-h_j.}`                             (4.5)

In words: failure of the projection-product Fourier gate forces almost all Pluecker basis mass onto bases containing **exactly one** member of the physical pair `{i,j}`.

If in addition `h_j<1/64`, then

`boxed: P_v(|S intersect {i,j}|=1)>63/64.}`                      (4.6)

Moreover the Gram matrix of all rows outside `{i,j}`,

`G_rest=I_3-r_ir_i^T-r_jr_j^T`,                                  (4.7)

has a unit vector `z` satisfying

`boxed:
 z^T G_rest z
 <(128/63) a h_j.}`                                              (4.8)

Hence, when `h_j<1/64`,

`boxed:
 <r_i,z>^2+<r_j,z>^2
 >61/63.}`                                                        (4.9)

Thus the unpaid gate-failure branch contains an **approximate two-element cocircuit**: two actual original coordinates capture more than `96.8%` of one spectral direction.

#### Proof

Equation (4.3) is Lemma 2.1. For (4.4), inclusion-exclusion and (2.3)-(2.5) give

`P_v(i,j both absent)
 =1-c-(s_j^2+h_j)+ch_j
 =a(1-h_j)-s_j^2
 =a(1-q_j)`.                                                      (4.10)

By (4.2), `1-q_j<h_j`, proving (4.4). The complement of the XOR event is the disjoint union of `both present` and `both absent`, so

`P_v(not XOR)<ch_j+ah_j=h_j`,

which proves (4.5)-(4.6).

For (4.8), write `w_j=sqrt(h_j)v` with unit `v perpendicular e`. On the one-dimensional direction in `e^perp` orthogonal to `v`, `G_rest` acts as the identity. On `span(e,v)` it has matrix

`K=[[a-s_j^2,-s_j sqrt(h_j)],
    [-s_j sqrt(h_j),1-h_j]]`.                                    (4.11)

Its determinant is exactly

`b:=det K=a(1-h_j)-s_j^2=a(1-q_j)<a h_j`.                        (4.12)

Its trace is

`T=1+a-s_j^2-h_j
  =1+b-c h_j
  >1-h_j
  >63/64`.                                                        (4.13)

Let `lambda_min<=lambda_max` be the eigenvalues of `K`. Since `lambda_max>=T/2>63/128`,

`lambda_min=b/lambda_max
 <(128/63)b
 <(128/63)a h_j`.                                                (4.14)

Choose `z` to be a unit eigenvector for `lambda_min` inside `span(e,v)`. Then (4.8) follows. Finally

`<r_i,z>^2+<r_j,z>^2=1-z^T G_rest z`.

Using `a<=1` and `h_j<1/64` in (4.8) gives

`z^T G_rest z<2/63`,

which is (4.9). QED.

## 5. Stronger specialization to the current B16 hard chamber

The r24 residual chamber already has the following source-valid exits.

1. The designated partner fleet04/B16 theorem `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical source

   `yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T231542Z-fleet04-B16-QFORM-r1/REPORT.md`,

   gives

   `||p_Q||_infinity
    <=12D^(-1/3)d^(-1/6)`.                                      (5.1)

   Therefore the actual threshold `d>=1/64` yields

   `boxed: ||p_Q||_infinity<=24.`                                (5.2)

   This is the required equation-level application of the designated partner result in this run.

2. In the complementary `d<1/64` chamber, r24 proves that any residual transverse leverage `h_j>=1/64` gives `||p_Q||_infinity<865`.

3. If all `h_j<1/64` and every duplicated leverage is at most `1/2`, r24 gives the continuous `<18.7` branch whenever its quantitative `c(1-c)` threshold is met; Theorem 3.1 gives an independent capped-basis proof at the exact determinant scale (3.5).

4. If the duplicated gate fails, Theorem 4.1 now upgrades the previous statement `s_j^2/a>31/32` to a geometric basis certificate:

   `P_v(|S intersect {i,j}|=1)>63/64`,                            (5.3)

   and there is a spectral direction more than `61/63` captured by the two physical coordinates `i,j`.

The leakage-dominant coordinate is unique: from `delta_j>1/2` and `h_j<1/64`,

`s_j^2/a>1-2h_j>31/32`;                                         (5.4)

two distinct coordinates cannot each consume more than `31/32` of `sum s_j^2=a`.

So the broad projection/dependence obstruction has been narrowed further. It is not merely "one large conditional projection height"; it is an approximate two-element cocircuit in the **physical Pluecker geometry**, with one uniquely identified second original coordinate.

## 6. Relation to the newest concurrent exact-rank-three work

A fresh concurrent report, fleet03/B10 r25,

`yspennstate/math-open-problems@291d344e0c5af27b8b5074dbba22fee22abddbf8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T034310Z-fleet03-B10-QFORM-r25/REPORT.md`,

proves an arbitrary-hub complement-whitening/three-deletion reduction and separately pays every second row with transverse leverage at least `1/4` in its near-null collar. The present theorem is complementary: in the much more transverse-diffuse `h_j<1/64` regime it identifies the exact two-coordinate Pluecker concentration created by failure of the source-product Fourier gate. No hypothesis from B10 is silently imported; the two reductions can be spliced only where their stated collar hypotheses overlap.

## 7. Next unpaid implication

The first B16 implication is now

`QFORM-TWO-COORDINATE-COCIRCUIT-CURVATURE-v1`:

> In exact rank three, assume the hard gate-failure state above: two actual original coordinates `{i,j}` capture more than `61/63` of one spectral direction, the natural basis law places more than `63/64` of its mass on bases containing exactly one of them, and all residual transverse leverages relative to the first hub are below `1/64`. Use the two independent physical scalars **jointly** with the remaining product projection to obtain a universal density bound, or force an already-paid physical-pair/scalar-pivot/capped-basis branch. Do not replace the residual leakage by zero and do not pass to a worst conditional projection density.

A promising exact object for that next step is the two-scalar nonlinear kernel before any absolute-value fiber supremum. The cocircuit estimate (4.8) says the remaining source has only `O(a h_j)` energy in one coefficient direction; the live no-perturbation correction means that small energy must be retained as oscillatory/product curvature rather than discarded.

Arbitrary additional spectrum remains a separate full-target interface after exact rank three.

## 8. Deterministic verification and status

The accompanying `VERIFY.py` checks the exact rational thresholds and the algebraic probability/Gram identities symbolically. It contains no Monte Carlo argument and is not used as proof.

- `QFORM-BALANCED-VOLUME-BASIS-v1`: **PROVED**.
- `QFORM-DUPLICATED-GATE-COCIRCUIT-v1`: **PROVED**.
- Paid branch continuity: **PROVED** through the capped-basis Fourier theorem; full-target continuity remains open.
- Exact rank-three QFORM: **OPEN / NOT PROVED**.
- Arbitrary-rank full QFORM: **OPEN / NOT PROVED**.
- Counterexample: **none**.
- Native learned-memory receiver ingestion: **not verified**; status remains `WITHOUT_VERIFIED_BRAIN`.
