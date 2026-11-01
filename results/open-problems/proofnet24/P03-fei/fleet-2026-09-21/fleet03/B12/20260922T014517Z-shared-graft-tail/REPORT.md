# fleet03/B12 — exact shared-graft tail theorem and a stronger FEI lower floor

**Outcome:** `ESSENTIAL_STEP_APPLIED / SCALAR-CAP_CANDIDATE_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**.

## 0. Live target, candidate version, and consumed peer result

The controlling natural-language owner instruction is the all-gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

with one symmetric nonnegative finite-cap potential. The source-exact equivalence with full FEI is
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`
(observed blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`).

The older read-once/AND-extremality candidate is already refuted. The exact successor attacked here is the
**shared-graft scalar-center tail candidate**: after the source-valid shared-graft sequence had reached the
certified fourth-round ratio \(R_4\), could one freeze the center cap there, or can the same Boolean construction
force a larger center again?

I consume substantively the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`,
report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

That theorem constructs an actual finite balanced monotone Boolean gadget at each round and proves the exact
recurrences below. I also use fleet03/B18's already certified \(R_4\) interval from
`fleet03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`,
blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`.

No arbitrary spectral law is introduced.

## 1. Why a balanced gate prices the center exactly

At uniform input biases, a balanced gate has \(p_i=p_{\rm out}=1/2\), \(V_{p_i}=1\), and
\(h(V_{p_i})=0\). Hence (G) becomes

\[
\Gamma(1/2)+H(G)\le I(G)\Gamma(1/2).
\]

Therefore every universal gate potential necessarily satisfies

\[
\boxed{\Gamma(1/2)\ge {H(G)\over I(G)-1}}
\tag{1.1}
\]

for every balanced non-affine Boolean gate. This is independent of the shape of \(\Gamma\) away from the center.

Relative to the historical read-once center \(C_0=6.4548\), the normalized quadratic margin of such a gate is

\[
c_G=4\left({H(G)\over I(G)-1}-C_0\right).
\tag{1.2}
\]

Thus a strict increase in the shared-graft ratio is a direct falsifier of a frozen scalar center, not an auxiliary
norm comparison.

## 2. Exact recurrence inherited from fleet01/B18

Let a balanced monotone gadget have entropy \(H\), influence \(I>1\),
\[
R={H\over I-1},
\]
and designated singleton Fourier coefficient \(c\). Take its fourth balanced self-composition and then apply the
same nine-host shared-core transform. With

\[
\alpha={9\over256},
\qquad
\phi(x)=-x\log_2x,
\]

the peer theorem gives

\[
I'={261\over128}+\alpha(I^4-1),
\tag{2.1}
\]

\[
c'={57\over256}+{c^4\over256},
\tag{2.2}
\]

and

\[
R'-R=
{K(c^4)-{133\over128}R\over
 {9\over256}I^4+{257\over256}},
\tag{2.3}
\]

where

\[
K(b)=H_{\rm core}(b)+{9\over256}
\left[-\phi(b^2)+16(1-b^2)\right],
\tag{2.4}
\]

\[
H_{\rm core}(b)=
\sum_{S\subseteq[9]}
\phi\!\left(
 \left[\widehat a(S)+b\sum_j\widehat Q_j(S)\right]^2
\right).
\tag{2.5}
\]

The normalizing \(512\) factors in (2.5) are those of the peer checker; the adjacent checker here reconstructs
the identical exact source arrays before evaluating the normalized coefficients.

The inherited certified fourth-round interval is

\[
\begin{aligned}
R_4\in[
&6.5218509485644448965490881329959858569477358114202361,\\
&6.5218509485644448965496895824490791318643557898359042].
\end{aligned}
\tag{2.6}
\]

The old missing implication was the tail question explicitly left by fleet03/B18: determine whether later
source-valid rounds keep increasing the lower envelope, rather than freezing another scalar lift at \(R_4\).

## 3. A small exact derivative lemma removes the huge-rational logarithm bottleneck

The peer source gives exact integer Walsh arrays \(A_j,Q_j\) for the nine-bit core. The checker reconstructs the
source-bound Numaro table, verifies SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

and then verifies

\[
\max_j|A_j|=114,\qquad
\max_j|Q_j|=18,\qquad
A_j=0\Longrightarrow Q_j=0,\qquad
\min_{A_j\ne0}|A_j|=2.
\tag{3.1}
\]

For \(b\in[0.0024,0.0025]\), write

\[
x_j(b)=\left({A_j+bQ_j\over512}\right)^2.
\]

If \(A_j\ne0\), then

\[
|A_j+bQ_j|\ge 2-{18\over400}={391\over200},
\]

so \(x_j>2^{-17}\). Also \(|A_j+bQ_j|<115\), and
\(1/\ln2<3/2\). Since

\[
\phi'(x)=\log_2(1/x)-{1\over\ln2},
\]

we may use \(|\phi'(x_j)|<37/2\). Moreover

\[
|x_j'(b)|\le {2\cdot18\cdot115\over512^2}.
\]

Summing over at most 512 terms gives

\[
|H_{\rm core}'(b)|<
{38295\over256}.
\tag{3.2}
\]

For the scalar correction in (2.4), \(b^2>2^{-18}\), so
\(|\phi'(b^2)|<39/2\), and its derivative has absolute value below

\[
{9\over256}{71\over400}.
\tag{3.3}
\]

Therefore, throughout the whole interval,

\[
\boxed{
|K'(b)|<
{15318639\over102400}
=149.596083984375<150.
}
\tag{3.4}
\]

This lets us evaluate \(K\) at a nearby modest-denominator dyadic and transfer the interval to the enormous exact
rational \(c_t^4\) without evaluating an enormous logarithm argument directly.

## 4. Two new finite Boolean rounds

Starting with the peer's exact
\[
c_1={14593\over65536},
\]
iterate (2.2). For the step \(F_4\to F_5\), evaluate \(K\) at the nearest \(2^{-50}\)-dyadic to \(c_4^4\).
The exact distance is below \(4.14\times10^{-16}\). Combining the rational logarithm enclosure there with (3.4)
gives

\[
{128\over133}K(c_4^4)
\in[
6.521851167347762883728066072662565363024803162295519471872653,
6.521851167347881910738220607081196362910021155709835480656530].
\tag{4.1}
\]

Substituting into the exact recurrence yields

\[
\boxed{
\begin{aligned}
R_5\in[
&6.521850949550445677603804527917030716029185560066064522017131,\\
&6.521850949550446214028876781337268672514139314941323193987472].
\end{aligned}}
\tag{4.2}
\]

In particular,

\[
R_{5,\rm lo}-R_{4,\rm hi}
>
9.8600078\times10^{-10}>0.
\tag{4.3}
\]

So freezing the scalar center at the certified \(R_4\) value is rigorously **REFUTED** by another actual finite
balanced Boolean gate.

Repeat once more. Using the nearest \(2^{-60}\)-dyadic to \(c_5^4\), whose exact distance is below
\(5.12\times10^{-20}\), gives

\[
{128\over133}K(c_5^4)
\in[
6.521851167347822389727000671364514383777891716471276886202631,
6.521851167347822404441751757589346408025574635481084173163533],
\tag{4.4}
\]

and therefore

\[
\boxed{
\begin{aligned}
R_6\in[
&6.5218509495504479166285700997599368621033431952391529352289380595007740,\\
&6.5218509495504484530536480190689720962455099423761306325859523377918521].
\end{aligned}}
\tag{4.5}
\]

The second new gain is still rigorously positive:

\[
R_{6,\rm lo}-R_{5,\rm hi}
>
1.70259969\times10^{-15}.
\tag{4.6}
\]

Because every \(F_t\) is an actual finite balanced Boolean gate by the consumed peer construction, balanced
self-composition gives

\[
\boxed{
C_{\rm FEI}\ge
6.5218509495504479166285700997599368621033431952391529352289380595007740.
}
\tag{4.7}
\]

Relative to \(C_0=6.4548\), the new finite gate forces

\[
\boxed{
c_{F_6}>
0.2682037982017916665142803990397474484133727809566117409157522380030960.}
\tag{4.8}
\]

Full FEI is still open; (4.7) is a lower bound, not a universal upper bound.

## 5. The tail no longer needs round-by-round certification

There is also a genuinely new infinite-tail statement. The singleton recurrence
\[
F(c)={57\over256}+{c^4\over256}
\]
has
\[
F'(c)={c^3\over64}< {1\over5000}
\quad\text{for }c\le0.223.
\tag{5.1}
\]

The exact values satisfy \(c_5>c_6\), so all later \(c_t\) decrease and lie within a geometric tail of \(c_5\).
Using (3.4) over that entire tail gives the uniform lower bound

\[
\boxed{
{128\over133}K(c_t^4)>
6.5218511673478223896951587198472353679409275430275523293089316853421847
\quad(t\ge6).
}
\tag{5.2}
\]

On the influence side, the exact recurrence has \(I_6>10^8\), and thereafter
\(I_{t+1}>I_t^2\). Since \(K<7\) on the same tail, the sum of **all possible future positive increments** after
\(R_6\) is below

\[
{14\over10^{16}-1}
=
1.40000000000000014\ldots\times10^{-15}.
\tag{5.3}
\]

Consequently every later \(R_t\) remains far below the threshold (5.2), so the numerator in (2.3) stays positive.
Thus:

\[
\boxed{R_6<R_7<R_8<\cdots}
\tag{5.4}
\]

and the limit exists in the fully rigorous interval

\[
\boxed{
\begin{aligned}
R_\infty\in[
&6.5218509495504479166285700997599368621033431952391529352289380595007740,\\
&6.5218509495504498530536480190691120962455099423901306325859523391918521].
\end{aligned}}
\tag{5.5}
\]

This closes the specific tail theorem requested by the previous B lead: no further giant-rational rounds are
needed to know the sign, and the shared-graft lower envelope is pinned to an interval of width below
\(2\times10^{-15}\).

## 6. Refutation attempt, status, and next obligation

**Exact candidate version attempted:** `GATE-SHARED-GRAFT-TAIL-v1`, meaning the all-gate reformulation at source
blob `1c0596...`, with the fleet01/B18 shared-graft recurrence at blob `cbe682...` and the inherited certified
\(R_4\) interval at blob `4d1e86...`.

**Prior missing implication:** determine whether the scalar center could be frozen at \(R_4\), or whether the same
source-valid Boolean mechanism keeps increasing the necessary center.

**New proved inference:** it keeps increasing. \(F_5\) and \(F_6\) give two strict certified gains, and the exact
derivative/contraction argument proves every later round is also increasing and pins the limiting lower envelope
to (5.5).

**Exact failed claim:** “the minimal scalar center can be frozen at \(R_4\)” is **REFUTED**.

**Replacement obligation:** any universal potential satisfying (G) must have
\(\Gamma(1/2)\ge R_\infty\) at least at the precision in (5.5), and must still satisfy (G) for every gate and every
product bias. The lower-bound family does not supply that universal upper-bound potential.

**Next recipient:** `fleet03/B18` (B lead). The next implication to full FEI is to build/test a replacement
finite-cap gate potential with center at least this rigorous shared-graft envelope, then prove its slack on every
composition-prime gate and every product bias (or produce the next genuine Boolean obstruction). The
fleet02/B17 composition cocycle remains the natural reduction for that step.

**Classification:** `ESSENTIAL_STEP_APPLIED` for the tail theorem and stronger source-valid lower floor;
`CANDIDATE_REFUTED` for freezing the scalar lift at \(R_4\). **Full FEI remains OPEN / NOT PROVED.**

## 7. Reproducibility

`CHECKER.py` reconstructs the exact source table and core Walsh arrays, verifies the source hash and coefficient
bounds, proves the derivative constant (3.4), iterates the exact rational \(c\)- and \(I\)-recurrences, evaluates
\(K\) at nearby dyadics using rational atanh-series logarithm enclosures, transfers them with (3.4), checks both
strict new gains, and proves the tail estimate (5.5).

Checker SHA-256: `8e9ff6902efcdbb5c8f2c4ac22ea9298ca2b2fd14f534f194006b40aee665c97`.  
Captured output SHA-256: `62ccb3c6712f5d177ee7c46294941d3c932ae0f71b40aff43014f4e63294df09`.

No novelty or publication-priority claim is made.
