# B14 — strict coercivity of the universal singleton repair

**Classification:** `ESSENTIAL_STEP_APPLIED / STRICT_SAFE_DIRECTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Live candidate and exact peer consumed

The live replacement from the preceding B14 run is

\[
\Gamma^{\rm new}=\Gamma^\dagger+\lambda\eta,
\qquad
\lambda={867221\over50000000},
\]

with

\[
\eta(p)=\phi(1-2p),\qquad
\phi(m)=1-m^4-\varepsilon(1-m^2)^3,
\qquad
\varepsilon={113009\over5000000}.
\]

Its center is `6.538803618888044`.  The previous theorem proved only the nonnegative all-gate increment

\[
L_\eta(G;p):=\sum_i\alpha_i\eta(p_i)-\eta(p_{\rm out})\ge0,
\qquad
\alpha_i=\Pr(i\text{ pivotal}).
\]

The first unpaid implication was whether this safe direction has enough *strict* coercivity to control new composition-prime gates, rather than merely fixing the known 18-input witness.

This run consumes, with its exact immutable version, account04/B17

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`,
creation commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, report blob `f7a069e0e44ab05ff574807e72973c131c960ca8`.

That report proves a biased Booleanity-KL lower bound and, importantly for the present attack, supplies the exact sparse two-flip family

\[
q_k=2^{2-k},\qquad I-1=(k-2)q_k,
\]

for which a *single* full-active Booleanity equation has a certificate-to-`I-1` ratio tending to zero super-exponentially.  I apply that exact family below to test the new singleton currency rather than merely cite it.

The quantitative scalar input is the exact account02/B12 Bernstein certificate

`proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T081203Z-bellman-repair-completion/CHECKER.py`, blob `7a1b97039601ea02aeb634df84ba974c56228cf3`, whose archived output blob `2f589b293d3525f70e1843c2a6eefdebd5be659b` gives

\[
r_0={1999313322941\over16492674416640000000}
=1.2122432495992445\times10^{-7}>0.
\tag{0.1}
\]

The certificate covers the full cube, so its minimum terminal Bernstein coefficient gives the pointwise lower bound `R>=r_0`, not merely `R>=0`.

## 1. Actual block-selection policy

At every nonconstant restriction state choose any **genuine active original input coordinate** `j` and reveal the singleton physical block `{j}`.  Continue on the two Boolean children, deleting dummy coordinates.  For the known 18-input prime witness one may choose its exceptional `p_1=3/8` coordinate first; the theorem below does not depend on that choice.

No selector labels, support labels, affine changes, or auxiliary bits are introduced.  All signs of the source are kept.

Fix one reveal.  Let its bias be `t in (0,1)`, let the two child means be `a,b`, and put

\[
\delta=\Pr(G_0\ne G_1),\qquad d=|a-b|.
\]

For the paired child values define

\[
Z={G_1-G_0\over2}\in\{-1,0,1\},
\qquad
P_+=\Pr(Z=1),\quad P_-=\Pr(Z=-1),\quad P_0=\Pr(Z=0).
\]

Then, exactly,

\[
\delta=P_++P_-,\qquad {d\over2}=|P_+-P_-|.
\tag{1.1}
\]

Thus the cancellation between positive and negative pivotal fibers is retained rather than replaced by an unsigned influence bound.

## 2. New quantitative local theorem

The preceding B14 factorization, together with the strict Bernstein floor (0.1), yields the following strengthening.

### Theorem 2.1 — signed singleton coercivity

For every Boolean reveal as above,

\[
\boxed{
S_j:=(1-t)\phi(a)+t\phi(b)+\delta\eta(t)
-\phi((1-t)a+tb)
\ge
r_0\,d\,t(1-t)(2-d)
+\left(\delta-{d\over2}\right)\eta(t).
}
\tag{2.1}
\]

Equivalently, using (1.1),

\[
\boxed{
S_j\ge
4r_0\,t(1-t)\,|P_+-P_-|\bigl(1-|P_+-P_-|\bigr)
+2\min(P_+,P_-)\eta(t).
}
\tag{2.2}
\]

Moreover, for interior `t`, equality `S_j=0` occurs **if and only if** one of the following source-valid cases holds:

1. `P_+=P_-=0`: coordinate `j` is pointwise inactive; or
2. `(P_+,P_-)=(1,0)` or `(0,1)`: the whole current gate is exactly `+/-` the literal `j`.

#### Proof

The previous exact factorization writes the local deficit with the minimal Boolean disagreement `d/2` as

\[
G_\varepsilon(d,t,u)
=d\,t(1-t)(2-d)R(d/2,t,u).
\]

The B12 certificate gives `R>=r_0` on the full parameter cube.  Restoring the actual disagreement adds exactly

\[
(\delta-d/2)\eta(t)\ge0,
\]

which proves (2.1), and (1.1) gives (2.2).

For `0<t<1`, `eta(t)>0`, `r_0>0`.  Therefore equality requires simultaneously

\[
d\in\{0,2\},\qquad \delta=d/2.
\]

If `d=0`, then `delta=0`; all product atoms have positive mass, so `G_0=G_1` pointwise and the coordinate is inactive.  If `d=2`, the child means are opposite endpoints `+/-1`, hence both children are constant and the parent is a literal or its negation.  The converse is immediate. `QED`.

This is the requested actual selector statement: every active physical coordinate of a genuinely multi-input gate pays **strictly** at the very first reveal.

## 3. Global equality classification

The restriction identity is exact:

\[
L_\eta(G;p)
=S_j+(1-t)L_\eta(G_0;p_{-j})+tL_\eta(G_1;p_{-j}).
\tag{3.1}
\]

Iterating the physical-block policy gives a decision-tree sum of nonnegative local quantities `S_j`.  Theorem 2.1 immediately yields:

### Corollary 3.1 — complete zero set of the safe direction

For every finite Boolean gate under interior product biases,

\[
\boxed{L_\eta(G;p)=0}
\]

if and only if `G` depends on at most one input: it is a constant, a literal, or a negated literal, possibly with dummy coordinates.

In particular every composition-prime gate with at least two active coordinates has

\[
\boxed{L_\eta(G;p)>0.}
\tag{3.2}
\]

This strengthens the previous nonnegative all-gate theorem into a strict decomposition/equality theorem.  XOR/parity does not create an equality loophole: for a balanced XOR reveal one has `d=0` but `delta=1`, so the second term in (2.1) is strictly positive.

## 4. Explicit interior coercivity

The strictness can be quantified without enumerating gates.  Suppose the current gate has effective arity `m>=2` and

\[
\rho\le p_i\le1-\rho\qquad(0<\rho\le1/2)
\tag{4.1}
\]

on its active coordinates.  Pick any active coordinate `j`.  Every atom of the other `m-1` active variables has probability at least

\[
\mu=\rho^{m-1}.
\]

There are two cases.

*If both pivotal signs occur*, then `min(P_+,P_-)>=mu`.  Since

\[
\eta(t)=V_t(2-V_t-\varepsilon V_t^2)
\ge(1-\varepsilon)V_t
\ge4(1-\varepsilon)\rho(1-\rho),
\]

(2.2) gives

\[
S_j\ge8(1-\varepsilon)\rho^m(1-\rho).
\tag{4.2}
\]

*If only one pivotal sign occurs*, activity gives `delta>=mu`.  Because the gate is not a literal, there is also a nonpivotal atom, so `1-delta>=mu`.  Then `d=2delta` and

\[
S_j\ge4r_0\rho(1-\rho)\delta(1-\delta)
\ge4r_0\rho^m(1-\rho)(1-\rho^{m-1}).
\tag{4.3}
\]

The second bound is the smaller one, hence every genuinely multi-input gate on the strip (4.1) satisfies

\[
\boxed{
L_\eta(G;p)
\ge
4r_0\rho^m(1-\rho)(1-\rho^{m-1})>0.
}
\tag{4.4}
\]

Consequently, for any bounded nonnegative symmetric base potential `Gamma`, writing `M=||Gamma||_infty`, the crude universal estimate `Ht_G<=m` gives

\[
D_\Gamma(G;p)\ge-(M+m).
\]

Therefore all genuinely `m`-input gates on the compact bias strip are repaired by

\[
\Gamma+\Lambda_{m,\rho}\eta,
\qquad
\Lambda_{m,\rho}
={M+m\over4r_0\rho^m(1-\rho)(1-\rho^{m-1})}.
\tag{4.5}
\]

This is not dimension-independent, but it is an exact **finite-arity interior completion theorem**.  A counterexample sequence to any fixed finite scaling of the safe direction cannot remain simultaneously in bounded effective arity and a fixed interior bias strip.  The only surviving escape routes are arity growth and/or approach to a biased boundary.

## 5. Application to the named sparse-defect obstruction

Account04/B17's exact two-flip family was designed to show that the *single full-active Booleanity equation* can lose essentially all influence-relative strength.  On the balanced uniform slice our currency behaves very differently.  Since every input bias and the output bias equal `1/2`,

\[
L_\eta=(1-\varepsilon)(I-1).
\]

Using its exact identity `I-1=(k-2)2^{2-k}` gives

\[
\boxed{
L_\eta(g_k)
=(1-\varepsilon)(k-2)2^{2-k}.
}
\tag{5.1}
\]

Thus the singleton repair stays exactly on the natural influence-excess scale for this source, while the peer's one-equation Booleanity certificate is at most order `q_k^{k-1}`.  The sparse-defect adversary therefore does **not** kill the new physical-block currency; it instead identifies why one must not replace the full restriction mechanism by a single global quadratic equation.

The same balanced-uniform identity automatically applies to majority, balanced tribes, addressing instances, and balanced tensor/self-composition tests:

\[
L_\eta=(1-\varepsilon)(I-1)\ge0.
\]

No every-coordinate entropy-payment assertion is made.  Arbitrary biased limits remain visible in (4.4): the coercive bound is allowed to decay as `rho -> 0`, so this result does not smuggle in a false boundary-uniform assumption.  No half-band positive-current estimate is used.

## 6. Conditional end-to-end chain and the first unpaid arrow

The current chain is now:

1. full FEI is equivalent to one finite symmetric nonnegative potential with nonnegative defect for every Boolean gate/bias;
2. `Gamma^dagger` is refuted by the known biased 18-input prime gate;
3. the explicit `eta` direction is universally gate-safe and `Gamma^new=Gamma^dagger+lambda eta` repairs that witness;
4. **new here:** `eta` is strictly gate-improving on every genuinely multi-input gate at every interior bias, with exact zero set only constants/literals and the explicit compact-strip lower bound (4.4);
5. hence no fixed-arity, uniformly interior family can be the reason that arbitrary finite scaling of `eta` fails;
6. **still missing:** a dimension- and boundary-uniform comparison
   \[
   [-D_{\Gamma^\dagger}(G;p)]_+
   \le K\,L_\eta(G;p)
   \tag{6.1}
   \]
   with one finite `K`, or an explicit source-valid sequence showing that this ratio diverges.

Equation (6.1), with finite `K`, would immediately produce a complete all-gate potential `Gamma^dagger+K eta` and hence full FEI.  The exact next attack should therefore target the only two remaining escape mechanisms isolated above: high effective arity and biased-boundary degeneration, while retaining the signed two-channel decomposition in (2.2).

**Old missing implication:** determine whether the safe repair has target-level coercivity beyond the single repaired witness.  
**New proved implication:** exact local signed coercivity, complete equality classification, and explicit finite-arity/interior completion.  
**New missing implication:** the arity- and boundary-uniform ratio bound (6.1), or a genuine Boolean counterexample sequence to it.  
**Classification:** `ESSENTIAL_STEP_APPLIED`.  **Full FEI remains OPEN.**

Scope/privacy review: mathematics and repository-relative scientific identifiers only; no credentials, machine paths, scheduler IDs, email/Drive content, benchmark gold, public posting, paid/remote compute, workflow dispatch, permission changes, or unrelated private data.
