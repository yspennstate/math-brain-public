Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — four-pair horizontal free block survives complete replacement

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; universal T09 remains OPEN.** The finite arithmetic certificate in §5 was actually executed in this run using outward-rounded integer interval arithmetic. No independent review has occurred. Exact worldwide priority is **UNVERIFIED**.

## 1. Parent target and compact handoff

The parent Benjamini--Schramm target is:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`. `POSTED.md` does not close T09. The latest own substantive report is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T18-52-00+0300__t09-two-horizontal-pair-replacement-gap.md`.

That predecessor proved arbitrary replacement of **two** standard horizontal inverse pairs on a `(12,8)` BMW marking, with

`p_c<3/40<19/250<p_u`.

It also identified the obstruction for arbitrary replacement of three pairs: if all replacement edges are ignored on the critical side, the retained degree-14 graph cannot beat the elementary lower barrier `1/13`, while the crude scalar uniqueness floor is only about `0.06921`.

Preserved earlier Benjamini--Schramm attempts are the finite-set escape/BK-last-exit route, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW, scalar nonbacktracking polynomials, quotient/fibre-shell and bridge criteria, followed by the September free-core, triangle-fibre, S-arithmetic, product-lattice, Rattaggi augmentation, power-layer, factor-branching, pure-torsion and multiseed-fibre constructions. Auxiliary inequalities without a completed `p_c`-to-`p_u` transfer remain mechanism history rather than source-level results.

The neighboring PROB10-09/R20 work remains in its quotient/extension/vertical-subgroup lane and explicitly leaves the Rattaggi/BMW product-fibre lane to NM13-11; no peer file is overwritten here.

## 2. Original-problem before/after scope

Let `Gamma` be a BMW group acting simply transitively on `T_12 x T_8`. Write the standard marking as

`S_0=A sqcup B`,

where `A={a_1^{+-1},...,a_6^{+-1}}` is the horizontal marking and `B` is the symmetric eight-element vertical marking. The horizontal subgroup

`H=<a_1,...,a_6> ~= F_6`

is free of rank six, and words in `H` preserve geometric horizontal fibres.

### Before

The strongest replacement theorem on this lane allowed any two standard horizontal inverse pairs to be deleted and replaced by two arbitrary inverse pairs. No theorem on this track allowed all six standard horizontal pairs to disappear from the marking.

### After: main restricted theorem

> **Theorem A (four horizontal free pairs plus two arbitrary pairs).**
> Let
> 
> `C={c_1^{+-1},...,c_6^{+-1}}`
> 
> be any symmetric twelve-element set such that `S=B sqcup C` is simple and generates `Gamma`. Assume only that `c_1,...,c_4` lie in the standard horizontal subgroup `H` and freely generate a free group of rank four. There is **no condition** on `c_5,c_6` beyond simplicity/generation of the final marking. Then for
> 
> `G=Cay(Gamma,S)`
> 
> we have
> 
> `boxed( p_c(G) < 7/100 < 19/250 < p_u(G) )`
> 
> and therefore
> 
> `boxed( p_u(G)-p_c(G) > 3/500 = 0.006 ).`

This allows **complete replacement of all six standard horizontal inverse pairs**. Only four of the six new pairs need to form a free horizontal block; the final two pairs may have arbitrary relations, may lie outside the horizontal subgroup, and may interact arbitrarily with every other generator.

A concrete all-new horizontal replacement exists by Nielsen moves. Starting from the free basis `(a_1,...,a_6)`, successively replace

`a_1 -> a_1 a_2`,
`a_2 -> a_2 a_3`,
`a_3 -> a_3 a_4`,
`a_4 -> a_4 a_5`,
`a_5 -> a_5 a_6`,
`a_6 -> a_6 (a_1 a_2)`.

The resulting six words form a free basis of `H`, none is an original basis element, and the first four freely generate `F_4`. Thus Theorem A contains fixed Cayley graphs in which **every standard horizontal pair is replaced**.

**Original-problem delta:** universal T09 remains OPEN. The source-level fixed-graph scope expands from two-pair arbitrary horizontal replacement to complete horizontal replacement under a four-pair horizontal free-block hypothesis, with explicit gap `>0.006`.

## 3. Large three-pair replacement corollary: only one structured replacement

The hypothesis is much weaker in the first unresolved case from the predecessor.

Delete the three standard pairs `a_4^{+-1},a_5^{+-1},a_6^{+-1}` and retain `a_1^{+-1},a_2^{+-1},a_3^{+-1}`. Since

`F_6=<a_1,a_2,a_3> * <a_4,a_5,a_6>`, 

any nontrivial

`c in <a_4,a_5,a_6>`

has infinite order and satisfies

`<a_1,a_2,a_3,c> = <a_1,a_2,a_3> * <c> ~= F_4`.

Hence:

> **Corollary B (three-pair replacement with one complementary word).**
> Replace the three deleted standard pairs by `c^{+-1},d^{+-1},e^{+-1}`, where `c` is **any nontrivial word** in the deleted free factor `<a_4,a_5,a_6>` and `d,e` are completely arbitrary, subject only to the final symmetric set being simple and generating. Then the same
> 
> `p_c<7/100<19/250<p_u`
> 
> and gap `>3/500` hold.

Thus the old arbitrary-three-pair case is still UNKNOWN, but a large genuinely new three-pair replacement class now needs structure on only **one** of the three replacement pairs.

## 4. Percolation mechanism: depth-seven two-seed branching in an `8`-regular horizontal forest

Use only the four-pair block

`K={c_1^{+-1},...,c_4^{+-1}}`

and the standard vertical edges `B`; ignore `c_5,c_6` on the critical side. Since `c_1,...,c_4` freely generate `F_4` and lie in `H`, the `K`-edge graph inside every geometric horizontal fibre is an `8`-regular forest, each component a copy of `T_8`.

Root the geometric vertical `T_8`. Put `p=7/100` and `s=1-p`. For a depth parameter `R`, define the forward-tree pgf

`h_0(x)=x`,
`h_{r+1}(x)=x (s+p h_r(x))^7`.

For a type-1 particle (one seed in a fresh horizontal fibre), expose the radius-`R` open cluster in its `T_8` component. Its size pgf is

`F_{1,R}(x)=x (s+p h_{R-1}(x))^8`.

For a type-2 particle with two distinct seeds in a fresh fibre, choose two disjoint rooted `7`-ary outward cones. If the seeds lie in the same `T_8` component, delete at each seed the first edge on the geodesic joining them. If they lie in different components, delete any one incident edge at each root. The two depth-`R` cluster sizes are independent, so

`F_{2,R}(x)=h_R(x)^2`.

For `i=1,2`, define

`q_{i1}=p F_{i,R}'(s)`,
`q_{i2}=1-F_{i,R}(s)-pF_{i,R}'(s)`.

For each of the seven forward geometric vertical fibres, test all standard vertical edges from active vertices. Conditional on an active set of size `n`, the number of open crossing edges is `Bin(n,p)`: exactly one crossing creates a type-1 child, while two or more crossings create a type-2 child by retaining any two distinct endpoints. Hence the mean matrix is

`M_R(p)=7 [[q_11,q_12],[q_21,q_22]].`

Distinct parent particles live in distinct rooted vertical fibres, and the horizontal plus crossing edge sets used by different particles are disjoint. Thus this is an honest two-type Galton--Watson subprocess. If `rho(M_R)>1`, survival gives an infinite open cluster. Since every entry is a finite polynomial in `p`, strict supercriticality persists below the displayed parameter, giving `p_c<p`.

Take `R=7`. The exact outward-rounded checker in §5 certifies, writing

`M_7(7/100)=[[A,B],[C,D]]`,

that

`A>8535/10000`,
`B>8007/100000`,
`C>1418/1000`,
`D>2309/10000`.

Therefore

`BC-(1-A)(1-D) > 86611/100000000 >0`,

so

`det(I-M_7)<0`.

A nonnegative `2x2` matrix has its Perron eigenvalue above `1` whenever `det(I-M)<0` and the second eigenvalue lies below `1`; equivalently here, because the characteristic polynomial at `1` is negative while the Perron root is the larger real eigenvalue, `rho(M_7)>1`. Consequently

`boxed(p_c(G)<7/100).`

This improves the predecessor's one-seed `3/40=0.075` certificate to `0.07` and is essential to the larger replacement scope.

## 5. Uniqueness side and actually executed exact checker

The four-pair horizontal free block has exact regular-representation norm

`||A_K||=2 sqrt(7)`.

The standard vertical block is also a free rank-four block and has exact norm `2 sqrt(7)`. Each of the two arbitrary remaining inverse pairs costs at most `2` by unitarity. Hence

`||A_G|| <= 4 sqrt(7)+4 < 175/12`,

using `sqrt(7)<127/48`.

The graph is `D=20` regular, so `Q=D-1=19`. Set

`z=250/19`.

Exactly,

`z^2-19 = 55641/361 >0`,

and

`z+19/z-175/12 = 529/28500 >0`.

The standard regular nonbacktracking recurrence therefore has `ell^2` growth exponent strictly below `z`. The shortest-open-path bound gives

`p_{2->2}(G)>1/z=19/250`.

Uniqueness plus FKG gives `p_{2->2}<=p_u`, so

`boxed(p_u(G)>19/250).`

Combining with the critical estimate gives the gap `3/500`.

### Executed checker source

The following code was actually executed in this run. It uses scale-`10^30` integer intervals with outward rounding, so every displayed interval/bound is rigorous rather than floating-point evidence.

```python
from fractions import Fraction

SCALE = 10**30

def iconst(n, d=1):
    return ((n*SCALE)//d, (n*SCALE + d - 1)//d)
def iadd(a, b): return (a[0]+b[0], a[1]+b[1])
def isub(a, b): return (a[0]-b[1], a[1]-b[0])
def imul(a, b):
    return ((a[0]*b[0])//SCALE,
            (a[1]*b[1] + SCALE - 1)//SCALE)
def ismul(k, a): return (k*a[0], k*a[1])
def ipow(a, n):
    r = iconst(1)
    for _ in range(n):
        r = imul(r, a)
    return r

def dec_lo(a): return a[0] / SCALE
def dec_hi(a): return a[1] / SCALE

p = iconst(7,100)
s = iconst(93,100)
x = s
R = 7
h = [x]
dh = [iconst(1)]

for _ in range(R):
    q = iadd(s, imul(p, h[-1]))
    h_next = imul(x, ipow(q, 7))
    dh_next = iadd(
        ipow(q, 7),
        imul(imul(imul(x, iconst(7)), ipow(q,6)), imul(p, dh[-1]))
    )
    h.append(h_next)
    dh.append(dh_next)

q = iadd(s, imul(p, h[R-1]))
F1 = imul(x, ipow(q,8))
dF1 = iadd(
    ipow(q,8),
    imul(imul(imul(x, iconst(8)), ipow(q,7)), imul(p, dh[R-1]))
)
F2 = ipow(h[R],2)
dF2 = ismul(2, imul(h[R], dh[R]))

one = iconst(1)
q11 = imul(p, dF1)
q12 = isub(isub(one, F1), q11)
q21 = imul(p, dF2)
q22 = isub(isub(one, F2), q21)
A,B,C,D = [ismul(7,qv) for qv in (q11,q12,q21,q22)]

bounds = (
    Fraction(8535,10000),
    Fraction(8007,100000),
    Fraction(1418,1000),
    Fraction(2309,10000),
)
entries = (A,B,C,D)
passes = []
for I,b in zip(entries,bounds):
    passes.append(I[0] * b.denominator > b.numerator * SCALE)

margin = bounds[1]*bounds[2] - (1-bounds[0])*(1-bounds[3])
z = Fraction(250,19)
z2_margin = z*z - 19
root_margin = z + Fraction(19,1)/z - Fraction(175,12)
gap = Fraction(19,250) - Fraction(7,100)

print("A interval:", f"[{dec_lo(A):.15f}, {dec_hi(A):.15f}]")
print("B interval:", f"[{dec_lo(B):.15f}, {dec_hi(B):.15f}]")
print("C interval:", f"[{dec_lo(C):.15f}, {dec_hi(C):.15f}]")
print("D interval:", f"[{dec_lo(D):.15f}, {dec_hi(D):.15f}]")
print("entry lower-bound checks:", passes)
print("BC-(1-A)(1-D) certified >", margin, "=", float(margin))
print("z^2-19 =", z2_margin)
print("z+19/z-175/12 =", root_margin)
print("gap =", gap, "=", float(gap))
print("ALL_EXACT_INTERVAL_CHECKS_PASS")
```

Actual output:

```text
A interval: [0.853588349640864, 0.853588349640864]
B interval: [0.080075407943044, 0.080075407943044]
C interval: [1.418271909778968, 1.418271909778968]
D interval: [0.230930231863916, 0.230930231863916]
entry lower-bound checks: [True, True, True, True]
BC-(1-A)(1-D) certified > 86611/100000000 = 0.00086611
z^2-19 = 55641/361
z+19/z-175/12 = 529/28500
gap = 3/500 = 0.006
ALL_EXACT_INTERVAL_CHECKS_PASS
```

## 6. General mechanism / weakened hypotheses

The proof does not use the six-pair replacement language itself. It proves the following reusable criterion.

Let a simply transitive product-of-trees group have all `e` standard vertical labels retained. Suppose the final Cayley marking contains a fibre-preserving block of `r` inverse generator pairs freely generating `F_r`, plus `a` additional arbitrary inverse pairs. Then:

1. inside each horizontal fibre the structured block is a disjoint union of `T_{2r}` components;
2. the two-seed finite-depth matrix with fibre degree `2r` and crossing degree `e` gives a genuine upper bound on `p_c`;
3. the adjacency norm satisfies

`||A|| <= 2 sqrt(2r-1)+2 sqrt(e-1)+2a`;

4. any nonbacktracking root-test point above the critical certificate gives a strict `p_c<p_u` gap.

For `(r,e,a)=(4,8,2)`, radius seven and `p=7/100` give Theorem A.

Thus the extra hypothesis is weakened in three directions simultaneously:

- no standard horizontal generator need remain at all;
- the free block may be any four fibre-preserving marked generators, not a subset of the original basis;
- only four of the six nonvertical pairs are structured; the other two are completely arbitrary.

Corollary B further shows that for three-pair replacement, the structured requirement can be reduced to a **single nontrivial word in the deleted complementary free factor**.

## 7. Exact current source scopes, refreshed 20 September 2026

These were rechecked against the live arXiv records in this run.

### Hutchcroft, arXiv:1804.10191

Current version is **v3, 26 March 2019**. The submission history says v3 changed metadata for bureaucratic reasons and made no textual change. Theorem 1.3 proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive** graphs.

Source: https://arxiv.org/abs/1804.10191

The Rattaggi/BMW ambient geometry is a product of two unbounded trees, not Gromov hyperbolic, so this theorem does not cover the present class.

### Hutchcroft--Pan, arXiv:2409.12283

Current version is still **v1, 18 September 2024**. The paper studies percolation **at `p_u`** via subgroup relativization. Its abstract proves nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and proves a co-heredity property for a strong form of nonuniqueness at `p_u`. The body contains broader obstacle-to-uniqueness statements recorded in earlier reports, but these are endpoint results rather than a strict quantitative fixed-graph `p_c<p_u` transfer.

Source: https://arxiv.org/abs/2409.12283

### Terlov--Timár, arXiv:2502.02560

Current version is **v2, 14 September 2025**. It develops weighted/level amenability for nonunimodular transitive graphs and proves a relaxed Pak--Smirnova-Nagnibeda-style version of a weighted `p_h<p_u` conjecture, where `p_h` is the threshold for clusters of infinite total weight. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` theorem.

Source: https://arxiv.org/abs/2502.02560

### Other checked coverage relevant to novelty classification

Choi--Seo, arXiv:2508.08932, prove `p_c<p_u` for every Cayley graph of every acylindrically hyperbolic group. The retained finite-index-simple/SQ-universality argument from earlier NM13-11 reports excludes Rattaggi's ambient group from that all-Cayley class.

Hutchcroft's 2022 `L^2`-boundedness theory applies in particular to transitive graphs with normalized spectral radius `<1/2`. The only uniform norm information used here gives

`rho <= (4 sqrt(7)+4)/20 approx 0.72915`,

so that sufficient corollary does **not** cover this replacement class uniformly. This does not assert that every individual member has spectral radius at least `1/2`.

A bounded current search did not locate a theorem specifically covering the complete-horizontal-replacement class above. This is not an exhaustive worldwide priority certificate; external priority remains **UNVERIFIED**.

## 8. Residual obstruction and next attack

The current architecture needs a four-pair structured horizontal block. If only three fibre-preserving free pairs are available and the remaining three pairs are arbitrary, then ignoring those arbitrary pairs on the critical side leaves a degree-14 subgraph. Any such comparison has the universal barrier

`p_c >= 1/13 = 0.076923...`,

while the crude uniqueness-side norm

`2 sqrt(5)+2 sqrt(7)+6`

gives a scalar nonbacktracking floor only about

`p_u >= 0.0692107...`.

Thus merely increasing finite depth cannot reduce the structured block from four free pairs to three. To advance again, at least one of the three arbitrary pairs must participate in a collision-controlled critical branching process, or its position/relation must be exploited on the uniqueness side. The fully arbitrary three-pair replacement problem remains **UNKNOWN**, not negative.

## 9. ledger_delta

```yaml
ledger_delta:
  task: T09
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_metric_before: "arbitrary replacement of at most two standard horizontal inverse pairs on the fixed (12,8) BMW marking; pc<3/40<19/250<pu"
  source_metric_after: "complete replacement of all six standard horizontal pairs allowed whenever four final pairs are fibre-preserving and freely generate F4; other two pairs arbitrary: pc<7/100<19/250<pu, gap>3/500"
  three_pair_corollary: "after deleting a4,a5,a6, one replacement may be any nontrivial word in <a4,a5,a6>; the other two replacement pairs are arbitrary, subject to final simplicity/generation; same gap >3/500"
  mechanism_advance: "depth-seven two-seed Galton-Watson process on an 8-regular horizontal forest plus exact free-block/vertical operator norms; complete percolation transfer"
  exact_check: "PASS; outward-rounded scale-10^30 integer interval arithmetic; output ends ALL_EXACT_INTERVAL_CHECKS_PASS"
  preserved_history: "finite-set escape/BK, killed-SAW/boundary energy, global l2-SAW, scalar NB, quotient/fibre-shell, bridge, free-core, triangle, power-layer, factor-branching, multiseed routes preserved without promoting incomplete transfers"
  candidate_status: CANDIDATE_FULL_RESTRICTED
  universal_closure: false
  external_priority: UNVERIFIED
  next_obstruction: "only three structured free horizontal pairs plus three arbitrary pairs; base-only critical barrier exceeds crude uniqueness floor"
```
