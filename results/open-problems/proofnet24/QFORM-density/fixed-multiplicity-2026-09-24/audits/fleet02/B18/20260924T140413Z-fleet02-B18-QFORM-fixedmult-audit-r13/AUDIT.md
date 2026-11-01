# fleet02 / B18 fixed-multiplicity complete audit — r13

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Immutable source pin and scope

I reread the complete fixed-multiplicity package and the entire 790-line manuscript in this invocation. The mathematical source remains byte-identical to the owner-pinned baseline:

- canonical source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 declared by the package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- size: 47,883 bytes, 790 lines.

The support package read in full comprised `README.md`, `SOURCE_MANIFEST.json`, `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`; `DELIVERY_STATUS.md` was also read because the package README requires it on every invocation. This review is mathematical audit, not formal verification or public release. It does not claim the unrestricted three-eigenvalue QFORM conjecture.

## Verdict

**Literal pinned 17-eigenvalue manuscript: PASS mathematically in this review.** I find no FALSE mathematical statement and no unfilled proof gap in the 790-line source. In particular, the singular-ambient limit in `lem:schur` is already valid as written; the later fixed-`delta` rewrite found in some fleet reviews is an optional exposition, not a necessary repair. The exact argument is recorded below.

**Package reproducibility: GAP, nonfatal to mathematics.** The historical `AUDIT.md` reports an older self-audit suite with counts not reproduced by the current `verify.py`; the current checker explicitly says it is a new delivery-reproducibility suite and `checks.json` records different counts. This is disclosed in the current package and does not enter any proof premise. Repair obligation: never describe the current `verify.py/checks.json` as reproduction of the historical suite.

**UNCHECKED:** the compiled-PDF binary/hash and visual-PDF inspection, because the PDF binary is not present in the package; exhaustive novelty/priority across all literature; reproduction of the historical finite-test suite. Search misses are not novelty evidence.

## Complete source-line ledger

Every source line 1--790 is covered by the following disjoint ranges.

| Lines | Status | Audit result / hypothesis check | Impact / next obligation |
|---|---|---|---|
| 1--35 | PASS | TeX setup, theorem environments and notation are consistent with later use. `||p||_infty` is essential supremum; no hidden continuity claim is encoded. | None. |
| 36--83 | PASS | Abstract, theorem, corollary, normalization and architecture match: arbitrary independent real cap-`K` densities, arbitrary symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`; no moments/support/log-concavity/iid assumptions. `9=4*3-3`, `17=4*5-3` bookkeeping is correct. | None. |
| 84--120 | PASS | Fourier convention, Gaussian transform, Plancherel factor `2*pi`, inversion factor `1/(2*pi)`, Gaussian inversion and rough-law approximation are normalized correctly. | None. |
| 121--130 | PASS | Power-envelope integral is `2ap/(p-1)` for `p>1`, giving `ap/[pi(p-1)]`. | None. |
| 131--160 | PASS | Gamma/Tonelli computation gives the coefficient `1/sqrt(2*pi)` in the negative-half-moment formula. The `3/4` envelope contributes exactly `12 sqrt(u)`. | None. |
| 161--181 | PASS | Operator/Frobenius conventions and Eckart--Young singular-value perturbation/rank loss hold for nonsymmetric matrices as used later. | None. |
| 182--207 | PASS | Schur spectral-count lemma is correct, including singular ambient `A`; detailed reconciliation below. No direct absolute-spectrum interlacing of an arbitrary principal compression is asserted. | Some fleet reports call line 205 a repairable gap; this audit rejects that diagnosis. |
| 208--217 | PASS | Strict row diagonal dominance implies invertibility without symmetry. | None. |
| 218--255 | PASS | Geometric rank-one Brascamp--Lieb heat-flow proof: frame contraction, integration by parts, large-time normalization, Lebesgue-point limit and monotone truncation are valid. | None. |
| 256--282 | PASS | Product-projection density proof keeps product structure in original coordinates; the orthogonal map is only deterministic integration. Frame weights and entropy estimate give `e^(d/2)`, scalar cap `sqrt(e)/|a|`. | None. |
| 283--301 | PASS | Scalar Fourier powers: `m=floor(p/2)`, integrable even power, inversion at zero and the scalar projection cap give the displayed `2*pi*sqrt(2e)/sqrt(p)`. Difference density is cap one. | None. |
| 302--324 | PASS | Decoupling introduces independent copies only of original product coordinates; same-bank phases are discarded only after modulus. Difference coordinates remain independent and cap one. | None. |
| 325--373 | PASS | Regularized crossing determinant: graph frame is exact; `c_j,d_i` lie in `[0,1]`; BL Jacobians, scalar Fourier powers and entropy factor cancel with `alpha=(2*pi*e)^2`; fourth root gives `det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`. | None. |
| 374--400 | PASS | Cauchy--Binet expansion and `Z_k` identification are exact. Order-five gives `5e Z_5^(-1/10)` by `L^1` inversion; order-three is used only with the Riesz weight and gives the stated half-potential. | None. |
| 401--414 | PASS | Scalar-square profile and interval inverse-image estimate are measure-valid for rough densities. Conditional profile is domination, not independence. | None. |
| 415--434 | PASS | Definite physical pair needs only a joint density cap; deterministic orthogonal diagonalization is inside the integral. Jacobian gives `pi M/sqrt(|det B|)`. | None. |
| 435--482 | PASS | Hyperbolic pair parameterization and `1/(2 sqrt D)` Jacobian are correct. Tail control chooses an original physical coordinate, uses density cap plus mass one, and does not infer rotated independence. Constants lead to `D^-1/2(6+log_+(16 sqrt D/|z-v|))`. | None. |
| 483--525 | PASS | Quarter-power concentration: large diagonal is paid by scalar square; otherwise a random sign **coordinate** cut has cross norm at least `L/4`; determinant theorem + Gaussian smoothing gives coefficient `<16`. Layer cake gives `4+4 log 16`. | None. |
| 526--541 | PASS | Pivot/volume definitions and the no-pivot entry bound `|a_ij|<1/7` follow from failure of scalar and principal-pair pivots. | None. |
| 542--564 | PASS | Volume-sampled interpolation: bordered determinant identity is exact; singular seeds only weaken the counting to an inequality; `P=A[:,T]B^-1A[S,:]` has rank `<=r` and exactly interpolates rows `S` and columns `T`. | Do not symmetrize `P`; see counterexample below. |
| 565--580 | PASS | Completion has zero-seed diagonal `D`, zero-diagonal error `E`, `||E||_F` bound, global `rank R<=3r`, and sharper restricted `rank R[L,L]<=r`. Nonsymmetry is harmless. | Both rank budgets must remain distinct. |
| 581--619 | PASS | Spectral-to-volume contradiction is correct. A bad ratio yields `||E||<=1/16`; global rank loss forces `r+1` large diagonal entries outside the seed; `371/400 > 23/28` gives strict diagonal dominance in an `(r+1)` block, contradicting restricted rank `<=r`. | None. |
| 620--645 | PASS | Fair coordinate cut gives expectation exactly `4^-k V_k`; no-pivot `s_9` gives full half-potential `<200`, and no-pivot `s_17` gives density `800e<2400`. | None. |
| 646--674 | PASS | Both singular-integral lemmas are valid by direct splitting/layer cake. Near constant in `J` is `<8`; log kernel is maximized by centered interval overlap and equals 8. | None. |
| 675--714 | PASS | Pivot half-potential branches are hypothesis-matched: scalar pivot uses one surviving Schur direction only for the log potential; definite pair is directly bounded; indefinite pair averages the hyperbolic envelope and uses `sup D^-1/2 log_+ D=2/e`. | None. |
| 715--724 | PASS | With `s_9>=1`, pivot branch gives truncated `H<=600`; no-pivot gives a full half-potential `<200`; outside distance one the kernel is `<=1`, hence full half-potential `<=601`. | None. |
| 725--749 | PASS | Main branch split is exhaustive. Scalar pivot under `s_17` leaves at least 16 Schur directions, enough for the nine-direction half-potential proposition; pair pivot leaves at least 15; no-pivot uses order five. Scaling `Y=KX` gives exactly `Q=(s/K^2) Qtilde` and final `10^4 K^2/s`. | None. |
| 750--790 | PASS | Threshold accounting, limitations and continuity disclaimer accurately describe what was proved. Bibliography is antecedent attribution, not a hidden theorem dependency. | Lower thresholds require a complete replacement argument. |

## Schur-limit reconciliation: literal source is valid

The disputed singular paragraph regularizes `A` to `A_e=A+e I`, with Schur complement `S_e`, and applies the valid invertible case at threshold `t-|e|`. Let

`q=N_A(t)-k`.

If `q<=0` there is nothing to prove. Otherwise the displayed count in the manuscript is exactly

`N_{S_e}(t-|e|)>=q`,

which is equivalent to

`s_q(S_e)>=t-|e|`,

where `s_q` denotes the `q`-th singular value (the `q`-th ordered eigenvalue modulus because `S_e` is symmetric). Since `B+eI` stays invertible for small `e`, `S_e->S` in operator norm. Singular values are 1-Lipschitz in operator norm, hence

`s_q(S)=lim s_q(S_e)>=lim(t-|e|)=t`.

Therefore `N_S(t)>=q=N_A(t)-k`. The moving threshold approaches `t` from below while an ordered modulus is bounded **from below**; an eigenvalue landing exactly at `t` is counted because `N` uses `>=`. Thus continuity is enough exactly as the manuscript says. A fixed-`delta` proof is also valid, but is not a mathematical repair requirement.

A useful adversarial warning: direct absolute-spectrum interlacing for an ordinary principal compression is false. For `A=[[0,L],[L,0]]` with `L>=1`, `N_A(1)=2` but either one-coordinate principal compression is `[0]` and has count zero. The manuscript correctly avoids this shortcut by working with the inverse Schur block in the invertible case.

## Counterexample checks against tempting proof edits

### 1. Symmetrizing the sampled interpolant is false

Take

```
A=[[0,1,2,0],
   [1,0,0,3],
   [2,0,0,0],
   [0,3,0,0]],
S={1}, T={2} (1-based).
```

Then `B=A[S,T]=1` and

```
P=A[:,T] B^-1 A[S,:]
 =[[0,1,2,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,3,6,0]].
```

`rank(P)=1`, and `P` has the exact row-`S`/column-`T` interpolation required by the proof. But `(P+P^T)/2` has rank two and no longer matches either interpolation identity. Any repair that silently forces `P` symmetric destroys the proof currency.

### 2. Order four does not lower 17 by direct baseline inversion

If the existing structural argument is run with `k=4`, multiplicity `13=4*4-3` forces fourth crossing volume, but the baseline determinant theorem gives only a `|t|^-1` tail. Its absolute integral diverges logarithmically. This is a route obstruction, not a counterexample to a thirteen- or eight-eigenvalue theorem.

## Primary-source prior-art verification

The bibliography contains BCCT and Rudelson--Vershynin (RV), and the manuscript explicitly presents them as antecedents while proving the exact results it uses.

- **BCCT, arXiv:math/0505065.** Example 1.6 states the geometric Brascamp--Lieb constant is one for orthogonal projections satisfying `sum p_j B_j^*B_j=I`. The manuscript's rank-one form `sum c_i u_i u_i^T=I` is precisely this specialization. BCCT's abstract also explicitly identifies heat-equation monotonicity as a principal technique. The manuscript nevertheless proves its needed rank-one inequality directly, so no unverified BCCT constant/hypothesis is imported.
- **RV, arXiv:1402.4492.** Theorem 1.1 assumes independent real coordinates with densities bounded by `K` almost everywhere and bounds every `d`-dimensional orthogonal projection by `(CK)^d`; Theorem 1.2 gives the sharp `sqrt(2)K` scalar-linear-form density bound for normalized coefficients. No moments, support, iid, centering, symmetry, smoothness or log-concavity are required. The manuscript uses its own weaker but self-contained `e^(d/2)`/`sqrt(e)` projection bounds, so RV is again attribution rather than an unproved dependency.

No external theorem is silently needed for the 17-eigenvalue proof. I make no novelty/priority claim from search results.

## Support-package audit

- `README.md`: **PASS** as package scope/status metadata.
- `SOURCE_MANIFEST.json`: **PASS** for the observed immutable manuscript blob/size/line count and for clearly distinguishing current and historical check suites. PDF assertions remain **UNCHECKED** here.
- package `AUDIT.md`: **GAP (provenance presentation only)** because historical finite-test counts are not reproduced by the current checker; its mathematical summaries are evidence, not proof premises.
- `proof_map.csv`: **PASS**; statement/proof ranges agree with the source and were used only for navigation.
- `verify.py`: **PASS as a finite diagnostic, not proof**. It pins the correct SHA-256 and directly tests the sensitive nonsymmetric interpolation/rank identities. Its floating Schur tests are not needed for the universal Schur proof.
- `checks.json`: **PASS** as the recorded result schema for the current checker; it explicitly disclaims formal verification and historical-suite reproduction.

## Threshold audit and owner-facing conclusion

The pinned 17-eigenvalue source is mathematically sound in this review, but it is no longer the lowest complete theorem present in the repository. I independently reconstructed the existing threshold-nine replacement proof in a sibling immutable improvement artifact for this same run. That replacement keeps the full rough-law/arbitrary-affine scope and gives the safe bound

`||p_Q||_infinity <= 6010 K^2/s` under `s_9(A)>=s>0`.

Multiplicity eight is not closed. The currently sharp audited obstruction is the no-pivot order-two interpolation-saturation chamber: the order-three structural proof can fail only at its terminal `r=2` seed, while the completed product-Fourier compiler has no generic `L^1` density endpoint at total smoothing dimension two. The unrestricted three-eigenvalue QFORM problem remains open.
