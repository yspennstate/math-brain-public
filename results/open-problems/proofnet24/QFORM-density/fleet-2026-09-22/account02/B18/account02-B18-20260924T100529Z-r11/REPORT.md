SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-24T10:05:29Z.
attacking: the latest rank-one full-cross collar; determine whether a vanishing nonzero second cross singular value is a genuine density obstruction or only an overlap-sensitive proof-certificate loss.

# account02/B18 r11 — source-separated near-rank-one cross tails are harmless, and bounded physical cores remain impossible

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** literature-to-proof transfer / complementary construction  
**Status:** `PROVED SUPPORTING LEMMA + TARGET-VALID STRUCTURAL OBSTRUCTION / FULL QFORM OPEN`  
**Continuity:** not claimed for the generic statement below.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The latest completed designated-partner result, account03/B18 `QFORM-TWOSIDED-ANCHOR-FULLCROSS-PAY-OR-RANK1-COLLAR-v1`, says that for a zero-self original-coordinate bank with full cross map `D`, top singular values `d1>=d2`, and arbitrary curvature retained on the opposite bank,

`||p_Q||_infinity <= 2 sqrt(pi)/(d1 d2)^(1/2)`

whenever `d2>0`. Equivalently, for a threshold `theta`, either `d1 d2>=theta` is paid or the full cross map lies within `sqrt(theta)` of rank one. The previous account02/B18 run then proved the deterministic funnel

`s3(A) <= d2 + ||P C P||_op`,

where `P` projects transverse to the top right singular direction of `D`. Thus the small-`d2` survivor has almost-unit transverse opposite-bank curvature.

The first unpaid issue is therefore not merely to prove `d2` cannot be small. This run proves that `d2` may tend to zero in literal target matrices while the density remains uniformly bounded, provided the small tail is carried by disjoint original sources. Hence the correct remaining distinction is **source overlap**: source-separated tails can be retained exactly by convolution; only tails sharing sources with the rank-one-cross/transverse-curvature packet remain genuinely difficult.

## 2. Primary source input, exact scope

The external theorem actually used is:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1.

For a genuine product probability density `f(x)=prod_i f_i(x_i)` on `R^n`, with one-dimensional density caps `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. In particular:

- every normalized scalar projection has density cap at most `sqrt(2)`;
- every orthogonal two-dimensional projection has **joint** density cap at most `2`.

The theorem requires no moments, bounded support, log-concavity, iid assumption, centering, symmetry, or smoothness. It does not assert independence of projected coordinates. The proof below uses only these `k=1,2` consequences and genuine independence between disjoint original-coordinate banks.

The completed internal analytic kernel used is account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, canonical source

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

It states: if `S` has density cap `K`, `(C,D)` is independent of `S` and has arbitrary **joint** density cap `M`, then for `beta,gamma!=0`,

`T0=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`

has an essentially bounded density with

`||p_T0||_infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3)`.   (2.1)

No independence between `C,D` is needed.

## 3. New transfer — arbitrary source-separated remainder stability

### Lemma `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-PLUS-INDEPENDENT-REMAINDER-v1`

Under the hypotheses of (2.1), let `R` be any real random variable independent of `(S,C,D)`. No density, moment, boundedness, or regularity assumption is imposed on `R`. Then

`T = T0 + R`

has an essentially bounded density and

`boxed: ||p_T||_infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`   (3.1)

### Proof

By the completed theorem, `T0` has a density `p0` with the bound (2.1). Let `mu_R` be the probability law of `R`, which may be arbitrary. Genuine independence gives

`Law(T)=Law(T0)*mu_R`,

hence a density

`p_T(t)=int p0(t-r) d mu_R(r)`

for almost every `t`. Therefore

`||p_T||_infinity <= ||p0||_infinity mu_R(R) = ||p0||_infinity`,

which is (3.1). `QED`

The lemma is elementary but materially changes the latest collar interpretation: a small nonzero cross singular direction cannot be declared negligible, but if its entire random contribution is carried by disjoint original coordinates, it is retained exactly as an independent convolution and costs nothing in `L^infinity`.

## 4. Target-valid family with `d2 -> 0` and a uniform bound

Fix an even integer `m>=4`. Take four pairwise-disjoint original-coordinate banks

`I0, J0, I1, J1`,

each of cardinality `m`. Let

`u  = m^(-1/2)(1,...,1)` on `I0`,
`u2 = m^(-1/2)(1,...,1)` on `I1`,
`v  = m^(-1/2)(1,...,1)` on `J0`,
`v2 = m^(-1/2)(1,...,1)` on `J1`,

and let `w` on `J0` have `m/2` entries `+m^(-1/2)` and `m/2` entries `-m^(-1/2)`. Then `v perpendicular w`, and all five vectors are unit vectors on their respective banks.

For `0<eps<1` define

`Q_eps
 = 2 (u^T X_I0)(v^T X_J0)
   + (w^T X_J0)^2
   + 2 eps (u2^T X_I1)(v2^T X_J1)`.                              (4.1)

Write

`U=u^T X_I0`, `V=v^T X_J0`, `W=w^T X_J0`,
`U2=u2^T X_I1`, `V2=v2^T X_J1`.

Because the four banks are disjoint, `(U,V,W)` is independent of `(U2,V2)`, and `U` is independent of the pair `(V,W)`. LPP gives

`||p_U||_infinity <= sqrt(2)`,
`||p_(V,W)||_infinity <= 2`.                                      (4.2)

Apply (3.1) with

`S=U`, `C=V`, `D=W`, `beta=gamma=1`, `alpha=delta=0`,
`R=2 eps U2 V2`, `K=sqrt(2)`, `M=2`.

Then, for every `0<eps<1`, every `m>=4`, and every allowed collection of rough cap-one input laws,

`boxed:
 ||p_Qeps||_infinity
 <= 3 (4 sqrt(2))^(2/3)
 = 3 * 2^(5/3)
 = 9.524406311809198... .`                                      (4.3)

The `eps`-term is not omitted, approximated, or treated perturbatively; it is present in the exact law and is paid by genuine source-separated convolution.

## 5. Exact spectrum and direct application of the latest partner result

The physical matrix of (4.1) is orthogonally supported on the five-dimensional space spanned by

`u, v, w, u2, v2`.

In this orthonormal basis it is block diagonal with blocks

`[[0,1],[1,0]]`, `[1]`, and `[[0,eps],[eps,0]]`.

Therefore

`boxed: spec_nonzero(A_eps)={-1,1,1,-eps,eps}.`                   (5.1)

For `0<eps<1`, the family has **exactly three** eigenvalues of modulus at least one, so it lies literally in the owner's unrestricted target.

Now group the zero-self bank as

`X-bank = I0 union I1`,

and the opposite bank as

`Y-bank = J0 union J1`.

Its physical cross map is

`D = u v^T + eps u2 v2^T`,

with singular values

`d1=1`, `d2=eps`.                                                   (5.2)

The newest completed account03/B18 theorem therefore gives the correct source-valid certificate

`||p_Qeps||_infinity <= 2 sqrt(pi) eps^(-1/2)`.                    (5.3)

As `eps downarrow0`, (5.3) diverges while the exact source-separated bound (4.3) stays below `9.525`. Thus reciprocal payment in `d2` is a **certificate loss**, not an intrinsic obstruction, on this real target family.

At the partner's live threshold `theta=2^(-12)`, every `eps<2^(-12)` enters the near-rank-one collar. The previous account02/B18 deterministic funnel forces transverse complement curvature at least `1-eps`; here that curvature is explicitly

`P_v C P_v = w w^T`,
`||P_v C P_v||_op=1`.                                              (5.4)

So this family sits exactly inside the current collar geometry rather than bypassing it.

## 6. Bounded-size physical localization is impossible on the same family

Every nonzero physical entry of `A_eps` has magnitude at most `1/m` because all active vectors are flat and `eps<1`. Let `S` be any set of `k` original coordinates. Then every row of the principal block `A_eps[S,S]` has absolute row sum at most `k/m`. Since the block is symmetric,

`||A_eps[S,S]||_op
 <= sqrt(||A_eps[S,S]||_1 ||A_eps[S,S]||_infinity)
 <= k/m`.                                                          (6.1)

Consequently, for every fixed `k`,

`sup_(|S|<=k) ||A_eps[S,S]||_op -> 0`

as `m->infinity`, uniformly in `0<eps<1`. More quantitatively, a physical principal block cannot have even one eigenvalue of modulus at least `c>0` unless it uses at least `cm` original coordinates.

Thus the latest rank-one collar plus forced transverse curvature does **not** admit a universal bounded-cardinality physical-core extraction. The proof compiler must aggregate original-coordinate banks before inversion or use a genuinely aggregate Fourier/volume receiver.

This is consistent with, and sharper for the live collar than, the older general corrections forbidding an assumed uniformly good fixed principal minor.

## 7. Required pinned `e5f71d79...` result applied to the same obstruction

Let

`Q0 = 2UV + W^2`

be the first two terms of (4.1). Its rank-three spectral range is

`span{u,v,w}`

and its nonzero spectrum is `{-1,1,1}`. The spectral-subspace leverage of each `I0` coordinate is `1/m`, while each `J0` coordinate has leverage

`v_j^2+w_j^2=2/m`.

For `m>=4`, every leverage is at most `1/2`. Therefore pinned Theorem F from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

applies literally with `B=0`, full active coordinate set `I=I0 union J0`, and Gram matrix `G_I=I_3`. It gives

`boxed: ||p_Q0||_infinity <= 12.`                                  (7.1)

The residual `R_eps=2eps U2V2` uses disjoint original sources, hence convolution gives independently

`boxed: ||p_Qeps||_infinity <= 12.`                                (7.2)

The LPP/dependent-pair route (4.3) is numerically sharper, but (7.2) is the required real use of a completed pinned result on the same target-valid obstruction.

The pinned counterexample search reports no valid QFORM counterexample. That negative search result is not used as novelty evidence or as support for any theorem above.

## 8. What is actually left

The full unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity remains separate.

Within the latest zero-self-bank near-rank-one collar, the new distinction is now precise:

- **source-separated tail:** if the small second cross contribution lives on original coordinates disjoint from a paid rank-one-cross/transverse-square core, it is retained exactly as an independent convolution and costs nothing in the density bound;
- **overlapping tail:** if that small nonzero direction shares original coordinates with the core, convolution is unavailable and it cannot be deleted under arbitrary unbounded cap-one inputs.

The sharpened unpaid implication is therefore

`QFORM-RANK1-CROSS-TRANSVERSE-CURVATURE-OVERLAPPING-TAIL-BRIDGE-v1`:

starting from the partner's rank-one collar and the previous transverse-curvature funnel, either extract a source-separated paid core plus independent remainder, or control the genuinely overlapping small second cross direction jointly with the transverse same-bank curvature by a product-preserving receiver. A bounded-size physical principal core cannot be the universal bridge by (6.1).

Globally, the bare condition `s3(A)>=1` still does not force the zero-self-bank packet itself; the full product-preserving compiler remains unpaid.

## 9. Deterministic checks

For `m=8`, direct finite diagonalization gives the nonzero spectra

- `eps=1/2`: `{-1,-1/2,1/2,1,1}`;
- `eps=10^-2`: `{-1,-10^-2,10^-2,1,1}`;
- `eps=10^-6`: `{-1,-10^-6,10^-6,1,1}`.

These agree with the exact block decomposition (5.1). The constant in (4.3) is

`3*2^(5/3)=9.524406311809198...`.

Finite calculations only check algebra/constants and are not evidence for the universal conjecture.

## 10. Correction discipline

No step above uses or infers:

- independence after rotating coordinates;
- an arbitrary-joint rank-three coarea bound;
- a positive moment or supremum of a worst conditional projection-density cap;
- law-uniform pointwise quadratic-phase decay;
- deletion of a small nonzero matrix coefficient;
- a uniformly good bounded physical minor;
- novelty from a literature or repository search miss.

All independence claims are traced to disjoint original-coordinate source sets. The small `eps` tail is retained exactly in the output law.
