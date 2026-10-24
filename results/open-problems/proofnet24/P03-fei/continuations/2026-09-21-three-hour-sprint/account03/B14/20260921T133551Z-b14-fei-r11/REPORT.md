# B14 FEI — an explicit quadratic-influence potential absorbs all restriction Jensen–Shannon cost

**Date:** 21 September 2026  
**Fleet scope:** account03/B14  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED universal auxiliary theorem. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Priority:** no publication-priority claim is made.

## 0. Fresh state and exact statement attacked

This run read the current FEI entry documents in the required order and then the newest compatible erasure/restriction handoffs. The scientific `master` head immediately before this report was `e067fbba2c77a956b240a924c833143bc3175ee9`. The live owner correction is preserved: the read-once/Hod value `6.4547837...` is not the current unrestricted lower-bound scale; the recovered external Numaro seed gives `C_FEI > 6.521845710923046575`. None of the proof below depends on that numerical correction.

The inherited exact coordinate decomposition is

\[
\Delta_i H=B_i+JS_i,
\qquad B_i=H(X_i\mid X_{-i}),
\tag{0.1}
\]

where `X` is the Fourier spectral sample, and the current strong-concavity result gives, with

\[
c_*:=\frac{2}{\ln 2},\qquad \alpha_i:=\operatorname{Inf}_i(f),
\]

\[
JS_i\le c_*\left(m_i-\frac{m_i^2}{3}\right),
\qquad m_i:=\min\{\alpha_i,1-\alpha_i\}.
\tag{0.2}
\]

The exact attempted statement in this run was:

> **Can one construct an explicit nonnegative, tensor-compatible potential whose physical-restriction drop pays the whole `JS_i` term for every coordinate, while leaving the mass-weighted erasure `B_i` as the only positive local charge?**

The answer is yes. This does not prove FEI because the remaining erasure charge still needs a dimension-independent existential selector.

## 1. The quadratic-influence potential

For a Boolean function `f:{-1,1}^n->{-1,1}`, put

\[
I(f)=\sum_j\alpha_j,
\qquad
A_2(f)=\sum_j\alpha_j^2,
\]

and define

\[
\boxed{
P_2(f):=c_*\left(I(f)-\frac13A_2(f)\right).
}
\tag{1.1}
\]

Since `0<=alpha_j<=1`,

\[
\frac{2c_*}{3}I(f)\le P_2(f)\le c_*I(f),
\tag{1.2}
\]

so the potential is nonnegative. It is also tensor-additive on disjoint-variable products because both `I` and `A_2` are additive there.

Fix a physical coordinate `i`. Write `f_i^+`,`f_i^-` for its two restrictions and, for `j != i`,

\[
\alpha_j^\pm:=\operatorname{Inf}_j(f_i^\pm),
\qquad d_{ij}:=\alpha_j^+-\alpha_j^-.
\]

Physical edge conditioning gives the exact averaging identity

\[
\alpha_j=\frac{\alpha_j^++\alpha_j^-}{2}\qquad(j\ne i).
\tag{1.3}
\]

### Theorem 1.1 — exact potential drop and universal JS absorption

For every Boolean `f` and every relevant coordinate `i`,

\[
\boxed{
\Delta_iP_2
=c_*\left[
\alpha_i-\frac{\alpha_i^2}{3}
+\frac1{12}\sum_{j\ne i}d_{ij}^2
\right].
}
\tag{1.4}
\]

Moreover

\[
\boxed{JS_i\le \Delta_iP_2.}
\tag{1.5}
\]

Consequently, defining the nonnegative **restriction gain**

\[
\boxed{
G_i:=\Delta_iP_2-JS_i\ge0,
}
\tag{1.6}
\]

one has the exact residual restriction identity

\[
\boxed{
\Delta_i(H-P_2)=B_i-G_i\le B_i.
}
\tag{1.7}
\]

#### Proof

The ordinary influence telescope is exact:

\[
I(f)-\frac{I(f_i^+)+I(f_i^-)}2=\alpha_i.
\tag{1.8}
\]

For the quadratic term, (1.3) and the elementary identity

\[
\frac{a^2+b^2}{2}=\left(\frac{a+b}{2}\right)^2+\frac{(a-b)^2}{4}
\]

give

\[
A_2(f)-\frac{A_2(f_i^+)+A_2(f_i^-)}2
=\alpha_i^2-\frac14\sum_{j\ne i}d_{ij}^2.
\tag{1.9}
\]

Substituting (1.8) and (1.9) in (1.1) proves (1.4).

Now set `phi(t)=t-t^2/3`. It is increasing on `[0,1]`. Since `m_i<=alpha_i`, the inherited strong-concavity estimate (0.2) gives

\[
JS_i\le c_*\phi(m_i)\le c_*\phi(\alpha_i)
\le\Delta_iP_2,
\]

where the final inequality is (1.4) and nonnegativity of the squared child-influence modulation. This proves (1.5). Finally combine (0.1) with (1.6) to obtain (1.7). QED.

A useful explicit lower bound on the gain follows from the stronger inherited fibrewise estimate. If `M_i=sum_T w_T s_T` and `Q_i=sum_Tw_Ts_T^2`, then

\[
G_i\ge
c_*\left[
\alpha_i-\frac{\alpha_i^2}{3}-M_i+\frac{Q_i}{3}
+\frac1{12}\sum_{j\ne i}d_{ij}^2
\right]\ge0.
\tag{1.10}
\]

Thus the gain has two distinct sources: scalar recombination slack and actual modulation of the other physical influences under the two children.

## 2. Exact global restriction-tree identity

Let `T` be any complete adaptive physical restriction tree. At an internal node `v`, let `mu_v=2^{-depth(v)}` be its reach weight, let `i(v)` be the queried physical coordinate, and write `B_v,G_v` for the quantities in (1.7).

Because terminal constants have `H=P_2=0`, (1.7) telescopes exactly:

\[
\boxed{
H(f)=P_2(f)+\mathcal B_T(f)-\mathcal G_T(f),
}
\tag{2.1}
\]

where

\[
\mathcal B_T:=\sum_v\mu_vB_v,
\qquad
\mathcal G_T:=\sum_v\mu_vG_v\ge0.
\tag{2.2}
\]

In particular,

\[
H(f)\le c_*I(f)-\frac{c_*}{3}A_2(f)+\mathcal B_T(f).
\tag{2.3}
\]

This is compatible with the new exact debit/reserve ledger from account04/B18, but it packages part of the dynamic reserve into a **static explicit influence potential** and leaves a concrete additional child-modulation rebate in `G_v`.

## 3. A strictly more faithful existential selector

Define the residual singleton selector constant in the extended sense

\[
K_R:=\sup_{f\text{ nonconstant}}
\min_{i:\alpha_i>0}
\frac{B_i-G_i}{\alpha_i}.
\tag{3.1}
\]

### Theorem 3.1 — residual-selector compiler

If `K_R<infinity`, then full uniform-cube FEI holds and, more precisely,

\[
\boxed{
H(f)\le (K_R+c_*)I(f)-\frac{c_*}{3}A_2(f).
}
\tag{3.2}
\]

Conversely, if FEI holds with constant `C`, then `K_R<=C`. Therefore for the optimal constants, whenever finite,

\[
\boxed{
C_{FEI}-c_*\le K_R\le C_{FEI}.
}
\tag{3.3}
\]

#### Proof

Choose at every nonconstant restriction state a coordinate satisfying `(B_i-G_i)<=K_R alpha_i`. Apply induction to `F:=H-P_2`. Equation (1.7) and the ordinary influence telescope give

\[
F(f)\le K_R I(f).
\]

Adding (1.1) proves (3.2).

For the converse, the general entropy inequality `sum_i B_i<=H(f)` and `G_i>=0` imply

\[
\sum_i(B_i-G_i)\le H(f)\le C\sum_i\alpha_i.
\]

Hence at least one relevant coordinate has `(B_i-G_i)/alpha_i<=C`. Taking the supremum over `f` proves `K_R<=C`; combining with (3.2) yields (3.3). QED.

This is not merely a renaming of the old erasure selector: `G_i` contains the squared physical child-influence shifts. The new universal obligation is

\[
\boxed{
\exists i:\quad B_i-G_i\le K\alpha_i
}
\tag{3.4}
\]

for some finite dimension-independent `K`, at every nonconstant state. The old false every-prescribed-coordinate payment is not revived.

## 4. Targeted stress test: width-two tribes

The current strong-concavity report records that width-two tribes with `s=8` kills the older fixed raw-erasure target even though it is not an FEI counterexample. Here the new residual charge can be computed exactly enough to see what the potential buys.

For width-two tribes with `s` tribes and a fixed physical coordinate,

\[
p=\alpha_i=\frac12\left(\frac34\right)^{s-1}.
\]

Conditioning that coordinate changes the mate's influence by `2p`, while each of the `2(s-1)` coordinates in the other tribes changes by `2p/3`. Hence

\[
\sum_{j\ne i}d_{ij}^2
=4p^2\left(1+\frac{2(s-1)}9\right),
\tag{4.1}
\]

and (1.4) simplifies to

\[
\frac{\Delta_iP_2}{p}
=c_*\left(1+\frac{2p(s-1)}{27}\right).
\tag{4.2}
\]

At `s=8`, using the already-derived exact tribes restriction formulas,

\[
p=0.066741943359375,
\]

\[
B_i/p=3.6068470020964082749\ldots,
\qquad
\Delta_iH/p=6.0037460565590882514\ldots,
\]

\[
JS_i/p=2.3968990544626799765\ldots,
\qquad
\Delta_iP_2/p=2.9852445847300804099\ldots,
\]

so

\[
\boxed{
G_i/p=0.5883455302674004335\ldots,
\qquad
\frac{B_i-G_i}{p}=3.0185014718290078415\ldots.
}
\tag{4.3}
\]

Thus the same family with raw erasure ratio `3.606847...` has residual selector ratio only `3.018501...`. At the current external lower-bound calibration `6.521845710923046575`, the corresponding additive residual threshold `C-c_*` is `3.6364556291451197603...`; this family therefore has about `0.6179541573` of room under that *calibration*. This is only a targeted stress test, not a universal bound or a claim that this `C` is sufficient for FEI.

## 5. Attempted refutations and dead routes

### 5.1 REFUTED: dual total correlation alone pays recombination

A tempting stronger route was to hope that the dependence reserve

\[
\operatorname{DTC}(X):=H(X)-\sum_iH(X_i\mid X_{-i})
\]

could pay `sum_i JS_i`. This is false already for the two-bit Boolean function that differs from a constant at exactly one input. Its squared Fourier law is uniform on all four subsets, so the two spectral membership bits are independent and `DTC(X)=0`. Yet each coordinate has `Delta_iH=2`, `B_i=1`, hence `JS_i=1`, so `sum_iJS_i=2`. Therefore

\[
\sum_iJS_i\le\operatorname{DTC}(X)
\]

is **REFUTED**. The quadratic-influence potential avoids this failure because its restriction drop is sensitive to the physical child influence profiles rather than only static spectral dependence.

### 5.2 Scalar coefficient `1/3` is sharp for the marginal-only step

The inherited strong-concavity calculation has

\[
j'(0)=c_*,\qquad j''(0+)=-\frac{2c_*}{3},
\]

so

\[
j(s)=c_*s-\frac{c_*}{3}s^2+o(s^2).
\]

Consequently no scalar inequality of the form

\[
j(s)\le c_*(s-a s^2)\quad\text{for all sufficiently small }s
\]

can hold with `a>1/3`. Thus improving the coefficient in `P_2` by the same marginal-only argument is a dead route. This does **not** rule out a stronger Boolean theorem that uses the positive child-modulation term in (1.4).

## 6. What is proved, conditional, open, and refuted

### PROVED in this run

- The explicit nonnegative tensor-additive potential `P_2=c_*(I-A_2/3)` has exact restriction drop (1.4).
- Using the current strong-concavity recombination theorem, `Delta_iP_2>=JS_i` for every Boolean function and every coordinate.
- The exact residual identity `Delta_i(H-P_2)=B_i-G_i`, `G_i>=0`.
- The exact tree identity `H=P_2+B_T-G_T` for every complete adaptive physical restriction tree.
- The residual-selector compiler (3.2) and additive equivalence window (3.3).
- The width-two-tribes `s=8` residual ratio calculation (4.3).

### CONDITIONAL / inherited dependency

- The inequality `JS_i<=c_*(m_i-m_i^2/3)` is the already-proved account04/B14 strong-concavity input. The present algebra and restriction telescope are complete once that input is accepted.
- The numerical unrestricted lower-bound correction comes from recovered external work and is used only as a calibration, not as part of a proof.

### OPEN

- A dimension-independent bound on the residual selector (3.4).
- A proof that the extra child-modulation term forces such a selector on a Boolean critical core.
- Full uniform-cube FEI.

### REFUTED / NOT CLAIMED

- `sum_i JS_i <= DTC(X)` is false, as shown in section 5.1.
- No every-prescribed-coordinate FEI payment is claimed; known counterexamples remain preserved.
- The scalar `1/3` sharpness statement is not a proof that every more sophisticated Boolean quadratic potential is optimal.
- The tribes calculation is not a universal theorem and is not FEI closure.

## 7. Next attack

The next B14 attack should target (3.4) directly, exploiting the two-case structure already visible in `G_i`:

1. **large child modulation:** if `sum_{j != i} d_{ij}^2` is appreciable, the explicit `c_*/12` rebate pays part of the erasure immediately;
2. **small child modulation at every candidate coordinate:** then every edge-disagreement indicator has weak first-order correlation with the other physical bits. Combine that near-invariance with the exact Boolean Fourier convolution identities/product-phase rigidity to force either a low erasure fibre profile or a higher-order modulation witness.

The sought theorem is existential and mass-weighted. It should not be weakened into another every-coordinate claim. If first-order modulation can cancel at all coordinates, the materially different next mechanism is a hierarchy of higher-order child block-influence shifts rather than another scalar Jensen bound.
