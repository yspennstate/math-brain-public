# B11 / A052 — tensor-prime quadratic curvature obstruction

**Status:** the proposed all-tensor-prime `GC14` good-coordinate estimate is
**REFUTED** by an explicit all-dimensional genuine Boolean family. A sharper
residual-qualified induction criterion remains open. Universal GU and full
FEI remain open.

## Frozen target and prior status

- Primary packet: **A052 (extremal/critical-source structure)**.
- Stable gap: `G-GU-SIGNED-KL`.
- Attempt: `A052-QUADRATIC-CURVATURE-5` (mechanism change from annealed
  upper-set charges to exact restriction curvature).
- Audited candidate: for every tensor-prime Boolean function,
  \[
  \min_i\frac{\Delta_iG}{\operatorname{Inf}_i}\le14.
  \]
- Claimed implication if true: `G<=14I`, then `U<=14I` and `H<=30I` by
  the source GU reduction.

The candidate survived every Boolean function through four variables, with
worst value `53/4` at the four-bit flat-spectrum gate. That gate is the first
member of the family below, not an isolated finite obstruction.

## Exact counterfamily

For every even `n>=2`, define

\[
q_n(x)=(-1)^{\sum_{r<s}x_rx_s}=(-1)^{\binom{|x|}{2}}.
\]

The quadratic polar form has full rank, so `q_n` is bent and has uniform
squared spectrum. Direct calculation gives

\[
U(q_n)=I(q_n)=\frac n2,qquad
G(q_n)=\frac{3n}{2}-n2^{1-n}.
\]

Every coordinate has influence `1/2`, and the exact restriction curvatures
are

\[
\Delta_iU=\frac32-2^{1-n},qquad
\Delta_iG=\frac{4n-1}{2}-(2n-1)2^{1-n}.
\]

Hence

\[
\boxed{
\frac{\Delta_iG}{\operatorname{Inf}_i}
=4n-1-(2n-1)2^{2-n}\to\infty
}
\]

for **every** coordinate. At `n=6` the ratio is `357/16=22.3125`, already
above 14. The family is tensor-prime: the mixed multiplicative rectangle at
zero equals `-1` for every pair of distinct coordinates, which is impossible
across a nontrivial disjoint tensor factorization.

For the general pair `(a,b)`, the normalized good-coordinate left side is

\[
4n-1-(2n-1)2^{2-n}-b(3-2^{2-n}),
\]

so the stronger criterion imposed on **all** tensor-prime functions fails for
every fixed finite `a` and `b<1`.

## Why this is not a GU or FEI counterexample

The same family satisfies the uniform proper-class theorem

\[
\frac{G(q_n)}{I(q_n)}=3-2^{2-n}<3,qquad
\frac{U(q_n)}{I(q_n)}=1.
\]

Thus `(a,b)=(3,0)` pays the family. The large local derivative comes from
negative child `G`: the same global reserve is recounted in every coordinate.
This refutes the descent helper, not GU and not FEI.

## Repaired smaller induction obligation

The minimal-counterexample proof never needs the good-coordinate estimate on
all tensor-prime functions. It suffices to prove it only for tensor-prime
functions with **positive residual**

\[
\mathcal R_{a,b}(f)=G(f)-aI(f)-bU(f)>0.
\]

Indeed, a smallest counterexample lies in that class and all its children
have nonpositive residual. Therefore the genuinely smaller sufficient target
is:

> Every tensor-prime Boolean `f` with `R_{a,b}(f)>0` has a relevant
> coordinate satisfying
> \[
> (1-b)\Delta_iU+sum_{j\ne i}\Delta_i\Delta_jU
> \le a\operatorname{Inf}_i.
> \]

For `(14,0)`, the quadratic family has strongly negative residual and is
correctly excluded. Whether the residual-qualified statement holds is open.
Future searches must filter by the complete residual and child residuals;
unqualified curvature maxima are structurally misleading.

## Verification and sources

The checker reconstructs literal Walsh spectra and physical children through
dimension 12, then checks the rational formulas for all 50 even dimensions
through 100. No randomness is used.

- Command: `python3 verify_quadratic_curvature.py`.
- Source input: `B20-A099-GU-CURVATURE-PRIME-v1`, report/proof at canonical
  commit `d4f6ed36c82043b71db1af3a1b633a6627c7cf33`.
- The original GU reduction remains unchanged: any proved universal pair
  gives `H <= (2+2a/(1-b))I`.

Independent review is pending. No full GU/FEI theorem is claimed.

