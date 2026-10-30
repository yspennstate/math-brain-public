# fleet03/B18 fixed-multiplicity audit r1

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T142238Z-fleet03-B18-QFORM-fixed-multiplicity-audit-r1`.
Role lens: primary-source prior-art verification plus complete proof audit; fleet03 emphasis on exact identities and alternative derivations.

## Source pin and scope

Pinned mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, declared SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines.

I read the complete manuscript and the package `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The current finite checker records PASS (534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, plus floating Schur/graph diagnostics), but it is correctly labeled a diagnostic rather than a proof.

## Verdict

**Pinned 17-eigenvalue theorem: PASS in this independent mathematical audit.** I find no FALSE mathematical statement or unfilled proof gap in the 790-line source. The theorem retains arbitrary independent cap-`K` one-dimensional densities, arbitrary symmetric `A`, arbitrary affine terms, arbitrary sign pattern and remaining spectrum, and proves an essential density bound. It does not silently assume moments, iid inputs, compact support, log-concavity, Gaussianity, smoothness, or independence after rotation.

**Nine-eigenvalue replacement: PASS in an independent reconstruction in this run.** Combining the baseline structural/pivot chain with the grouped product-Fourier mechanism gives, for `s_9(A)>=s>0`,

`||p_{X^TAX+b^TX+c}||_infinity <= 6010 K^2/s`.

I independently rederived the compiler and promotion identities rather than using a peer PASS as a premise. I also give below a primary-source Livshyts--Paouris--Pivovarov transfer which sharpens the internal order-three/order-two constants and independently closes the same nine-direction theorem. This is validation/sharpening, not a novelty claim.

**Threshold eight remains OPEN in this audit.** The present no-pivot structural argument can terminate at the order-two interpolation-saturation chamber, while the generic two-dimensional smoothing compiler gives a `|t|^-1` envelope, sufficient for a half-potential but not direct `L^1` Fourier inversion. I found no complete source-valid route from that chamber to a density bound.

**Global continuity remains unproved.** The no-pivot Fourier branches are `C_0`; pivot branches are controlled by measure domination / essential-density estimates.

## Complete source-line ledger

| Lines | Status | Independent check |
|---|---|---|
| 1--83 | PASS | Quantifiers, normalization, affine terms, essential-supremum scope and `K^2/s` scaling are consistent. |
| 84--168 | PASS | Fourier convention, Gaussian inversion, Plancherel, power-envelope integration and negative-half-moment normalization rederive correctly. |
| 169--217 | PASS | Singular-value perturbation and Schur spectral count are valid, including singular ambient `A`; diagonal dominance is used only as a rank contradiction. |
| 218--255 | PASS | Geometric rank-one Brascamp--Lieb heat-flow sign, frame contraction, integration by parts, large-time normalization and rough-input limiting argument are valid. |
| 256--301 | PASS | Product-projection argument preserves original product coordinates; deterministic rotations occur only in integration geometry. Scalar Fourier-power estimate is correctly normalized. |
| 302--373 | PASS | Decoupling uses independent copies of original coordinates only. Graph-frame weights and BL Jacobians give the stated regularized determinant bound and exponent `-1/8`. |
| 374--400 | PASS | Cauchy--Binet crossing volumes, order-five density endpoint and order-three half-potential endpoint are correct and are not interchanged. |
| 401--434 | PASS | Scalar-square domination and definite-pair density are measure-valid for rough densities and do not claim conditional independence after completion/rotation. |
| 435--482 | PASS | Hyperbolic pair parameterization, `1/(2 sqrt(D))` Jacobian, original-coordinate tail selection and logarithmic envelope are correct. |
| 483--525 | PASS | Quarter-power concentration: diagonal branch, random sign coordinate cut, determinant-envelope use, Gaussian smoothing and logarithmic layer cake all close. |
| 526--580 | PASS | Pivot/volume definitions, bordered determinant sampling, nonsymmetric interpolant support, global `rank R<=3r` and restricted `rank R[L,L]<=r` are all used with the correct scopes. |
| 581--645 | PASS | Spectral-to-volume contradiction, exact `4k-3` bookkeeping, random cut factor `4^-k`, and no-pivot analytic consequences are correct. |
| 646--724 | PASS | Singular kernels, scalar/definite/indefinite pivot half-potentials, truncated/full distinction and `s_9` half-potential proposition are correct. |
| 725--790 | PASS | Main case split is exhaustive; scalar pivot under `s_17` leaves enough Schur directions; pair branches close; scaling is exact; limitations/continuity disclaimer are accurate. |

No mathematical source range remains UNCHECKED in this run. The compiled PDF binary/visual rendering is UNCHECKED because the package does not include the PDF binary; this does not enter the proof.

## Sensitive derivations rechecked explicitly

### Singular Schur limit

Let `q=N_A(t)-k`. For the regularized matrices, the source obtains `N_{S_eps}(t-|eps|)>=q`. If `q>0`, this is exactly `s_q(S_eps)>=t-|eps|`, where `s_q` is the q-th singular value. Since `S_eps->S` in operator norm and singular values are continuous, `s_q(S)>=t`; because the count uses `>=`, equality at the threshold is retained. Thus the literal moving-threshold argument is valid.

### Nonsymmetric interpolation

For a nonsingular disjoint seed `B=A[S,T]`, `P=A[:,T]B^{-1}A[S,:]` has rank at most `r` and exactly interpolates rows `S` and columns `T`. Symmetrizing `P` would destroy the proof currency and is not done. The completion `A=D+R+E` has zero seed diagonal in `D`, zero diagonal in `E`, `rank R<=3r`, but crucially `rank R[L,L]<=r`; the spectral-to-volume contradiction uses both rank budgets separately.

### Spectral-to-volume contradiction

If `V_k<kappa^k`, a bad ratio `V_{r+1}/V_r<kappa` with `r<=k-1` gives `||E||<=1/16`. With `m=4k-3`, rank loss through `R` yields at least `r+1` diagonal entries of `D` of magnitude `>=1-1/16` outside the seed. On an `(r+1)` subset, `|R_ii|>=371/400` while each row's off-diagonal sum is `<4(1/7+1/16)=23/28`; strict diagonal dominance contradicts `rank R[L,L]<=r`.

### Hyperbolic pair

The level-set parameterization has Jacobian `1/(2 sqrt(D))`. The large-`|t|` tails are controlled by selecting an ORIGINAL coordinate whose coefficient in the expanding exponential direction is large, then using only its cap-one density and total mass one. No projected-coordinate independence is used. The resulting envelope is `D^-1/2(6+log_+(16 sqrt(D)/|z-v|))`.

## Primary-source prior-art verification

### Bennett--Carbery--Christ--Tao

Primary source: J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp--Lieb inequalities: finiteness, structure, and extremals*, arXiv:math/0505065. Its geometric Brascamp--Lieb framework and heat-flow monotonicity are genuine antecedents to the manuscript's rank-one theorem. The manuscript is self-contained here and proves exactly the specialization it needs, so no external constant is imported as an unproved premise.

### Rudelson--Vershynin

Primary source: M. Rudelson, R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492 / IMRN 2015. Its scope is independent real coordinates with bounded one-dimensional concentration/density, with no moment or log-concavity premise; the one-dimensional projection constant `sqrt(2)` is explicitly identified. The manuscript's weaker `sqrt(e)` / `e^(d/2)` projection estimates are self-contained and therefore source-safe.

### Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a product density with one-dimensional factors bounded by one, every k-dimensional orthogonal marginal is bounded by `2^(k/2)`. This exactly matches the rough product-law hypotheses used in the grouped compiler and requires no moments, support restriction, iid assumption, centering, smoothness or log-concavity.

I did not find an exact published theorem in this targeted search that states the present arbitrary-rough fixed-multiplicity quadratic-form density theorem. Search non-discovery is not novelty evidence; exhaustive novelty/priority remains UNCHECKED. Herry--Malicet--Poly (arXiv:2303.09488) assumes iid inputs admitting a sufficiently smooth Gaussian-field representation, so it does not subsume the present rough/non-iid theorem.

## Independent nine-direction reconstruction with sharp marginal transfer

The grouped compiler starts from disjoint ORIGINAL-coordinate banks `H,I,J` and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`.

Here `W` is k-dimensional with density cap `M_H`; the `J` restriction `M_J` has full row rank k with singular-value product `S`. Project the residual physical `I-J` crossing rows orthogonally off `row(M_J)` to obtain rows `c_i`. For an ell-subset volume law

`w_T=det(C_TC_T^T)/Z_ell`, `alpha_i=P(i in T)`,

assume `alpha_i<=1/2` and set `d=k+ell`.

Condition first on the literal `I` bank when estimating the light-bank complex pushforward. Jensen reduces its squared L2 norm to a copy only of the literal `J` bank. Thus `D=X_J-X'_J` has independent coordinates with densities bounded by one, and the remaining integral is

`E_D[kappa(M_J D) prod_i |psi_i(2t<a_i,D>)|]`.

For each determinant subset T, the linear image

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant `S^2 det(C_TC_T^T)`. LPP Theorem 1.1 therefore gives density cap

`2^(d/2)/(S sqrt(det(C_TC_T^T)))`.

A second LPP transfer sharpens the scalar Fourier powers. If `0<=f<=1`, `int f=1`, and `p>=2`, put `m=floor(p/2)`. Since `|hat f|<=1`,

`int |hat f|^p <= int |hat f|^(2m) = 2pi p_{sum_{j=1}^m(X_j-X'_j)}(0)`.

The coefficient vector has norm `sqrt(2m)`, while the normalized one-dimensional projection density is at most `sqrt(2)`. Hence the sum density is at most `1/sqrt(m)` and

`int |hat f|^p <= 2pi/sqrt(m) <= 4pi/sqrt(p)`.

At scale `2t`, this gives

`int |psi_i(2t(y+u))|^(1/alpha_i) dy <= 2pi sqrt(alpha_i)/|t|`.

Weighted Holder and entropy subadditivity for a uniformly ordered random ell-subset give

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining with hub Plancherel yields the source-sharpened envelope

`|phi_Q(t)| <= min(1, Ksharp |t|^(-d/2))`,

where

`Ksharp = M_H^(1/2) pi^(d/2) 2^((k+3ell)/4) (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

For `d>2`, direct inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^((k+3ell)/(2d)) (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

No random-variable rotation is used. In promotion branches, a full-dimensional orthogonal change inside k promoted physical hub coordinates preserves their joint density cap by determinant one; it does not make the transformed components independent and no such claim is needed.

### Order three

For a physical cross block B and `Z=E_3(B)=e_3(BB^T)`, the standard heavy-row promotion tree has branches `(k,ell)=(0,3),(1,2),(2,1)` and an exact rank-three terminal. The diffuse branch is the largest and gives

`||p_Q||_infinity <= C3sharp Z^(-1/6)`,

`C3sharp = 3*2^(3/2)*(9/2)^(1/6) = 6^(4/3) = 10.90272355699...`.

The heavy branches are smaller: the first promotion uses `J_i=||w||^2 E_2(C)>Z/2`; the second uses `det(PP^T)||C_2||_F^2>Z/4`; the terminal three-row Gram determinant is `>Z/8`. These identities are exact Gram--Schmidt base-times-height formulas and never divide by an arbitrarily selected small minor.

### Order two

The analogous promotion tree yields

`sup_a E|Q-a|^(-1/2) <= C2sharp E_2(B)^(-1/8)`,

`C2sharp = 8*2^(3/8) = 10.37471643721...`.

The diffuse `(0,2)` branch is largest; the promoted `(1,1)` and exact-rank-two terminal are smaller. This is a half-potential theorem, not a rank-two density theorem.

### Nine eigenvalues

Normalize `K=s=1`, `eta=1/100`, `kappa=1/80^2`.

- No pivot + `s_9(A)>=1`: the baseline `k=3` structural theorem gives `V_3>=kappa^3`; a fair coordinate cut gives `E_3>=4^-3 kappa^3`, hence `E_3^-1/6<=160`. The sharp source-transfer receiver gives `||p_Q||_infinity <= 160*6^(4/3) = 1744.435769... < 1800`.
- Scalar pivot: the Schur complement retains at least eight unit-scale directions. If it has a pivot, baseline pivot control gives full half-potential `<=601`. If it has no pivot, its `s_5>=1`; the baseline `k=2` structural theorem and fair cut give `E_2>=4^-2 kappa^2`, so the sharp source-transfer receiver gives full half-potential `<=C2sharp*sqrt(160)=131.230936...<132`. Thus the safe common bound is still 601, and the scalar square profile gives density `<=6010`.
- Definite two-coordinate pivot: direct conditional density `<10pi`.
- Indefinite two-coordinate pivot: Schur complement retains at least seven unit-scale directions, hence operator norm at least one; baseline hyperbolic/logarithmic control gives `<251`.

Therefore the complete arbitrary-law theorem

`boxed: s_9(A)>=s>0 => ||p_Q||_infinity <= 6010 K^2/s`

is independently closed in this run. The LPP transfer improves the internal no-pivot constants but not the global 6010 bottleneck without a separate pivot-constant improvement.

## Threshold and publication status

- Pinned `s_17` manuscript: mathematically PASS here.
- `s_9` replacement: mathematically PASS here by independent reconstruction; this run does not overwrite the pinned baseline or self-award a release certificate.
- `s_8`: OPEN.
- unrestricted `s_3`: OPEN.
- global continuity: OPEN.
- historical checker-suite reproduction: package provenance GAP only; current checker explicitly disclaims reproducing the older suite.
- exhaustive literature novelty/priority: UNCHECKED.

No task state, schedule, notification, email, public-release, cross-account-authentication, paid API/model, installation or permission setting was changed in this run.