# PROB10-09 idea before new checker — complete and extend the central-surface route

Date: 2026-09-20 UTC.

Frozen parent remains the Benjamini–Schramm iid **bond**-percolation conjecture for every locally finite Cayley graph of every finitely generated nonamenable group: `p_c(G)<p_u(G)`. The parent is not claimed solved.

This run does **not** pretend the central-extension idea is new: an earlier unreported artifact, `2026-09-20T02-49-30Z_central_extension_magnetic_route_idea.md`, already proposed the genus-two graph and magnetic domination. The new goal is to (i) turn that candidate into a full written theorem, (ii) sharpen its exact genus-two constant by using the published `0.662816` bound itself rather than rounding to `0.663`, and (iii) prove an all-genus family theorem for every nonzero Euler class.

## Frozen family

For `g>=2` and `e in Z\{0}`, let

\[
E_{g,e}=\langle a_1,b_1,\ldots,a_g,b_g,z\mid z\text{ central},\ [a_1,b_1]\cdots[a_g,b_g]=z^e\rangle,
\]

viewed as the standard infinite-cyclic central extension

\[
1\to\langle z\rangle\cong\mathbb Z\to E_{g,e}\to\Gamma_g\to1
\]

of the closed genus-`g` surface group. Let `C_{g,e}` be the standard Cayley graph with generators `a_i^{\pm1},b_i^{\pm1},z^{\pm1}`. It is `(4g+2)`-regular. Since the quotient `Gamma_g` is nonamenable, `E_{g,e}` is nonamenable.

## Three routes compared

### A. Central Fourier / magnetic domination — pursue

Fourier transform in the central `Z` coordinate decomposes the horizontal adjacency into magnetic surface operators `H_theta`. Every magnetic edge coefficient has modulus one, so pointwise

\[
|H_\theta f|\le A_{\Gamma_g}|f|,
\]

hence `||H_theta||<=||A_{Gamma_g}||`. The two central edges become `2 cos(theta)`, giving

\[
\|A_{C_{g,e}}\|\le\|A_{\Gamma_g}\|+2
\]

uniformly in `e`. The negation test is exactly whether the cocycle twist can enlarge the norm; the pointwise domination rules that out.

For `g=2`, use the published rigorous Nagnibeda upper bound `||M_2||<=0.662816` exactly, not the earlier `0.663` relaxation. For `g>=3`, use Zuk's rigorous `||M_g||<=1/sqrt(g)`.

### B. Free-lift subgroup / exact fibre branching — pursue

Omit one surface generator. Freiheitssatz makes the corresponding subgroup in the quotient free of rank `2g-1`. Its chosen lifts together with the central generator form exactly `F_{2g-1} x Z`: a relation `w z^n=1` projects to a relation in the free subgroup, forcing `w` freely trivial, then `n=0` because `z` has infinite order. Hence

\[
T_{4g-2}\square\mathbb Z\subseteq C_{g,e}.
\]

For `g=2`, orient the `T_6` factor and use the exact `Z`-cluster activation probability

\[
\phi_Z(p)=1-\frac{(1-p)^3}{(1-p+p^2)^2}.
\]

At `p=31/200`, test `5 phi_Z(p)>1`; this gives a strict `p_c` upper bound.

For `g>=3`, the simpler embedded-tree bound `p_c<=1/(4g-3)` should already be enough when combined with Zuk.

### C. Current subgroup-relativization / known-class transfer — obstruction check, not a claimed proof

Before treating the family as a new special case, test whether current theorems already cover it. Hutchcroft--Pan 2024's advertised new amenable-`wq`-normal theorem assumes **exponential growth** of the amenable subgroup; the central `Z` here has linear growth. Choi--Seo 2025 covers acylindrically hyperbolic groups; these groups have infinite centre, while a non-elementary acylindrically hyperbolic group cannot have an infinite central subgroup. Peres's product theorem applies to Cartesian products, whereas `e!=0` is a non-split central extension. Juschenko--Nagnibeda gives existence of suitable generating sets under an infinite-normal/nonamenable-quotient hypothesis, not this frozen standard generating set. This is a bounded scope check only, not a worldwide novelty certificate.

## Target inequalities

For `g=2`, with Nagnibeda used exactly,

\[
R_2=8(0.662816)+2=\frac{114102}{15625}.
\]

For degree `D=10`, `Q=9`, the nonbacktracking root yields

\[
p_{2\to2}(C_{2,e})\ge
\frac{114102-\sqrt{4230203904}}{281250}
=0.174442603690045\ldots.
\]

Together with `p_c<31/200`, the intended uniform exact gap is

\[
p_u-p_c>
\frac{282033-4\sqrt{4230203904}}{1125000}
=0.019442603690045\ldots.
\]

For every `g>=3`, Zuk gives

\[
\|A_{C_{g,e}}\|\le4\sqrt g+2.
\]

The embedded tree gives `p_c<=1/(4g-3)`, while the nonbacktracking bound is strictly larger than `1/(4 sqrt(g)+2)`. It is enough to prove

\[
4\sqrt g+2<4g-3.
\]

After positive-side squaring this is `(4g-5)^2-16g>0`; it equals `1` at `g=3` and its forward difference is `32g-40>0` for all `g>=3`.

If the finite exact checks pass and the written operator/subgroup arguments survive review, the mechanism scope advances from an earlier genus-two idea-only artifact to a proved standard-Cayley family `C_{g,e}` for every `g>=2,e!=0`. This remains **PARTIAL** for the universal parent and is self-checked only.