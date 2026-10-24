SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T01:13:27Z.
attacking: the r45 null-puncture overlap: prove a same-bank product-provenance L^m hyperbolic receiver that retains the entire residual quadratic phase, then identify exactly what third-curvature gain is still missing.

# account03/B11 r46 — same-bank hyperbolic L^m receiver through the null puncture

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW SUPPORTING THEOREM / r45 OVERLAP L2 GAP CLOSED / PARTNER RESULT APPLIED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This report proves a product-preserving analytic estimate for the exact-rank-three null-puncture model from B11 r45. It does not prove an `L^infinity` bound for the punctured branch, does not absorb arbitrary additional nonseparable spectrum, and does not prove full-target continuity.

No moments, compact support, connected support, Gaussianity, log-concavity, post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint coarea theorem, conditional projection-height moment, or deletion of a small nonzero coefficient is used.

## 1. Sources and exact first unpaid implication

Immediate predecessor:

`yspennstate/math-open-problems@12e2174445fbc824279bf1376da1346454d7060a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T002432Z-account03-B11-QFORM-r45/REPORT.md`.

There, for exact rank three
\[
A=RMR^T,\qquad R^TR=I_3,\qquad s=\min|\lambda(M)|,
\]
an original physical coordinate `i` with leverage `q=||r_i||^2`, `0<q<1`, and exact null pivot `A_ii=0` is put into the product-valid normal form
\[
Q=2\kappa\sqrt q\,H W+
  2\kappa\sqrt{1-q}\,T W+
  c(V')^2+\delta W^2,                                      \tag{1.1}
\]
where `H=X_i` is genuinely independent of the whole residual original-coordinate product bank, `(T,W,V)` is an orthonormal three-dimensional projection of that residual product source, and
\[
\kappa^2|c|=|\det M|\ge s^3,\qquad \kappa\ge s.             \tag{1.2}
\]
The residual triple is generally dependent internally. The small puncture term `TW` may not be dropped.

A compatible account02/B11 follow-up explicitly identified the missing interface as a product-provenance analogue of its hyperbolic-pair `L^2` estimate: the ambient three-dimensional density cap alone is insufficient.

The designated account04/B11 theorem used below is

`yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T111608Z-account04-B11-disjoint-volume-compiler-r5/REPORT.md`,

whose pair-area receiver gives
\[
\|p_Q\|_\infty\le {128\sqrt2\over s\sqrt{g_{ij}}},
\qquad g_{ij}=\|r_i\wedge r_j\|^2.                           \tag{1.3}
\]

## 2. A same-bank hyperbolic `L^m` theorem

The useful point is that the hyperbolic `L^2` mechanism does not actually require the coefficient variable and the residual phase to come from independent sources. Only the physical scalar being multiplied by that coefficient must be independent.

### Theorem 2.1 — `QFORM-PRODUCT-BANK-HYPERBOLIC-LM-v1`

Let `H` be a real random variable with probability density `f_H` satisfying
\[
\|f_H\|_\infty\le F.
\]
Let `Y` be an arbitrary random object independent of `H`. Let `U=U(Y)` be a real-valued function of `Y` whose marginal law has a density bounded by
\[
\|p_U\|_\infty\le G.
\]
Let `Psi(Y)` be an arbitrary measurable real-valued function of the SAME source `Y`; no independence between `U` and `Psi` is assumed. For real `c!=0,d`, define
\[
Z=(cU+d)H+\Psi(Y).                                           \tag{2.1}
\]
Then `Z` has a probability density `p_Z`. For every integer `m>=2`,
\[
\boxed{\;
\|p_Z\|_m^m
\le m!\left({2FG\over |c|}\right)^{m-1}.
\;}                                                         \tag{2.2}
\]
Equivalently,
\[
\boxed{\;
\|p_Z\|_m
\le (m!)^{1/m}
\left({2FG\over |c|}\right)^{1-1/m}.
\;}                                                         \tag{2.3}
\]

In particular
\[
\boxed{\;
\|p_Z\|_2^2\le {4FG\over |c|}.
\;}                                                         \tag{2.4}
\]
This is exactly the account02/B11 hyperbolic `L^2` constant, but now `Psi` may depend arbitrarily on the same bank as `U`.

### Proof

Set
\[
a(Y)=cU(Y)+d,\qquad r(Y)=\Psi(Y).
\]
Because `U` has a density and `c!=0`,
\[
P\{a(Y)=0\}=0.
\]
Conditioning on `Y=y`, the conditional law of `Z` has density
\[
k_y(z)={1\over |a(y)|}
 f_H\!\left({z-r(y)\over a(y)}\right).                       \tag{2.5}
\]
Thus
\[
p_Z(z)=E\,k_Y(z)
\]
is a probability density.

Take iid copies `Y_1,...,Y_m`. Tonelli gives
\[
\|p_Z\|_m^m
=
E\int_{\mathbb R}\prod_{j=1}^m k_{Y_j}(z)\,dz.               \tag{2.6}
\]
For fixed copies, order the absolute scales:
\[
S_1\le S_2\le\cdots\le S_m,
\qquad
\{S_j\}_{j=1}^m=\{|a(Y_j)|\}_{j=1}^m.
\]
The kernel having scale `S_1` is a probability density, while every other kernel obeys
\[
\|k_{Y_j}\|_\infty\le {F\over |a(Y_j)|}.
\]
Hence, independently of all translations `r(Y_j)`,
\[
\int\prod_{j=1}^m k_{Y_j}(z)\,dz
\le {F^{m-1}\over S_2S_3\cdots S_m}.                         \tag{2.7}
\]

Now put
\[
K={G\over |c|}.
\]
The scalar `A=cU+d` has density cap at most `K`, so for `R=|A|`,
\[
P\{R\le t\}\le \min(1,2Kt).                                  \tag{2.8}
\]
Thus `R` stochastically dominates `V/(2K)`, where `V` is `Uniform[0,1]`. The function
\[
(r_1,\ldots,r_m)\mapsto
{1\over \text{product of the largest }m-1\text{ coordinates}}
\]
is coordinatewise decreasing. Therefore, for iid copies and their order statistics,
\[
E{1\over S_2\cdots S_m}
\le (2K)^{m-1}
 E{1\over V_{(2)}\cdots V_{(m)}}.                             \tag{2.9}
\]

For iid `Uniform[0,1]` variables the ordered joint density is `m!` on
\[
0<v_1<\cdots<v_m<1.
\]
Consequently
\[
\begin{aligned}
E{1\over V_{(2)}\cdots V_{(m)}}
&=m!\int_{0<v_1<\cdots<v_m<1}
 {dv_1\cdots dv_m\over v_2\cdots v_m}\\
&=m!.                                                        \tag{2.10}
\end{aligned}
\]
Indeed the `v_1` integration contributes the factor `v_2` and cancels the first denominator; the same cancellation repeats successively.

Combining (2.6)--(2.10) proves
\[
\|p_Z\|_m^m
\le F^{m-1}m!(2K)^{m-1}
=m!\left({2FG\over|c|}\right)^{m-1}.
\]
QED.

### Endpoint sharpness in order

For independent unit uniforms `H,U` on `[0,1]`, `c=1,d=0,Psi=0`,
\[
p_{HU}(z)=-\log z,\qquad 0<z<1,
\]
and
\[
\int_0^1(-\log z)^m\,dz=m!.
\]
Thus factorial `L^m` growth is the genuine rank-two logarithmic endpoint. The theorem is not hiding an `L^infinity` estimate.

## 3. Direct application to the r45 puncture

Return to (1.1). Take
\[
Y=X_{-i},\qquad U=W,\qquad H=X_i,
\]
and absorb EVERYTHING else into
\[
\Psi(Y)=
2\kappa\sqrt{1-q}\,TW+c(V')^2+\delta W^2.                   \tag{3.1}
\]
No overlap term is removed. No conditional density of `(T,V,W)` is invoked.

Because `W` is a normalized one-dimensional linear form of the residual independent cap-one coordinates, the standard one-dimensional product-projection theorem gives
\[
G\le\sqrt2.                                                  \tag{3.2}
\]
The coefficient multiplying `UH` is
\[
c_{\rm hyp}=2\kappa\sqrt q.
\]
With `F=1`, Theorem 2.1 yields, for every integer `m>=2`,
\[
\boxed{\;
\|p_Q\|_m^m
\le m!\left({\sqrt2\over\kappa\sqrt q}\right)^{m-1}
\le
m!\left({\sqrt2\over s\sqrt q}\right)^{m-1}.
\;}                                                         \tag{3.3}
\]
This estimate is UNIFORM through the puncture `q->1` and retains the same-bank term
`2 kappa sqrt(1-q) T W` exactly.

At the live near-coloop threshold `q>=63/64`,
\[
{\sqrt2\over s\sqrt q}
\le {8\sqrt2\over s\sqrt{63}}
={1.4253932901995967\ldots\over s}.                         \tag{3.4}
\]
In particular,
\[
\boxed{\;
\|p_Q\|_2^2
\le {16\sqrt2\over \sqrt{63}}\;s^{-1}
=2.8507865803991934\ldots\,s^{-1},
\;}                                                         \tag{3.5}
\]
and
\[
\boxed{\;
\|p_Q\|_2
\le1.6884272505498108\ldots\,s^{-1/2}.
\;}                                                         \tag{3.6}
\]

For reference, the near-coloop constants in
\[
\|p_Q\|_m\le C_m s^{-1+1/m}
\]
are
\[
\begin{array}{c|cccccc}
m&2&3&4&6&8&10\\
\hline
C_m&
1.688427&
2.301478&
2.887379&
4.022546&
5.133138&
6.230423
\end{array}
\]
and grow linearly in `m`, exactly as expected for a logarithmic singularity.

### Linear-times-log small ball consequence

Let
\[
x={2FG\over|c|}|I|.
\]
For `0<x<=e^{-2}`, choose
\[
m=\left\lceil\log{1\over x}\right\rceil.
\]
By Holder, (2.3), `m!^{1/m}<=m`, and `x^{-1/m}<=e`,
\[
\boxed{\;
P\{Z\in I\}
\le
e\left(1+\log{1\over x}\right)x.
\;}                                                         \tag{3.7}
\]
For the r45 puncture this gives a source-valid quantitative `epsilon log(1/epsilon)` estimate uniform as `q->1`, with the whole residual quadratic phase retained.

This does not yet reach the required linear `C epsilon` law. It proves something more diagnostic: the same-bank overlap does NOT create an obstruction worse than the known opposite-sign rank-two logarithm.

## 4. Designated account04/B11 result applied at an actual inequality

The partner pair-area theorem (1.3) applies to the large-leaf exit used in the current near-coloop geometry. For the heavy physical hub `i=0` and residual transverse row `w_j`,
\[
g_{0j}=q\|w_j\|^2.
\]
If
\[
q\ge{63\over64},
\qquad
\|w_j\|^2\ge{1\over36},
\]
then
\[
g_{0j}\ge {63\over64}{1\over36}={7\over256}.
\]
Substituting this actual lower bound into the completed account04/B11 receiver gives
\[
\boxed{\;
\|p_Q\|_\infty
\le {128\sqrt2\over s\sqrt{7/256}}
=
{2048\sqrt{2/7}\over s}
=
{1094.7020468732903\ldots\over s}.
\;}                                                         \tag{4.1}
\]
Thus the r46 `L^m` puncture estimate is needed only after this already-paid physical pair-area exit is removed.

For comparison, at the exact separated endpoint `q=1`, the earlier account04/B11 null-scalar theorem and (1.2) give
\[
\|p_Q\|_\infty
\le 3\,2^{2/3}e^{2/3}|\det M|^{-1/3}
\le {9.275505197173393\ldots\over s}.                        \tag{4.2}
\]

## 5. What this says about the third direction

The mandatory rank-two control remains
\[
p_{2XY}(t)=\log{1\over2|t|},
\qquad 0<|t|<1/2,
\]
for independent centered unit uniforms. Theorem 2.1 shows that this logarithmic endpoint is stable under an arbitrary same-bank measurable phase: even the full r45 residual phase cannot make the output worse than factorial `L^m` growth / `epsilon log(1/epsilon)` small-ball behavior.

Therefore the precise remaining job of the THIRD direction in (1.1) is now isolated. The coefficient identity
\[
\kappa^2|c|=|\det M|\ge s^3
\]
guarantees that the transverse square `c(V')^2` is quantitatively tied to the hyperbolic coupling. At `q=1`, the account04/B11 theorem spends that square to convert the logarithmic `1/|W|` endpoint into the integrable `|W|^{-1/2}` kernel and obtains a bounded density. For `q<1`, the only unresolved step is to spend the same square while preserving the residual product provenance in the presence of the internally dependent `TW` overlap.

The overlap-L2 question itself is no longer the bottleneck.

## 6. Exact next implication

The next B11 target is

`QFORM-PUNCTURE-LM-TO-LINFINITY-THIRDSQUARE-v1`:

> In the r45 normal form (1.1), combine the uniform same-bank `L^m` estimate (3.3) with the determinant-tied third square `c(V')^2`, using the fact that `(T,W,V)` is an orthonormal projection of the residual original product source, to replace the factorial/linear-in-m growth by a uniform `L^infinity` bound. Equivalently, prove that the third-square averaging removes the final logarithm without conditioning away the product provenance.

A valid proof may use a product-source Brascamp--Lieb/Fresnel estimate before the `(T,V,W)` pushforward, or force a source-disjoint physical recut paid by an existing pair/cross-volume receiver. It may not replace the triple by an arbitrary joint density cap, invoke a positive conditional-density moment, or delete the `TW` term.

Arbitrary additional nonseparable spectrum remains a separate bridge to the full owner target. This run proves existence of an `L^m` density for every finite `m>=2` in its puncture scope; it does not prove continuity there.

## 7. Verification

`VERIFY.py` checks:
- the exact near-coloop constants in (3.4)--(3.6);
- the displayed `C_m` values;
- the account04/B11 pair-area substitution (4.1);
- the separated null-scalar constant (4.2);
- 24,000 deterministic random interval-kernel regressions of the fixed-copy inequality (2.7), for `m=2,...,7`.

The regression uses unit interval densities under arbitrary signed scales and arbitrary translations; the largest observed ratio of the exact overlap integral to the right side of (2.7) is `1.0000000000003`, i.e. equality up to floating-point roundoff. It is a check of the algebra, not a replacement for the proof.

The output terminates:

`QFORM_B11_R46_BANK_HYPERBOLIC_LM_CHECK_PASS`.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
