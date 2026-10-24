# POS3 account03/B11 — exact two-gap deletion fibers for extreme sibling bias

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

The active owner programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B11 assignment is to pursue a distinct order-polytope/correlation method and improve the decisive pair-selection statement, with named partner account04/B19. No benchmark or installation work is performed here.

## 1. Exact state and named peer result consumed

The immediate account03/B11 predecessor is the source-bound report

- `proofnet24/collective-POS3/account03/B11/20260922T011439Z-account03-B11-pos3-r12/REPORT.md`, blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`.

It proves, conditional on the inherited minimal-counterexample/strong-majority state: the order-polytope swap-defect identity; canonical positive blockers are Hasse neighbors; every adjacent incomparable strong-majority boundary has at least two canonical positive blockers; the first boundary has a two-cover successor fork `x \lessdot s_1,s_2`; the blocker siblings are nonautonomous, and every distinguisher of them occurs only after the entire second majority block; and an exact seven-element example refutes the stronger claim that the first fork triple alone must contain a balanced pair.

The exact named other-account partner result consumed in this run is **account04/B19**:

- `proofnet24/collective-POS3/account04/B19/B19-20260922T0113Z-r44/REPORT.md`, blob `f11967a121d6c257ff510714cfb49cf27467198a`.

That report gives an exact deletion-fiber law for a proper autonomous chain `C`: if `K(tau)` is the number of neutral elements in the admissible central corridor of a linear extension `tau` of `P\C`, then the number of lifts is exactly
\[
W_C(\tau)=\binom{|C|+K(\tau)}{K(\tau)}.
\]
It proves that all nonuniformity is localized to two boundary swap types, and that the constant-corridor case would induce the uniform law and is therefore impossible in a cardinality-minimal counterexample. Thus any surviving autonomous chain is boundary-active.

I use this result in the proof architecture, not merely as a citation: it rules out replacing the current deletion law by an unweighted/uniform quotient and establishes that the correct exchange object is an **exact fiber multiplicity**. The present report derives the complementary exact fiber law for deleting the two incomparable blocker siblings. This retains every multiplicity and directly localizes an extreme pair bias to a deterministic gap-profile witness.

## 2. Conditional end-to-end route and first missing implication

Assume a cardinality-minimal POS3 counterexample exists. The inherited collective state supplies a transitive strong-majority total order and at least five maximal chain blocks. At the first block boundary `x \prec_* y`, the account03/B11 predecessor produces two distinct upper covers
\[
x\lessdot s_1,\qquad x\lessdot s_2,
\]
with `s_1 || s_2`, `s_i || y`, and no local autonomous escape.

Because the hypothetical poset has no balanced incomparable pair, the sibling pair itself is extreme: after renaming,
\[
p_{s_1s_2}:=\Pr(s_1\hbox{ precedes }s_2)>2/3.
\]

The first missing exchange implication is therefore: what exact deterministic multiplicity asymmetry is forced when an incomparable pair has probability greater than `2/3`, without replacing the induced law after deletion by a uniform law? The theorem below answers this exactly for every finite poset.

## 3. Exact two-gap deletion-fiber theorem

Let `P` be any finite poset and let `a,b` be incomparable. Put `Q=P\setminus\{a,b\}`. Fix `tau in L(Q)`, and number the gaps of `tau` by `0,1,...,m`, where `m=|Q|`; gap `g` is immediately after the first `g` elements of `tau`.

For `v in {a,b}`, define
\[
\ell_v(\tau)=\max\bigl(\{\,\operatorname{pos}_\tau(u):u<v\,\}\cup\{0\}\bigr),
\]
\[
u_v(\tau)=\min\bigl(\{\,\operatorname{pos}_\tau(w)-1:v<w\,\}\cup\{m\}\bigr),
\]
and the exact admissible-gap interval
\[
I_v(\tau)=\{\ell_v(\tau),\ell_v(\tau)+1,\ldots,u_v(\tau)\}.
\]

### Theorem 3.1 — two-gap fiber multiplicity

For fixed `tau`, let `A_tau` be the number of lifts of `tau` to a linear extension of `P` with `a` before `b`, and `B_tau` the number with `b` before `a`. Then
\[
A_\tau=\#\{(i,j)\in I_a\times I_b:i<j\}+|I_a\cap I_b|,
\]
\[
B_\tau=\#\{(i,j)\in I_a\times I_b:i>j\}+|I_a\cap I_b|,
\]
and hence
\[
T_\tau:=A_\tau+B_\tau=|I_a|\,|I_b|+|I_a\cap I_b|.
\]
Moreover
\[
A_\tau-B_\tau=\sum_{i\in I_a,\ j\in I_b}\operatorname{sgn}(j-i).
\]
Summing over all `tau in L(Q)`,
\[
e(P)=\sum_\tau T_\tau,\qquad N(a<b)=\sum_\tau A_\tau,\qquad N(b<a)=\sum_\tau B_\tau.
\]

**Proof.** A lift of `tau` is specified by choosing an admissible external gap `i` for `a` and an admissible external gap `j` for `b`. If `i<j`, the relative order is forced to be `a<b`; if `i>j`, it is forced to be `b<a`. If `i=j`, both orders are valid because `a||b`, and these are two distinct lifts. No other multiplicity occurs. This gives the first two formulas and the total. Subtracting cancels the equal-gap contributions and leaves `+1` for each pair `i<j` and `-1` for each pair `i>j`, giving the sign-sum identity. Finally, every full linear extension restricts to a unique `tau`, so summing disjoint fibers gives the global identities. `□`

This is the exact multiplicity analogue of the order-polytope transposition defect: the continuous volume skew has been localized to an integer gap-profile skew with no change of measure.

## 4. Extreme global bias forces an extreme deterministic fiber

### Corollary 4.1 — `>2` fiber witness

If `Pr(a<b)>2/3`, then there exists a linear extension `tau of Q` such that
\[
A_\tau>2B_\tau.
\]
Equivalently, in that fiber,
\[
A_\tau-B_\tau>\frac{T_\tau}{3}.
\]

**Proof.** The global hypothesis is `sum A_tau > 2 sum B_tau`. If every fiber satisfied `A_tau<=2B_tau`, summing would give the opposite inequality. The equivalent form follows from `T_tau=A_tau+B_tau`. `□`

Therefore every first-boundary Hasse-fork sibling pair in a hypothetical POS3 counterexample has at least one exact deletion fiber whose admissible-gap profiles themselves have a greater-than-two orientation skew. This is strictly stronger than saying only that the averaged pair probability is extreme.

### Corollary 4.2 — identical profiles are exactly balanced

If `I_a(tau)=I_b(tau)` for every `tau`, then `Pr(a<b)=1/2`. This recovers the incomparable two-element autonomous-module case by exact multiplicities: every deletion fiber is symmetric before any averaging.

## 5. A quantitative nested-profile obstruction

Suppose in one fiber the intervals have a common left endpoint and are nested:
\[
I_a=[L,L+r-1],\qquad I_b=[L,L+s-1],\qquad s\ge r\ge1.
\]
Then direct summation in Theorem 3.1 gives
\[
A_\tau=rs-\frac{r(r-1)}2,\qquad B_\tau=\frac{r(r+1)}2,
\]
so
\[
\frac{A_\tau}{B_\tau}=\frac{2s-r+1}{r+1}.
\]
In particular,
\[
A_\tau>2B_\tau\quad\Longrightarrow\quad 2(s-r)>r+1.
\]
Thus a one-sided nested fiber cannot create counterexample-level bias from a one-gap perturbation. It needs a quantitatively wide admissible-gap extension. This gives a concrete span parameter for the next boundary-propagation step.

## 6. Width three makes the common-neutral region one-dimensional

For incomparable `a,b`, define `N(a,b)={z:z||a and z||b}`.

### Lemma 6.1

If `width(P)<=3`, then `N(a,b)` is a chain.

**Proof.** If two elements `z_1,z_2 in N(a,b)` were incomparable, then `{a,b,z_1,z_2}` would be a four-element antichain. `□`

Hence the exact gap-profile skew of a fork-sibling pair cannot be amplified by a two-dimensional cloud of elements simultaneously neutral to both siblings. The common-neutral part is a single chain; all remaining asymmetry must come from elements that distinguish the two profiles. This is the precise bridge to the account04/B19 corridor philosophy: width three makes the surviving multiplicity distortion boundary-driven and essentially one-dimensional on the common-neutral side.

## 7. Adversarial test: one fork plus its earliest distinguisher is still not enough

The predecessor report had already refuted a theorem confined to the first fork triple. I tested the stronger local candidate that the first boundary `x,y`, its two Hasse successor blockers `s_1,s_2`, and the earliest strong-majority-order element distinguishing the siblings must contain a balanced incomparable pair. This is also false.

Take the eight-element poset whose transitive closure is generated by
\[
0<2,\ 0<5,\ 1<2,\ 1<3,\ 1<6,\ 2<4,\ 3<4,\ 3<5,\ 5<7,\ 6<7.
\]
It has exactly `e(P)=121` linear extensions and width `3`. Its transitive strong-majority order is
\[
1\prec_*0\prec_*3\prec_*6\prec_*2\prec_*5\prec_*4\prec_*7.
\]
At the first boundary `x=1,y=0`,
\[
\Pr(1<0)=81/121>2/3.
\]
The canonical positive successor blockers are exactly `s_1=3,s_2=6`, and both are Hasse covers of `1`.

The elements distinguishing `3` and `6` are exactly `4,5`; the earliest is `z=5`, with `3<5` and `6||5`. Nevertheless all incomparable pairs in the local set `{0,3,6,5}` are extreme in the required orientations:
\[
\Pr(0<3)=89/121,\quad \Pr(0<6)=100/121,
\]
\[
\Pr(3<6)=82/121,\quad \Pr(6<5)=83/121.
\]
So the first fork plus its earliest nonautonomy witness still does not force balance.

The poset is not a POS3 counterexample. The next majority-span pair already escapes:
\[
\Pr(6<2)=66/121,
\]
which lies in `[1/3,2/3]`. This is a useful failure: the proof must propagate the exact fiber skew across the whole strong-majority span, rather than close on one fork and one distinguisher.

## 8. Exact fibers in the adversary identify the right obstruction

Apply Theorem 3.1 to the extreme sibling pair `(a,b)=(3,6)`. Deleting the pair leaves exactly `12` linear extensions of `Q`. Summing their exact lift multiplicities gives
\[
N(3<6)=82,\qquad N(6<3)=39.
\]
A maximally skew deletion fiber has
\[
I_3=(2),\qquad I_6=(2,3,4,5),
\]
and therefore
\[
A_\tau=4,\qquad B_\tau=1.
\]
Across every deletion fiber of this example, the two intervals are nested with the same lower endpoint, and the extreme fibers satisfy the quantitative width condition from Section 5.

Thus the adversary says exactly where the surviving proof difficulty sits: the local Hasse fork can remain extreme only by generating a wide admissible-gap profile; the balanced pair appears at the next span boundary instead. The missing theorem should couple those two facts.

## 9. New residual / next recipient

The order-polytope route has now converted the first-boundary bias through the following exact chain: extreme adjacent strong-majority boundary; at least two Hasse-local canonical blockers; a nonautonomous blocker-sibling pair; a delayed distinguisher; for the extreme sibling orientation, an exact deletion fiber with `A_tau>2B_tau`; and, in the common nested case, a quantitatively wide gap-profile extension is necessary.

The first unpaid implication is now a **span-propagation statement**, not a local fork statement:

> In a width-three cardinality-minimal counterexample, show that an extreme first-fork sibling fiber with `A_tau>2B_tau` cannot propagate across every adjacent strong-majority boundary up to the first profile distinguisher while all those boundary pairs remain extreme.

The eight-element example shows this statement must use the complete span: the first local four-point configuration survives, but the next span pair becomes balanced. The width-three common-neutral-chain lemma and account04/B19's boundary-active corridor law are the natural inputs for converting a large interval-width difference into either a balanced adjacent pair, a proper autonomous subset, or a new forced blocker escalation.

This is the handoff to account04/B19 and the POS3 lead. The parent POS3 target remains open.

## 10. Verification and status

A deterministic standard-library verifier checks the exact transitive closure and `121` linear extensions of the adversary; width exactly `3`; the stated transitive strong-majority order; the first-boundary canonical blockers and Hasse-cover status; the exact distinguisher set and earliest distinguisher; every quoted extension count; the balanced escape `Pr(6<2)=66/121`; Theorem 3.1 against direct full-extension counts for every incomparable pair of the adversary; the `(3,6)` global fiber sum `82/39`; the maximal exact fiber `4/1` with intervals `(2)` and `(2,3,4,5)`; and the nested-interval formulas and their necessary width condition. The recorded output ends with `POS3_TWO_GAP_FIBER_CHECK_PASS`.

Claim status: exact two-gap deletion-fiber theorem **PROVED**; extreme global bias implies an exact `>2` skew fiber **PROVED**; identical-profile balance **PROVED**; common-left nested-profile formula and quantitative wide-profile necessity **PROVED**; common-neutral set is a chain in width three **PROVED**; stronger fork-plus-earliest-distinguisher local closure **REFUTED** by the exact `121`-extension width-three example; width-three `1/3–2/3` parent target **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, held-out keys, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, or public release was used.
