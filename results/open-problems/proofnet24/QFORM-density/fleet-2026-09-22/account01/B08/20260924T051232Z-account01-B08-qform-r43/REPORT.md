SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-24T05:12:32Z.
attacking: the localized-row compiler after the diffuse-top-three router — extend the completed physical-pair theorem to every positive conditioning scale, convert any fixed-size original off-diagonal edge into a full-matrix density receiver, and reduce the unpaid localized-row branch to a genuinely distributed physical star.

# account01/B08 r43 — all-scale physical pair + fixed-edge compiler + distributed-star survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING ANALYTIC THEOREMS + SHARPER GLOBAL SURVIVOR REDUCTION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Full-target continuity remains OPEN. The new paid branches below establish essential boundedness; continuity is not imported from the logarithmic physical-pair or scalar-pivot receivers.

No moment, bounded-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or law-uniform pointwise quadratic-phase decay hypothesis is introduced.

## 1. Completed inputs actually used

### 1.1 Designated partner account02/B08: physical-pair gate

Source pin:

`yspennstate/math-open-problems@d904e910bf8f33151faa938fd501e4358fb8d58d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T214909Z-account02-B08-qform-diffuse-r28/REPORT.md`.

Its completed theorem says: if `s_3(A)>=L` and some invertible ORIGINAL-coordinate principal pair `B` satisfies

`kappa:=sigma_min(B)>=L/64`,

then the full ambient quadratic form has a density with

`||p_Q||_infinity<619/L`; a definite pair has the stronger `<202/L` bound. Arbitrary complementary spectrum and affine terms are retained. This theorem is applied below at the actual branch `kappa>=L/64`.

The same source proves, for an invertible indefinite pair with `D=|det B|`, after exact pair completion,

`p_Q(s) <= 2 sqrt(2)/r
           + D^(-1/2) E log_+(2r^2/(kappa |s-R|))`,              (1.1)

for every `r>0`, while Schur spectral retention plus the arbitrary-rank small-ball theorem gives

`P(|R-w|<rho)<=min(1,5(rho/L)^(1/4))`.                          (1.2)

These two displayed source estimates are the only ingredients needed for the all-scale extension below.

### 1.2 All-sign scalar pivot

At the immutable current source snapshot

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`,
`proofnet24/QFORM-density/interactive/20260923T192150Z-all-sign-scalar-pivot/REPORT.md`,

if `s_3(A)>=L` and an ORIGINAL diagonal coefficient `a=A_ii` is nonzero, then

`||p_Q||_infinity <= C_sp/sqrt(|a|L)`,                           (1.3)

where

`C_sp=1+44*10^(15/2)=1.3914021714740868...*10^9`.

This is an essential-boundedness theorem; continuity is not asserted there.

### 1.3 Current diffuse-to-localized router

The present B08 predecessor is

`yspennstate/math-open-problems@209e9a8756cdab08ef8fb12c49d1d46934742b9c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260924T033839Z-account01-B08-qform-r42/REPORT.md`.

The newer quantitative three-frame half-cut/crossing refinement is source-pinned at

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T042041Z-account03-B08-qform-diffuse-r50/REPORT.md`.

For a diffuse leading three-eigenvector frame, r50 proves: either

`p_Q in C_0`, `||p_Q||_infinity<197.779/L`,                     (1.4)

or some ORIGINAL coordinate `k` satisfies

`max{|A_kk|,||A[k,-k]||_2}>rho_* L`,                            (1.5)

with

`rho_*=0.0006247538095703261`.                                  (1.6)

If the leading three-frame is not diffuse, r42 gives the stronger row witness `>L/sqrt(96)`, which in particular implies (1.5). Thus (1.4) or (1.5) is available globally, although only the diffuse branch of (1.5) carries the selected-frame leverage information used later.

## 2. All-scale indefinite physical-pair estimate

The partner r28 theorem was stated with `kappa>=L/64`. Its own logarithmic proof actually gives an explicit finite bound for every `kappa>0`; the missing small-`kappa` branch only requires evaluating the layer-cake integral before the source's `c>=1` simplification.

### Theorem 2.1 — `QFORM-THREEEIG-PHYSICAL-PAIR-ALLSCALE-v1`

Let `A=A^T` satisfy `s_3(A)>=L>0`, and let `B=A[{i,j},{i,j}]` be an invertible indefinite ORIGINAL-coordinate principal block. Put

`kappa=sigma_min(B)`, `y=kappa/L`.

Then the full ambient form has a density and

`||p_Q||_infinity <= G(y)/L`,                                   (2.1)

where

`G(y)= [2+20 sqrt(2) y^(1/4)]/y`,          `0<y<=1/2500`,       (2.2)

`G(y)= [6+4 log(5 sqrt(2) y^(1/4))]/y`,    `y>=1/2500`.         (2.3)

The function `G` is strictly decreasing on `(0,infinity)`. For `y>=1/64`, the completed designated-partner theorem may be used directly instead, giving `<619/L`.

#### Proof

Start from (1.1)-(1.2). Let

`a=2r^2/kappa`,
`c=5(a/L)^(1/4)`.

Layer cake gives

`E log_+(a/|s-R|)
 <= integral_0^infinity min(1,c exp(-u/4)) du`.                  (2.4)

The right side is elementary:

`J(c)=4c` for `0<c<=1`,                                         (2.5)

`J(c)=4(1+log c)` for `c>=1`.                                   (2.6)

Choose

`r=sqrt(2) kappa`.                                               (2.7)

Then the first term of (1.1) is `2/kappa`, while

`a=4kappa`, `c=5 sqrt(2) y^(1/4)`.                              (2.8)

Since the singular values of the indefinite `2x2` block are `s_1(B)>=kappa`,

`sqrt(D)=sqrt(s_1(B)kappa)>=kappa`.                              (2.9)

Therefore

`p_Q(s)<=kappa^(-1)[2+J(5 sqrt(2)y^(1/4))]`.                    (2.10)

The threshold `c=1` is exactly

`y=(5 sqrt(2))^(-4)=1/2500`.                                    (2.11)

Substituting (2.5)-(2.6) into (2.10) gives (2.2)-(2.3).

For monotonicity, on `(0,1/2500]`,

`G(y)=2y^(-1)+20sqrt(2)y^(-3/4)`,                               (2.12)

which is strictly decreasing. On `[1/2500,infinity)`, write

`G(y)=N(y)/y`,
`N(y)=6+4log(5sqrt(2))+log y`.                                  (2.13)

At `y=1/2500`, `N=6`; thereafter `N>=6`, so

`G'(y)=(1-N(y))/y^2<0`.                                         (2.14)

This proves the theorem. For `y>=1/64`, the partner's already-completed `<619/L` theorem applies at the actual inequality `kappa>=L/64`, so no extension of its stated scope is needed there. QED.

### Definite pair

If `B` is definite, the completed conditional ellipse estimate gives

`||p_Q||_infinity<=pi/sqrt(|det B|)<=pi/kappa`.                 (2.15)

Hence every invertible physical pair has a finite explicit full-matrix receiver at every fixed positive `kappa/L`; the price is allowed to diverge as that ratio tends to zero.

## 3. A single fixed-size physical edge is now a receiver

The next lemma compiles a literal off-diagonal coefficient without requiring either diagonal to be large.

### Theorem 3.1 — `QFORM-FIXEDSCALE-PHYSICAL-EDGE-COMPILER-v1`

Assume `s_3(A)>=L`. If some ORIGINAL pair `i!=j` satisfies

`|A_ij|>=gamma L`,                                               (3.1)

for a fixed `gamma>0`, then `Q=X^TAX` has a density satisfying

`||p_Q||_infinity <= C_edge(gamma)/L`,                           (3.2)

where one valid explicit constant is

`C_edge(gamma)
 = max{ C_sp sqrt(2/gamma), 619, G(gamma/2) }`.                 (3.3)

For `gamma/2>=1/64`, the pair alternative is paid directly by the designated partner and `G(gamma/2)` may be omitted.

#### Proof

Write the physical principal pair as

`B=[[a,b],[b,c]]`, with `|b|>=gamma L`.                          (3.4)

If

`max{|a|,|c|}>=|b|/2`,                                          (3.5)

then an ORIGINAL scalar pivot has magnitude at least `gamma L/2`, and (1.3) gives

`||p_Q||_infinity
 <= C_sp sqrt(2/gamma) L^(-1)`.                                 (3.6)

Suppose instead

`|a|<|b|/2`, `|c|<|b|/2`.                                       (3.7)

Then

`det B=ac-b^2<0`,
`|det B|>3b^2/4`,                                                (3.8)

and the operator norm obeys the row-sum bound

`s_1(B)<=3|b|/2`.                                                (3.9)

Thus

`kappa=sigma_min(B)=|det B|/s_1(B)>|b|/2>=gamma L/2.            (3.10)

If `kappa>=L/64`, apply the completed account02/B08 partner theorem to this actual pair and obtain `<619/L`. If `kappa<L/64`, Theorem 2.1 and the monotonicity of `G` give

`||p_Q||_infinity<=G(kappa/L)/L<=G(gamma/2)/L`.                 (3.11)

This proves (3.2)-(3.3). QED.

The theorem retains all other matrix entries and all complementary spectrum. It is therefore stronger than a finite-minor structural statement: once a single off-diagonal physical coefficient is bounded below at the target scale, the full density problem is paid, albeit with a large constant when `gamma` is tiny.

## 4. Compile the r50 localized row

Set

`rho_*=0.0006247538095703261`,
`gamma_*=rho_*/16=3.904711309814538e-5`.                         (4.1)

Combining r50 in the diffuse leading-three-frame chamber with r42 in the non-diffuse chamber gives either the continuous payment (1.4) or an ORIGINAL coordinate `k` with

`max{|A_kk|,||A[k,-k]||_2}>rho_*L`.                             (4.2)

Now apply the two receivers above globally.

If ANY physical diagonal satisfies

`|A_ii|>=rho_*L/2`,                                              (4.3)

then the all-sign scalar-pivot theorem gives

`||p_Q||_infinity
 <= C_sp sqrt(2/rho_*) L^(-1)
 <7.873*10^10/L`.                                               (4.4)

If ANY physical off-diagonal coefficient satisfies

`|A_ij|>=gamma_*L`,                                              (4.5)

then Theorem 3.1 pays the full form. At the live value `gamma_*`,

`gamma_*/2=1.952355654907269e-5<1/2500`,
`G(gamma_*/2)=198740.242052...`,                                (4.6)

while the scalar subbranch in Theorem 3.1 gives

`C_sp sqrt(2/gamma_*)
 =3.14900397938...*10^11`.                                      (4.7)

Hence the whole fixed-edge branch is paid by, for example,

`||p_Q||_infinity<3.150*10^11/L`.                               (4.8)

Therefore any STILL-UNPAID configuration after the diffuse-to-localized router necessarily satisfies all of

`max_i |A_ii| < rho_*L/2`,                                      (4.9)

`max_{i!=j}|A_ij| < rho_*L/16`,                                 (4.10)

and for the localized row supplied by (4.2),

`||A[k,-k]||_2>rho_*L`.                                         (4.11)

Consequently that row is genuinely distributed in the ORIGINAL coordinates:

`(||A[k,-k]||_2 / ||A[k,-k]||_infinity)^2 > 256`.               (4.12)

Equivalently, no almost-single-edge star can survive. In fact the squared edge weights can be partitioned into two disjoint original-coordinate leaf sets `J_1,J_2` such that

`||A[k,J_r]||_2^2 >= (127/256)||A[k,-k]||_2^2`,  `r=1,2`.       (4.13)

To see this, greedily take a subset whose squared-weight sum first crosses half of the total. Every single squared weight is less than `1/256` of the total by (4.10)-(4.11), so the chosen side has weight at most `129/256` of the total and the complement at least `127/256`; the chosen side itself is at least `1/2>127/256`. Thus both disjoint banks carry at least `sqrt(127/256)>0.704` of the star norm.

This two-bank star certificate is deterministic and product-preserving. It does NOT by itself give a density bound because arbitrary child cross-curvature can couple `J_1` and `J_2`; one may not simply factor their characteristic functions.

## 5. Extra structure on the genuinely diffuse r50 source branch

When (4.2) comes specifically from r50's diffuse leading-three-frame branch, its selected-three leverage at the row `k` obeys

`p_k<=1/48`.                                                     (5.1)

Deleting coordinate `k` and writing

`A=[[a,b^T],[b,C]]`,                                             (5.2)

B08's exact deletion identity from r35 gives

`s_2(C)>=sqrt(1-p_k)L>=sqrt(47/48)L`.                           (5.3)

Hence an unpaid diffuse source state now has, simultaneously:

- a distributed physical star with `||b||_2>rho_*L`;
- every star edge `<rho_*L/16`;
- every physical diagonal `<rho_*L/2`;
- two child spectral directions of size at least `sqrt(47/48)L`;
- two disjoint original-coordinate leaf banks each carrying at least `sqrt(127/256)||b||_2` of star energy.

This is a substantially narrower product-safe survivor than the previous generic localized-row witness.

## 6. What remains

The first unpaid implication is now

`QFORM-DISTRIBUTED-STAR-TWOCHILD-COMPILER-v1`:

> Starting from the exact physical deletion geometry (5.2)-(5.3), the global entrywise caps (4.9)-(4.10), and the two disjoint star banks (4.13), produce a universal density bound while retaining arbitrary child curvature `C[J_1,J_2]`, arbitrary complementary spectrum and all induced affine terms. One cannot factor the two bank transforms unless that cross-curvature is handled rather than discarded.

This is the correct next B08 endpoint. The live account02/B01 heavy-edge/tail half-Riesz theorem is complementary but does not directly pay (4.13): it requires an exact diagonal-plus-star residual after scalar completion, whereas the present child block is arbitrary. Its mechanism suggests that the next useful quantity is a product-safe two-bank Fourier/volume currency that survives arbitrary same-bank and inter-bank child curvature.

The full universal QFORM theorem remains OPEN, and the global continuous-density conclusion remains OPEN.

## 7. Scope/correction audit

The proof does not use any refuted shortcut. In particular:

- no law-uniform pointwise van der Corput decay;
- no arbitrary-joint quadratic coarea cap;
- no conditional density-cap substitution;
- no independence after spectral rotation;
- no assumed uniformly good finite minor;
- no probabilistic deletion of a small coefficient matrix;
- no numerical experiment as proof.

The only numeric work in Sections 2-4 is deterministic evaluation of explicit constants.
