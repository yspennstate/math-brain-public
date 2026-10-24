# account01/B08 r12 — complete fixed-multiplicity audit amendment

Run: `20260924T135201Z-account01-B08-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `account01/B08`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source pin and correction to my preceding B08 review

Fresh owner control was read before selecting work from `yspennstate/math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md`. I acknowledge the current owner order `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh `master` observed before publication: `afb8a72698c7367670a6cd19dd98a3135ee4835b`.  
Current `manuscript.tex` Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, unchanged from baseline.  
Manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Source size/length recorded by the manifest: 47,883 bytes, 790 lines.

I read all 790 lines again in this invocation, together with current `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`.

**Important amendment:** my preceding B08 r11 report classified the baseline manuscript as `PASS`. That was too strong. The exact current source has one genuine but repairable proof gap in the singular case of Lemma `lem:schur`. The correct canonical-source verdict is therefore

> **GAP (repairable), not FALSE.**

With the fixed-threshold repair in Section 2 inserted, I independently find the complete seventeen-eigenvalue theorem chain mathematically sound with unchanged hypotheses and constants. The unpatched blob itself should not be labelled independently validated.

The theorem under audit remains only the fixed-multiplicity statement

` s_17(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity <=10000 K^2/s `,

for arbitrary real symmetric `A`, arbitrary independent coordinate densities bounded by `K`, and arbitrary affine `b,c`. Nothing here proves the unrestricted three-eigenvalue conjecture.

## 1. Fatal issues first

No fatal defect was found.

### GAP-B08-1 — singular Schur spectral-count limiting paragraph

**Label/range:** Lemma `lem:schur`, source lines 183–207, specifically the final singular-`A` paragraph at lines 205–207.

The invertible part of the lemma is correct. The written singular argument replaces `A` by `A+epsilon I`, applies the invertible result at the *moving* threshold `t-|epsilon|`, and then invokes continuity of ordered eigenvalue moduli. Continuity by itself does not justify passage from counts at moving thresholds to the closed threshold `t`; an eigenvalue of the limiting Schur complement can approach `t` at a rate larger than `|epsilon|`.

This is a proof gap, not a counterexample to the lemma.

### Exact repair

Fix `delta in (0,t)`. Choose a sequence `epsilon_m ->0` such that `A+epsilon_m I` is invertible, the principal pivot `B+epsilon_m I` remains invertible, and `|epsilon_m|<delta`. Let `S_m` be its Schur complement. Then `S_m->S` and, because every eigenvalue of `A+epsilon_m I` differs from the corresponding eigenvalue of `A` by exactly `epsilon_m`,

`N_(A+epsilon_m I)(t-delta) >= N_A(t)`.

Apply the already proved invertible case at the **fixed** threshold `t-delta`:

`N_(S_m)(t-delta) >= N_A(t)-k`.

If `q=N_A(t)-k<=0` there is nothing to prove. Otherwise the `q`-th largest eigenvalue modulus of `S_m` is at least `t-delta`. Passing to the limit gives `s_q(S)>=t-delta`. Since `delta>0` is arbitrary, `s_q(S)>=t`, hence

`N_S(t)>=N_A(t)-k`.

This repairs every downstream use without changing a hypothesis, threshold, or constant.

A genuinely separate account01/B18 review independently found the same moving-threshold defect, and a later account03/B20 amendment independently checked the fixed-threshold repair. This corroboration does not alter the fact that the current canonical manuscript blob remains unpatched.

## 2. Complete line-by-line mathematical audit

Every source line 1–790 is covered below. `PASS*` means the step is valid after inserting the repaired Schur lemma above. No mathematical source range is silently omitted.

| Source range / label | Verdict | Reconstruction |
|---|---|---|
| 1–35 | **PASS** | Macros/metadata only; no hidden mathematical premise. |
| 36–83, abstract, `thm:main`, `cor:33`, architecture | **PASS** | Quantifiers match the owner target for the fixed-multiplicity candidate: arbitrary dimension/signature/remaining spectrum, arbitrary affine terms, rough non-iid product laws with density caps. Main theorem claims essential boundedness only. |
| 84–151, Fourier convention, Gaussian inversion, `lem:envelope`, `lem:riesz` | **PASS** | Plancherel/inversion constants are consistent with `hat f(t)=int e^{itx}f(x)dx`; Gaussian smoothing and half-Riesz normalization have the stated powers; the weighted envelope integral is finite with the displayed constants. |
| 152–182, nonsymmetric singular-value/rank inequalities | **PASS** | Approximation-number argument gives both rank-shift and perturbation inequalities without symmetry. |
| 183–204, `lem:schur` invertible case | **PASS** | `S^{-1}` is the complementary principal compression of `A^{-1}`; apply min-max separately to positive and negative tails of `A^{-1}` to obtain the absolute-value count. |
| 205–207, `lem:schur` singular case | **GAP, REPAIRED ABOVE** | Moving-threshold continuity is insufficient as written. Fixed-`delta` proof above is rigorous and preserves the result. |
| 208–220, `lem:dd` | **PASS** | Strict row diagonal dominance needs no symmetry; kernel-vector contradiction is valid. |
| 221–260, geometric Brascamp–Lieb heat flow | **PASS** | Frame contraction gives the monotonicity sign; Gaussian large-time normalization is correct; truncation/Fatou/monotone convergence close the rough-law endpoint. |
| 261–285, product-projection density | **PASS** | Orthogonal maps occur only in deterministic integration. Rows with zero coefficient can be discarded; equivalently retain them with `-b log b=0`, and `sum(1-b_i)=d` gives the displayed `e^{d/2}` cap. No rotated-coordinate independence is asserted. |
| 286–319, scalar Fourier powers | **PASS** | Independent differences have density cap one; projection density and inversion at zero yield the stated even-power estimate; `floor(p/2)>=p/4` is used in the correct direction. |
| 320–373, decoupling | **PASS** | Both Cauchy–Schwarz/two-copy identities use original independent banks. Pure same-bank phases cancel or disappear after modulus; Jensen gives the fourth-power form. |
| 374–420, regularized determinant theorem and Cauchy–Binet | **PASS** | Frame weights/Jacobian and scalar Fourier exponents cancel as claimed; fourth root gives determinant exponent `-1/8`. Cauchy–Binet identifies crossing volumes. Order five supplies integrable `|t|^{-5/4}`; order three is used with the half-Riesz weight, not incorrectly as an `L^1` density estimate. |
| 421–455, scalar square and definite pair | **PASS** | Conditional square profile is a measure-domination statement, not independence. The definite-pair two-dimensional integral has the correct Jacobian `1/(2 sqrt(det B))`. |
| 456–500, hyperbolic pair / beginning quarter-power | **PASS** | Original-coordinate branch parametrization, monotone-tail rearrangement and determinant scaling are valid for rough product densities. No forbidden rotated-product assumption occurs. |
| 501–527, completion of `lem:quarter` | **PASS** | Random signs produce a physical crossing of norm at least `L/4`; determinant theorem gives the quarter-power envelope; layer cake gives the logarithmic-potential constant. |
| 528–565, pivot-volume definitions, no-pivot entry bound, `lem:sampling` | **PASS** | Principal pivot alternatives imply the entry bound. The bordered determinant identity is exact; singular seeds correctly turn the aggregate extension count into an inequality. `P=A[:,T]B^{-1}A[S,:]` interpolates rows `S` and columns `T`. |
| 566–600, `lem:completion` — primary B08 lens | **PASS** | Independently reconstructed in Section 3 below. `E` has zero diagonal, `D` vanishes on the seed, `R[L,L]=P[L,L]` has rank `<=r`, while the support of `R-P` gives global rank `<=3r`. No symmetry of `P,R,E` is silently used. |
| 601–630, `prop:volume` | **PASS** | Bad ratio gives `||E||<=(r+1)/80<=1/16`; `m=4k-3>=4r+1`; global rank loss forces `r+1` large diagonal entries of `D`, seed vanishing puts them in `L`, and strict diagonal dominance contradicts restricted rank `<=r`. Exact slack remains positive. |
| 631–653, random cut / no-pivot analytic consequences | **PASS** | Each ordered disjoint `k`-minor survives a fair physical cut with probability `4^{-k}`. Order three yields the full half-potential bound; order five yields the density bound. |
| 654–714, singular kernels and `prop:pivot-H` | **PASS*** | Kernel estimates, log-potential convolution, scalar/definite/indefinite physical pivot branches all reconstruct. Invocations of the Schur spectral count use the repaired lemma. |
| 716–724, nine-direction half-potential proposition | **PASS*** | Pivot/no-pivot split is exhaustive; no-pivot order-three estimate is already a full half-potential; the pivot case needs only the repaired Schur count and two surviving directions. |
| 726–773, main normalized theorem and scaling | **PASS*** | No-pivot `<2400`; scalar pivot reduces to the nine-direction half-potential; definite pair is direct; indefinite pair retains ample Schur spectrum. `Y=KX`, `tilde Q=(K^2/s)Q` gives exactly the factor `K^2/s`. |
| 774–790, corollary, limitations, bibliography | **PASS mathematically / UNCHECKED priority** | The 33-direction corollary follows immediately and limitations are honest. A comprehensive novelty/priority search is outside this run and remains `UNCHECKED`; it is not a proof premise. |

## 3. B08 interpolation reconstruction

Order coordinates as `S,T,L`, with `|S|=|T|=r`, and write

```
A = [ C    B    G
      B^T  F    H
      G^T  H^T  J ],              B=A[S,T] invertible.
```

The manuscript interpolant is

`P=A[:,T] B^{-1} A[S,:]`.

Hence

`P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`, and `P[L,L]=H^T B^{-1}G`.

With `E[L,L]=off(A[L,L]-P[L,L])`, zero elsewhere, and `D` the diagonal part of `A-P-E`, one gets:

- `diag E=0`;
- `D=0` on `S union T`;
- `R=A-D-E` satisfies `R[L,L]=P[L,L]`, so `rank R[L,L]<=r`;
- `R-P` vanishes on rows `S`, columns `T`, and the entire `L x L` block. Every possible nonzero of `R-P` is therefore in rows `T` or columns `S`. Splitting those supports into two matrices gives `rank(R-P)<=2r`; since `rank P<=r`,

`rank R<=3r`.

There is a stronger exact normal form. The completion is

```
R = [ C    B    G
      B^T  F    H
      G^T  H^T  H^T B^{-1}G ].
```

After permuting columns to `T,S,L` and eliminating with the invertible `B`,

`rank R = r + rank K`,

where

```
K = [ B^T-FB^{-1}C       H-FB^{-1}G
      G^T-H^TB^{-1}C     0          ].
```

The top block row and left block column each contribute at most `r`, giving `rank K<=2r`. This recovers global `3r` and separately explains restricted `r`.

### Sharpness

Both bounds can be attained simultaneously even within the no-pivot entry regime. For any `r`, take the direct sum of `r` copies of

```
(1/200) [0 1 1
         1 0 1
         1 1 1]
```

and take the first coordinate of each block in `S`, the second in `T`, the third in `L`. Then `B=(1/200)I_r`, `C=F=0`, `G=H=(1/200)I_r`, `J=P[L,L]=(1/200)I_r`, and `D=E=0`. Therefore

`rank R=3r`, `rank R[L,L]=r`.

All scalar diagonals are below `eta=1/100`, and every principal two-by-two determinant is below `eta`. Thus a bookkeeping-only replacement `3r ->2r`, or a claim that symmetry of `A` forces a better completion rank, is false.

## 4. Supplementary package audit

Unlike my preceding B08 run, the current root now contains all four formerly missing artifacts:

- `SOURCE_MANIFEST.json` — **PASS consistency/read**;
- `proof_map.csv` — **PASS consistency/read**;
- `verify.py` — **PASS source/read**;
- `checks.json` — **PASS recorded output/read**.

`checks.json` records suite `delivery-reproducibility-2026-09-24-v1` as `PASS`, with source SHA-256 matching the manifest, 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics. The file itself states that these finite diagnostics are not formal verification and do not replace the analytic proof. I read the checker and recorded output but did not independently execute the Python suite in this connector-only invocation; an independent rerun is therefore **UNCHECKED** here.

## 5. Baseline verdict

- Exact current `manuscript.tex` blob: **GAP (repairable), not FALSE**, solely because of `GAP-B08-1`.
- Mathematical theorem chain **with the fixed-threshold Schur repair inserted**: **PASS** in this complete B08 reconstruction.
- Global continuity: not claimed by the baseline theorem and not proved here.
- Full three-eigenvalue conjecture: **OPEN / not addressed by this validation result**.

The separate improvement report for this run audits the current nine-eigenvalue reduction, records the strongest rigorously supported threshold, and isolates the multiplicity-eight collar still unpaid.
