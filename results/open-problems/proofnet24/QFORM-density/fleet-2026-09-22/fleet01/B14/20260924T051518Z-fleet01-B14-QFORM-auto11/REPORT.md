SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-24T05:15:18Z.
attacking: collision-energy localization — replace the aggregate slope L-infinity payment in the overlap receiver by the exact L2 collision energy, then prove arbitrary independent translation/localization mixtures are zero-tax by L2 convolution contraction.

# fleet01/B14 — collision-energy localization of translated slope banks

Run: `20260924T051518Z-fleet01-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: translations and localization  
Status: **SUPPORTING L2 REFINEMENT PROVED / FULL QFORM OPEN / CONTINUITY ONLY IN THE STATED OVERLAP CHAMBER**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN: independent real coordinates with arbitrary probability densities at most one; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one; no moment, bounded-support, centering, connectedness, finite-fragment, post-rotation-independence or regularity assumption.

## 0. Mechanism change after source matching

I initially tested an exact bang-bang reduction from cap-one marginals to indicators of measure-one sets. Before using it as a new result I source-matched it against the live QFORM corpus. It is already proved in the earlier fleet04/B14 extreme-point localization theorem, as recorded explicitly in fleet03/B14 at `math-open-problems@54f2d04e936d0dfefe345d17ee18a46b35039d7e`. That source also proves that no universal finite fragment-count strengthening is available for the coordinatewise bathtub step.

So this run did **not** relabel the known bang-bang reduction as new. The mechanism was changed to a different quantity before reciprocal payment: the `L2` collision energy of the **aggregate** slope pushforward.

## 1. Completed designated-partner input actually used

The newest completed fleet02/B14 mathematical report observed in this run is

- `yspennstate/math-open-problems@b376a5b911fdf54fef212829f376ab301e2561a3`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260924T025846Z-fleet02-B14-QFORM-auto11/REPORT.md`,
- theorem `QFORM-PREPLANCHEREL-COHERENT-PARTITION-v1`.

Use its notation. `X` has density at most one. `(L,Y)` is independent of `X`, with slices

`P((L,Y) in dl dy)=nu_l(dy) dl`,

and

`F_t(l)=int exp(i t y) nu_l(dy)`,
`esssup_l |F_t(l)| <= A |t|^(-1/2)`,
`int nu_l(R) dl=1`.

An independent bank has positive finite law `tau`, total mass `m<=1`, slope `S`, and arbitrary phase/self-curvature `R`. If its positive slope pushforward has density `h` with `||h||_infinity<=L`, the partner proves, after coherent reassembly before the second Plancherel norm,

`||p_eta||_infinity <= 5 pi^(-1/5) A^(2/5)m^(3/5)L^(2/5)`.

The important proof identity retained below is the partner's first factor

`||G_t||_2 <= sqrt(pi A)|t|^(-3/4)`,                                  (1.1)

where

`G_t(x)=int exp(2itxl)F_t(l)dl`.

## 2. New refinement: pay collision energy, not slope height

### Theorem `QFORM-OVERLAP-SLOPE-L2-COLLISION-v1`

Keep the partner setup, but do **not** assume the slope density is bounded. Assume only that

`S_#tau(ds)=h(s) ds`,

where

`H_2:=||h||_2<infinity`.

Let `eta` be the output finite measure of

`Q=H(X)+2XL+Y+2X S(Z)+R(Z)`,                                          (2.1)

where the bank phase `R` is arbitrary measurable. Then `eta` has a continuous `C_0` density and

`boxed:
 ||p_eta||_infinity
 <= 5 pi^(-1/5) A^(2/5)m^(1/5) H_2^(4/5).`                           (2.2)

This strictly refines the completed partner estimate because

`H_2^2 <= m ||h||_infinity`;                                          (2.3)

substitution of (2.3) into (2.2) recovers exactly the partner power `m^(3/5)L^(2/5)`.

### Proof

For fixed `t`, push the complex measure `exp(itR(z)) tau(dz)` forward by `S`. Since it is dominated in total variation by the positive pushforward `h(s)ds`, it has a density `g_t` satisfying

`|g_t(s)|<=h(s)` a.e.                                                  (2.4)

Hence

`||g_t||_2 <= H_2`.                                                    (2.5)

Define, exactly as in the partner proof,

`K_t(x)=int exp(2itxs) g_t(s) ds`.

With Fourier convention `hat g(xi)=int exp(i xi s)g(s)ds`, Plancherel and the change `xi=2tx` give

`||K_t||_2^2=(pi/|t|)||g_t||_2^2
             <= pi H_2^2 |t|^(-1)`,                                  (2.6)

thus

`||K_t||_2 <= sqrt(pi) H_2 |t|^(-1/2)`.                              (2.7)

The exact hub factorisation is

`hat eta(t)=int f_X(x) exp(itH(x)) G_t(x)K_t(x) dx`.

Since `0<=f_X<=1`, Cauchy--Schwarz, (1.1) and (2.7) imply

`|hat eta(t)|
 <= pi sqrt(A) H_2 |t|^(-5/4).`                                      (2.8)

Also `|hat eta(t)|<=m`, because `eta` has total mass `m`. Put

`D=pi sqrt(A) H_2`.

The exact crossover integral is

`int_R min{m,D|t|^(-5/4)}dt
 =10 D^(4/5)m^(1/5)`.                                                  (2.9)

Indeed the positive crossover is `t_0=(D/m)^(4/5)`, and

`2[m t_0 + D int_(t_0)^infinity t^(-5/4)dt]
 =2[m t_0+4D t_0^(-1/4)]
 =10D^(4/5)m^(1/5)`.

Therefore `hat eta in L1`; Fourier inversion yields a continuous `C_0` density and

`||p_eta||_infinity
 <=(1/(2pi))10[pi sqrt(A)H_2]^(4/5)m^(1/5)
 =5 pi^(-1/5)A^(2/5)m^(1/5)H_2^(4/5)`.

This proves (2.2). QED.

### Collision interpretation

For a probability slope with density `h`,

`||h||_2^2=(h*tilde h)(0)`, `tilde h(s)=h(-s)`,                        (2.10)

so the new price is a fractional power of the collision density of two independent copies of the aggregate slope. A deterministic translation of the entire slope leaves (2.10) exactly unchanged.

## 3. Zero-tax arbitrary translation/localization mixtures

The `L2` formulation has a localization consequence stronger than paying a separate `L-infinity` endpoint for every fragment.

### Corollary `QFORM-L2-ANCHOR-TRANSLATION-ZERO-TAX-v1`

Split the independent slope bank as `(Z_H,Z_C)`. Assume

`S(Z_H,Z_C)=S_H(Z_H)+S_C(Z_C)`,                                      (3.1)

and that the positive law of `S_H` has a probability density `k in L2`, with

`K_2=||k||_2`.

No density, support, moment or connectedness assumption is imposed on the complement slope `S_C`. Its law may be decomposed into any finite/countable/soft positive localization

`tau_C=sum_j tau_j`, `m_j=tau_j(R^C)`, `sum_j m_j=1`,                 (3.2)

and the pieces may be translated by arbitrary label-dependent real shifts before entering (3.1). The bank phase/self-curvature `R(Z_H,Z_C)` may couple the two subbanks arbitrarily.

Then the full output of (2.1) satisfies

`boxed:
 ||p_Q||_infinity
 <=5 pi^(-1/5) A^(2/5) K_2^(4/5).`                                  (3.3)

The right side is **identical to the bound with the complement slope deleted altogether**. Thus every complement translation, fragment location, fragment count, separation, unbounded tail and absence of moments costs exactly zero.

### Proof

For piece `j`, let `mu_j` be the positive pushforward of `tau_j` by its translated complement slope. It has total mass `m_j` but need not have a density. Independence of the anchor gives the positive total-slope pushforward density

`h_j=k*mu_j`.

Young's `L2*measure -> L2` inequality gives

`||h_j||_2 <= ||k||_2 ||mu_j||_(TV)=K_2 m_j`.                        (3.4)

Apply Theorem (2.2) to the finite output measure from piece `j`:

`||p_j||_infinity
 <=5 pi^(-1/5) A^(2/5)
   m_j^(1/5)(K_2m_j)^(4/5)
 =5 pi^(-1/5) A^(2/5)K_2^(4/5)m_j`.                                 (3.5)

The output pieces are positive and sum to the full output law. Hence

`||p_Q||_infinity <=sum_j ||p_j||_infinity`,

and summing (3.5) uses only `sum_jm_j=1`, proving (3.3). QED.

This is mass-linear **after** the `L2` anchor contraction. In particular, no finite-fragment approximation is required.

### Cap-one original-coordinate anchors

If `S_H=aZ` for one original coordinate `Z` with density `f_Z<=1`, then

`k(s)=|a|^(-1)f_Z(s/a)`

and

`K_2^2=|a|^(-1)||f_Z||_2^2 <= |a|^(-1)`.                            (3.6)

Therefore

`||p_Q||_infinity
 <=5 pi^(-1/5)A^(2/5)|a|^(-2/5)`.                                   (3.7)

For a multi-coordinate linear anchor, the product-projection `L-infinity` theorem implies the previous partner estimate via (2.3), while (3.3) may be strictly better when the aggregate anchor has low collision energy.

## 4. Actual exact-target family: strict improvement over the partner bound

The partner theorem is now applied to a real inequality, then (2.2) improves it.

Let `R>=2`. Define the cap-one probability density

`f_R(z)=1_[0,1/R](z) + R^(-1) 1_[2,R+1](z)`.                         (4.1)

The first component has mass `1/R`; the second interval has length `R-1` and mass `(R-1)/R`, so (4.1) has total mass one and `||f_R||_infinity=1`. Its collision energy is exact:

`||f_R||_2^2
 =1/R +(R-1)/R^2
 =(2R-1)/R^2`.                                                         (4.2)

Let

`X,L,Y ~ Unif[-1/2,1/2]`

be independent, let `Z_R` have density (4.1), and let `W=(W_1,...,W_m)` be an arbitrary additional independent cap-one product bank. Fix any `b in R^m`. Let `D` be an arbitrary symmetric matrix on `(Z_R,W)` and let `ell` be any affine coefficient vector on that bank. Consider

`Q_R
 =2XL+Y^2
  +2X(Z_R+b^T W)
  +(Z_R,W)^T D(Z_R,W)+ell^T(Z_R,W)+H(X)+alpha L`,                    (4.3)

where `H` is any measurable real function of `X` (for a genuine quadratic-form chamber one may take `H(x)=cx^2+dx+e`). The bank quadratic/affine term is absorbed into the arbitrary partner phase `R(Z)`, while `alpha L` only multiplies the slice transform by a unit phase.

### 4.1 Exact target spectrum

In the original independent coordinates `(X,L,Y)`, the retained principal quadratic block is

`B=[[0,1,0],[1,0,0],[0,0,1]]`,                                      (4.4)

with

`spec(B)={1,-1,1}`.                                                    (4.5)

Therefore every genuine quadratic form in the family (4.3), regardless of the bank dimension, `b`, `D`, translations or bank support, has at least two eigenvalues `>=1` and one eigenvalue `<=-1` by Cauchy interlacing. It lies inside the owner's exact three-large-eigenvalue target.

### 4.2 Completed fleet02/B14 theorem applied literally

Use `(L,Y^2+alpha L)` as the slice. The partner's elementary Fresnel calculation for uniform `Y` gives

`|E exp(itY^2)|<=4|t|^(-1/2)`,                                      (4.6)

so the slice constant is `A=4` (the factor `exp(it alpha l)` has modulus one).

Use the whole slope

`S=Z_R+b^TW`.

Its positive density is `h=f_R*nu_b`, where `nu_b` is the probability law of `b^TW` (a point mass is allowed when `b=0`). Since convolution by a probability measure cannot increase `L-infinity`,

`||h||_infinity<=||f_R||_infinity=1`.                               (4.7)

Thus the completed fleet02/B14 coherent-partition theorem gives the actual target-level inequality

`boxed:
 ||p_(Q_R)||_infinity
 <=C_*:=5 pi^(-1/5)4^(2/5)
 =6.924111078456212... .`                                            (4.8)

This is uniform in `R,m,b,D,ell`, the law/support/fragments of `W`, and all bank translations.

### 4.3 Collision-energy refinement

Young's `L2*measure -> L2` inequality instead gives

`||h||_2<=||f_R||_2
          =sqrt((2R-1)/R^2)`.                                        (4.9)

Apply (2.2), with `m=1` and `A=4`:

`boxed:
 ||p_(Q_R)||_infinity
 <= C_* ((2R-1)/R^2)^(2/5).`                                        (4.10)

Numerically,

- `R=2`: bound `6.171468713842839...`;
- `R=10`: bound `3.563407311091524...`;
- `R=100`: bound `1.445124476573149...`;
- `R=1000`: bound `0.576353777561135...`.

In particular the certificate tends to zero like

`C_* 2^(2/5) R^(-2/5)`                                              (4.11)

although `||f_R||_infinity=1` for every `R` and the small high-density fragment can be translated arbitrarily far away. This is a strict quantitative effect invisible to a proof that records only the final slope `L-infinity` cap.

The family is not a counterexample—the support length of the output grows, so a density supremum tending to zero is compatible with total mass one.

## 5. Localization meaning and full-target gap

The proved localization rule on this overlap branch is now:

`aggregate an L2 anchor -> carry arbitrary translation/fragment labels -> use convolution contraction -> pay collision energy -> Plancherel`.

It is stronger than normalizing remote fragments separately, and it does not require a common support radius, moment bound, connected support, finite fragment count, or even a density for the complement slope.

What remains unpaid is **structural**, not a law-localization defect: from the bare matrix hypothesis `s_3(A)>=1`, force before destructive normalization either

1. an overlap/hub representation with a source-disjoint aggregate slope anchor whose collision energy is controlled at the correct coefficient scale; or
2. one of the already-completed whole-law ridge, grouped-bank, physical-pair/triple, Schur or receiver exits.

The theorem above does not create such a representation for arbitrary `A`, and it does not repair the live counterexamples to pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea, fixed bounded-diameter localization, or fixed fragment count. Therefore the full unrestricted QFORM conjecture remains explicitly OPEN.
