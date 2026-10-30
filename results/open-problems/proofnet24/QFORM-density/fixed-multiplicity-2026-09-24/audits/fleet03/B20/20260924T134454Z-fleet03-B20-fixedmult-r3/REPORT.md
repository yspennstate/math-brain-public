SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-24T13:44:54Z.

# fleet03/B20 r3 — fixed-multiplicity release gate and threshold ledger

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Model self-report: GPT-5.6 Sol. Configured reasoning effort/provider reasoning-token and thinking-time counters: UNKNOWN/not exposed.

Pinned baseline source:

- repository `yspennstate/math-open-problems`;
- commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`;
- blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## 1. Release-gate verdict

There are three different statuses and they must not be conflated.

1. **Literal pinned 17-eigenvalue source: GAP (repairable), not exact-source release-ready.** The singular-`A` paragraph of the Schur-count lemma regularizes by `A+epsilon I` and then moves a threshold in the limit. The valid repair is: fix `0<delta<t`, apply the invertible count at the fixed threshold `t-delta`, pass `epsilon->0`, and only then let `delta downarrow 0`. This yields the intended count `N_S(t)>=N_A(t)-k`. The repair does not change constants, but the pinned blob itself remains unpatched.

2. **Repaired 17-eigenvalue mathematical chain: PASS in the prior B20 reconstruction.** This is a statement about the repaired mathematics, not about the literal pinned source blob.

3. **Nine-eigenvalue replacement theorem: PASS at release-gate mathematical level with two genuinely separate complete reviews.** The safe independently reviewed constant is `6010`, because both fleet01/B16 and fleet02/B09 independently reconstruct the entire threshold-nine mechanism and obtain/validate that bound. A separate fleet01/B11 reconstruction and fleet02/B10 complete proof give still sharper constants, but this report does not promote a sharper constant beyond the two-review common denominator.

Accordingly the current release-grade fixed-multiplicity theorem is:

> **Theorem (independently reviewed threshold nine).** Let `X_1,...,X_n` be independent real random variables with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary real symmetric, and let `b,c` be arbitrary. If
> `s_9(A)>=s>0`,
> then
> `Q=X^T A X+b^T X+c`
> has an essentially bounded density satisfying
> `||p_Q||_infinity <= 6010 K^2/s`.
>
> No Gaussianity, log-concavity, moment, bounded-support, connected-support, iid, sign, diagonal-basis, exact-rank, leverage, or post-rotation-independence assumption is introduced.

Global continuity is **not** part of this release-grade theorem. The no-pivot Fourier branch below has a continuous `C_0` density; the scalar/pair pivot branches are presently closed by domination/potential estimates and only establish essential boundedness.

Independent complete reviews used for the release gate:

- fleet01/B16, commit `54ec2a651d854563f8db0d92c4c3426f76551786`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet01/B16/20260924T124038Z-r11/REPORT.md`: independent reconstruction, PASS, theorem constant `6010`;
- fleet02/B09, commit `51022fbf2819704f220b1dc6d5f1889f979ca77b`: independent reconstruction, PASS, theorem constant `6010`.

Additional complete supporting reconstructions/proofs include fleet02/B10 commit `6a3dcc2a560799c770b5db496e88179a31e566b6` and fleet01/B11 commit `c2f5f92b4d408190e4e2e0737135cf1623b4bdbb`.

## 2. Independent synthesis of the nine-direction proof

Normalize first to `K=s=1`, with the audited baseline parameters

`eta=1/100`, `kappa=1/80^2`.

### 2.1 Grouped product-Fourier compiler

Take disjoint literal original-coordinate banks `H,I,J`. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and write

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,  `X'=(X_I,X_J)`,

where `F` is arbitrary measurable, `R` arbitrary quadratic/affine, and `M_J` has row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Project the physical `I-J` crossing rows orthogonally off `row(M_J)` and call the residual row matrix `C`.

For `ell>=1`, set

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,

and determinant weights `w_T=det(C_T C_T^T)/Z_ell`, with inclusion marginals `alpha_i=sum_{T contains i}w_T`. If every positive `alpha_i<=1/2` and `d=k+ell`, then

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
 (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

The proof is product-law valid: the hub complex measure has `L^2` norm controlled by the projection density cap; the light-bank pushforward is mollified, squared with an independent copy only of the literal product bank, and passed to the limit by uniform `L^2` bounds/weak lower semicontinuity; weighted Holder is applied to literal physical rows; and the entropy inequality comes from ordering a sampled `ell`-subset. No projected coordinates are declared independent.

For `d>2`, integrating the envelope gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
 (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d))`.

### 2.2 Marginal-free order-three density receiver

For a literal physical crossing matrix `M`, put `Z=E_3(M)=e_3(MM^T)`. Let `J_i` be the incident third-volume mass at row `i`, so `sum_i J_i=3Z`.

If all `J_i/Z<=1/2`, use the compiler at `(k,ell,d)=(0,3,3)`. If one row is heavy, promote that literal row and project the remainder off it; exact Gram-Schmidt gives `J_i=||w||^2 e_2(CC^T)`. If a residual row is heavy for this second volume, promote it; then `H_ij=det(PP^T)||C_2||_F^2>J_i/2`. A final heavy residual row produces a literal three-row determinant `>H_ij/2`. The four branches are paid by compiler parameters `(0,3)`, `(1,2)`, `(2,1)`, or the exact rank-three terminal.

Thus

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.

Every branch has an integrable characteristic-function majorant, so this receiver gives a continuous `C_0` density.

### 2.3 Marginal-free order-two half-potential receiver

The same promotion tree one dimension lower gives

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

This is deliberately a half-potential estimate, not a rank-two bounded-density theorem.

### 2.4 No-pivot branch under nine large directions

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited spectral-to-volume proposition at crossing order `3` gives

`V_3(A)>=kappa^3`.

A fair partition into literal original-coordinate banks gives a crossing matrix with

`E_3(M)>=4^-3 kappa^3`, hence `E_3(M)^(-1/6)<=160`.

The order-three receiver yields

`||p_Q||_infinity <=160 C_3=2370.9340...<2400`,

with a continuous `C_0` density.

### 2.5 Scalar-pivot branch

A scalar pivot removes one original coordinate. The repaired Schur count leaves at least eight unit-scale directions.

If the Schur complement has a pivot, the audited pivot estimate gives truncated half potential at most `600`; the outside-unit tail costs at most one, so the full half potential is at most `601`.

If the Schur complement has no pivot, it in particular has `s_5>=1`. The order-two spectral-to-volume proposition plus a fair cut gives

`E_2>=4^-2 kappa^2`,

and therefore

`sup_a E|R-a|^-1/2 <= C_2 sqrt(160)=152.9919...<153`.

The outer scalar-square profile costs `eta^-1/2=10`, hence the scalar-pivot branch is bounded by

`10*601=6010`.

### 2.6 Pair pivots and scaling

A definite two-coordinate pivot has a direct density bound `<32`. An indefinite pair removes only two Schur directions, leaving at least seven unit-scale directions; the audited hyperbolic/log-potential receiver gives `<251`.

Thus `6010` dominates the normalized problem. For general `K,s`, set `Y=KX` and apply the normalized theorem to `A/s`; since `Q=(s/K^2) Qtilde`, density scaling gives

`||p_Q||_infinity <=6010 K^2/s`.

This completes the release-gate synthesis.

## 3. Threshold accounting: nine is currently the lowest complete theorem

Multiplicity eight is **not** closed. Recent independent work sharply localizes the obstruction but does not furnish the missing product-preserving endpoint.

One reviewed `s_8` terminal description is the overlap-one currency. In the no-pivot chamber with `s_8(A)>=1`, either the ordinary order-three crossing-volume gate fires, or one obtains a dimension-free lower bound for the repeated-anchor compound

`W_{2,1}(A)=sum_{S,T disjoint, |S|=|T|=2} sum_{h outside S union T}
 det A[S union {h}, T union {h}]^2`.

The difficulty is structural, not merely numerical: each large `3x3` bordered determinant repeats the same physical coordinate `h` on row and column sides. A fair disjoint coordinate cut cannot place that same independent coordinate on both sides. Treating `h` as a one-dimensional hub leaves, after projecting the two-by-two crossing off the hub row space, at most one genuinely new crossing direction in the smallest configuration, so the grouped compiler reaches total Fourier dimension `d=2`, the borderline half-potential regime rather than an `L^1` characteristic-function envelope. This explains why the existing `E_3` receiver cannot simply be applied to `W_{2,1}`.

A complementary `s_8` reduction (fleet03/B08 commit `5142196d67ec572a7146be423323f5f53945757e`) shows that if the parent and all one-/two-coordinate deletion children evade a diffuse spectral-window payment, there are three nested literal physical stars of norm at least

`c_* = 9/(6400 sqrt(2)) = 0.0009943689...`,

while the state simultaneously lies in the exact rank-two interpolation-saturation chamber. Those stars need not be linearly independent, so their row norms cannot be promoted to a third compound without a new argument.

Therefore the exact next mathematical interface is:

`QFORM-S8-OVERLAP-ONE/NESTED-STAR-PRODUCT-RECEIVER-v1`:
construct a bounded-density receiver for the repeated-anchor order-three currency (or show that the simultaneous nested stars plus rank-two saturation force an already-paid disjoint `E_3` crossing), while retaining all same-bank curvature and arbitrary cap-one product laws.

No threshold below nine is claimed here.

## 4. Constant sharpening status

Fleet03/B10 commit `636863855ed4c6c976785e35fae8d855f49450ea` gives a coherent sharpening of the nine-direction constant to `<2600 K^2/s`, using sharper singular-kernel and logarithmic-potential constants. This run has not supplied the two independent end-to-end reviews required to place `2600` at the same release grade as `6010`; therefore `2600` is recorded as **candidate sharpening**, not the release constant.

Fleet01/B11 commit `c2f5f92b4d408190e4e2e0737135cf1623b4bdbb` independently reconstructs a `<5338 K^2/s` version. Again, for this release-gate ledger the conservative common theorem with two explicit independent complete reviews is `6010 K^2/s`.

## 5. Scope and open status

- Release-grade fixed-multiplicity threshold in this synthesis: **9**.
- Safe two-review constant: **6010 K^2/s**.
- Literal pinned 17 manuscript: **repairable GAP, unpatched**.
- Repaired 17 mathematical chain: **PASS in B20 reconstruction**.
- Threshold 8: **OPEN**.
- Unrestricted three-large-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Global continuity at threshold nine: **not proved**; no-pivot `E_3` branch is `C_0`, pivot branches establish essential boundedness only.
- Native learned-memory receiver ingestion: **not verified**, so execution remains `WITHOUT_VERIFIED_BRAIN`.
