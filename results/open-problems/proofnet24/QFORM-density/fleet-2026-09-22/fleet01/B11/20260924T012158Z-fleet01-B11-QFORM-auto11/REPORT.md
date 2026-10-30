SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-24T01:21:58Z.
attacking: the rank-one-transverse one-sided-leakage collar; recover a genuine rank-three ORIGINAL-coordinate crossing by adjoining the physical hub to the correct source bank.

# fleet01/B11 auto11 — hub-augmented crossing trichotomy for the rank-one transverse collar

Programme: `QFORM-DENSITY-3EIG-20260922`.
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.
Owner control revision: `2026-09-22.15`.
Status: **NEW STRUCTURAL TRICHOTOMY / NEW CONTINUOUS ONE-SIDED BRANCHES / DESIGNATED PARTNER RESULT APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, finite-fragmentation, post-rotation independence, conditional-density-cap, arbitrary-joint coarea, pointwise law-uniform van-der-Corput estimate, or perturbative deletion of a small coefficient is used. The new estimates below are quantitative but are not uniform as the surviving leakage size tends to zero; the exact double-aligned collar remains open.

## 1. Fresh source state

Fresh `math-research-brain/main` control was read at the start and again immediately before publication. The current owner control remains revision `2026-09-22.15`, QFORM-only, and `CLAIMS.json` still marks `QFORM-FULL` and the full continuous-representative claim OPEN.

The immediate predecessor for this slot is:

- `yspennstate/math-open-problems@375b36740eb56e2f22aa3c0e87e0cd9d10f9eaab`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260924T004226Z-fleet01-B11-QFORM-auto11/REPORT.md`.

It established the **bilateral-leakage** identity in the rank-one transverse branch: if both off-axis leakage vectors are nonzero then the physical pivot vanishes and the original `L x R` crossing has three-dimensional singular volume
`Delta_3(N)=sigma ||p_0|| ||q_0||`.

The completed designated-partner theorem used below is fleet02/B11:

- `yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T201026Z-fleet02-B11-QFORM-auto11/REPORT.md`,
- theorem `QFORM-3D-PROJECTION-CROSS-L2-v1`.

Its exact statement needed here is: if two disjoint ORIGINAL-coordinate source banks have rank-three cross matrix `K`, while every same-bank quadratic term and every affine term is retained as arbitrary phases, then
`Q` has a continuous `C_0` density and
`||p_Q||_infinity <= 6 Delta_3(K)^(-1/3)`,
where `Delta_3(K)=s_1(K)s_2(K)s_3(K)`. More generally, if the two three-dimensional projected bank laws have joint density caps `M_X,M_Y`, the bound is
`3 (M_X M_Y / Delta_3(K))^(1/3)`.

The newest fleet02/B11 run was also read. Its `QFORM-HYPERBOLIC-PAIR-L2-ONE-SIDED-CURVATURE-v1` remains a useful source-disjoint L2 receiver, but it does not by itself justify replacing two projections of the same product bank by independent variables. I do not use that forbidden replacement here.

## 2. Canonical rank-one transverse geometry

Fix one ORIGINAL coordinate `i` (the physical hub) and disjoint ORIGINAL-coordinate banks `L,R`. Write

`a=A_ii`,
`c=A[L,i]`,
`r=A[i,R]`,
`N=A[L,R]`.

Assume `c,r` are nonzero. Set

`alpha=||c||`, `beta=||r||`,
`e=c/alpha`, `f=r/beta`,
`P_e=I-ee^T`, `P_f=I-ff^T`.

Suppose the transverse crossing

`C=P_e N P_f`

has rank one. Choose unit singular directions `u in e^perp`, `v in f^perp` and singular value `sigma>0` so

`C=sigma u v^T`.

Define the two off-axis leakage vectors

`p_0=P_{span(e,u)^perp} N f`,
`q_0=P_{span(f,v)^perp} N^T e`.

After deterministic orthogonal changes of basis **inside coefficient spaces only** (not probabilistic rotations of the input law), the cross block has the exact form

```
          f       v       F_0
e       [ d      q_1      q_0^T ]
u       [ p_1    sigma    0     ]
E_0     [ p_0    0        0     ].
```

This is only a matrix identity. No claim of independence between the displayed projected coordinates is made.

## 3. New theorem: hub-augmented crossing trichotomy

### Theorem `QFORM-RANK1-TRANSVERSE-HUB-AUGMENTED-TRICHOTOMY-v1`

In the preceding rank-one-transverse setup, define

`K_R=A[{i} union L, R] = [ r^T ; N ]`

and

`K_L=A[L, {i} union R] = [ c | N ]`.

Then:

1. **Bilateral leakage.** If `p_0 != 0` and `q_0 != 0`, the inherited exact-rank-three identity gives
   `a=0` and
   `Delta_3(N)=sigma ||p_0|| ||q_0||`.

2. **Right-only leakage.** If `p_0=0` and `q_0!=0`, then `K_R` has rank exactly three and
   `boxed(Delta_3(K_R)=beta sigma ||q_0||)`.

3. **Left-only leakage.** If `q_0=0` and `p_0!=0`, then `K_L` has rank exactly three and
   `boxed(Delta_3(K_L)=alpha sigma ||p_0||)`.

4. **Double alignment.** If `p_0=q_0=0`, then
   `rank N<=2`, `rank K_R<=2`, and `rank K_L<=2`.
   Thus none of these three natural source-disjoint cuts contains a third crossing direction. The third spectral direction must then be paid by the aligned shared-hub/same-bank-curvature mechanism rather than by a three-dimensional cross volume.

### Proof

The bilateral statement is the previous B11 theorem, so only (2)--(4) are new here.

For (2), rotate the `F_0` coefficient subspace so its first basis vector is `q_0/||q_0||`. Because `p_0=0`, every `E_0` row of `N` vanishes. Because the transverse block has rank one, every `F_0` column except the `q_0` direction also vanishes. Therefore `K_R` is supported on the exact active `3 x 3` block with row basis `(hub,e,u)` and column basis `(f,v,qhat)`:

```
K_R,act =
[ beta    0       0          ]
[ d       q_1     ||q_0||    ]
[ p_1     sigma   0          ].
```

Its determinant is

`det K_R,act = - beta sigma ||q_0||`.

All remaining rows and columns are zero. Hence the three nonzero singular values of `K_R` are exactly those of this active block and

`Delta_3(K_R)=|det K_R,act|=beta sigma ||q_0||`.

For (3), rotate `E_0` so its first basis vector is `p_0/||p_0||`. Since `q_0=0`, all `F_0` columns of `N` vanish. The active `3 x 3` block of `K_L`, with rows `(e,u,phat)` and columns `(hub,f,v)`, is

```
K_L,act =
[ alpha   d       q_1   ]
[ 0       p_1     sigma ]
[ 0       ||p_0|| 0     ].
```

Therefore

`det K_L,act = - alpha sigma ||p_0||`

and

`Delta_3(K_L)=alpha sigma ||p_0||`.

For (4), if both leakage vectors vanish, `N` is supported on the two-dimensional row space `span(e,u)` and the two-dimensional column space `span(f,v)`, so `rank N<=2`. Appending the hub row `r^T=beta f^T` does not enlarge the column support beyond `span(f,v)`, hence `rank K_R<=2`. Appending the hub column `c=alpha e` does not enlarge the row support beyond `span(e,u)`, hence `rank K_L<=2`. QED.

The theorem is useful because every nonzero leakage configuration now has a **source-valid third direction**: it is either already in the `L x R` cross block (bilateral leakage), or it appears after adjoining the physical hub to exactly one of the two ORIGINAL source banks (one-sided leakage). No eigen-coordinate independence is invoked.

## 4. Density consequences from the designated fleet02/B11 theorem

Condition on all ORIGINAL coordinates outside the two banks used in the relevant cut. Conditioning only creates arbitrary within-bank quadratic/affine phases, which are explicitly allowed in `QFORM-3D-PROJECTION-CROSS-L2-v1`.

Therefore:

- if `p_0,q_0 !=0`,
  `||p_Q||_infinity <= 6 (sigma ||p_0|| ||q_0||)^(-1/3)`;

- if `p_0=0`, `q_0!=0`,
  `boxed(||p_Q||_infinity <= 6 (beta sigma ||q_0||)^(-1/3))`;

- if `q_0=0`, `p_0!=0`,
  `boxed(||p_Q||_infinity <= 6 (alpha sigma ||p_0||)^(-1/3))`.

All three branches have continuous `C_0` densities because the partner proof gives an `L^1` Fourier envelope.

Quantitatively, if the relevant three factors are each at least `eta s`, then the corresponding branch obeys

`||p_Q||_infinity <= 6 eta^(-1) s^(-1)`.

The theorem does **not** make this uniform as a leakage factor tends to zero; the exact double-aligned collar remains the first unpaid branch.

## 5. Actual target-valid one-sided-leakage example

The one-sided mechanism is not empty. Consider the exact symmetric matrix

```
A_* =
[ 1  1  0   1  0  0 ]
[ 1  2  0   0  0  1 ]
[ 0  0 -1   0  1  0 ]
[ 1  0  0   2  0 -1 ]
[ 0  0  1   0 -1  0 ]
[ 0  1  0  -1  0  1 ].
```

Take hub `i=0`, `L={1,2}`, `R={3,4,5}`. Then

`c=(1,0)^T`, so `alpha=1`,
`r=(1,0,0)^T`, so `beta=1`,

and

```
N=A_*[L,R]=
[0 0 1
 0 1 0].
```

Thus `e=(1,0)`, `f=(1,0,0)`, the transverse crossing has rank one with `sigma=1`, and

`p_0=0`, `||q_0||=1`.

The hub-augmented cross matrix is

```
K_R=A_*[{0,1,2},R]=
[1 0 0
 0 0 1
 0 1 0],
```

so `Delta_3(K_R)=1`.

Moreover the exact characteristic polynomial is

`chi_A(lambda)=lambda^3 (lambda-3)^2 (lambda+2)`,

hence the nonzero spectrum is `{3,3,-2}`. This is a genuine target-valid `(+,+,-)` matrix, and `-A_*` is a target-valid `(+,-,-)` matrix.

For arbitrary independent cap-one inputs `X_0,...,X_5`, apply the designated fleet02/B11 theorem directly to the ORIGINAL split
`S={0,1,2}`, `T={3,4,5}`. Here the two three-dimensional bank laws themselves have joint density caps at most one and `|det K_R|=1`, so the sharper general form of the partner bound yields

`boxed(||p_(X^T A_* X)||_infinity <= 3)`.

The density is continuous and `C_0`. The same bound holds for `-A_*` by reflection. This is an actual inequality in both indefinite signatures, not merely a structural citation.

## 6. Rank-two logarithmic control and the role of the third direction

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`.

Thus one opposite-sign hyperbolic pair really has an unbounded density.

The present theorem identifies the third smoothing direction without rotating the probability law:

- bilateral leakage: the third source direction is the genuine `L x R` volume
  `sigma ||p_0|| ||q_0||`;
- right-only leakage: it is the hub-augmented source volume
  `beta sigma ||q_0||`;
- left-only leakage: it is the reflected hub-augmented volume
  `alpha sigma ||p_0||`.

The partner Fourier proof converts any such nonzero three-dimensional cross volume into `|t|^(-3/2)` decay, while a rank-two crossing produces only the borderline `|t|^(-1)` scale. Hence the third direction removes the logarithmic singularity here by an ORIGINAL-coordinate source-crossing volume, not by fictitious independence of rotated eigen-coordinates.

## 7. Exact remaining implication

The rank-one-transverse branch is now localized to the **double-aligned endpoint**

`p_0=q_0=0`.

After star-preserving determinant-one shears, its interbank crossing can be written on the active two-dimensional bank projections as

`delta Y_1 Z_1 + sigma Y_2 Z_2`

while the same physical hub couples to `alpha Y_1 + beta Z_1`, and arbitrary same-bank quadratic phases remain.

This is precisely where the newest fleet02/B11 direct operator calculation warns that an arbitrary hub phase can cancel a tempting extra oscillatory gain. Therefore the next B11 implication is:

`QFORM-RANK1-TRANSVERSE-DOUBLEALIGNED-RANK2-CURVATURE-v1`:

> Obtain a universal bound through the double-aligned rank-two crossing by using the exact-rank-three same-bank curvature/product-projection provenance, or force an already-paid physical-pair, tensor, ruled, or cross-volume exit. Do not condition on dependent projected coordinates, and do not delete a small coefficient on unbounded inputs.

A second, separate full-target bridge remains: arbitrary additional nonseparable spectrum beyond the exact-rank-three reduction.

## 8. Verification

`VERIFY.py` in this run directory performs:
- 5,000 right-only random canonical checks of
  `Delta_3(K_R)=beta sigma ||q_0||`;
- 5,000 left-only checks of
  `Delta_3(K_L)=alpha sigma ||p_0||`;
- 5,000 bilateral checks of
  `Delta_3(N)=sigma ||p_0|| ||q_0||`;
- the exact target matrix check: rank three, spectrum `{-2,0,0,0,3,3}`, determinant-one hub-augmented cross block, and partner bound `3`.

The observed worst relative singular-volume discrepancies were below `3e-14`; the script ends
`QFORM_B11_HUBAUGMENTED_TRICHOTOMY_CHECK_PASS`.

## 9. Scope and integrity

This is a supporting theorem, not a full solution. Continuity is proved in the three nonzero-leakage branches through the designated partner's integrable Fourier estimate. No continuity or universal height bound is claimed for the double-aligned endpoint or the full target.

A repository search before publication found no source-matching statement of the one-sided hub-augmented identities. The bilateral identity is explicitly inherited rather than re-claimed as new.

No scheduler/task state, cadence, enabled/paused state, email, notification, public release, cross-account authentication, permissions, paid model/API call, remote workflow, or installation setting was changed.
