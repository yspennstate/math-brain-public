# fleet03/B18 — two further recursive shared-graft steps raise the FEI lower floor

**Run:** `20260922T011005Z-B18-fei-gate-extremal`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` and `CANDIDATE_REFUTED` for freezing the scalar gate lift at either of the two preceding certified balanced caps.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository sources were read directly, but no authenticated installed cognitive/mathematical-brain retrieval was used.

## 0. Version and exact live implication

The latest owner control converges FEI work to the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_u=4u(1-u),
\tag{G}
\]

and asks either for a proof of decomposable/AND extremality or a genuine Boolean gate requiring a larger normalized margin. The older small-arity measurements are not the current extremal picture: completed cross-account work has now produced balanced Boolean gates whose margin is much larger than the two-input AND margin.

The exact successor attacked in this report is the natural **minimal re-lift** after the newest completed balanced obstruction: if one raises the centre of the scalar-lift gate potential only to the latest certified balanced ratio, does the same candidate survive the next source-valid shared-coordinate construction? The answer is no, twice in succession.

## 1. Named cross-account result consumed substantively

The main peer input is fleet01/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`,
commit `b9b63c908139fcd280a4913229afd7ab62ca50aa`, report blob
`cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

That report starts from the validated 18-bit balanced monotone Numaro gate and the previously constructed 162-input shared-core gate. It proves that the shared-core transform can be applied to **any balanced monotone gadget with a chosen singleton coefficient**, and constructs a new balanced Boolean gate `F_2` with

\[
R_2:=\frac{H(F_2)}{I(F_2)-1}
>
6.521850763518463531668608228451477683404661344\ldots .
\tag{1.1}
\]

It also proves the exact recurrence needed below. If a balanced monotone gadget `f` has entropy `H`, influence `I>1`, excess ratio

\[
R=\frac{H}{I-1},
\]

and a designated singleton Fourier coefficient `c`, first take the fourth balanced self-composition of `f` and then apply the same nine-host shared-core transform. With

\[
\alpha=\frac9{256},\qquad
\phi(x)=-x\log_2x,
\]

and the fixed source core functional

\[
H_{\rm core}(b)=
\sum_{S\subseteq[9]}
\phi\!\left(\left[\widehat a(S)+b\sum_j\widehat Q_j(S)\right]^2\right),
\tag{1.2}
\]

the transformed gadget has

\[
\boxed{
I'=\frac{261}{128}+\alpha(I^4-1),
}
\tag{1.3}
\]

\[
\boxed{
H'=H_{\rm core}(c^4)
+\alpha\left[
H\frac{I^4-1}{I-1}-\phi(c^8)+16(1-c^8)
\right],
}
\tag{1.4}
\]

and the designated singleton for the next round is

\[
\boxed{
c'=\frac{57}{256}+\frac{c^4}{256}.}
\tag{1.5}
\]

The peer also proves the equivalent ratio increment identity

\[
R'-R=
\frac{K(c^4)-\frac{133}{128}R}
     {\frac9{256}I^4+\frac{257}{256}},
\qquad
K(b)=H_{\rm core}(b)+\frac9{256}
[-\phi(b^2)+16(1-b^2)].
\tag{1.6}
\]

The second cross-account input is fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`.

It proves for every symmetric potential that both gate slack and the Poincare margin currency obey the same nonnegative disjoint-composition cocycle. Hence a gate with normalized margin above a proposed threshold has a composition-prime factor with at least that margin. This is used below to show that the new obstruction cannot be dismissed merely by restricting a re-lift to prime gates.

## 2. New construction: `F_3` and `F_4`

Let `F_1` be the first shared-core gate in the peer construction. The source gives exactly

\[
I_1=\frac{68013}{32768},
\qquad
c_1=\frac{14593}{65536}.
\tag{2.1}
\]

The peer constructs

\[
F_2=T(F_1^{\circ4},c_1^4).
\]

This report continues **the same source-valid transformation**, without changing the mechanism or replacing the Boolean source by an arbitrary spectral law:

\[
F_3:=T(F_2^{\circ4},c_2^4),
\qquad
F_4:=T(F_3^{\circ4},c_3^4),
\tag{2.2}
\]

where the singleton recurrence (1.5) gives

\[
\begin{aligned}
c_2&=0.2226658532590027729602990934224329699909\ldots,\\
c_3&=0.2226658522834051108729250953420650114555\ldots,\\
c_4&=0.2226658522832368234585407797301598223079\ldots .
\end{aligned}
\tag{2.3}
\]

Balanced monotonicity is preserved by balanced self-composition and by the peer's shared-core transform, so `F_3` and `F_4` are genuine finite balanced monotone Boolean functions. No giant truth table is assumed or sampled.

Their influences are determined exactly by (1.3). In particular

\[
I_2=
\frac{784028312243315011737}{295147905179352825856}
=2.65639124820108\ldots,
\tag{2.4}
\]

\[
I_3=
\frac{7293635508681408439604535567475568379907630049888658770829188246173012479808017893097}
{1942668892225729070919461906823518906642406839052139521251812409738904285205208498176}
=3.754440881752649\ldots,
\tag{2.5}
\]

and

\[
I_4=8.989183126916552511946952686220\ldots .
\tag{2.6}
\]

## 3. Certified strict ratio gains

The adjacent extension checker reconstructs the peer's validated source truth table and refuses it unless its full SHA-256 is the inherited expected value. It then recomputes the nine-bit core Walsh data and evaluates every logarithm with exact `Fraction` arithmetic using the identity

\[
\log x=2\sum_{j=0}^{N-1}
\frac{z^{2j+1}}{2j+1}+\mathcal R_N,
\qquad
z=\frac{x-1}{x+1},
\]

with the explicit remainder enclosure

\[
0\le \mathcal R_N
\le
\frac{2z^{2N+1}}{(2N+1)(1-z^2)}
\]

after dyadic range reduction to `1<=x<=2`. Twenty terms are already far more accurate than needed for the signs below; the resulting ratio intervals have width below `6.1e-22`.

It obtains

\[
\begin{aligned}
R_2&\in[
6.5218507635184635316685893234363436695035260370806896,\\
&\hspace{2.25cm}
6.5218507635184635316691901626179398857683143881788648],
\end{aligned}
\tag{3.1}
\]

then, for the new third-round gate,

\[
\boxed{
\begin{aligned}
R_3&\in[
6.5218509158557171794336583919648574196767563718341573,\\
&\hspace{2.25cm}
6.5218509158557171794342597335463471829453334335276482].
\end{aligned}}
\tag{3.2}
\]

The interval comparison is exact-rational and gives

\[
\boxed{
R_{3,\rm lo}-R_{2,\rm hi}
>
1.5233725364776446\times10^{-7}
>
1.52\times10^{-7}.}
\tag{3.3}
\]

Applying the transform once more gives

\[
\boxed{
\begin{aligned}
R_4&\in[
6.5218509485644448965490881329959858569477358114202361,\\
&\hspace{2.25cm}
6.5218509485644448965496895824490791318643557898359042].
\end{aligned}}
\tag{3.4}
\]

and again an exact-rational strict gain,

\[
\boxed{
R_{4,\rm lo}-R_{3,\rm hi}
>
3.2708727717114828\times10^{-8}
>
3.27\times10^{-8}.}
\tag{3.5}
\]

Relative to the peer's `F_2` interval, the two new rounds yield

\[
\boxed{
R_{4,\rm lo}-R_{2,\rm hi}
>
1.8504598136487989\times10^{-7}
>
1.85\times10^{-7}.}
\tag{3.6}
\]

This is not floating-point evidence: each displayed strict inequality is decided between exact rational interval endpoints.

## 4. New FEI lower bound and the gate-margin consequence

For every balanced Boolean gate `F`, ordinary balanced disjoint self-composition satisfies

\[
I(F^{\circ d})=I(F)^d,
\qquad
H(F^{\circ d})=H(F)\frac{I(F)^d-1}{I(F)-1}.
\tag{4.1}
\]

Therefore

\[
\frac{H(F^{\circ d})}{I(F^{\circ d})}
\longrightarrow
\frac{H(F)}{I(F)-1}.
\tag{4.2}
\]

Applying this to the actual finite balanced Boolean gate `F_4` proves the source-valid lower bound

\[
\boxed{
C_{\rm FEI}
>
6.5218509485644448965490881329959858569477358114202360.}
\tag{4.3}
\]

This is a lower bound, not a finite upper bound and not a proof of FEI.

At the uniform bias point every balanced gate has, relative to the old read-once centre `C_0=6.4548`,

\[
c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\tag{4.4}
\]

Thus `F_4` forces

\[
\boxed{
c_{F_4}>
0.2682037942577795861963525319839434277909432456809443.}
\tag{4.5}
\]

This is more than sixty times the old two-input AND margin `0.0043974201`; decomposable/AND extremality for the original read-once potential is therefore not just numerically inaccurate but decisively refuted by a source-valid gate family.

If one instead anchors at the rigorously proved read-once cap `6.4573`, any purely quadratic centre lift must have coefficient at least

\[
\boxed{
\lambda>
0.2582037942577795861963525319839434277909432456809443.}
\tag{4.6}
\]

on the balanced slice.

Finally apply the consumed fleet02/B17 composition cocycle. If `F_4` is functionally decomposable into disjoint gate factors, its normalized required margin is a convex average of the factor margins at the induced biases. Hence **some composition-prime factor has margin at least (4.5)**. Restricting a scalar lift to prime gates therefore does not rescue any cap below (4.3).

## 5. Exact refutation attempt and what remains unpaid

A tempting extrapolation is that the shared-core recurrence raises the lower bound monotonically forever. I did **not** promote that extrapolation. The exact recurrence (1.6) makes the sign of each later gain depend on the comparison

\[
R_t<\frac{128}{133}K(c_t^4),
\tag{5.1}
\]

and this report certifies (5.1) only through the two new rounds needed for `F_3` and `F_4`. The singleton coefficients are rapidly converging, while the influence recurrence grows quartically; a later proof should exploit this to control the entire tail rather than certify one huge rational round at a time.

**Old missing implication.** After the previous lower-bound construction, prove the minimally re-lifted `PRIME-GATE-LIFT` inequality at a fixed centre cap.

**New proved inference.** The same genuine Boolean shared-coordinate mechanism can be applied twice more, and each application strictly increases the balanced excess ratio. Hence freezing the scalar lift at the previous `F_2` cap, or at the intermediate `F_3` cap, is false. Any valid all-gate potential must have centre at least (4.3).

**Replacement obligations.** Either:

1. analyze the recurrence (1.3)--(1.6) as an infinite source-valid family and determine a rigorous limiting lower envelope before fixing another scalar cap; and then prove an all-prime/all-bias gate inequality above that envelope, or
2. abandon the one-parameter scalar lift and construct a different finite-cap potential whose gate slack survives this shared-coordinate interference.

The next mathematically sharp inference is a tail theorem for (1.6): prove a uniform interval containing all later `c_t`, obtain a rigorous lower bound on `(128/133)K(c_t^4)`, and show that the total future positive increments remain below that barrier while still giving an explicit improved limiting FEI lower bound.

**Next recipients:** fleet01/B18 (owner of the shared-graft recurrence), fleet02/B17 (prime-gate cocycle/adversary reduction), and the Campaign-B gate builders. They should not freeze a new centre at `R_2` or `R_3`.

No publication-priority or novelty claim is made. Full unrestricted FEI remains **OPEN / NOT PROVED**.
