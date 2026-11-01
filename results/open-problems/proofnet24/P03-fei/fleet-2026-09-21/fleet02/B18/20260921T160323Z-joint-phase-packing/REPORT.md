TASK: B18 ACCOUNT: fleet02 RUN: 2026-09-21T16:03:23Z — FEI proof integration: joint phase-discrepancy packing and a two-bank hard-core inequality

# Status

**Full uniform-cube Friedgut–Kalai Fourier entropy-influence conjecture: OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated math_brain retrieval or receiver-side brain context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. **Configured reasoning / provider reasoning usage:** UNKNOWN / not exposed.


Scientific master was first recovered at `c4715211f484254e32128df087f3ed673978edb3` and refreshed before this write to `98abd6e5c171732d2e2246514d1231f4c2b5dd5f`. Current entry rules, P03 README, the 21 September TASKS/REPORT/APPROACHES packet, the previous fleet02/B18 KL-projection ledger, fleet02/B13 block-parity KL theorem, fleet02/B16 q-flip density theorem, and the fresh fleet04/B18 exact phase-defect theorem were read at compatible master states. The current owner correction is preserved: `6.521845710923046575` is already a certified lower bound for the unrestricted FEI constant; the `6.4547837...` scale is read-once/Hod-class and is not the unrestricted target.

Creative moves used: FLEET_RULES #25 (count the same dependence bank twice but without double-counting it), #3 (prove the stronger simultaneous packing statement instead of another one-coordinate lower bound), and #30 (localize first to singleton phase discrepancies, then identify exactly what still fails to glue at diffuse scale).

The new mathematical movement is a **joint/tensorized phase-discrepancy certificate**. Earlier work had (i) a global Hellinger phase-stability inequality but only extracted a one-coordinate phase-free corollary, and (ii) a KL-strengthened one-block cap theorem whose explicit next target was a joint packing/tensorization theorem. The result below aggregates *all singleton Boolean phase discrepancies against one Hellinger/total-correlation budget*, with no factor of `n`. I then combine it with the fresh scalar-frontier phase theorem to obtain a two-bank inequality: a dangerous hard core must pay its phase discrepancy either in product-law KL/Hellinger distance or in scalar tangent slack.

---

# 1. Setup and inherited exact identities

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad a_S=\widehat f(S),\qquad \mu(S)=a_S^2.
\]

Write

\[
p_i=\Pr_{\mu}(i\in S)=\operatorname{Inf}_i(f),\qquad I=\sum_i p_i,
\]

and let

\[
Q(S)=\prod_{i\in S}p_i\prod_{i\notin S}(1-p_i)
\]

be the matched product law. Choose phases `eps_S` agreeing with `sgn(a_S)` when `a_S!=0`, arbitrarily at zero coefficients, and define

\[
b_S=\varepsilon_S\sqrt{Q(S)},\qquad
 t=\|b-a\|_2^2.
\tag{1.1}
\]

The previous B18 phase-stability theorem proves

\[
\sum_{U\ne\varnothing} (|R_U|-t)_+^2\le4t,
\qquad R_U:=\langle b,T_Ub\rangle,
\tag{1.2}
\]

and

\[
\operatorname{TC}(\mu):=D_{\mathrm{KL},2}(\mu\|Q)\ge {t\over\ln2}.
\tag{1.3}
\]

For a singleton `i`, writing

\[
d_i(T)=\varepsilon_T\varepsilon_{T\cup\{i\}},\qquad T\subseteq[n]\setminus\{i\},
\]

one has the exact product-phase formula

\[
R_i=2\sqrt{p_i(1-p_i)}\,\mathbb E_{Q_{-i}}d_i.
\tag{1.4}
\]

Define the exact sign discrepancy of a finite law `P` by

\[
\operatorname{disc}(P)=
\min_{d:\Omega\to\{\pm1\}}|\mathbb E_P d|
=2\min_{A\subseteq\Omega}|P(A)-1/2|.
\tag{1.5}
\]

Set

\[
\delta_i:=\operatorname{disc}(Q_{-i}),\qquad
A_i:=2\sqrt{p_i(1-p_i)}\,\delta_i.
\tag{1.6}
\]

Because the actual derivative sign `d_i` is one admissible sign function,

\[
|R_i|\ge A_i.
\tag{1.7}
\]

If `M_i=\max_TQ_{-i}(T)`, then

\[
\delta_i\ge(2M_i-1)_+,
\tag{1.8}
\]

which gives an explicit phase-free lower surrogate

\[
A_i^{\rm dom}:=2\sqrt{p_i(1-p_i)}(2M_i-1)_+\le A_i.
\tag{1.9}
\]

---

# 2. PROVED: joint singleton phase-discrepancy packing

## Theorem B18-JOINT-PHASE-PACKING-01

For every Boolean `f`, with the notation above,

\[
\boxed{
\sum_{i=1}^n (A_i-t)_+^2\le4t.
}
\tag{2.1}
\]

Consequently the same inequality holds with `A_i^{dom}` in place of `A_i`.

Define `Theta(A)` as the unique nonnegative solution `s` of

\[
\sum_i(A_i-s)_+^2=4s,
\tag{2.2}
\]

with `Theta=0` if all `A_i=0`. Then

\[
\boxed{
 t\ge\Theta(A),\qquad
 \operatorname{TC}(\mu)\ge {\Theta(A)\over\ln2}.
}
\tag{2.3}
\]

The same conclusion holds for the computable dominant-atom vector `A^{dom}`.

### Proof

The global B18 stability theorem (1.2) already packs *all* xor shifts into the single Hellinger budget `t`. Restricting its nonnegative sum to singleton shifts gives

\[
\sum_i(|R_i|-t)_+^2\le4t.
\tag{2.4}
\]

By (1.7), the map `x -> (x-t)_+` is increasing on the nonnegative half-line, hence

\[
(A_i-t)_+\le(|R_i|-t)_+
\]

for every `i`. Squaring and summing proves (2.1).

The function

\[
F(s)=\sum_i(A_i-s)_+^2-4s
\]

is continuous and strictly decreasing until it becomes negative (unless all `A_i=0`), with `F(0)>=0` and `F(max A_i)<0`. Thus (2.2) has the asserted unique root. Inequality (2.1) says `F(t)<=0`, so `t>=Theta(A)`. Equation (1.3) gives the KL conclusion. Replacing `A_i` by the smaller `A_i^{dom}` preserves every inequality. QED.

### Equal-tranche corollary

If a set `J` of `m` coordinates satisfies `A_i>=a>0` for every `i in J`, then

\[
\boxed{
 t\ge {\bigl(\sqrt{1+ma}-1\bigr)^2\over m}.
}
\tag{2.5}
\]

Indeed, (2.1) implies `m(a-t)_+^2<=4t`; solving the equality in the nontrivial branch gives (2.5).

This is the promised joint packing statement: unlike the old one-coordinate Hellinger corollary, it can gain from many simultaneously biased coordinates without paying an ambient-dimension factor.

---

# 3. Decisive numerical stress calculation: genuine aggregation, still not FEI closure

Take the symmetric marginal profile

\[
n=20,\qquad p_i=0.01\quad(1\le i\le20).
\]

This is only a marginal stress profile; no assertion is made that the matched product law itself is a Boolean spectral law.

For every `i`,

\[
M_i=(0.99)^{19}=0.8261686238355866\ldots,
\]

so

\[
A_i^{\rm dom}
=2\sqrt{0.01\cdot0.99}\,[2(0.99)^{19}-1]
=0.1298134732379054\ldots.
\]

The old one-coordinate Hellinger lower bound gives only

\[
\operatorname{TC}\ge
{0.01(0.99)[2(0.99)^{19}-1]^2\over\ln2}
=0.0060779075161480\ldots\text{ bits}.
\]

The newer B13 one-block exact KL certificate gives about

\[
0.0145680578657556\ldots\text{ bits}
\]

for this coordinate profile.

The joint theorem instead gives

\[
t\ge {\bigl(\sqrt{1+20(0.1298134732379054\ldots)}-1\bigr)^2\over20}
=0.0401751473446908\ldots,
\]

hence

\[
\boxed{\operatorname{TC}\ge0.0579604858411688\ldots\text{ bits}.}
\]

So on this stress profile the simultaneous packing certificate is about `9.54x` the earlier max-coordinate Hellinger certificate and about `3.98x` the exact one-block KL certificate.

But this still does **not** pay the whole FEI defect at the current unrestricted lower-bound scale. At

\[
C=6.521845710923046575,
\]

the product-marginal excess for this profile is about

\[
20\,[h_2(0.01)-C(0.01)]
=0.3114935757336143\ldots\text{ bits},
\]

far above the certified `0.05796...` dependence payment. The remaining gap is real and is not hidden by the aggregation theorem.

---

# 4. PROVED: two-bank inequality with the fresh scalar-frontier phase theorem

This section is **not** a universal statement for arbitrary `f`; it applies exactly in the restriction-maximal scalar hard-core setting of the fresh fleet04/B18 tangent-defect theorem.

Use its notation. For coordinate `i`, write the paired spectral masses

\[
x_T=\widehat g(T)^2,\qquad y_T=\widehat g(T\cup\{i\})^2,
\]

and on supported pairs define the same phase derivative

\[
d_i(T)=\operatorname{sgn}(\widehat g(T)\widehat g(T\cup\{i\})).
\]

Let

\[
Z_i=\sum_{x_Ty_T>0}d_i(T)y_T
\]

be the supported signed upper mass and

\[
U_i=\sum_{x_T=0<y_T}y_T
\]

the unsupported upper mass. At the fixed scalar calibration `r`, the fresh theorem proves

\[
\sum_i Z_i^2\le K_r s,
\qquad
\sum_iU_i\le{s\over d_r},
\qquad
s:=B(g)-b(r)I(g),
\tag{4.1}
\]

where `K_r<infinity` and `d_r>0` are its exact scalar constants.

Let `mu` be the spectral law of this same `g`, `Q` its matched product law, and retain

\[
t=\|\operatorname{sgn}(\widehat g)\sqrt Q-\widehat g\|_2^2.
\]

## Theorem B18-TWO-BANK-02

In the scalar hard-core setting just stated,

\[
\boxed{
\sum_i\bigl(p_i\delta_i-2\sqrt t\bigr)_+^2
\le
2\left(K_r+{1\over d_r}\right)s.
}
\tag{4.2}
\]

Thus simultaneous product-phase discrepancy must be paid by one of two already-certified banks:

1. product-law Hellinger/KL distance `t` (hence total correlation), or
2. scalar tangent slack `s=B-bI`.

### Proof

Extend each phase derivative `d_i(T)` arbitrarily to zero-coefficient pairs, as was already done in the product surrogate. Define the full signed upper moment

\[
M_i^\mu
:=\mathbb E_\mu[d_i(S\setminus\{i\})\mathbf1_{\{i\in S\}}].
\tag{4.3}
\]

The supported part is `Z_i`; the only omitted contribution is unsupported upper mass, hence

\[
|M_i^\mu-Z_i|\le U_i.
\tag{4.4}
\]

Under the product law,

\[
M_i^Q
=p_i\mathbb E_{Q_{-i}}d_i,
\]

so by definition of `delta_i`,

\[
|M_i^Q|\ge p_i\delta_i.
\tag{4.5}
\]

The test function in (4.3) has absolute value at most one. Therefore

\[
|M_i^\mu-M_i^Q|\le\|\mu-Q\|_1.
\tag{4.6}
\]

The Hellinger-amplitude distance controls this `L1` distance directly:

\[
\begin{aligned}
\|\mu-Q\|_1
&=\sum_S|\sqrt{\mu(S)}-\sqrt{Q(S)}|
       (\sqrt{\mu(S)}+\sqrt{Q(S)})\\
&\le\sqrt t\,\sqrt{4-t}\le2\sqrt t.
\end{aligned}
\tag{4.7}
\]

Combining (4.4)--(4.7) gives

\[
p_i\delta_i\le |Z_i|+U_i+2\sqrt t.
\]

Hence

\[
(p_i\delta_i-2\sqrt t)_+\le|Z_i|+U_i.
\]

Square, sum, and use `(u+v)^2<=2u^2+2v^2`, `0<=U_i<=1`, and (4.1):

\[
\begin{aligned}
\sum_i(p_i\delta_i-2\sqrt t)_+^2
&\le2\sum_iZ_i^2+2\sum_iU_i^2\\
&\le2K_rs+2\sum_iU_i\\
&\le2(K_r+d_r^{-1})s.
\end{aligned}
\]

This is (4.2). QED.

### Exact-saturation consequence

If the scalar tangent slack vanishes (`s=0`), then

\[
\boxed{p_i\delta_i\le2\sqrt t\quad\text{for every }i.}
\tag{4.8}
\]

Therefore an exact scalar-frontier saturator that is also near the matched product law can only survive when every residual product law admits an extremely well-balanced sign cut. This is a precise simultaneous obstruction, not the unsupported assertion that scalar saturation itself makes the spectrum product.

---

# 5. What this does and does not solve

The fleet02/B13 block-parity theorem ended with the exact request for a joint block-cap packing/tensorization theorem. Theorem 01 supplies such a theorem for the **singleton phase-discrepancy channel**: one global Boolean Hellinger budget pays the whole family simultaneously, not merely their maximum. It does not yet tensorize B13's stronger KL water-fill costs for arbitrary overlapping blocks.

The fleet04/B18 theorem ended with the request to connect its scalar phase vector `Z` to a simultaneous transport/product-phase obstruction. Theorem 02 gives one exact connection: the same derivative phases under the matched product law cannot all be discrepant unless either total-correlation distance or scalar tangent slack is large.

The fleet02/B18 Han/KL descent ledger remains unchanged in one essential respect. At descent scale `q>1`, only

\[
K_q=T-(n/q)\bar T_q
\]

is spendable; full total correlation `T` cannot be subtracted again. Theorems 01–02 lower-bound the global dependence bank, but they do not prove that this bank contracts at the needed projection scale. Treating their `TC` payment as an additional independent Han credit would be double counting.

The decisive remaining regime is now narrower:

> **Diffuse phase-balanced rare-coordinate regime.** A hypothetical high-ratio hard core can evade the new aggregate singleton certificate only by spreading its dangerous product-marginal entropy excess over coordinates for which the phase discrepancy amplitude is below the common threshold set by `t`, or by arranging extremely fine balanced cuts of the residual product laws. If it simultaneously has small scalar tangent slack, Theorem 02 forces the same fine balancing at the `p_i delta_i` scale. The missing universal implication must exploit the *curl-free/global compatibility* of those many fine balances, or convert them into projection-scale KL contraction `K_q`; independent one-coordinate balancing is no longer an adequate relaxation.

This is consistent with B16's current q-flip result: random q-flip channelization does not make the active channel bank sparse, so the remaining work is on signed load/cancellation, not channel counting.

---

# 6. PROVED / CONDITIONAL / OPEN / refuted-or-forbidden ledger

## PROVED in this run

P1. **Joint phase packing:** `sum_i(A_i-t)_+^2<=4t`, with `A_i=2 sqrt(p_i(1-p_i)) disc(Q_-i)`, and therefore `TC>=Theta(A)/ln2`.

P2. **Dominant-atom aggregate corollary:** the same theorem holds with `disc(Q_-i)` replaced by `(2M_i-1)_+`.

P3. **Equal-tranche closed form:** if `m` coordinates have `A_i>=a`, then `t >= (sqrt(1+ma)-1)^2/m`.

P4. **Two-bank scalar-hard-core inequality:** under the exact hypotheses of the fleet04 scalar tangent-defect theorem, `sum_i(p_i delta_i-2 sqrt(t))_+^2 <= 2(K_r+1/d_r)(B-bI)`.

## PROVED inherited and used without broadening hypotheses

I1. B18 product-phase theorem: `sum_{U != empty}(|R_U|-t)_+^2<=4t` and `TC>=t/ln2`.

I2. B13 block-parity conditional caps and KL I-projection are one-block statements; their relaxed `Bern(1/64)^64` product profile shows that maximizing one block certificate cannot close FEI.

I3. Fleet04/B18 scalar-frontier theorem supplies `sum Z_i^2<=K_r(B-bI)` and `sum U_i<=(B-bI)/d_r` only in its restriction-maximal calibrated hard-core setting.

I4. B18 KL-projection descent spends `K_q=T-(n/q)\bar T_q`, not all of `T`, at scale `q>1`.

I5. B16 q-flip channel-density theorem shows basis randomization cannot solve the signed-transport route merely by making active channels sparse.

## CONDITIONAL

C1. If one can upgrade Theorem 01 from singleton discrepancy to a bounded-overlap family of block/curl discrepancies whose aggregate root pays the positive FEI defect, full FEI follows through the exact defect identity.

C2. If the global dependence certified here can be shown to yield a summable lower bound on projection KL contraction `K_q` at a valid sequence of descent scales, it closes the current `Rcal_q-K_q` integration gap.

## OPEN

O1. Prove a **curl-free biased discrepancy packing theorem** for many simultaneously balanced rare coordinates/blocks. The derivative signs are gradients of one global Fourier phase and cannot be chosen independently.

O2. Convert global `TC`/Hellinger payment into the scale-specific `K_q` payment without spending projected total correlation twice.

O3. Tensorize B13's KL water-fill block costs with bounded overlap; Theorem 01 is only the singleton phase analogue.

O4. Relate B16 signed q-flip load/plaquette divergence quantitatively to the phase discrepancies in Theorems 01–02.

## REFUTED / forbidden synthesis steps

R1. **"Sum the old one-coordinate TC lower bounds."** Invalid: they all lower-bound the same global `TC`. Theorem 01 is the valid simultaneous packing replacement and follows from one Bessel budget.

R2. **"Count the B13 KL block certificate and the Han `K_q` credit independently."** Invalid unless an exact decomposition proves disjointness; projected TC is a reserve.

R3. **"Scalar tangent saturation implies a product spectrum."** Not proved. Theorem 02 only gives the quantified phase-discrepancy consequence (4.8).

R4. **"The aggregate singleton certificate closes FEI."** False as a proof claim: the numerical stress calculation above leaves a large unpaid product-marginal excess, and fine/dispersed phase balance remains possible in the current relaxation.

---

# 7. Literature/applicability check

Fresh primary-source checks on 21 September 2026 still do not provide an unrestricted FEI proof:

- V. N. Potapov, arXiv:2609.21563 (18 Sep 2026), proves FEI for Boolean plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2. These are structured classes, not unrestricted FEI.
- M. J. González, P. MacManus, M. C. Pereyra, arXiv:2606.00246 (29 May 2026), gives restriction/stopping-tree results; its key universal restriction inequality would imply FEI but is not established for every Boolean function.
- P. Li and G. Han, arXiv:2512.03117 (2 Dec 2025), sharpen Han's profile-dependent entropy-influence inequality but retain the coordinate influence-profile entropy term rather than a dimension-independent FEI bound.

A targeted web search did not locate a source for the exact joint phase-packing formulation above. **No novelty or publication-priority claim is made.** The theorem is recorded as a source-exact project lemma derived from already-proved project identities.

---

# 8. Nonoverlapping next ownership

- **B12:** continue terminal-to-prefix information loss / Palm-row depth. Do not duplicate phase packing.
- **B13:** attack KL-level bounded-overlap block-cap tensorization. Theorem 01 is a singleton phase input, not a substitute for its stronger block objective.
- **B14:** bind exact erasure/composition quantities to restriction recombination `Rcal_q`; preserve activation/refund signs.
- **B15:** project the packet/product bridge to q-marginals and quantify the reserved `(n/q)\bar T_q`; no duplicate KL spending.
- **B16:** attack the remaining curl-free fine-balance regime and signed q-flip load. A useful concrete target is a lower bound on a bounded-overlap family of actual `R_U`/plaquette moments when every singleton `delta_i` is tiny.
- **B17:** structural normal forms/peeling, with representation compatibility stated explicitly.
- **B18:** integrate the first block/curl tensorization or projection-scale KL result into `UNPAID_q=Rcal_q-K_q`; do not spend another run merely renaming the obstruction.

**Conclusion:** PARTIAL. The current run replaces max-coordinate phase payment by a rigorous simultaneous packing theorem and proves an exact Hellinger/KL-versus-scalar-slack dichotomy, but the full FEI conjecture remains OPEN / NOT PROVED.
