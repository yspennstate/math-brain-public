# B14 — a bounded influence potential that absorbs the full Jensen–Shannon recombination cost

**Status:** PARTIAL / PROVED structural theorem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Live route:** erasure / existential-coordinate selector, APPROACHES 5–6.  
**Fresh mathematical head before derivation:** `730a6f62e8fca2787a7cd915373355c224a2e3b5`.

This run does new mathematics on the remaining restriction obstruction. It does not rerun the read-once certificate. The input facts used at their current scopes are the exact restriction decomposition
\[
\Delta_i H=B_i+JS_i,
\qquad B_i=H(S_i\mid S_{-i}),
\]
the singleton overlap description, and the current strong-concavity theorem for the recombination profile
\[
j(s)=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right),\qquad 0\le s\le\frac12,
\]
which gives
\[
JS_i\le j(M_i)\le j(\min\{\alpha_i,1-\alpha_i\}),
\quad \alpha_i=\operatorname{Inf}_i(f),
\]
and
\[
j''(s)\le-\frac{4}{3\ln2},\qquad j'(s)\ge0.
\]
Here `M_i` is the fibrewise overlap/prediction error. The new observation is that the marginal upper envelope itself can be summed into a bounded restriction potential; its cross-coordinate Jensen gaps are a bonus rather than a liability.

## 1. The potential

Define the symmetric function
\[
\eta(p):=j(\min\{p,1-p\}),\qquad 0\le p\le1.
\tag{1}
\]
Because `j` is concave on `[0,1/2]`, increasing there, and has left derivative `j'(1/2)=0`, reflection across `1/2` shows that `eta` is concave on `[0,1]`. In fact the current curvature theorem implies that `eta` is `4/(3 ln 2)`-strongly concave on the whole interval (with the midpoint understood by continuity).

For a Boolean function `f`, put
\[
\boxed{\Phi(f):=\sum_k\eta(\alpha_k(f)).}
\tag{2}
\]
Irrelevant coordinates contribute zero.

The tangent bound at zero is
\[
\eta(p)\le \frac2{\ln2}\min\{p,1-p\}\le\frac2{\ln2}p,
\]
so
\[
\boxed{0\le\Phi(f)\le c_* I(f),\qquad c_*:=\frac2{\ln2}=2.885390081777\ldots.}
\tag{3}
\]
Thus, unlike `sum h(alpha_i)`, this potential has a dimension-free linear budget.

## 2. PROVED: `Phi` pays the entire JS term at every restriction

Let `f_+,f_-` be the two physical restrictions at coordinate `i`. For `k\ne i`, influence averages exactly:
\[
\alpha_k(f)=\frac{\alpha_k(f_+)+\alpha_k(f_-)}2.
\tag{4}
\]
Define the cross-coordinate Jensen gap
\[
G_{ik}:=\eta(\alpha_k(f))-
\frac{\eta(\alpha_k(f_+))+\eta(\alpha_k(f_-))}{2}\ge0.
\tag{5}
\]
Since coordinate `i` disappears in the children,
\[
\boxed{
\Delta_i\Phi:=\Phi(f)-\frac{\Phi(f_+)+\Phi(f_-)}2
=\eta(\alpha_i)+\sum_{k\ne i}G_{ik}.
}
\tag{6}
\]
The current sharp marginal recombination envelope gives `JS_i<=eta(alpha_i)`. Therefore
\[
\boxed{\Delta_i\Phi\ge JS_i\quad\text{for every Boolean }f\text{ and every physical }i.}
\tag{7}
\]

Equivalently, for the corrected entropy
\[
\mathcal E(f):=H(f)-\Phi(f),
\tag{8}
\]
one has the exact rebate identity
\[
\boxed{
\Delta_i\mathcal E
=B_i-R_i,
\qquad
R_i:=\eta(\alpha_i)-JS_i+\sum_{k\ne i}G_{ik}\ge0,
}
\tag{9}
\]
and hence
\[
\boxed{\Delta_i\mathcal E\le B_i.}
\tag{10}
\]

This is the requested APPROACH 6 mechanism: the Jensen–Shannon recombination obstruction is absorbed by an explicit potential whose total initial size is at most `(2/ln2) I`. What remains is purely the erasure payment. This is **not** full FEI because a dimension-free erasure selector is still missing.

## 3. Adaptive-tree amortization

The local statement telescopes on an arbitrary adaptive physical restriction tree. Give an internal node `v` its natural uniform-input weight `2^{-depth(v)}`, let `f_v` be the restricted function at that node, and let `i(v)` be the queried physical coordinate. Then
\[
\sum_v2^{-\operatorname{depth}(v)}JS_{i(v)}(f_v)
\le
\sum_v2^{-\operatorname{depth}(v)}\Delta_{i(v)}\Phi(f_v)
\le \Phi(f).
\]
Therefore
\[
\boxed{
\text{total JS recombination cost on any adaptive restriction tree}
\le \Phi(f)\le c_*I(f).
}
\tag{11}
\]
The last inequality does not charge `c_* I` anew at each level; it is one global amortized budget.

Consequently, on a complete restriction tree ending at constants,
\[
H(f)
\le c_*I(f)+
\sum_v2^{-\operatorname{depth}(v)}B_{i(v)}(f_v).
\tag{12}
\]
Thus full FEI is reduced to constructing an adaptive restriction tree whose **erasure-only** cost is at most a universal constant times `I(f)`.

## 4. A stricter critical core after subtracting the potential

Choose, among all nonconstant physical restriction descendants of `f`, a descendant `g` maximizing
\[
\rho(g):=\frac{\mathcal E(g)}{I(g)}.
\]
The same maximal-descendant argument used for `H/I` applies to `mathcal E/I`: for every relevant coordinate `i` of `g`,
\[
\boxed{\Delta_i\mathcal E(g)\ge\rho(g)\alpha_i(g).}
\tag{13}
\]
Combining with (9),
\[
\boxed{B_i(g)\ge\rho(g)\alpha_i(g)+R_i(g)
\quad\text{for every relevant }i.}
\tag{14}
\]

If the original `f` violates `H<=C I`, then by (3)
\[
\mathcal E(f)> (C-c_*)I(f),
\]
so the selected descendant satisfies `rho(g)>C-c_*`. Therefore every coordinate of the same descendant must obey the strengthened requirement
\[
\boxed{
B_i>(C-c_*)\alpha_i+
\bigl[\eta(\alpha_i)-JS_i\bigr]
+\sum_{k\ne i}G_{ik}.
}
\tag{15}
\]
This preserves the known counterexamples to a universal every-coordinate upper payment: (15) is a **necessary lower condition only at an existentially selected corrected-critical descendant**.

At the Hod calibration `C=6.4547837`, the old erasure threshold is `C-c_*=3.569393618222...`. For width-two tribes with eight tribes, the current exact formulas give
\[
B_i/\alpha_i=3.606847002096409,
\quad
JS_i/\alpha_i=2.396899054462681,
\quad
\eta(\alpha_i)/\alpha_i=2.817542327818821.
\]
Thus the **own-coordinate** rebate alone raises the corrected-critical requirement to
\[
3.569393618222+(2.817542327819-2.396899054463)
=3.990036891578,
\]
which exceeds `3.606847002096` by `0.383189889482`, even before any cross-coordinate Jensen gaps are counted. Hence the width-two-tribes family that killed the old fixed erasure threshold cannot be a Hod-scale corrected-critical endpoint for this potential.

## 5. New global second-order necessary condition

Let
\[
B(g):=\sum_iB_i(g),
\qquad
\operatorname{DTC}(S):=H(S)-\sum_iH(S_i\mid S_{-i})=H(g)-B(g).
\]
Sum (14) over all relevant coordinates. Since `rho I=mathcal E=H-Phi` and
\[
\sum_iR_i
=\Phi-\sum_iJS_i+
\sum_{i\ne k}G_{ik},
\]
one obtains after cancellation
\[
\boxed{
\operatorname{DTC}(S)+\sum_{i\ne k}G_{ik}
\le\sum_iJS_i.
}
\tag{16}
\]
This is a necessary condition on every corrected-critical descendant, independent of the value of `C`.

Strong concavity of `eta` gives the explicit lower bound
\[
G_{ik}\ge
\frac{1}{6\ln2}
\left(\alpha_k(f_{i,+})-\alpha_k(f_{i,-})\right)^2.
\tag{17}
\]
Hence
\[
\boxed{
\operatorname{DTC}(S)
+\frac1{6\ln2}
\sum_{i\ne k}
\left(\alpha_k(f_{i,+})-\alpha_k(f_{i,-})\right)^2
\le\sum_iJS_i
\le\Phi(g)
\le c_*I(g).
}
\tag{18}
\]
The new term measures how much the influence of coordinate `k` changes when another physical bit `i` is fixed. Thus a hypothetical high-ratio corrected-critical core must spend its finite recombination budget on **both** spectral dual total correlation and all pairwise influence-instability. This points to a quantitative stability dichotomy: either many influences move under restrictions, consuming the right side of (18), or they are nearly restriction-stable, where the current product-spectrum/all-shift rigidity should become applicable.

## 6. Native finite validation of the new identities

A separate direct Walsh implementation enumerated Boolean functions up to global sign for `n<=4` and checked every relevant coordinate. Relevant-coordinate case counts were

- `n=1`: 1,
- `n=2`: 12,
- `n=3`: 360,
- `n=4`: 130,560.

Across all 130,933 relevant-coordinate tests, the minimum observed `Delta_i Phi-JS_i` was `0` (attained at exact equality cases); no negative violation was found. The maximum floating error in identity (9) was `1.11e-16`. The strong-concavity Jensen-gap lower bound (17) had no negative violation. The largest observed `Phi/I` at `n=4` was `2.7515394962`, below the proved universal `2/ln2=2.8853900818`. These calculations are checks only; the proof above does not depend on finite enumeration.

## 7. Relation to current literature and exact remaining gap

A bounded current primary-literature search found González–MacManus–Pereyra, arXiv:2606.00246 (29 May 2026), which also uses restriction entropy decrements and stopping binary trees. I make **no novelty/priority claim** for the potential above without a dedicated literature review. The current internal B14 results on strong concavity, block prediction error, signed all-shift orthogonality, and the exact scalar hard-core endpoint are compatible with (2)–(18).

**What is proved here:** an explicit dimension-linearly-bounded influence potential that universally absorbs the entire JS recombination term, a one-budget adaptive-tree amortization, a stronger corrected-critical descendant inequality, and the second-order budget (18).

**What remains open:** prove a universal bound for the remaining erasure-only tree cost in (12), equivalently rule out corrected-critical Boolean cores satisfying (15) and (18). Full FEI remains OPEN.

**Next B14 step:** combine (18) with the existing all-shift Boolean orthogonality/product-spectrum rigidity. The concrete target is a quantitative dichotomy: if the pairwise influence-instability sum in (18) is small, show that the spectral law is sufficiently close to the forbidden low-marginal product regime to force a proper-block erasure selector; if it is large, (18) itself pays for it.
