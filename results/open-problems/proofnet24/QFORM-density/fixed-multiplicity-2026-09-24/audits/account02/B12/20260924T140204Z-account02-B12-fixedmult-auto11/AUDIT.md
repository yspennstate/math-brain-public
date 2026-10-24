SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T14:02:04.972115Z.
attacking: full fixed-multiplicity manuscript audit, with counterexample-first emphasis on scalar pivots, completing-square shifts, square-root/logarithmic kernels, and endpoint integrability for rough cap-one laws.

# account02/B12 auto11 — independent fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline source:
- repository: `yspennstate/math-open-problems`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- bytes/lines: `47883 / 790`

Package snapshot read in full for this audit: master descendant `d20042453af0454a953b6b204c1d68b6024be881`; the source blob above is unchanged there. Required package files read: `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`; `DELIVERY_STATUS.md` was also read because the package README makes it part of the invocation contract.

## Verdict

**PASS** for the mathematical statement actually made by the pinned 17-eigenvalue manuscript:

> independent real coordinate densities `<=K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; `s_17(A)>=s>0`; then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity <= 10000 K^2/s`.

I found no false lemma, missing hypothesis, hidden moment/support/log-concavity assumption, post-rotation independence step, or rough-law endpoint failure. This is an independent mathematical audit, not formal verification or journal peer review. The unrestricted three-eigenvalue QFORM conjecture is **not** proved by this manuscript.

The package's PDF-build/visual-inspection assertions and bibliographic-priority claims are **UNCHECKED in this run**; they are not proof dependencies. The finite checker result in `checks.json` is a package-provided execution receipt; I audited the checker logic but did not treat its finite samples as proof.

## Complete line/proof ledger

Every source line was read. The following contiguous ledger covers lines 1--790; displayed equations in each range were checked against the surrounding derivation.

| Source lines | Object | Status | Audit conclusion / next obligation |
|---|---|---|---|
| 1--46 | preamble, abstract, conventions | PASS | The abstract matches the theorem proved later. No extra continuity or unrestricted-three-eigenvalue claim is made. |
| 47--61 | Theorem 1.1 and 33-eigenvalue corollary | PASS | Quantifiers and scaling target are coherent; `s_17>=s` is the actual hypothesis. |
| 62--90 | architecture, parameters `eta=1/100`, `kappa=1/80^2` | PASS | The stated `9=4*3-3`, `17=4*5-3` accounting is exactly what Proposition 5.4 later proves. |
| 91--160 | Fourier inversion, power envelope, Riesz half-potential | PASS | Fourier normalization, Gaussian factor, gamma substitution, and constants checked. Tonelli is used on nonnegative kernels; rough laws are allowed. |
| 161--217 | singular values, Schur spectral count, diagonal dominance | PASS | The Schur count correctly treats absolute eigenvalue thresholds using the complementary block of `A^{-1}` and a singular-limit argument. Nonsymmetric singular-value perturbation is used only where valid. |
| 218--255 | geometric rank-one Brascamp--Lieb | PASS | Heat-flow sign is correct: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`. Large-time and small-time limits have valid domination/Fatou arguments. |
| 256--301 | product projections and scalar Fourier powers | PASS | `b_i=0` rows may be dropped; the remaining frame is exact. The `e^{d/2}` cap and scalar `2pi sqrt(2e)/sqrt p` bound follow. Integrability at `p=2m` is not circular because `|hat f|^{2m}<=|hat f|^2`. |
| 302--400 | decoupling, regularized determinant, crossing volumes | PASS | Powers 2 and 4, graph weights/Jacobian, `alpha=(2pi e)^2`, exponent `-1/8`, Cauchy--Binet expansion, order-5 density and order-3 half-potential constants all check. |
| 401--422 | scalar square profile and conditional profile | PASS | See detailed B12 reconstruction below. The random completing-square shift is conditional on original coordinates and introduces no independence claim. |
| 423--434 | definite physical pair | PASS | Deterministic orthogonal diagonalization occurs only inside a two-dimensional integral; the original pair law need only have joint density cap. |
| 435--482 | hyperbolic physical pair | PASS | Jacobian, exponential-tail changes of variable, middle interval, AM--GM reduction, and rough-density/test-function formulation checked. The logarithmic singularity is the correct endpoint. |
| 483--525 | quarter-power concentration and log potential | PASS | Both diagonal and off-diagonal branches checked. The Gaussian smoothing coefficient is finite; the manuscript's coarse constant 16 is safe. Layer cake gives exactly `4+4 log 16`. |
| 526--544 | pivot/volume definition and no-pivot entry bound | PASS | Principal determinant condition implies `|a_ij|^2<eta^2+eta<1/49`; ordered-disjoint convention is consistent. |
| 545--580 | sampled interpolation and completion | PASS | Bordered determinant identity, singular-seed inequality, support of `R-P`, `rank R<=3r`, `rank R[L,L]<=r`, zero diagonal of `E`, and `D=0` on seed all check for nonsymmetric auxiliaries. |
| 581--619 | no-pivot spectral-to-volume proposition | PASS | `m=4k-3`, rank spending, forced `r+1` diagonal entries in `L`, and strict diagonal-dominance contradiction are valid. Numerical slack is `371/400-23/28=297/2800>0`. |
| 620--645 | random cut and no-pivot analytic consequences | PASS | Each ordered disjoint `k,k` minor survives a fair directed cut with probability `4^{-k}`. Constants `12 sqrt(80e)<200` and `800e<2400` are safe. |
| 646--653 | truncated half-potential definition | PASS | Atom convention is appropriate and is later excluded exactly where needed. |
| 654--674 | singular kernels `J(d)` and logarithmic kernel | PASS | Endpoint integrability checked independently below. The uniform logarithmic-kernel constant 8 is in fact attained at center `a=0`. |
| 675--714 | pivot controls truncated half potentials | PASS | Scalar, definite-pair and indefinite-pair alternatives are exhaustive. Each lemma hypothesis is met; dependence of conditional critical values is handled by Tonelli/test-function domination. |
| 715--724 | nine-eigenvalue half-potential | PASS | Pivot branch uses `s_2>=1`; no-pivot branch uses the already-proved order-3 half-potential. Tail outside distance 1 costs at most one. |
| 725--749 | proof of 17-eigenvalue theorem | PASS | No-pivot, scalar, definite and indefinite pivot branches close with constants below `10^4`; Schur counts are 16 and 15 as stated. Scaling gives exactly `K^2/s`. |
| 750--781 | threshold accounting and limitations | PASS | Dependency table matches the proof. It explicitly denies a three-eigenvalue conclusion and global continuity. |
| 782--790 | acknowledgment and bibliography | UNCHECKED | Bibliographic/priority metadata was not independently source-verified here. No cited theorem is used as an unproved mathematical dependency: the needed BL/projection statements are reproved in the manuscript. |

### Label-by-label hypothesis check

`lem:fourier` PASS; `lem:envelope` PASS; `lem:riesz` PASS; `lem:rank` PASS; `lem:schur` PASS; `lem:dd` PASS; `thm:bl` PASS; `lem:projection` PASS; `lem:scalar-fourier` PASS; `lem:decoupling` PASS; `thm:determinant` PASS; `cor:vol-fourier` PASS; `lem:square` PASS; `lem:definite` PASS; `lem:hyperbola` PASS; `lem:quarter` PASS; `def:pivot-volume` PASS; `lem:sampling` PASS; `lem:completion` PASS; `prop:volume` PASS; `lem:cut` PASS; `cor:no-pivot` PASS; `lem:kernels` PASS; `prop:pivot-H` PASS; `prop:nine` PASS; `thm:main` PASS; `cor:33` PASS.

No invocation above uses a stronger hypothesis than the caller supplies.

## B12 reconstruction: scalar pivot and completing-square shift

Write, in the original coordinate split `x=(x_i,y)`,

`A=[[a,c^T],[c,D]]`, `b=(beta,b_y)`.

Then

`Q=a x_i^2+2x_i c^T y+beta x_i+y^T D y+b_y^T y+c_0`

has the exact conditional completion

`Q=a(x_i-m(y))^2+R(y)`,

where

`m(y)=-(c^T y+beta/2)/a`

and the quadratic matrix of `R` is

`D-c c^T/a`,

the Schur complement of the physical scalar pivot. Conditional on `y`, the shifted variable has density `u -> f_i(u+m(y))<=1`; no independence between the square and `R` is asserted or needed. The square profile therefore gives, as a domination of output measures,

`p_Q(z) <= |a|^{-1/2} E |z-R|^{-1/2`}

for almost every `z`. This validates manuscript lines 404--422 and every later scalar-pivot use.

For a two-coordinate invertible physical block `B`, the same calculation gives shift

`x_0(y)=-B^{-1}(Cy+u/2)`

and residual quadratic matrix `D-C^T B^{-1}C`. Conditional translations are coordinatewise deterministic, hence preserve product independence and density caps. Subsequent eigenvector rotations in the definite/hyperbolic proofs are changes of variables in deterministic integrals, not rotations of the random product law.

## B12 reconstruction: square-root and logarithmic endpoints

### Scalar square is genuinely singular

Let `X` be uniform on `[-1/2,1/2]`, an admissible cap-one law. For `T=X^2`,

`p_T(z)=z^{-1/2}` for `0<z<1/4`.

Thus a scalar pivot alone cannot give an `L^infinity` output bound. The manuscript correctly requires a half-potential of the residual.

### Opposite-sign pair has a genuine logarithmic divergence

Let `X,Y` be independent uniform variables on `[-1/2,1/2]` and put `Q=X^2-Y^2`. With `u=X-Y`, `v=X+Y`, the joint density of `(u,v)` is `1/2` on the diamond `|u|+|v|<=1`. For `0<z<1/4`, the product change of variables gives

`p_Q(z)=log(u_+(z)/u_-(z))`,

where

`u_+/-=(1 +/- sqrt(1-4z))/2`.

Hence `p_Q(z)~log(1/z)` as `z downarrow 0`. This is a source-valid counterexample to any attempted uniformly bounded indefinite-pair conditional density. It supports, rather than contradicts, manuscript `lem:hyperbola`: the logarithm is necessary.

### Kernel endpoint is exactly where the remainder is needed

`J(d)=int_{-1}^1 |x|^{-1/2}|x-d|^{-1/2} dx` is finite for every `d!=0` but `J(0)=infinity`. For small positive `d`, already the interval `[2d,1]` gives a logarithmic lower divergence. Thus an atom of the remainder at the scalar-pivot critical value would be fatal. The quarter-power lemma supplies exactly the missing fact: a nonzero residual quadratic matrix has no atoms and has a uniform logarithmic potential.

By contrast,

`sup_a int_{-1}^1 |x|^{-1/2} log_+(1/|x-a|) dx = 8`,

with equality at `a=0`. Hence the indefinite-pair logarithmic singularity is integrable against the scalar square-root kernel, uniformly over translations, even for rough laws. This validates the manuscript's use of truncated half potentials and shows the constant 8 in `eq:log-kernel` is sharp for that deterministic kernel inequality.

## Hyperbolic-tail check

For the hyperbolic parametrization, writing a branch as `u e^t+w e^{-t}` gives `|u|=|w|=sqrt(delta Lambda)/2`. Choosing an original coordinate with `|u_i|>=|u|/sqrt2` and `t>=(3/4)log2` guarantees one-sided monotonicity and

`|w_i'(t)| >= |w_i(t)|/3`.

After the cutoff makes `|w_i(t)|>=1`, the cap-one/mass-one constraint implies

`int f_i(y)/|y| dy <= log(1+1/m)<=log2`.

Both tails and the finite middle interval therefore give the claimed logarithmic envelope without support or moment assumptions. The exceptional critical level is harmless because the proof is a measure-domination statement against nonnegative tests.

## Package/support-file audit

- `README.md`: PASS for mathematical status and source pin; correctly says the 17 theorem is a candidate and the three-eigenvalue theorem is not solved.
- `SOURCE_MANIFEST.json`: PASS for internal source identity: commit/blob/SHA/bytes/lines agree with the source read here. PDF build/visual-inspection receipt is UNCHECKED independently.
- `AUDIT.md`: PASS as a clearly labelled historical self-audit, not independent validation. Its older finite-test counts are explicitly distinguished from the new checker.
- `proof_map.csv`: PASS; statement/proof ranges match the 790-line source and cover every labelled mathematical object.
- `verify.py`: PASS as a finite diagnostic program. It pins the correct source SHA; exact checks cover interpolation support/ranks/bordered identities and diagonal-dominance slack; numerical Schur/graph checks are explicitly nonproof diagnostics.
- `checks.json`: PASS as the recorded output of that finite suite (`534` exact interpolation seeds, `18` exact volume cases, `240` Schur threshold diagnostics, `30` graph-weight diagnostics). Execution itself was not rerun in this audit.

## Gaps / false claims / unchecked items

- **FALSE:** none found in the pinned mathematical argument.
- **GAP:** none found that affects the 17-eigenvalue theorem.
- **UNCHECKED:** independent PDF compilation/visual inspection; bibliographic priority/completeness. These do not enter the proof.

## Downstream obligation

The baseline is mathematically secure enough to use as a dependency. A lower multiplicity must be a replacement proof, not a relabeling of the same order-five endpoint. In this same run I independently reconstruct a complete nine-eigenvalue replacement, with explicit constants and a rigorous Gaussian-cutoff proof of the grouped product-Fourier step, in the sibling immutable improvement artifact. The current order-three interpolation route still has a genuine multiplicity-eight terminal `r=2` chamber; no eight-eigenvalue theorem is claimed here.

Execution context: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native Brain ingestion.
