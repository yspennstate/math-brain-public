SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B15, 2026-09-24T08:11:40Z.
attacking: exact continuity and jump structure of rough ruled mixtures with conditioning-generated moving boundaries.

# B15 — exact atomic-boundary jump formula for ruled mixtures

Run: 20260924T081140Z-fleet04-B15-atomic-boundary-r10.

Status: NEW REGULARITY THEOREM / FULL QFORM OPEN.

The full universal density conjecture remains open. This report distinguishes essential boundedness from continuity and never evaluates an arbitrary representative of the final rough density on a surface.

## 1. Moving-boundary theorem with atoms

Let \((\Omega,\pi)\) be a probability space, \(b:\Omega\to\mathbb R\) measurable, and for almost every \(\omega\) let
\[
h_\omega\in C_0([0,\infty)),\qquad 0\le h_\omega\le M.
\]
Assume joint measurability and define the canonical mixture
\[
H(t)=\int_\Omega {\bf1}_{\{t\ge b(\omega)\}}
h_\omega(t-b(\omega))\,d\pi(\omega).
\tag{1.1}
\]

Then \(H\) is a bounded density representative for the corresponding mixture measure and
\[
0\le H\le M.
\tag{1.2}
\]
It vanishes at both infinities. At every \(t_0\), both one-sided limits exist and
\[
\boxed{
H(t_0+)-H(t_0-)
=
\int_{\{b=t_0\}}h_\omega(0)\,d\pi(\omega).
}
\tag{1.3}
\]
With the convention in (1.1), \(H(t_0)=H(t_0+)\).

Consequently,
\[
\boxed{
H\in C_0(\mathbb R)
\iff
\int_{\{b=t\}}h_\omega(0)\,d\pi(\omega)=0
\quad\text{for every }t.
}
\tag{1.4}
\]
Because the kernels are nonnegative, this is equivalent to \(h_\omega(0)=0\) for almost every \(\omega\) on every atomic level set of \(b\). Atomlessness of \(b\) is therefore sufficient, but the theorem gives the exact weaker condition.

### Proof

For \(t_n\downarrow t_0\), the integrand in (1.1) converges pointwise to
\[
{\bf1}_{\{t_0>b(\omega)\}}h_\omega(t_0-b(\omega))
+
{\bf1}_{\{t_0=b(\omega)\}}h_\omega(0).
\]
For \(t_n\uparrow t_0\), it converges to the first term only. Dominated convergence with majorant \(M\) proves the one-sided limits and (1.3). It also proves ordinary continuity at every non-atomic boundary level.

As \(t\to-\infty\),
\[
H(t)\le M\pi\{b\le t\}\to0.
\]
For \(t\to+\infty\), choose \(R\) with \(\pi\{|b|>R\}<\varepsilon/M\). On \(\{|b|\le R\}\), \(t-b(\omega)\to\infty\), so dominated convergence gives decay; the complement costs at most \(\varepsilon\). Hence \(H\) vanishes at both infinities.

The interval identity
\[
\int_I H(t)\,dt
=
\int_\Omega\int_0^\infty
{\bf1}_{\{b(\omega)+s\in I\}}h_\omega(s)\,ds\,d\pi(\omega)
\tag{1.5}
\]
follows from Tonelli. Thus (1.1) is a canonical density obtained from interval probabilities, not a pointwise trace of an arbitrary version.

## 2. Finite-mixture and rough-product stability

If the cap-one input laws are approximated in total variation by finite mixtures or smooth cap-one laws, every uniform interval bound passes to the limit. Formula (1.5) identifies the limiting ruled submeasure, while (1.3) identifies its possible discontinuities. No threshold maximizer on the line and no surface value of a rough density is invoked.

This is compatible with the completed fleet01/B15 finite-\(L^p\) stability theorem: whenever its hypotheses provide strong finite-\(L^p\) convergence of output densities, (1.5) identifies the same limit; continuity is then decided by (1.4), rather than by an invalid \(L^\infty\)-limit argument.

## 3. Application to the physical reflection

Let
\[
B_*=I_3-\frac23{\bf1}{\bf1}^T,\qquad B_*^2=I_3,
\]
and write \(Q=U^TB_*U+Z\), where \(U\) consists of three original cap-one coordinates and \(Z\) is any independent outside quadratic polynomial. The completed ruled theorem supplies for the majority sheet a kernel
\[
h_+\in C_0([0,\infty)),\qquad \|h_+\|_\infty\le\pi\sqrt2.
\]
Therefore its translated submeasure has the canonical density
\[
H_+(t)=\mathbb E\!\left[
{\bf1}_{\{t\ge Z\}}h_+(t-Z)\right],
\]
with
\[
\boxed{\|H_+\|_\infty\le\pi\sqrt2,}
\tag{3.1}
\]
and exact jump formula
\[
\boxed{
H_+(t_0+)-H_+(t_0-)
=
\Pr(Z=t_0)\,h_+(0).
}
\tag{3.2}
\]

If \(Z\) is a nonconstant polynomial of independent absolutely continuous coordinates, then \(\Pr(Z=t)=0\) for every \(t\): each level set of a nonzero polynomial has Lebesgue measure zero. Thus
\[
\boxed{H_+\in C_0(\mathbb R),\qquad \|H_+\|_\infty\le\pi\sqrt2.}
\tag{3.3}
\]
This includes arbitrary fragmented and unbounded cap-one supports. If \(Z\) is constant, (3.2) records the possible sheet-edge jump exactly instead of falsely asserting continuity.

For the full output, the completed fleet01/B15 regularity compiler remains the appropriate route once a uniform full interval estimate is available. The present theorem supplies the missing sheetwise trace justification and shows precisely why a half-line estimate alone is not a full rank-three continuity theorem.

## 4. Remaining obstruction

The minority/two-sheet contribution may have a genuinely singular boundary kernel rather than a bounded trace \(h_\omega(0)\). Formula (1.3) does not control that singularity. The unresolved analytic task is a uniform two-sheet interval estimate, or an integrable envelope strong enough to replace the bounded majorant \(M\).

## Source pins

- Claude baseline: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837.
- Later single-hub continuation checked: math-open-problems@c4c23b784395630c094ba299a50712209921d1ae.
- Completed fleet01/B15 finite-\(L^p\) stability input retained.
- Predecessor rough ruled compiler: math-open-problems@a1654d5fe319f483999583921d127819e40bc868.
- Atomless-boundary predecessor: math-open-problems@10e3c2c60076516744368c00a83bb2f27c908298.

No post-rotation independence, arbitrary-joint coarea bound, support/moment hypothesis, or pointwise evaluation of a rough density representative is used.
