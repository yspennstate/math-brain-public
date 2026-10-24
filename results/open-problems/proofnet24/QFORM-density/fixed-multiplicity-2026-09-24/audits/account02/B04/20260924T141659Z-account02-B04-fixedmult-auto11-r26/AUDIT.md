SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T14:16:59.832995Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924; independent full-package audit with B04 emphasis on the geometric Brascamp--Lieb heat-flow proof, endpoint limits, rough-law approximation, and constants, followed by a counterexample stress test of the current multiplicity-eight endpoint.

# account02/B04 r26 — full fixed-multiplicity audit

## Source and control pin

Owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Fresh mathematical master at the beginning of the audit was `1021307c73d1f46686db7fbdfef6d30100236918`; a pre-write refresh advanced to `79faa620b387eca306bd8625dcbc5f0145a2b13b` through concurrent immutable worker additions. The baseline mathematical source is unchanged:

- initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 47,883 bytes, 790 lines.

I read `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, all 790 source lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. I also read the current multiplicity-nine replacement and multiplicity-eight terminal/collar reports needed to assess whether a lower threshold is closed. The support checker is diagnostic only, not a proof premise.

## Baseline verdict

**PASS.** I found no FALSE statement and no unresolved mathematical GAP in the written seventeen-eigenvalue theorem. I left no source range of `manuscript.tex` mathematically UNCHECKED. The theorem audited is exactly

`independent real coordinate densities <=K; A=A^T; arbitrary b,c; s_17(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infinity <=10000 K^2/s`.

The theorem asserts an essentially bounded density, not global continuity. It does not solve the unrestricted three-eigenvalue conjecture.

## Complete source-range ledger

| Source lines | Status | Reason / downstream impact |
|---|---|---|
| 1--46 | PASS | Preamble, notation, abstract and scope match the normalized/scaled theorem; no moment, support, sign, smoothness or rotated-independence hypothesis is hidden. |
| 47--61 | PASS | Main theorem and 33-corollary quantifiers are correct; interval domination and essential-density formulation agree. |
| 62--90 | PASS | Parameters `eta=1/100`, `kappa=80^-2`, pivot architecture and 9/17 counts agree with the later proof. |
| 91--121 | PASS | Fourier normalization, Gaussian approximate identity, Plancherel, inversion and Gaussian inversion are consistent. Weak convergence plus uniform Fourier convergence supplies the density without assuming one in advance. |
| 122--160 | PASS | Power-envelope and negative-half-moment/Riesz calculations have the correct exponents and constants; Tonelli is applied only to nonnegative integrands. |
| 161--220 | PASS | Singular-value perturbation/rank shift, Schur spectral count including singular ambient matrices, and strict diagonal dominance have the required directions and hypotheses. |
| 221--255 | PASS | Geometric rank-one Brascamp--Lieb heat flow, differentiation/integration by parts, large-time Gaussian limit, small-time Lebesgue-point/Fatou limit and monotone truncation all check; reconstruction below. |
| 256--301 | PASS | Product-projection density and integrated scalar Fourier powers preserve physical product provenance. Deterministic orthogonal coordinates are used only inside an integral. |
| 302--400 | PASS | Two/four-power decoupling, graph frame/Jacobian, regularizer `alpha=(2*pi*e)^2`, determinant exponent `-1/8`, Cauchy--Binet, order-five density and order-three half-potential endpoints are correct. |
| 401--525 | PASS | Scalar square profile, definite pair, hyperbolic pair, rough-law measure domination, quarter-power small ball and logarithmic potential are valid at the constants used. |
| 526--645 | PASS | Pivot/no-pivot definitions, ordered disjoint volumes, nonsymmetric sampled interpolation, bordered determinants, `rank R<=3r`, `rank R[L,L]<=r`, seed-vanishing diagonal, spectral-to-volume contradiction and fair-cut factor `4^-k` check. |
| 646--724 | PASS | Singular kernels, three pivot half-potential branches, truncated-versus-full distinction and the nine-direction full half-potential proposition are consistent. |
| 725--790 | PASS | Main 17-direction case split, Schur survivor counts, scaling `K^2/s`, threshold accounting, limitations and continuity disclaimer are correct. |

The historical finite-test counts in the author self-audit are **UNCHECKED as historical executions** in this run; the newly supplied checker explicitly does not reproduce that old suite. This has no theorem impact because no proof step depends on those counts.

## B04 lens — heat-flow proof rebuilt

For bounded compactly supported nonnegative `h_i` of positive mass, let

`f_i(t,s)=g_t*h_i(s)`, `v_i=partial_s log f_i`,

and

`F(t,x)=prod_i f_i(t,u_i.x)^(c_i)`.

The heat kernel satisfies `partial_t f_i=partial_s^2 f_i`. Direct differentiation gives

`(partial_t-Delta_x)F = F[sum_i c_i v_i^2-|sum_i c_i u_i v_i|^2]`.

If `W` is the matrix with columns `sqrt(c_i)u_i`, the geometric-frame identity is `WW^T=I_d`, so `||W||=1`. Applying `W` to `(sqrt(c_i)v_i)_i` proves the bracket is nonnegative. Hence the spatial integral of `F` is nondecreasing once differentiation under the integral and integration by parts are justified.

Those operations are justified on every compact time interval `[tau,T]` with `tau>0`: compact support of `h_i` gives Gaussian tails for `f_i` and all required derivatives, while `v_i` and the second logarithmic derivatives have at most polynomial growth in the one-dimensional argument. The frame identity converts the weighted product of the Gaussian tails into a genuine integrable Gaussian in `x`. Thus the differentiated integrand and the boundary flux have integrable Gaussian majorants; there is no hidden nonintegrable boundary term.

Taking traces in the frame identity gives `sum_i c_i=d`. With `x=sqrt(t)z`, for fixed `z`,

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4*pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`,

where `M_i=int h_i`. The product exponent is

`-(1/4) sum_i c_i (u_i.z)^2 = -|z|^2/4`.

For `t>=1`, compact support gives a uniform majorant `C exp(-|z|^2/8)`, so dominated convergence yields the exact large-time limit `prod_i M_i^(c_i)`.

At `t downarrow 0`, each one-dimensional heat convolution converges to `h_i` at its Lebesgue points. The inverse image of a one-dimensional null set under the nonzero linear functional `x -> u_i.x` is null by rotation and Fubini; finitely many such exceptional sets still have measure zero. Thus all factors converge simultaneously almost everywhere. Fatou gives

`int prod_i h_i(u_i.x)^(c_i) dx <= liminf_(t down 0) int F(t,x)dx`,

and monotonicity plus the large-time limit bounds this by `prod_i M_i^(c_i)`. No uniform-integrability assertion at `t=0` is needed. Zero-mass factors vanish almost everywhere. Finally `min(h_i,m) 1_[-m,m]` increases pointwise to a general nonnegative integrable `h_i`, so monotone convergence on both sides closes the theorem.

**B04 conclusion:** no endpoint exchange, boundary term, logarithmic-derivative singularity, or rough-input passage invalidates the geometric Brascamp--Lieb proof.

## Determinant and rough-law cross-check

In the determinant theorem the graph-frame weights satisfy `0<c_j<=1`, `0<=d_i<=1`, and `sum_i d_i=sum_j(1-c_j)=theta`. The scalar Fourier-power estimate at exponent `2/d_i` contributes `(2*pi*sqrt(e d_i))^(d_i)`; the `d_i` powers cancel their one-dimensional Jacobian factors. The entropy bound for the `c_j` contributes `e^(theta/2)`. With `alpha=(2*pi*e)^2`, the remaining scalar powers cancel exactly. Taking fourth roots gives

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

The order-five endpoint is integrable (`5/4>1`); the order-three endpoint is not used for direct inversion, only after multiplying by the Riesz weight `|t|^-1/2`. This distinction is correct.

## Current lower-threshold status checked in this invocation

The current complete nine-direction replacement is mathematically compatible with the baseline interfaces: the marginal-free `E_3` physical-crossing receiver pays the no-pivot `s_9` branch, while the marginal-free `E_2` half-potential receiver plus baseline pivots pays the scalar-pivot branch. Independent recent release-gate reconstruction records the complete bound `(2010+1200 log 16)K^2/s<5338 K^2/s`; I found no new defect in the interfaces used here.

Multiplicity eight remains **GAP / unproved**. The strongest current no-pivot reduction forces either disjoint `V_3` (already paid) or a quantitative overlap-one / two-sided order-two collar. A three-color extraction gives a literal physical `E_2` packet and a bounded full half-potential, but a generic `E_2` packet alone is not a density endpoint. The sibling improvement artifact from this run gives an explicit cap-one product-law counterexample showing why that last implication cannot be inserted.

## Package/checker status

`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py` and `checks.json` are present. The committed new checker reports PASS with 534 exact interpolation seeds, 18 volume comparisons, 9 strict cases, exact diagonal-dominance slack `297/2800`, 240 Schur diagnostics and 30 graph-weight diagnostics. These agree with the symbolic formulas tested, but remain finite diagnostics rather than mathematical verification.

## Next obligation

The correct next multiplicity-eight target is a dependence-safe receiver that consumes the **overlap-one / two-sided provenance itself**, or another physical third smoothing channel. It cannot first forget that provenance and retain only a positive order-two crossing volume: the improvement artifact supplies a no-pivot product-law counterexample with `E_2>0` and unbounded density.

The unrestricted three-eigenvalue conjecture remains OPEN.

Privacy/write review: only mathematical formulas, source pins, run labels and nonsecret repository paths appear here; no credentials, account secrets, machine paths, unrelated data or private personal material are included. No scheduler state, permissions, notifications, remote workflows or public-release state were changed.
