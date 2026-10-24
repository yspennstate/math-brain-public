# account03/B17 — B0 asymmetric dyadic lattice and a one-variable prime-gate reduction

**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-EXACT_LATTICE_CERTIFICATE + ANALYTIC_CURVE_REDUCTION`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository mathematical sources were retrieved directly, but no authenticated installed-brain retrieval/context was used in the derivation.  
**Publication priority:** `UNVERIFIED`; no novelty claim.

## 1. Candidate and exact missing implication

The current all-gate formulation is

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

For a base potential \(\Gamma_0\), the scalar quadratic lift satisfies

\[
D_{\Gamma_0+cq}(G;p)=D_{\Gamma_0}(G;p)+cW_G(p),
\qquad
W_G(p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0,
\]

so the requested gate margin is

\[
c_G(p)=-\frac{D_{\Gamma_0}(G;p)}{W_G(p)}
\]

when \(W_G>0\).

The fixed peer candidate consumed here is account01/B18's completed stable candidate from

`account01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`, report blob
`6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`:

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\qquad
a^\dagger=0.268204856,
\]

with \(\Gamma_0(1/2)=C_0=6.4548\). That report closes the full common-data addressing family, leaving genuinely composition-prime gates as the live obstruction.

The second cross-account result consumed substantively is account04/B17's exact biased restriction-margin cocycle,

`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`.

It proves that defect and quadratic currency telescope on the same physical restriction tree, with the exact nonnegative branch/KL and vertical-overlap credits retained. In particular a gate whose scalar-lift margin exceeds a proposed threshold must contain a positive-currency restriction gluing whose exact local margin exceeds that threshold. That makes the four-input composition-prime class

\[
B_0=\{0,1,2,3,4,5,8,10\}\subset Q_4
\]

a source-valid adversarial target rather than an arbitrary truth table.

**Old missing implication.** Prove that every composition-prime Boolean gate at every interior product bias has \(c_G\) no larger than the two-input AND extremum, or find a genuine gate/bias counterexample. The preceding B17 run closed one five-input \(p_5=1/4\) slice and explicitly handed off a fully nonuniform attack on \(B_0\).

This run performs that handoff without repeating the previous five-input slice.

## 2. Exact Boolean structure of B0

Use bit coordinates \(x_0,x_1,x_2,x_3\), least-significant bit first, and let the points in \(B_0\) be the negative event. Restricting on \(x_3\) gives two decomposable children:

\[
G_{x_3=0}^{-1}(-1)=\{x:\neg(x_1\wedge x_2)\},
\]

independent of \(x_0\), while

\[
G_{x_3=1}^{-1}(-1)=\{x:\neg x_0\wedge\neg x_2\},
\]

independent of \(x_1\).

Thus for product biases \(p_i=\Pr[X_i=1]\),

\[
\boxed{
p_{\rm out}
=(1-p_3)(1-p_1p_2)+p_3(1-p_0)(1-p_2).
}
\tag{2.1}
\]

This exhibits \(B_0\) as a genuinely prime *gluing* of two two-input-decomposable restrictions, exactly the geometry to which the consumed account04/B17 cocycle applies.

## 3. New analytic reduction on a nontrivial asymmetric curve

Take the one-parameter interior curve

\[
(p_0,p_1,p_2,p_3)=(s,s,1/2,1-s),\qquad 0<s<1,
\]

and put

\[
u=s(1-s).
\]

Equation (2.1) gives the exact cancellation

\[
\boxed{p_{\rm out}=1/2}
\]

for every \(s\). A direct biased-Walsh expansion gives the following complete nonzero squared spectrum:

\[
\begin{array}{c|c}
\text{multiplicity} & \widehat G(S)^2\\ \hline
2 & u(1-s)^2\\
2 & us^2\\
1 & (1-2u)^2\\
1 & u\\
4 & u^2\\
1 & u(1-4u).
\end{array}
\tag{3.1}
\]

All remaining five Fourier masses vanish. Hence, writing \(\phi(w)=w\log_2(1/w)\),

\[
\boxed{
\widetilde H_{B_0}(s)
=2\phi(u(1-s)^2)+2\phi(us^2)+\phi((1-2u)^2)
+\phi(u)+4\phi(u^2)+\phi(u(1-4u)).
}
\tag{3.2}
\]

The four biased spectral influences simplify exactly to

\[
\boxed{
\begin{aligned}
\operatorname{It}_0&=2s(1-s)^2,\\
\operatorname{It}_1&=2s^2(1-s),\\
\operatorname{It}_2&=1-2u,\\
\operatorname{It}_3&=2u.
\end{aligned}}
\tag{3.3}
\]

Therefore

\[
I=1+2u,
\qquad
\boxed{W_{B_0}=u/2.}
\tag{3.4}
\]

For *every symmetric* potential with \(\Gamma(1/2)=C_0\), the three noncentral coordinates in (3.3) contribute exactly one copy of \(\Gamma(s)+h_2(4u)\), while coordinate 2 contributes \((1-2u)C_0\). Thus the full four-input gate inequality on this curve is equivalent to the one-variable scalar inequality

\[
\boxed{
D_\Gamma^{B_0}(s)
=\Gamma(s)+h_2(4u)-2uC_0-\widetilde H_{B_0}(s).
}
\tag{3.5}
\]

This is a genuine dimensional reduction: the asymmetric prime-gate attack has gone from four bias variables plus a sixteen-point Walsh transform to one explicit scalar potential evaluation and the elementary entropy expression (3.2). It is independent of any finite search.

## 4. Exact point on the curve: the apparent dyadic maximizer is strongly safe

At \(s=1/4\) (or by symmetry \(3/4\)), the bias vector is

\[
(1/4,1/4,1/2,3/4),\qquad p_{\rm out}=1/2.
\]

The nonzero spectral masses are rational. Collecting them in denominator 256 gives numerators

\[
3,27,100,3,27,48,9,9,12,9,9,
\]

so

\[
\widetilde H
=\frac{51}{8}-\frac{75}{64}\log_2 3-\frac{25}{32}\log_2 5.
\tag{4.1}
\]

The influence vector is, up to the displayed orientation,

\[
\left(\frac9{32},\frac3{32},\frac58,\frac38\right),
\qquad
W=\frac3{32}.
\tag{4.2}
\]

Using the source-exact dyadic identity \(\Gamma_0(1/4)=C_0-2\), equation (3.5) becomes

\[
\boxed{
D_{\Gamma_0}
=\frac58C_0-\frac{51}{8}
+\frac{27}{64}\log_2 3
+\frac{25}{32}\log_2 5
}
\tag{4.3}
\]

and hence

\[
\boxed{
D_{\Gamma_0}
=0.1419123791224895983244831712665711645\ldots,
}
\]

\[
\boxed{
c_{B_0}=-1.5137320439732223821278204935100924216\ldots .}
\tag{4.4}
\]

This is not close to the positive two-input AND floor. Adding the stable lift only increases the defect:

\[
D_{\Gamma^\dagger}
=D_{\Gamma_0}+0.268204856\cdot\frac3{32}>0.
\]

## 5. Source-exact dyadic/mirror lattice certificate

To stress the same gate far beyond the single curve point without requiring interpolation of the stored candidate, define

\[
\mathcal P_{12}=\{1/2\}\cup
\{2^{-k},1-2^{-k}:2\le k\le12\}.
\]

I tested every bias tuple in \(\mathcal P_{12}^4\) whose output from (2.1) also satisfies

\[
\min(p_{\rm out},1-p_{\rm out})=2^{-m}
\]

for an integer \(m\). There are exactly **639** such tuples. At every input and output probability used in this finite test, \(\Gamma_0\) is source-exact from the AND-chain equality; no interpolation of the candidate array is used.

All biased Fourier coefficients, entropies, influences, defects and currencies were then enclosed with `mpmath.iv` at 60 decimal digits. Every one of the 639 sign decisions certified

\[
D_{\Gamma_0}>0,
\qquad
W>0.
\]

The smallest certified lower endpoint of \(D_{\Gamma_0}\) over the lattice is

\[
6.332282019167005\times10^{-6}>0.
\]

More importantly, the largest certified upper endpoint of the gate margin is

\[
\boxed{
\max_{\text{this certified lattice}}c_{B_0}
<-1.5137320439732223.
}
\tag{5.1}
\]

The maximizing symmetry orbit contains the point of Section 4. Therefore this entire source-exact dyadic/mirror lattice is not merely below the stable \(0.268204856\) lift; it asks for *no positive quadratic lift at all*. The owner's current positive AND floor is separated from this lattice by more than 1.5 units of margin.

This is a finite-lattice theorem, not an all-bias theorem. It must not be promoted to full \(B_0\) closure or full FEI.

Checker SHA-256:
`e2cf26f808b39fdf292dee3e6a71d5a7ec5dfb977e3012b2e0c38ef920f9d8b2`.

Captured output SHA-256:
`0a4266bdbf43cc7ad4a4e04e5350d32d2c08d5892cbce63e78cf7b622e613509`.

## 6. Refutation status and replacement obligation

**REFUTED ON THE CERTIFIED LATTICE:** the stronger adversarial hope that the handed-off prime gate \(B_0\), when pushed deep into asymmetric dyadic/mirror product biases while keeping all candidate evaluations source-exact, can exceed the AND margin. It cannot on any of the 639 certified tuples; in fact all have negative base margin.

**NOT REFUTED:** a genuinely non-dyadic interior bias for \(B_0\), another composition-prime gate, the universal AND-extremality conjecture, or FEI itself.

The replacement obligation is now narrower and source-valid. Use the exact one-variable formula (3.5) with the committed read-once candidate array and interval interpolation to prove or refute

\[
D_{\Gamma_0}^{B_0}(s)\ge0
\qquad(0<s<1)
\tag{6.1}
\]

on the entire asymmetric curve. If (6.1) is certified, move to a genuinely two- or four-dimensional non-dyadic deformation of \(B_0\) using the account04/B17 restriction cocycle, rather than repeating another dyadic battery. If (6.1) fails, preserve the first rigorous interval counterexample as the next adversarial witness and evaluate its actual \(c_G\) against the AND floor.

**Primary next recipient:** `account04/B17`, which owns the exact biased restriction-cocycle/B0 all-bias line.  
**Secondary integration recipient:** `account01/B18`, which owns the stable fixed candidate.

## 7. Exact old/new implication to full FEI

- **Exact candidate version attacked:** \(\Gamma^\dagger=\Gamma_0+0.268204856\,z(1-z)\), \(C^\dagger=6.521851214\), with the margin reported relative to \(\Gamma_0\), \(C_0=6.4548\).
- **Old first missing implication:** bound every composition-prime gate at every product bias by the AND extremal margin, or find a counterexample.
- **New proved mathematics:** exact scalar reduction (3.5) for a genuinely asymmetric one-parameter \(B_0\) family; exact negative margin (4.4) at its most dangerous certified dyadic point; and a 639-point interval certificate showing the full source-exact dyadic/mirror lattice has \(c_{B_0}<-1.5137320439732223\).
- **Remaining implication:** all non-dyadic biases of \(B_0\), then all other composition-prime gates/all arities.
- **Implication to full FEI:** useful elimination and dimensional reduction only. The universal quantifier remains open.

\[
\boxed{\text{Full Friedgut--Kalai FEI remains OPEN / NOT PROVED.}}
\]

## 8. Provenance and safety

The source mathematical snapshot was read from the current research branch before this run's writes, including the read-once certificate, all-gate reformulation, the account01/B18 fixed-candidate result and the account04/B17 restriction cocycle. The repository advanced concurrently through unrelated worker commits; this run used a unique immutable output directory and did not overwrite peer artifacts. No external model/API, workflow dispatch, email, Drive action, credentials, private non-mathematical data, scheduler mutation or public release was used. A narrow manual secret/privacy review found only mathematical constants, relative research paths and content hashes in the changed files.
