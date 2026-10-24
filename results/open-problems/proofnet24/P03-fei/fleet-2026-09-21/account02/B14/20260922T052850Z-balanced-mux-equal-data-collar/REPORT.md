# account02/B14 — a physical address restriction pays a uniform unequal-data MUX collar

**Classification:** `ESSENTIAL_STEP_APPLIED / PHYSICAL_TERMINAL_SELECTOR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and scientific sources were consumed directly; no installed/native brain receiver context entered the derivation.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. Compact universal chain and first missing implication

The current Campaign-A lead is account01/B18

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`

(blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`). Its fixed candidate is

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\qquad
a^\dagger=0.268204856.
\tag{0.1}
\]

The exact gate reformulation says that

\[
D_{\Gamma^\dagger}(G;p)\ge0
\tag{0.2}
\]

for every composition-prime Boolean gate and every interior product bias implies full FEI with constant `C^dagger`; the gate-composition cocycle then handles decomposable gates. The old AND/decomposable-extremality shortcut is already refuted and is not used here.

The newest directly relevant completed **other-account** result consumed is account01/B15

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T050419Z-mux-negative-posterior-credit/REPORT.md`

(blob `03139b76b82958ede536e9cb4019583974a5dd92`). It retains the exact negative posterior-entropy credit for unequal-data MUX, and on the balanced-address slice reduces the whole remaining statement to one explicit midpoint-potential inequality.

For

\[
M(a,x_0,x_1)=(1-a)x_0+a x_1,
\qquad t=\Pr(a=1)=\frac12,
\]

put

\[
u=1-q_0-q_1,\qquad v=q_1-q_0,\qquad |u|+|v|\le1.
\tag{0.3}
\]

The peer theorem gives the exact identity

\[
\boxed{D_{\Gamma^\dagger}(M;1/2,q_0,q_1)=R_{C^\dagger}(u,v)-J_{\Gamma^\dagger}(u,v)}
\tag{0.4}
\]

with

\[
J_\Gamma(u,v)=
\Gamma\!\left(\frac{1-u}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u-v}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u+v}{2}\right),
\tag{0.5}
\]

and proves the source-independent entropy reserve

\[
\boxed{R_C(u,v)\ge (C-6)\,\delta,
\qquad
\delta=\frac{1-u^2+v^2}{2}.}
\tag{0.6}
\]

Thus the first missing implication on this slice is exactly to pay the midpoint gap `J` with the reserve `R`. The theorem below does this on a uniform, scale-free collar around the equal-data diagonal. Because revealing the physical address bit leaves the two literal gates `x_0,x_1`, whose gate defects are exactly zero, this is simultaneously a **direct physical one-step selective decrement with terminal values**, not merely a scalar gate check.

## 1. Source potential facts actually used

On the small side `0<z<=1/2`, write the source read-once potential as

\[
\Gamma_0(z)=zG(\log_2(1/z)),
\tag{1.1}
\]

with symmetric extension to `z>=1/2`. The committed h96 source diagnostics used already by account01/B18 and account04/B18 give

\[
G(1)=12.9096,
\qquad |G'(x)|<31\quad(x\ge1),
\tag{1.2}
\]

where the derivative statement means the global piecewise-linear slope bound, hence `G` is `31`-Lipschitz even across source nodes. No unavailable candidate bytes are substituted.

The only additional elementary bounds used below are

\[
\frac1{\ln2}<\frac32,
\qquad
-\ln(1-r)\le\frac r{1-r},
\qquad
\ln(1+r)\le r
\quad(0\le r<1).
\tag{1.3}
\]

## 2. Main theorem — a global relative collar around equal data

Define

\[
m:=1-|u|=\min\{q_0+q_1,\,2-q_0-q_1\}.
\tag{2.1}
\]

### Theorem 2.1

For every interior `q_0,q_1 in (0,1)`, if

\[
\boxed{|q_1-q_0|\le\frac1{128}
\min\{q_0+q_1,\,2-q_0-q_1\},}
\tag{2.2}
\]

then the balanced-address MUX satisfies

\[
\boxed{
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)
>0.0187\,m>0.
}
\tag{2.3}
\]

Equivalently, throughout this entire genuinely unequal-data collar, the **physical singleton restriction of the address bit is a paid terminal selector** for the live candidate.

### Proof

The exact formulas are invariant under exchanging the data inputs and under complementing both data bits/output. Hence we may assume

\[
u\ge0,\qquad v\ge0.
\tag{2.4}
\]

Then `m=1-u`. We split according to whether the midpoint interval remains on one side of `1/2`.

### Case I: `v<=u` — both data biases remain on the small side

Put

\[
p=\frac{1-u}{2}=\frac m2,
\qquad
\rho=\frac v{1-u}\le\frac1{128}.
\tag{2.5}
\]

Then the three potential arguments are

\[
p,\qquad p(1-\rho),\qquad p(1+\rho),
\]

all at most `1/2`. Set

\[
x=\log_2(1/p),
\quad
\alpha=-\log_2(1-\rho),
\quad
\beta=\log_2(1+\rho).
\tag{2.6}
\]

For the source part, exact cancellation of the constant `G(x)` gives

\[
\begin{aligned}
J_{\Gamma_0}
={}&-rac p2\Bigl[
(1-\rho)(G(x+\alpha)-G(x))\\
&\hspace{43mm}+(1+\rho)(G(x-\beta)-G(x))
\Bigr].
\end{aligned}
\tag{2.7}
\]

By the source Lipschitz bound,

\[
J_{\Gamma_0}
\le \frac{31p}{2}
\left[(1-\rho)\alpha+(1+\rho)\beta\right].
\tag{2.8}
\]

Using (1.3),

\[
(1-\rho)(-\ln(1-\rho))\le\rho,
\qquad
(1+\rho)\ln(1+\rho)\le\rho+\rho^2,
\]

so

\[
(1-\rho)\alpha+(1+\rho)\beta
<3\rho+\frac32\rho^2.
\tag{2.9}
\]

The quadratic lift has exact midpoint gap

\[
J_{a^\dagger z(1-z)}
=a^\dagger p^2\rho^2
\le\frac{a^\dagger}{2}p\rho^2.
\tag{2.10}
\]

Therefore

\[
J_{\Gamma^\dagger}
< p\left[
\frac{93}{2}\rho+
\left(\frac{93}{4}+\frac{a^\dagger}{2}\right)\rho^2
\right].
\tag{2.11}
\]

At `rho=1/128` the bracket is exactly

\[
\frac{1493846025607}{4096000000000}
=0.364708502345458984375.
\tag{2.12}
\]

Meanwhile

\[
\delta=\frac{1-u^2+v^2}{2}
\ge\frac{1-u^2}{2}
\ge\frac{1-u}{2}=p.
\tag{2.13}
\]

Since `C^dagger-6=0.521851214`, (0.6), (2.11), and (2.12) yield

\[
D_{\Gamma^\dagger}
>p\,
\frac{643656546937}{4096000000000}
>0.15714\,p
>0.07857\,m.
\tag{2.14}
\]

This is much stronger than (2.3).

### Case II: `u<v` — the midpoint interval crosses `1/2`

The collar assumption gives

\[
u<v\le\frac{1-u}{128},
\]

hence

\[
\boxed{u<\frac1{129},\qquad v<\frac1{128}.}
\tag{2.15}
\]

All three potential arguments in (0.5) then lie strictly between `63/128` and `65/128`. On this interval `Gamma^dagger` is `62`-Lipschitz. Indeed, by symmetry it is enough to consider

\[
\frac{63}{128}\le z\le\frac12,
\qquad x=\log_2(1/z).
\]

Here `x<1.05`: since `ln2>2/3`,

\[
2^{1.05}=2e^{(\ln2)/20}>2\left(1+\frac1{30}\right)=\frac{31}{15}>\frac{128}{63}.
\tag{2.16}
\]

Thus (1.2) gives

\[
|G(x)|<12.9096+31(0.05)=14.4596.
\]

On each source segment,

\[
\Gamma_0'(z)=G(x)-\frac{G'(x)}{\ln2},
\]

so

\[
|\Gamma_0'(z)|<14.4596+\frac{93}{2}=60.9596.
\]

The quadratic lift contributes derivative magnitude `<a^dagger<0.269`, hence

\[
\boxed{|(\Gamma^\dagger)'|<62}
\tag{2.17}
\]

on the interval, with the same global Lipschitz conclusion across any piecewise-linear source node.

Write `h=v/2`. The midpoint gap therefore obeys

\[
J_{\Gamma^\dagger}
\le \frac12\bigl(
|\Gamma^\dagger(p)-\Gamma^\dagger(p-h)|
+|\Gamma^\dagger(p)-\Gamma^\dagger(p+h)|
\bigr)
<62h=31v<\frac{31}{128}.
\tag{2.18}
\]

Also (2.15) implies

\[
\delta=\frac{1-u^2+v^2}{2}
>\frac12\left(1-\frac1{129^2}\right).
\tag{2.19}
\]

Hence

\[
\begin{aligned}
D_{\Gamma^\dagger}
&>0.521851214\,
\frac12\left(1-\frac1{129^2}\right)
-\frac{31}{128}\\
&=
\frac{15577995649}{832050000000}
=0.0187224273168679\ldots
>0.0187.
\end{aligned}
\tag{2.20}
\]

Since `m<=1`, this also implies (2.3). The two cases prove the theorem. `square`

## 3. Physical/adaptive interpretation and terminal values

The theorem is not merely a pointwise potential estimate. The policy is the actual physical singleton reveal

\[
\boxed{T=\{a\}}
\tag{3.1}
\]

at the MUX address. Its two children are exactly the one-input identity gates `x_0` and `x_1` at their original biases `q_0,q_1`. For a literal gate `L` at any interior bias,

\[
D_{\Gamma^\dagger}(L)=0,
\tag{3.2}
\]

because `It/V=1`, the output bias equals the input bias, and the biased spectral entropy is exactly `h_2(V)`. Therefore

\[
D_{\Gamma^\dagger}(M)
-\frac12D_{\Gamma^\dagger}(x_0)
-\frac12D_{\Gamma^\dagger}(x_1)
=D_{\Gamma^\dagger}(M),
\tag{3.3}
\]

and Theorem 2.1 is an exact one-step selective decrement with zero terminal debit. No prescribed-coordinate statement is asserted outside this MUX geometry, and no crossing or posterior credit is reused: the account01/B15 exact negative Shannon term is already present in `R_C`.

## 4. Relation to the latest lead and neighboring results

The A lead already proves a different source-valid tube: complementary data `q_1=1-q_0` with address bias

\[
|t-1/2|\le q^2/8192.
\]

Theorem 2.1 is transverse to that result. It keeps the address exactly balanced but releases the **equal-data relation** by a fixed *relative* amount at every data scale. In `(u,v)` coordinates the two covered sets are, respectively, an address tube around the complementary line `u=0` and the new fixed-width collar

\[
|v|\le\frac{1-|u|}{128}
\tag{4.1}
\]

around the equal-data diagonal `v=0`.

The fresh account01/B15 cap-six Boolean-rigidity handoff is compatible but not used to fake coverage: it pays a different shared-character child geometry by an exact sector KL credit. On the remaining MUX frontier the child spectral geometry can have zero such sector credit, so the source-potential midpoint term genuinely has to be controlled rather than replaced by Pinsker/variance.

The fresh account04/B14 balanced-transposition barrier is also consistent: finite one-pair truth-table mutations of the known balanced source prime move strictly *into* the safe half-space at the balanced point. It does not imply the MUX collar and is not used as a universal extremality statement.

## 5. Last-three B14 comparison and mechanism change

The last three persisted substantive account02/B14 reports were:

1. `20260922T000131Z-diagonal-tag-transfer-selector`: a pairwise Fourier-tag collision gave a cheap physical pivot selector on duplicate near-subcube proxy rows;
2. `20260922T0145Z-js-poincare-currency`: the entire coherent Jensen-Shannon restriction bill was paid globally and sharply in exact Poincare currency, leaving pure erasure as the universal tree obstruction;
3. `20260922T0502Z-block-envelope-collapse`: exact block currency plus erasure superadditivity proved that unsigned erasure/Poincare block envelopes can never outperform the best singleton, isolating signed output-potential/exact-entropy credit as the only possible block advantage.

The universal prime-gate implication remained unpaid. This run therefore **changes mechanism** rather than adding another unsigned block ratio: it retains the signed posterior entropy from account01/B15 and controls the remaining live source-potential midpoint gap directly. The resulting selector terminates in one physical step.

**FULL-PROBLEM CHANGE:** none. Full FEI is still open.  
**MECHANISM CHANGE:** yes. A genuinely unequal-data, balanced-address MUX collar is now rigorously paid by a physical terminal selector.

## 6. Exact remaining implication

For balanced-address MUX, the still-unpaid region is the compact interior complement of the already closed faces/lines and Theorem 2.1:

\[
uv\ne0,\qquad |u|+|v|<1,\qquad
|v|>\frac{1-|u|}{128},
\tag{6.1}
\]

subject also to the previously closed complementary-data line and two-input boundary faces. On this slice the exact obligation remains

\[
\boxed{J_{\Gamma^\dagger}(u,v)\le R_{C^\dagger}(u,v).}
\tag{6.2}
\]

Beyond MUX, one must still prove `D_{Gamma^dagger}>=0` for every composition-prime gate and every interior product bias, or produce a genuine prime/bias counterexample to this fixed candidate. The theorem here is an essential source-valid advance on that path, not a full proof.

A useful next step is to combine the same source-Lipschitz cancellation with the exact negative posterior term away from `t=1/2`, aiming for a three-parameter MUX collar without replacing the posterior credit by a sign-free bound.

## 7. Sanity arithmetic and literature status

The two scalar margins used above were checked exactly as rational arithmetic:

\[
(C^\dagger-6)-
\left[
\frac{93}{2}\frac1{128}
+\left(\frac{93}{4}+\frac{a^\dagger}{2}\right)\frac1{128^2}
\right]
=
\frac{643656546937}{4096000000000}>0,
\tag{7.1}
\]

and

\[
(C^\dagger-6)\frac{1-129^{-2}}2-\frac{31}{128}
=
\frac{15577995649}{832050000000}>0.
\tag{7.2}
\]

These arithmetic checks only verify the displayed constants; the theorem is analytic.

A fresh primary-literature check still finds the unrestricted FEI conjecture open: González--MacManus--Pereyra (May 29, 2026) give a restriction-decrement/stopping-tree conditional framework and new verified classes, while Potapov (September 18, 2026) proves FEI for plateaued and partially bent classes rather than universally. No novelty claim is inferred from that search.

## 8. Scope/privacy

Only FEI mathematics, public source-bound repository identifiers, and sanitized provenance appear here. No credentials, scheduler identifiers, machine paths, benchmark gold, email/Drive data, unrelated private information, raw transcripts, paid/remote compute, public posting, permission changes, or production-state promotion are included.
