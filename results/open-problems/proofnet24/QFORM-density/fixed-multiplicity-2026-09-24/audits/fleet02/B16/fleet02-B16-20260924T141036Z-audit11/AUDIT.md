# fleet02/B16 independent end-to-end audit — 2026-09-24 14Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `fleet02-B16-20260924T141036Z-audit11`.

## Source pin and review status

- Initial mathematical source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Package-recorded source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source size/length: 47,883 bytes / 790 lines.
- Fresh master snapshot used for the full package read: `6d9894b251cce5639e8e3cb6ca5033ca230c63d1`; final pre-write refresh: `9203b0ef7a0137f2996a2f4b9aff4556732c0cf9`.
- At the final refresh `manuscript.tex` still had blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, so the mathematical source itself was unchanged.

**Baseline mathematical verdict: PASS in this one independent B16 review.** I read all 790 lines and reconstructed the proof graph before consulting any peer threshold-lowering verdict. I found no fatal gap in the written theorem

` s_17(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity <= 10000 K^2/s`

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature/remaining spectrum and arbitrary affine `b,c`.

This is one worker review, not formal verification or a release certificate. It does **not** solve the unrestricted three-eigenvalue QFORM conjecture.

## Full package audit

| component | status | reasoning / impact / next obligation |
|---|---|---|
| `README.md` | PASS | Correctly identifies the 790-line self-contained source, the candidate 17-direction theorem, support files, and review limitations. |
| `SOURCE_MANIFEST.json` | PASS / limited | The source blob, recorded SHA-256, byte/line counts and support-file metadata are internally consistent with the package and checker. I did not independently rebuild the conversation-only PDF binary in this connector-only run; its build/render claims remain **UNCHECKED** here and have no theorem-proof dependency. |
| `AUDIT.md` | UNCHECKED as attestation | Read in full but treated only as the historical author self-audit, never as evidence for my mathematical PASS. Its historical finite-test counts are explicitly distinct from the new checker. |
| `proof_map.csv` | PASS | Every listed theorem/lemma statement and proof range agrees with the source ranges used below. |
| `verify.py` | PASS as finite diagnostics | Code pins the baseline SHA, checks the exact interpolation identities/ranks and the `297/2800` slack, and labels floating Schur/graph tests as diagnostics rather than proof. |
| `checks.json` | PASS | I independently reran the checker logic in a separate interpreter: 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict cases, 240 Schur threshold cases and 30 graph-weight cases, matching the supplied result. |

## Complete source ledger

The following contiguous ranges cover every source line. `PASS` means I checked the definitions/quantifiers/equations and every invoked hypothesis in that range, rather than inheriting the package self-audit.

### Lines 1–46 — preamble, abstract, global definitions: PASS

The abstract matches the theorem actually proved. Singular values, essential supremum and Lebesgue-density conventions are coherent. No continuity, moment, support, log-concavity, iid, sign or rotated-independence hypothesis is silently added.

### Lines 47–61 — Theorem 1.1 and Corollary 1.2: PASS

Quantifiers are unrestricted except for independent coordinate densities `<=K` and `s_17(A)>=s>0`. The 33-direction statement is a literal stronger-hypothesis corollary.

### Lines 62–90 — architecture, parameters and Fourier conventions: PASS

`eta=1/100`, `kappa=1/80^2`. Pivot alternatives are exhaustive. The announced counts `9=4*3-3`, `17=4*5-3` match the later structural proposition. The text explicitly preserves original-coordinate conditioning.

### Lines 91–120 — Fourier identities: PASS

For `hat f(t)=int exp(itx)f(x)dx`, Plancherel has factor `2*pi`, inversion `1/(2*pi)`, and the Gaussian transform is `exp(-eps t^2)`. The approximate-identity and weak-limit steps are valid for rough laws. The Gaussian inversion formula has the correct `1/(2 sqrt(pi v))` normalization.

### Lines 121–130 — power envelope: PASS

The envelope integral is exactly `2ap/(p-1)`, so Fourier inversion gives `ap/[pi(p-1)]`.

### Lines 131–160 — negative half moments: PASS

The gamma representation at exponent `1/4`, Tonelli uses and Gaussian Fourier substitution are valid with extended nonnegative values. The inner integral is `sqrt(2) Gamma(1/4)|t|^-1/2`, giving coefficient `1/sqrt(2*pi)`. For the `3/4` envelope the weighted Fourier integral is exactly `12 sqrt(u)`.

### Lines 161–181 — singular-value notation and rank perturbation: PASS

The approximation formula for singular values proves both inequalities without symmetry. This is later applied correctly to the nonsymmetric auxiliary `A-E` / `D+R`.

### Lines 182–207 — Schur spectral count: PASS

For invertible `A`, the complementary block of `A^-1` is `S^-1`. Positive and negative principal-compression counts give `(n-k)-N_S(t) <= n-N_A(t)`. The singular case is correctly obtained from `A+eps I`, with threshold `t-|eps|`, invertible pivot along a sequence, and continuity of ordered eigenvalue moduli. Boundary `>=t` is preserved in the limit.

### Lines 208–217 — strict diagonal dominance: PASS

The maximum-coordinate proof works for nonsymmetric matrices, exactly as needed later.

### Lines 218–255 — geometric rank-one Brascamp–Lieb: PASS

The heat-flow identity is

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`,

because the frame map is a contraction. Trace gives `sum c_i=d`; the large-time Gaussian limit has the correct mass normalization. Compact support supplies an integrable Gaussian majorant; the small-time Lebesgue-point/Fatou step is valid; monotone truncation handles general nonnegative integrable inputs.

### Lines 256–282 — product projections: PASS

Complement-row weights `b_i=1-|U^T e_i|^2` form the required frame. Factors with `b_i=0` are safely dropped because their densities are `<=1`. `f_i^(1/b_i)<=f_i` for `0<b_i<=1`; `-b log b<=1-b` gives `||p_(U^TX)||_infinity<=e^(d/2)`. Deterministic rotation is used only for a marginal integral, not for independence. Scalar scaling yields `sqrt(e)/|a|`.

### Lines 283–301 — integrated scalar Fourier powers: PASS

For `m=floor(p/2)>=p/4`, `|hat f|^p<=|hat f|^(2m)`, and `|hat f|^(2m)` is the characteristic function of a sum of `m` independent differences. Integrability follows from the `L^2` bound. Applying the scalar projection cap to the `2m` signed original coordinates gives exactly `2*pi*sqrt(2e)/sqrt(p)`.

### Lines 302–324 — cross-form setup and decoupling: PASS

Cauchy–Schwarz is taken in a literal source bank. Expanding only an independent copy of the other bank makes `D=X_J-X'_J` a product vector with cap-one coordinates. Pure phases are discarded only after modulus. Jensen correctly upgrades the square to the fourth-power inequality. No moments are used.

### Lines 325–373 — regularized crossing determinant: PASS

With `a=2t`, `alpha=(2*pi*e)^2`, the vectors weighted by `c_j,d_i` form an exact frame. In geometric BL, the coordinate changes produce the displayed `alpha^(c_j/2)c_j^(-c_j/2)` and `d_i^(-d_i/2)` terms. `||g_j||_(1/c_j)<=1`; the scalar Fourier-power lemma at `p=2/d_i` cancels the `d_i` powers. `prod c_j^(-c_j/2)<=exp(theta/2)` and the chosen `alpha` cancels the remaining theta factor. Taking fourth roots gives determinant exponent `-1/8` with denominator `pi^2 e^2`.

### Lines 374–400 — crossing volumes and Fourier envelopes: PASS

Cauchy–Binet yields `det(I+zM^TM)=sum z^k Z_k`. Retaining one term gives `u_k=pi e Z_k^(-1/(2k))`. `k=5` gives the density constant `5e Z_5^-1/10`; `k=3` is used only for the half-potential, not incorrectly for direct density inversion.

### Lines 401–422 — scalar square and conditional profile: PASS

The two monotone inverse branches give the claimed square-root profile and the interval-preimage length. Conditioning on the original scalar produces a Schur-complement remainder and a measure-domination formula; no independence between the square and the remainder is asserted.

### Lines 423–434 — definite pair: PASS

After deterministic completion/diagonalization, elliptic polar coordinates have Jacobian `1/(2 sqrt(|det B|))`. Integrating the joint density cap around the angle gives `pi M/sqrt(|det B|)` without post-rotation independence.

### Lines 435–482 — hyperbolic pair: PASS

The two branches have Jacobian `1/(2 sqrt D)`. Writing a branch as `u e^t+w e^-t` gives `|u|=|w|=sqrt(delta Lambda)/2`. On each tail an original physical coordinate is monotone and satisfies `|y'|>=|y|/3`; cap one plus mass one bounds the tail by `3 log 2`. The middle interval, two tails and `Lambda>=2/sqrt D` yield `D^-1/2(6+log_+(16 sqrt D/|z-v|))`. Exceptional critical levels are null and the nonnegative-test-function formulation is valid for rough densities.

### Lines 483–525 — quarter-power concentration: PASS

A large diagonal gives the stated conditional small-ball bound. Otherwise the random sign cut produces a literal original-coordinate crossing block of operator norm at least `L/4`. The determinant theorem gives the `|t|^-1/4` envelope. The Gaussian smoothing calculation at `v=1/8` has coefficient `2^(5/8) pi^-1/4 e^(3/8) Gamma(3/8)<16`. Layer cake gives `L_0=4+4 log16` and rules out atoms.

### Lines 526–544 — pivot/volume definitions and small-entry estimate: PASS

With no `eta`-pivot, `|a_ii|<eta` and `|a_ij|^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. Ordered disjoint minors and the empty-sum convention are unambiguous.

### Lines 545–564 — volume-sampled interpolation: PASS

The bordered determinant identity is exact for nonsingular seeds. Sorting signs disappear after squaring. Because singular seeds can have nonsingular extensions, each order-`r+1` term is counted **at most** `(r+1)^2` times; the manuscript correctly states an inequality, not equality. `P` has rank at most `r` and agrees on rows `S` and columns `T`.

### Lines 565–580 — diagonal plus nonsymmetric interpolation: PASS

`E` is exactly the off-diagonal residual on `LxL`; `D` is diagonal on `L` and vanishes on the seed. `R_LL=P_LL`, so restricted rank is at most `r`. `R-P` is supported in rows `T` or columns `S`, yielding the distinct global bound `rank R<=3r`. Symmetry is neither claimed nor needed for `R,E`.

### Lines 581–619 — no-pivot spectral-to-volume proposition: PASS

A bad final volume gives a bad consecutive ratio. The `r=0` case contradicts `||A||<1/100+1/80<1`. For `1<=r<=4`, `epsilon<=1/16`. Rank subtraction yields at least `r+1` large diagonal entries because `m=4k-3>=4r+1`; they lie in `L` since `D` vanishes on the seed. The exact strict-dominance slack is

`371/400 - 23/28 = 297/2800 > 0`.

Thus an `(r+1)x(r+1)` subblock of `R_LL` is invertible, contradicting `rank R_LL<=r`. This checks the most sensitive nonsymmetric rank interface.

### Lines 620–645 — random cut and no-pivot consequences: PASS

Each ordered disjoint `(S,T)` lands across a fair cut with probability `4^-k`. Therefore `Z_k^-1/(2k)<=160`. The resulting constants are `12 sqrt(80e)<200` for the full half-potential at order three and `800e<2400` for density at order five.

### Lines 646–674 — truncated potential and kernel integrals: PASS

The near part of `J(d)` is the stated scale-invariant integral `<8`; the far part is bounded by `3 log_+(1/|d|)`. The logarithmic-kernel overlap is maximized when the interval centers coincide, giving exactly `8` by Tonelli.

### Lines 675–714 — pivot half-potential: PASS

Scalar pivot: Schur leaves one large direction under `s_2`, quarter-power excludes atoms and controls the logarithm. The exact scalar bound is

`H(Q)<=10(20+12 log16)=200+120 log16`.

Definite pair gives `<160`. Indefinite pair plus `sup D^-1/2 log_+ D=2/e` gives `<444`. All are uniform in conditioning and affine terms.

### Lines 715–724 — nine-direction half-potential: PASS

Pivot uses the preceding proposition; no pivot uses the full order-three half-potential `<200`. Outside the truncation interval the kernel is at most one, so the full half-potential is at most `601` (and can be sharpened in the pivot subcase).

### Lines 725–749 — main 17-direction proof and scaling: PASS

No pivot gives `<2400`; scalar pivot leaves at least sixteen Schur directions and therefore at least nine, giving `6010`; definite pair gives `10pi`; indefinite pair leaves at least fifteen and its Schur part has norm at least one, giving `<251`. For general `K,s`, `Y=KX` has cap-one coordinate densities and `Q=(s/K^2) Qtilde`, so the density rescales by `K^2/s`. Interval domination is equivalent to an essential density bound by standard outer regularity.

### Lines 750–777 — threshold accounting and limitations: PASS

The text correctly distinguishes order-five `5/4>1` density inversion from order-three `3/4>1/2` Riesz use. It does not claim threshold optimality or the three-eigenvalue theorem. Continuity is asserted only in the Fourier branch.

### Lines 778–790 — acknowledgment/bibliography/end: PASS as presentation

The two cited papers are antecedents only; no external theorem from them is a hidden logical dependency because the specialized estimates used above are reproved in the manuscript.

## Counterexample / adversarial checks

### 1. Physical-pivot-only strategies are impossible even at 17 directions

For `m>=101`, let

`A_(17,m)=I_17 tensor (J_m/m)`.

Its nonzero spectrum consists of seventeen eigenvalues equal to one, hence `s_17=1`. Every physical diagonal is `1/m<1/100`. A principal `2x2` determinant is either zero (two coordinates in one rank-one block) or `1/m^2<1/100` (different blocks). Thus this is a strict no-pivot 17-direction family. It is not a theorem counterexample; it shows why the no-pivot Fourier/volume branch is structurally necessary.

### 2. Both interpolation rank bounds can be simultaneously sharp

For

```
A=
[-1 -1 -1 -1  0 -1]
[-1 -1  1 -1  1  0]
[-1  1  1  1 -1  1]
[-1 -1  1  0  0  1]
[ 0  1 -1  0  0 -1]
[-1  0  1  1 -1 -1]
```

with one-based seed `S={1,2}`, `T={3,4}`, exact rational reconstruction gives `det A[S,T]=2`, `rank P=2`, `rank R=6=3r`, and `rank R[L,L]=2=r`; moreover

`R[L,L]=[[-1/2,-1/2],[0,1]]`

is invertible. I independently recomputed these identities. This is a proof-interface sharpness witness, not a fixed-multiplicity counterexample because it is not asserted to satisfy the theorem's no-pivot/spectral hypotheses.

### 3. Generic order-two indefinite density cannot be the missing endpoint

For independent `U,V~Uniform[-1,1]`, each source density is `1/2<=1`, while `U^2` has density `1/(2 sqrt y)` on `(0,1)`. Hence the density of `U^2-V^2` at zero contains

`int_0^1 [1/(2 sqrt y)]^2 dy = infinity`.

Thus a generic rank-two/order-two indefinite receiver cannot by itself replace the order-three density endpoint. This is an obstruction to a proof interface, not a counterexample to an eight- or three-direction theorem.

## Baseline dependency graph checked in this run

`Fourier/Gaussian/Riesz -> geometric BL -> product projections -> scalar Fourier powers -> decoupling -> regularized determinant -> crossing-volume envelopes`;

`ordered disjoint minors -> sampled nonsymmetric interpolation -> global/restricted rank bounds -> strict diagonal dominance -> no-pivot V_3/V_5 -> fair physical cut`;

`square / definite / hyperbolic physical pivots + Schur spectral count + quarter-power logarithmic control -> pivot half-potential branches`;

`no-pivot order five + scalar/pair pivot branches + scaling -> Theorem 1.1`.

Every arrow above was checked directly from the manuscript. No peer verdict is an inherited dependency.

## Improvement status

After completing this baseline audit, I independently reconstructed and checked a complete grouped product-Fourier replacement that lowers the fixed multiplicity from 17 to 9 while preserving all original quantifiers. I record that proof separately under this run's `improvements/` path, with explicit constants and dependency map. I do **not** claim threshold eight, and I do **not** claim the unrestricted three-eigenvalue conjecture.
