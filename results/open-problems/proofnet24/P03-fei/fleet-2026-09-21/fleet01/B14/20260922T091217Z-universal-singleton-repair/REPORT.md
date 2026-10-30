# B14 — a universally safe shaped repair from an actual singleton-restriction policy

**Classification:** `ESSENTIAL_STEP_APPLIED / UNIVERSAL_SINGLETON_RESTRICTION_REPAIR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact live target and mechanism change

The live target is still a finite symmetric potential `Gamma` whose Boolean gate defect is nonnegative for every finite gate and every interior product bias.  The source-exact fixed lift

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

is refuted by the exact composition-prime 18-input Numaro gate at

\[
p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,
\qquad p_{\rm out}=967/2048,
\]

with

\[
D_{\Gamma^\dagger}=-d,
\qquad
d=0.0176114199558017537894958865691\ldots .
\tag{0.1}
\]

The preceding B14 run produced a 35-AND positive dual which ruled out financing a same-center repair from only the *uniform* quadratic reserve.  The exact compatible other-account result consumed and applied here is fleet02/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T082907Z-actual-and-slack-dual/REPORT.md`
(blob `29f2babb2b70fa77ffb278cc0ea6e582b5f85166`).  It evaluates the actual nonuniform AND slack on that same dual and proves

\[
\sum_j\lambda_jD_{\Gamma^\dagger}(AND;p_j,q_j)
=0.18372439190844233245\ldots>10.43d.
\tag{0.2}
\]

So the old aggregate-dual obstruction is genuinely dead: the actual AND bank is large enough in aggregate.  Repeating or slightly improving that dual would not address the first missing inference.  This run therefore executes a different method: construct a shaped direction which is paid by **literal restrictions on original coordinates**, pointwise for every Boolean gate.

I also consume the exact fleet02/B12 artifact

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T081203Z-bellman-repair-completion/CHECKER.py`,
checker commit `e0db54d4170e2884d98188742f7e2cb27f5c7875`, checker blob `7a1b97039601ea02aeb634df84ba974c56228cf3`, and output blob `2f589b293d3525f70e1843c2a6eefdebd5be659b`.

That artifact contains an exact Bernstein certificate for a scalar polynomial and exact repair constants, but no accompanying theorem statement.  The derivation below identifies precisely what that scalar certificate proves: a universal original-coordinate restriction inequality.  No claim from an absent peer report is assumed.

## 1. Actual block-selection policy

At every nonconstant gate/restriction state, choose a **genuine remaining input coordinate** `k` and reveal the singleton physical block

\[
A=\{k\}.
\]

No selector label, Fourier-support label, affine change of variables, or auxiliary coordinate is introduced.  For the current 18-input critical witness, take the exceptional biased coordinate `k=1` first and then reveal the remaining original coordinates in any fixed order.  The theorem below in fact shows that *every* choice of the next physical coordinate is safe for the new repair currency, so no coverage or greedy-core assumption is needed.

For a Boolean gate `G` under product biases, write

\[
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}}
=\Pr(i\text{ is pivotal}),
\qquad V_u=4u(1-u).
\]

The policy will telescope because parent pivotal probabilities of coordinates other than the revealed coordinate are exactly the bias-weighted averages of the corresponding child pivotal probabilities.

## 2. The shaped repair direction

Put

\[
\varepsilon={113009\over5000000}=0.0226018
\]

and, in mean coordinates `m in [-1,1]`, define

\[
\phi(m)=1-m^4-\varepsilon(1-m^2)^3.
\tag{2.1}
\]

For a Bernoulli bias `p`, define the symmetric endpoint-zero repair

\[
\boxed{\eta(p)=\phi(1-2p).}
\tag{2.2}
\]

It is nonnegative.  Indeed, with `x=m^2`,

\[
\phi(m)=(1-x)\bigl[1+x-\varepsilon(1-x)^2\bigr]\ge0
\]

because `0<=x<=1` and `0<epsilon<1`.  Also

\[
\eta(0)=\eta(1)=0,
\qquad
\eta(1/2)=1-\varepsilon={4886991\over5000000}.
\]

The point of the small sixth-order correction is that it improves the known prime witness while remaining universally restriction-safe.  A pure sixth-power direction is not safe; the consumed exact checker gives the genuine two-input NAND countervalue

\[
-{24703056\over244140625}<0.
\]

## 3. One physical reveal: exact local inequality

Fix a revealed original coordinate `k` with bias `t`, and put `q=1-t`.  Let the two Boolean restrictions have means

\[
a=\mathbb E G_{k=0},\qquad b=\mathbb E G_{k=1},
\]

and let

\[
\delta=\Pr(G_{k=0}\ne G_{k=1})=\alpha_k.
\]

The parent mean is

\[
c=qa+tb.
\]

Actual Boolean realizability, with signs retained, gives the sharp elementary constraint

\[
|a-b|
=|\mathbb E(G_{k=1}-G_{k=0})|
\le \mathbb E|G_{k=1}-G_{k=0}|
=2\delta.
\tag{3.1}
\]

### Lemma 3.1 — local singleton payment

For all `a,b in [-1,1]` and `t in [0,1]` arising as above,

\[
\boxed{
q\phi(a)+t\phi(b)+\delta\phi(1-2t)-\phi(qa+tb)\ge0.
}
\tag{3.2}
\]

### Proof

Since `phi>=0`, (3.1) reduces the problem to replacing `delta` by `d/2`, where

\[
d=|a-b|\in[0,2].
\]

Interchanging the two children if necessary, take `b>=a`.  There is a unique `u in [0,1]` such that

\[
a=-1+u(2-d),\qquad b=a+d,
\]

and therefore

\[
c=-1+td+u(2-d).
\]

Define

\[
G_\varepsilon(d,t,u)
=(1-t)\phi(a)+t\phi(b)
+{d\over2}\phi(1-2t)-\phi(c).
\tag{3.3}
\]

Direct exact expansion factors this polynomial as

\[
\boxed{
G_\varepsilon(d,t,u)
=d\,t(1-t)(2-d)\,R(d/2,t,u),
}
\tag{3.4}
\]

where `R(X,T,U)` has degree at most four in each variable.  The consumed B12 checker stores every rational power coefficient of this exact `R`, converts it exactly to the tensor Bernstein basis on `[0,1]^3`, and recursively bisects only boxes whose Bernstein lower hull is not yet nonnegative.  It terminates with

- 134 certified terminal boxes,
- 153 total boxes,
- maximum subdivision depth 6,
- no unresolved boxes, and
- minimum terminal Bernstein coefficient

\[
{1999313322941\over16492674416640000000}
=1.2122432495992445\times10^{-7}>0.
\tag{3.5}
\]

Hence `R>=0` throughout `[0,1]^3`.  All prefactors in (3.4) are nonnegative, proving (3.3), and therefore (3.2).  Boundary cases are included because one of the explicit prefactors vanishes.  QED.

This identifies the exact mathematical content of the peer's scalar certificate: it is not a finite gate test.  It proves the local inequality for a continuum of all admissible child means, pivot biases and Boolean disagreement levels.

## 4. Universal theorem by the actual restriction policy

### Theorem 4.1 — universal shaped repair monotonicity

For every finite Boolean gate `G` and every interior product-bias vector `p`,

\[
\boxed{
\sum_i\alpha_i\eta(p_i)-\eta(p_{\rm out})\ge0.
}
\tag{4.1}
\]

Consequently, for every symmetric potential `Gamma` and every `lambda>=0`,

\[
\boxed{
D_{\Gamma+\lambda\eta}(G;p)
\ge D_\Gamma(G;p)
}
\tag{4.2}
\]

for every Boolean gate, every arity and every product bias.

### Proof

Induct on the number of genuinely active original coordinates.  A constant gate has output mean `+/-1`, so `eta(p_out)=0` and the assertion is trivial.

At a nonconstant node, execute the policy of Section 1 and reveal one actual coordinate `k`.  For every earlier/unrevealed coordinate `i`, its parent pivotal probability is exactly

\[
\alpha_i^{parent}=q\alpha_i^{(0)}+t\alpha_i^{(1)}.
\tag{4.3}
\]

Apply the induction hypothesis to both Boolean children and average with weights `q,t`.  This pays

\[
q\phi(a)+t\phi(b)
\]

from the unrevealed coordinates.  The revealed coordinate contributes exactly

\[
\alpha_k\eta(t)=\delta\phi(1-2t).
\]

Lemma 3.1 says that these contributions dominate the parent term `phi(c)=eta(p_out)`.  This proves (4.1).  Equation (4.2) follows because an additive change of potential changes the gate defect by exactly the left side of (4.1).  QED.

Thus the block policy is literal and source-valid: singleton physical restrictions telescope all the way to constants, and every local debit is paid before proceeding to the next original coordinate.

## 5. Exact repair of the current composition-prime witness

For the exact 18-input prime witness, the additive repair functional is

\[
L(\eta)
={57\over256}\eta(3/8)
+{465\over256}\eta(1/2)
-\eta(967/2048).
\tag{5.1}
\]

Here the mean coordinates are `1/4`, `0`, and `57/1024`.  Exact rational arithmetic gives

\[
\boxed{
L(\eta)
={5853348229889641167388287
\over5764607523034234880000000}
=1.015394058745685\ldots .
}
\tag{5.2}
\]

Take

\[
\boxed{
\lambda={867221\over50000000}=0.01734442.
}
\tag{5.3}
\]

Then

\[
\lambda L(\eta)
=0.017611421020389834\ldots
>0.017611420
>d.
\tag{5.4}
\]

The margin above the source-exact deficit (0.1) is approximately

\[
1.06458808\times10^{-9}>0.
\]

Therefore the replacement

\[
\boxed{
\Gamma^{new}(p)
=\Gamma^\dagger(p)+{867221\over50000000}\eta(p)
}
\tag{5.5}
\]

repairs the exact currently known composition-prime obstruction, and Theorem 4.1 guarantees that it cannot make **any** Boolean gate/bias defect smaller than it was under `Gamma^dagger`.

Its center is exactly

\[
\boxed{
\Gamma^{new}(1/2)
=6.521851214
+{4238101222011\over250000000000000}
=6.538803618888044.
}
\tag{5.6}
\]

For comparison, the completed fleet04/B17 universally safe quartic repair has center `6.538814964`.  The new shaped restriction-safe repair lowers that center by

\[
\boxed{1.1345111956\times10^{-5}.}
\tag{5.7}
\]

This is a strict improvement inside the class of explicitly proved globally gate-safe repairs of the known prime witness.

## 6. Obstruction hygiene

The theorem does not posit that some coordinate has large influence or that every coordinate individually pays an FEI entropy term.  It therefore is not defeated by large majority, tribes, diffuse tensor constructions, sparse defects, or addressing.  Those sources simply generate particular values of `(a,b,t,delta)` in Lemma 3.1, already covered by the continuum certificate.  The proof also includes arbitrary biased limits by continuity and keeps the actual signed Boolean constraint (3.1); it is not a spectral-probability relaxation.

No half-band positive-current estimate is used.  In particular, the refuted all-Boolean `O(J)` positive-current budget from the source-current correction is not silently reintroduced.

## 7. Conditional end-to-end chain and the exact remaining gap

A compact conditional chain is now:

1. the all-gate potential theorem reduces full FEI to one finite symmetric nonnegative potential with nonnegative defect for every finite Boolean gate/bias;
2. composition reduction allows one to search the composition-prime gates;
3. `Gamma^dagger` was refuted by the explicit biased 18-input prime gate;
4. Theorem 4.1 constructs an explicit universal safe direction, and (5.5) repairs that gate while preserving every defect already nonnegative for `Gamma^dagger`;
5. **still missing:** prove
   \[
   D_{\Gamma^{new}}(P;p)\ge0
   \]
   for every composition-prime Boolean gate and every interior product bias, or produce a new prime counterexample to this exact replacement.

The theorem does **not** infer that fixing the currently known worst witness closes the universal quantifier.  In particular, finite tests, the 35-AND bank, and the exact repair of one prime gate do not settle FEI.

## 8. Old/new missing implication and classification

**Old first missing inference:** after the 35-AND uniform-bank obstruction, determine whether actual nonuniform AND slack still blocks every shaped repair.  Fleet02/B16 proves that aggregate obstruction fails by more than a factor ten.

**Executed different attack:** replace dual obstruction by an actual physical singleton-restriction construction.

**New proved implication:** the explicit direction

\[
\eta(p)=1-(1-2p)^4-{113009\over5000000}\,[1-(1-2p)^2]^3
\]

is universally Boolean-gate-safe, with a proof that is literally an induction over genuine singleton restriction blocks.  At scale `867221/50000000` it repairs the exact biased 18-input prime witness and gives center `6.538803618888044`, strictly improving the earlier safe quartic repair center.

**New first essential missing implication:** either prove the all-prime inequality for the exact replacement `Gamma^new` in (5.5), or construct an explicit composition-prime Boolean gate/bias with negative `D_{Gamma^new}`.  Any next shaped repair must preserve the local singleton inequality (3.2) or replace it with another genuinely paid physical-block mechanism.

**Classification:** `ESSENTIAL_STEP_APPLIED`.  **Full FEI remains OPEN.**

Privacy/scope review: this report contains only FEI mathematics, repository-relative source identifiers, exact constants and logical account/slot labels.  It contains no credentials, scheduler IDs, machine paths, email/Drive content, public posting, paid/remote compute, workflow dispatch, permission changes, benchmark gold, or unrelated private data.
