# B17 — asymmetric quarter-bias dyadic interior slice for the live FEI gate candidate

**Run:** `20260922T040248Z-B17-r11`  
**Account/slot:** `fleet03/B17`  
**Outcome:** `AUXILIARY_ONLY / DIRECT_SLICE_EXCLUSION`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Change summary and exact live target

The latest owner control supersedes the older interface-specific assignment and directs all FEI workers to converge on the all-gate inequality.  For a symmetric potential `Gamma`, define

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p).
\tag{0.1}
\]

The source gate-reformulation proves that one symmetric nonnegative `Gamma` with finite
`Gamma(1/2)` and `D_Gamma>=0` for every Boolean gate, every arity and every product bias
implies full FEI.  The current scalar-lift candidate is

\[
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\qquad
a_*=0.2682048,\qquad
\Gamma_*(1/2)=C_*=6.5218512.
\tag{0.2}
\]

This run does **not** repeat the earlier all-fair five-input balanced/quarter-output sweeps.
It attacks the first genuinely asymmetric interior cross-section left open by the peer
boundary theorem: one input has bias `1/4`, four are fair, and the gate is otherwise
arbitrary.

The result is a computer-assisted theorem for that exact cross-section.  Every five-input
gate in the specified dyadic-output slice already satisfies the **unlifted** read-once-base
inequality `D_{Gamma_RO}>=0`; every non-subcube gate has a strict gap.  Therefore no gate in
this slice can falsify the live lift.

This is a finite-arity slice theorem, not a proof of the universal all-gate implication.

## 1. Peer result consumed and applied

The completed cross-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B13/20260922T033410Z-local-boundary-repulsion/REPORT.md`

at blob `1734d9c369048def5488adf228dc03e433af3216`.

It uses the exact restriction-margin cocycle from fleet04/B17 and proves that any
violation of `LIMIT-PRIME-GATE-LIFT-v1` must contain a **genuinely two-sided interior**
positive-currency gluing.  For a pivot of bias `t`, restriction-output masses `r_0,r_1`,
disagreement `delta`, and `Delta=r_1-r_0`, the local quadratic currency is

\[
\mathcal W=t(1-t)(\delta-\Delta^2)\ge0,
\tag{1.1}
\]

and genuinely two-sided gluings satisfy `c_loc(t)->-infinity` as `t->0` or `1`; one-sided
constant-child cases reduce to the already-certified binary AND/OR inequality.

**Application here.**  I move deliberately away from the boundary to the exact interior
pivot `t=1/4` and exhaust an asymmetric sparse-output cross-section.  Thus this is not a
repeat of the peer's boundary argument: it attacks the interior class that theorem leaves
as the only possible threat.

## 2. Exact asymmetric slice

Let `G` have five Boolean inputs.  The first input has true-probability

\[
p_0={1\over4},
\]

and the remaining four have bias `1/2`.  Write `A,B subseteq Q_4` for the true (`-1`) sets
of the two physical restrictions at input 0, with

\[
a=|A|,\qquad b=|B|.
\]

Then the gate output mass is exactly

\[
r=p_{\rm out}={3a+b\over64}.
\tag{2.1}
\]

This run exhausts every gate for which

\[
r\in\left\{
{1\over64},{1\over32},{1\over16},{1\over8},{1\over4}
\right\}.
\tag{2.2}
\]

The corresponding `(a,b)` classes are

\[
\begin{array}{c|l}
64r & (a,b)\\ \hline
1 &(0,1)\\
2 &(0,2)\\
4 &(0,4),(1,1)\\
8 &(0,8),(1,5),(2,2)\\
16&(0,16),(1,13),(2,10),(3,7),(4,4),(5,1).
\end{array}
\tag{2.3}
\]

Their total number of truth tables is

\[
\boxed{10,857,979}.
\tag{2.4}
\]

Input negation transfers the same conclusion to `p_0=3/4`, and output negation transfers it
to the mirrored high-output masses, because the live potentials are symmetric and the gate
data transform by the standard NPN symmetries.

## 3. Exact spectral reduction: no candidate NPZ is needed

Let

\[
u_T=\sum_{y\in Q_4} f_A(y)\chi_T(y),
\qquad
v_T=\sum_{y\in Q_4} f_B(y)\chi_T(y),
\]

be the **unnormalised integer** Walsh sums of the two four-bit restrictions.  Directly from
the normalized biased basis at `p_0=1/4`,

\[
\widehat G(T)={3u_T+v_T\over64},
\qquad
\widehat G(T\cup\{0\})={\sqrt3\,(u_T-v_T)\over64}.
\tag{3.1}
\]

Therefore every squared spectral mass has denominator `4096`:

\[
q_T={ (3u_T+v_T)^2\over4096},
\qquad
q_{T\cup\{0\}}={3(u_T-v_T)^2\over4096}.
\tag{3.2}
\]

All Walsh transforms, Parseval checks, total-influence numerators, pivot-influence
numerators and Poincare-currency numerators can therefore be computed in exact integer
arithmetic.

The key point is that every output mass in (2.2) is dyadic.  The source read-once fixed
point is exact on the dyadic AND chain, so with

\[
C_0=\Gamma_{\rm RO}(1/2)=6.4548
\]

we may compute, source-exactly,

\[
\Gamma_{\rm RO}(2^{-k})
=
C_0\,{k\over2^{k-1}}-H(\operatorname{AND}_k).
\tag{3.3}
\]

Also

\[
\Gamma_{\rm RO}(1/4)=C_0-2,\qquad
h_2(3/4)=2-{3\over4}\log_2 3.
\]

Hence on the present slice the full gate defect simplifies to

\[
\boxed{
D_{\Gamma_{\rm RO}}
=
C_0 I
+
\left({C_0\over3}-\log_2 3\right)\operatorname{It}_0
-\Gamma_{\rm RO}(r)
-\widetilde H_G.
}
\tag{3.4}
\]

Thus the unavailable value-iteration NPZ is irrelevant to this run: every value of
`Gamma_RO` used by the theorem is fixed by the exact dyadic AND-chain identity.

The quadratic-lift currency is also exact:

\[
W_G={I\over4}-r(1-r)
={I_{\rm num}-4m(64-m)\over16384},
\qquad m=64r,
\tag{3.5}
\]

and the integer numerator is nonnegative in all cases, in agreement with Poincare.

## 4. Computer-assisted theorem

### Theorem 4.1 — quarter-bias dyadic rare-output slice

For every five-input Boolean gate at product bias

\[
(1/4,1/2,1/2,1/2,1/2)
\]

whose output mass is one of the five values in (2.2),

\[
\boxed{D_{\Gamma_{\rm RO}}(G;p)\ge0.}
\tag{4.1}
\]

The only equality cases are coordinate-subcube truth sets; there are exactly `153` of them
in this slice.  Every other gate satisfies

\[
\boxed{D_{\Gamma_{\rm RO}}(G;p)\ge0.056849999999999-10^{-8}>0.}
\tag{4.2}
\]

Consequently

\[
D_{\Gamma_*}
=
D_{\Gamma_{\rm RO}}+0.2682048\,W_G
\ge0
\tag{4.3}
\]

throughout the entire slice.

Among non-subcube gates with positive currency, the largest requested **base** margin is

\[
\boxed{c_G\le -0.72768.}
\tag{4.4}
\]

If both physical slices are nonempty and nonconstant in the classes in (2.3), the stronger
bound observed by the exhaustive certificate is

\[
\boxed{c_G\le -2.137.}
\tag{4.5}
\]

So the genuinely two-sided part of this interior slice is not close to consuming the live
positive lift `a_*=0.2682048`; it has substantial slack already at the unlifted base
potential.

### Certification method

The checker is exhaustive over all `10,857,979` truth tables in (2.3).

* The four-bit Walsh transforms and all spectral numerators are integers.
* `log_2(q)` for every integer `1<=q<=4096` is enclosed by the positive atanh series
  \[
  \log x=2\sum_{j=0}^{N-1}{z^{2j+1}\over2j+1}+R_N,
  \qquad
  z={x-1\over x+1},
  \]
  with an explicit positive geometric tail bound.
* The widest rational logarithm enclosure is `1.203e-35`.
* Midpoint binary64 evaluation has a derived conservative forward-error bound
  `7.089e-13`; the checker uses the much looser sign envelope `1e-8`.
* Every one of the `153` cases inside that envelope is independently recognized as a
  coordinate subcube.  Such a gate is an AND/OR of literals with dummies and has exact
  `D=0` by the dyadic AND-chain identity and symmetry.
* Every non-subcube case is separated from zero by at least `0.05685`, over five million
  times the chosen sign envelope.
* Parseval and the exact integer Poincare-currency numerator are checked for every batch.

The captured run prints `PASS`.

## 5. Independent definition-level cross-check

As a second implementation path, the checker evaluates one genuinely two-sided near-edge
case directly from the 32 product-weighted input points, without using (3.1).

Take

\[
A=\{0,1\},\qquad B=\{0,2\}
\]

in the four-bit slice encoding.  Then

\[
p_{\rm out}=1/8,\qquad
\widetilde H_G=2.62255624891827,\qquad
I=0.84375,\qquad
\operatorname{It}_0=0.09375.
\]

The direct calculation gives

\[
D_{\Gamma_{\rm RO}}=0.252620703327825.
\tag{5.1}
\]

Here

\[
W_G={1664\over16384}=0.1015625,
\]

so

\[
c_G=-{D\over W}\approx-2.48734230968934,
\]

and the live defect is approximately

\[
D_{\Gamma_*}=0.279860253327825.
\]

The direct spectrum and the integer slice formula agree to below `7e-18` in spectral mass
in the development check.

## 6. What was attempted, what would refute it, and what remains

**Exact candidate version.** `LIMIT-PRIME-GATE-LIFT-v1`:
`Gamma_*=Gamma_RO+0.2682048 p(1-p)`, cap `C_*=6.5218512`.

**Old missing implication.**  The peer boundary theorem reduces any counterexample to a
genuinely two-sided **interior** local gluing.  No universal bound on that interior class is
proved.

**Attempted stronger bridge.**  On the first asymmetric interior five-input cross-section,
ask whether the *unlifted* base inequality `D_{Gamma_RO}>=0` already holds for every gate
at the sparse dyadic output masses (2.2).

**Result.** `PROVED (computer-assisted, source-exact at every Gamma value used)` for this
slice.  A counterexample would have been any enumerated admissible Boolean gate with
`D<-1e-8` or a non-subcube inside the certification envelope.  None exists.

**What this does not prove.**  It does not control non-dyadic output masses, other interior
bias vectors, higher arity, or the universal local inequality.  It is not a finite-to-
infinite extrapolation and not a proof of FEI.

**Replacement obligation / next mathematical attack.**  Do **not** rerun another nearby
dyadic truth-table battery.  The useful successor is to derive or refute the analytic
quarter-bias rare-output extension

\[
D_{\Gamma_{\rm RO}}
\bigl(G;(1/4,1/2,\ldots,1/2)\bigr)\ge0
\quad\text{for }p_{\rm out}\le1/4,
\tag{6.1}
\]

first for genuinely two-sided pairs, using the exact restriction cocycle and retaining the
information credit.  If (6.1) is false, preserve the first exact non-dyadic Boolean witness
and attack the weaker live-lift inequality instead.  This moves the method from finite
dyadic enumeration to an analytic interpolation/convexity problem, as required after
repeated finite-slice work.

**Next recipient.** `fleet01/B18` (gate/universal proof lead), with
`fleet04/B17` as the restriction-cocycle/boundary partner.

**Implication to full FEI.**  The live candidate survives a substantial asymmetric
interior sparse-output slice with much more slack than required, but the universal
all-gate implication remains open.  **Full FEI remains OPEN / NOT PROVED.**

## 7. Reproducibility and provenance

Checker: `CHECK_ASYMMETRIC_QUARTER_DYADIC.py`  
Captured output: `CHECK_OUTPUT.txt`

Local source SHA-256 before repository delivery:

`d0e50ee9d1c2b0a7f5bc1931be2d8111385a1a821881157d8f5c5ad056828f0`

Captured output SHA-256:

`7c48f9e01631681ec23b23f162548d3094a3032cf692181a9ee94bc2ebd43786`

No novelty or publication-priority claim is made.  The peer theorem and source gate
reformulation are inherited repository results.  No authenticated mathematical-brain
retrieval/context was used, hence `WITHOUT_VERIFIED_BRAIN`.
