# account03/B08 r55 — full textual audit, interpolation/rank lens

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: account03/B08  
Run: `20260924T114807Z-account03-B08-fixedmult-audit-r55`  
Canonical manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current-master manuscript blob observed in this run: the same `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS as a complete textual proof audit; no fatal mathematical gap found in the 17-eigenvalue theorem.** This is one worker review, not the two-review independent-validation gate and not a claim about the unrestricted three-eigenvalue conjecture.

The B08-sensitive nonsymmetric interpolation argument is correct. In particular:

1. `P=A_{.,T} B^{-1} A_{S,.}` really interpolates rows `S` and columns `T` without requiring symmetry.
2. With the manuscript definitions of `D,E,R`, one has exactly `R[L,L]=P[L,L]`, so `rank R[L,L] <= r`.
3. The correction `Q:=R-P` has support only in rows `T` or columns `S`; more precisely
   `Q = Pi_T Q + (I-Pi_T) Q Pi_S`, hence `rank Q <= 2r` and therefore `rank R <= 3r`.
4. `D` vanishes identically on `S union T` by construction.
5. The spectral-to-volume contradiction correctly combines the global `3r` rank loss with the restricted `r` rank contradiction and needs `m>=4r+1`; for the worst sampled order `r=4`, this is exactly `m>=17`.

I also found one **repository/reproducibility GAP, not a proof gap**: at the current master snapshot inspected in this run, the manuscript root contained only `README.md`, `AUDIT.md`, and `manuscript.tex`. `README.md` and the current objective refer to `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but those files were not present in the root directory listing. Therefore the finite-check claims could not be independently rerun from the currently published root. The mathematical manuscript is self-contained, so this does not invalidate the theorem proof.

## End-to-end source audit

The entire 790-line `manuscript.tex` was read from beginning to end in this run. Statuses below refer to the pinned source blob above.

| Source range / statement | Status | Independent reasoning in this run | Downstream impact |
|---|---|---|---|
| lines 1–120, theorem statement, normalization, Fourier inversion | PASS | Quantifiers retain arbitrary independent cap-`K` laws, arbitrary symmetric `A`, affine `b,c`, and scaling `Y=KX` gives density cap one and final factor `K^2/s`. Fourier normalization is consistent with `hat f(t)=int e^{itx}f(x)dx`. | Main statement/scaling sound. |
| lines 121–240, power envelope, Riesz half-potential, singular-value perturbation, Schur count | PASS | Recomputed the Riesz constant `1/sqrt(2 pi)` from the gamma/Gaussian integrals; the weighted envelope integrates to `12 sqrt(u)`. Singular-value rank inequality is used in the correct direction. The Schur-count argument through the complementary block of `A^{-1}` is valid, including the singular limit. | Pivot spectral counts are supported. |
| lines 241–360, geometric BL, product projections, scalar Fourier powers, decoupling setup | PASS | Heat-flow sign is correct: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`; the `t->infty` normalization uses `sum c_i=d`. Projection proof never rotates independence. Scalar Fourier power uses an actual sum of independent differences. Decoupling conditions only on original coordinate blocks. | Determinant theorem premises are sound. |
| lines 361–480, determinant conclusion, crossing volumes, scalar/definite/hyperbolic local changes | PASS | BL scale factors and cancellation at `alpha=(2 pi e)^2` are consistent; fourth root gives exponent `-1/8`. `k=5` gives `|t|^{-5/4}` and direct density, while `k=3` is used only with the Riesz weight. Definite pair uses original-coordinate joint cap; hyperbolic coordinates parameterize level sets rather than asserting rotated independence. | No hidden conditional-independence shortcut found. |
| lines 481–600, hyperbolic tails, quarter-power concentration, `lem:sampling`, `lem:completion` | PASS | Tail monotonicity can choose different physical coordinates on the two tails; the proof only needs existence. Quarter-power random sign cut correctly extracts a crossing block with norm at least `L/4`. The ordered-minor sampling count is an inequality because singular seeds may have nonsingular extensions. Detailed interpolation/rank derivation is given below. | Sensitive algebraic core passes. |
| lines 601–720, `prop:volume`, random cut, no-pivot consequences, kernels, pivot half-potential | PASS | Rechecked `m=4k-3`, `r<=k-1`, hence `m>=4r+1`; after losing `3r` singular directions there are at least `r+1` large entries of `D`, all in `L`. Diagonal dominance contradicts `rank R[L,L]<=r`. Kernel and pivot constants remain below the manuscript ceilings. | 9- and 17-direction no-pivot branches close as stated. |
| lines 721–790, nine-direction half potential, main proof, general `K,s` scaling | PASS | Pivot/no-pivot case split is exhaustive. Scalar pivot leaves at least 16 directions, hence enough for the nine-direction input. Indefinite pair leaves at least 15, and only one surviving direction is used for the logarithmic potential. Final normalized branch maxima are `<6010`, `<2400`, `<40`, `<251`; scaling gives `10000 K^2/s`. | Candidate theorem closes. |
| Supplementary finite-check package cited by README/AUDIT | GAP | `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were absent from the current root listing. | Reproducibility/documentation gap only; no theorem dependency because the proof is in `manuscript.tex`. |

## Detailed B08 derivation: nonsymmetric interpolation support

Let `S,T` be disjoint `r`-sets, `B=A[S,T]` invertible, `L=[n]\(S union T)`, and

`P=A[:,T] B^{-1} A[S,:]`.

No symmetry of `P` is needed. Direct multiplication gives

`P[S,:]=B B^{-1}A[S,:]=A[S,:]`,

`P[:,T]=A[:,T]B^{-1}B=A[:,T]`.

The manuscript sets `E[L,L]=off(A[L,L]-P[L,L])`, all other entries of `E` zero, and sets

`D_ii=A_ii-P_ii` for `i in L`, `D_ii=0` on `S union T`.

With `R=A-D-E`, the diagonal and off-diagonal parts on `L x L` separately give the exact identity

`R[L,L]=P[L,L]`.

Moreover `R-P` vanishes on every row in `S`, every column in `T`, and on all of `L x L`. Write `Pi_T` for row projection to `T` and `Pi_S` for column projection to `S`. Then

`R-P = Pi_T(R-P) + (I-Pi_T)(R-P)Pi_S`.

The two terms have ranks at most `r` and `r`, respectively. Hence

`rank(R-P)<=2r`,

`rank R <= rank P + rank(R-P) <= r+2r=3r`.

On the seed complement,

`R[L,L]=A[L,T] B^{-1} A[S,L]`,

so

`rank R[L,L] <= r`.

This independently verifies both rank statements and the exact support statement used later in `prop:volume`.

## Exact adversarial example: both rank bounds are sharp already at r=1

The following rational symmetric matrix also satisfies the manuscript's `eta=1/100` **no-pivot** inequalities:

`A = [[1/1000, 1/1000, 1/500],
      [1/1000, 3/1000, 1/250],
      [1/500,  1/250,  0]]`.

Take `S={1}`, `T={2}`, `L={3}`. Then `B=1/1000` and

`P = [[1/1000,1/1000,1/500],
      [3/1000,3/1000,3/500],
      [1/250, 1/250, 1/125]]`.

Since `L` has one element, `E=0`, while `D_33=-1/125`. Thus

`R = [[1/1000,1/1000,1/500],
      [1/1000,3/1000,1/250],
      [1/500, 1/250, 1/125]]`.

Exact arithmetic gives

`det R = 1/250000000 != 0`, hence `rank R=3=3r`;

`rank R[L,L]=1=r`;

and `rank(R-P)=2=2r`.

The no-pivot checks are also exact:

`max_i |A_ii| = 3/1000 < 1/100`,

while the three principal `2x2` determinant moduli are

`1/500000`, `1/250000`, and `1/62500`, all `<1/100`.

Therefore neither `rank R<=3r` nor `rank R[L,L]<=r` can be lowered in general by a purely formal sharpening of this same construction. In particular, the present `4r+1` spectral accounting cannot be improved merely by replacing either rank constant with a smaller universal coefficient. Any threshold below seventeen must use genuinely new structure or a different analytic receiver.

## Spectral-to-volume arithmetic

In the bad-volume branch choose `0<=r<=k-1` with `V_{r+1}<kappa V_r`. For `r>0`, `eps=||E||<= (r+1)/80 <=1/16`. With `m=4k-3`,

`s_m(D+R)=s_m(A-E)>=1-eps`.

Since `rank R<=3r`,

`s_{m-3r}(D)>=1-eps`.

And because `m>=4r+1`, `m-3r>=r+1`, so at least `r+1` diagonal entries of `D` have modulus at least `1-eps`. They all lie in `L`. On an `(r+1)`-set `H` of such coordinates,

`|R_ii| >= 1-eps-eta >=371/400`,

whereas, using no pivot and `|E_ij|<=eps`,

`sum_{j!=i}|R_ij| < r(1/7+1/16) <= 23/28 <371/400`.

Thus `R[H,H]` is invertible and has rank `r+1`, contradicting `rank R[L,L]<=r`. Every inequality is in the needed direction; nonsymmetry of `R` is harmless because strict row diagonal dominance and singular-value rank perturbation require no symmetry.

## Constants independently recomputed

- `12 sqrt(80e) = 176.96... <200`.
- `800e = 2174.63... <2400`.
- Scalar pivot half-potential: `10(20+12 log 16) = 532.71... <560<600`.
- Definite pair half-potential: `40 pi =125.67... <160`.
- Indefinite pair truncated half-potential upper bound is `<444` as stated.
- Main scalar branch: `6010<10000`.
- Main indefinite-pair branch: `10(10+5 log 16)+1/e = 238.996... <251`.

These are arithmetic checks, not substitutes for the proofs above.

## Threshold reduction conclusion from this lens

No valid lower multiplicity theorem was obtained in this run. The exact rank-sharp example shows that the obvious B08 route—replace `3r` by `2r`, or replace the restricted `r` by `r-1`—is false even in a no-pivot configuration. The order-five Fourier receiver still requires crossing order strictly greater than four, and the current interpolation contradiction at the worst ratio `r=4` genuinely asks for five large diagonal entries after the global low-rank loss. Therefore lowering 17 requires a new mechanism (for example a stronger order-four endpoint receiver or additional symmetric structure not captured by the present nonsymmetric interpolation decomposition), not a cosmetic rank recount.

## Next obligations

1. Restore/publish the missing `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` if their intended source artifacts still exist, or correct the README/AUDIT claims if they do not.
2. Seek a genuinely new threshold-lowering step; this B08 audit rules out the simplest rank-bound shortcut.
3. Preserve the pinned baseline and wait for a second genuinely separate complete review before any independent-validation label.

Status: `WITHOUT_VERIFIED_BRAIN`; repository read/write is not native brain ingestion.
