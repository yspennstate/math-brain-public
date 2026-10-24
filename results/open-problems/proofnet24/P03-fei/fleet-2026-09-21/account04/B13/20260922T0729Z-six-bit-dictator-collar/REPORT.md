# account04/B13 — balanced six-bit dictator collar is strictly safe

**Classification:** `ESSENTIAL_STEP_APPLIED / BAL6_DICTATOR_COLLAR_CLOSED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim is made.

## 0. Live target and the peer result consumed

The later owner control converges the FEI fleet on the source-exact all-gate inequality.  At the balanced uniform centre, for a balanced Boolean gate `f`, the current lifted candidate reduces to

\[
H(f)\le C^\dagger[I(f)-1],
\qquad C^\dagger=6.521851214.
\]

The exact newest compatible other-account result consumed in this run is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T063239Z-six-bit-gibbs-shell/REPORT.md`

from scientific commit `4f330f0e645774b18bc2add4646c1b89a1c211bb`, report blob `12652ca949efdfe4eada1d64e23312fa142d15b4`.

That result proves that every hypothetical balanced six-bit falsifier of the live candidate must satisfy

\[
W_1:=\sum_{i=1}^6\widehat f(\{i\})^2\ge \frac{21}{64},
\]

and, using account03/B13's two-generation theorem, every singleton coefficient is nonzero.  Hence some physical pivot has
\(|\widehat f(\{i\})|\ge1/4\).  Its remaining gap, `BAL6-STRONG-PIVOT`, was to control the resulting unequal five-bit children without losing their actual slack.

This run changes that argument by closing the entire *near-dictator escape* before the child-slack calculation: a balanced six-bit gate with any singleton coefficient of magnitude at least `11/16` satisfies the much stronger constant-six inequality.  Therefore a live falsifier must lie in a compact correlation annulus rather than being allowed to approach a character.

## 1. Exact close-to-dictator parametrization

Let
\[
f:\{-1,+1\}^6\to\{-1,+1\}
\]
be balanced, and fix a coordinate, say `x_1`.  Negating `f` if necessary, suppose
\(a:=\widehat f(\{1\})\ge0\).
Because both `f` and `x_1` are balanced, the disagreement set
\[
E=\{x:f(x)\ne x_1\}
\]
contains the same number `r` of points in each of the two `x_1` half-cubes.  Consequently
\[
a=1-\frac r{16}.
\tag{1.1}
\]
Thus `a>=11/16` is exactly the finite range `0<=r<=5`.

Identify each half-cube with `Q_5`.  Let `E_+,E_-\subset Q_5` be the two mismatch sets, each of size `r`, and define the unnormalized five-bit Walsh sums
\[
A_\pm(s)=\sum_{y\in E_\pm}(-1)^{s\cdot y},
\qquad s\in Q_5.
\]
A direct two-half expansion gives the complete six-bit Walsh transform.  If `c` records whether the pivot coordinate belongs to the Fourier set, then
\[
\begin{aligned}
h(0,s)&=2(A_-(s)-A_+(s)),\\
h(1,0)&=64-4r,\\
h(1,s)&=-2(A_+(s)+A_-(s))\qquad(s\ne0),
\end{aligned}
\tag{1.2}
\]
and every Fourier mass is exactly `h(c,s)^2/4096`.

Input negations and permutations of the five transverse coordinates preserve both `H` and `I`.  Therefore, for each `r`, it is enough to put `E_+` in one orbit representative under the full translation/permutation isometry group of `Q_5` and let `E_-` range over *all* `r`-subsets.  The checker independently verifies that its representative lists cover every `r`-subset.

## 2. Theorem: the entire `|hat f_i|>=11/16` collar has constant six

### Theorem 2.1

If `f` is balanced on six uniform bits and
\[
\max_i |\widehat f(\{i\})|\ge\frac{11}{16},
\]
then either `f` is a character, or
\[
\boxed{H(f)<6[I(f)-1].}
\tag{2.1}
\]

In particular it satisfies the live centre inequality with substantial slack because `6<C^dagger`.

### Proof

After the symmetry reduction above, `r` lies in `{1,2,3,4,5}`.  Formula (1.2) makes both the influence and the spectral probabilities exact integers divided by `4096`.

The finite certificate uses no floating-point sign decision.  For every possible nonzero amplitude `h`, it constructs a rational upper bound for
\[
-\frac{h^2}{4096}\log_2\frac{h^2}{4096}
\]
by reducing the logarithm to `u in [1,2)` and using
\[
\log u=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{u-1}{u+1},
\]
with a positive geometric remainder, while a positive partial series at `z=1/3` supplies a rational lower bound for `ln 2`.  Each contribution is then rounded *up* at scale `10^9`.

For every orbit representative `E_+` and every `E_-`, the checker proves by exact integer cross multiplication that the resulting entropy upper bound is strictly smaller than `6(I-1)`.  Orbit coverage is also checked exactly.  The complete counts are

| `r` | `E_+` orbit representatives | all `E_-` subsets | pairs checked | certified lower bound on `6(I-1)-H` |
|---:|---:|---:|---:|---:|
| 1 | 1 | 32 | 32 | 0.367581125 |
| 2 | 5 | 496 | 2,480 | 0.298762224 |
| 3 | 10 | 4,960 | 49,600 | 0.372179490 |
| 4 | 47 | 35,960 | 1,690,120 | 0.033082813 |
| 5 | 131 | 201,376 | 26,380,256 | 0.175342676 |

The global certified gap is therefore at least `0.033082813`.  For `r=0`, Parseval forces `f` to be exactly the pivot character and both sides of (2.1) are zero.  This proves the theorem. `QED`

The certificate covers `28,122,488` symmetry-reduced ordered mismatch pairs.  It is a finite proof of this six-bit statement, not evidence for an unbounded-arity extrapolation.

## 3. Owner-comparable gate margin

The owner requests the gate margin rather than raw defect.  At the balanced centre for the read-once base potential with
\(C_0=6.4548\),
\[
c_f=4\left(\frac{H(f)}{I(f)-1}-C_0\right)
\]
whenever `I(f)>1`.  Theorem 2.1 therefore gives throughout this collar
\[
\boxed{c_f<4(6-6.4548)=-1.8192.}
\tag{3.1}
\]
So these gates are not merely below the current positive AND request: they ask for a strongly negative margin.  Characters are the degenerate zero-currency case and require no correction.

## 4. Exact change to the newest account01/B13 argument

The account01/B13 Gibbs-shell theorem forced a hypothetical live balanced six-bit falsifier to satisfy
\[
W_1\ge21/64,
\qquad \widehat f(\{i\})\ne0\ \forall i,
\qquad \max_i|\widehat f(\{i\})|\ge1/4,
\]
but it did not bound the strong pivot away from a character.  Theorem 2.1 adds exactly that missing side.

Balanced six-bit singleton coefficients are multiples of `1/16`; therefore any live falsifier must now obey
\[
\boxed{
\frac1{16}\le |\widehat f(\{i\})|\le\frac58\quad\forall i,
\qquad
\sum_i\widehat f(\{i\})^2\ge\frac{21}{64}.
}
\tag{4.1}
\]
In particular the strong pivot supplied by account01/B13 has
\[
\frac14\le |\widehat f(\{i\})|\le\frac58.
\tag{4.2}
\]
For a balanced parent, its two five-bit child output probabilities are
\((1\mp\widehat f(\{i\}))/2\).  Hence that pivot is localized to the compact off-centre band
\[
\boxed{
3/16\le p_{\rm small}\le3/8,
\qquad
5/8\le p_{\rm large}\le13/16.
}
\tag{4.3}
\]
This removes both the near-balanced escape already excluded by the Gibbs first-shell forcing and the near-constant/near-character escape closed here.  The next `BAL6-STRONG-PIVOT` calculation can therefore work on a compact child-output band with actual five-bit child slack and the exact two-channel restriction cocycle.

The earlier account01 dichotomy is retained and sharpened only by the new upper cap: either at least two coordinates have singleton magnitude at least `1/4`, or the unique such coordinate lies in
\[
7/16\le|\widehat f(\{i\})|\le5/8.
\]

## 5. Relation to interface B and preserved account04/B18 results

This finite balanced-centre argument does **not** replace the account04/B18 mixed-curvature theorem.  Its exact source identity remains
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]
including the opposite-sign term, and the exact zero-positive-depth classification remains unchanged: the zero-defect branch is a character times a signed one-point defect (irrelevant variables allowed), with its stated `H<4J` consequence.  No claim `sum d_k=O(J)` is introduced here, and no cube-measure error is multiplied by ambient dimension.

The later owner all-gate convergence order makes the present balanced-six-bit gate localization the active use of the old Booleanity/stability role.  It is compatible with, rather than a weakening of, the prior interface-B results.

## 6. Status and next exact implication

**New proved inference:** the complete balanced six-bit near-dictator collar `max_i |hat f_i|>=11/16` is safe already at constant `6`, with exact finite certificate and owner-comparable margin `<-1.8192`.

**Peer result consumed and changed:** account01/B13's `W_1>=21/64` theorem now localizes every hypothetical live falsifier to (4.1)-(4.3), eliminating a previously open character-boundary escape.

**Remaining implication:** on the compact chamber (4.1), use the exact restriction cocycle and certified five-bit child slack to prove nonnegative parent defect, or exhibit a genuine Boolean gate in that chamber asking for a larger owner margin.  Closing this chamber would settle only the balanced six-bit central slice, not arbitrary bias or arity.

Full FEI remains **OPEN / NOT PROVED**.
