# fleet04/B14 — exact extreme-product reduction and compact-fragment localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T114319Z-b14-qform-extreme-reduction-r1`  
**Status:** `TARGET_LEVEL_REDUCTION / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source corrections

Let (X_1,\dots,X_n) be independent real random variables with densities
(0\le f_i\le1), and let (A) be real symmetric with at least three
eigenvalues of absolute value at least one.  The target is a universal
(C<\infty) such that (Q(X)=X^TAX) has density bounded by (C).

This report does not use the refuted law-uniform pointwise oscillatory-decay
claim, does not diagonalize (A) while retaining false independence, and does
not use the dimension-losing fiber-supremum bound.

## 2. Interval formulation

For a probability law \(\mu\) on \(\mathbb R\), the following are equivalent:

1. \(\mu\) has a Radon--Nikodym density bounded by \(C\) almost everywhere;
2. \(\mu(I)\le C|I|\) for every bounded interval \(I\).

Only (2) needs proof in the quadratic-form problem.  Indeed, (2) first extends
from intervals to open sets, then to all Borel sets by regularity, giving
\(\mu\le C\,\mathrm{Leb}\); Radon--Nikodym gives (1).  The converse is immediate.

## 3. One-coordinate bathtub lemma

Let \(g:\mathbb R\to[0,1]\) be measurable.  Among all probability densities
\(f\) satisfying \(0\le f\le1\), the functional

\[
             f\longmapsto\int g(x)f(x)\,dx
\]

is maximized by an indicator \(1_E\) of a measurable set \(E\) of Lebesgue
measure one.

To see this, choose a threshold \(c\) for which

\[
 |\{g>c\}|\le1\le |\{g\ge c\}|,
\]

with the evident endpoint conventions, and choose a measurable subset of the
level set \(\{g=c\}\) so that the union with \(\{g>c\}\) has measure one.
Nonatomicity of Lebesgue measure permits this choice.  Call the resulting set
\(E\).  Then

\[
 \int (1_E-f)(g-c)\,dx\ge0,
 \qquad \int(1_E-f)\,dx=0,
\]

so \(\int_E g\ge\int gf\).  If the positive support of \(g\) has measure below
one, fill \(E\) in \(\{g=0\}\).

## 4. Exact extreme-product reduction

Fix a Borel interval \(I\), a real symmetric matrix \(A\), and all input
densities except \(f_i\).  Conditional integration defines

\[
 g_i(x)=\int 1_{\{Q(x_1,\ldots,x_{i-1},x,x_{i+1},\ldots,x_n)\in I\}}
          \prod_{j\ne i}f_j(x_j)\,dx_{-i},
\]

where \(0\le g_i\le1\).  The preceding lemma replaces \(f_i\) by
\(1_{E_i}\), \(|E_i|=1\), without decreasing \(\Pr\{Q(X)\in I\}\).
Doing this successively for \(i=1,\ldots,n\) gives

\[
 \Pr_f\{Q(X)\in I\}
 \le
 \Pr_{E_1,\ldots,E_n}\{Q(U)\in I\},
\]

where the \(U_i\) are independent and uniform on measurable sets \(E_i\) of
measure one.  The sets may depend on \(I\), which is harmless because the
desired bound is uniform over all such sets and intervals.

Hence the full conjecture is **equivalent**, with exactly the same best
constant, to its restriction to product densities

\[
                       f_i=1_{E_i},\qquad |E_i|=1.
\]

The reverse implication is trivial because these are admissible densities.
This reduction is valid for every measurable phase, not only quadratic phases.

## 5. Compact finite-fragment localization without moment assumptions

The extreme sets need not be bounded or connected.  Nevertheless no constant
is lost by restricting further to compact finite unions of intervals.

For a measurable \(E\subset\mathbb R\) with \(|E|=1\), put
\(A_R=E\cap[-R,R]\) and \(d_R=1-|A_R|\).  Choose a bounded measurable filler
\(F_R\subset[-M_R,M_R]\setminus A_R\) of measure \(d_R\), and set
\(E_R=A_R\cup F_R\).  Then \(|E_R|=1\) and

\[
                       |E\triangle E_R|\le2d_R\longrightarrow0.
\]

Lebesgue regularity approximates each bounded \(E_R\) in symmetric difference
by a finite union of bounded intervals.  Adding or deleting finitely many
interval pieces corrects its total measure to exactly one while increasing the
symmetric difference by at most the original measure error.  Thus there are
compact finite unions \(E^{(m)}\), all of measure one, with
\(|E^{(m)}\triangle E|\to0\).

For indicator densities of equal mass one,

\[
 d_{\rm TV}(1_Edx,1_Fdx)=\frac12|E\triangle F|.
\]

The product total-variation bound

\[
 d_{\rm TV}\!\left(\bigotimes_i\mu_i,\bigotimes_i\nu_i\right)
 \le\sum_i d_{\rm TV}(\mu_i,\nu_i)
\]

therefore shows that all interval probabilities converge under the simultaneous
finite-fragment approximation.  Consequently the original conjecture is
equivalent, with no loss in \(C\), to the following sharply localized problem:

> each input is uniform on a compact finite union of intervals of total length
> one; the locations, diameters, number of fragments and separations are
> arbitrary and receive no moment bound.

This is the correct way to retain arbitrary translations and distant fragments.
A coordinate translation merely moves these interval components and creates
the corresponding linear term after completing the quadratic expression; no
compactness uniform in the translation or support diameter is asserted.

## 6. What this pays and what remains

This is a target-level reduction, not a proof of the density bound.  It removes
general fractional densities, unbounded support and infinitely fragmented
support as separate analytic obstacles.  A future proof may work on finite
unions of intervals and pass to the full class by total variation without
assuming moments or connected support.

The first unpaid implication is now geometric: prove a universal small-ball
bound for rotated indefinite quadratic forms under product indicators of
finite interval unions, uniformly in the number, positions and separation of
the components.  The phase-aligned-density correction still forbids a uniform
pointwise Fourier-decay shortcut even on this localized class as the number and
locations of fragments vary.

No completed fleet01/B14 quadratic-form handoff was discoverable at the
coherent source snapshot.  The reduction is compatible with the proven
diagonal \(C=\pi\) theorem in `CURRENT_RESEARCH.md`: it changes only the input
class and leaves that theorem's convolution proof intact.

