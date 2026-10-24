# account02/B03 r12 — full fixed-multiplicity audit and endpoint-copy obstruction

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141710Z-account02-B03-fixed-multiplicity-audit-r12`  
Logical role: B03, decoupling / copies / conditional independence / exponent transfer; account02 counterexample emphasis.

## Source pin and review scope

I resolved fresh `math-open-problems` master before the review at `e1644f9d140e605f1ec5ab058328dd63d63daced`, and refreshed it before publication at `122a92fbfd1f6cc6d228666fa56d9e7ffea16b65`. At both refs the manuscript has the identical Git blob

`183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Package-declared / checker-pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Source size: 47,883 bytes, 790 lines.

I read the complete package at the pinned current blob: `README.md`, `DELIVERY_STATUS.md` (required by the README), `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. I also independently reran the finite checker logic for its algebraic and numerical counts. The compiled binary PDF is not present in this GitHub root, so the package's PDF compilation/render claim is **UNCHECKED by this run**.

## Executive verdict

**PASS** for the stated 17-singular-value bounded-density theorem in this B03 review. I found no fatal mathematical gap in the 790-line proof. This is a worker review, not formal verification or a self-awarded independent-validation certificate.

**No threshold below 17 is proved here.** The current order-four route at `s_13` remains an endpoint problem. This run adds an explicit source-valid counterexample showing that the natural B03 attempt to combine an order-four `O(1/|t|)` characteristic-function envelope with a uniform negative-half potential, or even with a bounded density for the independent-copy difference, is insufficient to imply a one-copy `L^infty` density bound. This does not refute an `s_13` theorem; the witness has only two large eigenvalues.

The unrestricted three-eigenvalue QFORM conjecture remains **OPEN**.

## Complete line-status ledger

| source lines | status | audit finding |
|---|---|---|
| 1–45 | PASS | LaTeX setup, abstract, definitions and scope agree with the theorem actually proved. |
| 47–82 | PASS | Main quantifiers, `s_17`, affine terms, normalization plan, pivot/no-pivot architecture, and explicit no-rotated-independence caveat are consistent. |
| 84–120 | PASS | Fourier convention, Plancherel, inversion, Gaussian regularization, weak identification of the density. Constants checked. |
| 122–160 | PASS | Power envelope and negative-half Riesz bound; gamma normalization and weighted exponent checked. |
| 161–217 | PASS | Singular-value perturbation, Schur spectral count including singular `A`, strict diagonal dominance. |
| 221–255 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof and rough-law limiting steps. |
| 258–301 | PASS | Product-projection density and integrated scalar Fourier powers. Deterministic rotations are integration coordinates only. |
| 303–324 | PASS | Decoupling, independent-copy construction, independence provenance of difference coordinates, Jensen fourth-power transfer. |
| 326–400 | PASS | Regularized crossing determinant, graph weights, determinant exponent `-1/8`, crossing-volume exponents and constants. |
| 401–421 | PASS | Scalar square profile and conditional domination formula; no false independence between square and Schur remainder. |
| 423–434 | PASS | Definite two-coordinate estimate and deterministic orthogonal diagonalization. |
| 435–482 | PASS | Hyperbolic-pair Jacobian, original-coordinate tail selection, rough-density exceptional-slice handling. |
| 483–525 | PASS | Quarter-power concentration, random sign cut, Gaussian smoothing, atom exclusion, logarithmic potential. |
| 526–542 | PASS | Pivot and disjoint-volume definitions; no-pivot entry estimates. |
| 545–564 | PASS | Volume-sampled interpolation, bordered determinant identity, ordered multiplicity bound; inequality correctly allows singular seeds with nonsingular extensions. |
| 566–580 | PASS | Completion `A=D+R+E`, support, `D=0` on seed, global `rank R<=3r`, restricted `rank R[L,L]<=r`. |
| 582–619 | PASS | Spectral-to-volume proposition; nonsymmetric singular-value perturbation and diagonal-dominance contradiction checked. |
| 621–645 | PASS | Random-cut factor `4^{-k}` and no-pivot order-three/order-five analytic consequences. |
| 647–674 | PASS | Truncated half potential and both singular-kernel integrals. |
| 676–714 | PASS | Scalar/definite/hyperbolic pivot alternatives and their exact hypotheses; conditional critical-value dependence is retained. |
| 716–724 | PASS | Nine-direction truncated/full half-potential distinction: `H<=600`, full potential `<=601`. |
| 726–749 | PASS | Main theorem branch closure and `K,s` rescaling. |
| 751–782 | PASS | Threshold accounting and limitations accurately describe what the proof does and does not imply. |
| 783–789 | PASS | Bibliographic metadata/attribution only; no external theorem is a proof dependency for the specialized estimates used. |
| 790 | PASS | Document terminator. |

No manuscript line remains mathematically UNCHECKED in this review. The only UNCHECKED package assertion is the uncommitted binary-PDF build/render claim.

## Definition, equation, and invocation ledger

The following groups were each re-derived or checked against the hypotheses at the point of use.

### Fourier / measure-theoretic inputs — PASS

`eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `eq:envelope`, `eq:riesz`, and `eq:riesz-power` have the stated normalization under `\widehat f(t)=\int e^{itx}f(x)dx`. The gamma calculation gives the coefficient `1/sqrt(2*pi)` in the Riesz inequality. All Tonelli uses are on nonnegative majorants or bounded modulus-one integrands before taking limits.

### Spectral inputs — PASS

`eq:rank-perturb` is a singular-value statement and is correctly applied later to the possibly nonsymmetric `A-E`. The Schur lemma loses at most the pivot dimension at each absolute-eigenvalue threshold. In the singular case, replacing `A` by `A+eps I` and using threshold `t-|eps|` closes the limit without assuming invertibility of `A`.

### Product projections / scalar Fourier — PASS

`eq:projection` is proved from the original product density via a deterministic orthogonal change in an integral. It does not assert that rotated random coordinates are independent. In `eq:scalar-fourier`, for `p>=2`, `m=floor(p/2)` gives `m>=p/4`; the `2m`-power is integrable by Plancherel and boundedness of the characteristic function, and Fourier inversion at zero is legitimate for the sum of independent signed original coordinates.

### Decoupling and copies — PASS

For

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`,

Cauchy–Schwarz is taken in the genuine original-coordinate law of `X_I`. Expanding with one independent whole copy `X'_J` gives `D=X_J-X'_J`. The coordinates `D_j` are independent because the pairs `(X_j,X'_j)` are independent across `j`; each difference density is `f_j*\tilde f_j<=1`.

Critically, the residual factor

`exp(it(G(X_J)-G(X'_J)))`

is neither declared to be a function of `D` nor independent of `D`. It is removed only after taking absolute values. Thus `eq:decouple2` preserves the dependence that would be destroyed by a false sum/difference independence shortcut. From `|phi|^2<=E P(D)` with `P>=0`, Jensen gives

`|phi|^4 <= (E P)^2 <= E P^2`,

which is exactly `eq:decouple4`.

**Counterexample stress test of the shortcut:** if `X,X'` are iid uniform on `[-1/2,1/2]`, then `(X-X',X+X')` has diamond support `|d|+|s|<=1`; hence the sum and difference are not independent. The manuscript never uses this false assertion. Status: **FALSE shortcut / PASS manuscript**.

### Regularized determinant / exponent transfer — PASS

The frame weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

sum in outer-product form to the identity. The graph Brascamp–Lieb factor scales are correct. The `d_i` powers cancel after applying the scalar Fourier-power estimate, while `prod c_j^{-c_j/2}<=e^{theta/2}`. With `alpha=(2*pi*e)^2`, the fourth-power bound has determinant exponent `-1/2`; taking the fourth root gives exactly

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`.

Retaining order `k` in the determinant expansion gives the tail exponent `k/4`. Therefore:

- `k=5`: `5/4>1`, direct `L^1_t` inversion works;
- `k=3`: `3/4`, and multiplying by the Riesz weight `|t|^{-1/2}` gives tail exponent `5/4>1`;
- `k=4`: exactly `1`, the direct majorant is endpoint `C/|t|` and does not provide an `L^1_t` estimate.

No square/fourth-root/exponent loss is missing.

### Pivot kernels and conditional independence — PASS

The scalar profile is a conditional density domination statement, not an independence assertion. The definite pair rotates only a deterministic two-dimensional integral. The hyperbolic proof translates original coordinates separately (which preserves their independence), then uses eigenvectors only to parametrize level sets. In all pivot branches, conditioning is on disjoint original coordinates. No conditional density cap is inferred from an unconditional projected density.

### Interpolation / volume / ranks — PASS

The ordered volume `V_r` and the sampling weights are consistent. The bordered determinant identity is correct after sorting, with squaring removing orientation signs. `P` may be nonsymmetric and is never used as a quadratic-form coefficient matrix. In the completion, `R-P` is supported only in rows `T` or columns `S` outside the already controlled blocks, so `rank R<=3r`, while `R[L,L]=P[L,L]` gives the sharper restricted rank `<=r`. `D` is zero on `S union T` exactly as required.

In Proposition `prop:volume`, when `V_{r+1}/V_r<kappa`, `epsilon=||E||_F<=(r+1)sqrt(kappa)<=1/16`. With `m=4k-3` and `r<=k-1`, `m-3r>=r+1`. Hence at least `r+1` large diagonal entries of `D` occur inside `L`. The row sum bound `23/28` is strictly below the diagonal lower bound `371/400`, contradicting `rank R[L,L]<=r`. The argument correctly uses singular values for the nonsymmetric perturbation.

### Main theorem dependency closure — PASS

No pivot + `s_17>=1` supplies order-five crossing volume and density `<2400`. A scalar pivot loses at most one large eigenvalue under Schur, leaving at least sixteen and hence the nine-direction full half-potential `<=601`; the scalar density is `<=6010`. A two-coordinate pivot loses at most two, leaving at least fifteen; the definite branch is bounded directly and the indefinite branch needs only one surviving direction for the logarithmic potential. The final scaling `Y=KX`, `A->A/s`, `Q=(s/K^2)\widetilde Q` gives exactly `10000 K^2/s`.

## Independent arithmetic / finite checks

I independently reran the logic of `verify.py` (fixed RNG seed and exact SymPy algebra) and reproduced:

- 534 exact interpolation seeds;
- 18 exact volume-sampling cases;
- 9 strict sampling cases;
- exact diagonal-dominance slack `297/2800`;
- 240 floating Schur-threshold diagnostics;
- 30 floating graph-weight diagnostics.

I independently recomputed the displayed coarse constants:

- `12 sqrt(80 e)=176.959336... <200`;
- `800e=2174.625463... <2400`;
- scalar-pivot truncated bound `10(20+12 log16)=532.710647... <560`;
- indefinite-pivot truncated bound `10(32+4log16)+4/e=432.375067... <444`;
- final indefinite-pair density bound `10(10+5log16)+1/e=238.997316... <251`;
- quarter-power coefficient `2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)=3.99525936... <16`.

These computations supplement but do not replace the symbolic proof.

## New B03 counterexample: endpoint/copy resources do not imply one-copy height

This is the main new finding of the run. It stress-tests the natural `17 -> 13` attempt at exactly the B03 interfaces.

Let `X,Y` be independent uniform variables on `[-1/2,1/2]`, and set

`Z=4XY`.

The inputs are genuine independent cap-one original-coordinate densities. The quadratic coefficient matrix is

`[[0,2],[2,0]]`,

so its eigenvalues are `+2,-2`. This witness therefore has **only two** large eigenvalues and is **not** a counterexample to the 17-, 13-, or 3-large-eigenvalue target.

A direct product change of variables gives, for `0<|z|<1`,

`p_Z(z)=(1/2) log(1/|z|)`,

and `p_Z(z)=0` for `|z|>=1`. Hence

`||p_Z||_infty = infinity`.

Nevertheless its characteristic function is exactly

`phi_Z(t)=Si(t)/t`,

with the continuous value `phi_Z(0)=1`; an elementary split at frequency one and one integration by parts give the safe endpoint envelope

`|phi_Z(t)| <= min(1,4/|t|)`.

So an order-four-style `O(1/|t|)` envelope is compatible with an unbounded density.

More strongly, the **full negative-half potential is uniformly finite**. Since

`||p_Z||_3^3 = 3/2`,

and

`sup_a || |.-a|^{-1/2} 1_{[-1,1]} ||_{3/2} <=4`,

Hölder gives

`sup_a E|Z-a|^{-1/2} <= 4(3/2)^(1/3) = 4.5788569702...`.

Thus adding a strong translation-uniform half-potential bound to the endpoint Fourier envelope still does not force one-copy `L^infty`.

The independent whole-output copy is no rescue either. Here

`||p_Z||_2^2=1`,

so for an independent copy `Z'`,

`||p_{Z-Z'}||_infty <= ||p_Z||_2^2 =1`

and by Plancherel

`int |phi_Z(t)|^2 dt = 2*pi`.

Yet `p_Z` remains unbounded. Therefore neither a bounded density for the copy difference nor an `L^2_t` characteristic-function estimate can be unsquared into a one-copy height bound without additional structure.

**Status:** PASS counterexample.  
**Impact:** the existing `s_13 -> V_4` structural conclusion cannot be completed merely by combining the order-four endpoint envelope with the manuscript's nine-direction half-potential machinery, or by squaring to a whole-copy difference and controlling that difference. A valid 17-to-13 replacement must supply a genuine endpoint gain/cancellation, a stronger structural receiver, or another one-copy density mechanism.  
**Next obligation:** prove such an endpoint mechanism under the actual `s_13` structural hypotheses, with all same-bank phases and original-coordinate product provenance retained.

## Secondary algebraic stress witness: the global `3r` loss cannot simply be edited to `2r`

For `r=1`, take

`A=[[-1,-1,-1],[-1,-1,0],[-1,0,-1]]`, `S={1}`, `T={2}` (one-based indices).

Then `B=A[S,T]=[-1]`, the interpolation is

`P=[[-1,-1,-1],[-1,-1,-1],[0,0,0]]`.

With `L={3}`, the completion has `D=diag(0,0,-1)`, `E=0`, and

`R=A-D-E=[[-1,-1,-1],[-1,-1,0],[-1,0,0]]`.

Hence `rank R=3=3r`, while `rank R[L,L]=0<=r`. So the global `3r` bound is sharp for the completion algebra itself. This matrix has large coordinate pivots, so it is not a no-pivot theorem counterexample; it only rules out a threshold reduction obtained by mechanically replacing the global rank bound by `2r` without a new argument.

## Package-file status

| file | status | note |
|---|---|---|
| `README.md` | PASS | Correctly states candidate scope and current support-file inventory. |
| `DELIVERY_STATUS.md` | PASS / UNCHECKED-PDF | Repository/source statements checked; binary PDF build/render is outside this GitHub run. |
| `SOURCE_MANIFEST.json` | PASS / UNCHECKED-PDF | Source blob/size/line metadata consistent; PDF fields not independently inspected. |
| `manuscript.tex` | PASS | Entire 790-line source audited. |
| `AUDIT.md` | PASS-AS-HISTORICAL-SELF-REPORT | Its old finite-test counts are retained historical claims, not reproduced by the new checker. |
| `proof_map.csv` | PASS | Statement/proof ranges agree with source. |
| `verify.py` | PASS-SCOPED | Logic inspected and independently rerun; finite checks are not proof. |
| `checks.json` | PASS | Matches the rerun counts above. |

## Final status and threshold decision

- 17-singular-value theorem at the pinned source: **PASS in this B03 audit**.
- Fatal mathematical defect found: **NO**.
- Every manuscript line audited: **YES**.
- Compiled PDF/render: **UNCHECKED by this run**.
- Complete unconditional threshold reduction below 17: **NO**.
- Reason no improvement artifact is created: the new result is an obstruction to an endpoint proof interface, not a replacement theorem with a lower multiplicity.
- Unrestricted three-eigenvalue QFORM: **OPEN**.

The clean next B03 obligation is now sharper: an `s_13` proof must exploit information beyond an order-four `1/t` envelope, beyond a uniform negative-half potential, and beyond boundedness of the whole-copy difference density. Any proposed endpoint transfer should be tested first against the exact `4XY` logarithmic-singularity witness above while preserving the stronger spectral structure actually available at `s_13`.
