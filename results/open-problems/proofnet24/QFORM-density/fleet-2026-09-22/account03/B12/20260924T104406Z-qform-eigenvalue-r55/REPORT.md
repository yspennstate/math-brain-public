SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T10:44:06.080177Z.
attacking: a finite-large-spectrum closure theorem: prove that sufficiently many |lambda|>=1 directions force either a bounded physical five-mode carrier or a five-cross-direction ridge certificate, with arbitrary remaining signed spectrum allowed.

# account03/B12 — 189-large-eigenvalue closure and additional-spectrum reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T104406Z-qform-eigenvalue-r55`  
Role: Additional eigenvalue control  
Status: **PROVED TARGET-SCOPE SUBTHEOREM / FULL QFORM OPEN**  
Regularity: **continuous `C_0` density is proved on the whole subtheorem below**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source-valid inputs

The owner target is unchanged: `X_1,...,X_n` are independent real variables with arbitrary probability densities `0<=f_i<=1`; `A` is arbitrary real symmetric; the full conjecture assumes only three eigenvalues of absolute value at least one. No moment, iid, Gaussian, log-concave, compact-support, connected-support, or diagonal-basis hypothesis is introduced. The proof below never rotates the random vector and never treats an added quadratic remainder as independent noise.

The live correction inbox was reread immediately before publication. In particular, no law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, conditional-density cap, fiber-supremum reduction, or post-rotation independence is used.

Three completed analytic/deterministic inputs are used at their exact scopes.

1. **Five-square-mode physical compiler**, account03/B12 r47:  
   `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`.  
   If a literal ORIGINAL-coordinate set `H`, `m=|H|>=5`, satisfies
   `lambda_5((A^2)[H,H])>=g^2>0`, then the full final quadratic form has a continuous `C_0` density and
   `||p_Q||_infinity <= sqrt(24*pi*m+K3^2)/g`,
   where `K3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.

2. **One-scale ridge theorem**, interactive ridge-window proof:  
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,  
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.  
   For a literal ORIGINAL-coordinate cross block `B=A[I,J]`, `gamma>0`,
   `K=B B^T(gamma^2 I+B B^T)^(-1)`, `theta=tr K`, if `max_i K_ii<=q/2` and `theta>2q`, `1<=q<=2`, then the full form has a continuous `C_0` density with
   `||p_Q||_infinity <= sqrt(e)/(sqrt(2q)*gamma) * theta/(theta-2q)`.
   The same source proves the two-part MSS frame application used below: a Parseval frame of vectors of squared norm at most `alpha` admits a partition whose two partial Gram matrices are at least
   `delta I`, `delta=1/2-alpha-sqrt(2 alpha)`.

3. **Square-order physical monotonicity**, account03/B12 r54:  
   `yspennstate/math-open-problems@de50ec1784dcc262198255b7628fb87d02b8f2e2`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T101039Z-qform-eigenvalue-r54/REPORT.md`.  
   If symmetric `A,B` satisfy `A^2>=B^2`, then on every literal physical carrier `H`, `s_k(AP_H)>=s_k(BP_H)`.

The published MSS theorem itself is Marcus-Spielman-Srivastava, *Interlacing Families II*, Annals of Mathematics 182 (2015), Corollary 1.5, as source-pinned and instantiated in the ridge proof above.

## 2. Main theorem: 189 large eigenvalues are already enough

### Theorem 2.1 — `QFORM-189-LARGE-EIGENVALUE-CLOSURE-v1`

Let `A=A^T` have at least **189** eigenvalues satisfying `|lambda|>=1`. Then, for every independent cap-one product input, `Q=X^T A X` has a continuous density in `C_0(R)` and

`boxed: ||p_Q||_infinity < 3,060,011.`

No restriction is imposed on any other eigenvalue: there may be arbitrarily many additional eigenvalues, of either sign, arbitrary multiplicity and arbitrary magnitude below or above any other scale. Their eigenvectors may be arbitrarily oriented in the ORIGINAL coordinates.

Consequently the full three-large-eigenvalue conjecture reduces, without loss, to matrices having between **3 and 188** eigenvalues of absolute value at least one. This is a genuine finite-large-spectrum reduction; it is not the full conjecture.

### Constants

Fix

`alpha=213/2500=0.0852`, `m=47`, `tau=1/512`.

Let

`delta = 1/2-alpha-sqrt(2 alpha)
       = 1037/2500 - sqrt(426)/50
       = 0.002004651188994122...`

and

`sigma=delta-tau=0.00005152618899412209... >0`.

The positivity is exact: since `1037/2500-1/512>0`,

`(1037/2500-1/512)^2 - 426/2500
 =4356321/102400000000>0`.

Also set

`beta=(47 alpha-4)/43 = 11/107500 =0.0001023255813953488...`.

### Proof

Let `P` be the spectral projection of `A` onto **all** eigenspaces with `|lambda|>=tau`, and choose an orthonormal-column matrix `U` spanning `Ran P`, so `P=UU^T`. Write the corresponding spectral truncation as

`A_H=U Lambda U^T`,

where every diagonal entry of `Lambda` has absolute value at least `tau`, and set `E=A-A_H`. Then

`||E||_op<tau`.                                                    (2.1)

Let `r_1` be the number of eigenvalues of `A` with absolute value at least one. By hypothesis `r_1>=189`. For each ORIGINAL coordinate let

`ell_i=P_ii=||u_i||^2`,

where `u_i` is the `i`th row of `U`, viewed as a column in the high-spectral coordinate space. Define the heavy-coordinate set

`S={i: ell_i>alpha}`, `h=|S|`.

We split exhaustively.

### Case A: at least 47 heavy physical coordinates

Suppose `h>=47` and choose any literal ORIGINAL-coordinate subset `H subset S` of size `47`. The compression

`K=P[H,H]=U_H U_H^T`

is a positive contraction. Let its eigenvalues be

`kappa_1>=...>=kappa_47>=0`.

Its trace obeys

`sum_j kappa_j = sum_{i in H} ell_i >47 alpha =4+11/2500`.        (2.2)

Since every `kappa_j<=1`, the first four contribute at most four. Therefore

`sum_{j=5}^{47} kappa_j > 11/2500`.

There are 43 terms in this tail and each is at most `kappa_5`, hence

`boxed: kappa_5 > (11/2500)/43 = beta =11/107500.`                (2.3)

Spectrally `A^2>=tau^2 P`. Compressing to these ORIGINAL coordinates and using min-max gives

`lambda_5((A^2)[H,H]) > tau^2 beta`.                              (2.4)

Thus the five-mode compiler applies with

`g_H=tau sqrt(beta)=1.975705229917...*10^(-5)`.

With `m=47`,

`||p_Q||_infinity
 < sqrt(24*pi*47+K3^2)/(tau sqrt(beta))
 =3060010.258326368... <3060011`.                                 (2.5)

The same compiler gives a continuous `C_0` representative.

### Case B: at most 46 heavy physical coordinates

Assume `h<=46` and put `L=S^c`. Work inside the high-spectral coordinate space `R^r`, where `r=rank P`. Define

`W=ker(U_S)`,

and let `R` denote orthogonal projection onto `W`. Because `U_S` has at most `h` rows,

`codim W<=h`.                                                       (2.6)

For each light ORIGINAL coordinate `i in L`, put

`w_i=R u_i`.

These vectors form a Parseval frame on `W`. Indeed, for `x in W`, `U_S x=0`, and since `U^TU=I`,

`sum_{i in L} <w_i,x>^2
 =sum_{i in L}<u_i,x>^2
 =||Ux||^2
 =||x||^2`.                                                        (2.7)

Moreover

`||w_i||^2<=||u_i||^2=ell_i<=alpha`.                              (2.8)

Apply the two-part MSS frame partition to obtain a disjoint partition

`L=I disjoint_union J`

such that, as operators on `W`,

`M_I:=sum_{i in I} w_iw_i^T >= delta I_W`,
`M_J:=sum_{j in J} w_jw_j^T >= delta I_W`.                        (2.9)

Now let `E_1` be the span of those high-spectral eigen-coordinate axes whose actual eigenvalues have absolute value at least one, so `dim E_1=r_1>=189`. Define the symmetric compression

`C=R Lambda R |_W`.                                                (2.10)

The key point is that `C` retains many genuinely large singular directions despite the heavy-coordinate removal. Consider

`V=E_1 intersect W intersect Lambda^(-1)W`.                       (2.11)

Both `W` and `Lambda^(-1)W` have codimension at most `h` in the high-spectral coordinate space, because `Lambda` is invertible there. Hence

`dim V >= r_1-2h`.                                                 (2.12)

For `x in V`, one has `Rx=x` and `Lambda x in W`, so

`Cx=R Lambda R x=Lambda x`,

and because `x in E_1`,

`||Cx||=||Lambda x||>=||x||`.                                     (2.13)

By the singular-value min-max principle,

`s_{r_1-2h}(C)>=1`.                                                (2.14)

Since `h<=46` and `r_1>=189`,

`5+2h <=97 <= r_1-2h`,

so in particular

`boxed: s_{5+2h}(C)>=1.`                                          (2.15)

Construct the compressed physical cross block

`G=U_I R Lambda R U_J^T`.                                         (2.16)

The two maps `U_I R:W->R^I` and `U_J R:W->R^J` have Gram matrices `M_I,M_J`. By (2.9), their least singular values are at least `sqrt(delta)`. Their polar decompositions therefore show, for every admissible singular index,

`s_k(G)>=delta s_k(C)`.                                           (2.17)

Taking `k=5+2h` and using (2.15),

`s_{5+2h}(G)>=delta`.                                              (2.18)

The actual high-spectral physical cross block is

`B_H=A_H[I,J]=U_I Lambda U_J^T`.

Let `Q=I-R`. Then

`Lambda-R Lambda R = Q Lambda + R Lambda Q`,                      (2.19)

so

`rank(Lambda-R Lambda R)<=2 rank Q<=2h`.                          (2.20)

Therefore

`rank(B_H-G)<=2h`.                                                 (2.21)

Rank-`2h` singular-value interlacing gives

`boxed: s_5(B_H)>=s_{5+2h}(G)>=delta.`                            (2.22)

Finally the actual full cross block is

`B=A[I,J]=B_H+E[I,J]`.

By (2.1), `||E[I,J]||<=||E||<tau`, hence rectangular Weyl gives

`boxed: s_5(B)>delta-tau=sigma>0.`                                (2.23)

This is the crucial additional-spectrum statement: **all** spectrum below the threshold, of either sign and arbitrary orientation, enters only through the deterministic operator tail `tau`; the high signed spectrum is retained exactly through `Lambda` and the compression argument. No random independence is asserted for either piece.

Apply the ridge theorem to this actual cross block with

`q=2`, `gamma=sigma/3`.                                            (2.24)

Because `0<=K_gamma<=I`, the ridge-leverage condition is automatic:

`max_i (K_gamma)_ii<=1=q/2`.                                      (2.25)

The five singular values at least `sigma` contribute at least

`sigma^2/(gamma^2+sigma^2)=9/10`

each, so

`theta_gamma>=5*(9/10)=9/2>4=2q`.                                (2.26)

The ridge theorem therefore gives a continuous `C_0` density and

`||p_Q||_infinity
 <= sqrt(e)/(2 gamma) * theta/(theta-4)
 <= sqrt(e)/(2 gamma) * 9
 = 27 sqrt(e)/(2 sigma)
 =431969.4040828599... <431970`.                                  (2.27)

Combining Cases A and B proves Theorem 2.1. QED.

## 3. Why the threshold 189 appears

The number is not claimed sharp. It is the exact finite-dimensional accounting of this proof mechanism.

- `m=47` is the smallest carrier size compatible with a heavy-coordinate trace forcing five projector modes while keeping the two-part MSS lower frame bound positive after a nonzero spectral-tail allowance.
- If fewer than 47 coordinates are heavy, `h<=46`.
- The light-case compression loses at most `2h` large singular directions when imposing `W` and `Lambda^{-1}W`.
- The physical cross block may then lose another `2h` indices through the rank-`2h` difference between `Lambda` and `R Lambda R`.
- Five surviving cross singular directions therefore require

  `r_1 >= 5+4h <= 5+4*46 =189`.

This is why the theorem closes the `r_1>=189` sector. A different compiler with fewer than five physical/cross modes could lower this threshold substantially; the present argument makes no optimality claim.

## 4. Required designated-partner application at an actual inequality

Use the completed account04/B12 r8 theorem:

`yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`,  
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`,  
`QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`.

Take a partner-theorem physical carrier of size `m=10` with `p=2`, `ell=8`, satisfying

`s_2(Lambda)>=4`, `s_8(R)>=2`, `||Lambda^(-1)W^T||_op<=1/2`.

The partner shear inequality gives the actual equation

`s_10(A_* P_H)
 >= gamma(1/2) min(4,2)
 = (sqrt(17)-1)/2
 =1.5615528128088303...`.                                         (4.1)

Now add an **arbitrary symmetric signed packet** `F` satisfying only

`rank(FP_H)<=5`.                                                   (4.2)

Its global rank, complement spectrum, signs and magnitudes are otherwise unrestricted. Rank-five interlacing gives

`s_5((A_*+F)P_H)>=s_10(A_*P_H)`.                                 (4.3)

Then add an arbitrary symmetric dense packet `T` satisfying only

`||TP_H||_op<=1/20`.                                              (4.4)

Rectangular Weyl gives for the actual final matrix

`boxed:
 sqrt(lambda_5((A^2)[H,H]))
 >= (sqrt(17)-1)/2 -1/20
 =1.5115528128088302... >1.`                                      (4.5)

The five-mode compiler therefore yields

`boxed: ||p_Q||_infinity <19.461`,                                (4.6)

with a continuous `C_0` density. Since `s_5(AP_H)>1`, the final matrix itself has at least five, hence at least three, eigenvalues of absolute value greater than one. This is an actual owner-target family.

This partner application shows the same principle on a bounded carrier: arbitrary large signed additions are paid by **dimension of their local destructive action**, not by treating their quadratic values as an independent convolution remainder.

## 5. Deterministic checks

`CHECKS.py` and `CHECK_RESULTS.json` in this run directory record exact constants plus two 10,000-instance seeded sanity suites (`seed=20260924104406`).

- Downstream light-branch rank/tail checks: `0/10000` violations of the rank-interlacing plus dense-tail lower bound; minimum observed `s_5-sigma =0.012587291305590505`. The minimum observed ridge effective dimension at `gamma=sigma/3` was `4.999998150483134`, safely above the required `4`.
- Heavy trace-to-fifth-eigenvalue checks: `0/10000` violations of `lambda_5>=beta` under the positive-contraction trace condition; minimum observed margin `0.6683305965907714`.

These are consistency checks only. The proof is analytic: spectral truncation, dimension counting, MSS frame partition, singular-value min-max/interlacing, and the two source-valid density receivers.

## 6. Exact remaining gap

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

This run removes an entire additional-spectrum regime: **the conjecture is now proved, with continuity, whenever at least 189 eigenvalues satisfy `|lambda|>=1`**. Therefore any unresolved counterexample or proof obstruction can be assumed to have at most 188 such eigenvalues.

The owner target starts at three, so the finite-rank window `3<=r_1<=188` remains. It may still contain arbitrarily many nonzero eigenvalues below one, of either sign and arbitrary orientation. The next B12 task is to lower the required spectral-resource count by replacing the five-mode endpoint in one or both branches with a proved three-resource receiver, or to show that the matrices with `3<=r_1<=188` and no five-mode physical/cross certificate necessarily enter one of the already-paid grouped-hub, projected-crossing, ridge, Schur, pair, common-plane, or Pluecker-volume mechanisms.

No counterexample to the full conjecture was found.
