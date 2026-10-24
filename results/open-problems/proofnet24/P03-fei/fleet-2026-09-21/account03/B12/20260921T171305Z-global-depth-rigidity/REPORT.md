# B12 FEI creative attempt: global zero-depth rigidity and why a quantitative gap is false

**Status:** full uniform-cube Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. The normal `math_brain` import was unavailable in this invocation, so no brain-assisted claim is made.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), using the derivative/sensitivity bridge from #3.  
**Exact universal statement attempted:** characterize the zero set, and then seek a quantitative gap, for the Palm-row depth defect that arose in the sequential compression route.

This run read the live `TASKS_2026-09-21.md`, then the read-once `REPORT.md`, then `APPROACHES.md` before substantive work. It did not re-audit the read-once certificate or repeat an old exhaustive FEI sweep. The immediate input is the current Palm-row handoff: for a Boolean derivative row with influence `j_i<=1/2`,

\[
\Delta_i:=\mathbb E[|S\setminus\{i\}|\mid i\in S]-\frac12\log_2\frac1{j_i}\ge0,
\]

and equality forces the derivative to be a signed indicator of a subcube. The exact slack identity there is

\[
\operatorname{Slack}_{\rm sign,i}+\operatorname{Slack}_{\rm iso,i}=4j_i\Delta_i.
\tag{1}
\]

No literature-priority claim is made here. The point is to push that local equality theorem through the **global compatibility constraints between derivative rows** and then attack the hoped-for quantitative strengthening.

## 1. Setup

Let `f:{-1,1}^n -> {-1,1}` be nonconstant, let

\[
p_A=\widehat f(A)^2,\qquad j_i=\operatorname{Inf}_i(f)=\Pr(i\in S),
\]

where `S` is the spectral sample. Assume every active coordinate satisfies

\[
0<j_i\le\frac12.
\tag{2}
\]

For an active `i`, write

\[
Z_i=|S\setminus\{i\}|\quad\text{conditioned on }i\in S
\]

and define

\[
\Delta_i=\mathbb E Z_i-\frac12\log_2(1/j_i),
\qquad
\mathcal D(f)=\sum_i j_i\Delta_i.
\tag{3}
\]

The imported local equality classification says that `Delta_i=0` iff there is a set `M_i` of

\[
m_i=\log_2(1/j_i)
\]

coordinates such that the derivative `D_i f` is, up to sign, the indicator of a codimension-`m_i` subcube. Equivalently, the Fourier coefficients in row `i` obey

\[
\widehat f(\{i\}\cup A)\ne0\iff A\subseteq M_i,
\qquad
|\widehat f(\{i\}\cup A)|=j_i.
\tag{4}
\]

The new question is what happens when **all** rows simultaneously attain equality.

## 2. PROVED: zero total depth defect globally forces a one-point defect

### Theorem

Under (2), if

\[
\boxed{\mathcal D(f)=0,}
\tag{5}
\]

then, after deleting dummy coordinates and applying cube symmetries and an output sign, `f` is a one-point defect: it is constant except at one vertex.

This is a rigidity theorem for the equality case of the Palm-depth inequality. It is **not** FEI.

### Proof

Because every `Delta_i>=0`, (5) gives `Delta_i=0` on every active coordinate. Hence (4) holds for every active `i`.

#### Step 1: equality rows glue into cliques

If `j in M_i`, then the coefficient `hat f({i,j})` is nonzero. Looking at the same coefficient from row `j` shows `i in M_j`. Moreover (4) gives

\[
|\widehat f(\{i,j\})|=j_i=j_j,
\]

so `m_i=m_j`.

Now take `k in M_i\setminus\{j\}`. The coefficient `hat f({i,j,k})` is nonzero. Viewed from row `j`, this forces both `i,k in M_j`. Therefore

\[
M_i\setminus\{j\}\subseteq M_j\setminus\{i\}.
\]

The sets have the same size, so

\[
\boxed{M_j=(M_i\setminus\{j\})\cup\{i\}.}
\tag{6}
\]

Let `C_i={i}\cup M_i`. Equation (6) says `C_i=C_j` whenever `j in M_i`. Thus the graph on active coordinates with edges `i~j` iff `j in M_i` is a disjoint union of cliques. In addition, every nonempty Fourier support set lies wholly in one clique: if a nonzero coefficient contains `i`, (4) puts every other coordinate of that coefficient in `M_i`.

Consequently the Fourier expansion separates as

\[
f(x)=c+\sum_{C\in\mathcal C} h_C(x_C),
\tag{7}
\]

where the `C` are disjoint active cliques and every `h_C` is mean-zero and nonconstant.

#### Step 2: Booleanity permits only one active clique

Suppose two terms `u(x)` and `v(y)` in disjoint nonempty blocks occur in (7). Since both are nonconstant, choose `x_0,x_1` with `u(x_0)\ne u(x_1)`. The difference

\[
[c+u(x_1)+v(y)]-[c+u(x_0)+v(y)]
\]

is the same nonzero number for every `y`. Because both bracketed quantities belong to `{+1,-1}`, that difference must be `+2` or `-2`; therefore the ordered pair of Boolean outputs is forced to be the same `(-1,+1)` or `(+1,-1)` for every `y`. That makes `v` constant, a contradiction. Hence there is exactly one active clique.

Let its size be `r`. Then for every active `i`,

\[
M_i=C\setminus\{i\},\qquad m_i=r-1,\qquad j_i=2^{-(r-1)}.
\tag{8}
\]

#### Step 3: the active Boolean function has the minimum possible edge boundary

On the `r`-cube, influence `j_i` equals the number of undirected sensitive edges in direction `i`, divided by `2^{r-1}`. By (8), there is therefore exactly **one sensitive edge in each active coordinate direction**. The total edge boundary of either sign class is exactly `r`.

Let `A` be the smaller sign class. For `r>=3`, cube edge isoperimetry gives

\[
|\partial A|\ge |A|\log_2\frac{2^r}{|A|}.
\tag{9}
\]

For every integer `2<=|A|<=2^{r-1}`, the right side is strictly larger than `r`; hence `|A|=1`.

For `r=2`, a two-point minimizer is an edge and its two boundary edges lie in the same coordinate direction, contradicting the already-proved fact that there is exactly one sensitive edge in each direction. Thus `|A|=1` here as well. (`r=1` is excluded by (2), since its unique active influence is one.)

So, after deleting dummies, one sign class consists of a single vertex. This is exactly a one-point defect. QED.

## 3. Attempted strengthening: a positive rigidity gap

The natural next hope was the following quantitative statement.

> **Gap conjecture (attempted, then refuted).** There exists `c_0>0` such that every function satisfying (2) which is not an exact one-point defect after deleting dummies obeys
> \[
> \mathcal D(f)\ge c_0 I(f).
> \tag{10}
> \]

Such a gap would be extremely useful for the sequential proof: every non-extremal row configuration would pay a fixed fraction of influence before any delicate information estimate.

It is false.

## 4. REFUTED: there is no dimension-independent positive gap

Fix `r>=3`. On `r+d` bits let the minority set be

1. the codimension-`r` subcube in which the first `r` bits are zero, with the final `d` bits free; and
2. one additional point obtained by flipping the first fixed bit, with all other bits zero.

Call the resulting Boolean function `f_{r,d}`. Every finite `d` has genuinely active formerly-free coordinates, so this is not a one-point defect after deleting dummies.

Put

\[
a=2^{1-r},\qquad \varepsilon=2^{-d}.
\]

Direct edge counting gives the exact influences

\[
j_1=a(1-\varepsilon),
\tag{11}
\]

\[
j_i=a(1+\varepsilon),\qquad 2\le i\le r,
\tag{12}
\]

and for every one of the `d` free directions,

\[
j_i=a\varepsilon.
\tag{13}
\]

Hence

\[
I(f_{r,d})=a\,[r+(r+d-2)\varepsilon].
\tag{14}
\]

For `r>=3`, every influence is at most `1/2`, so the Palm depth theorem applies.

Using the exact two-coordinate spectral/sensitivity matching identity from the immediately preceding B12 sensitivity bridge,

\[
\mathbb E[K(K-1)]
=\mathbb E[|\operatorname{Sens}_f(X)|(|\operatorname{Sens}_f(X)|-1)].
\tag{15}
\]

The sensitivity degrees of this family can be counted exactly. The resulting second factorial moment is

\[
\mathbb E[K(K-1)]
=
\frac{(2^d-1)r(r-1)+(r-1)(r-2)+(r+d-1)(r+d-2)+2d}{2^{r+d}}.
\tag{16}
\]

Summing (3) over coordinates gives the exact identity

\[
\mathcal D(f)
=
\mathbb E[K(K-1)]
-
\frac12\sum_i j_i\log_2\frac1{j_i}.
\tag{17}
\]

Substituting (11)--(16), the order-one terms cancel. For fixed `r`, the remainder is

\[
\boxed{\frac{\mathcal D(f_{r,d})}{I(f_{r,d})}=O_r(d^2 2^{-d})\longrightarrow0.}
\tag{18}
\]

Thus (10) is false.

This counterexample is conceptually useful: the exact equality theorem is globally rigid, but its quantitative neighborhood contains functions in growing dimension that are arbitrarily close in normalized defect while having additional active coordinates of exponentially small influence. A viable stability theorem therefore needs a **distance/error modulus that weights tiny coordinates appropriately**; it cannot be a fixed spectral gap.

## 5. Executed checks and numbers

`check_global_depth_rigidity.py` was executed with the Python standard library.

### Exact exhaustive equality classification through n=4

The checker uses an integer Walsh-Hadamard transform and exact equality conditions. Among nonconstant functions with every active influence at most `1/2`:

| n | eligible | zero-defect | one-point after dummies | counterexamples |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 8 | 8 | 8 | 0 |
| 3 | 104 | 40 | 40 | 0 |
| 4 | 14528 | 144 | 144 | 0 |

These finite checks support the algebraic theorem; they are not its proof.

### Gap-refuting family, r=3

For `d=1,...,12`, the script independently computes the spectrum and checks it against the closed forms above. Selected rows:

| d | n | H/I | D/I | I | min influence |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 2.848681566 | 0.094360938 | 1.000000 | 0.125 |
| 4 | 7 | 3.093090452 | 0.090349958 | 0.828125 | 0.015625 |
| 8 | 11 | 2.972460197 | 0.013803825 | 0.758789 | 0.0009765625 |
| 12 | 15 | 2.957287817 | 0.001359370 | 0.750793 | 0.00006103515625 |

The normalized defect is already below `1.4e-3` at `d=12`, while the function is not an exact one-point defect. The complete output is archived in `verification.txt`.

## 6. What this changes in the compression route

The scalar-depth obstruction from the preceding peer run showed that an arbitrary subset law can saturate the Palm mean-depth inequality while losing unbounded terminal identity information. The theorem above shows that a **genuine Boolean spectrum cannot globally realize that exact pathology**: exact row-depth equality everywhere collapses the whole function to the one-point family.

But the family in Section 4 shows that this rigidity has no fixed quantitative gap. Therefore the next proof step cannot simply say “non-one-point functions have `D >= cI`.” The correct shape must be a stable decomposition:

- large `Delta_i` rows pay information loss directly;
- small `Delta_i` rows are close, in a weighted sense, to signed-subcube derivative rows;
- the compatibility graph of those near-subcube rows must be close to a hierarchical/clique block structure;
- exponentially tiny exceptional coordinates must be charged at their own influence scale rather than by ambient dimension.

This is precisely compatible with the earlier hierarchical spectral-prefix code: near-clique blocks should be encoded as blocks, not as independent singleton branches.

## 7. Ledger

**PROVED**

- Under `0<Inf_i<=1/2` on every active coordinate, zero total Palm depth defect `D(f)=sum_i Inf_i Delta_i=0` forces `f`, after dummies/symmetries, to be a one-point defect.
- Exact compatibility relation (6) glues all equality derivative rows into disjoint Fourier cliques; Booleanity allows only one active clique.
- The explicit subcube-plus-point family has influences (11)--(13), total influence (14), factorial moment (16), and normalized defect tending to zero as in (18).

**REFUTED**

- A universal positive constant gap `D(f)>=c_0 I(f)` away from exact one-point defects.

**OPEN**

- A quantitative *stable* global row-shape theorem with a weighted distance modulus.
- A corresponding amortized reverse-data-processing / prefix-branching inequality.
- Full uniform-cube FEI.

## 8. Next attack

Prove a weighted stability theorem by combining (1) with quantitative cube edge-isoperimetric stability and the internal-sign slack, but measure row error in an influence-weighted transport/divergence rather than total variation over all ambient coordinates. Then propagate pairwise near-neighborhood consistency to a near-clique block decomposition. The immediate falsification test should be the family `f_{r,d}` above: any proposed stability modulus must correctly assign only `O_r(d^2 2^{-d})` total cost to its exponentially weak extra coordinates. If that survives, insert the stable blocks into the exact uniform-prefix chain and attempt to pay terminal-to-prefix identity loss by `sum_i j_i Delta_i` plus block entropy, preserving the factorial rebate.
