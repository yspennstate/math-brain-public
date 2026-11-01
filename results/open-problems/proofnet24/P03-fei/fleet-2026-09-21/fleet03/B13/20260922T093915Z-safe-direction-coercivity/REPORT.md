# fleet03/B13 — the universal singleton-safe repair has no nontrivial zero mode

**Outcome:** `AUXILIARY_ONLY / UNIVERSAL_STRICT_SAFE_DIRECTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control and mathematical sources were used, but no authenticated mathematical-brain retrieval plus receiver-context result entered the mathematics.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/publication priority:** not assessed; no priority claim.

## 0. Live target, exact candidate, and peer result consumed

The live natural-language owner control at revision `2026-09-22.2` supersedes the older fleet03/B13 interface-B-only assignment where they conflict and asks all FEI workers to converge on the all-gate formulation. The universal target is one finite symmetric nonnegative potential `Gamma` such that, for every finite Boolean gate `G` and every interior product-bias vector `p`,

\[
D_\Gamma(G;p):=
\sum_i {\rm It}_i(G;p)
 {\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}}
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The previous fixed candidate

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\tag{0.2}
\]

is source-exactly refuted by the biased composition-prime 18-input Numaro gate at

\[
p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,
\tag{0.3}
\]

with deficit

\[
d=0.0176114199558017537894958865691\ldots .
\tag{0.4}
\]

The named compatible **other-account** result consumed and applied in this run is:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B14/20260922T091217Z-universal-singleton-repair/REPORT.md`, commit `63189a15a82c34331909a42fe35786109f3c8a29`.

That report proves a new universally gate-safe repair direction. Put

\[
\varepsilon={113009\over5000000}=0.0226018,
\qquad
\phi(m)=1-m^4-\varepsilon(1-m^2)^3,
\tag{0.5}
\]

and

\[
\eta(p)=\phi(1-2p).
\tag{0.6}
\]

For

\[
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}}
=\Pr(i\text{ is pivotal}),
\tag{0.7}
\]

define its gate currency

\[
M_\eta(G;p)=\sum_i\alpha_i\eta(p_i)-\eta(p_{\rm out}).
\tag{0.8}
\]

The peer theorem proves

\[
M_\eta(G;p)\ge0
\tag{0.9}
\]

for **every** Boolean gate and every product bias. Hence

\[
D_{\Gamma+\lambda\eta}(G;p)
=D_\Gamma(G;p)+\lambda M_\eta(G;p)
\ge D_\Gamma(G;p)
\tag{0.10}
\]

for every `lambda>=0`.

It uses

\[
\lambda={867221\over50000000}=0.01734442
\tag{0.11}
\]

to repair the known 18-input witness, producing

\[
\Gamma^{\rm new}=\Gamma^\dagger+\lambda\eta,
\qquad
\Gamma^{\rm new}(1/2)=6.538803618888044.
\tag{0.12}
\]

The **prior missing implication** remains universal nonnegativity of `D_{Gamma^new}`. The exact sub-implication attacked here is different and necessary for understanding whether this repair direction can carry further work:

> Can a nontrivial Boolean gate have `M_eta=0`, so that a negative all-gate defect is completely invisible to the new universally safe direction?

The answer is **no**. More strongly, the peer's Bernstein certificate implies an explicit local coercivity inequality.

## 1. A useful exact form of the repair

Write

\[
V_p=4p(1-p)=1-(1-2p)^2.
\]

Then (0.5)-(0.6) simplify exactly to

\[
\boxed{
\eta(p)=2V_p-V_p^2-\varepsilon V_p^3
=V_p(2-V_p-\varepsilon V_p^2).
}
\tag{1.1}
\]

Thus

\[
\eta(0)=\eta(1)=0,
\qquad
\eta(p)>0\quad(0<p<1),
\tag{1.2}
\]

and, since `0<=V<=1`,

\[
\boxed{
\eta(p)\ge(1-\varepsilon)V_p.
}
\tag{1.3}
\]

At the center,

\[
\eta(1/2)=1-\varepsilon={4886991\over5000000}=0.9773982.
\tag{1.4}
\]

## 2. Exact singleton recurrence

Fix an actual input coordinate `k`, put

\[
t=p_k,\qquad q=1-t,
\]

and let `G_0,G_1` be its two Boolean restrictions. Let

\[
a=\mathbb E G_0,\qquad b=\mathbb E G_1,
\qquad d=|a-b|,
\tag{2.1}
\]

and

\[
\delta=\Pr(G_0\ne G_1)=\alpha_k.
\tag{2.2}
\]

Booleanity gives the sharp relation

\[
0\le d\le2\delta\le2.
\tag{2.3}
\]

Parent pivotal probabilities of every coordinate other than `k` are the `q,t` averages of the two child pivotal probabilities. Therefore the safe currency has the exact recurrence

\[
\boxed{
M_\eta(G;p)
=qM_\eta(G_0;p_{-k})
+tM_\eta(G_1;p_{-k})
+L_k,
}
\tag{2.4}
\]

where

\[
L_k=q\phi(a)+t\phi(b)+\delta\phi(1-2t)-\phi(qa+tb).
\tag{2.5}
\]

This is the same literal-restriction quantity in the peer proof, now retained quantitatively rather than only by its sign.

## 3. New quantitative coercivity theorem

The fleet01/B14 proof consumes the exact fleet02/B12 Bernstein certificate for the polynomial factor `R`. Its certified global lower bound is

\[
\boxed{
r_0={1999313322941\over16492674416640000000}
=1.2122432495992445\times10^{-7}>0.
}
\tag{3.1}
\]

Specifically, after replacing `delta` by the extremal allowed `d/2`, the peer factorization is

\[
q\phi(a)+t\phi(b)+{d\over2}\phi(1-2t)-\phi(qa+tb)
=d\,t(1-t)(2-d)R,
\tag{3.2}
\]

with `R>=r_0` throughout the full parameter cube.

Restoring the actual Boolean disagreement `delta` gives immediately:

### Theorem 3.1 — one-step strict currency

For every finite Boolean gate, every interior product bias and every actual input coordinate `k`,

\[
\boxed{
L_k\ge
r_0\,d\,t(1-t)(2-d)
+\left(\delta-{d\over2}\right)\eta(t).
}
\tag{3.3}
\]

Consequently,

\[
\boxed{
M_\eta(G;p)\ge
r_0\,d\,t(1-t)(2-d)
+\left(\delta-{d\over2}\right)\eta(t).
}
\tag{3.4}
\]

because the two child currencies in (2.4) are nonnegative by the peer theorem.

There is also an influence-only corollary. For fixed `delta`, put

\[
F(d)=r_0d\,t(1-t)(2-d)
+\left(\delta-{d\over2}\right)\eta(t),
\qquad 0\le d\le2\delta.
\tag{3.5}
\]

Using (1.3),

\[
F'(d)
=2r_0t(1-t)(1-d)-{\eta(t)\over2}
\le2t(1-t)\,[r_0-(1-\varepsilon)]<0,
\tag{3.6}
\]

because the exact certificate satisfies `r_0<1-epsilon`. Therefore the minimum is attained at `d=2delta`, giving

\[
\boxed{
M_\eta(G;p)\ge r_0V_t\,\delta(1-\delta).
}
\tag{3.7}
\]

This last bound is deliberately only a coarse projection of (3.4): it vanishes when `delta=1`, whereas (3.4) can still be strictly positive.

## 4. New exact zero-set classification

### Theorem 4.1 — no nontrivial zero mode

For interior product biases,

\[
\boxed{
M_\eta(G;p)=0
}
\tag{4.1}
\]

if and only if, after deleting dummy variables, `G` is either a constant or a literal (an input coordinate or its complement, with optional output complement).

### Proof

Constants and literals give equality directly. Conversely suppose `G` is nonconstant and choose an active coordinate `k`.

All terms on the right side of (3.3) are nonnegative, and `eta(t)>0` because the bias is interior. Hence `L_k=0` forces simultaneously

\[
d\in\{0,2\},
\qquad
\delta=d/2.
\tag{4.2}
\]

If `d=0`, then `delta=0`, so the two Boolean restrictions agree with probability one. Since the product measure on the remaining finite cube has full support, they agree pointwise; `k` was dummy, contradicting that it was active.

If `d=2`, then the two child means are the opposite endpoints `+1,-1`, so the two restrictions are opposite constants. Thus `G` depends only on `k` and is a literal up to complementation.

Therefore every active coordinate of a nonliteral gate has `L_k>0`. Equation (2.4) and nonnegativity of the child currencies then give `M_eta(G;p)>0`. QED.

This closes a genuine universal loophole in the shaped-repair mechanism: **the new safe direction is strictly gate-improving on every nonliteral Boolean gate.** There is no hidden nontrivial gate on which the repair direction has exactly zero currency.

## 5. Application to the current all-gate candidate

For every nonliteral gate define the shaped normalized margin

\[
\boxed{
c_G^{(\eta)}(p)
={[-D_{\Gamma^\dagger}(G;p)]_+\over M_\eta(G;p)}.
}
\tag{5.1}
\]

Theorem 4.1 proves that the denominator is strictly positive for every gate that can be a genuine obstruction. Constants and literals satisfy the gate identity exactly and need no repair.

Thus a finite number `Lambda` with

\[
\sup_{G,p}c_G^{(\eta)}(p)\le\Lambda
\tag{5.2}
\]

would imply the all-gate theorem for

\[
\Gamma^\dagger+\Lambda\eta
\tag{5.3}
\]

and therefore FEI with finite center

\[
6.521851214+\Lambda(1-\varepsilon).
\tag{5.4}
\]

**This run does not prove (5.2).** The point of Theorem 4.1 is that the normalized problem now has no nontrivial zero-denominator exception.

For the known biased 18-input prime witness, the consumed peer gives

\[
M_\eta
={5853348229889641167388287
\over5764607523034234880000000}
=1.015394058745685\ldots .
\tag{5.5}
\]

Combining (5.5) with the source-exact deficit (0.4), its shaped margin is

\[
\boxed{
c_{18}^{(\eta)}
=0.0173444189515517944962860942953\ldots .
}
\tag{5.6}
\]

The peer coefficient `lambda=0.01734442` is therefore genuinely above this requirement, but only by about `1.05e-9` in coefficient units. That very small clearance makes a nearby off-centre bias search on the same prime gate a high-value falsification test for `Gamma^new`.

## 6. Exact finite counterexample search

`CHECK.py` independently checks the algebraic identities used above and exhausts small Boolean gates with exact rational arithmetic.

At **uniform bias**, every Boolean function through four inputs was tested exactly. No negative currency occurs. The zero set is exactly the constants and literals:

| arity | gates with `M_eta=0` | minimum positive `M_eta` |
|---:|---:|---:|
| 1 | 4 | none |
| 2 | 6 | `15818667/320000000 = 0.049433334375` |
| 3 | 8 | `15818667/320000000 = 0.049433334375` |
| 4 | 10 | `15818667/320000000 = 0.049433334375` |

The count `2n+2` is exactly two constants plus the two literals for each coordinate, as Theorem 4.1 predicts.

On the interior bias grid

\[
\{1/4,1/2,3/4\}^n,
\]

the checker also exhausts all gates at `n=2,3`. It tests 144 gate/bias pairs at `n=2` and 6912 at `n=3`, again with no negative value. The only zeros are constants/literals at every bias. The minimum positive value on both searches is

\[
{109080219\over4096000000}
=0.026630912841796875.
\tag{6.1}
\]

These finite searches are sanity checks only; the zero-set theorem is analytic and uses the peer's continuum Bernstein certificate.

Checker SHA-256:

`a9033bb7fd184c974e0e73012abb97271ae4973393f991222bd834b9dd9d22b1`

Captured-output SHA-256:

`a83bb434b7c5c0c83542a5ebaee27cc8a66e232c3f0205ddcc9377ee471b5988`

The captured output reports `PASS`.

## 7. What is proved, what is not, and the next attack

**PROVED, conditional only on the already-completed exact Bernstein certificate consumed from the peer:**

1. the singleton-safe repair has the quantitative local lower bound (3.3);
2. the influence projection (3.7) holds for every coordinate;
3. `M_eta=0` exactly for constants/literals/dummy extensions;
4. adding any positive multiple of `eta` strictly increases the all-gate defect of every nonliteral gate.

**FINITE CHECK ONLY:** exhaustive small-gate searches in Section 6.

**OPEN:** no finite universal bound on the shaped margin (5.1) has been proved. Therefore neither `Gamma^new` nor full FEI is certified by this run.

**Decisive next attack:** evaluate the source-exact shaped margin `c_G^(eta)` along the one-coordinate bias line of the same composition-prime 18-input Numaro gate, beginning in a fine dyadic collar around `p_1=3/8`. The current coefficient clears that point by only about `1.05e-9`; a nearby value above `0.01734442` would immediately refute `Gamma^new`, while a rigorous local maximum below it would certify a nontrivial off-centre collar. This is more informative than another disconnected finite gate slice.

## 8. Required collaboration fields

- `exact_candidate_version`: `Gamma^new = Gamma^dagger + (867221/50000000) eta`, fleet01/B14 commit `63189a15a82c34331909a42fe35786109f3c8a29`.
- `prior_missing_implication`: prove `D_{Gamma^new}(G;p)>=0` for every finite Boolean gate and every interior product bias, or exhibit a genuine counterexample.
- `new_proved_inference`: `M_eta(G;p)>0` for every nonliteral gate, with quantitative lower bounds (3.3) and (3.7); zero modes are exactly constants/literals/dummy extensions.
- `replacement_obligation`: prove `sup c_G^(eta)<infinity` (and ideally `<=0.01734442`) or find a gate/bias with larger shaped margin.
- `consumed_peer_artifact`: fleet01/B14 `20260922T091217Z-universal-singleton-repair/REPORT.md`, commit `63189a15a82c34331909a42fe35786109f3c8a29`.
- `applied_to_claim`: removes every nontrivial zero-denominator exception from the current universally safe shaped-repair direction and makes strict improvement quantitative.
- `remaining_implication`: a dimension-independent upper bound for the normalized shaped margin (5.1), or a counterexample to the current coefficient.
- `next_recipient`: `fleet01/B14` for the singleton-repair candidate and `fleet03/B18` for all-gate integration.
- `full_problem_change`: useful universal structural narrowing only; full FEI remains OPEN.

No scheduler mutation, cross-account mutation, email, Drive write, public posting, workflow dispatch, paid model/API/Codex use, credential access, or unrelated private-data operation was used.
