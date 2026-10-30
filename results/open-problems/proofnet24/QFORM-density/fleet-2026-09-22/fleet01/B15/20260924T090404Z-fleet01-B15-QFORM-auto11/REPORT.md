SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-24T09:04:04Z.
attacking: exact separation of qualitative absolute continuity, fixed-instance C0 regularity, and the still-open matrix-uniform height theorem; audit the fixed-rank regularity bridge and apply the latest fleet02/B15 ruled theorem to a genuinely anisotropic exact-target family.

# fleet01/B15 — the target regularity ledger closes at C0; the universal problem is exactly height

Status: `TARGET_C0_LEDGER_CLOSED / BEST-CONSTANT-SMOOTH-ROUGH-EQUIVALENCE / PARTNER_APPLIED / FULL_QFORM_OPEN`.

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`; owner control revision `2026-09-22.15` read at `math-research-brain@33056a258ac41cf4c874419503b9ff920f5dfbb8`. Execution remains `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner theorem is **not proved**. The new point is a precise regularity closure: for the owner target, existence of a canonical continuous density is already a fixed-instance theorem, and the optimal universal height constant is exactly the same whether one works with arbitrary rough cap-one product marginals or only smooth compactly supported cap-one marginals. Thus continuity can be removed completely from the central universal-height proof obligation.

## 1. Qualitative absolute continuity is much weaker than the target

### Lemma 1.1 — nonconstant quadratic pushforwards preserve null sets under AC input

Let `A!=0` be real symmetric and let `X` have any absolutely continuous joint law on `R^n`; independence and the cap-one assumption are not needed. Then

`Q=X^T A X`

is absolutely continuous on `R`.

**Proof.** Put `q(x)=x^T A x`. Its critical set is

`Crit(q)={x: grad q(x)=0}=ker A`,

which is a proper linear subspace and hence Lebesgue-null. If `N subset R` is Lebesgue-null, set

`E_k=q^{-1}(N) intersect {|grad q|>=1/k}`.

Coarea gives

`integral_(E_k) |grad q(x)| dx
 = integral_N H^{n-1}(q^{-1}(t) intersect {|grad q|>=1/k}) dt=0`.

Because `|grad q|>=1/k` on `E_k`, `|E_k|=0`. Also

`q^{-1}(N) subset ker A union union_(k>=1) E_k`,

so `q^{-1}(N)` is Lebesgue-null. An absolutely continuous input therefore gives it probability zero. This proves `Q<<dt`.

This is only a null-set statement. It gives neither a bounded density nor continuity and does not invoke the refuted arbitrary-joint rank-three coarea-cap mechanism.

## 2. Fixed-target C0 regularity is already unconditional for rank >=3

A source-pinned fleet03/B15 theorem at

`yspennstate/math-open-problems@696a0784ba7d270db657c1596d9c2ee940a1745d`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260924T032517Z-fleet03-B15-qform-auto32/REPORT.md`

proves the following fixed-matrix statement:

> For every fixed real symmetric `A` with `rank(A)>=3` and every cap-one product input, the quadratic output has a canonical density in `C_0(R)`. More quantitatively, replacing one original-coordinate marginal by a cap-one subdensity of mass `m` gives a fixed-matrix bound `K(A,j) sqrt(m)`; consequently cap-preserving input mollification converges uniformly at the output-density level.

The coefficient `K(A,j)` can degenerate arbitrarily with the geometry of `A`; this theorem is **not** the owner universal-height theorem.

Because `s_3(A)>=1` implies `rank(A)>=3`, every single instance in the owner's target class already has a canonical `C_0` density. In particular, the remaining owner problem is not existence or fixed-instance continuity; it is the one constant uniform in `n`, `A`, and all cap-one product laws.

### Structural audit: why a fixed physical carrier of size 3 or 4 always exists

For completeness, every real symmetric matrix of rank at least three contains an invertible original-coordinate principal block of order `3` or `4`.

Use symmetric elimination. A nonzero symmetric matrix has either a nonzero diagonal entry, giving an invertible `1x1` principal pivot, or all diagonals vanish and some off-diagonal entry `a_ij` is nonzero, giving the invertible principal pivot

`[[0,a_ij],[a_ij,0]]`.

After such a pivot `P`, pass to the Schur complement `S`; congruence gives

`rank A = rank P + rank S`,

and if `K` is a principal pivot of `S`, determinant factorization gives

`det A[J union K,J union K]=det P * det S[K,K] !=0`,

where `J` is the previously selected original-coordinate set. Repeat until the accumulated pivot size first reaches at least three. Each increment is one or two, so the first such size is `3` or `4`. This argument never rotates the product law.

Size four can genuinely be necessary for this particular carrier statement: the symmetric matrix

`[[0,0,1,0],
  [0,0,0,1],
  [1,0,0,0],
  [0,1,0,0]]`

has rank four while every odd-order principal determinant vanishes.

Conditioning on all outside **original** coordinates leaves an affine quadratic in the selected independent physical coordinates. The fixed-block certificates used by fleet03 are uniform in those affine terms; averaging over the conditioned coordinates then preserves the paid interval height. No post-rotation independence is used.

## 3. Same-height canonical C0 transfer

### Lemma 3.1 — an essential height becomes the identical pointwise height

Let a probability law have a canonical continuous density `p_c in C_0(R)`. If

`P(Q in I)<=M |I|`

for every interval `I`, then

`boxed( sup_t p_c(t) <= M. )`

**Proof.** Interval domination gives `p_c<=M` almost everywhere. If `p_c(t_0)>M`, continuity supplies an open interval on which `p_c>M`, contradicting the a.e. bound. Equivalently, for a nonnegative continuous density,

`sup_I P(Q in I)/|I| = ||p_c||_infinity`.

Thus a future universal interval estimate does not need a second regularity proof and loses no constant when passed to the canonical continuous representative.

## 4. Exact best-constant equivalence: rough = smooth compact = interval

Let `T` be the owner target class of all tuples `(n,A,f_1,...,f_n)` with `A=A^T`, `s_3(A)>=1`, independent marginals `0<=f_j<=1`, `integral f_j=1`. Define

`C_rough = sup_T ||p_can||_infinity`,

where `p_can` is the fixed-instance canonical `C_0` density from Section 2. Let `C_sm` be the same supremum restricted to

`f_j in C_c^infinity(R), 0<=f_j<=1, integral f_j=1`,

and let

`C_int = sup_T sup_(interval I) P(Q in I)/|I|`.

These quantities are allowed to be `+infinity`.

### Theorem 4.1 — `QFORM-TARGET-REGULARITY-EQUIVALENCE-v1`

`boxed( C_rough = C_sm = C_int. )`

In particular,

`boxed( C_rough<infinity iff C_sm<infinity, with exactly the same best constant. )`

**Proof.** Section 3 gives `C_rough=C_int` instance by instance. Trivially `C_sm<=C_rough`.

For the reverse inequality, fix one rough target instance. Every cap-one marginal has cap-preserving compact-smooth `L1` approximants. One explicit construction is: truncate the marginal so the discarded tail has mass `epsilon`; replace that lost mass by a cap-one set of finite measure outside the truncation window; then convolve with a compactly supported nonnegative probability mollifier. The result is a compactly supported smooth probability density still bounded by one, and its `L1` distance from the original tends to zero.

For product densities `F=prod_j f_j` and `G=prod_j g_j`,

`||F-G||_1 <= sum_j ||f_j-g_j||_1`.

A deterministic pushforward contracts total variation, so the quadratic output measures of the smooth approximants converge in total variation to the rough output measure. If `C_sm<infinity`, each smooth approximant satisfies

`mu_k(I)<=C_sm |I|`

for every interval. Passing to the total-variation limit gives

`mu(I)<=C_sm |I|`

for every interval. Lemma 3.1 and the already-established canonical `C_0` representative then give

`||p_can||_infinity<=C_sm`.

Taking the supremum over rough instances yields `C_rough<=C_sm`. If `C_sm=+infinity` the reverse inequality is trivial. Hence all three constants agree.

**Interpretation.** The fleet may attack the owner theorem solely on smooth compactly supported cap-one marginals, using any product-preserving analytic method that is legitimate there. A bound obtained in that smooth category returns to arbitrary measurable cap-one marginals with the identical final constant. Output continuity is neither a premise nor a source of height.

## 5. Uniqueness and the correct regularity endpoint

The `C_0` representative is unique: two continuous densities representing the same measure agree almost everywhere; their continuous difference cannot be nonzero at one point without being nonzero on a positive-measure neighborhood.

This is essentially the correct class-uniform endpoint. The earlier fleet01/B15 phase-aligned construction at

`yspennstate/math-open-problems@a2f4a2724486aef1a765fffe49c1c5bc3943be3e`

already shows that even for fixed `A=I_3`, smooth compactly supported cap-one iid inputs and a common finite output-height bound, the output densities need not have any law-uniform modulus of continuity. Hence the owner theorem should not be burdened with a uniform Holder/Lipschitz conclusion: canonical `C_0` exists instancewise, while the one universal quantitative object still sought is height.

## 6. Required fleet02/B15 result applied to an actual anisotropic target inequality

The latest completed partner source is

`yspennstate/math-open-problems@847a25a6130a1470eb8f1abbb298ae5e5f1cdc8f`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260924T070011Z-fleet02-B15-qform-auto11-r1/REPORT.md`.

Its anisotropic ruled theorem applies to

`q(X)=lambda_1 <r_1,X>^2 + lambda_2 <r_2,X>^2 - mu <r_3,X>^2`,

with orthonormal spectral columns but **without assuming the rotated coordinates are independent**. It gives the majority-sheet coefficient

`C_+ = (lambda_1 lambda_2 mu)^(-1/2)
       integral_0^(2pi)
       [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta`,

and, if the maximum original-row leverage is at most `1/2`, the source-stability bound

`||r_f^+-r_g^+||_infinity <= sqrt(2) C_+ Delta`,

where `Delta=sum_j ||f_j-g_j||_1`.

Take three disjoint original-coordinate banks of size `m>=2` and define

`Y_k = m^(-1/2) sum_(j=1)^m X_(k,j)`,

`Q_m = 4Y_1^2 + Y_2^2 - Y_3^2`.

The original matrix has nonzero spectrum

`{4,1,-1}`,

so it is exactly in the owner target. Every row leverage is `1/m<=1/2`.

For `(lambda_1,lambda_2,mu)=(4,1,1)`, the partner coefficient simplifies exactly to

`C_+
 = (1/2) integral_0^(2pi) [2-(3/4)sin^2 theta]^(-1/2) dtheta
 = sqrt(2) K(3/8)`,

where

`K(3/8)=integral_0^(pi/2) [1-(3/8)sin^2 theta]^(-1/2) dtheta`.

Numerically,

`K(3/8)=1.7605688117719545...`,

`C_+=2.489820291098983...`.

Therefore the completed partner theorem gives the concrete rough-input inequality

`boxed(
 P(Q_m in I, Q_m>=0)
 <= sqrt(2) K(3/8) |I|
 < 2.490 |I|,
)`

for every interval `I`, every `m>=2`, and arbitrary independent cap-one marginals in all `3m` original coordinates.

It also gives the genuinely dimension-free rough-source stability estimate

`boxed(
 ||r_f^+-r_g^+||_infinity
 <= 2 K(3/8) sum_(k,j)||f_(k,j)-g_(k,j)||_1
 < 3.522 Delta.
)`

Equivalently, the majority-sheet triangular kernel obeys

`E[(epsilon-|Q_m-y|)_+ 1_{Q_m>=0}]
 <= sqrt(2)K(3/8) epsilon^2`.

This is an actual completed partner result used at a non-isotropic exact-target inequality; no projection-only shortcut or post-rotation independence is being asserted.

## 7. A full-density bound for the same anisotropic diffuse family

Because the three banks above are disjoint original-coordinate banks, `Y_1,Y_2,Y_3` are genuinely independent. The one-dimensional product-projection theorem used in the partner source gives

`||p_(Y_k)||_infinity<=sqrt(2)`.

For `s>0`, the square-pushforward formula therefore gives

`p_(4Y_1^2)(s)<=1/(sqrt(2)sqrt(s))`,

`p_(Y_2^2)(s)<=sqrt(2)/sqrt(s)`.

Consequently

`p_(4Y_1^2+Y_2^2)(t)
 <= integral_0^t du/[sqrt(u)sqrt(t-u)]
 = pi`.

Convolution with the independent probability law of `-Y_3^2` cannot increase `L^infinity`, so

`boxed( ||p_(Q_m)||_infinity <= pi )`

uniformly in `m>=2` and all cap-one marginals. By the fixed-target theorem in Section 2, the canonical density is also in `C_0(R)` with the same pointwise bound.

This family again illustrates why reciprocal payment of one physical `3x3` minor is the wrong global interface: each physical coefficient is only `O(1/m)`, yet bank aggregation yields a uniform full-density bound.

## 8. What remains unpaid

The universal owner theorem is still OPEN. Sections 1--5 remove regularity as a possible hidden obstruction:

- `A!=0` + absolutely continuous joint input => qualitative absolute continuity;
- fixed `rank(A)>=3` + cap-one product input => a unique canonical `C_0` density, with a finite matrix-dependent height;
- under the owner target, the best universal rough height constant is exactly the best smooth-compact height constant;
- any universal interval domination immediately becomes the identical pointwise bound on the canonical `C_0` representative;
- no class-uniform modulus stronger than `C_0` should be expected.

The first unpaid implication is therefore purely quantitative and structural: prove one matrix- and dimension-independent interval-height bound on the smooth compact product core under only `s_3(A)>=1`. The live diffuse-bank examples show why local physical-minor inversion can deteriorate while the true density stays bounded. Any successful proof still has to aggregate original-coordinate product geometry before paying such reciprocal local parameters.

## Corrections preserved

This report does not use or imply:

- law-uniform pointwise quadratic Fourier decay;
- independence after spectral rotation;
- a projection/X-ray-only closure;
- the refuted arbitrary-joint rank-three coarea density cap;
- a universal conditional-projection density moment gate;
- a good single physical triple under `s_3(A)>=1`.

The newest correction inbox was re-read before publication. Full QFORM remains OPEN.
