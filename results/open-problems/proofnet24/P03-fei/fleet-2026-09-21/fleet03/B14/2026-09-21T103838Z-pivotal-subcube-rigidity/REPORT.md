# B14 — pivotal-subcube rigidity at the erasure-selector endpoint

**Run:** 2026-09-21, fleet03/B14  
**Role:** FEI erasure and selector proof  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Target:** full uniform-cube Fourier entropy-influence conjecture. **OPEN / NOT PROVED.**  
**New result status:** the structural theorem below is **PROVED for its stated class**. It is not full FEI. Publication priority is **UNVERIFIED**.

## 1. Exact route attempted

The live restriction-critical reduction says that any counterexample to `H <= C I` can be replaced by a physical restriction descendant `g` maximizing `r=H/I` among its descendants and satisfying

\[
\Delta_iH(g)\ge r(g)\alpha_i(g)
\]

for every relevant coordinate. The exact erasure decomposition is

\[
\Delta_iH=B_i+JS_i,
\qquad
B_i=H(X_i\mid X_{-i}),
\]

with `JS_i <= B_i` and `JS_i <= (2/ln 2) min(alpha_i,1-alpha_i)`. The compatible fleet04/B14 run translated this into signed-overlap and logarithmic-surprise constraints on every coordinate of the same critical core.

This run tried a different endpoint: the hereditary payment theorem from 20 September bounds erasure by the physical boundary of the pivotal set. Let

\[
P_i(x_{-i})={\bf 1}\{g(+1,x_{-i})\ne g(-1,x_{-i})\},
\qquad \mathbb E P_i=\alpha_i.
\]

The existing exact bound is

\[
B_i(g)\le \frac12 I(P_i)+\frac{\alpha_i}{\ln2}
\tag{1}
\]

when `alpha_i <= 1/2` (equivalently this is the multiplicative-derivative curvature bound). The cube edge-isoperimetric inequality gives

\[
I(P_i)\ge 2\alpha_i\log_2(1/\alpha_i).
\tag{2}
\]

The creative question was: **what does exact equality at the isoperimetric endpoint force simultaneously for all pivotal sets?** If the equality structure is rigid enough, one can then ask for a stability theorem around that endpoint rather than another false every-coordinate payment.

## 2. Two-face compatibility identity

For distinct physical coordinates `i,j`, define

\[
\eta_{ij}:=\operatorname{Inf}_j(P_i).
\]

On a fixed two-dimensional `i,j` face, `P_i` changes across `j` exactly when the product of the four Boolean values on that face is `-1`. The same condition is obtained after swapping `i` and `j`. Therefore

\[
\boxed{\eta_{ij}=\eta_{ji}.}
\tag{3}
\]

This is pointwise on the residual cube, not merely an equality after averaging.

There is also an exact physical/spectral second-moment identity. If

\[
\beta_{ij}:=\Pr_{S\sim \widehat g^2}[i,j\in S]
=\sum_{S\supseteq\{i,j\}}\widehat g(S)^2,
\]

and `s_i(x)` is the indicator that coordinate `i` is sensitive at `x`, then

\[
\boxed{\beta_{ij}=\mathbb E_x[s_i(x)s_j(x)].}
\tag{4}
\]

Indeed

\[
\beta_{ij}=rac14\left(1-\mathbb E gg^{(i)}-\mathbb E gg^{(j)}+\mathbb E gg^{(ij)}\right),
\]

while expanding `E[s_i s_j]` gives the same expression because
`E[g^{(i)}g^{(j)}]=E[gg^{(ij)}]` by translation invariance. Consequently

\[
\mathbb E|S|(|S|-1)=\mathbb E_x s(x)(s(x)-1).
\tag{5}
\]

On each two-face, the Boolean table is either affine (one two-bit Fourier coefficient has magnitude one) or nonlinear (all four have magnitude `1/2`). Hence

\[
\beta_{ij}=q_{ij}+\frac14\eta_{ij}\ge\frac14\eta_{ij},
\tag{6}
\]

where `q_ij` is the probability of an affine two-face whose active character contains both `i` and `j`. This recovers the familiar inequality between pivotal-set curvature and the conditional spectral degree, but (3) is the compatibility fact used below.

## 3. Main theorem: subcube pivotal sets force a product of one-point blocks

### Theorem 3.1 — pivotal-subcube rigidity

Let `f:{0,1}^n->{-1,1}` be Boolean. Suppose that for every relevant coordinate `i`, its pivotal set

\[
A_i:=\{x_{-i}:f(0,x_{-i})\ne f(1,x_{-i})\}
\]

is a subcube of the residual `(n-1)`-cube. Then, after deleting irrelevant variables, there is a partition of the relevant coordinates into disjoint blocks

\[
C_1\sqcup\cdots\sqcup C_m
\]

and one-point Boolean functions `h_a` on `C_a` such that

\[
\boxed{f(x)=\pm\prod_{a=1}^m h_a(x_{C_a}).}
\tag{7}
\]

Here a one-point function is constant except at one input of its block, where its sign is flipped. A one-variable block is therefore just a signed character.

In particular this entire all-dimensional class satisfies

\[
\boxed{H(f)\le4 I(f).}
\tag{8}
\]

Thus a full-FEI counterexample above any coefficient `C>4` cannot lie at the simultaneous exact subcube endpoint of the pivotal-set isoperimetric problem.

### Proof

For relevant `i`, write the subcube condition as

\[
P_i(x_{-i})=1
\quad\Longleftrightarrow\quad
x_k=b_{ik}\text{ for every }k\in N_i,
\tag{9}
\]

where `N_i subset [n]\{i}` is the set of fixed coordinates. Then

\[
\alpha_i=2^{-|N_i|}.
\tag{10}
\]

For `j != i`, the boundary of this subcube in direction `j` is empty if `j notin N_i`, while if `j in N_i` it is the residual subcube obtained by dropping the one constraint on `j`. Therefore

\[
\eta_{ij}=\operatorname{Inf}_j(P_i)
=\begin{cases}
0,&j\notin N_i,\\
2\alpha_i,&j\in N_i.
\end{cases}
\tag{11}
\]

By the exact symmetry (3), `j in N_i` iff `i in N_j`; moreover on an adjacent pair `2 alpha_i=2 alpha_j`, hence `|N_i|=|N_j|`.

More is true. When `j in N_i`, the event that the `i,j` face is nonlinear is exactly

\[
x_k=b_{ik}\quad(k\in N_i\setminus\{j\}).
\tag{12}
\]

Writing the same event from the `j` side gives the identical subset of the residual `(n-2)`-cube, so equality of subcubes yields

\[
N_i\setminus\{j\}=N_j\setminus\{i\},
\tag{13}
\]

with the same fixed values on all common coordinates.

Create a graph on relevant coordinates by joining `i` to `j` when `j in N_i`. It is undirected by (3). Equation (13) shows that two neighbors of a vertex are neighbors of each other: if `j,k in N_i`, then `k in N_i\{j}=N_j\{i}`. Hence every connected component is a clique. For a component `C`,

\[
N_i=C\setminus\{i\}\qquad(i\in C).
\tag{14}
\]

The equality of the residual subcubes in (12) also makes the fixed bit attached to a coordinate independent of which other member is used to read it. Thus there is one center `b^C in {0,1}^C` for which

\[
P_i=1\quad\Longleftrightarrow\quad
x_{C\setminus\{i\}}=b^C_{C\setminus\{i\}}
\qquad(i\in C).
\tag{15}
\]

Fix all coordinates outside `C`. Inside the `C`-cube, (15) says that the sensitive edges are exactly the edges incident to the single vertex `b^C`. Removing those edges leaves `b^C` isolated and all other vertices connected (the one-variable case is immediate). Therefore the restricted Boolean function is constant on all vertices except `b^C`, where it has the opposite sign. Its overall sign may depend on the outside assignment, so

\[
f(x_C,z)=h_C(x_C)\sigma(z)
\tag{16}
\]

for a fixed one-point function `h_C`. Multiplication by the nonzero factor `h_C` does not change whether an outside coordinate is sensitive. Repeating component by component gives the factorization (7).

It remains only to bound one block. For a one-point function on `k` variables, let `N=2^k`. Up to signs and input translation its squared Fourier law is

\[
p_\varnothing=(1-2/N)^2,
\qquad p_S=4/N^2\quad(S\ne\varnothing),
\tag{17}
\]

and

\[
I=\frac{2k}{N}.
\tag{18}
\]

For `k>=2`,

\[
\begin{aligned}
H
&=p_\varnothing\log_2(1/p_\varnothing)
 +(N-1)\frac4{N^2}(2k-2)\\
&\le \frac{4}{N\ln2}+\frac{8(k-1)}N
\le\frac{8k}{N}=4I,
\end{aligned}
\tag{19}
\]

using `-p ln p <= 1-p` and `1-p_empty<=4/N`. The `k=1` block is a character and has zero Fourier entropy. Fourier laws tensorize under products on disjoint variables, so both `H` and `I` add over the blocks. Equation (8) follows. QED.

### Relation to edge isoperimetry

For an indicator of density `alpha`, cube edge isoperimetry gives `I(P)>=2 alpha log_2(1/alpha)`. A subcube of codimension `k` has `alpha=2^{-k}` and equality. Thus Theorem 3.1 completely identifies the simultaneous **subcube/equality endpoint** relevant to the present route. No quantitative stability theorem is claimed here.

## 4. Attempted refutation / finite check

The theorem was attacked by exhaustive enumeration only as a targeted sanity check, not as its proof and not as an FEI sweep. `check_pivotal_subcube.py` enumerates all Boolean functions through four variables, filters exactly those for which every pivotal set is a subcube, and then checks the clique decomposition and product-of-one-point factorization.

The executed output was:

| n | accepted functions | classification failures | max H/I in accepted class |
|---|---:|---:|---:|
| 1 | 4 | 0 | 0 |
| 2 | 16 | 0 | 2.0000000000 |
| 3 | 80 | 0 | 2.9558895823 |
| 4 | 480 | 0 | 3.4024755512 |

At `n=4` the component-size patterns were exactly the partitions expected from disjoint clique blocks: empty, `(1)`, `(1,1)`, `(1,1,1)`, `(1,1,1,1)`, `(2)`, `(2,1)`, `(2,1,1)`, `(2,2)`, `(3)`, `(3,1)`, `(4)`. There were zero classification failures. The checker is supporting evidence only; the proof above is all-dimensional.

## 5. Dead route: a uniform stability deficit is false even existentially

A tempting next step would be to hope that every Boolean function has **some** relevant coordinate whose pivotal set is within `O(alpha_i)` of the edge-isoperimetric endpoint, i.e. that for a universal `K`

\[
I(P_i)\le2\alpha_i\log_2(1/\alpha_i)+K\alpha_i.
\tag{20}
\]

This route is **REFUTED** by balanced tribes, where all coordinates are symmetric.

Take `s` disjoint tribes of width `w`, with the function the OR of the `s` width-`w` ANDs. Put `q=1-2^{-w}`. For a coordinate `i`,

\[
\alpha_i=2^{-(w-1)}q^{s-1}.
\tag{21}
\]

Its pivotal indicator requires the other `w-1` variables in its own tribe to be one and every other tribe to be incomplete. Hence a coordinate `j` in the same tribe contributes

\[
\operatorname{Inf}_j(P_i)=2\alpha_i,
\]

while a coordinate in another tribe contributes

\[
2^{-2(w-1)}q^{s-2}.
\]

Therefore

\[
\boxed{
\frac{I(P_i)}{\alpha_i}
=2(w-1)+(s-1)w\frac{2^{-(w-1)}}q.
}
\tag{22}
\]

For balanced tribes, `s ~ (ln 2)2^w`, so

\[
\frac{I(P_i)}{\alpha_i}
=2(1+\ln2)w+O(1),
\qquad
2\log_2(1/\alpha_i)=2w+O(1).
\tag{23}
\]

The normalized excess is therefore `2 ln(2) w+O(1)`, unbounded, and by symmetry there is no better coordinate. Concrete balanced choices `s=round(log(1/2)/log(1-2^{-w}))` give:

| w | s | alpha_i | I(P_i)/alpha_i | 2 log2(1/alpha_i) | excess |
|---:|---:|---:|---:|---:|---:|
| 4 | 11 | 0.0655576 | 11.3333 | 7.86219 | 3.47115 |
| 6 | 44 | 0.0158765 | 18.1905 | 11.9539 | 6.23655 |
| 8 | 177 | 0.00392309 | 25.0431 | 15.9876 | 9.05555 |
| 10 | 709 | 0.000977934 | 31.8416 | 19.9960 | 11.8457 |
| 12 | 2839 | 0.000244187 | 38.6330 | 23.9994 | 14.6335 |

So the exact endpoint theorem cannot be extended to full FEI merely by asserting a uniformly bounded pivotal-set isoperimetric deficit. This failure is compatible with the known fact that tribes itself does not threaten FEI: raw pivotal curvature can be huge while the actual erasure/recombination payment remains controlled.

## 6. Consequence for a restriction-critical core

Combining the existing critical-core lower bound

\[
B_i\ge\left(r-\frac2{\ln2}\right)\alpha_i
\]

with (1) gives, for every relevant coordinate of a critical core with `alpha_i<=1/2`,

\[
\boxed{
\frac{I(P_i)}{\alpha_i}
\ge 2\left(r-\frac3{\ln2}\right).
}
\tag{24}
\]

At the Hod-scale calibration `r=6.4547837`, the right side is

\[
4.2533971547\ldots.
\]

But the already-known low-influence bound `alpha_i<0.1805539925` plus edge isoperimetry (2) gives the stronger numerical lower bound

\[
\frac{I(P_i)}{\alpha_i}
>2\log_2(1/0.1805539925)
=4.9389955453\ldots.
\tag{25}
\]

This is a decisive diagnostic: **the raw curvature consequence of erasure-heavy criticality adds no new Hod-scale contradiction beyond the low-influence/isoperimetric information already available.** The small-alpha asymptotics explain why: the sharp scalar restriction cap behaves as `log2(1/alpha)+3/ln2+o(1)`, so (24) meets the edge-isoperimetric scale to first order. The bent-marker obstruction is precisely of this endpoint type.

## 7. Status and next attack

- **PROVED:** simultaneous subcube pivotal sets force a product of disjoint one-point blocks, hence `H<=4I`.
- **PROVED:** the exact two-face compatibility identities (3)--(6).
- **REFUTED:** a universal additive `O(alpha)` stability deficit for the pivotal-set edge boundary, even with an existential coordinate; balanced tribes make the deficit per influence unbounded.
- **OPEN:** full FEI. Nothing here upgrades a structured class or finite check to universal closure.
- **PRESERVED:** the bent-marker counterexample to arbitrary prescribed-coordinate entropy payment and all previously retired absolute-overlap / pointwise-erasure shortcuts.

The next useful B14 attack should therefore be a **stability theorem conditioned on large erasure itself**, not on low influence or pivotal boundary alone. The exact target is to exploit simultaneously

\[
B_i/\alpha_i\text{ large},\qquad
A_iD_i=0,\qquad A_i^2+D_i^2=1,
\]

and the all-translate Fourier orthogonality of the two complementary-support pieces. A promising dichotomy is: either the pivotal sets of an erasure-heavy critical core are quantitatively close to the subcube endpoint, in which case Theorem 3.1 suggests a stable product-of-one-point reduction, or their large isoperimetric excess must create a **spectral-phase rebate** absent from the raw curvature bound (1). Balanced tribes shows that the rebate is essential: boundary excess by itself is not a cost that can be charged to influence.

The run remains `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.
