SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T22:05:14Z.
attacking: target-level regularity via physical-pair height certificates and leave-one-coordinate-out stability of the output density.

# account01/B15 automation 11 — definite-pair C0 closure and a four-coordinate rough-core lemma

**Status:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-REGULARITY-AND-STABILITY-LEMMA`. The full universal-height QFORM conjecture remains **OPEN**.

## 1. Source state and corrections


Completed assigned partner results actually used:

1. `account02/B15` r18, canonical mathematics `yspennstate/math-open-problems@159482a9594e177145fa61c337bf16e1f9fefc55`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T212015Z-account02-B15-qform-r18/REPORT.md`. If an ORIGINAL-coordinate `2x2` principal block `D` is positive or negative definite, then, after conditioning on every other physical coordinate, the resulting affine two-variable quadratic has density cap

   `pi/sqrt(|det D|)`.

   In particular the full quadratic form has this same cap, independently of all outside couplings. The proof is the exact ellipse-shell area estimate and is affine-term insensitive.

2. `account02/B15` r4, canonical mathematics `yspennstate/math-open-problems@28ddaf28bf6779837fb1212a025d8a8b9d329f8a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T160529Z-account02-B15-qform-r4/REPORT.md`. For every fixed real symmetric matrix of rank at least three and arbitrary cap-one product marginals, the quadratic output has an instance-dependent bounded density in `C_0(R)`. More locally, an invertible physical principal block `B` of order `d=3` or `4` gives a uniform-in-affine-term conditional cap

   `C_d/sigma_min(B)`,

   where `C_3=2*pi+3*sqrt(3)` and `C_4=4*pi+8`.

The latter report explicitly treats arbitrary affine terms in the conditioned local block. Therefore every statement below also holds for

`Q(x)=x^T A x+2 ell^T x+c`

with the same height certificates.

## 2. First new consequence: the definite-pair branch is automatically C0 under rank >= 3

The latest partner r18 proves the height bound from a definite physical pair, but its separate Proposition 3 imposed an additional uncoupled third physical coordinate in order to prove continuity directly. At the full target rank this extra decoupling hypothesis is unnecessary.

### Theorem 2.1 — definite-pair height plus unconditional target regularity

Let `X_1,...,X_n` be independent with densities bounded by one. Let `A` be symmetric with `rank(A)>=3`, let `ell` and `c` be arbitrary, and suppose that for some original-coordinate pair `I={i,j}` the principal block

`D=A_{I,I}`

is positive or negative definite. Then

`Q=X^T A X+2 ell^T X+c`

has a density `p_Q in C_0(R)` and

`max_t p_Q(t) <= pi/sqrt(|det D|).`                                      (2.1)

No condition such as `A_ik=A_jk=0` for a third coordinate is required.

**Proof.** The partner r18 ellipse-shell argument is unchanged by the deterministic affine vector `ell`: after conditioning on all coordinates outside `I`, it only changes the two affine coefficients. Hence the conditional and therefore unconditional output measure is dominated by

`M dx`,  `M=pi/sqrt(|det D|)`.

Separately, the partner r4 rank-three regularity theorem applies to the same affine quadratic: choose an invertible physical principal block of order three or four and condition on its complement. Its local theorem allows arbitrary affine terms and gives a common finite matrix-dependent conditional cap, so dominated convergence yields a canonical representative `p_Q in C_0(R)`.

The measure domination from r18 says `p_Q<=M` almost everywhere. Since this canonical representative is continuous, `p_Q(t0)>M` at one point would imply `p_Q>M` on an interval of positive Lebesgue measure, contradicting the a.e. bound. Hence (2.1) holds pointwise. A nonnegative `C_0` density attains its supremum, giving the displayed maximum. QED.

Thus, on every target instance possessing a physical definite pair with `|det D|>=delta`, both parts are now cleanly separated and simultaneously available:

`max p_Q <= pi/sqrt(delta)`  and  `p_Q in C_0`,

with continuity costing no extra quantitative constant.

## 3. Leave-one-out density certificates

For a coordinate `k`, write `A^{(k)}` for the principal matrix obtained by deleting row and column `k`. Define a finite certificate whenever one of the following is available inside `A^{(k)}`:

- a definite physical `2x2` principal block `D`, paying `pi/sqrt(|det D|)` by partner r18;
- an invertible physical principal block `B` of order `d=3` or `4`, paying `C_d/sigma_min(B)` by partner r4.

Precisely, with the infimum of an empty set interpreted as `+infinity`, put

`H_k(A) = min {`
`   inf_D  pi/sqrt(|det D|),`
`   inf_{d in {3,4}, B} C_d/sigma_min(B)`
`}`                                                            (3.1)

where `D` ranges over definite `2x2` principal blocks of `A^{(k)}` and `B` over invertible `dxd` principal blocks of `A^{(k)}`.

If `rank(A^{(k)})>=3`, the completed principal-pivot theorem used in partner r4 supplies an invertible principal block of order three or four. Hence

`rank(A^{(k)})>=3  =>  H_k(A)<infinity.`                         (3.2)

The point of `H_k` is that it controls the output after conditioning on the *deleted* coordinate.

### Lemma 3.1 — one-marginal L1-to-output-Linfinity stability

Fix all marginals except the `k`th one. Let `f_k,g_k` be two probability densities bounded by one, and assume `H_k(A)<infinity`. Let `p_f,p_g` denote the output densities obtained with `f_k` and `g_k`, respectively, for the same matrix and the same other marginals. Then

`||p_f-p_g||_infinity <= H_k(A) ||f_k-g_k||_1.`                  (3.3)

**Proof.** Condition on `X_k=x`. The remaining variables are still independent cap-one variables and the conditional polynomial is

`X_{-k}^T A^{(k)} X_{-k}`
` + 2(ell_{-k}+x A_{-k,k})^T X_{-k}`
` + (a_kk x^2+2 ell_k x+c).`

Every certificate in (3.1) is insensitive to these affine and constant terms. Therefore there is a measurable version `h_x(t)` of the conditional output density satisfying

`0<=h_x(t)<=H_k(A)`

for almost every `(x,t)`. Consequently

`p_f(t)-p_g(t)=int h_x(t)(f_k(x)-g_k(x)) dx`,

and taking absolute values gives (3.3). QED.

### Theorem 3.2 — multi-marginal stability

Let two cap-one product laws `f=(f_1,...,f_n)` and `g=(g_1,...,g_n)` differ only on a set `K` of coordinates for which `H_k(A)<infinity`. Then

`||p_f-p_g||_infinity`
` <= sum_{k in K} H_k(A) ||f_k-g_k||_1.`                         (3.4)

**Proof.** Replace the marginals one at a time. At every step all untouched and already replaced marginals remain cap-one product marginals, so Lemma 3.1 applies with the same matrix-only constant `H_k(A)`. Sum the one-coordinate estimates. QED.

This is stronger than total-variation convergence of output laws: it is direct uniform convergence of the density itself.

## 4. At most four coordinates can fail the leave-one-out rank-three certificate

The next structural fact is purely linear algebra and appears useful independently of any density estimate.

### Lemma 4.1 — four-coordinate exceptional-set bound

Let `A` be real symmetric of rank `r>=3`, and define

`E_0(A)={k : rank(A^{(k)})<=2}.`

Then

`|E_0(A)|<=4.`                                                   (4.1)

More precisely:

- if `r>=5`, then `E_0(A)=empty`;
- if `r=4`, then `|E_0(A)|<=4`;
- if `r=3`, then `|E_0(A)|<=3`.

**Proof.** Take a spectral-sign factorization

`A=U J U^T`,

where `U` is `n x r` with full column rank and `J` is an invertible `r x r` symmetric signature matrix. Write `u_i` for the rows of `U`. Since the rows span `R^r`, after deleting one row the span

`W_k=span{u_i:i!=k}`

has dimension either `r` or `r-1`.

If `dim W_k=r`, then `U_{-k}` still has full column rank. Since `J` is invertible,

`rank(U_{-k} J U_{-k}^T)=r`.

Thus `rank(A^{(k)})=r`.

If `dim W_k=r-1`, the rank of `A^{(k)}` is the rank of the nondegenerate bilinear form `J` restricted to the hyperplane `W_k`. Its radical is

`W_k cap W_k^{perp_J}`.

Because `J` is nondegenerate and `W_k` is a hyperplane, `dim W_k^{perp_J}=1`; hence the radical of the restriction has dimension at most one. Therefore

`rank(A^{(k)}) >= (r-1)-1 = r-2.`                               (4.2)

If this rank is at most two, then (4.2) forces `r<=4`, and necessarily deleting row `u_k` lowers the row-span dimension. Such a row is a coloop: `u_k` is not in the span of the other rows.

All coloop rows are linearly independent. Indeed, for each coloop `k` there exists a linear functional `L_k` annihilating every other row and satisfying `L_k(u_k)!=0`; applying `L_k` to a linear relation among coloop rows kills every coefficient except the kth. Hence there are at most `r` coloops. For `r=3,4` this gives the claimed bounds. QED.

Combining (3.2) with Lemma 4.1 yields the target-level conclusion

`#{k:H_k(A)=infinity} <= |E_0(A)| <=4.`                          (4.3)

The first set can be smaller, because even if `rank(A^{(k)})=2`, a definite rank-two physical block gives a finite partner-r18 certificate.

The number four is sharp for the *leave-one-out certificate*. Let

`H=[[0,1],[1,0]]`,  `A=diag(H,H)`.

Then `A` has eigenvalues `{1,-1,1,-1}`, so it is an exact owner-target matrix. Deleting any physical coordinate leaves rank exactly two, with the only nonsingular quadratic block indefinite. Thus all four coordinates lie in `E_0`, and none is recovered by the definite-pair clause in (3.1). Likewise the rank-three hollow triangle

`[[0,1,1],[1,0,1],[1,1,0]]`

has eigenvalues `{2,-1,-1}` and all three leave-one-out matrices are indefinite rank two.

These are not counterexamples to QFORM; they show only that this particular density-stability interface reaches a finite rough core of size at most four and can be sharp at that level.

## 5. Uniform-density smoothing outside a four-coordinate rough core

Let `A` be any fixed symmetric matrix of rank at least three, and let the input marginals be arbitrary cap-one probability densities. Choose

`E=E_0(A)`.

By Lemma 4.1, `|E|<=4`. For every `k notin E`, choose cap-preserving positive real-analytic Schwartz probability densities `f_{k,m}` with

`||f_{k,m}-f_k||_1 ->0`.

Such approximants were constructed in the preceding account01/B15 regularity-normal-form report; only ordinary truncation, cap-preserving mollification and a narrow Gaussian convolution are needed. Leave the at most four marginals in `E` unchanged.

For the resulting product law `f^(m)`, Theorem 3.2 gives, for this fixed matrix,

`||p_{f^(m)}-p_f||_infinity`
` <= sum_{k notin E} H_k(A)||f_{k,m}-f_k||_1 ->0.`               (5.1)

The sum is finite because the dimension is fixed and every `H_k(A)` in it is finite. By partner r4 both sides have canonical `C_0` representatives. Therefore

`max_t p_{f^(m)}(t) -> max_t p_f(t).`                            (5.2)

So every fixed target instance admits **uniform output-density approximation** in which all but at most four physical marginals are positive analytic Schwartz cap-one laws. This is stronger than weak or total-variation convergence of the pushforward: the entire density converges in `L^infinity`, and the actual attained peak converges.

If some exceptional deletion has a definite rank-two block, r18 makes its `H_k` finite and that coordinate can also be smoothed uniformly. Thus four is only a universal worst-case cap for the unsmoothed core.

A particularly clean sufficient condition is `rank(A)>=5`: then (4.2) gives `rank(A^{(k)})>=3` for every `k`, so **every marginal** may be perturbed in `L1` with quantitative `L1 -> L-infinity` output control (3.4). For positive- or negative-semidefinite rank-three matrices, the rank-two leave-one-out restrictions are semidefinite and contain definite `2x2` principal blocks whenever their rank is two, so the pair certificate often removes the nominal rank-three exceptions as well.

## 6. Logical regularity ledger

For the current target class the source-valid implications are now:

`three large eigenvalues`
` => rank(A)>=3`
` => instance-dependent bounded C_0 density`  (partner r4)
` => continuous density`
` => absolute continuity.`

The central owner theorem is strictly the missing uniform quantitative step

`sup_target max_t p_Q(t) < infinity.`                            (6.1)

On the definite-pair branch, partner r18 plus Theorem 2.1 pays this directly by `pi/sqrt(|det D|)`. On arbitrary fixed matrices, Theorems 3.2 and 4.1 show that rough marginal instability can be confined to at most four physical coordinates when one uses leave-one-out bounded-density certificates.

This does **not** solve (6.1): the constants `H_k(A)` may diverge with the matrix and dimension, and the at-most-four rough core can itself be an indefinite rank-two leave-one-out configuration. No claim is made that the three-large-eigenvalue condition forces a uniformly good local determinant or a uniformly bounded `H_k`.

The first unpaid implication from this run is therefore: combine the aggregate product-coordinate mechanisms from the geometry/cross-block workers with the finite rough-core decomposition above so that the matrix-dependent leave-one-out constants are never paid one at a time. In particular, any use of (5.1) in a universal proof must occur after a source-valid aggregate bank estimate, not as a substitute for it.

## 7. Result status

`FULL QFORM: OPEN -> OPEN.`

New proved supporting results:

1. For rank at least three, a physical definite `2x2` block gives a `C_0` density with the exact pointwise peak certificate `pi/sqrt(|det D|)` **without** the extra uncoupled-third-coordinate assumption in partner r18's direct continuity proposition.
2. A leave-one-out conditional height certificate gives the exact marginal perturbation inequality (3.3), and telescoping gives (3.4).
3. Every symmetric rank-`>=3` matrix has at most four physical coordinates whose leave-one-out principal matrix can have rank at most two.
4. Consequently, for every fixed target instance, all but at most four marginals can be smoothed to positive analytic Schwartz cap-one laws with **uniform convergence of the output densities and convergence of the attained maxima**.

Execution context remains `WITHOUT_VERIFIED_BRAIN`: GitHub retrieval and synchronization are repository transport, not verified native learned-memory receiver use. No scheduler, task, email, notification, permission, public-release, cross-account-authentication or paid/remote-call change is part of this result.
