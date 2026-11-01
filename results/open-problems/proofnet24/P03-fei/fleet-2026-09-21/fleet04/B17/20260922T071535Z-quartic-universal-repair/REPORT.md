# B17 — a universal quartic repair direction after the prime-gate refutation

**Run:** `20260922T071535Z-b17-fei-r17`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REPLACEMENT_CONSTRUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current target and source state

The later owner control converges the FEI fleet on the all-gate formulation.  For a symmetric potential `Gamma`, write

\[
D_\Gamma(G;p)
=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The formerly live fixed candidate

\[
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\tag{0.2}
\]

has now been refuted by the exact composition-prime 18-input Numaro gate at

\[
p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,\qquad
p_{\rm out}=967/2048.
\tag{0.3}
\]

The source-certified defect is

\[
D_{\Gamma^\dagger}
=-0.0176114199558017537894958865691\ldots<0.
\tag{0.4}
\]

This is fleet03/B12
`20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`,
report blob `36fea824c2dcae8c65c3d485e5d5714899699855`.
The exact prime classification is inherited from fleet04/B14
`20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob
`43ad8483eb8a56cb7141a33821ab89e4119dbc49`.

The newest compatible **other-account B15** result consumed substantively is fleet02/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`,
blob `cf93eee18f564475eb441c9118026a1f962084b5`.

Its fixed-candidate five-input tube became conditional historical information after (0.4), but its central structural theorem is potential-agnostic and survives unchanged: for every nonconstant Boolean gate and every symmetric `Gamma`, the entire all-gate defect is exactly a Gibbs relative-entropy credit minus one partition demand,

\[
D_\Gamma(G;p)
=D_{\rm KL,2}(w\|\nu_p)-\log_2 Z-\Gamma(q),
\tag{0.5}
\]

and, after conditioning on the nonempty Fourier atom,

\[
D_\Gamma(G;p)
=V_q\left[
D_{\rm KL,2}(w^+\|\nu_p^+)
-\log_2{Z-1\over x_q}
\right].
\tag{0.6}
\]

Moreover the full conditional KL is exactly preserved by the physical magnitude/original-coordinate-price sufficient statistic.  No KL term is discarded below.

The newest integration result used is fleet04/B18
`20260922T071537Z-prime-repair-shape-barrier/REPORT.md`.  It proves that every additive repair `Gamma^dagger+eta` must satisfy the exact affine prime-witness constraint

\[
{57\over256}\eta(3/8)+{465\over256}\eta(1/2)-\eta(967/2048)
\ge d,
\qquad d=-D_{\Gamma^\dagger},
\tag{0.7}
\]

and that a symmetric concave endpoint-zero repair satisfying its two local shape inequalities must raise the center by at least

\[
{1024\over1121}d
=0.0160875058293853\ldots.
\tag{0.8}
\]

The problem is therefore no longer to optimize the refuted quadratic lift.  It is to build replacement directions that (i) pay (0.7), (ii) do not destroy already-valid gate inequalities, and (iii) preserve the exact information credits.

## 1. New universal repair direction

Define

\[
\boxed{
\eta_4(u):=u(1-u)\bigl(1-2u(1-u)\bigr)
={1-(1-2u)^4\over8}.
}
\tag{1.1}
\]

It is symmetric, nonnegative, endpoint-zero, and concave:

\[
\eta_4''(u)=-6(2u-1)^2\le0,
\qquad
\eta_4(1/2)={1\over8}.
\tag{1.2}
\]

The important point is not merely that `eta_4` is safe for AND.  It is safe for **every Boolean gate of every arity and every product bias**.

### Theorem 1.1 — universal quartic defect monotonicity

Let `G` be any finite Boolean gate and `p in (0,1)^k`.  Put

\[
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}}
=\Pr(\text{input }i\text{ is pivotal}),
\qquad r=p_{\rm out}.
\tag{1.3}
\]

Then

\[
\boxed{
\sum_i \alpha_i\eta_4(p_i)-\eta_4(r)\ge0.
}
\tag{1.4}
\]

Equivalently, for every symmetric potential `Gamma` and every `lambda>=0`,

\[
\boxed{
D_{\Gamma+\lambda\eta_4}(G;p)
\ge D_\Gamma(G;p).
}
\tag{1.5}
\]

Thus adding a positive multiple of `eta_4` can repair gate failures but can never create a new gate failure anywhere in arity or bias space.

### Proof

Use the `+-1` encoding.  Let

\[
\mu=\mathbb E G,
\qquad m_i=1-2p_i.
\]

Because

\[
\eta_4(p_i)={1-m_i^4\over8},
\qquad
\eta_4(r)={1-\mu^4\over8},
\]

(1.4) is equivalent to

\[
\boxed{
1-\mu^4\le\sum_i\alpha_i(1-m_i^4).
}
\tag{1.6}
\]

We prove (1.6) by induction on the number of inputs.  Split on the last input, whose bias is `t`; put `q=1-t`.  Let the two Boolean restrictions have means `a,b in [-1,1]`, disagreement probability `delta`, and total mean

\[
\mu=qa+tb.
\]

For every earlier coordinate, its parent pivotal probability is the `q,t` average of its two child pivotal probabilities.  Therefore the induction hypotheses for the two restrictions reduce the parent step exactly to

\[
qa^4+tb^4-(qa+tb)^4
\le \delta\bigl(1-(q-t)^4\bigr).
\tag{1.7}
\]

Actual Boolean realizability gives

\[
|a-b|\le2\delta,
\tag{1.8}
\]

because `|G_0-G_1|` is two exactly on the disagreement set.  Hence it is enough to prove the scalar inequality

\[
\boxed{
qa^4+tb^4-(qa+tb)^4
\le {|a-b|\over2}\bigl(1-(q-t)^4\bigr)
}
\tag{1.9}
\]

for all `a,b in [-1,1]` and `t in [0,1]`.

Assume `b>=a` and set

\[
d=b-a\in[0,2],\qquad c=qa+tb.
\]

Then

\[
c\in[-1+td,\,1-qd]
\tag{1.10}
\]

and direct expansion gives

\[
qa^4+tb^4-c^4
=d^2tq\left[
6c^2+4cd(q-t)+d^2(1-3tq)
\right].
\tag{1.11}
\]

Also

\[
{d\over2}\bigl(1-(q-t)^4\bigr)
=4dtq(1-2tq).
\tag{1.12}
\]

The bracket in (1.11) is convex as a function of `c`, so after cancelling the trivial factors `dtq` it is enough to check the two endpoints of (1.10).  At `c=1-qd` the difference between the right- and left-hand sides factors as

\[
(2-d)P(d,t),
\tag{1.13}
\]

where

\[
P(d,t)
=(d^2+2d+4)t^2
-(3d^2+2d+4)t
+(3d^2-2d+2).
\tag{1.14}
\]

At the other endpoint the factor is `(2-d)P(d,1-t)`.  The leading coefficient of `P` in `t` is positive and its discriminant is

\[
\Delta_tP=-R(d),
\qquad
R(d)=3d^4+4d^3+12d^2-32d+16.
\tag{1.15}
\]

Now

\[
R''(d)=36d^2+24d+24>0,
\]

so `R'` is strictly increasing.  Exact rational evaluations give

\[
R'(39/50)=-{8893\over31250}<0,
\qquad
R'(4/5)={128\over125}>0.
\tag{1.16}
\]

Thus the unique minimum of `R` lies in `[39/50,4/5]`.  On that interval

\[
R(d)
\ge
3(39/50)^4+4(39/50)^3+12(39/50)^2-32(4/5)+16
={4434123\over6250000}>0.
\tag{1.17}
\]

Therefore `P(d,t)>0` for all real `t`; (1.13) is nonnegative because `d<=2`.  This proves (1.9), then (1.7), then the induction and (1.4).  Degenerate cases `d=0` or `t in {0,1}` follow directly/continuously.  `QED`.

### Interpretation

Equation (1.6) is a product-space fourth-power Poincare inequality specialized to actual Boolean functions.  The Boolean disagreement inequality (1.8) is essential in this proof; no arbitrary spectral probability law is substituted for the Boolean source.

## 2. Exact repair of the known composition-prime witness

For an additive repair, the exact source affine functional from (0.7) is

\[
L(\eta)
={57\over256}\eta(3/8)
+{465\over256}\eta(1/2)
-\eta(967/2048).
\tag{2.1}
\]

For `eta_4` the three values are rational and

\[
\eta_4(1/2)={1\over8},
\qquad
\eta_4(3/8)={255\over2048},
\]

\[
\eta_4(967/2048)
={1099501071775\over8796093022208}.
\tag{2.2}
\]

Hence

\[
\boxed{
L(\eta_4)
={1141515555425\over8796093022208}
=0.12977529370630236\ldots .
}
\tag{2.3}
\]

Take the simple rational scale

\[
\boxed{\lambda={13571\over100000}=0.13571.}
\tag{2.4}
\]

Then the exact defect improvement on the prime witness is

\[
\lambda L(\eta_4)
={619660304106907\over35184372088832000}
=0.017611805108882293\ldots .
\tag{2.5}
\]

The source certificate has

\[
d<0.017611420,
\]

so the repaired potential

\[
\boxed{
\Gamma^{(4)}(u)
:=\Gamma^\dagger(u)+{13571\over100000}\eta_4(u)
}
\tag{2.6}
\]

satisfies the known prime-gate inequality with rigorous slack at least

\[
\boxed{
3.8510888229\times10^{-7}.
}
\tag{2.7}
\]

By Theorem 1.1, every gate/bias pair that was already nonnegative for `Gamma^dagger` remains nonnegative for `Gamma^(4)`.  In particular this replacement repairs the exact known prime witness without sacrificing any previously certified all-gate region.

The center is

\[
\boxed{
\Gamma^{(4)}(1/2)
=6.521851214+{13571\over800000}
=6.538814964.
}
\tag{2.8}
\]

The refutation report showed that repairing the same witness by increasing only the old quadratic coefficient forces the center above `6.53897885`.  Thus this universal quartic direction improves the required cap by at least

\[
\boxed{0.000163886}
\tag{2.9}
\]

relative to the pure-quadratic repair, while being globally gate-safe rather than merely witness-specific.

This is a replacement **construction**, not a universal FEI certificate: there may be other gates for which `Gamma^dagger` had a larger negative defect than the quartic payment at scale (2.4).  The theorem says only that the repair cannot make any gate worse and that it fixes the exact currently known prime obstruction.

## 3. Near the new concave-repair barrier

The B18 shape barrier applies because `eta_4` is itself symmetric, concave and endpoint-zero.  Indeed

\[
\eta_4(3/8)={255\over2048}<\eta_4(1/2)={1\over8}
\]

and

\[
\eta_4(967/2048)
-{967\over1024}\eta_4(1/2)
={61192727967\over8796093022208}
>0.
\tag{3.1}
\]

Thus this explicit construction lies in exactly the repair class for which B18 proved the center-increment lower bound (0.8).  Its increment is

\[
{13571\over800000}=0.01696375,
\]

only

\[
0.0008762441706146\ldots
\]

above the source lower barrier, about `5.45%` relative overhead.  So the prime witness plus binary/read-once constraints do not merely give a barrier: there is now an explicit globally gate-safe concave direction fairly close to that barrier.

## 4. Exact KL credits are preserved

The fleet02/B15 Gibbs identity (0.5)-(0.6) is valid for **every** symmetric potential.  Therefore it applies verbatim to `Gamma^(4)` after redefining

\[
a_i={\Gamma^{(4)}(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad x_i=2^{-a_i},
\qquad Z=\prod_i(1+x_i).
\]

No posterior, magnitude-packet, coordinate-price, empty-atom, or conditional relative-entropy credit is thrown away by the repair.  In particular the exact conditional statement remains

\[
D_{\Gamma^{(4)}}(G;p)
=V_q\left[
D_{\rm KL,2}(w^+\|\nu_{p,(4)}^+)
-\log_2{Z_{(4)}-1\over x_{q,(4)}}
\right].
\tag{4.1}
\]

The quartic theorem is therefore compatible with the strongest current B15 information accounting rather than replacing it by a credit-free scalar surrogate.

## 5. Decisive checks

The adjacent standard-library checker verifies, with exact rational arithmetic:

1. `eta_4(p)=(1-(1-2p)^4)/8` on rational test points;
2. the exact discriminant-bracketing constants in (1.16)-(1.17);
3. all `256` three-bit Boolean truth tables at all `3^3` bias vectors with coordinates in `{1/4,1/2,3/4}` — `6912` exact all-gate increment cases, all nonnegative;
4. the exact affine gain (2.3), rational scale (2.4), rigorous coarse repair slack (2.7), center (2.8), and comparison (2.9);
5. the exact local-shape inequalities (3.1).

The continuum theorem is the analytic induction above; the finite sweep is a stress test, not its proof.

## 6. Old/new missing implication

**Old current implication:** repair or replace `Gamma^dagger` after the exact composition-prime Numaro counterexample, while retaining the already-established gate regions and the full B15 KL credits.

**New proved inference:** `eta_4=(1-(1-2u)^4)/8` is a universal all-gate nonnegative defect direction.  The explicit potential `Gamma^(4)=Gamma^dagger+0.13571 eta_4` repairs the exact known prime obstruction, preserves every gate inequality already valid for `Gamma^dagger`, preserves the full potential-agnostic Gibbs/KL factorization, and has center `6.538814964`, below the center forced by pure quadratic repair.

**New first missing implication:** determine

\[
\sup_{G,p:\,D_{\Gamma^\dagger}(G;p)<0}
{-D_{\Gamma^\dagger}(G;p)
\over
\sum_i\alpha_i\eta_4(p_i)-\eta_4(p_{\rm out})}
\tag{6.1}
\]

with the convention that a zero denominator is an obstruction.  A finite universal bound would immediately turn the quartic direction into a full finite-cap all-gate potential.  A Boolean gate with zero quartic currency and negative `Gamma^dagger` defect would decisively kill this replacement mechanism.  This is now the sharp adversarial test; it should be attacked first on composition-prime gates and biased one-coordinate lines.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.  No novelty or publication-priority claim is made.
