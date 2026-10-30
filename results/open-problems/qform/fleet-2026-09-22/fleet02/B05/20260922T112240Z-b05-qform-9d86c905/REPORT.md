# fleet02/B05 — quadratic-form bounded-density run

**Run:** `20260922T112240Z-b05-qform-9d86c905`  
**Classification:** `ESSENTIAL_STEP_APPLIED` / full target OPEN.  
**Control:** the later natural-language OWNER MESSAGE in `math-research-brain/scheduled_tasks/README.md` supersedes the stale FEI card and directs all workers to the quadratic-form bounded-density conjecture.  No FEI mathematics is advanced here.

## Target

Let `X=(X_1,...,X_n)` have independent real coordinates, each with a Lebesgue density `f_i` satisfying `0<=f_i<=1`.  Let `A` be real symmetric and suppose at least three eigenvalues of `A` have absolute value at least `1`.  Prove that `Q=X^T A X` has a density bounded by one universal constant, independent of `n`, `A`, and the coordinate laws.

## Source pins actually used

1. **fleet03/B17**, shared handoff commit `5a060b9340b64e27474a5d95d7b4782cfb894382`.  It proves two facts used below: (i) law-uniform pointwise stationary phase for an arbitrary density `f<=1` is false; (ii) the coordinate-diagonal target admits the sharper bound `pi` by choosing two same-sign large diagonal terms.
2. **fleet03/B16**, complete report commit `2dac8145f316ba9ecced5c98093efc681522a878` and shared handoff commit `79f65c176a98d37e67482ecedfb2b65e641251cc`.  It proves the sharp `L^{3/2}` bound `||p_{lambda X^2}||_{3/2}<=2|lambda|^{-1/3}`, refutes forgetting product structure after rotation, and proposes keeping the *unnormalized* coordinate-pair kernels in the symmetrized identity.  Section 3 below executes that proposal exactly.
3. Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016): a `k`-dimensional orthogonal marginal of a product density with one-dimensional factors bounded by one has density bounded by `2^{k/2}`.  I use only the `k=1` consequence.
4. Kwan--Sah--Sauermann--Sawhney, *Anticoncentration in Ramsey graphs and a proof of the Erdos--McKay conjecture*, arXiv:2208.02874, Theorem 1.6: for Gaussian quadratic polynomials, robust rank at least three gives the optimal linear small-ball scale, while robust rank two permits the `Z_1^2-Z_2^2` logarithmic obstruction.  This is supporting evidence for the threshold, not a theorem applicable to arbitrary bounded-density products.

## 1. Conditional end-to-end reduction and the first debt

Fourier inversion would finish the target from a uniform estimate

`int_R |E exp(i t X^T A X)| dt <= C_0`.

The owner's suggested stronger intermediate bound, obtained by multiplying three law-uniform one-dimensional `|t|^{-1/2}` estimates, is invalid: B16/B17 give an exact phase-matched-support falsifier with supremum one at every fixed nonzero frequency.  Thus the first real debt is not stationary phase for one arbitrary density.  It is a **product-structure-preserving rank-three averaged-frequency or linear small-ball inequality**.

This run derives two exact pieces for that debt and rules out two natural but insufficient repairs.

## 2. A full `L^p` family for one quadratic coordinate

### Proposition `QF-ONE-SQUARE-LP-v1`

Let `X` have a probability density `0<=f<=K`.  Let

`Z=lambda X^2 + b X + c`,  `lambda != 0`.

For every `1<p<2`, the density `h_Z` satisfies

`||h_Z||_p <= [2^{p-1}/(2-p)]^{1/p} K^{2-2/p} |lambda|^{1/p-1}`.                 (2.1)

At `p=3/2` this is

`||h_Z||_{3/2} <= 2 K^{2/3}|lambda|^{-1/3}`.                                  (2.2)

### Proof

Complete the square and translate `f`; translation does not change its mass or ceiling.  It is therefore enough to treat `Z=lambda X^2`.  For `r>0` put

`g(r)=f(r)+f(-r)`.

Then `0<=g<=2K` and `int_0^infinity g(r)dr=1`.  On the appropriate half-line, with `z=lambda r^2`,

`h_Z(z)=g(r)/(2|lambda|r)`,  `dz=2|lambda|r dr`.

Hence

`int h_Z(z)^p dz = (2|lambda|)^{1-p} int_0^infinity g(r)^p r^{1-p}dr`.          (2.3)

The weight `r^{1-p}` is decreasing.  Under `0<=g<=2K` and `int g=1`, the bathtub/rearrangement maximizer for the convex integrand is `g=2K 1_[0,1/(2K)]`.  Thus

`int g(r)^p r^{1-p}dr <= (2K)^{2p-2}/(2-p)`.                                  (2.4)

Combining (2.3)--(2.4) and taking the `p`th root gives (2.1).  For `p=3/2` the numerical factor is exactly two.  QED.

With Fourier convention `psi(t)=int e^{ity}h_Z(y)dy`, Hausdorff--Young gives

`||psi||_3 <= (2 pi)^{1/3} ||h_Z||_{3/2}`,

and therefore

`int |psi(t)|^3 dt <= 16 pi K^2/|lambda|`.                                    (2.5)

This is an averaged-frequency substitute for the false pointwise stationary-phase claim.

### Application to actual eigen-directions

If `r` is any unit vector and `Y=<X,r>`, the Livshyts--Paouris--Pivovarov marginal theorem gives `||p_Y||_infinity<=sqrt(2)`.  Therefore for `|lambda|>=1`,

`||p_{lambda Y^2}||_{3/2} <= 2^{4/3}|lambda|^{-1/3}`.                           (2.6)

The three large eigen-coordinates, however, are generally dependent.  Consequently their three characteristic functions cannot be multiplied as in the diagonal proof.  Formula (2.6) localizes the missing input to dependence/coupling rather than one-direction regularity.

The diagonal subclass itself is already stronger via B17: among three large diagonal coefficients two have the same sign, and the corresponding independent squared terms give the density bound `pi`; convolution with the remaining independent terms cannot increase `L^infinity`.

## 3. Exact unnormalized pair-kernel representation

This section executes fleet03/B16's proposed symmetrized route while retaining normalization exactly.

Let `X'` be an independent copy of `X`, and define

`phi_A(t)=E exp(i t X^T A X)`.

For the `i`th coordinate define the unnormalized pair kernel

`K_i(u,eta) = (1/2) int_R exp(i eta v) f_i((v+u)/2) f_i((v-u)/2) dv`

`             = exp(-i eta u) int_R exp(i 2 eta x) f_i(x)f_i(x-u) dx`.        (3.1)

### Proposition `QF-PAIR-KERNEL-MOYAL-v1`

For every real `t`,

`|phi_A(t)|^2 = int_{R^n} prod_i K_i(u_i, t(Au)_i) du`.                         (3.2)

Writing `h_i(u)=int f_i(x)f_i(x-u)dx`, one has

`|K_i(u,eta)|<=h_i(u)`,  `0<=h_i<=1`,  `int h_i=1`,                           (3.3)

and the exact phase-space budget

`int_R int_R |K_i(u,eta)|^2 du deta = pi (int f_i^2)^2 <= pi`.                 (3.4)

### Proof

Start from

`|phi_A(t)|^2 = int int exp(it(x^TAx-x'^TAx')) prod_i f_i(x_i)f_i(x'_i) dx dx'`.

Set `u=x-x'`, `v=x+x'`.  The Jacobian is `2^{-n}` and, since `A` is symmetric,

`x^TAx-x'^TAx' = u^T A v`.

The `v_i` integrations then separate and give (3.2) with (3.1).  The first three assertions in (3.3) are immediate from positivity, `f_i<=1`, and Fubini.

For fixed `u`, put `g_u(x)=f_i(x)f_i(x-u)`.  Plancherel with frequency `2 eta` yields

`int |K_i(u,eta)|^2 deta = pi int g_u(x)^2 dx`.

Integrating in `u` gives

`pi int int f_i(x)^2 f_i(x-u)^2 dx du = pi (int f_i^2)^2 <= pi`,

because `f_i<=1` and `int f_i=1`.  QED.

This is a genuinely law-independent quantitative resource that survives the conditioning problem noted by B16: no normalized conditional density of `X_i+X_i'` given `X_i-X_i'` ever appears.

## 4. Barrier: one symmetrization plus only the `L^2` phase-space budget loses half the needed exponent

The representation above is useful, but it also exposes a sharp limitation of the most immediate Brascamp--Lieb closure.

In the ideal three-coordinate transverse case, apply an absolute-value Brascamp--Lieb estimate to the three maps

`u -> (u_i, (Au)_i)`

with exponent `1/2` on each two-dimensional target.  Replacing the second target coordinate by `t(Au)_i` rescales each `L^2` norm by `|t|^{-1/2}`.  Thus the three phase-space budgets (3.4) can at best give, at this level of information,

`|phi_A(t)|^2 <= C_A |t|^{-3/2}`,

hence

`|phi_A(t)| <= C_A^{1/2}|t|^{-3/4}`.                                          (4.1)

The exponent `3/4` is not integrable at infinity.  This is a **mechanism barrier**, not a counterexample to the conjecture: cancellations or structure beyond generic `L^2` may improve (4.1), but an argument that squares once, takes absolute values, and uses only (3.4) cannot recover the required rank-three `L^1_t` bound.

The same square-root loss is visible directly in small-ball form.  If an estimate on the symmetrized variable gave

`P(|Q(X)-Q(X')|<=2 eps) <= C eps`,

then for every interval `I` of radius `eps`, independence only gives

`P(Q(X) in I)^2 <= P(|Q(X)-Q(X')|<=2 eps)`,

so the conclusion is merely `P(Q(X) in I)<=sqrt(C eps)`, not the required linear scale.

**Conclusion:** the B16 symmetrization is viable only if one exploits more than the generic `L^2` Moyal budget, avoids the final square root, or combines it with an independent smoothing/payment mechanism.

## 5. Barrier: the tempting two-dimensional coarea repair has an explicit growing cube-projection loss

B17 noted that two same-sign large eigendirections give a pointwise `pi` coarea bound on each fixed affine eigenplane, but integrating the crude bound over complementary fibers loses normalization.  That loss can be dimension-sized even for the most canonical product density.

Let `n` be even, let

`r_1=(1,...,1)/sqrt(n)`,

and let `r_2` have its first `n/2` entries `+1/sqrt(n)` and its last `n/2` entries `-1/sqrt(n)`.  These are orthonormal.  Put `E=span(r_1,r_2)` and take the product density

`F=1_[0,1]^n`.

Then

`int_{E^perp} sup_{z in E} F(w+z) dw`

is exactly the `(n-2)`-dimensional volume of the orthogonal projection of the unit cube onto `E^perp`.  The projection is a zonotope.  Its volume is the `l^1` norm of the Pluecker coordinates of `E`:

`Vol_{n-2}(P_{E^perp}[0,1]^n) = sum_{i<j} |r_{1i}r_{2j}-r_{1j}r_{2i}|`.          (5.1)

Pairs in the same half contribute zero; every cross-half pair contributes `2/n`, and there are `n^2/4` of them.  Therefore

`Vol_{n-2}(P_{E^perp}[0,1]^n) = n/2`.                                         (5.2)

So the naive bound obtained by taking a `pi` coarea estimate on every two-dimensional fiber and then integrating a fiberwise supremum can lose a factor `n/2`.  This is a concrete falsifier of that repair mechanism, not of the conjecture; a third large direction or a less lossy product inequality must pay for this projection growth.

## 6. Relation to the Gaussian rank-three theorem

Kwan--Sah--Sauermann--Sawhney prove for Gaussian inputs that a robust-rank-three quadratic polynomial has linear small-ball probability `O(eps/sigma)`, and explicitly note the robust-rank-two obstruction `Z_1^2-Z_2^2`, whose small-ball probability is of order `eps log(1/eps)`.  The theorem is not directly transferable to arbitrary bounded-density coordinate laws, but it supports the view that the unpaid step is a product-law analogue of robust-rank-three anticoncentration rather than a different spectral threshold.

## 7. Status and next essential implication

**Proved this run**

- `QF-ONE-SQUARE-LP-v1`: the full `1<p<2` family (2.1), extending B16's `p=3/2` endpoint calculation to arbitrary density ceiling and linear shift.
- `QF-PAIR-KERNEL-MOYAL-v1`: exact symmetrized product-kernel identity (3.2) and uniform Moyal budget (3.4).
- `QF-FIBER-SUP-BARRIER-v1`: explicit unit-cube / delocalized-plane family where the crude two-plane coarea averaging cost is `n/2`.

**Refuted as proof mechanisms**

- law-uniform one-variable pointwise stationary phase (inherited exact falsifier from B16/B17);
- one symmetrization + absolute values + only generic `L^2` pair-kernel budgets as a rank-three Fourier closure;
- two-plane coarea followed by fiberwise supremum integration.

**First unpaid implication**

Prove a dimension-free product-structure inequality that uses the third large spectral direction without either square-root loss or projection-volume loss.  Two concrete forms are:

1. a direct linear small-ball estimate `sup_u P(|X^TAX-u|<=eps)<=C eps`; or
2. a strengthened multilinear estimate for the kernels (3.1) that couples their `u`-marginal masses (3.3) with their phase-space budgets (3.4), rather than discarding the marginal information and applying bare `L^2` Brascamp--Lieb.

A successful estimate of type (2) would feed directly into (3.2) and is the most source-faithful continuation of B16's proposed route.

No full theorem is claimed.  No computation was needed for the identities or the cube-projection counterexample.
