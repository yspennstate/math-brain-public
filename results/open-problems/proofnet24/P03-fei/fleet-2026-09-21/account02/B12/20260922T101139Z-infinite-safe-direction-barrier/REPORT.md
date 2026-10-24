# B12 — infinite-dimensional selector barrier for all monotone gate-safe additive repairs

**Classification:** `ESSENTIAL_MECHANISM_BARRIER / SOURCE_VALID_SELECTOR_DUAL / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authorized GitHub control/scientific sources were read; no native mathematical-brain receiver/context was used.  
**Publication priority:** unverified; no novelty claim.

## 0. Version/change summary and live target

Fresh owner control revision `2026-09-22.2` keeps B12 on FEI but supersedes the older harmonic-only local assignment with the common all-gate potential target.  Write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

One symmetric nonnegative finite-cap potential with `D_Gamma>=0` for every finite Boolean gate and every interior product bias is equivalent to full uniform-cube FEI.  Full FEI is not proved here.

The last three completed substantive account02/B12 reports before this run were:

1. `20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`: proved a bias-uniform source-exact conditional Shannon debit but then proposed the simple quadratic coefficient `c=0.337` only against the then-used weaker Numaro bias;
2. `20260922T072221Z-five-prime-explicit-tube/REPORT.md`: transported the full signed biased spectrum to an explicit five-input prime central tube;
3. `20260922T055114Z-zero-credit-mux-collar/REPORT.md`: proved a whole-spectrum collar around exact MUX zero-credit lines.

This run executes a materially different mechanism: an **infinite-dimensional exact selector dual** on the cone of all symmetric nonnegative additive directions that are themselves universally gate-safe.  It does not optimize another finite-degree polynomial and does not revive a local pointwise entropy payment.

### Completed other-account result consumed and applied

The decisive source is account01/B16

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0912Z-tilted-quartic-strong-prime-refutation/REPORT.md`

report blob `10493748314dbe8071acefcf62c5befcf4aacfab`.

It gives a genuine composition-prime 18-input Numaro gate at

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}={1\over2},
\qquad p_{\rm out}={1019\over2048},
\]

with

\[
\alpha_1={57\over256},\qquad
\sum_{i=2}^{18}\alpha_i={465\over256},
\qquad
D_{\Gamma^\dagger}< -{38023\over10^6},
\tag{0.1}
\]

where

\[
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u).
\]

This source immediately supersedes the weaker witness used in my preceding `c=0.337` proposal.  In the owner-comparable quadratic-margin normalization, its Poincare denominator is

\[
W={62098577\over239075328}=0.2597448156591047\ldots,
\]

so already

\[
\boxed{c_G>0.4145908383477758.}
\tag{0.2}
\]

Thus the previous `0.337` quadratic candidate is refuted.  The remainder of this report asks whether *some other universally gate-safe additive direction*, with arbitrary shape and no polynomial-degree restriction, can repair this source cheaply at the centre.

## 1. Exact class being tested

Let `F:[-1,1]->[0,infty)` be even and set

\[
\eta(u)=F(1-2u).
\]

Call `F` **universally gate-safe** when for every finite Boolean gate `G` and every interior product bias,

\[
\boxed{
E_F(G;p):=
\sum_i \alpha_i F(m_i)-F(\mu)\ge0,
}
\tag{1.1}
\]

where

\[
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}},
\qquad m_i=1-2p_i,
\qquad \mu=\mathbb E G.
\]

Then adding any nonnegative multiple of `eta` to any potential can never decrease any gate defect.  Since constant gates are included and `F>=0`, (1.1) forces

\[
F(1)=F(-1)=0.
\tag{1.2}
\]

No smoothness, polynomial representation, convexity, differentiability, or finite-dimensional ansatz is assumed below.

The question attacked is:

> How much strong-Numaro defect can any such direction pay per unit centre `F(0)`?

The answer is bounded by a finite collection of exact Boolean selector constraints.

## 2. First exact selector inequality: a tent-map upper recursion

Fix `x in (0,1)`.  Consider the actual two-input selector gate whose selector has bias `t=1-x`, whose `0`-child is the constant `-1`, and whose `1`-child is a balanced literal on a fresh residual bit.

The child means are

\[
a=-1,\qquad b=0,
\]

their disagreement probability is exactly

\[
\delta={1\over2},
\]

the parent mean is `-x`, and the selector mean is `2x-1`.  Applying universal gate safety to this genuine Boolean gate gives

\[
(1-x)F(0)-F(x)+{1\over2}F(|1-2x|)\ge0.
\]

Hence every direction in the class obeys the exact recursion

\[
\boxed{
F(x)\le(1-x)F(0)+{1\over2}F(Tx),
\qquad T(x):=|1-2x|.
}
\tag{2.1}
\]

This is a constraint from one Boolean source.  No arbitrary spectral row or moment relaxation appears.

## 3. Second exact selector inequality: a source-valid lower envelope

For `x in (0,1)`, construct two Boolean child functions on two independent biased residual bits `z,w` as follows:

\[
V=+1\iff z=1,
\qquad
U=+1\iff z=w=1,
\]

with

\[
\Pr(z=1)={1+x\over2},
\qquad
\Pr(w=1)={1-x\over1+x}.
\]

Then

\[
\mathbb EU=-x,
\qquad
\mathbb EV=x,
\qquad
\Pr(U\ne V)=x.
\tag{3.1}
\]

Use a fresh balanced selector between these two children.  Its parent mean is zero and its selector mean is zero.  Equation (1.1) therefore gives

\[
F(x)-F(0)+xF(0)\ge0.
\]

Thus

\[
\boxed{F(x)\ge(1-x)F(0).}
\tag{3.2}
\]

Again this is an explicit product-biased Boolean construction, not a realizability-free scalar row.

## 4. Exact finite tent orbit at the strong witness

The strong Numaro biased input has mean coordinate

\[
x_0={5\over228}.
\]

Its exact tent-map orbit is

\[
\begin{aligned}
x_0&={5\over228},&x_1&={109\over114},&x_2&={52\over57},\\
x_3&={47\over57},&x_4&={37\over57},&x_5&={17\over57},\\
x_6&={23\over57},&x_7&={11\over57},&x_8&={35\over57},\\
x_9&={13\over57},&x_{10}&={31\over57},&x_{11}&={5\over57},
\end{aligned}
\tag{4.1}
\]

and

\[
T(x_{11})=x_3.
\tag{4.2}
\]

Assume first `F(0)>0` and normalize `y_j=F(x_j)/F(0)`.  Iterating (2.1) around the exact period-nine cycle gives

\[
y_3
\le
{\displaystyle\sum_{r=0}^{8}2^{-r}(1-x_{3+r})
 \over 1-2^{-9}}
=\boxed{{6640\over9709}}.
\tag{4.3}
\]

Propagating (2.1) backward through `x_2,x_1,x_0` gives

\[
\boxed{
{F(5/228)\over F(0)}
\le {129023\over116508}
=1.107417516393724\ldots .
}
\tag{4.4}
\]

The strong Numaro output has mean coordinate

\[
x_{\rm out}={5\over1024}.
\]

Applying the independent lower selector (3.2) gives

\[
\boxed{
{F(5/1024)\over F(0)}
\ge {1019\over1024}.
}
\tag{4.5}
\]

No continuity assumption is needed for these rational interior points.

### Zero-centre case

If `F(0)=0`, the nonnegative recursion (2.1) around the same finite cycle forces `F(x_3)=...=F(x_{11})=0`, then the three backward recursions force `F(5/228)=0`.  Nonnegativity gives `F(5/1024)>=0`.  Hence the strong witness receives nonpositive additive payment.  Such a direction cannot repair a negative defect.  Therefore no zero-centre escape is hidden by the normalization above.

## 5. Infinite-dimensional payment/centre barrier

For the strong source (0.1), the additive response of `F` is exactly

\[
L(F)=
{57\over256}F(5/228)
+{465\over256}F(0)
-F(5/1024).
\tag{5.1}
\]

Combining (4.4) and (4.5), every symmetric nonnegative universally gate-safe direction with positive centre satisfies

\[
\boxed{
{L(F)\over F(0)}
\le
{57\over256}{129023\over116508}
+{465\over256}-{1019\over1024}
={279387\over261632}
=1.06786249388454\ldots .
}
\tag{5.2}
\]

This bound is **infinite-dimensional**: it holds for every function `F` in the stated safe cone, not only quartics, sextics, polynomials, smooth functions, or a finite basis.

Consequently, if a repair of the fixed seed has the form

\[
\Gamma=\Gamma^\dagger+\lambda\eta,
\qquad \lambda\ge0,
\]

with `eta(u)=F(1-2u)` in this universally gate-safe nonnegative class, and if it repairs even the single strong source (0.1), then

\[
\lambda F(0)
>
{38023/10^6\over279387/261632}
=oxed{{155438024\over4365421875}}
=0.03560664431773847\ldots .
\tag{5.3}
\]

Thus its centre must obey

\[
\boxed{
\Gamma(1/2)
>
{916034239330909\over139693500000000}
=6.557457858317738\ldots .
}
\tag{5.4}
\]

This is **not** a lower bound on the true FEI constant.  It is a lower barrier for the mechanism “fixed seed `Gamma^dagger` plus a separately nonnegative universally gate-safe additive repair direction”.  A repair allowed to decrease some old gate slacks while remaining globally feasible is outside this theorem, as is changing the seed potential altogether.

## 6. Relation to the other-account degree-six barrier

The completed account03/B16 report

`proofnet24/P03-fei/fleet-2026-09-21/account03/B16/20260922T0913Z-sextic-safe-direction-barrier/REPORT.md`

proves a numerically stronger centre barrier, about `6.558443385`, but only for endpoint-zero symmetric even polynomial safe repairs of degree at most six.  The present theorem is numerically weaker by about `9.86e-4` at the centre, but removes the degree, polynomial and differentiability restrictions entirely.

Therefore the useful conclusion is structural rather than a decimal improvement: **low-degree optimization was not the essential restriction.**  The whole monotone-safe additive cone has a source-valid finite selector dual obstruction on the strong Numaro bias.

## 7. Conditional end-to-end implication and exact remaining gap

A compact route to a full proof would now be:

1. find one finite symmetric nonnegative potential `Gamma`;
2. prove `D_Gamma(G;p)>=0` for every finite Boolean gate and every interior product bias;
3. invoke the already-established all-gate equivalence to obtain `H(f)<=Gamma(1/2) I(f)` for every uniform-cube Boolean function.

The mechanism tested here attempted step 1 by starting from `Gamma^dagger` and moving only in directions which cannot make any existing gate worse.  Theorem (5.4) says that this architecture must pay at least `0.0356066443...` at the centre merely to clear the presently known strong prime witness.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.  No universal finite-cap potential is proved, and no lower bound on the true FEI constant is claimed.

**MECHANISM CHANGE:** yes.  Before this run, the safe-direction obstruction was finite-dimensional (quartic/sextic coefficient optimization) or a single candidate failure.  After this run, arbitrary-shape nonnegative universally gate-safe additive repair directions above the fixed seed obey the exact selector-dual barrier (5.2)-(5.4).

**First remaining implication:** either

- prove a finite coercivity bound for some safe ray at a centre at least compatible with (5.4), thereby paying *all* composition-prime gates, or
- construct a **non-monotone slack-trading/Bellman-shaped potential** (or a different seed) whose changes are not separately gate-safe but whose final total defect is nonnegative everywhere, or
- find a new genuine Boolean gate whose comparable margin exceeds the present strong witness's certified `0.4145908383...` lower bound.

The last option would falsify the current quadratic replacement family more strongly; the first two are proof directions.  No retired global phase/rank/l1, sign-free, ordinary depth, fixed-relative near-subcube, or credit-free local route is revived.

## 8. Verification, provenance, and scope

`CHECKER.py` is standard-library exact `Fraction` arithmetic.  It reconstructs the rational tent orbit, verifies the period-nine recursion, derives (4.3)-(4.5), the exact efficiency fraction (5.2), the centre increment (5.3), the fixed-seed barrier (5.4), and the owner-comparable strong-witness quadratic margin (0.2).  The archived output reports `PASS`.

Scoped privacy/secret review of the changed scientific files: only FEI formulas, rational constants, repository-relative source references and standard-library arithmetic are present.  No credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private material, benchmark gold, email/Drive data, remote workflows, paid APIs/models, Codex calls, public posting, or permission changes are included.
