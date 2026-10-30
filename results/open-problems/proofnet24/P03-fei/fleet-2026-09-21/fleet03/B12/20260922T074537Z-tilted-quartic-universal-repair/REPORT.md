# fleet03/B12 — tilted-quartic universal repair and a sharpness bracket

**Run:** `20260922T074537Z-fleet03-B12-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REPLACEMENT_CONSTRUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current source-exact target

The current owner control supersedes the older spectral-code-only duty and converges the FEI fleet on the all-gate formulation.  For a symmetric potential `Gamma`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

A single symmetric nonnegative finite-cap `Gamma` with `D_Gamma(G;p)>=0` for every finite Boolean gate and every interior product bias is equivalent to full FEI.

The previously fixed candidate

\[
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

is already refuted by the exact composition-prime 18-input Numaro gate at

\[
p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,\qquad p_{\rm out}=967/2048,
\]

with source-certified defect

\[
D_{\Gamma^\dagger}=-0.0176114199558017537894958865691\ldots<0.
\]

So the current obligation is to construct a replacement potential that repairs this and every other gate, or produce another source-valid obstruction.

## 1. Named other-account result consumed

This run consumes fleet04/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T071535Z-quartic-universal-repair/REPORT.md`.

That report proves the universally gate-safe quartic direction

\[
\eta_4(u)={1-(1-2u)^4\over8},
\]

namely

\[
\sum_i \alpha_i\eta_4(p_i)-\eta_4(p_{\rm out})\ge0,
\qquad
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}},
\]

for every Boolean gate and every product bias.  It repairs the known prime witness with scale `0.13571`, producing center `6.538814964`, but does not prove that all previously negative gates have been repaired.

The present run applies that exact mechanism to the missing implication and strengthens the repair direction itself.

## 2. New universal gate-safe direction

Put

\[
F_*(m):=1-m^4-{1\over36}(1-m^2)^2,
\qquad
\eta_*(u):={F_*(1-2u)\over8}.
\tag{2.1}
\]

Then

\[
F_*(m)=(1-m^2)\left({35\over36}+{37\over36}m^2\right)\ge0
\qquad(|m|\le1),
\tag{2.2}
\]

so `eta_*` is symmetric, nonnegative and endpoint-zero.

### Theorem 2.1 — universal tilted-quartic defect monotonicity

For every finite Boolean gate `G` and every interior product bias vector `p`, let

\[
\mu=\mathbb E G,
\qquad m_i=1-2p_i,
\qquad
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}}
=\Pr(i\hbox{ is pivotal}).
\]

Then

\[
\boxed{
\sum_i \alpha_i F_*(m_i)\ge F_*(\mu).
}
\tag{2.3}
\]

Equivalently,

\[
\boxed{
\sum_i \alpha_i\eta_*(p_i)-\eta_*(p_{\rm out})\ge0.
}
\tag{2.4}
\]

Therefore for every symmetric potential `Gamma` and every `lambda>=0`,

\[
\boxed{
D_{\Gamma+\lambda\eta_*}(G;p)\ge D_\Gamma(G;p)
}
\tag{2.5}
\]

for every gate and bias vector.  Thus this direction can repair failures but can never create a new one.

### Proof

Induct on the arity.  Split on the last input, with bias `t` and `q=1-t`.  Let the two restrictions have means `a,b in [-1,1]`, disagreement probability `delta`, and parent mean

\[
c=qa+tb.
\]

For every earlier coordinate the parent pivotal probability is the `q,t` average of its child pivotal probabilities.  Applying the induction hypothesis to the two children therefore reduces (2.3) exactly to

\[
qF_*(a)+tF_*(b)-F_*(c)+\delta F_*(q-t)\ge0.
\tag{2.6}
\]

Boolean realizability gives

\[
\delta\ge {|a-b|\over2},
\tag{2.7}
\]

because `|G_0-G_1|=2` exactly on the disagreement set.  Since `F_*>=0`, it is enough to prove (2.6) with `delta=|a-b|/2`.

Assume `b>=a`, set

\[
d=b-a\in[0,2],
\]

and retain `c=qa+tb`.  Feasibility gives

\[
c\in[-1+td,\,1-qd].
\tag{2.8}
\]

A direct expansion yields

\[
qF_*(a)+tF_*(b)-F_*(c)+{d\over2}F_*(q-t)
=dtq\,B(c,d,t),
\tag{2.9}
\]

where the coefficient of `c^2` in `B` is

\[
-{37d\over6}\le0.
\tag{2.10}
\]

Hence `B` is concave in `c`, so its minimum on (2.8) occurs at an endpoint.  The two endpoints are interchanged by `t<->1-t`; it is enough to take `c=1-qd`.  There one obtains the exact factorization

\[
36B=(2-d)P(d,t),
\tag{2.11}
\]

with

\[
P(d,t)=
(37d^2+74d+148)t^2
-(111d^2+74d+148)t
+111d^2-74d+72.
\tag{2.12}
\]

The leading coefficient is positive and the discriminant in `t` is

\[
\operatorname{Disc}_t P=-37R(d),
\]

\[
R(d)=111d^4+148d^3+436d^2-1200d+560.
\tag{2.13}
\]

Now

\[
R''(d)=4(333d^2+222d+218)>0,
\]

so `R'` is strictly increasing.  Exact evaluations are

\[
R'(79/100)=-{3777571\over250000}<0,
\qquad
R'(4/5)={1136\over125}>0.
\tag{2.14}
\]

Thus the unique minimizer of `R` lies in `[79/100,4/5]`.  On that interval, convexity and monotonicity give

\[
|R'(d)|\le {3777571\over250000},
\]

and since

\[
R(4/5)={176\over625},
\]

we get the explicit rational bound

\[
R(d)\ge {176\over625}
-{1\over100}{3777571\over250000}
={3262429\over25000000}>0.
\tag{2.15}
\]

Outside `[79/100,4/5]`, strict monotonicity of `R` away from its unique minimizer gives an even larger value.  Hence `R(d)>0` throughout `[0,2]`, so `Disc_t P<0` and `P(d,t)>0` for all real `t`.  Equation (2.11), then (2.9), proves the scalar step.  Degenerate cases `d=0` or `t in {0,1}` follow directly.  The induction closes.  QED.

## 3. A sharpness bracket inside this one-parameter family

The coefficient `1/36` is not an arbitrary tiny perturbation.  Increasing it to `1/35` already destroys universal gate safety.

Define

\[
F_{35}(m)=1-m^4-{1\over35}(1-m^2)^2.
\]

Take the two-input Boolean gate obtained by a selector whose restrictions have means

\[
a={1\over5},\qquad b=1,
\]

with selector bias

\[
t={3\over5},\qquad q={2\over5}.
\]

This is an actual Boolean two-input OR/MUX configuration: the disagreement probability is

\[
\delta={2\over5}={|b-a|\over2},
\]

and the parent mean is

\[
c={17\over25}.
\]

Its proposed `F_35` defect is exactly

\[
qF_{35}(a)+tF_{35}(b)-F_{35}(c)+\delta F_{35}(q-t)
=-{3744\over13671875}<0.
\tag{3.1}
\]

Therefore the universal safety statement is **REFUTED** at coefficient `1/35`.

Consequently, if `theta_*` denotes the supremal subtraction coefficient for which

\[
1-m^4-\theta(1-m^2)^2
\]

is universally gate-safe, then this run rigorously brackets it by

\[
\boxed{
{1\over36}\le\theta_*<{1\over35}.
}
\tag{3.2}
\]

This is a genuine Boolean obstruction, not a non-Boolean spectral relaxation.

## 4. Exact improvement on the known Numaro prime witness

For the known prime witness, fleet04/B18 gives the exact additive-repair functional

\[
L(\eta)=
{57\over256}\eta(3/8)
+{465\over256}\eta(1/2)
-\eta(967/2048).
\tag{4.1}
\]

For `eta_*`,

\[
\eta_*(1/2)={35\over288},
\tag{4.2}
\]

and exact rational evaluation gives

\[
\boxed{
L(\eta_*)=
{39974940944389\over316659348799488}
=0.12623957289099824\ldots .
}
\tag{4.3}
\]

Take the rational scale

\[
\boxed{\lambda_*={34877\over250000}=0.139508.}
\tag{4.4}
\]

Then

\[
\lambda_*L(\eta_*)
={1394206015317455153\over79164837199872000000}
=0.01761143033487738\ldots .
\tag{4.5}
\]

The source certificate has `d=-D_{Gamma^dagger}<0.017611420`, so the repaired witness has rigorous positive slack exceeding

\[
1.03\times10^{-8}.
\]

Define

\[
\boxed{
\Gamma^*(u)=\Gamma^\dagger(u)+{34877\over250000}\eta_*(u).
}
\tag{4.6}
\]

Its center increment is exactly

\[
\lambda_*\eta_*(1/2)
={244139\over14400000}
=0.01695409722222222\ldots,
\]

so

\[
\boxed{
\Gamma^*(1/2)=6.538805311222222\ldots .
}
\tag{4.7}
\]

The fleet04/B17 pure-quartic repair center was `6.538814964`.  Thus this universally safe tilted-quartic repair lowers the cap needed to fix the same source-certified prime obstruction by

\[
\boxed{9.652777777\ldots\times10^{-6}.}
\tag{4.8}
\]

More importantly than the small numerical improvement, Theorem 2.1 gives a new exact safe direction and (3.2) identifies a nearby Boolean obstruction to pushing this particular deformation much further.

## 5. Status and implication to full FEI

**Candidate version:** `TILTED-QUARTIC-GATE-REPAIR-v1`, equation (4.6).

**Prior missing implication:** after `Gamma^dagger` was refuted, construct a replacement finite-cap symmetric nonnegative potential that repairs the known composition-prime witness without destroying any gate/bias pair already paid by `Gamma^dagger`, and then establish all remaining prime gates.

**Consumed peer artifact:** fleet04/B17 `20260922T071535Z-quartic-universal-repair`, which supplied the universal quartic mechanism and the known-witness repair baseline.

**New proved inference:** `eta_*` is universally gate-safe for every arity and product bias; scaled as in (4.4), it repairs the exact known Numaro prime witness while preserving every previously nonnegative gate inequality.  Within the natural one-parameter deformation `1-m^4-theta(1-m^2)^2`, universal safety holds at `theta=1/36` and fails at `theta=1/35` on an explicit two-input Boolean gate.

**Replacement obligation / remaining implication:** prove

\[
D_{\Gamma^*}(P;p)\ge0
\]

for **every** finite composition-prime Boolean gate and every interior product bias, or find a new source-valid negative witness.  Only then does the composition cocycle plus all-gate equivalence yield full FEI, with finite constant `Gamma^*(1/2)`.  This universal arrow remains OPEN.

**Next attack:** solve the exact scalar extremal problem for `theta_*` in the bracket (3.2), then test the resulting optimally safe direction immediately against the known biased prime catalogue.  A richer safe polynomial basis should be considered only if it gives a strictly better witness-payment/center ratio while retaining a universal gate theorem.

**Next recipients:** fleet03/B18 (B lead/integration), fleet04/B17 (universal repair direction), and fleet04/B18 (prime-repair shape barrier).

## 6. Operational truth status

The canonical current-hour login write was attempted before substantive work and was blocked by platform safety.  It was not retried or bypassed.  No authenticated brain retrieval or receiver-context use occurred, so this run is `WITHOUT_VERIFIED_BRAIN` and does not claim full-brain connectivity.  No scheduler mutation, email, Drive action, public post, remote workflow, paid API/model call, Codex call, credential access, or unrelated private-data access was performed.
