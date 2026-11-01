# fleet02/B15 — product-transversality continuity closure for every fixed rank>=3 matrix

**Worker:** fleet02/B15  
**Run:** `20260922T150242Z-fleet02-B15-qform-r3`  
**Assignment:** Absolute continuity and regularity  
**Status:** TARGET-LEVEL CONTINUOUS-REPRESENTATIVE THEOREM / FULL UNIVERSAL-CONSTANT QFORM OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The sole live problem is the following universal quantitative statement: for every dimension `n`, every independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove

`P(X^T A X in I) <= C |I|`

for one finite absolute constant `C`, independent of `n`, the laws and `A`, or give a valid counterexample.

The present B15 card is the regularity branch. The first unpaid regularity implication on entry was the one isolated by both the preceding fleet02/B15 run and the fresh assigned-partner result:

> prove an individually continuous output density in the fully coupled/no-separator product case, without assuming input continuity and without replacing the product law by a generic joint `L^infinity` density.

This report proves that implication at full target scope. It does **not** prove a matrix-independent height constant.

## 2. Source-pinned completed result actually applied

The fresh completed assigned-partner result is:

- repository `yspennstate/math-open-problems`
- commit `5b2073a19b463978d5e0b10df035842a8f3e22ff`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T142847Z-fleet03-B15-r11/REPORT.md`.

I use two exact conclusions from it.

1. If a random vector has any absolutely continuous joint law and `A!=0`, then `X^T A X` is absolutely continuous. Thus existence of an a.e. coarea density is not the hard part.
2. Generic bounded joint density plus rank-three curvature does **not** imply continuity: the normalized spherical shell density under `q(x)=|x|^2` gives a bounded output density with jumps. Therefore the proof below must use original-coordinate product structure in an essential way.

I also use two earlier fleet02/B15 theorems, with no strengthening of their quantitative scopes:

- `d5392d73398e2811f58b612fb8f191aa79d8ee5e`, same archive root, run `20260922T110507Z-fleet02-B15-qform-pivot-r1`: every invertible symmetric `3x3` physical block gives the affine conditional height
  `C_3/sigma_min(B)`, `C_3=2*pi+3*sqrt(3)`.
- `60e7f51716e67553ce759519f9801ff3674dcce9`, run `20260922T120155Z-fleet02-B15-qform-r1`: the analogous `4x4` height
  `C_4/sigma_min(B)`, `C_4=4*pi+8`, and every symmetric matrix of rank at least three has a nonsingular principal block of order `3` or `4`.

The preceding B15 run `b1d930ff0fbc625393aebcd4a59f9ba1ead465ed` showed that a common modulus of continuity is false even for fixed `A=I_3`; this report does not seek one.

## 3. New local theorem: nondegenerate product quadratics in dimension 3 or 4 are continuous

### Theorem 3.1 — product-transversality continuity

Let `d in {3,4}`. Let `Y_1,...,Y_d` be independent real variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `B` be an invertible real symmetric `dxd` matrix and let `b in R^d`, `c in R`. Then

`Z = Y^T B Y + 2 b^T Y + c`

has a bounded **continuous** density.

The already-proved quantitative bounds remain valid:

- for `d=3`, `||p_Z||_infinity <= (2*pi+3*sqrt(3))/sigma_min(B)`;
- for `d=4`, `||p_Z||_infinity <= (4*pi+8)/sigma_min(B)`.

No continuity, bounded support, moments, connectedness or smoothness of the `f_i` is assumed.

### Reduction to a centered quadratic

Translate by `x_0=-B^{-1}b`:

`x^T B x + 2b^T x + c
 = (x-x_0)^T B (x-x_0) + c - b^T B^{-1}b`.

Coordinate translation preserves independence and the bounds `f_i<=1`. It is therefore enough to prove continuity for

`q(x)=x^T B x`.

Write

`F(x)=prod_i f_i(x_i)`.

By the partner absolute-continuity theorem the pushforward has an a.e. density. Away from the sole critical point `0`, coarea gives the canonical representative

`p(t)=int_{q^{-1}(t)} F(x)/|2Bx| dH^{d-1}(x)`.

The proof below shows that this representative extends continuously through every `t`, including the critical value `0`.

## 4. Three uniform remainder estimates

Put `sigma=sigma_min(B)` and `Lambda=||B||`.

### Lemma 4.1 — critical neighborhood is uniformly small

For every `r>0`, let `p_near,r(t)` be the coarea contribution from `|x|<=r`. Then

- in dimension three,
  `sup_t p_near,r(t) <= 2*pi |det B|^(-1/2) Lambda^(1/2) r`;
- in dimension four,
  `sup_t p_near,r(t) <= 4*pi |det B|^(-1/2) Lambda r^2`.

In particular this contribution tends to zero uniformly in `t` as `r downarrow0`.

**Proof.**
Set `z=|B|^(1/2)x`; then `q(x)=z^T sign(B) z` and
`dx=|det B|^(-1/2) dz`. The image of `|x|<=r` lies in the Euclidean ball
`|z|<=Lambda^(1/2)r`. The previous local shell calculation for the canonical
quadratic gives slice height at most `2*pi*rho` in dimension three and
`4*pi*rho^2` in dimension four inside a ball of radius `rho`. Multiplying by
the Jacobian gives the displayed bounds. Since `F<=1`, inserting the product
density can only reduce the slice integral. QED.

### Lemma 4.2 — the far field is uniformly small

Let `p_far,R(t)` be the contribution from `|x|>=R`. Then for `d=3,4`,

`sup_t p_far,R(t) <= d^(3/2)/(sigma R)`.

Hence it tends to zero uniformly as `R to infinity`.

**Proof.**
On `|x|>=R`, `|Bx|>=sigma R`; hence some original coordinate satisfies
`|(Bx)_i|>=sigma R/sqrt(d)`. Partition the far region according to one such
index `i`. Conditional on all coordinates except `x_i`, the phase is a
one-variable quadratic and

`d q/d x_i = 2(Bx)_i`.

On the set where `|(Bx)_i|>=sigma R/sqrt(d)`, that derivative has magnitude at
least `2 sigma R/sqrt(d)`. Because it is affine in `x_i`, this set has at most
two monotone components. The inverse image of an output interval of length
`h` therefore has total `x_i`-length at most
`sqrt(d) h/(sigma R)`. The cap `f_i<=1` gives the same conditional probability
bound. Integrating the other product densities and summing `d` indices gives
`d^(3/2)h/(sigma R)`. Interval domination gives the asserted density bound.
QED.

### Lemma 4.3 — one-gradient-coordinate tubes are uniformly negligible

Fix `0<r<R<infinity`. Let

`g(x)=Bx`

and let `Bad_eta` be the subset of the annulus `r<=|x|<=R` on which the
second-largest number among `|g_1(x)|,...,|g_d(x)|` is at most `eta`.
Then there is a finite constant `C(B,r,R,d)` such that

`sup_t p_Bad_eta(t) <= C(B,r,R,d) eta^(d-2)`.

In particular this contribution tends uniformly to zero as `eta downarrow0`.

**Proof.**
If all but possibly the `i`th coordinate of `Bx` have magnitude at most
`eta`, then `x` lies in an `O_B(eta)` tube around the line

`L_i = B^{-1}(span(e_i))`.

Thus `Bad_eta` is contained in the union of `d` such tubes.

On the fixed annulus, `|Bx|>=sigma r`; hence `|grad q|=2|Bx|` is uniformly
bounded away from zero. Cover the annulus by finitely many coordinate patches
on each of which one derivative `|partial_k q|` is bounded below by a positive
constant. On such a patch, condition on the other `d-1` coordinates. Along
the `x_k` line the inverse image of an output interval of length `h` has
length `O(h)` on each of at most two monotone pieces.

The projection of an `O(eta)` tube around a bounded line segment onto any
`(d-1)`-dimensional coordinate hyperplane has volume
`O(eta^(d-2))`: it is an `O(eta)` neighborhood of either a bounded line
segment or a point. Since every `f_i<=1`, integrating the conditional
`O(h)` line bound over that projection costs
`O(eta^(d-2) h)`. Summing the finite patches and the `d` lines proves the
interval estimate and hence the density bound. QED.

The exponent `d-2` is exactly where the dimension threshold enters this
regularity mechanism; in dimension two the bad tubes do not become small.

## 5. Product structure on a two-coordinate transverse chart

The preceding three lemmas reduce continuity to compact pieces on which at
least two original-coordinate derivatives of `q` are bounded away from zero.

### Lemma 5.1 — two-coordinate product chart is continuous

Let `chi` be a compactly supported `C^1` cutoff contained in a region on which

`|partial_i q|>=a` and `|partial_j q|>=a`

for two distinct original coordinates `i!=j` and some `a>0`. Then

`p_chi(t)=int chi(x) F(x) delta(q(x)-t) dx`

is a continuous function of `t`.

**Proof.**
Subdivide the compact support into finitely many small coordinate boxes so
that on each piece the sign of `partial_i q` is fixed and the implicit root is
single-valued. Write the remaining coordinates other than `i,j` as `z`.

On one such piece, solve

`q(x_i,x_j,z)=t`

for

`x_i=psi_t(x_j,z)`.

The delta/coarea formula gives

`p_chi(t)
 = int f_i(psi_t(x_j,z)) f_j(x_j) F_z(z)
       a_t(x_j,z) dx_j dz`,

where `a_t` is a smooth compactly supported Jacobian/cutoff factor and
`F_z=prod_{k notin {i,j}} f_k(z_k)`.

Implicit differentiation gives

`partial_{x_j} psi_t = -(partial_j q)/(partial_i q)`.

On the compact patch, both numerator and denominator are separated from zero
and bounded, so `x_j -> u=psi_t(x_j,z)` is a `C^1` diffeomorphism with
uniformly bounded Jacobian and inverse Jacobian. After changing variables,

`p_chi(t)
 = int f_i(u) f_j(theta_t(u,z)) F_z(z)
       b_t(u,z) du dz`,

where `theta_t` is the inverse map and the families `theta_t,b_t` vary
continuously in `C^1` with `t` on a common compact set.

It remains to handle the rough factor `f_j`. Let `t_n->t`. Choose
`g in C_c(R)` with `||f_j-g||_1<epsilon`. Uniform Jacobian bounds imply,
after changing variables through `theta_t`,

`int |(f_j-g)(theta_t(u,z))| du <= C epsilon`

uniformly in `t,z`; the factors `f_i<=1`, `F_z` and `b_t` only contribute a
fixed finite constant, and `int F_z<=1`. For the continuous approximation
`g`, uniform convergence of `theta_{t_n}` and `b_{t_n}` gives convergence of
the integrals by ordinary dominated convergence. Letting `epsilon downarrow0`
proves

`p_chi(t_n)->p_chi(t)`.

Summing the finitely many subpieces proves the lemma. QED.

This is the only step that uses the original product structure. It fails for
a generic bounded joint amplitude, exactly as the assigned partner's spherical
shell counterexample shows.

## 6. Proof of Theorem 3.1

Fix `t_0` and `epsilon>0`.

1. Choose `r` so small that the critical-neighborhood density from Lemma 4.1
   is `<epsilon`.
2. Choose `R` so large that the far-field density from Lemma 4.2 is
   `<epsilon`.
3. On the compact annulus between those scales, choose `eta` so small that
   the bad-tube density from Lemma 4.3 is `<epsilon`.

Choose a smooth cutoff `psi`, `0<=psi<=1`, which equals one on a slightly
smaller compact annulus away from slightly enlarged bad tubes and vanishes in
the three remainder regions. The density of `(1-psi)F` is uniformly
`O(epsilon)` by the three lemmas.

On `supp psi`, at least two original-coordinate derivatives of `q` are
bounded away from zero. A finite smooth partition of unity writes

`psi=sum_m chi_m`

with every `chi_m` satisfying Lemma 5.1 for some pair of coordinates.
Therefore

`p_good(t)=sum_m p_{chi_m}(t)`

is continuous.

For `t` near `t_0`,

`|p(t)-p(t_0)|
 <= |p_good(t)-p_good(t_0)| + 2 sup_s p_remainder(s)`.

The first term tends to zero and the second is `O(epsilon)`. Since `epsilon`
is arbitrary, `p` is continuous at `t_0`. This includes `t_0=0`: the critical
point is already paid by Lemma 4.1.

Thus every nondegenerate `3`- or `4`-coordinate product quadratic has a
continuous density. The previously proved local interval estimates supply the
stated finite `L^infinity` bound. QED.

## 7. Full fixed-matrix continuity

### Theorem 7.1 — every rank-at-least-three product quadratic has a bounded continuous density

Let `X_1,...,X_n` be independent with densities bounded by one, and let `A`
be any real symmetric matrix with `rank(A)>=3`. Then `Q=X^T A X` has a bounded
continuous density.

More precisely, if `J` is any nonsingular principal block of order
`d in {3,4}` and `B=A_{J,J}`, then

`||p_Q||_infinity <= C_d/sigma_min(B)`

with the same `C_3,C_4` above, and `p_Q` has a continuous representative.

**Proof.**
By the already-proved symmetric principal-pivot lemma, such a `J` exists.
Condition on all coordinates `W=X_{J^c}`. The conditional polynomial in
`Y=X_J` is

`Y^T B Y + 2 b(W)^T Y + c(W)`.

The variables in `J` retain their original independent densities. By Theorem
3.1, for every fixed `W=w` the conditional output has a continuous density
`p_w(t)`. The previous local theorem gives the uniform domination

`0<=p_w(t)<=C_d/sigma_min(B)`

for all `w` and all `t` (choosing the continuous representative).

Measurability in `(w,t)` follows, for example, from the coarea formula or from
the limit of conditional interval averages. Hence

`p_Q(t)=int p_w(t) dP_W(w)`

is a density. For `t_n->t`, `p_w(t_n)->p_w(t)` pointwise in `w`, and the
displayed matrix-dependent bound is an integrable dominator. Dominated
convergence therefore gives `p_Q(t_n)->p_Q(t)`.

Thus `p_Q` is continuous and bounded. QED.

The target hypothesis of three eigenvalues with modulus at least one implies
`rank(A)>=3`, so Theorem 7.1 applies to every target instance. It is stronger
qualitatively than required for absolute continuity, but still weaker
quantitatively than the owner's conjecture because the displayed bound depends
on `A`.

## 8. Exact implication picture after this run

Under the exact target product hypotheses:

1. **Absolute continuity:** settled in much greater generality by the assigned
   partner: any nonzero quadratic applied to an absolutely continuous joint
   law is absolutely continuous.
2. **Finite essential boundedness for each fixed matrix:** already proved by
   the fleet02/B15 principal-pivot theorem for every `rank(A)>=3`.
3. **Continuous representative for each fixed matrix:** proved in this report
   for every `rank(A)>=3`, using product transversality plus the same physical
   `3/4` principal block.
4. **One universal height constant:** still open. The known fixed-matrix bound
   contains the factor `sigma_min(B)^(-1)`, which can diverge with dimension.

The logical notions must not be conflated. Absolute continuity alone does not
give a bounded density (rank-one square is the standard control). Essential
boundedness alone does not imply continuity for generic joint inputs (the
assigned partner's spherical-shell example). Conversely continuity by itself
does not supply the owner's matrix-independent height. The new theorem says
that the **specific original-coordinate product structure** rules out the
generic coarea jump mechanism once a nondegenerate physical block has
dimension at least three.

## 9. Sharpness control for continuity

The dimension-three threshold is not an artifact of the proof. Let
`X_1,X_2` be iid uniform on `[0,1]` and

`Q=X_1^2+X_2^2`.

For `0<t<1`,

`P(Q<=t)=pi t/4`,

so the density equals `pi/4` on `(0,1)`, while it is zero on `(-infinity,0)`.
No a.e.-equivalent representative can be continuous at `0`. Thus even a
positive-definite rank-two form with perfectly regular product inputs can have
a bounded but discontinuous density. Rank three is genuinely the first
dimension in which the present product-transversality regularity theorem can
hold without further assumptions.

## 10. What remains unpaid for the full conjecture

The regularity hierarchy is now qualitatively closed at target scope. The
remaining owner target is purely quantitative:

> prove a matrix- and dimension-independent linear small-ball estimate
> `P(X^T A X in I)<=C|I|` under the three-large-eigenvalue hypothesis.

The previous single-principal-block certificate cannot pay this uniformly:
its `sigma_min(B)^(-1)` can grow on diffuse/mixed-leverage matrices, and the
current correction inbox already records that a simple "good principal 3/4
block OR rank-three cross cut" dichotomy is false.

This report therefore does not propose continuity as a substitute for the
universal bound. It removes continuity as a separate obstruction and returns
the programme to the quantitative aggregate-curvature/bank-aggregation gap.

## 11. Corrections respected

No pointwise uniform oscillatory decay, no rotated-coordinate independence, no
generic joint-density continuity principle, no fixed fragment-count
localization, no fiberwise trace cap and no local/cross-rank3 dichotomy is
used. The product structure is retained until the two-coordinate chart step.
The generic shell obstruction from the assigned partner is explicitly
respected rather than contradicted.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**REGULARITY CHANGE:** `absolute continuity + fixed-A L-infinity, continuity
open -> absolute continuity + fixed-A bounded continuous density for every
rank(A)>=3`.

**FIRST REMAINING TARGET IMPLICATION:** replace the matrix-dependent physical
principal-block price by a universal aggregate-curvature payment.
