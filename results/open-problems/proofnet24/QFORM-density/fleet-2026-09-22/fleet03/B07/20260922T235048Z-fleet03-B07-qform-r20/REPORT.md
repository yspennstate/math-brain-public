SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T23:50:48Z.
attacking: shared-coordinate third-compound mass — exact scalar-pivot Schur transfer one exterior degree down, plus a quarter-Riesz square transducer for the tiny-nonzero-pivot survivor.

# fleet03/B07 r20 — shared third-compound / Schur-compound transfer and quarter-Riesz square interpolation

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** coordinate minor selection / GEOMETRY  
**Run:** `20260922T235048Z-fleet03-B07-qform-r20`  
**Owner control at start:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_AND_ANALYTIC_THEOREMS / FULL_TARGET_OPEN`.

The full target remains unchanged and open: for arbitrary dimension, independent original real coordinates with scalar densities at most one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a valid target counterexample. No moment, support, Gaussian, log-concavity, connected-support, or post-rotation independence hypothesis is used below. Continuity of the full target remains open.

The live correction discipline is enforced. In particular, this run does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea bound, a worst conditional projected-density cap, a one-good-minor inference from aggregate mass, or the false idea that a tiny nonzero scalar square can simply be replaced by a zero pivot.

## 1. Incoming state and completed peer inputs

The latest own B07 run reduced the two-star scalar-Schur survivor to a physical anchor with a large outside row and a genuinely tiny nonzero diagonal. The current purpose is to keep exact determinant weights when such a scalar pivot is made, rather than losing the third-compound resource to one selected local minor.

Two completed inputs are used at their exact scopes.

1. **fleet02/B19 scalar-Schur second-compound reduction.**  
   Canonical report: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T192830Z-fleet02-B19-qform-r17/REPORT.md`. It proves that for every genuine physical scalar pivot `a=A_ii!=0`, with exact Schur complement `S_i`, the owner hypothesis `s_3(A)>=1` implies `s_2(S_i)>=1`, hence the full second-compound mass `M_2(S_i)=e_2(S_i S_i^T)>=1`. It then decomposes that second compound into disjoint, one-shared and principal-pair physical overlap classes.

2. **fleet02/B07 random-shift zero-self theorem plus fleet04/B18 sharp product-projection transfer.**  
   fleet02/B07 canonical report: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T223302Z-fleet02-B07-QFORM-ddc6a5/REPORT.md`. It uses the completed fleet04/B18 rearrangement/product-projection input from `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md` to prove that if a quadratic residual `H` has an exact zero-self physical coordinate whose off-diagonal row has Euclidean norm `eta>0`, then

   `H_(1/2)(H):=sup_t E|H-t|^(-1/2) <= (16/sqrt(3)) eta^(-1/2).`       (1.1)

   This statement allows arbitrary curvature on all complementary coordinates. The fleet04 theorem enters the actual inequality through the product-projection density bound for the linear coefficient bank; no rotation of the independent source coordinates is made.

The designated fleet04/B07 current-QFORM artifact was checked and was still absent, so no theorem is fabricated or attributed to it. The compatible completed fleet04/B18 theorem is the fleet04 mathematics actually consumed below.

## 2. Exact scalar-pivot transfer of shared third-compound weight

Let `A` be any real symmetric `n x n` matrix. For a physical coordinate `i`, define

`W_i(A):=sum_{R,C subset [n]\{i}, |R|=|C|=2}
              det A[{i} union R,{i} union C]^2.`                         (2.1)

This quantity is defined even when `A_ii=0`; it is the entire squared third-minor mass whose row and column triples share the physical coordinate `i`.

Assume now

`a_i:=A_ii !=0`,                                                          (2.2)

write `b_i=A_[hat i,i]`, `C_i=A_[hat i,hat i]`, and let

`S_i=C_i-b_i b_i^T/a_i`                                                   (2.3)

be the exact physical Schur complement.

### Theorem 2.1 — `QFORM-SHARED3-SCALAR-SCHUR-COMPOUND-v1`

For every nonzero physical pivot `a_i`,

`boxed: W_i(A)=a_i^2 M_2(S_i),`                                           (2.4)

where

`M_2(S_i):=sum_{|R|=|C|=2} det S_i[R,C]^2
          =||wedge^2 S_i||_F^2
          =e_2(S_i S_i^T).`                                               (2.5)

Thus **all** shared-coordinate third-minor weight through a physical pivot descends exactly one exterior degree under the scalar Schur complement. There is no reciprocal selection of one minor and no loss of aggregate determinant weight.

#### Proof

For every two-subsets `R,C` of the residual coordinates, order the shared coordinate first. The corresponding `3 x 3` minor is

`[[a_i, b_i[C]^T],
  [b_i[R], C_i[R,C]]].`

The block determinant identity gives

`det A[{i} union R,{i} union C]
 =a_i det(C_i[R,C]-b_i[R]b_i[C]^T/a_i)
 =a_i det S_i[R,C].`                                                       (2.6)

Squaring (2.6) and summing over every ordered pair `(R,C)` proves (2.4). Equation (2.5) is the Cauchy--Binet/Frobenius identity for the second compound. QED.

### Exact global overlap bookkeeping

For `q=0,1,2,3`, define the full third-compound overlap energy

`E_q(A):=sum_{|I|=|J|=3, |I intersect J|=q} det A[I,J]^2.`                (2.7)

Every ordered triple pair `(I,J)` is counted in `W_i` once for each `i in I intersect J`. Therefore

`boxed: sum_i W_i(A)=E_1(A)+2E_2(A)+3E_3(A).`                              (2.8)

Combining (2.4) with (2.8), and denoting the zero-diagonal set by `Z={i:A_ii=0}`, gives the exact decomposition

`boxed:
 E_1+2E_2+3E_3
 = sum_{i in Z} W_i(A)
   +sum_{i notin Z} A_ii^2 M_2(S_i).
`                                                                         (2.9)

This is the desired determinant-weighted conditioning ledger for every non-disjoint third-minor class. Exact zero pivots remain exact zero pivots; every nonzero pivot is transferred to the exact physical Schur second compound.

### Consequence under the owner spectral hypothesis

The completed fleet02/B19 theorem says that, whenever `A_ii!=0` and `s_3(A)>=1`,

`M_2(S_i)>=1.`                                                            (2.10)

Hence (2.9) immediately yields

`boxed:
 E_1+2E_2+3E_3 >= sum_i A_ii^2.
`                                                                         (2.11)

Equation (2.11) is not a density theorem. Its use is structural: if the non-disjoint third-compound energy is small, then the entire physical diagonal is small in `l^2`; if it is large, (2.9) says precisely how much of that energy sits on exact-zero star pivots versus genuine Schur second compounds. The remaining difficulty is to **pay this aggregate pivot mixture without selecting one dimension-dependent pivot**.

## 3. A new dependence-safe square interpolation theorem

The current tiny-nonzero-pivot problem cannot be handled by continuity from the zero-pivot theorem: a nonzero self coefficient can align with the random shift and collapse to one square. The next lemma instead asks the exact Schur remainder to supply a fractional-trace bound and quantifies how much is lost when the square is restored.

For a random variable `V`, write

`H_(alpha)(V):=sup_t E|V-t|^(-alpha)`                                      (3.1)

when finite.

### Lemma 3.1 — weak-`L^2` quadratic kernel

Let `f` be a probability density with `0<=f<=1`. For `A,u>0`, every center `m`, and either sign `epsilon in {+1,-1}`,

`boxed:
 int_R f(x) |A(x-m)^2+epsilon u|^(-1/2) dx
 <=4 A^(-1/4) u^(-1/4).
`                                                                         (3.2)

#### Proof

Put `r=sqrt(u/A)` and `y=(x-m)/r`. Then the left side equals

`A^(-1/2) int g(y) k_epsilon(y) dy`,                                     (3.3)

where `g(y)=f(m+ry)` satisfies `0<=g<=1` and `int g=1/r`, and

`k_+(y)=(1+y^2)^(-1/2)`,
`k_-(y)=|y^2-1|^(-1/2).`                                                   (3.4)

For every `s>0`, direct solution of the one-dimensional sublevel sets gives

`|{k_+>s}| <=2 s^(-2),`
`|{k_->s}| <=4 s^(-2).`                                                    (3.5)

Indeed, for `k_-` and `s>1`, with `delta=s^(-2)<1`, the set has measure

`2(sqrt(1+delta)-sqrt(1-delta))<=4delta=4s^(-2)`;

for `s<=1` it has measure `2sqrt(1+s^(-2))<=2sqrt(2)s^(-1)<=4s^(-2)`. The plus case is easier.

If a nonnegative kernel satisfies `|{k>s}|<=B s^(-2)`, then for every `0<=g<=1` of mass `L`, layer cake gives

`int gk
 <=int_0^infinity min(L,Bs^(-2)) ds
 =2 sqrt(BL).`                                                            (3.6)

Use `B=4`, `L=1/r` in (3.3):

`int f |A(x-m)^2+epsilon u|^(-1/2)
 <=4 A^(-1/2) r^(-1/2)
 =4 A^(-1/4)u^(-1/4).`                                                    (3.7)

QED.

### Theorem 3.2 — `QFORM-SQUARE-HALFRIESZ-QUARTERROOT-v1`

Let `X` have a probability density at most one and be independent of a random element `Y`. Let `m(Y),H(Y)` be arbitrary measurable functions and let `d!=0`. Put

`F=d(X+m(Y))^2+H(Y).`                                                      (3.8)

If `H_(1/2)(H)<=K<infinity`, then

`boxed:
 H_(1/2)(F) <=4 |d|^(-1/4) K^(1/2).
`                                                                         (3.9)

No independence between `m(Y)` and `H(Y)` is needed, and all quadratic curvature hidden inside `H` is retained.

#### Proof

Fix `t`. Finiteness of `H_(1/2)(H)` implies `H` has no atom at `t`, so `u=|H(Y)-t|>0` almost surely. Conditional on `Y`, the translate `X+m(Y)` still has density cap one. Apply Lemma 3.1 with `A=|d|` and the sign determined by `d(H-t)`:

`E_X |F-t|^(-1/2)
 <=4 |d|^(-1/4)|H-t|^(-1/4).`                                             (3.10)

Average in `Y` and use Cauchy--Schwarz,

`E|H-t|^(-1/4)
 <=(E|H-t|^(-1/2))^(1/2)
 <=K^(1/2).`                                                              (3.11)

Taking the supremum in `t` proves (3.9). QED.

### Why this does not violate the same-square correction

If the Schur remainder is identically zero, then `K=infinity`, so (3.9) says nothing. In particular the exact counterexample

`dX^2+2XY+Y^2/d=d(X+Y/d)^2`

is not paid: after completing the square its remainder is zero and has infinite half-Riesz potential. Thus (3.9) spends genuine residual smoothing rather than treating a small nonzero square as a harmless perturbation.

## 4. Actual application to the current tiny-nonzero-pivot chamber

Write the current residual after a genuine physical pivot as

`R=d(X_i+h(Z))^2+H(Z),   0<|d|<1/16,`                                    (4.1)

where all coordinates in `Z` remain the original independent product bank. The new theorem gives a quantitative bridge from any completed half-Riesz payment for the exact Schur remainder `H`.

### 4.1 Zero-self strong row in the inner Schur remainder

Suppose `H` has a physical coordinate `j` with exact zero self coefficient and full off-diagonal row norm `eta>0`. The completed fleet04/B18 product-projection inequality, as used in fleet02/B07's random-shift theorem, yields the actual bound (1.1):

`H_(1/2)(H) <=(16/sqrt(3)) eta^(-1/2).`                                   (4.2)

Substitution into (3.9) gives the new composite inequality

`boxed:
 H_(1/2)(R)
 <=16*3^(-1/4) |d|^(-1/4) eta^(-1/4)
 <12.158 (|d| eta)^(-1/4).
`                                                                         (4.3)

In particular, the tiny-pivot branch is **uniformly paid** whenever the exact inner Schur remainder exposes a zero-self row at the natural reciprocal scale

`eta >= |d|^(-1),`                                                        (4.4)

because then

`boxed: H_(1/2)(R)<12.158.`                                                (4.5)

This is an actual application of the completed fleet04/B18 product-projection result to a new inequality; the fleet04 theorem supplies the density control on the physical linear coefficient bank inside (4.2).

### 4.2 Diffuse two-eigenvalue inner Schur window at the natural reciprocal scale

The completed fleet01/B09 theorem `QFORM-TWOEIG-RIDGE-HALFRIESZ-v1` gives, after scaling, the following: if a symmetric inner Schur matrix `T` has at least two eigenvalues of modulus at least `sigma>0` and its `sigma/64` spectral window has maximum physical leverage at most `1/32`, then

`H_(1/2)(Z^T T Z + affine) <25.46 sigma^(-1/2).`                           (4.6)

Applying (3.9),

`boxed:
 H_(1/2)(R)
 <4 sqrt(25.46) (|d| sigma)^(-1/4)
 <20.184 (|d| sigma)^(-1/4).
`                                                                         (4.7)

Thus this branch is uniformly paid whenever

`sigma >= |d|^(-1).`                                                      (4.8)

The same conclusion with the weaker constant `4sqrt(128)<45.255` follows from the completed hollow-two-eigen theorem when the inner Schur matrix is hollow.

Hence a current tiny-nonzero-pivot survivor must now avoid **both** natural-scale exits: it cannot expose a zero-self physical row of norm at least `|d|^(-1)`, and it cannot have two reciprocal-scale eigenvalues in a diffuse high spectral window. The obstruction is therefore concentrated on a one-huge-direction / high-leverage / non-hollow inner Schur geometry rather than on arbitrary tiny nonzero pivots.

## 5. How the two new theorems fit the coordinate-minor programme

The structural and analytic pieces fit exactly as follows.

1. Full third-compound mass is first split by row/column overlap in original coordinates.
2. Every non-disjoint third minor carries one, two, or three shared physical coordinates.
3. Equation (2.9) says that choosing any **genuine** shared pivot transfers its complete determinant weight to the exact Schur second compound with factor `A_ii^2`; exact-zero shared pivots remain on the zero-self route.
4. fleet02/B19 then decomposes the Schur second compound into disjoint-two-volume, one-shared, and principal-pair banks, again before selecting a tiny pair.
5. If a later scalar pivot is tiny but nonzero, Theorem 3.2 allows already-proved half-Riesz smoothing in its exact Schur remainder to be spent with only a quarter-root loss. At the natural `1/|d|` scale, the loss cancels completely in (4.5) and (4.7).

What is **not** proved is a dimension-free selection of one pivot from (2.9). The exact aggregate may be spread over many physical coordinates, and dividing by the number of pivots would reintroduce forbidden dimension loss. The correct remaining interface is therefore an aggregate pivot/Schur transducer, not `max_i W_i`.

## 6. Exact computation checks

The accompanying checker uses a symmetric integer `5 x 5` matrix. For every one of its five nonzero diagonal pivots it verifies with exact rational arithmetic that

`W_i(A)-A_ii^2 M_2(S_i)=0`.

The five common values are

`7877, 16736, 19581, 27032, 15619`.

It also verifies the global identity

`sum_i W_i=E_1+2E_2+3E_3=86845`,

with

`E_1=2556, E_2=36830, E_3=3543`.

The weak-`L^2` distribution constants used in Lemma 3.1 are checked symbolically from the exact sublevel formulas; the universal choice `B=4` is valid for both signs. The numeric constants in (4.3) and (4.7) are

`16*3^(-1/4)=12.1573709704...`,
`4*sqrt(25.46)=20.1831612985...`.

These are algebraic/numerical checks of the proof, not Monte Carlo evidence for the conjecture.

## 7. First unpaid implication

The first unpaid B07 implication is now

`QFORM-SHARED3-AGGREGATE-PIVOT-TRANSDUCER-v1`:

> Starting from a constant non-disjoint third-compound overlap bank, use the exact ledger (2.9) without selecting one dimension-dependent pivot. Either aggregate the exact-zero terms by the zero-self random-shift/product mechanisms, or aggregate the nonzero terms `A_ii^2 M_2(S_i)` into one of the completed Schur S0/S1/S2 payments. In the tiny-pivot subbranch, exploit Theorem 3.2 to pay every state whose exact inner Schur remainder has two reciprocal-scale diffuse eigenvalues or a reciprocal-scale zero-self row; reduce the survivor to the one-huge-direction/high-leverage chamber.

The disjoint third-compound O0 route and the previously isolated edge-times-bank sibling remain separate obligations. A full solution still requires all overlap classes, all signs, degenerate cases, arbitrary extra spectrum, and two independent end-to-end reviews.

## 8. Status

- `QFORM-SHARED3-SCALAR-SCHUR-COMPOUND-v1`: **PROVED**.
- exact global ledger (2.9): **PROVED**.
- `QFORM-SQUARE-HALFRIESZ-QUARTERROOT-v1`: **PROVED**.
- reciprocal-scale zero-self/two-eigen tiny-pivot exits: **PROVED CONDITIONAL BRANCHES** at the stated source scopes.
- full QFORM density theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- full continuity conclusion: **OPEN**.
- no scheduler, notification, email, public-release, paid-model/API/Codex, or cross-account native state is changed by this report.
