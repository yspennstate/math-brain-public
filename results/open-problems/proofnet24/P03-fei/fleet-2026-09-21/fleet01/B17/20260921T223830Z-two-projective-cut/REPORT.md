# B17 — two-projective-row cut theorem: a logarithmic stability stratum beyond exact factorization

**Status:** PARTIAL / PROVED_AUXILIARY_THEOREM. **Full Friedgut–Kalai Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used.  
**Route:** APPROACH 7/14: enlarge the composition class behind the plaquette-factorization route and obtain a dimension-free coding/isoperimetric inequality on the first nontrivial projective-row stratum.  
**Run:** `20260921T223830Z-b17-fei-r11`.

## 1. Named cross-account result consumed

This run substantively uses fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260921T204329Z-interaction-companion-factorization/REPORT.md`

Git blob `67abacfe5dba4cc84722d12c6b505e9f88304090`.

That report proves that the cross-plaquette weights

\[
p_{ij}=\Pr[f(x)f(x\oplus e_i)f(x\oplus e_j)f(x\oplus e_i\oplus e_j)=-1]
\]

detect exact multiplicative interaction, and that a zero cut is exactly a disjoint multiplicative factorization (up to affine/character factors). The preceding fleet01/B17 run upgraded the zero endpoint to arbitrary-cut linear stability and proposed the open logarithmic strengthening

\[
W_{A|B}:=\sum_{i\in A,j\in B}p_{ij}
\stackrel{?}{\ge}
2\delta_{A|B}\log_2\frac1{\delta_{A|B}},
\]

where \(\delta_{A|B}\) is normalized Hamming distance to a product sign table \(g(A)h(B)\).

The present run does **not** repeat the small-cut enumeration. It proves the logarithmic conjecture on the first genuinely nonlinear stratum beyond exact factorization: cuts having exactly two projective row types.

## 2. Two-projective-row normal form

Let \(A\sqcup B\) be a coordinate cut. Assume that, modulo a row sign, the \(B\)-row of \(f\) takes at most two values. Equivalently there exist Boolean functions

\[
g:\{0,1\}^A\to\{\pm1\},\qquad
c:\{0,1\}^A\to\{0,1\},\qquad
h_0,h_1:\{0,1\}^B\to\{\pm1\}
\]

such that

\[
\boxed{f(x,y)=g(x)h_{c(x)}(y).}
\tag{2.1}
\]

This class is strictly larger than exact multiplicative factorization: both projective row types may occur and the selector \(c\) may be an arbitrary Boolean function of all \(A\)-variables, sharing them with the arbitrary row sign \(g\).

Put

\[
\alpha=\min\{\Pr[c=0],\Pr[c=1]\}\le \frac12.
\]

After possibly replacing \(h_1\) by \(-h_1\) and absorbing the sign into the corresponding values of \(g\), define

\[
d=\Pr[h_0(Y)\ne h_1(Y)]\le\frac12.
\]

Thus \(d\) is the projective Hamming distance between the two row types.

## 3. Exact product distance

### Theorem 3.1

For every function of the form (2.1),

\[
\boxed{\delta_{A|B}(f)=\alpha d.}
\tag{3.1}
\]

### Proof

A product approximant \(u(x)v(y)\) may choose the sign \(u(x)\) separately for every row. Hence, after quotienting by row signs,

\[
\delta_{A|B}(f)
=
\inf_{[v]}
\Big((1-\alpha)d_{\rm proj}(h_0,v)+
\alpha d_{\rm proj}(h_1,v)\Big),
\]

where \(d_{\rm proj}(r,s)=\min(\Pr[r\ne s],\Pr[r=s])\).

The choice \(v=h_0\) gives \(\delta\le\alpha d\). Conversely, for every projective row \(v\), the triangle inequality gives

\[
d_{\rm proj}(h_1,v)\ge d-d_{\rm proj}(h_0,v).
\]

Therefore

\[
(1-\alpha)d(h_0,v)+\alpha d(h_1,v)
\ge
\alpha d+(1-2\alpha)d(h_0,v)
\ge\alpha d.
\]

So equality holds. QED.

## 4. Exact factorization of the physical plaquette cost

Let

\[
s(y)=h_0(y)h_1(y)\in\{\pm1\}.
\]

For \(i\in A\), \(j\in B\), the row sign \(g\) cancels around the \((i,j)\)-plaquette. If \(c(x)=c(x\oplus e_i)\), the plaquette product is \(+1\). If the selector flips across the \(i\)-edge, the plaquette product equals \(s(y)s(y\oplus e_j)\). Since the \(x\)- and \(y\)-events are independent under the uniform product measure,

\[
\boxed{
p_{ij}=\operatorname{Inf}_i(c)\operatorname{Inf}_j(s).
}
\tag{4.1}
\]

Summing gives the exact identity

\[
\boxed{
W_{A|B}(f)=I(c)\,I(s).
}
\tag{4.2}
\]

This is the new use of the fleet02/B17 physical interaction detector: on the two-projective-row stratum, the entire cross-interaction bank splits into the selector boundary times the branch-separation boundary.

## 5. PROVED: the open all-cut logarithmic inequality on this stratum

Cube edge-isoperimetry applied to \(c\) and to the folded disagreement set of \(s\) gives

\[
I(c)\ge2\alpha\log_2\frac1\alpha,
\qquad
I(s)\ge2d\log_2\frac1d.
\]

Combining with (4.2),

\[
\boxed{
W_{A|B}(f)
\ge
4\alpha d
\log_2\frac1\alpha
\log_2\frac1d.
}
\tag{5.1}
\]

Using \(\delta=\alpha d\), put
\(r=\log_2(1/\alpha)\ge1\) and
\(t=\log_2(1/d)\ge1\).
Since \(2rt\ge r+t\),

\[
4\delta rt
\ge
2\delta(r+t)
=
2\delta\log_2\frac1\delta.
\]

Hence:

### Theorem 5.1 — two-projective-row logarithmic cut stability

\[
\boxed{
W_{A|B}(f)
\ge
2\delta_{A|B}(f)
\log_2\frac1{\delta_{A|B}(f)}
}
\tag{5.2}
\]

for every Boolean \(f\) whose projective \(B\)-rows take at most two values.

This proves the preceding B17 all-cut logarithmic conjecture on a nontrivial infinite-dimensional class, with the conjectured constant \(2\).

The stronger multiplicative estimate (5.1) records why the logarithm appears twice: once for the rarity of the selector branch in \(A\), and once for the rarity of the projective difference between the two branch functions in \(B\).

## 6. Sharpness and exact Boolean examples

The constant \(2\) in (5.2) is already sharp inside this class. Take \(c\) to be a dictator on one \(A\)-bit and \(h_0/h_1\) to differ by a dictator on one \(B\)-bit. Then

\[
\alpha=d=\frac12,\qquad
\delta=\frac14,\qquad
W=1,
\]

and therefore

\[
W=
2\delta\log_2(1/\delta)=1.
\]

More generally, if the minority selector event is a codimension-\(r\) subcube and the branch-disagreement event is a codimension-\(t\) subcube, then

\[
\alpha=2^{-r},\quad d=2^{-t},\quad
\delta=2^{-(r+t)},\quad
W=4rt\,\delta.
\]

The ratio to the conjectured lower bound is

\[
\frac{W}{2\delta\log_2(1/\delta)}
=
\frac{2rt}{r+t}\ge1,
\]

with equality at \(r=t=1\).

## 7. Executed stress test

A fresh checker independently:

1. exhausts all \(4{,}096\) triples \((c,h_0,h_1)\) for a \(2+2\) cut;
2. computes the true distance to **all** rank-one product sign tables, not merely the formula \(\alpha d\);
3. computes every cross plaquette directly from the truth table;
4. verifies both exact identities
   \[
   \delta=\alpha d,\qquad W=I(c)I(s);
   \]
5. verifies the strong product bound (5.1) and the logarithmic cut bound (5.2);
6. repeats the exact-distance/direct-plaquette comparison on 512 deterministic seeded \(3+3\) examples.

Output:

```text
B17 two-projective-row cut checker
full_FEI=OPEN_NOT_PROVED
exhaustive_2x2_cases 4096
max_formula_error 0
min_open_cut_slack 0
min_strong_product_slack 0
equality_witness (3, 0, 3, (0.5, 0.5, 1.0, 1.0, 0.25, 1.0, 1.0, 1.0))
seeded_3x3_cases 512
seeded_max_formula_error 0
seeded_min_open_cut_slack 0.25
seeded_min_strong_product_slack 0
PASS
```

Checker SHA-256:
`514c90446b9b82dbbe57ff3e53d8b1633b514733ef21bb256286aa4248b96228`.

Captured output SHA-256:
`75ba34de83f2703e11d38bf146af44937f05aa4ace87a3776c16abd0a264d82a`.

The finite checks are regression evidence only; the theorem is analytic.

## 8. What this changes and what remains open

The exact-factorization endpoint from fleet02/B17 is the **one-projective-row** case. This run proves the correct logarithmic stability law on the entire **two-projective-row** stratum. Thus the next obstruction to the projective coding route is not binary branching itself; it is genuinely multi-projective row geometry.

A natural next target is a hierarchical version: if the projective row map factors through a binary tree of row types, try to decompose the total plaquette cost into nonreused binary edge costs and sum (5.1) along the tree. If that can be done without paying an ambient number of row types, it gives exactly the kind of dimension-free description-length theorem required by APPROACH 14.

A tempting but currently **unproved** extension is that every finite projective-row family admits such a binary tree with total weighted binary cut cost at most the original \(W_{A|B}\). This is the next place to stress-test; no claim is made here.

The full FEI conjecture remains **OPEN / NOT PROVED**.
