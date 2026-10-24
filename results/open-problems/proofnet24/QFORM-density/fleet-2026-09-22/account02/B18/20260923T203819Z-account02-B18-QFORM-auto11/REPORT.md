SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T20:38:19Z.
attacking: the near-coloop/near-planar exact-null-hub puncture via account03/B18 r34 and a nonaligned source-private Fresnel--Brascamp--Lieb aggregation.

# account02/B18 — diffuse private-bank aggregation beyond aligned subbank selection

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW SUPPORTING THEOREM + TARGET-VALID CERTIFICATE-SEPARATION FAMILY + DESIGNATED-PARTNER AND PINNED-e5f APPLICATION / FULL QFORM OPEN**.

Execution: `WITHOUT_VERIFIED_BRAIN`. Continuity is proved only for the new branch below, because its characteristic function is integrable; no global continuity claim is made.

## 1. First unpaid implication and live corrections

The exact-rank-three null-hub normal form is

`Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2`,          (1.1)

with independent original-coordinate cap-one inputs,

`||beta||_2=1`, `beta dot g=0`, `gamma:=||g||_2>0`, `d!=0`.          (1.2)

The preceding B18 run paid planar residual twist and a diffuse three-frame nonplanar branch, but the bound degenerates in the simultaneous near-coloop/near-planar collar. The latest designated partner `account03/B18 r34` adds a different source-private exit: if a literal source bank `K` satisfies `g_K=0`, `rho=||beta_K||>0`, and `ell_K=a beta_K`, then

`||p_Q||_infinity <= 2^(13/4)/(rho sqrt(|d| gamma)).`                (1.3)

Its proof is source-valid and allows arbitrary shear on the complementary source bank.

The live correction `QFORM-B15-NONZERO-SQUARE-AFFINE-SLOPE-RESCUE-FALSE-v1` forbids treating a nonzero linear slope in the *same scalar* as an improvement of a translated square. The newer `QFORM-NEARZERO-ARBITRARY-REMAINDER-EXTENSION-FALSE-v1` likewise forbids an arbitrary-remainder near-zero continuation without genuine third curvature. The result below does neither: a nonaligned private twist is spent as a second **original-product direction**, and the independent complementary projection supplies the third oscillatory dimension. The proof uses the full product factorization on `K`, not a numerical cap on an arbitrary joint law. This also respects the new negative-two-sheet obstruction showing that numerical 3D/2D projection caps alone are insufficient.

## 2. Primary-source input actually needed

The external projection input is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, arXiv:1507.07949. For a genuine product probability density `prod f_i` with every `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In particular, for a deterministic nonzero coefficient vector `r`,

`||p_(r dot X)||_infinity <= sqrt(2)/||r||_2`.                       (2.1)

No moment, support, log-concavity, smoothness, iid, centering, or symmetry hypothesis is present. The theorem gives a projected **joint/marginal density cap**, not independence of projected coordinates.

The other analytic input is already a completed theorem/lemma in the owner-pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`:

for every original cap-one factor and every `p>=2`,

`int_R |psi_i(s)|^p ds <= 4 pi/sqrt(p)`,                             (2.2)

and the normalized rank-one geometric Brascamp--Lieb step used in Theorem F. I use these at their literal product-source hypotheses below.

## 3. New theorem — `QFORM-NULLHUB-DIFFUSE-PRIVATE-BANK-v1`

Assume (1.1)--(1.2). Suppose the leaves have a literal source split

`L = J disjoint_union K`, `g_K=0`,                                  (3.1)

and put

`rho=||beta_K||_2>0`.                                                (3.2)

Orthogonally decompose the private-bank twist against the private square direction:

`ell_K = a beta_K + r`,
`a=(ell_K dot beta_K)/rho^2`,
`r perp beta_K`, `eta=||r||_2`.                                     (3.3)

Assume `eta>0`. Define unit coefficient vectors on the **original K coordinates**

`b=beta_K/rho`, `v=r/eta`.                                          (3.4)

Thus `b perp v`, and assume the two-frame is diffuse:

`b_k^2+v_k^2 <= 1/2` for every `k in K`.                            (3.5)

Let

`G=g_J dot X_J`, `M_G=||p_G||_infinity`.                            (3.6)

Then `Q` has a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) M_G^(2/3) (rho^2 eta^2 |d|)^(-1/3).`                  (3.7)

Using (2.1), `M_G<=sqrt(2)/gamma`, so in the owner class

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/3) [|d| gamma^2 rho^2 eta^2]^(-1/3).`                    (3.8)

Numerically `3*2^(5/3)=9.524406311809198...`.

### Proof

Write

`C=beta_J dot X_J`, `S=X_0+ell_J dot X_J`,
`B=b dot X_K`, `V=v dot X_K`.                                       (3.9)

Then `beta_K dot X_K=rho B` and `r dot X_K=eta V`. Exact completion of the aligned private component gives

`Q = R_J + d rho^2 (B+c_J)^2 + 2 eta G V`,                          (3.10)

where

`c_J=(C+aG/d)/rho`,
`R_J=2SG-2aCG-a^2G^2/d`.                                            (3.11)

Both `c_J` and `R_J` are measurable with respect to the complementary source block `(X_0,X_J)`. No independence is claimed between `B` and `V`; they are generally dependent projections of the same product bank.

Let `psi_k` be the characteristic function of original coordinate `X_k`. Conditional on `X_J` (and dropping the harmless outside phase and the `X_0` characteristic factor by modulus at most one), the one-square Fresnel identity from the pinned e5f source gives for `t!=0`

`|phi_Q(t)|
 <= (4 pi |t d| rho^2)^(-1/2)
    E_J int_R prod_(k in K)
       |psi_k(b_k u + 2t eta G v_k)| du.`                            (3.12)

The random square center `c_J` contributes only a unimodular factor in the Fresnel variable and therefore disappears from (3.12).

The right side now depends on `J` only through `G`. Since `G` has density bounded by `M_G`, change variables

`y=2t eta G`.                                                        (3.13)

Then

`|phi_Q(t)|
 <= (4 pi |t d| rho^2)^(-1/2)
    [M_G/(2|t|eta)] I_K`,                                           (3.14)

where

`I_K = int_(R^2) prod_(k in K) |psi_k(b_k u+v_k y)| du dy.`         (3.15)

Set `c_k=b_k^2+v_k^2`. The rows `(b_k,v_k)` form a Parseval frame in `R^2`:

`sum_k (b_k,v_k)(b_k,v_k)^T = I_2`, `sum_k c_k=2`.                 (3.16)

Rows with `c_k=0` are discarded. For the rest, the geometric Brascamp--Lieb inequality, with normalized row `(b_k,v_k)/sqrt(c_k)`, gives

`I_K
 <= prod_k [c_k^(-1/2) int_R |psi_k(s)|^(1/c_k) ds]^(c_k).`        (3.17)

By (3.5), `1/c_k>=2`, so the pinned e5f estimate (2.2) yields

`c_k^(-1/2) int |psi_k|^(1/c_k)
 <= c_k^(-1/2) 4pi sqrt(c_k)=4pi`.                                  (3.18)

Using `sum c_k=2`,

`I_K <= (4pi)^2`.                                                    (3.19)

Substitution into (3.14) gives

`|phi_Q(t)|
 <= B_* |t|^(-3/2)`,
`B_*=4 pi^(3/2) M_G/[rho eta sqrt(|d|)]`.                            (3.20)

Together with `|phi_Q|<=1`,

`int_R |phi_Q(t)| dt
 <= int_R min(1,B_* |t|^(-3/2))dt
 =6 B_*^(2/3)`.                                                      (3.21)

Fourier inversion therefore gives

`||p_Q||_infinity <= (3/pi) B_*^(2/3)`,                             (3.22)

which is exactly (3.7). Equation (3.8) follows from LPP (2.1). Since (3.21) proves `phi_Q in L^1`, the inverse Fourier transform is a continuous `C_0` density. QED.

### What the theorem spends

The gain does **not** come from an affine slope of the translated square. It comes from three genuine pieces of source provenance before conditioning destroys them:

1. Fresnel curvature in the private square direction `b`;
2. the nonaligned private direction `v` inside the same original product bank, handled jointly with `b` by the two-dimensional Brascamp--Lieb integral;
3. the genuinely independent complementary product projection `G`, whose density cap supplies the extra `|t|^-1` scaling in (3.14).

This is why the two recent arbitrary-remainder counterexamples do not apply.

## 4. Strict quantitative family: aligned subbank selection loses sqrt(m), aggregate BL stays constant

For `m>=8`, take original coordinates

`X_0, X_1,...,X_m, G`,                                               (4.1)

all independent with arbitrary densities bounded by one. On the private bank `K={1,...,m}`, define

`b_j=1/sqrt(m)`,                                                     (4.2)

and

`v_j = sqrt(12/[m(m^2-1)]) (j-(m+1)/2)`.                            (4.3)

Then

`||b||=||v||=1`, `b dot v=0`,                                       (4.4)

and the exact endpoint leverage is

`max_j (b_j^2+v_j^2)
 = (4m-2)/[m(m+1)] <= 1/2` for `m>=8`.                              (4.5)

The ratios

`v_j/b_j = sqrt(12/(m^2-1))(j-(m+1)/2)`                             (4.6)

are all distinct.

Put

`B=b dot X_K`, `V=v dot X_K`,
`Q_(m,eta)=2(X_0+eta V)G+B^2`, `eta>0`.                             (4.7)

The three active coefficient directions are

`w=e_0+eta v`, `g=e_G`, `beta=b`.                                   (4.8)

They are mutually orthogonal, with norms `sqrt(1+eta^2),1,1`. Hence the physical matrix has exactly the three nonzero eigenvalues

`boxed: {-sqrt(1+eta^2), 1, +sqrt(1+eta^2)}.`                       (4.9)

Thus (4.7) is a literal owner-target family for every `m>=8`, `eta>0`, and every allowed product law.

### 4.1 Actual application of designated partner account03/B18 r34

The r34 aligned-private-bank theorem may choose any source-private subbank `K' subset K`, but alignment requires

`ell_(K') = a beta_(K')`,                                           (4.10)

so by (4.6) any nonempty aligned `K'` has at most one coordinate. Therefore its best possible private square mass is

`rho_(K')=1/sqrt(m)`.                                                (4.11)

Applying r34 literally to the target family (4.7) gives the valid but dimension-losing certificate

`||p_(Q_(m,eta))||_infinity
 <= 2^(13/4) sqrt(m)
 =9.513656920021768... sqrt(m).`                                    (4.12)

This is a bound on the output, not a claim that the true density grows like `sqrt(m)`.

The aggregate theorem above instead uses the whole private bank, with `rho=1`, `eta` as in (4.7), `d=gamma=1`. Since `G` is itself an original coordinate, its density cap is actually `M_G<=1`, sharper than the generic LPP `sqrt(2)`. Therefore

`boxed:
 ||p_(Q_(m,eta))||_infinity
 <= 3*2^(4/3) eta^(-2/3).`                                         (4.13)

For `eta=1`,

`boxed: ||p_(Q_(m,1))||_infinity <= 7.559526299369239...}`           (4.14)

uniformly in `m`. This is the concrete benefit of aggregating a diffuse nonaligned private bank before selecting a coordinate.

### 4.2 Required pinned e5f application to the same target family

The pinned `COUNTEREXAMPLE_SEARCH.md` proves the ruled one-sheet theorem for exact rank three with signature `(2+,1-)`: if all three nonzero eigenvalue magnitudes are at least one, then

`p_Q(t) <= pi sqrt(2)` for a.e. `t>=0`.                             (4.15)

The spectrum (4.9) has that signature, so the theorem applies literally:

`boxed:
 p_(Q_(m,eta))(t) <= pi sqrt(2)=4.442882938158366...
 for a.e. t>=0.`                                                     (4.16)

Thus a completed pinned result has been spent on an actual target inequality. The new theorem (4.13) additionally controls the entire real line, including the two-sheet side. The e5f counterexample search's failure to find a QFORM counterexample is not used as novelty evidence.

## 5. Relation to the newest interactive independent-square receiver

A newer owner-pinned interactive theorem gives a global `O(1/rho)` bound for

`2HL+beta L^2+V^2+2 epsilon LP`

when a positive portion of the square direction `V` lives on original coordinates unused by both `L` and `P`. That theorem is compatible but does not subsume (4.7): here the square direction `B` and leakage direction `V` overlap on **every** private coordinate, and in the distinct-ratio construction no positive square mass can be isolated on a source subset unused by the leakage. The present proof instead keeps the overlapping product bank intact and pays it with the two-dimensional Brascamp--Lieb integral (3.15).

Likewise, the newer dependent-shell obstruction says numerical two-dimensional projection caps alone cannot control the negative hyperboloid sheet. Equation (3.17) uses the actual coordinatewise product characteristic functions before projection, so it does not make that forbidden replacement.

## 6. Sharpened remaining debt

Inside an exact source-private `g_K=0` branch, there are now two complementary payments:

- exact alignment `eta=0`: account03/B18 r34, with the private-square currency `rho`;
- nonalignment `eta>0` plus diffuse normalized two-frame (3.5): the new aggregate bound (3.8), with currency `rho eta`.

The strict family above shows why selecting one aligned subbank can lose dimension even when the full private bank is harmless.

The first unpaid source-private implication is therefore:

`QFORM-PRIVATE-BANK-HEAVY-OR-NEARALIGNED-v1`: when useful private beta mass exists but every nonaligned private two-frame either has a coordinate leverage `>1/2` or has `rho eta` tending to zero, force an already-paid physical-pair/zero-edge/independent-square exit or retain enough product provenance for a heavy-row version of (3.17).

The broader null-hub obstruction remains the fully source-entangled case in which no substantial exact `g=0` private bank exists. No small nonzero `g_k` may be deleted: the live corrections give explicit unbounded-density proof-shortcut counterexamples to such perturbative replacements.

The unrestricted QFORM theorem remains OPEN / NOT PROVED / NOT DISPROVED.

## 7. Source and correction audit

Consumed fresh owner/control revision `2026-09-22.15`, the current exclusive-QFORM sign-in continuation, the current Fisher-information continuation (regular-input supporting theorem only), `MANIFEST/CURRENT_RESEARCH/CLAIMS/DELTAS/CORRECTION_INBOX/PATHWAYS/MEMORY_PROTOCOL`, assignment `account02/B18`, and the required `QFORM-PROOF-FIRST` and `QFORM-CLAUDE-LATEST` entrypoints.

Consumed pinned e5f source `e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.

Consumed designated partner account03/B18 r34:
`math-open-problems@12cb94062390a52deaf9a0c74b5d81aa41e5a128:proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T195443Z-account03-B18-QFORM-r34/REPORT.md`.

Primary external source checked: Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1.

Later corrections explicitly retained: `QFORM-B15-NONZERO-SQUARE-AFFINE-SLOPE-RESCUE-FALSE-v1`, `QFORM-NEARZERO-ARBITRARY-REMAINDER-EXTENSION-FALSE-v1`, `QFORM-GSTAR-SCALE-FORCING-FALSE-v1`, conditional-cap-not-independence, arbitrary-joint-coarea failure, and the negative-convex dependent-shell obstruction. None conflicts with (3.7), whose key integral is over original-coordinate characteristic functions.
