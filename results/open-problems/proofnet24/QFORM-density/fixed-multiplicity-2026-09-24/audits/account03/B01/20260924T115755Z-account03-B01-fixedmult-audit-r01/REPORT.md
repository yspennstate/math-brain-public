# account03/B01 independent audit — fixed multiplicity 17

Run: `20260924T115755Z-account03-B01-fixedmult-audit-r01`

Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Audited manuscript source:
- repository: `yspennstate/math-open-problems`
- branch: `master`
- pinned initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- stated SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- current master still exposes the same manuscript blob.

Candidate audited: for independent real coordinates with densities `0<=f_i<=K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, the law of `X^T A X+b^T X+c` has an essentially bounded density with `||p||_infty <= 10000 K^2/s`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent B01 audit, with one local wording GAP and one repository-package GAP.** I found no fatal mathematical defect in the 790-line proof. This is an independent scheduled-worker review, not formal verification and not a self-awarded independent-validation certificate. The full three-eigenvalue conjecture remains open.

The local wording issue is in the product-projection proof: after indices with `b_i=0` are dropped, the proof should use

`sum_{b_i>0}(1-b_i) <= d`,

not equality with `d`. The upper bound `exp(d/2)` remains valid, so no downstream theorem or constant changes.

The package gap is nonmathematical but release-relevant: the root listing inspected contains `README.md`, `AUDIT.md`, `manuscript.tex`, and `audits/`, while the README names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` as package members. Those four files were not present in the inspected root. This does not invalidate the self-contained manuscript proof, but the repository should not be described as containing those reproducibility files until they are restored or the README is corrected.

## End-to-end ledger

### Lines 1–79 — theorem quantifiers, architecture, normalization target: PASS

The statement preserves all required fixed-multiplicity hypotheses: arbitrary dimension, arbitrary independent rough coordinate laws with only a density cap, arbitrary signature and remaining spectrum, and arbitrary affine terms. The proof deliberately claims only an essentially bounded density globally. The relation between singular values and absolute eigenvalues is correct for real symmetric `A`.

The dependency architecture is logically consistent: no-pivot density uses order-five crossing volume; no-pivot half-potential uses order-three crossing volume; scalar pivots invoke the nine-direction half-potential after Schur complementation; pair pivots are handled directly.

### Lines 80–179 — Fourier normalization, inversion, Riesz half-potential, rank perturbation: PASS

With `fhat(t)=int exp(itx)f(x) dx`, Plancherel has the stated `2*pi` normalization, and Gaussian inversion has factor `1/(2 sqrt(pi v))`. Recomputing the gamma substitution gives

`int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4) |t|^(-1/2)`,

hence the manuscript's factor `(2*pi)^(-1/2)` in the negative-half-moment inequality is correct.

For the envelope `min(1,(u/|t|)^(3/4))`, the weighted integral is exactly `12 sqrt(u)`, so the order-three branch is being used at the correct weighted threshold rather than incorrectly as an `L^1` Fourier bound.

The singular-value approximation formula and rank perturbation statement are valid for nonsymmetric matrices, which is essential later.

### Lines 180–259 — Schur spectral count, strict diagonal dominance, heat-flow Brascamp–Lieb: PASS

For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Applying positive and negative eigenvalue interlacing to that principal compression gives

`N_S(t) >= N_A(t)-k`.

The singular case is correctly reached by `A+epsilon I`, with the pivot staying invertible for small enough epsilon along a suitable sequence and with threshold `t-|epsilon|`; ordered eigenvalue moduli then pass to the limit.

The heat-flow proof has the correct sign:

`partial_t F-Delta F = F( sum c_i v_i^2 - |sum c_i u_i v_i|^2 ) >=0`,

because the weighted frame defines a contraction. The large-time Gaussian limit and the monotone approximation to general nonnegative integrable inputs are compatible with the stated geometric Brascamp–Lieb inequality.

### Lines 260–339 — product projection, scalar Fourier powers, decoupling setup: PASS WITH LOCAL WORDING GAP

For `U^T U=I_d`, the orthogonal complement rows satisfy `b_i=1-|U^T e_i|^2`. The Brascamp–Lieb argument gives

`p(y) <= product_{b_i>0} b_i^(-b_i/2)`.

Using `-b log b <= 1-b` yields

`log p(y) <= 1/2 sum_{b_i>0}(1-b_i) <= d/2`.

The manuscript's equality to `d` after zero-`b_i` factors have been removed is a wording error; the required inequality is enough. **Status: GAP, local repair only; downstream result PASS.**

For scalar Fourier powers, `|fhat|^(2m)` is integrable because `|fhat|<=1` and `|fhat|^2` is integrable. It is the characteristic function of a sum of `m` independent differences. Normalizing the signed coefficient vector of length `sqrt(2m)` and applying the projection bound gives the stated `p^(-1/2)` estimate.

The decoupling identities use original-coordinate independence only. The fourth-power bound follows from Jensen applied to the nonnegative right side of the squared decoupling estimate.

### Lines 340–429 — regularized crossing determinant and crossing-volume consequences: PASS

Writing

`H=alpha I+a^2 M^T M`,
`c_j=alpha e_j^T H^(-1)e_j`,
`d_i=a^2 m_i^T H^(-1)m_i`,

produces a genuine rank-one frame after normalizing the corresponding vectors. The one-dimensional changes of variables give exactly the factors

`alpha^(c_j/2)c_j^(-c_j/2)` and `d_i^(-d_i/2)`.

The scalar Fourier estimate with exponent `2/d_i` gives `(2*pi*sqrt(e d_i))^(d_i)`, cancelling the `d_i` powers. The `c_j` entropy factor contributes at most `exp(theta/2)`, so with `alpha=(2*pi*e)^2` the nuisance scalar factor cancels exactly. Taking fourth roots yields

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Cauchy–Binet gives the `Z_k` coefficient identity. Retaining the order-`k` term yields exponent `k/4`. At `k=5`, the power-envelope lemma gives the stated `5e Z_5^(-1/10)` density bound; at `k=3`, the Riesz-weighted integral gives the stated half-potential bound. No false pointwise scalar Fresnel estimate is used.

### Lines 430–519 — scalar/definite/hyperbolic pivots and quarter-power concentration: PASS

The scalar square profile has the correct two-branch Jacobian. The conditional inequality for `p_Q` is a domination statement integrated by Tonelli and does not claim independence of the square term and Schur remainder.

The definite-pair bound is a deterministic two-dimensional change of variables; orthogonal diagonalization is applied only inside that deterministic integral, so no rotated-coordinate independence is assumed.

For the indefinite pair, the hyperbolic parameterization has Jacobian `1/(2 sqrt(D))`. On each tail, one original coordinate has exponential growth, and the cap-one/mass-one bathtub estimate controls the logarithmic tail. The two branches and the inequality `Lambda>=2/sqrt(D)` give the displayed logarithmic envelope with the correct determinant scaling.

For quarter-power concentration, if no diagonal coefficient carries half the operator norm, the random-sign cut produces a physical cross block of norm at least `L/4`. Retaining one singular factor in the determinant theorem gives the required `|t|^(-1/4)` envelope, and Gaussian smoothing yields the `rho^(1/4)` small-ball estimate. Layer cake then gives the uniform logarithmic potential bound.

### Lines 520–609 — disjoint volumes, sampled interpolation, completion ranks: PASS

With no `eta`-pivot, the entry estimate `|a_ij|<1/7` follows from

`a_ij^2 <= |a_ii a_jj| + |a_ii a_jj-a_ij^2| < eta^2+eta`.

For a sampled nonsingular disjoint seed `B=A_{S,T}`, the bordered determinant identity exactly controls the off-diagonal `L x L` residual. Every ordered disjoint `(r+1)` pair is counted at most `(r+1)^2` times; singular seeds contribute zero weight, so the manuscript correctly uses an inequality rather than equality.

For

`P=A_{.,T} B^(-1) A_{S,.}`,

`P` agrees with `A` on rows `S` and columns `T`. In the completion `A=D+R+E`, `D` is diagonal and zero on the seed, `E` is zero-diagonal and supported in `L x L`, and `R_{L,L}=P_{L,L}` has rank at most `r`. Globally, `R-P` can be supported only in rows `T` or columns `S`, yielding `rank R<=3r`. This distinction between the global and restricted rank is used correctly later.

### Lines 610–699 — spectral-to-volume forcing, random cut, kernel estimates, pivot half-potential: PASS

If `V_k<kappa^k`, telescoping or first vanishing gives a ratio `V_{r+1}/V_r<kappa`. For `1<=r<=4`, the completion error satisfies

`epsilon <= (r+1)/80 <=1/16`.

With `m=4k-3>=4r+1`, global rank `<=3r` forces at least `r+1` diagonal entries of `D` with modulus at least `1-epsilon`. They lie in the seed complement because `D` vanishes on the seed. On such an `(r+1)`-set,

`|R_ii| >=371/400`,
`sum_{j!=i}|R_ij| <4(1/7+1/16)=23/28`,

and the exact slack is

`371/400-23/28 = 297/2800 >0`.

Strict row diagonal dominance therefore contradicts `rank R_{L,L}<=r`. The `r=0` branch is separately excluded by the operator-norm bound from the small diagonal and small off-diagonal Frobenius norm.

The fair coordinate cut retains each ordered disjoint `k`-minor with probability `4^(-k)`. Combining this with `k=3,5` gives the stated no-pivot analytic bounds.

The two kernel inequalities are adequate at their stated constants. In the scalar-pivot branch of the truncated half-potential proposition, Schur complementation leaves one spectral direction, which is exactly what the quarter-power logarithmic bound needs. Definite and indefinite pairs are handled by conditional measure domination and Tonelli.

### Lines 700–790 — nine-direction half-potential, main theorem, scaling, threshold accounting: PASS

`prop:nine` correctly distinguishes the full half potential in the no-pivot branch from the truncated half potential in the pivot branch, adding only the trivial tail contribution `<=1` outside distance one.

In the normalized main theorem:
- no pivot + `s_17>=1` gives density `<2400`;
- scalar pivot removes one coordinate, leaving at least sixteen large Schur directions, hence enough for the nine-direction half-potential, and gives `6010`;
- definite pair gives `<40`;
- indefinite pair removes two directions and uses only one surviving direction for the logarithmic critical-value average, giving `<251`.

For general `K,s`, setting `Y=KX` makes every `Y_i` density at most one, and

`Q=(s/K^2) [Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c]`.

Thus the normalized `10^4` bound scales exactly to `10^4 K^2/s`. This checks the B01 theorem-quantifier/scaling lens directly.

The interval formulation is equivalent to the essential-density formulation by standard measure domination, as stated.

## Deterministic constant recomputation

Independent arithmetic in this run gave:

- diagonal-dominance slack: `297/2800 = 0.1060714285714286`;
- `L0=4+4 log 16 = 15.090354888959125`;
- scalar-pivot truncated-half bound before rounding: `532.7106466687737 <560`;
- indefinite-pair truncated-half bound before rounding: `432.375066654277 <444`;
- no-pivot nine-direction full half-potential constant: `176.9593361872953 <200`;
- no-pivot seventeen-direction density constant: `2174.625462767236 <2400`;
- final indefinite-pair density constant: `238.99731555316055 <251`.

These computations support, but do not replace, the symbolic proof.

## Threshold reduction attempt

The audited interpolation mechanism gives `4k-3` directions because the global correction rank can be `3r` while the contradiction needs `r+1` large diagonal coordinates in the seed complement, where only the restricted rank `r` is available. The manuscript's order-five analytic endpoint therefore yields seventeen.

Trying the same dependency chain at `k=4` would algebraically correspond to thirteen directions, but the determinant theorem gives only

`|phi(t)| <= min(1,u_4/|t|)`,
`u_4=pi e Z_4^(-1/8)`.

Its absolute Fourier integral diverges logarithmically. More quantitatively, for `T>=u_4`,

`int_{-T}^T |phi(t)| dt <= 2u_4[1+log(T/u_4)]`,

which is not uniform in `T`. Therefore the existing absolute-inversion dependency chain does **not** prove a 13-eigenvalue theorem. This is an endpoint obstruction of the current method, not a counterexample to multiplicity 13 or to the full three-eigenvalue conjecture.

I did not find a rigorous threshold reduction below seventeen in this run. The next exact obligation is an order-four endpoint theorem: prove a dimension-free `L^infty` small-ball/density estimate from a positive fourth crossing volume while retaining arbitrary quadratic same-bank phases and all rough product laws, or replace the `4k-3` structural step with a stronger one.

## Package/review state

- mathematical 17-eigenvalue baseline: **PASS in this audit**;
- fatal mathematical defect: **none found**;
- local manuscript wording repair: **GAP, nonfatal** in product-projection summation after zero weights are dropped;
- package reproducibility files named by README but absent from root: **GAP, release-relevant but nonmathematical**;
- portions mathematically left UNCHECKED: **none of manuscript.tex**; I read the full 790-line source end to end;
- external citation priority/novelty: **UNCHECKED in this B01 audit** and not needed for the internal mathematical dependency closure because the specialized inputs are proved in the manuscript;
- lower multiplicity: **not established**;
- full three-eigenvalue conjecture: **OPEN**;
- continuity: continuous in the no-pivot Fourier branch, not proved globally by the manuscript.

This report does not overwrite the pinned baseline and should not be used as a substitute for a second genuinely separate end-to-end review.
