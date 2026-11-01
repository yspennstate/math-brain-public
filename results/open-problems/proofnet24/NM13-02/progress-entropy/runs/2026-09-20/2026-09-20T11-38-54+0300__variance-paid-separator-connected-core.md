Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — variance-paid separator allocation and a connected-core obstruction to root Wiener width

## 0. Parent scope/bound versus demonstrated mechanism gain

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one universal finite constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent scope/bound before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. Nothing in this report promotes a finite-dimensional check, a bounded-Wiener theorem, or a separator class to full FEI.

**Mechanism gain in this run.** P03's newest report localizes its remaining structural obstruction to a *single connected degree-at-least-three ANF interaction core* and proposes querying a small physical separator before applying its quadratic-product Wiener theorem to the descendant components. This run proves a paid separator lemma and then applies it to an explicit connected one-hub cubic family on which the root quadratic-product Wiener width is exponentially large although hereditary allocation is uniformly bounded.

The two new conclusions are:

1. the previously stated P03 minor-child inequality has the stronger, restriction-useful form
   \[
   \boxed{
   B_i(f)\le C_\chi j_i(f)+
   \min\{\operatorname{Var}(f^+),\operatorname{Var}(f^-)\},
   }
   \tag{0.1}
   \]
   where
   \[
   C_\chi=2+\frac1{\sqrt e\,\ln2}=2.8750387749\ldots;
   \]
   this stronger variance term is present before the Poincare relaxation in P03's proof, but was not previously promoted as the tree payment. I rederive it below and use it to prove a **constant-preserving variance-paid separator rule**;
2. for
   \[
   F_m(b,y,z)=(-1)^{bQ_m(y,z)},
   \qquad
   Q_m=\sum_{a=1}^m y_az_a\pmod2,
   \tag{0.2}
   \]
   the degree-three interaction hypergraph is connected but has the single physical separator `b`, while
   \[
   \boxed{
   2^{\lceil m/2\rceil}
   \le \Omega_2(F_m)=\Lambda_2(F_m)
   \le 2^{\lfloor m/2\rfloor}+2^{\lceil m/2\rceil}-2^{-\lceil m/2\rceil}.
   }
   \tag{0.3}
   \]
   Thus root `Omega_2` grows exponentially even on a one-separator connected core. Querying `b`, however, leaves one constant and one quadratic branch, and the paid separator rule gives a dimension-free hereditary certificate. The earlier NM13-02 cubic-star theorem already gave the sharper coarse certificate `A(F_m)<=2`; that prior result is preserved and is **not** relabeled new here.

The lesson is precise: a universal proof cannot pay `C_QW(Omega_2(f))` once at the root of every connected core. Large root quadratic-normalized Wiener width can be entirely a separator artifact. What remains viable is branchwise use of `Omega_2` *after* a paid physical separator.

## 1. Current directive, dependencies, and compact handoff

The controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Current LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory complementary to P03. The policy prioritizes substantive proof work over archive-wide auditing and explicitly forbids treating restricted results as full FEI.

The current P03 entrypoint `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`, still records full FEI as OPEN and preserves the false/retired routes: the pointwise erasure shortcut, fixed-coefficient affine drift, the full resolvent/interpolation target, and Han's all-coordinate absolute-overlap criterion are not valid universal FEI arguments. None is revived here. The fresh-control theorem still uses appended independent controls and remains a restricted result; it is not used below.

### Compact NM13-02 handoff

Preserved without scope inflation:

- quadratic phases have the exact polar-rank hereditary telescope and hereditary constant at most `1`;
- queried influence plus weighted descendant influence is an exact budget, enabling max-splicing of branch-dependent certificates;
- character-child, one-defect, and truncated minor-child payments give dimension-free hereditary control in their stated classes;
- the descendant-influence theorem gives bounded-depth-to-quadratic control and, in particular, the earlier cubic-star certificate `A<=2`;
- hybrid decision-tree recursion gives uniform control for nested canalizing quadratic twists;
- one- and two-affine-flat quadratic twists have their previously stated restricted constants;
- the newest NM13-02 theorem defines
  \[
  \Lambda_2(f)=\min_{\deg q\le2}\Lambda((-1)^qf)
  \]
  and proves
  \[
  H(f),R_T(f)\le C_{QW}(\Lambda_2(f))I(f),
  \qquad
  C_{QW}(L)=\max\{15,2\log_2e+12\log_2L\},
  \]
  with `Lambda_2` nonincreasing under physical restrictions.

### Exact newest P03 dependency

The newest P03 report is

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T10-27-34+0300__fei-quadratic-product-wiener-recombination.md`

blob `b6a4a006b7747fb222b9895f29f6a156f1f5cf28`.

It defines a quadratic-product width `Omega_2` by factoring the nonquadratic part into disjoint physical blocks and taking the maximum `Lambda_2` of one block. It proves that disconnected high-degree components and arbitrary cross-block quadratic couplings do not multiply the constant. Its exact remaining obstruction is a **single connected degree>=3 ANF interaction core**. Its proposed next route is separator width: query a small physical separator, let the descendants break into controlled components, and charge the separator queries to actual influence.

That is the obstruction attacked below. I do not take over P03's `Omega_2` theorem; I use its definition and newest obstruction as the target.

### P03 local input and ownership

P03's earlier report

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T05-32-22+0300__fei-minor-child-allocation.md`

blob `7e12f35a9c2fae61f3c63e8434a493762a0e8081`, states

\[
B_i(f)\le C_\chi j_i(f)+\min\{I(f^+),I(f^-)\}.
\tag{1.1}
\]

Its proof passes through a variance estimate and only at the last step invokes Poincare `Var<=I`. Section 2 independently rederives the proof while stopping before that relaxation. Thus P03 retains ownership of its stated minor-influence lemma; the project-level delta here is the **variance-paid tree/separator use** of the sharper intermediate inequality.

## 2. Stronger local theorem: pay the minor child by variance, not influence

Let `i` be a physical coordinate, `g=f^+`, `h=f^-`, and for residual Fourier labels `T` write

\[
a_T=\widehat g(T),\qquad b_T=\widehat h(T).
\]

The two parent coefficients in the `i`-fiber are

\[
\widehat f(T)=\frac{a_T+b_T}{2},
\qquad
\widehat f(T\cup\{i\})=\frac{a_T-b_T}{2}.
\]

Put

\[
q_T=\frac{a_T^2+b_T^2}{2},
\qquad
 e_T=\frac{(a_T-b_T)^2}{4}.
\]

Then the conditional spectral-bit entropy is exactly

\[
B_i(f)=\sum_T q_T h_2(e_T/q_T).
\tag{2.1}
\]

Multiplying `f` by the physical character `x_i` complements the spectral bit, preserves `B_i` and both child variances, and changes the queried disagreement probability `delta` to `1-delta`. Hence normalize

\[
\varepsilon:=j_i(f)=\min\{\delta,1-\delta\}\le\frac12
\]

and again call the resulting children `g,h`, so `Pr[g!=h]=epsilon`. Exchange them so that

\[
\operatorname{Var}(g)=\min\{\operatorname{Var}(f^+),\operatorname{Var}(f^-)\},
\]

then multiply both by a common sign so `E g>=0`. Write

\[
\eta=\Pr[g=-1]\le\frac12,
\qquad
\beta=\Pr[h=-1].
\]

Because the children differ on an `epsilon` fraction,

\[
|\beta-\eta|\le\varepsilon.
\tag{2.2}
\]

For every nonconstant Fourier fiber, `h_2<=1`, so

\[
\begin{aligned}
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
&\le \frac12(\operatorname{Var}g+\operatorname{Var}h)\\
&=2\eta(1-\eta)+2\beta(1-\beta).
\end{aligned}
\tag{2.3}
\]

Let `t=beta-eta`. Since `eta<=1/2` and `|t|<=epsilon<=1/2`,

\[
\beta(1-\beta)-\eta(1-\eta)
=t(1-2\eta)-t^2
\le\varepsilon(1-\varepsilon).
\tag{2.4}
\]

Therefore

\[
\sum_{T\ne\varnothing}q_T h_2(e_T/q_T)
\le \operatorname{Var}(g)+2\varepsilon(1-\varepsilon).
\tag{2.5}
\]

At the constant Fourier fiber,

\[
e_\varnothing=(\beta-\eta)^2\le\varepsilon^2.
\]

For fixed `e`, `q -> q h_2(e/q)` is increasing on `[e,1]`, and

\[
h_2(x)\le x\log_2(e/x).
\]

Thus

\[
q_\varnothing h_2(e_\varnothing/q_\varnothing)
\le\varepsilon^2\log_2\frac e{\varepsilon^2}.
\tag{2.6}
\]

Combining (2.5)--(2.6),

\[
B_i(f)
\le \operatorname{Var}(g)+\varepsilon U(\varepsilon),
\]

where

\[
U(\varepsilon)=2(1-\varepsilon)
+\varepsilon\log_2\frac e{\varepsilon^2}.
\]

A direct derivative calculation gives the unique maximizer

\[
\varepsilon_0=\frac1{2\sqrt e},
\qquad
\max_{0<\varepsilon\le1/2}U(\varepsilon)
=2+\frac1{\sqrt e\ln2}=C_\chi.
\]

Hence:

### Theorem 2.1 — variance-minor conditional allocation

For every Boolean function and every physical coordinate,

\[
\boxed{
B_i(f)
\le C_\chi j_i(f)
+\min\{\operatorname{Var}(f^+),\operatorname{Var}(f^-)\}.
}
\tag{2.7}
\]

P03's stated inequality (1.1) follows immediately from `Var(g)<=I(g)`, but the variance version is strictly more informative for separator branches that become highly biased or constant.

For any adaptive restriction tree `T`, define

\[
V_T:=\sum_{v\ {m internal}}w_v
\min\{\operatorname{Var}(f_v^+),\operatorname{Var}(f_v^-)\}.
\tag{2.8}
\]

Summing (2.7) gives the all-dimensional tree estimate

\[
\boxed{R_T\le C_\chi J_T+V_T.}
\tag{2.9}
\]

No fresh variables or branch-independence assumption is used.

## 3. Paid dependent-branch separator rules

### Theorem 3.1 — constant-preserving variance-paid separator

Suppose a physical split at coordinate `i` has two descendant continuation trees satisfying a common hereditary certificate

\[
R_+\le K I(f^+),\qquad R_-\le K I(f^-),
\]

with `K>=C_chi`. Put

\[
\alpha=\operatorname{Inf}_i(f),
\qquad
v=\min\{\operatorname{Var}(f^+),\operatorname{Var}(f^-)\}.
\]

If

\[
\boxed{v\le(K-C_\chi)\alpha,}
\tag{3.1}
\]

then grafting the two dependent branch continuations below this split preserves the same constant:

\[
\boxed{R_{\rm graft}(f)\le K I(f).}
\tag{3.2}
\]

#### Proof

By Theorem 2.1, `j_i<=alpha`, and the exact one-step influence identity,

\[
\begin{aligned}
R_{\rm graft}(f)
&\le C_\chi j_i+v
+\frac K2\left(I(f^+)+I(f^-)\right)\\
&\le C_\chi\alpha+v+K(I(f)-\alpha)\\
&=K I(f)+v-(K-C_\chi)\alpha.
\end{aligned}
\]

Condition (3.1) gives (3.2). QED.

This is a literal paid dependent-branch recombination statement: no independence of `f^+` and `f^-` is asserted, and a separator incurs no increase in the hereditary constant once the smaller branch variance is paid by the queried physical influence.

Two useful special cases are immediate.

- If one child is constant, then `v=0`. Any common descendant constant `K>=C_chi` is preserved **with zero separator surcharge**.
- More generally, if a candidate separator has influence `alpha` and its lower-variance child has variance `v`, the only local burden is the dimensionless ratio `v/alpha`, not that child's total influence or decision-tree depth.

### Corollary 3.2 — variance-heavy spine amortization

Build a partial spine by continuing at each node into the child of larger variance and stopping the smaller-variance child. Then

\[
V_T=2\sum_{\ell\ {m minor\ leaf}}w_\ell\operatorname{Var}(f_\ell).
\tag{3.3}
\]

Law of total variance for the terminal restriction partition gives

\[
\sum_{\ell\ {m all\ leaves}}w_\ell\operatorname{Var}(f_\ell)
\le\operatorname{Var}(f),
\]

hence

\[
\boxed{V_T\le2\operatorname{Var}(f).}
\tag{3.4}
\]

If every stopping leaf has a hereditary continuation with constant `K`, exact influence telescoping and (2.9) yield

\[
\boxed{
R_{\rm graft}(f)
\le \max\{C_\chi,K\}I(f)+2\operatorname{Var}(f).
}
\tag{3.5}
\]

This does not by itself give full FEI: `Var(f)<=I(f)` only recovers an additive `2` in the multiplicative constant. Its value is bias-sensitive amortization and the zero-variance separator case above.

## 4. The connected one-hub cubic family

Identify the physical cube with bit coordinates over `F_2`. For `m>=1`, define

\[
Q_m(y,z)=\sum_{a=1}^m y_az_a,
\qquad
F_m(b,y,z)=(-1)^{bQ_m(y,z)}.
\tag{4.1}
\]

The high-degree ANF monomials are precisely

\[
b y_1z_1,\ldots,b y_mz_m.
\]

Their interaction hypergraph is connected because every hyperedge contains `b`; deleting the single physical coordinate `b` destroys every degree-three hyperedge. Thus this is exactly the kind of connected core with a tiny separator proposed in P03's newest report.

### 4.1 Influence and inherited hereditary cost

For one hyperbolic pair,

\[
\mathbb E(-1)^{yz}=\frac12,
\]

so

\[
\mathbb E(-1)^{Q_m}=2^{-m}.
\]

Therefore

\[
\delta_m:=\operatorname{Inf}_b(F_m)
=\Pr(Q_m=1)
=\frac{1-2^{-m}}2.
\tag{4.2}
\]

For every `y_a` and `z_a`, the derivative is respectively `b z_a` or `b y_a`, hence

\[
\operatorname{Inf}_{y_a}(F_m)
=\operatorname{Inf}_{z_a}(F_m)=\frac14.
\]

Thus

\[
\boxed{I(F_m)=\frac m2+\delta_m.}
\tag{4.3}
\]

Querying `b` gives a constant child and the quadratic phase `(-1)^{Q_m}`. Its polar rank is `2m`, its total influence is `m`, and the earlier NM13-02 quadratic rank theorem gives hereditary allocation exactly `m` on a full continuation tree. Since the root conditional bit entropy is at most one,

\[
R_T(F_m)\le1+\frac m2\le2I(F_m).
\tag{4.4}
\]

This recovers the **previously proved** cubic-star certificate `A(F_m)<=2`; it is included only to put the new obstruction calculation on the same family. Using Theorem 2.1 instead, the constant child has variance zero, so the separator itself has no residual variance payment and a `C_chi` common continuation constant is preserved.

## 5. Exponential root `Omega_2` on the same cheap hereditary family

The new calculation is that P03's root quadratic-product Wiener width is exponentially large on `F_m`.

### Lemma 5.1 — connectedness forces one `Omega_2` block

In any quadratic product presentation

\[
F_m=(-1)^q\prod_a u_a(x_{B_a})
\]

with disjoint physical blocks, the unique `F_2` phase polynomial is the sum of the degree-at-most-two global phase and block-local phase polynomials. A cubic monomial cannot be supplied by the global quadratic. Hence every support `{b,y_a,z_a}` must lie inside one block. Since all supports share `b`, every active coordinate lies in the same block. Therefore

\[
\boxed{\Omega_2(F_m)=\Lambda_2(F_m).}
\tag{5.1}
\]

### Lemma 5.2 — exponential lower bound for every quadratic normalization

Let `r(b,y,z)` be an arbitrary quadratic twist. Write

\[
r(b,u)=r_0(u)+b\ell(u),
\]

where `u=(y,z)`, `r_0` is quadratic, and `ell` is affine. The two `b`-children of the twisted function are quadratic phases

\[
g=(-1)^{r_0},
\qquad
h=(-1)^{r_0+Q_m+\ell}.
\]

Let `A` be the alternating polar matrix of `r_0` and let `M` be that of `Q_m`. Then

\[
\operatorname{rank}M=2m,
\qquad
\operatorname{polar}(h)=A+M.
\]

Rank subadditivity gives

\[
2m=\operatorname{rank}M
\le\operatorname{rank}A+\operatorname{rank}(A+M).
\tag{5.2}
\]

Both alternating ranks are even, so

\[
\max\{\operatorname{rank}A,\operatorname{rank}(A+M)\}
\ge2\lceil m/2\rceil.
\tag{5.3}
\]

A quadratic phase of polar rank `r` has Wiener norm `2^{r/2}`. If `a_S=\widehat g(S)` and `b_S=\widehat h(S)`, the parent Fourier pair over `S` is

\[
\frac{a_S+b_S}{2},\qquad\frac{a_S-b_S}{2},
\]

and the elementary real identity

\[
\left|\frac{a+b}{2}\right|+
\left|\frac{a-b}{2}\right|
=\max\{|a|,|b|\}
\tag{5.4}
\]

implies

\[
\Lambda((-1)^rF_m)
=\sum_S\max\{|a_S|,|b_S|\}
\ge\max\{\Lambda(g),\Lambda(h)\}.
\]

Together with (5.3),

\[
\boxed{
\Lambda((-1)^rF_m)\ge2^{\lceil m/2\rceil}
}
\]

for every quadratic `r`, and hence

\[
\boxed{\Lambda_2(F_m)\ge2^{\lceil m/2\rceil}.}
\tag{5.5}
\]

### Lemma 5.3 — matching exponential upper bound

Let `k=floor(m/2)` and twist by

\[
r_0=\sum_{a=1}^{k}y_az_a.
\]

At `b=0` the child is the hyperbolic quadratic on the first `k` pairs; at `b=1` those terms cancel from `Q_m` and the child is the hyperbolic quadratic on the remaining `m-k=ceil(m/2)` pairs. Their Fourier supports lie on complementary coordinate subspaces and meet only at the empty frequency. The first has `2^{2k}` coefficients of magnitude `2^{-k}`, the second has `2^{2(m-k)}` coefficients of magnitude `2^{-(m-k)}`. Using (5.4) and `k<=m-k`, the parent Wiener norm is exactly

\[
2^k+2^{m-k}-2^{-(m-k)}.
\]

Therefore

\[
\boxed{
\Lambda_2(F_m)
\le
2^{\lfloor m/2\rfloor}
+2^{\lceil m/2\rceil}
-2^{-\lceil m/2\rceil}.
}
\tag{5.6}
\]

Combining (5.1), (5.5), and (5.6) proves (0.3):

\[
\Omega_2(F_m)=\Lambda_2(F_m)=\Theta(2^{m/2}).
\tag{5.7}
\]

This is an all-dimensional analytical statement, not a numerical extrapolation.

## 6. Direct application to P03's newest obstruction

P03's newest theorem gives a hereditary certificate controlled by

\[
C_{QW}(\Omega_2(f))
=\max\{15,2\log_2e+12\log_2\Omega_2(f)\}.
\]

For the connected core `F_m`, (5.5) forces

\[
C_{QW}(\Omega_2(F_m))
\ge
\max\{15,2\log_2e+12\lceil m/2\rceil\},
\tag{6.1}
\]

so the **root scalar certificate grows linearly in `m`**, even though the actual hereditary allocation has the inherited uniform bound `A(F_m)<=2`.

This does not refute P03's theorem, and it does not refute every possible `Omega_2`-based stopping argument. It proves the sharper structural point that P03's own proposed separator step is necessary: `Omega_2` can be huge *before* the separator and collapse to `1` on both descendants.

Indeed, query `b`. The two children are constant and quadratic, hence each has `Lambda_2=Omega_2=1` and hereditary constant at most `1`. The lower-variance child is constant, so `v=0`. Theorem 3.1 therefore pays the separator with no residual variance surcharge. Equivalently, direct max-splicing with Theorem 2.1 gives

\[
R_T(F_m)
\le C_\chi\delta_m+\frac m2
\le C_\chi I(F_m).
\tag{6.2}
\]

The earlier crude cubic-star estimate (4.4) is numerically sharper (`2<C_chi`), but (6.2) is the mechanism relevant to P03's current proof: **large connected-core Wiener width is discharged by one paid physical separator, not by bounding the root width**.

Thus the current full-scope obstruction is narrower than it was one run ago. A useful universal separator theorem must control, along a branch-adaptive separator tree,

\[
\frac{
\min\{\operatorname{Var}(f_v^+),\operatorname{Var}(f_v^-)\}
}{
\operatorname{Inf}_{i(v)}(f_v)
}
\]

or another amortized quantity that implies (3.1), while descendant connected components are terminated by P03's `Omega_2` theorem or another certified class. A theorem that merely upper-bounds root `Omega_2` is impossible on this family.

## 7. Sanity checks executed now

The new checker was executed before persistence.

1. **Variance-minor inequality.** Exhaustive over every ordered pair of Boolean children through residual dimension three:
   \[
   4+16+256+65536=65812
   \]
   cases. It directly computed the Fourier-fiber conditional entropy `B_i` and checked
   \[
   B_i\le C_\chi j_i+\min\{\operatorname{Var}(f^+),\operatorname{Var}(f^-)\}.
   \]
   Maximum numerical violation: exactly `0.0` (trivial zero-cost cases).
2. **Connected cubic hub formulas.** For `m=1,...,16`, it checked the exact formulas for `Inf_b`, total influence, the inherited `R<=1+m/2<=2I` certificate, and the analytical lower/upper Wiener-width formulas. Maximum `R-2I` was `0.0`, at `m=1`.
3. **Direct `Lambda_2` brute force in the first two nontrivial sizes.** Affine terms were omitted because multiplying by an affine character only translates/signs the Fourier spectrum and leaves Wiener norm invariant. Exhausting every pure quadratic twist gave
   \[
   \Lambda_2(F_1)=2.5,
   \qquad
   \Lambda_2(F_2)=3.5,
   \]
   consistent with the all-dimensional bounds.

Checker:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T11-38-54+0300__check_variance_paid_separator.py`

- creation commit `050e171f2882c9492e70949ad0b36b5409276629`
- blob `cf2a505a8587c795d548d3eb5ea653c1d0b445ff`

Archived output:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T11-38-54+0300__variance_paid_separator_check.json`

- creation commit `d1b53e9be569507efd3eb8955507f89d1f6c3b36`
- blob `2ed70416d99b32fab1586799da1747ca26fcf9b4`

The checker is a sanity check only. The claims above are proved analytically.

## 8. Current primary-source status and literature boundary

A fresh bounded public-source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture* (submitted 29 May 2026). Its current abstract still states universal FEI as a conjecture, develops the physical-restriction/stopping-tree route, and says that its key branching inequality would imply full FEI **if** it held for all Boolean functions. It proves proper subclasses, not the universal theorem.

The current Li--Han paper, arXiv:2512.03117 (2 December 2025), still proves a general inequality containing the coordinate-profile correction

\[
\sum_i I_i(f)\log\frac1{I_i(f)}
\]

rather than a universal constant times total influence alone.

A bounded search for `Fourier entropy influence + quadratic Wiener norm`, `quadratic phase + Wiener norm + FEI`, and related terms recovered older Fourier-entropy complexity bounds but did not identify the exact variance-paid separator theorem or the `Omega_2(F_m)` calculation above. This is negative search evidence only: **publication priority remains UNVERIFIED**.

## 9. Failures, scope limits, and next mathematical target

Three limits are explicit.

1. The variance-minor inequality does **not** make `V_T` universally bounded on an arbitrary full tree. A parity-style expansion can repeatedly carry variance one. The variance-heavy spine only gives `V_T<=2 Var(f)`, not a zero universal surcharge.
2. The family `F_m` does **not** refute FEI or hereditary allocation. It does the opposite: it has a cheap hereditary tree. What it refutes is the hope that the *root value* of `Omega_2` or `Lambda_2` is itself a universally bounded complexity for connected cores.
3. P03's separately reported paid recombination theorem is not assumed as an established external theorem here. The main result is hereditary allocation and uses only exact Fourier identities, the rederived local variance bound, prior NM13-02 quadratic continuation, and P03's definition/current obstruction. Any source-facing FEI corollary that also consumes P03's recombination theorem remains project-conditional pending later independent review.

The next nonredundant attack is therefore a **separator amortization potential** rather than another root norm: for a chosen physical separator `S`, recursively query its coordinates while tracking the weighted minor-child variance, and prove a constant bound when deletion of `S` breaks the degree>=3 interaction hypergraph into `Omega_2`-controlled components. The one-hub theorem here is the base case. A materially different fallback, if variance payment accumulates on width-two examples, is to search for a connected bounded-separator family where every separator branch has large minor variance but hereditary allocation is still small; that would identify the next missing side-information term rather than adding another false scalar envelope.

## ledger_delta

```yaml
ledger_delta:
  track: NM13-02
  target: T01-FEI-hereditary-allocation
  parent_problem: Friedgut-Kalai Fourier entropy-influence conjecture
  parent_status_before: OPEN
  parent_status_after: OPEN
  universal_C_before: UNKNOWN
  universal_C_after: UNKNOWN
  new_claims:
    - "VARIANCE-MINOR: B_i <= C_chi j_i + min(Var child+, Var child-) (rederived strengthening implicit before P03's Poincare relaxation)"
    - "PAID-SEPARATOR: if both descendants have hereditary K>=C_chi and min child variance <= (K-C_chi) Inf_i, the parent retains the same K"
    - "CONNECTED-HUB-WIENER: for F_m=(-1)^{b sum y_a z_a}, Omega_2=Lambda_2 is between 2^{ceil(m/2)} and 2^{floor(m/2)}+2^{ceil(m/2)}-2^{-ceil(m/2)}"
    - "APPLICATION: root Omega_2 can be exponentially large on a connected one-separator core with inherited hereditary constant <=2; separator query collapses both descendants to Omega_2=1"
  mechanism_metric_before: "connected high-degree core remained P03's unresolved Omega_2/separator target"
  mechanism_metric_after: "root Omega_2 scalar shown insufficient; one-step variance-paid separator proved and applied"
  restricted_fresh_control_status: PRESERVED_RESTRICTED_NOT_FULL_FEI
  false_lemma_corrections: PRESERVED
  peer_claims_overwritten: false
  checker:
    path: "proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T11-38-54+0300__check_variance_paid_separator.py"
    commit: "050e171f2882c9492e70949ad0b36b5409276629"
    blob: "cf2a505a8587c795d548d3eb5ea653c1d0b445ff"
  checker_output:
    path: "proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T11-38-54+0300__variance_paid_separator_check.json"
    commit: "d1b53e9be569507efd3eb8955507f89d1f6c3b36"
    blob: "2ed70416d99b32fab1586799da1747ca26fcf9b4"
  checker_status: PASS
  independent_review: PENDING
  publication_priority: UNVERIFIED
  remaining_obstruction: "amortize minor-child variance along a separator tree for a single connected degree>=3 core; terminate descendants in Omega_2-controlled classes without paying root Omega_2"
  next_step: "prove width-one/multi-query separator variance budget, then stress width-two connected cores"
```

**End of complete run report.**
