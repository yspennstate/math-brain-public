SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T12:01:07Z.
attacking: protected-anchor localization—prove that an arbitrary linear Schur-slope bank may be fragmented/localized in every active coordinate except one whole anchor with exactly zero mass tax, then force the obstruction to symmetric active fragmentation onto the partner's strict rational skeleton while keeping the full target and arbitrary self curvature.

# account02/B14 r35 — early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **SUPPORTING TARGET-LEVEL LOCALIZATION THEOREM / FULL QFORM OPEN / CONTINUITY SEPARATE**

## 1. First unpaid implication attacked

The live debt inherited from r34 is `QFORM-SCHUR-LEAKAGE-OR-WHOLE-VOLUME-EXIT-v1`: before active-law fragmentation, expose a useful whole-bank Schur leakage or a whole-law volume/ridge/bank exit. The issue addressed here is the exact localization order once a scalar Schur slope

`S(V)=beta+sum_j c_j V_j`

has been exposed after completing an original-coordinate indefinite physical pair.

The preceding r34 theorem (`QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1`) gives, for bank submeasure mass `m` and unnormalised slope-density cap `L`,

`||p_Q^sub||_inf <= 8 sqrt(m L/kappa) + C_* m/sqrt(D)`,

where `D=|det C|`, `kappa=sigma_min(C)` for the completed physical pair and

`C_* = 2 + log 2 + sqrt(2 pi e) erfc(1/sqrt 2) = 4.004506265397...`.

Thus exact mixture transfer occurs whenever `L <= H m` with the same `H` on every localized piece.

## 2. New theorem: protected-anchor localization

### Theorem — `QFORM-PROTECTED-ANCHOR-SLOPE-LOCALIZATION-v1`

Let `V_1,...,V_d` be independent original-coordinate probability variables with densities `f_j<=1`. Let

`S(V)=beta+sum_{j=1}^d c_j V_j`

and fix an anchor coordinate `k` with `c_k != 0`.

For every `j != k`, allow an arbitrary finite or countable positive decomposition

`f_j = sum_{r in R_j} g_{j,r}`,

where `g_{j,r}>=0`; write `m_{j,r}=int g_{j,r}`. Do **not** fragment the anchor density `f_k`. For a multi-index `alpha=(r_j)_{j != k}`, let `nu_alpha` be the resulting product submeasure and

`m_alpha = prod_{j != k} m_{j,r_j}`.

Then the pushforward `(S)_# nu_alpha` has an unnormalised density satisfying

`boxed: || d(S_#nu_alpha)/ds ||_inf <= m_alpha/|c_k|.`          (2.1)

This remains true with any additional unfragmented probability-bank coordinates and arbitrary translations `beta`.

#### Proof

Condition on every bank coordinate except the anchor. For a fixed non-anchor configuration `v_{-k}`, the `S`-density contributed by `V_k` is

`(1/|c_k|) f_k((s-beta-sum_{j!=k} c_j v_j)/c_k) <= 1/|c_k|`.

Integrating against the non-anchor product submeasure of total mass `m_alpha` gives (2.1). No support radius, moment, fragment location, separation, or count appears. QED.

Now suppose that after exact completion of an original-coordinate invertible indefinite pair the active remainder is

`Y = h X^2 + X S(V) + R(V)`,

where `X` is another genuine independent cap-one coordinate, `h` is arbitrary, and `R(V)` is arbitrary and may be fully correlated with `S(V)`. Applying r34 to every `nu_alpha`, (2.1) gives

`||p_{Q,alpha}^sub||_inf`
` <= m_alpha [ 8/sqrt(kappa |c_k|) + C_*/sqrt(D) ].`             (2.2)

Since `sum_alpha m_alpha=1`, positive summation yields the **exact zero-tax localization rule**

`boxed:`
`||p_Q||_inf <= 8/sqrt(kappa |c_k|) + C_*/sqrt(D).`              (2.3)

Hence every slope-active coordinate except a single protected anchor can be spatially fragmented/localized arbitrarily, even countably and at arbitrarily remote locations, without changing the constant at all. For the common Schur slope `S=beta+2a^T V`, choosing anchor `k` gives

`||p_Q||_inf <= 4 sqrt(2)/sqrt(kappa |a_k|) + C_*/sqrt(D).`       (2.4)

This is not a good diffuse-bank bound when every `|a_k|` is tiny; the whole-bank projection cap must then be paid before coordinate selection. The theorem is instead a localization principle: once one anchor is retained whole, every other active bank coordinate may be localized freely.

## 3. Strict rational-skeleton obstruction to fragmenting the anchor too

The newest compatible designated partner account03/B14 r34 proves `QFORM-COUNTABLE-RATIONAL-SKELETON-LOCALIZATION-v1`: the exact optimal affine interval-concentration constant for the full target equals the optimum over a countable skeleton with rational finite-fragment indicator marginals, rational symmetric matrices of simple nonzero spectrum with three eigenvalues strictly outside `[-1,1]`, rational affine data and rational intervals. Thus any claimed localization ordering must survive such skeleton laws with arbitrarily many remote fragments.

The following family lies **already inside that strict skeleton**. Let

`E_N = union_{j=1}^N [4^j, 4^j+1/N]`.

Take `U_1,U_2,X` uniform on `[0,1]`, and `V_1,V_2` with density `1_{E_N}`. Define

`Q_N = 4 U_1 U_2 - 3 X^2 + 2X V_1 + 2X V_2 + V_1^2 + V_2^2`.    (3.1)

Its rational symmetric coefficient matrix is the direct sum of

`C=[[0,2],[2,0]]`

and

`B=[[-3,1,1],[1,1,0],[1,0,1]].`

The spectra are

`spec(C)={-2,2}`,
`spec(B)={1,-1-sqrt(6),-1+sqrt(6)}`.

Therefore the full matrix has simple nonzero spectrum and **four** eigenvalues with modulus strictly greater than one. It satisfies the exact QFORM target with room to spare.

Complete the outer pair `C`. Then `D=4`, `kappa=2`, and the remainder has

`h=-3`,
`S(V)=2(V_1+V_2)`,
`R(V)=V_1^2+V_2^2`.

Since `V_1+V_2` has density cap at most one by convolution, the slope `S` has density cap `H<=1/2`. The whole-law r34 compiler gives

`boxed: ||p_{Q_N}||_inf <= 4 + C_*/2 = 6.002253132698...`         (3.2)

uniformly in `N` and in the exponential fragment separation.

The new protected-anchor theorem reproduces **exactly the same constant** if, say, `V_1` is split into all `N` component intervals while `V_2` is kept whole: each one-sided piece has mass `m=1/N` and slope cap `L<=m/2`, so the subdensity bound is exactly `m(4+C_*/2)` and the pieces sum to (3.2).

By contrast, split **both** `V_1` and `V_2` into their `N` component intervals and apply the same random-slope compiler separately to all `N^2` cells. Each cell has

`m=N^{-2}`

and the unnormalised density of `2(V_1+V_2)` on that cell is a scaled triangular convolution with exact peak

`L=1/(2N)`.

Therefore the black-box cell certificate is

`8 sqrt(mL/kappa) + C_* m/sqrt(D)`
` = 4 N^{-3/2} + (C_*/2) N^{-2}.`

Summing over `N^2` cells gives

`boxed: 4 sqrt(N) + C_*/2,`                                      (3.3)

which diverges although the whole-law bound (3.2) is uniform.

This is `QFORM-STRICT-SKELETON-TWOSIDED-SLOPE-FRAGMENT-BARRIER-v1`. It is a proof-order obstruction only, not a QFORM counterexample and not a lower bound on the true density.

## 4. Required Claude result applied to a real inequality

The required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, proves Theorem A: a three-dimensional quadratic form whose three eigenvalues all have modulus at least `sigma`, with arbitrary linear terms, has density at most `6 sqrt(pi)/sigma`.

Condition on `U_1,U_2` in (3.1). The remaining three-variable block is exactly `B`, whose eigenvalues have moduli at least one. Claude Theorem A therefore gives the independent whole-law check

`boxed: ||p_{Q_N}||_inf <= 6 sqrt(pi) = 10.6347231054...`           (4.1)

for every `N`. Thus (3.3) is decisively an artifact of symmetric active fragmentation; the true skeleton family is uniformly bounded by a completed source theorem even without using r34.

## 5. Interpretation

The newest partner's countable rational-skeleton theorem and the new protected-anchor theorem fit together as follows:

- global TV/rational approximation may be used to reduce the **whole extremal problem** to rational finite-fragment laws at zero constant loss;
- within an analytic branch based on a random Schur slope, one may then fragment every non-anchor active coordinate at zero tax;
- one must not infer from skeleton reduction that all active factors may be normalized/paid cellwise before reciprocal smoothing. The strict-skeleton family (3.1) shows a `sqrt(N)` loss even with arbitrary nonzero hub self-curvature and a fixed target matrix.

The first remaining implication is therefore sharpened to `QFORM-PROTECTED-ANCHOR-OR-WHOLE-BANK-EXIT-v1`: after exposing a useful Schur slope, either retain one quantitatively heavy physical anchor and localize all other slope coordinates by (2.3), or pay the diffuse whole-bank projection/volume/Fresnel certificate before any active fragmentation.
