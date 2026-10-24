SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T07:10:13Z.
attacking: probability-level extreme-product localization—replace fragment-by-fragment normalization by convex mixtures of unit-mass extreme marginals, so translations, distant fragments and unbounded supports carry zero certificate tax.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid localization issue

Account02/B14 r27 (`math-open-problems@ac36d657bbcb7bb560c74e2b7c1cb65c886b85a7`) computed the exact subprobability homogeneity of the Claude D_k volume certificate. If an active marginal is split into small subprobability fragments and the D_k estimate is applied cellwise, the mass exponent is below one on every volume-active coordinate. Equal N-way splitting of all active coordinates therefore creates an N^2 loss, independently of k. This is a proof-order obstruction, not a QFORM counterexample.

The correct localization object is not a partition into subprobabilities. It is a convex mixture of full probability densities of the extreme form `1_E`, `|E|=1`. The lemma below gives such mixtures constructively in L1 and therefore preserves any affine-uniform small-ball constant exactly.

## 2. One-dimensional probability-level mixture lemma

Let

`D={f in L1(R): 0<=f<=1 a.e., integral f=1}`.

Let `F` be the class of indicator densities `1_E` where `E` is a bounded finite union of intervals and `|E|=1`.

### Lemma 2.1

For every `f in D` and every `eps>0`, there exist finitely many weights `theta_r>=0`, `sum_r theta_r=1`, and sets `E_r in F` such that

`|| f - sum_r theta_r 1_(E_r) ||_1 < eps`.                     (2.1)

No common support radius, fragment-count bound, or moment bound is asserted.

### Proof

Choose R so that `tau=int_{|x|>R} f(x) dx < eps/8`. Let J be any bounded interval of length one disjoint from `[-R,R]`, and put

`g=f 1_[-R,R] + tau 1_J`.

Then `0<=g<=1`, `int g=1`, `g` has bounded support, and

`||f-g||_1 <= 2 tau < eps/4`.                                  (2.2)

Fix an integer N and partition a bounded interval containing `supp g` into finitely many half-open cells `I_1,...,I_M`, all of common length `1/N`. Let `s_N` be the conditional expectation of g on this partition (and zero outside). Then `0<=s_N<=1`, `int s_N=1`, and for N large

`||s_N-g||_1 < eps/2`.                                         (2.3)

Write `s_N=sum_k a_k 1_(I_k)`. Because `|I_k|=1/N`,

`0<=a_k<=1`,  and  `sum_k a_k=N`.                              (2.4)

The finite polytope

`P={a in [0,1]^M: sum_k a_k=N}`

has only 0-1 extreme points: if two coordinates are fractional, one can perturb them by `+delta,-delta`; if exactly one coordinate were fractional, the integer sum N would be impossible. Hence P is the convex hull of vectors `v^(r) in {0,1}^M` having exactly N ones. Thus

`a=sum_r theta_r v^(r)`, `theta_r>=0`, `sum_r theta_r=1`.       (2.5)

Set `E_r=union_{k:v_k^(r)=1} I_k`. Then `|E_r|=N*(1/N)=1` and

`s_N=sum_r theta_r 1_(E_r)`.                                  (2.6)

Equations (2.2)-(2.6) prove (2.1). QED.

## 3. Product and random-environment localization

Let `f_i in D`, `i=1,...,m`. Applying Lemma 2.1 with errors `eps/m` gives finite mixtures

`g_i=sum_{r_i} theta_(i,r_i) 1_(E_(i,r_i))`

with `||f_i-g_i||_1<eps/m`. Since all factors have L1 norm one,

`|| prod_i f_i - prod_i g_i ||_1 <= sum_i ||f_i-g_i||_1 < eps`. (3.1)

Expanding the product,

`prod_i g_i = sum_r Theta_r prod_i 1_(E_(i,r_i))`,             (3.2)

where `Theta_r=prod_i theta_(i,r_i)` and `sum_r Theta_r=1`.

Now let `(Z,eta)` be an arbitrary probability space and let `F_z:R^m->R` be any jointly measurable family. For every interval J define

`T_f(J)=int_Z int 1_{F_z(x) in J} prod_i f_i(x_i) dx d eta(z)`.

By (3.1), `|T_f(J)-T_g(J)|<=eps`. By (3.2), `T_g(J)` is a convex combination of the corresponding extreme-product probabilities. Therefore, if

`int_Z int 1_{F_z(x) in J} prod_i 1_(E_i)(x_i) dx d eta(z) <= C |J|`  (3.3)

for every `E_i in F`, every interval J, and the whole parameter family `F_z`, then letting `eps->0` yields exactly

`T_f(J)<=C|J|`                                                  (3.4)

for every arbitrary cap-one product law. The constant C is unchanged.

This includes arbitrary outside-generated affine terms, because one may take

`F_z(x)=x^T Bx + ell(z)^T x + c(z)`.

No normalization of a thin fiber occurs; the same unit-mass extreme marginal is used as a probability density before any component intervals inside `E_i` are examined.

## 4. Immediate comparison with the partner D_k fragment tax

For the target-valid matrix

`A_5 = [[0,I_5],[I_5,0]]`,

all ten nonzero eigenvalues are `+1` or `-1`. Claude D5 gives the whole-law estimate

`||p_(X^T A_5 X)||_infinity <= 5 sqrt(2e)`.                    (4.1)

Account02/B14 r27 shows that if each active marginal is first split into N equal distant subprobability fragments and its subprobability D5 estimate is summed over the `N^10` cells, the resulting black-box certificate is only

`5 sqrt(2e) N^2`.                                              (4.2)

Lemma 2.1/Section 3 gives the exact repair: approximate each full marginal by a convex mixture of unit-measure indicator probability densities, apply (4.1) to each extreme product component, and average. One recovers (4.1) with no N dependence. In the special remote-fragment law

`f_N=1_( union_{j=1}^N [4^j,4^j+1/N] )`,

the marginal is itself already one extreme point of D, so no mixture or componentwise fragment normalization is needed at all.

The mathematical distinction is therefore exact:

* **unsafe:** split an extreme support into subprobability interval pieces and normalize/pay the analytic certificate on every Cartesian cell;
* **safe:** keep each unit-mass extreme support whole, or approximate a general cap-one density by a convex mixture of such whole unit-mass extreme supports, apply the probability theorem, then average.

This gives a zero-tax localization mechanism compatible with arbitrary translations, arbitrarily distant fragments and unbounded supports. The full QFORM conjecture remains open because one still needs an exhaustive matrix certificate from `s_3(A)>=1`; this lemma removes only the law/localization loss.
