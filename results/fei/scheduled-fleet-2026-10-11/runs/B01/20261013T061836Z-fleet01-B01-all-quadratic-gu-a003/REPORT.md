# B01 / A003 — GU'(3,0) for every quadratic Boolean phase

**Run:** `20261013T061836Z-fleet01-B01-all-quadratic-gu-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Attempt:** `A003-GUP-ALL-QUADRATIC-6`  
**Status:** author-proved class theorem, pending A086/A094 independent review.  
**Full FEI:** **OPEN**.

## 1. Result

For every quadratic polynomial `q:F_2^n -> F_2`, including every rank,
linear term and constant term, let

`f(x)=(-1)^q(x)`.

With

`p(S)=hat f(S)^2`, `pi(S)=sum_(T superset S) p(T)`,

`U(f)=sum_S p(S) log_2(pi(S)/p(S))`, and

`G(f)=sum_i [U(f)-E U(f|x_i)]`,

one has the coordinatewise bound

`Delta_i U(f) <= 3 Inf_i(f)`                                      (1)

for every physical coordinate. Consequently

`G(f) <= 3 I(f)`.                                                  (2)

Thus the full restriction-closed class of quadratic Boolean phases satisfies
`GU'(3,0)`. The constant 3 is the sharp supremum: the even-dimensional
clique-quadratic phases from the preceding B01 run have

`G/I = 3-2^(2-n) -> 3`.

This strictly extends the earlier clique-quadratic and bent results. It allows
arbitrary alternating polar matrices of every rank, arbitrary affine shifts,
plateaued spectra, shared quadratic variables, and every physical restriction.
The constants do not depend on dimension, rank, support size, overlap degree,
or the number of restrictions.

There is also a sharper direct potential endpoint on this class:

`U(f) <= I(f)`,                                                     (3)

and `H(f)<=2I(f)`. Equation (3) is not used to prove (1); it is recorded to
separate the class endpoint from the GU mechanism.

## 2. Quadratic spectral form

Write the quadratic part of `q` by its alternating polar matrix `A`. If
`r=rank(A)`, the Walsh spectrum of `f` is flat on one affine coset

`C=b+im(A)`

of size `2^r` and vanishes off `C`. Hence the squared spectrum is the uniform
law on `C` and `H(f)=r`.

For any finite affine set `C` define

`N_C(s)=#{t in C:t superset s}` and
`mathcal U(C)=|C|^(-1) sum_(s in C) log_2 N_C(s)`.

Then `U(f)=mathcal U(C)`.

## 3. New coset-merge lemma

Let `V<=F_2^m`, and let `C_0=b+V` and `C_1=b+a+V` be distinct cosets. Put
`D=C_0 union C_1`. Then

`mathcal U(D) <= [mathcal U(C_0)+mathcal U(C_1)]/2 + 1`.            (4)

Proof. Fix `x in C_j` and put `R=supp(x)`. The within-coset upper fiber is

`N_(C_j)(x)=#{v in V: v|_R=0}`.

The cross-coset upper fiber is

`N_(C_(1-j))(x)=#{v in V: v|_R=a|_R}`.

Both are fibers of the same linear projection `V -> F_2^R`. Therefore the
cross fiber is either empty or has exactly the size of the within fiber. It
follows pointwise that

`log_2[N_D(x)/N_(C_j)(x)] in {0,1}`.

Averaging first over each coset and then over the two equal cosets gives (4).
This is the single-use upper-cone ownership missing from a generic mixture:
cross dominance can contribute one bit, never an ancestor or dimension
factor.

## 4. Coordinate proof of GU'(3,0)

Fix coordinate `i`, write its bit as `z`, and write the other bits as `y`.
Every quadratic polynomial has the form

`q(z,y)=q_0(y)+z(a dot y+beta)`.

Thus its two children are

`g(y)=(-1)^q_0(y)`,

`h(y)=(-1)^beta chi_a(y) g(y)`.

Let the squared spectrum of `g` be uniform on `C=b+V`. Multiplication by
`chi_a` translates the child support, so the squared spectrum of `h` is
uniform on `C+a`.

### 4.1 `a=0`

The function is either independent of `z` or is `chi_{i}` times a function
independent of `z`. In the first case `Inf_i=0`; in the second `Inf_i=1`.
Appending a fixed spectral zero or one coordinate does not change upper-fiber
ratios, and both children have the same `U`. Hence `Delta_i U=0`, proving (1).

### 4.2 `a in V`, `a!=0`

The two child supports coincide. Their Walsh coefficients have equal
magnitudes at every support point. The parent restriction formula

`hat f(s_i,t)=[hat g(t)+(-1)^s_i hat h(t)]/2`

therefore leaves exactly one of the two `s_i` values at every `t in C`. The
parent squared spectrum is uniform on a graph `{(lambda(t),t):t in C}`.
Every upper fiber in this graph injects into the corresponding upper fiber in
`C`, so `U(f)<=mathcal U(C)`. Since both children have potential
`mathcal U(C)`, `Delta_i U<=0`. Here `a!=0` also gives `Inf_i=1/2`, so (1)
holds.

### 4.3 `a notin V`

The child supports `C` and `C+a` are disjoint. At every point of their union
only one child Walsh coefficient is nonzero. The displayed restriction formula
then shows that the parent squared spectrum is the product of a fair
`s_i`-bit and the uniform law on `D=C union (C+a)`. Product additivity gives

`U(f)=1/2+mathcal U(D)`.

The coset-merge lemma gives

`Delta_i U <= 1/2+1=3/2`.

Because `a!=0`, the derivative in coordinate `i` is the balanced character
`(-1)^beta chi_a`, so `Inf_i=1/2`. This again proves (1), now with the sharp
constant `3` at the coordinate scale.

The three cases exhaust every coordinate. Summing (1) proves (2).

## 5. Direct `U<=I` and `H<=2I`

Let `M` be the coordinates on which the direction space `V=im(A)` is
nonconstant. Equivalently, `M` is the set of nonzero rows of `A`. Under the
uniform law on `C=b+V`, every coordinate in `M` is unbiased and every
coordinate outside `M` is fixed.

For `s in C`, a point of `C` dominating `s` can vary only at zero coordinates
of `s` lying in `M`. Therefore

`log_2 N_C(s) <= |M|-|s intersect M|`.

Averaging yields `U(f)<=|M|/2`. Meanwhile

`I(f)=E_(S uniform C)|S|=|M|/2 + (# fixed-one coordinates outside M)`,

which proves (3). Finally `H(f)=rank(A)<=|M|<=2I(f)`.

## 6. Exact verification

`CHECK_ALL_QUADRATIC_GU.py` exhausts all quadratic and linear coefficient
choices through five variables, quotienting only the irrelevant output sign.
It uses integer Walsh transforms and exact `Fraction` arithmetic. Every
quadratic spectrum is checked to be uniform on a power-of-two support, and
every upper-fiber count is checked to be a power of two before taking its
integer logarithm.

It verifies, for all 33,866 cases:

- `U<=I`;
- `H<=2I`;
- every coordinate inequality `Delta_i U<=3 Inf_i`;
- `G<=3I`.

The maximum observed `G/I` is `11/4` at dimensions four and five, agreeing
with the prior dense quadratic witness. The computation is a convention and
endpoint check; Sections 2--5 are the all-dimensional proof.

## 7. Scope and remaining universal gap

This run removes the earlier restriction to one parity-hyperplane child pair:
all affine plateaued child supports arising from quadratic phases are covered,
including a coherent merge of two translated plateaued cosets. The merge is
paid once because linear-projection fibers have equal size.

The proof does not extend to degree at least three. There, the two restrictions
need not have flat spectra on translates of one common affine space; cross
upper fibers need not be empty-or-equal, and a cross/within ratio can exceed
one. That is exactly where the aggregate `B_i-Gamma_i+KL_i` asymmetry mismatch
remains unpaid. No universal `a<infinity,b<1` has been proved for all Boolean
functions. Full FEI remains **OPEN**.

The next mathematical step is to replace the affine equal-fiber conclusion by
a stable inequality for approximately flat translated pieces: control the
average logarithm of the cross/within upper-fiber ratio by physical influence
plus a strict fraction of retained `U`, without paying the number of pieces.

## 8. Sources and provenance

- Owner control revision `2026-10-12.1`, Brain commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- A003 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Prior B01 quadratic report: canonical package commit
  `4b5c51804df04c0f4d5fecc679f49367297112db`, final receipt commit
  `bbb845720442decff5b478033fe992153b295590`.
- Accepted retained-difference telescope consulted for mechanism selection:
  B05 final canonical commit `31e667c3af7f8441f14ab4615c13f21590cf7264`,
  independently accepted by B19 final canonical commit
  `f832645b91bf1128824e8ee99749ae4a68c39a6c`. The present proof does not import
  that theorem.
- Source heads observed before save: canonical
  `f832645b91bf1128824e8ee99749ae4a68c39a6c`; Brain
  `12d1e2c226dda5f2847ad2b4ca6ed643e029749a`.

No external novelty claim is made. No protected source, paid compute, email,
public release, scheduler mutation, or subagent was used. Exposed model:
Codex; reasoning-effort metadata was not exposed.
