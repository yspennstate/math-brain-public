# account02/B15 — complete fixed-multiplicity audit, auto11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T150156Z-account02-B15-fixedmult-auto11`  
Reviewer lens: Gaussian inversion, Riesz half-potential, rough-law regularity scope, counterexample stress tests.

## Source pin and package coverage

Pinned mathematical baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
`manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Size/length: 47,883 bytes / 790 lines.

Fresh package master was first observed at `0c9cc754b1771e4d06e1063bef99e62b71c62a7a`; the source manifest states `source_unchanged=true`. I read in full `README.md`, `SOURCE_MANIFEST.json`, `manuscript.tex` (all 790 lines at the pinned source commit), `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and the README-required `DELIVERY_STATUS.md`. I also fetched the pinned manuscript blob itself.

The support checker is correctly scoped as a finite reproducibility check, not a proof certificate. Its source-hash gate is correct; its exact tests cover interpolation/rank/support/bordered-minor identities and the `297/2800` dominance slack. `checks.json` reports 534 exact interpolation seeds, 18 volume comparisons, 9 strict-sampling cases, 240 floating Schur-threshold cases and 30 graph-weight cases. The different historical counts in the author self-audit are explicitly documented as belonging to a different suite, so this is not a contradiction.

## Overall verdict

**PASS for the stated seventeen-direction theorem, with one nonfatal notation GAP and no FALSE mathematical statement found.** The theorem proved by the source is exactly the fixed-multiplicity statement

` s_17(A) >= s > 0  =>  ||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`

for arbitrary dimension, signature, remaining spectrum, affine terms and independent rough coordinate densities bounded by `K`. This audit does not confer formal-verification or journal-review status. It does not solve unrestricted three-eigenvalue QFORM.

The local GAP is in the final indefinite-pair paragraph of the main proof: after defining the pair Schur complement through Lemma `lem:schur`, the manuscript says `||A/B||>=1`, but the notation `A/B` is nowhere defined. Replace it by `||S||>=1`, where `S=D-C^T B^{-1}C` is the already-defined Schur complement. The next invocation is exactly the quarter-power/log-potential lemma for the critical-value polynomial with quadratic matrix `S`, so the repair is local and has no numerical or logical downstream cost.

## Line-by-line/range audit ledger

The following ranges cover all 790 source lines. “PASS” means I independently checked the definitions, displayed identities, hypotheses and the proof mechanism in that range; comments identify the sensitive point checked. There are no hidden UNCHECKED mathematical proof ranges.

| Lines | Label/content | Status | Reasoning / repair / impact |
|---|---|---|---|
| 1–46 | preamble, abstract, definitions | PASS | Singular-value convention, essential-supremum meaning and abstract quantifiers match the theorem. |
| 47–61 | `thm:main`, `cor:33` statements | PASS | Quantifiers include arbitrary affine terms and rough product laws; scaling dimensions are correct. |
| 62–90 | architecture, parameters, Fourier convention | PASS | `eta=1/100`, `kappa=1/80^2`; pivot/no-pivot split exhaustive. No rotated independence is asserted. |
| 91–120 | `lem:fourier` | PASS | Plancherel normalization, Gaussian approximate identity, inversion and arbitrary-law Gaussian identity rebuilt below. |
| 121–130 | power envelope | PASS | Envelope integral is `2ap/(p-1)`; inversion contributes `1/(2pi)`. |
| 131–160 | `lem:riesz` | PASS | Gamma/Tonelli normalization and constant rebuilt below. Extended nonnegative values are legitimate. |
| 161–168 | norm and spectral-count conventions | PASS | Operator/Frobenius and `N_A(t)` conventions used consistently. |
| 169–181 | singular-value perturbation/rank | PASS | Eckart–Young approximation argument works without symmetry. |
| 182–207 | Schur spectral count | PASS | Invertible case follows by principal compression of `A^{-1}` separately on positive/negative sides; singular case via `A+eps I` and moving threshold is sound. |
| 208–217 | strict diagonal dominance | PASS | Standard maximal-coordinate proof works for nonsymmetric matrices. |
| 218–255 | geometric rank-one BL | PASS | Heat-flow sign, frame contraction, large-time normalization and small-time Fatou argument checked. |
| 256–282 | product projections | PASS | Deterministic orthogonal completion is only a change of variables; entropy estimate gives `e^(d/2)` without claiming projected independence. |
| 283–301 | scalar Fourier powers | PASS | For `p>=2`, `m=floor(p/2)>=p/4`; `|hat f|<=1`, Plancherel and scalar projection yield the displayed constant. |
| 302–309 | cross-form setup | PASS | Every quadratic polynomial across an original-coordinate cut has this form, affine terms included. |
| 310–324 | decoupling | PASS | Cauchy–Schwarz and a copy only of the `J` bank give the product; Jensen gives the fourth-power form. Difference coordinates remain independent and cap one. |
| 325–373 | regularized determinant | PASS | Frame weights `c_j,d_i`, trace identity, scalar Fourier exponents and cancellation at `alpha=(2pi e)^2` reproduce determinant exponent `-1/8`. |
| 374–400 | crossing volumes and volume envelopes | PASS | Cauchy–Binet coefficients and exponents checked; order five gives density, order three only a half-potential. |
| 401–422 | square profile and conditional profile | PASS | Two inverse branches and interval-preimage length correct. Conditional inequality is measure domination/Tonelli, not independence. |
| 423–434 | definite pair | PASS | Elliptic polar Jacobian is `1/(2 sqrt(det B))`; integration over angle gives `pi M/sqrt(det B)`. |
| 435–482 | hyperbolic pair | PASS | Hyperbolic Jacobian, both tails and logarithmic envelope checked. The negative tail may choose its own original coordinate with a large component of the `w` vector; “using `w` instead of `u`” is sufficient for this harmless relabeling. Exceptional critical level handled measure-theoretically. |
| 483–525 | quarter-power concentration/log potential | PASS | Diagonal and off-diagonal cases checked; sign randomization preserves a literal cross block; Gaussian small-ball coefficient is safely `<16`; layer cake is correct. |
| 526–544 | pivot/volume definition and no-pivot entry bound | PASS | Ordered disjoint-pair convention and `|a_ij|<1/7` estimate correct. |
| 545–564 | sampled interpolation | PASS | Bordered determinant identity, determinant-square sampling and “at most `(r+1)^2`” count correctly allow singular seeds with nonsingular extensions. |
| 565–580 | completion/restricted rank | PASS | `E` support, `D=0` on seed, global rank `<=3r`, and complement rank `<=r` all follow from exact interpolation; nonsymmetry is harmless. |
| 581–619 | spectral-to-volume proposition | PASS | Telescoping bad ratio, `r=0` norm contradiction, singular-value rank subtraction and complement diagonal-dominance contradiction checked. Exact slack is `371/400-23/28=297/2800>0`. |
| 620–630 | random cut | PASS | Each ordered disjoint `k,k` pair survives with probability `4^-k`; no independence after projection is introduced. |
| 631–645 | no-pivot consequences | PASS | `Z_k^-1/(2k)<=160`; constants `12 sqrt(80e)<200` and `800e<2400` checked. |
| 646–653 | truncated half-potential definition | PASS | Atom convention and truncation are explicit. |
| 654–674 | singular kernels | PASS | Near/far split for `J(d)` and overlap/layer-cake proof of log-kernel bound are valid. |
| 675–714 | pivot half-potential | PASS | Scalar, definite and indefinite alternatives are exhaustive; Schur hypotheses match each invocation; conditioning is on original coordinates. |
| 715–724 | nine-direction half-potential | PASS | Pivot branch uses only two directions; no-pivot branch uses the full order-three half-potential; tail outside unit distance costs at most one. |
| 725–749 | main proof | PASS + local GAP | All three pivot branches and no-pivot branch close. Undefined `A/B` must be replaced by the already-defined pair Schur complement `S`; no other change. |
| 750–777 | scaling, threshold accounting, dependency table | PASS | `Y=KX`, `Q=(s/K^2) Qtilde` gives the exact `K^2/s` scaling. Order-three is not misused for density. |
| 778–790 | limitations, regularity remark, acknowledgments/bibliography | PASS (mathematical scope) | Regularity remark correctly separates integrable-Fourier continuity from essential density bounds in pivot branches. Bibliography is attribution only and is not used as an unproved dependency. |

## B15 reconstruction: Gaussian inversion

With the manuscript convention

`hat f(t)=int exp(itx) f(x) dx`, `phi_Z(t)=E exp(itZ)`,

the elementary Gaussian transform gives

`exp(-v x^2) = [1/(2 sqrt(pi v))] int exp(-t^2/(4v)) exp(-itx) dt`.

Substitute `x=Z-a`, use Fubini against the integrable Gaussian, and then replace `t` by `-t` if desired. For every probability law of `Z`, with no density assumption,

`E exp[-v(Z-a)^2]
 = [1/(2 sqrt(pi v))] int exp[-t^2/(4v)] exp(-ita) phi_Z(t) dt.`

Thus the manuscript normalization and sign convention are correct. Separately, if `phi_Z in L^1`, the Gaussian-regularized densities converge uniformly to the inverse transform, which is continuous; that is a legitimate continuity conclusion because there is a common `L^1` Fourier majorant.

## B15 reconstruction: Riesz half-potential

The gamma identity is

`|z|^-1/2 = Gamma(1/4)^-1 int_0^infinity v^-3/4 exp(-v z^2) dv`.

Tonelli is available because this representation is nonnegative, even when the value is `+infinity`. Insert the Gaussian identity and take absolute values. The remaining inner integral is, under `w=t^2/(4v)`,

`int_0^infinity v^-5/4 exp[-t^2/(4v)] dv
 = sqrt(2) Gamma(1/4) |t|^-1/2`.

Hence exactly

`E|Z-a|^-1/2 <= (2pi)^-1/2 int |t|^-1/2 |phi_Z(t)| dt.`

For `|phi_Z(t)|<=min(1,(u/|t|)^(3/4))`, the weighted integral is

`2 int_0^u t^-1/2 dt + 2u^(3/4) int_u^infinity t^-5/4 dt = 4sqrt(u)+8sqrt(u)=12sqrt(u)`,

so the stated bound `12 sqrt(u/(2pi))` is correct.

## Regularity scope: height passes to rough laws; continuity does not

Let `f_i^(eps)=f_i*rho_eps` in the original coordinates. Then `0<=f_i^(eps)<=1`, mass and independence are preserved, and

`|| product_i f_i^(eps) - product_i f_i ||_1
 <= sum_i ||f_i^(eps)-f_i||_1 ->0`.

A deterministic quadratic pushforward contracts total variation. Therefore any interval inequality `mu_eps(I)<=C|I|` uniform in `eps` passes directly to `mu(I)<=C|I|`; this yields an essentially bounded density with the same `C`. It does **not** imply continuity.

A literal quadratic counterexample to that overclaim is: let `X` be uniform on `[1,2]` (density cap one) and `Q=X^2`. Then

`p_Q(z)=1_[1,4](z)/(2 sqrt z)`

(up to endpoint versions), so `||p_Q||_infinity=1/2` but no continuous representative exists because the one-sided values at `1` disagree. Smooth cap-preserving mollifications `f_eps=1_[1,2]*rho_eps` have smooth output densities and their quadratic pushforwards converge in total variation to this law. Thus smooth approximants + uniform essential height + total-variation convergence cannot be used to smuggle continuity into a rough pivot branch.

## Counterexample stress test at the critical Fourier/Riesz endpoint

Let `U,V` be independent `Unif[-1/2,1/2]`, both cap one, and set `R=2UV`. Direct change of variables gives

`p_R(t)=log(1/(2|t|)),   0<|t|<1/2`.

Hence `p_R` is unbounded, although

`E|R|^-1/2
 =2 int_0^(1/2) t^-1/2 log(1/(2t)) dt
 =4 sqrt 2 < infinity`,

and for every finite `r>=1`,

`||p_R||_r^r = Gamma(r+1)`.

Gaussian output regularization also cannot manufacture a uniform height. With the manuscript Gaussian `g_eps`,

`(p_R*g_eps)(0)
 = int log(1/(2|y|)) g_eps(y) dy
 = (1/2) log(1/eps)+O(1)`

as `eps downarrow0` (substitute `y=sqrt(eps)u` and use Gaussian domination). Thus a critical `1/|t|` Fourier envelope, finite Riesz half-potential, all finite `L^r` norms, and smooth Gaussian regularization can coexist with an unbounded limiting density. Any multiplicity-eight endpoint argument must spend additional shared-anchor/product structure to gain a genuinely integrable improvement or a direct linear small-ball inequality.

This is a counterexample to a **proof interface**, not to the fixed-multiplicity-eight theorem itself.

## Threshold status after this audit

The complete threshold-nine replacement already written in this same account02/B15 line of work was re-read from current master. Its grouped product-Fourier receiver yields a marginal-free `E_3` density receiver and an `E_2` half-potential receiver, after which the no-pivot and pivot cases close at `s_9(A)>=s`. A conservative fully closed constant is

`||p_Q||_infinity <= 6010 K^2/s`.

The later Fejer-kernel constant patch improves constants but does not lower multiplicity. Threshold eight is not closed: current source-backed work reaches the critical `|phi(t)|<=min(1,U/|t|)` / `epsilon log(1/epsilon)` endpoint in its remaining no-pivot collar, and the explicit `2UV` example above shows why Gaussian inversion or Riesz regularity alone cannot remove that logarithm.

Therefore the lowest complete replacement theorem I can certify in this run remains **multiplicity nine**. Multiplicity eight remains OPEN, and unrestricted three-eigenvalue QFORM remains OPEN.
