# account03/B18 r26 — rank-two cross-cut fractional compiler

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** `20260923T092851Z-account03-B18-QFORM-r26`  
**Assignment:** literature-to-proof transfer  
**Status:** `SUPPORTING_THEOREM_PROVED / PARTNER_RESULT_APPLIED`; full QFORM remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

Fresh source control at start: `yspennstate/math-research-brain@e9a503e4b86bf6c9891fb052cca7d944d16688b4`, OWNER CONTROL revision `2026-09-22.15`. This run consumes the live corrections forbidding post-rotation independence, arbitrary-joint coarea, positive conditional projection-density moments, conditional-density-as-independence, fixed-minor extraction, and pointwise law-uniform quadratic Fresnel decay.

## 1. Main new analytic lemma: cross-block half-Riesz bound at rank >= 2

Let the original independent coordinates be split into disjoint blocks `I,J`. Let

`R = F(X_I) + G(X_J) + 2 X_I^T B X_J`,

where `F,G` are arbitrary measurable real-valued same-side terms (in particular arbitrary quadratic-plus-affine terms), and `B` has rank `r>=2` with nonzero singular values `sigma_1,...,sigma_r`.

Then for every real `u`,

`E |R-u|^(-1/2) <= [4r/(r-1)] (prod_{l=1}^r sigma_l)^(-1/(2r)).`       (1)

For rank exactly two this is

`sup_u E|R-u|^(-1/2) <= 8 (sigma_1 sigma_2)^(-1/4).`                    (2)

No moment, symmetry, support, Gaussian, log-concavity, identical-law, or diagonal-basis hypothesis is used.

### Proof

Take a thin SVD `B=P Sigma Q^T`, with `P,Q` having orthonormal columns, and define

`U=P^T X_I`, `V=Q^T X_J`.

The primary theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, gives

`||p_U||_infinity <= 2^(r/2)`, `||p_V||_infinity <= 2^(r/2)`

for the present product densities `f_i<=1`. This theorem requires none of the forbidden extra hypotheses.

For a real frequency `t`, absorb all same-side curvature into conditional complex amplitudes

`a_t(u)=p_U(u) E[exp(it F(X_I)) | U=u]`,
`b_t(v)=p_V(v) E[exp(it G(X_J)) | V=v]`.

Then `|a_t|<=p_U`, `|b_t|<=p_V`, hence

`||a_t||_2, ||b_t||_2 <= 2^(r/4)`.

Because the two original-coordinate blocks are genuinely independent,

`phi_R(t)=int int a_t(u)b_t(v) exp(2it u^T Sigma v) du dv`.

With Fourier convention `hat b(xi)=int exp(i xi.v)b(v)dv`, Cauchy--Schwarz and Plancherel give

`|phi_R(t)|
 <= ||a_t||_2 [int |hat b_t(2t Sigma u)|^2 du]^(1/2)
 <= (2pi)^(r/2) |t|^(-r/2) (prod sigma_l)^(-1/2).`                 (3)

Indeed the scaling determinant is `(2|t|)^r prod sigma_l`, Plancherel contributes `(2pi)^r`, and the two L2 norms contribute `2^(r/2)`, leaving exactly `(2pi)^(r/2)`.

Thus

`|phi_R(t)| <= min(1, K |t|^(-r/2))`,
`K=(2pi)^(r/2)(prod sigma_l)^(-1/2).`                                (4)

Use the one-dimensional half-Riesz identity, justified by Abel regularization,

`|x|^(-1/2)=sqrt(2/pi) int_0^infinity t^(-1/2) cos(tx) dt`.

Taking absolute values after expectation and using (4), with the crossing time `T=K^(2/r)`,

`sup_u E|R-u|^(-1/2)
 <= sqrt(2/pi) [int_0^T t^(-1/2)dt + K int_T^infinity t^(-(r+1)/2)dt]
 = sqrt(2/pi) [2 + 2/(r-1)] K^(1/r)
 = [4r/(r-1)] (prod sigma_l)^(-1/(2r)).`

This proves (1). In particular rank two, which is exactly non-integrable for ordinary Fourier inversion (`|phi(t)| ~ 1/t`), becomes integrable after the half-Riesz weight `t^(-1/2)`. This is the missing endpoint that the prior rank>=3 density theorem could not use.

## 2. New Schur rank-two cross-cut density theorem

Let `A` be any real symmetric matrix and choose an original physical coordinate `i` with

`a=A_ii != 0`.

Write, after moving coordinate `i` first,

`A = [[a,b^T],[b,C]]`, `S=C-bb^T/a`.

Partition **all remaining original coordinates** into disjoint blocks `I,J`. Suppose the physical cross block `B=S_IJ` has rank exactly two with nonzero singular values `sigma_1,sigma_2`. Then for every independent cap-one input law,

`Q=X^T A X`

has an essentially bounded density and

`||p_Q||_infinity <= 8 |a|^(-1/2) (sigma_1 sigma_2)^(-1/4).`          (5)

The diagonal blocks `S_II,S_JJ` are completely arbitrary and may have any signs and ranks.

### Proof

Complete the physical square:

`Q = a (X_i + a^(-1)b^T Y)^2 + R(Y)`, `R(Y)=Y^T S Y`.

The scalar `X_i` is independent of `Y` and has density at most one. By (2), applied to the `I|J` cut of `R`,

`sup_s E|R-s|^(-1/2) <= 8 (sigma_1 sigma_2)^(-1/4).`                 (6)

For completeness, the deterministic scalar-shell estimate used here is the following. If `H=[t,t+h]`, `a>0`, and `r` is fixed, then

`Leb{x: a(x+g)^2+r in H} <= h |a|^(-1/2)|r-t|^(-1/2).`              (7)

For `r<t`, this follows from

`2/sqrt(a) [sqrt(t+h-r)-sqrt(t-r)] <= h/[sqrt(a)sqrt(t-r)]`.

For `t<r<t+h`, it is equivalent to `4(r-t)(t+h-r)<=h^2`; for `r>=t+h` the set is empty. For `a<0`, apply the same argument to `-Q` and use the upper endpoint `t+h`.

Conditioning on `Y`, using `f_i<=1`, and averaging (7) with (6) gives

`P{Q in [t,t+h]} <= 8 h |a|^(-1/2)(sigma_1 sigma_2)^(-1/4)`.

A probability measure satisfying this interval estimate is absolutely continuous with Radon--Nikodym derivative bounded by the displayed constant. This proves (5).

**Continuity:** not proved by this argument. The conclusion here is absolute continuity plus the stated essential-supremum bound.

## 3. Cross-cut hierarchy, including an actual account04/B18 application

The previous account03/B18 theorem `QFORM-CROSSBLOCK-RANKGE3-FRESNEL-v1`, source

`yspennstate/math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f`

proves that when a residual cross block has rank `r>=3`,

`||p_R||_infinity <= [2r/(r-2)] (prod sigma_l)^(-1/r)`.              (8)

Now apply the completed **account04/B18** Schur-pivot square-smoothing theorem at

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

which states that if a residual has density cap `M`, then after the physical completed square the full form has density cap `2 sqrt(M/|a|)`, without assuming independence after the completion. Combining it with (8) gives the actual inequality

`||p_Q||_infinity
 <= 2 sqrt(2r/(r-2)) |a|^(-1/2) (prod sigma_l)^(-1/(2r)), r>=3.`    (9)

Thus a nonzero physical pivot plus **any Schur cross cut of rank at least two** is analytically payable:

- rank `2`: new fractional route (5), constant `8`;
- rank `r>=3`: partner-dependent density route (9), with the better constant `2 sqrt(2r/(r-2))`.

Arbitrary same-side Schur curvature is allowed in every case. The remaining obstruction is therefore structural: the bare hypothesis `s_3(A)>=1` does not itself force a quantitatively good rank>=2 physical Schur cross cut.

## 4. Concrete closure of the live rank-at-most-two-cut obstruction family

Consider the exact target family used in the live correction inbox:

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`, `m>=1`.

Its nonzero spectrum is exactly `{1,1,-1}`. Earlier rank>=3 cross-cut methods cannot touch it because every physical cross cut has rank at most two.

For `m>=2`, pivot the singleton (`a=1`). Split each `m`-coordinate rank-one bank as evenly as possible: let `k=floor(m/2)` coordinates from each sign bank lie in `I`, and the rest in `J`. The Schur cross block is the direct sum of

`J_{k,m-k}/m` and `-J_{k,m-k}/m`.

Hence it has rank exactly two and both nonzero singular values are

`s_m = sqrt(k(m-k))/m`.

Therefore

`sigma_1 sigma_2 = k(m-k)/m^2 >= 2/9`, `m>=2`,

(the even case is `1/4`; for odd `m=2q+1`, the ratio is `q(q+1)/(2q+1)^2`, minimized at `q=1`). Applying (5),

`||p_{X^T A_m X}||_infinity
 <= 8 (9/2)^(1/4)
 = 11.651802520975762...`                                           (10)

for every admissible product input law and every `m>=2`. For `m=1`, the form is diagonal `diag(1,1,-1)` and the established diagonal theorem gives `<=pi`.

This is a source-valid rank-two-cross-cut closure of the standard family that refutes the proposed rank-three-cut dichotomy. It does **not** assert that every target matrix possesses such a cut.

## 5. Primary-source audit

### Applicable source

Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), applies exactly: the source measure is a product `prod f_i`, each `f_i` is a probability density bounded by one, and the theorem bounds every `r`-dimensional orthogonal marginal by `2^(r/2)`. This is the only external probabilistic input in the new half-Riesz proof.

### Recent theorem checked but not an exact target solution

Glazer--Hendel--Sodin, *Integrability of pushforward measures by analytic maps*, Algebraic Geometry 13 (2026), 154--192, DOI 10.14231/AG-2026-006 / arXiv:2202.12446, studies `L^{1+epsilon}` integrability of pushforwards of **smooth compactly supported measures** via analytic maps and singularity invariants. Its stated hypotheses and conclusion do not supply a distribution-uniform `L^infinity` bound for arbitrary fragmented product densities `f_i<=1`, so it is not an exact prior solution of QFORM and is not used as a premise here.

No exact published solution matching all QFORM quantifiers was located in this focused transfer.

## 6. Remaining debt

The full conjecture remains **OPEN / NOT PROVED**. The exact correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` shows that three large eigenvalues do not even qualitatively force one nonzero physical pivot whose Schur complement has a rank-two disjoint cross block. Therefore (5)/(9) are an analytic compiler once such a cut exists, not the missing global structural theorem.

The next non-duplicative step is to combine this newly paid rank-two endpoint with the current grouped/ridge/zero-pivot branches in an exhaustive product-preserving structural dichotomy, especially for the rank-one-star Schur families. No fixed-small-minor extraction, arbitrary-joint coarea, or conditional-cap-as-independence shortcut is permitted.

## 7. Constant ledger

- LPP cap in dimension `r`: `2^(r/2)`.
- Cross-block characteristic coefficient: `K=(2pi)^(r/2)(prod sigma)^(-1/2)`.
- Half-Riesz integral: `2r/(r-1) K^(1/r)` before multiplying by `sqrt(2/pi)`.
- Final half-Riesz constant: `4r/(r-1)`.
- Rank-two endpoint: `8 (sigma_1 sigma_2)^(-1/4)`.
- Obstruction-family product lower bound: `2/9`.
- Obstruction-family density bound: `8(9/2)^(1/4)=11.651802520975762...`.
