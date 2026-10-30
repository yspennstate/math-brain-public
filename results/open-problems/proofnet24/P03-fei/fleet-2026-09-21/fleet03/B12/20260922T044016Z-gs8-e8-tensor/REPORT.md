# fleet03/B12 — E8 survives the full G_* restriction closure, and tensor amplification cannot create a GS8 counterexample

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact candidate and peer result consumed

The historical read-once `Gamma` / AND-extremality candidate is already rigorously refuted by the source-bound balanced gates in the current archive, including this slot's earlier ten-input gate and the later shared-graft lower-bound family.  I therefore do not repeat the obsolete small-arity sweep.

The concrete replacement candidate attacked here is the fleet01/B18 quadratic-eight compiler

\[
\Gamma_8(p)=32p(1-p)=8V_p,
\]

with

\[
D_8(F)=8\bigl(I(F)-\operatorname{Var}(F)\bigr)-H(F).
\]

For an essential physical coordinate `i`, write

\[
L_i(F)=H(F)-\frac{H(F_{i=0})+H(F_{i=1})}{2},
\]

\[
C_i(F)=\bigl(I-\operatorname{Var}\bigr)(F)
-\frac{\bigl(I-\operatorname{Var}\bigr)(F_{i=0})+
       \bigl(I-\operatorname{Var}\bigr)(F_{i=1})}{2}.
\]

The exact split recursion is

\[
D_8(F)=\frac{D_8(F_{i=0})+D_8(F_{i=1})}{2}+8C_i(F)-L_i(F).
\tag{0.1}
\]

Thus the universal statement

\[
\boxed{\text{GS8: for every nonaffine Boolean }F\text{ there is an essential }i
\text{ with }L_i(F)\le 8C_i(F)}
\tag{0.2}
\]

would prove `H(F)<=8 I(F)` by induction.

**Named peer result consumed and applied:** fleet02/B16,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T022804Z-quadratic8-all-restrictions/REPORT.md`, report blob
`477be830d660661df540e60366f578e002e7962f`.
It proves GS8 on all `3^10=59,049` physical restrictions of the source-bound ten-input prime gate `G_*`, while also finding **31 rigorously bad individual split edges**.  Its exact universal gap is (0.2).

I apply that result to the missing stronger aggregate implication from fleet01/B18,

\[
\boxed{\mathrm{E8}:\qquad
\sum_iL_i(F)\le8\sum_iC_i(F)}.
\tag{0.3}
\]

Since
\[
C_i(F)=\operatorname{Inf}_i(F)-\widehat F(\{i\})^2,
\]
we have
\[
\sum_i C_i(F)=I(F)-W_1(F),\qquad
W_1(F):=\sum_i\widehat F(\{i\})^2.
\tag{0.4}
\]
E8 implies GS8 by averaging, but had not been proved even on the hard `G_*` closure.

## 1. New exact finite theorem: every restriction of G_* satisfies E8

The adjacent checker reconstructs the immutable source-bound truth table with SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

enumerates all `59,049` coordinate restrictions, computes Walsh coefficients as exact integers, and encloses every logarithm by a rational atanh series.  For each restriction it evaluates

\[
R_{\mathrm{E8}}(F):=
8\bigl(I(F)-W_1(F)\bigr)-\sum_iL_i(F).
\tag{1.1}
\]

The result is

\[
\boxed{R_{\mathrm{E8}}(F)\ge0
\quad\text{for every one of the }59,049\text{ restrictions of }G_*.}
\tag{1.2}
\]

No floating-point comparison decides the sign.  The certificate records:

- E8-negative states: **0**;
- exact equality states: **41,904**;
- exact equality states with positive bank `I-W_1`: **9,888**;
- exact maximum of `(sum_i L_i)/(I-W_1)`: **8**;
- smallest rigorously positive E8 residual among non-equality states:
  \[
  \boxed{R_{\mathrm{E8}}>0.468209290806667;}
  \]
- at the ten-input root,
  \[
  I-W_1=\frac{51135}{32768},
  \]
  \[
  8.986619096573759<\sum_iL_i<8.986619096573760,
  \]
  and
  \[
  \boxed{R_{\mathrm{E8}}>3.497511762801240.}
  \]

This is strictly stronger than merely selecting one paid coordinate on this closure.  In particular, the 31 bad individual edges found by the consumed peer do not aggregate into an E8 failure at any restriction state.

## 2. New universal theorem: tensor products only improve the E8/GS8 bank

This part is algebraic and applies to **all** Boolean functions, not only `G_*`.

Let `f:{-1,1}^X->{-1,1}` and `g:{-1,1}^Y->{-1,1}` be on disjoint coordinate sets and put

\[
F(x,y)=f(x)g(y).
\]

The Fourier coefficients factor:

\[
\widehat F(A\cup B)=\widehat f(A)\widehat g(B).
\tag{2.1}
\]

Therefore

\[
H(F)=H(f)+H(g),\qquad I(F)=I(f)+I(g),
\tag{2.2}
\]

and, because `E F=(E f)(E g)`,

\[
\operatorname{Var}(F)
=\operatorname{Var}(f)+\operatorname{Var}(g)
-\operatorname{Var}(f)\operatorname{Var}(g).
\tag{2.3}
\]

Consequently the quadratic-eight defect is **superadditive**:

\[
\boxed{
D_8(F)=D_8(f)+D_8(g)
+8\operatorname{Var}(f)\operatorname{Var}(g).}
\tag{2.4}
\]

There is a sharper local identity.  If `i in X`, then restriction commutes with multiplication by `g`, so entropy additivity gives

\[
L_i(F)=L_i(f).
\tag{2.5}
\]

Also `Inf_i(F)=Inf_i(f)` while

\[
\widehat F(\{i\})
=\widehat f(\{i\})\widehat g(\varnothing).
\]
Hence

\[
\boxed{
C_i(F)=C_i(f)+\widehat f(\{i\})^2\operatorname{Var}(g).}
\tag{2.6}
\]

Thus, writing `r_i=8C_i-L_i`,

\[
\boxed{
r_i(F)=r_i(f)+8\widehat f(\{i\})^2\operatorname{Var}(g)\ge r_i(f).}
\tag{2.7}
\]

The symmetric identity holds for coordinates of `g`.  Summing gives the exact aggregate formula

\[
\boxed{
R_{\mathrm{E8}}(fg)
=R_{\mathrm{E8}}(f)+R_{\mathrm{E8}}(g)
+8\Bigl(W_1(f)\operatorname{Var}(g)
       +W_1(g)\operatorname{Var}(f)\Bigr).}
\tag{2.8}
\]

Every correction term in (2.4), (2.7), and (2.8) is nonnegative.

### Consequences

1. **E8 tensor closure.** If E8 holds for `f` and `g`, it holds for `fg`.
2. **GS8 tensor closure.** If a nonaffine factor has a GS8-good essential coordinate, the same coordinate remains good in the product.  Hence tensor products of GS8-safe factors are GS8-safe.
3. Any minimal counterexample to E8 or GS8 can be assumed **tensor-prime** after deleting affine/constant factors.
4. The natural attempted adversary “take one of fleet02/B16's 31 bad edges and amplify it by independent tensor copies” cannot create the missing all-bad function.  Equation (2.7) shows tensoring can only preserve or improve that coordinate's residual; it never makes it worse.

This is an exact nonreuse/decomposition fact in the current all-gate campaign: independent spectral components contribute their entropy once, and the singleton/variance cross term supplies extra quadratic-eight currency rather than duplicating debt.

## 3. Infinite source-bound corollary

Combining (1.2) with (2.8):

> Every finite disjoint tensor product of arbitrary physical coordinate restrictions of the source-bound gate `G_*` satisfies E8 and therefore GS8.

So the consumed finite peer theorem extends to an infinite Boolean class, and its finitely many locally bad split edges cannot be turned into a tensor-amplified obstruction.

This is still **not** full FEI.  The hard universal case is now cleanly localized to tensor-prime Boolean functions.

## 4. Refutation attempt and what failed

The first counterexample attempt was to exploit the peer's 31 negative one-step residuals by replicating a bad restriction in independent variable blocks.  That route is **REFUTED** by (2.7): for a coordinate in the first factor, multiplication by any nonconstant independent factor adds exactly

\[
8\widehat f(\{i\})^2\operatorname{Var}(g)\ge0
\]

to the GS8 residual.  If the singleton coefficient vanishes, the badness is unchanged; otherwise it strictly improves.  Independent replication therefore cannot convert “some bad coordinates” into an all-bad state.

A separate numerical hill-climb was used only as a falsification attempt, not as proof: no E8 ratio above 8 was found for random/hill-climbed Boolean functions through dimension 7; AND2 remained at the exact value 8.  This numerical observation is not used in any theorem above.

## 5. Exact status and next implication

**Exact candidate version:** `GAMMA8-GS8-E8-v1`.

**Prior missing implication:** prove or refute universal GS8; fleet01/B18 proposed the stronger aggregate E8 target, while fleet02/B16 showed that arbitrary-coordinate GS8 is false but one good coordinate survives throughout the complete `G_*` restriction closure.

**New proved inference:**
- E8 is rigorously true on all 59,049 restrictions of `G_*`;
- E8 and GS8 are universally preserved under disjoint tensor products, with the exact nonnegative credits (2.4), (2.7), (2.8).

**Exact failed counterexample mechanism:** tensor-amplifying a locally bad coordinate is **REFUTED**.

**Replacement obligation:** prove E8 or at least GS8 on tensor-prime Boolean functions, or construct a tensor-prime Boolean function for which every essential coordinate has `L_i>8C_i`.  A valid counterexample must use genuinely interacting Fourier structure, not independent block replication.

**Consumed peer artifact:** fleet02/B16 `20260922T022804Z-quadratic8-all-restrictions/REPORT.md`, blob `477be830d660661df540e60366f578e002e7962f`, applied to the universal GS8/E8 gap and to its 31-bad-edge obstruction.

**Next recipient:** `fleet03/B18` (FEI B lead).  The next implication to full FEI is the tensor-prime GS8/E8 case; the fleet01/B18 signed Boolean convolution constraints are the natural next source because scalar edgewise payment is already refuted.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
