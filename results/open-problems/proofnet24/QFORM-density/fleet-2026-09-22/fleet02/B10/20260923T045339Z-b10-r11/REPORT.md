SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-23T04:53:39.282611Z.
attacking: the true-near-coloop exact-rank-three collar after the designated partner paid c<=63/64; quantify the surviving physical star and test a product-safe nonzero-pivot interpolation against the ruled-side theorem.

# fleet02/B10 — true-near-coloop strong-star lemma and a collar-valid square-peel falsifier

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Rank-three coupled case; complementary constructions/source-valid counterexamples  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW SUPPORTING STRUCTURAL LEMMA + TARGET-VALID INTERMEDIATE-MECHANISM FALSIFIER / FULL QFORM OPEN`.

The full target is unchanged: arbitrary independent real inputs with one-dimensional probability densities at most one and arbitrary real symmetric A with at least three eigenvalues of modulus at least one. No moments, bounded support, log-concavity, spectral-coordinate independence, or arbitrary-joint coarea bound is used.

## 1. Sources actually used at equations

The designated partner result is

`yspennstate/math-open-problems@46df88a3c81ee860e09a67bc8193514c26281555`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T041602Z-fleet03-B10-QFORM-r23/REPORT.md`.

It pays every still-unpaid B10 small-Pluecker collar state with hub leverage `c<=63/64`. In the surviving collar it also leaves, after its earlier transverse-heavy exit, the hypotheses

`c>63/64`, `rho:=1-c<1/64`, `|q|<1/16`, and `h_j<1/4` for every residual row,                         (1.1)

where `r_0=sqrt(c)e`, `q=e^T M e`, and `h_j=||(I-ee^T)r_j||^2`.

The required newest-Claude source used below is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its proved ruled-surface Theorem C states that for an exact rank-three form of spectral signature `(+, +, -)` with all three absolute eigenvalues at least one, the one-sheet side `t>=0` has

`p_Q(t)<=pi sqrt(2)`                                                        (1.2)

(after the stated coefficient rescaling; for eigenvalues `{1,1,-1}` this is exactly `pi sqrt(2)`). The proof uses line integrals of the genuine projection of the ORIGINAL product law; it does not assert independence after spectral rotation.

The exact-null endpoint is already paid by fleet02/B16 at

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`.

I do not reprove that endpoint. The present question is the nonzero near-null interpolation.

## 2. Strong-star identity in the true-near-coloop collar

Let the exact-rank-three target be

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`.                         (2.1)

Adapt an orthonormal spectral basis to the physical hub row:

`r_0=sqrt(c)e`,
`M=[[q,b^T],[b,C]]`,
`r_j=s_j e+w_j`, `w_j perpendicular e`, `j!=0`.                       (2.2)

Parseval gives the three exact identities

`sum_j s_j^2=rho=1-c`,
`sum_j s_j w_j=0`,
`sum_j w_j w_j^T=I_2`.                                                (2.3)

The ORIGINAL-coordinate hub cross coefficient is

`A_0j=sqrt(c)(q s_j+b^T w_j)`.                                        (2.4)

Therefore

`sum_(j!=0) A_0j^2
 =c sum_j (q s_j+b^T w_j)^2
 =c(q^2 rho+||b||^2).`                                                (2.5)

The mixed term vanishes exactly by `sum s_j w_j=0`. Thus longitudinal leakage cannot cancel the transverse hub field at the aggregate physical-product level.

Since `sigma_min(M)>=1`,

`q^2+||b||^2=||Me||^2>=1`.                                            (2.6)

Combining (2.5)-(2.6),

`boxed: sum_(j!=0) A_0j^2 >= c(1-c q^2).`                             (2.7)

In the designated-partner survivor (1.1),

`sum_(j!=0) A_0j^2 > (63/64)(255/256)=16065/16384>0.9807.`             (2.8)

So the true-near-coloop obstruction is emphatically not a vanishing-star regime. As `rho->0` and `q->0`, the hub retains an order-one physical cross field.

There is a second useful consequence when the partner transverse-heavy exit has not fired. Put

`a_j=q s_j+b^T w_j`, `B=||b||`.

Then `sum a_j^2=B^2+q^2 rho`, while `h_j<1/4` and `|s_j|<=sqrt(rho)` imply

`|a_j| <= B/2+|q|sqrt(rho)`.                                          (2.9)

Also `B>=sqrt(1-q^2)>=sqrt(255)/16`. Hence, with `rho<1/64` and `|q|<1/16`,

`x:=|q|sqrt(rho)/B <1/(8 sqrt(255))`,

and

`a_j^2/(sum_k a_k^2)
 <=[(1/2+x)^2/(1+x^2)]<0.259.`                                       (2.10)

Thus the surviving order-one star is itself diffuse across residual ORIGINAL coordinates. This is a structural narrowing, not yet a density proof: arbitrary same-bank quadratic curvature is still present, so the mixed-hub theorem cannot simply be invoked after discarding it.

I record this as

**QFORM-TRUE-NEARCOLOOP-STRONG-DIFFUSE-STAR-v1.**

## 3. A target-valid family inside the true-near-coloop collar

The next construction tests whether the standard nonzero scalar square peel can bridge to the exact-null endpoint. It shows that it cannot, even after imposing the partner's true-near-coloop and transverse-diffuse hypotheses.

Fix

`m=5`, `rho=1/128`, `c=127/128`.                                      (3.1)

Use the spectral basis `e_1,e_2,e_3` and the following physical Parseval rows:

- one hub `r_0=sqrt(c)e_1`;
- five leakage rows `r^E_k=sqrt(rho/m)e_1`;
- five transverse rows `r^W_k=e_2/sqrt(m)`;
- five transverse rows `r^V_k=e_3/sqrt(m)`.

Their outer products sum to `I_3`. Every residual transverse leverage is either `0` or `1/m=1/5<1/4`, while `c=127/128>63/64`.

For `0<eps<1/128`, take

`M_eps=[[-eps,0,sqrt(1-eps^2)],
        [0,1,0],
        [sqrt(1-eps^2),0,eps]].`                                     (3.2)

The `e_1,e_3` block has trace zero and determinant `-1`, so the spectrum is exactly

`spec(M_eps)={1,1,-1}`.                                               (3.3)

The hub Rayleigh coefficient is `q=-eps`, and `A_00=-c eps`; hence this is a genuine nonzero near-null pivot in the exact target.

For completeness, the Pluecker distribution factorizes over the three axis banks. Two independent volume-sampled bases are disjoint with probability

`D_disj=(1-c^2-rho^2/m)(1-1/m)^2
       =637/64000
       <1/64.`                                                        (3.4)

So the family lies in the small-disjoint-Pluecker collar as well as the true-near-coloop/transverse-diffuse chamber.

Its hub star energy is

`sum_(j!=0) A_0j^2=c[(1-eps^2)+eps^2 rho]=c(1-c eps^2)`,              (3.5)

in agreement with (2.5), and stays near one.

## 4. The raw square-peel interface still loses logarithmically

Take all ORIGINAL input coordinates iid `Uniform[-1/2,1/2]`, an admissible cap-one product law. Define the independent bank variables

`S=sqrt(rho/m) sum_(k=1)^m X^E_k`,
`W=m^(-1/2) sum_(k=1)^m X^W_k`,
`V=m^(-1/2) sum_(k=1)^m X^V_k`.                                      (4.1)

Then the three spectral projection coordinates are

`Z_1=sqrt(c)X_0+S`, `Z_2=W`, `Z_3=V`,                                (4.2)

and

`Q_eps=-eps Z_1^2+W^2+2sqrt(1-eps^2) Z_1 V+eps V^2`.

Completing the ORIGINAL hub square gives the exact identity

`Q_eps
 =-c eps [ X_0+(S-sqrt(1-eps^2)V/eps)/sqrt(c) ]^2
   +R_eps`,

`R_eps=W^2+V^2/eps.`                                                  (4.3)

The standard square-peel interface therefore pays the majorant

`B_eps=(c eps)^(-1/2) H_(1/2)(R_eps)
      >=(c eps)^(-1/2) E(R_eps^(-1/2)).`                              (4.4)

For fixed `m=5`, the density `g_m` of a normalized sum of five centered unit uniforms is continuous and strictly positive in a neighborhood of zero. Hence there are fixed `a,eta>0`, independent of `eps`, such that

`g_m(x)>=eta` for `|x|<=a`.                                          (4.5)

Using independence of the W and V banks, (4.4)-(4.5), and substituting `v=sqrt(eps) z`,

`B_eps
 >=c^(-1/2) eta^2 int_(|w|<=a, |z|<=a/sqrt(eps))
       (w^2+z^2)^(-1/2) dw dz.`                                     (4.6)

For `eps<1/4`, restrict to `|w|<=a` and `a<=z<=a/(2sqrt(eps))`. Since `sqrt(w^2+z^2)<=sqrt(2)z`,

`boxed:
 B_eps >= c^(-1/2) eta^2 sqrt(2) a log(1/(2sqrt(eps))) -> infinity.`  (4.7)

Thus even in the exact remaining true-near-coloop collar, with every residual transverse leverage below `1/4`, small disjoint Pluecker mass, and order-one diffuse physical star, the unconditional scalar square-peel/half-Riesz bridge diverges logarithmically as the nonzero hub pivot tends to zero.

This is **QFORM-TRUE-NEARCOLOOP-SQUARE-PEEL-LOG-LOSS-v1**. It refutes an intermediate mechanism, not QFORM.

## 5. Actual use of the newest ruled-side theorem

For the same family, the eigenvalues are exactly `{1,1,-1}`. The proved ruled-surface theorem from the required newest-Claude package applies to the actual output density on the one-sheet side and yields, in particular,

`boxed: p_(Q_eps)(0)<=pi sqrt(2)}`                                   (5.1)

uniformly in `eps` and independently of the growing majorant (4.7).

Hence the logarithm in (4.7) is demonstrably a proof-interface loss in a target-valid member of the *current remaining B10 collar*. It cannot be repaired by merely sharpening constants in the raw half-Riesz square peel. The missing interpolation must retain the hub density factor jointly with the product-projection geometry / ruled cancellation before taking the absolute fractional remainder potential.

This consumes the ruled-side theorem at a real inequality/obstruction rather than reproving it.

## 6. What is now paid and what is not

The designated partner pays all small-Pluecker collar states with `c<=63/64`; the present lemma shows that every true-near-coloop survivor `c>63/64`, `|q|<1/16` has an order-one aggregate hub cross field, and, after the partner transverse-heavy exit, that field is quantitatively diffuse in original coordinates. The construction proves that the obvious nonzero-square interpolation nevertheless loses a logarithm even under all of these favorable geometric facts.

The first unpaid implication is therefore sharpened to:

**QFORM-TRUE-NEARCOLOOP-JOINT-HUB-RULED-INTERPOLATION-v1.** In the exact-rank-three small-Pluecker collar with `c>63/64`, `0<|q|<1/16`, order-one diffuse star as in (2.7)-(2.10), prove the minority/two-sheet bound by integrating the ORIGINAL hub density jointly with the transverse product projection before any unconditional `H_(1/2)` or worst conditional-profile step. The exact `q=0` endpoint is already paid and the one-sheet side is already paid by Theorem C.

The full arbitrary-rank QFORM conjecture remains OPEN. Continuity for the unrestricted target remains separate. No claim here transfers spectral-coordinate independence or treats a small matrix coefficient as a small random perturbation on unbounded inputs.
