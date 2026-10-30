# POS3 fleet01/B19 — width-two ideal-cut convolution for deleting the first majority element

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run changes the bookkeeping mechanism again. Instead of projecting through an entire deleted chain and then trying to control its biased extension law, I delete only the **first element of the common strong-majority order** and refine the induced law by the actual order ideal that appears before that element. In width three, that cut ideal lives in a width-at-most-two poset. The resulting recurrence is an exact convolution of uniform linear-extension counts of strictly smaller induced subposets. No biased projected law is declared uniform.

## 1. Source-bound collective state consumed

The active programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; the former brain-installation/benchmark assignment is superseded.

I used the following completed state.

1. **Campaign lead fleet04/B10**, run `20260922T011127Z-fleet04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-at-most-three counterexample, the transitive strong-majority order `L_*` exists and every element occupies its `L_*` rank with probability `>1/81`; in the one-sided endpoint case the same argument gives `>4/9`.
2. **Assigned OTHER-account partner fleet02/B10**, run `20260922T014627Z-fleet02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`. At the first adjacent strong-majority block boundary it proves the exact endpoint blocker-product cap `2/3 < p < 7/9` and shows that both canonical Hasse-blocker channels carry positive weighted deletion-fiber defect. I apply its strict endpoint cap below in the singleton-first-block subcase and use its two-channel result to identify why a scalar cut-size statistic is not the final endpoint invariant.
3. **Prior fleet01/B19**, run `20260922T021702Z-pos3-b19-r11`. It proved an exact first-interruption renewal recurrence for deleting the first maximal majority-chain block, reducing the biased projection to at most two first-interrupter channels of actual uniform residual-poset laws. The present recurrence is a different, finer state decomposition: it resolves **every legal cut ideal before the first majority element**, not only the first interrupter.
4. **fleet04/B11**, run `20260922T021940Z-B11-pos3-r13`, report blob `5075f5ae42742da375b0688cef37dbc8e8c65484`. It source-validly refutes the stronger pairwise transfer claim: an arbitrary pair balanced in the smaller uniform poset need not remain balanced after exact insertion weighting. Therefore the remaining induction statement must be existential/adaptive rather than fixed-pair transfer.

## 2. Compact conditional end-to-end induction

Assume for contradiction that POS3 is false and choose a counterexample `P` of minimum cardinality. Let `L_*` be the inherited transitive strong-majority order and let `c` be its first element. Since `L_*` extends `P`, `c` is minimal in `P`. Put

`Q=P\{c}`.

If `Q` were a chain, then `P` would be the union of the chain `Q` and the singleton chain `{c}`, hence would have width at most two; the known width-two theorem would already give a balanced pair. Thus `Q` is a smaller nonchain of width at most three, so by minimality its **uniform** linear-extension law has a balanced incomparable pair.

The only issue is transferring the existential balance information from uniform `L(Q)` to the actual restriction of the uniform law on `L(P)`. The theorem below gives the exact transfer kernel.

## 3. The incomparability set of the first element is a width-two ideal

Define

`S={z in Q : z || c}`,  `T=Q\S`.

Because `c` is minimal, every element of `T` satisfies `c<z`.

### Lemma 3.1

`S` is an order ideal of `Q`, and `width(S)<=2`.

### Proof

Take `z in S` and `u<z` in `Q`. If `c<u`, transitivity gives `c<z`, contradiction. The alternative `u<c` is impossible because `c` is minimal. Hence `u||c`, so `u in S`; therefore `S` is an ideal.

If `S` contained a three-element antichain, adjoining `c`, which is incomparable with every element of `S`, would give a four-element antichain in `P`. Since `width(P)<=3`, `width(S)<=2`. `□`

This is the useful width-three collapse: all nontrivial insertion cuts for `c` live in the ideal lattice of a width-two poset.

## 4. Exact ideal-cut convolution

For a full linear extension `L in L(P)`, let

`I(L)={z in S : z precedes c in L}`.

Since everything preceding `c` is incomparable with it and predecessors of preceding elements also precede `c`, `I(L)` is an order ideal of `S` (equivalently of `Q`). Conversely, fix any ideal `I in J(S)`, any `alpha in L(I)`, and any `beta in L(Q\I)`. Then

`alpha, c, beta`

is a linear extension of `P`: no relation can point from `Q\I` into `I` because `I` is an ideal, every element comparable with `c` lies in `T subseteq Q\I` and is above `c`, and the remaining elements are incomparable with `c`.

Hence restriction gives a bijection

`L(P)  <->  disjoint union_{I in J(S)} L(I) x {c} x L(Q\I)`.

### Theorem 4.1 — exact cut recurrence

Writing `e(R)=|L(R)|`,

`e(P)=sum_{I in J(S)} e(I)e(Q\I)`.                         `(CUT0)`

Under the uniform law on `L(P)`, the random cut ideal has the exact distribution

`pi(I)=e(I)e(Q\I)/e(P)`.                                   `(CUT1)`

For every `z in S`,

`Pr_P(z<c)=sum_{I contains z} pi(I)`.                        `(CUT1a)`

For incomparable `a,b in Q`, define `N_R(a<b)` as the number of linear extensions of an induced subposet `R` in which `a<b` (when both elements belong to `R`). Then

`N_P(a<b)=sum_{I in J(S)} K_I(a,b)`,                         `(CUT2)`

where

- if `a,b in I`, `K_I=e(Q\I) N_I(a<b)`;
- if `a in I`, `b notin I`, `K_I=e(I)e(Q\I)`;
- if `b in I`, `a notin I`, `K_I=0`;
- if `a,b notin I`, `K_I=e(I) N_{Q\I}(a<b)`.

Thus every pair numerator is an exact mixture of **uniform laws on strictly smaller induced posets**, plus deterministic cross-cut orientations. This is a direct induction-ready replacement for an unproved uniform-projection shortcut.

## 5. Equivalent hitting-time form and the exact covariance obstruction

There is a second form that makes the remaining transfer problem quantitative. Let `nu` be the uniform law on `L(Q)`. For

`tau=(q_1,...,q_n) in L(Q)`,

let `kappa(tau)` be the number of initial elements of `tau` lying in `S` before the first element of `T`; if `T` is empty, put `kappa=n`.

Since `c` must precede every member of `T` and is incomparable with every member of `S`, exactly the first `kappa+1` insertion gaps of `tau` are legal. Therefore

`W_c(tau)=kappa(tau)+1`,                                      `(5.1)`

`e(P)=e(Q) E_nu[kappa+1]`,                                   `(5.2)`

and for every event `A` determined only by the order on `Q`,

`Pr_P(A)= E_nu[(kappa+1) 1_A] / E_nu[kappa+1]`.               `(5.3)`

Consequently

`Pr_P(A)-Pr_Q(A)=Cov_nu(1_A,kappa)/E_nu[kappa+1]`.            `(5.4)`

This is an exact signed transfer formula. In particular, if `A={a<b}` is a pair balanced under uniform `Q`, with `q=Pr_Q(A)`, then failure of transfer requires

`Cov_nu(1_A,kappa) > (2/3-q) E_nu[kappa+1]`                   `(5.5+)`

or

`Cov_nu(1_A,kappa) < -(q-1/3) E_nu[kappa+1]`.                 `(5.5-)`

So the remaining induction problem is no longer “control an arbitrary biased deletion law.” It is: **among the uniform-balanced pairs of `Q`, find one whose indicator cannot have the required extreme signed covariance with the width-two-ideal hitting time `kappa`.**

A useful rigorous sufficient condition follows immediately from Cauchy-Schwarz:

`|Pr_P(A)-q| <= sqrt(q(1-q) Var_nu(kappa))/E_nu[kappa+1]`.     `(5.6)`

For example, a uniform `q=1/2` pair certainly survives whenever

`sqrt(Var_nu(kappa)) <= E_nu[kappa+1]/3`.                     `(5.7)`

This does not close the general case, but it identifies an exact quantitative interface with the team's bounded-width/rank-variance route.

## 6. Counterexample constraints become moment constraints on the width-two cut process

Because `c` is first in the strong-majority order, every `z in S` satisfies

`Pr_P(c<z)>2/3`, hence `Pr_P(z<c)<1/3`.                        `(6.1)`

The campaign lead's one-sided rank estimate gives

`pi(empty)=Pr_P(c is first)=e(Q)/e(P)=1/E_nu[kappa+1] > 4/9`, `(6.2)`

so

`E_nu[kappa+1] < 9/4`.                                        `(6.3)`

Summing `(CUT1a)` over `z in S` and counting insertion gaps on each fixed `tau` gives the exact moment identity

`sum_{z in S} Pr_P(z<c)`
`= E_nu[kappa(kappa+1)/2] / E_nu[kappa+1]`.                   `(6.4)`

Indeed, when the initial `S`-prefix has length `kappa`, an element at prefix position `r` precedes `c` in exactly `kappa-r+1` of the `kappa+1` legal insertion gaps, and summing over `r=1,...,kappa` gives `kappa(kappa+1)/2`.

Combining (6.1) and (6.4), every hypothetical counterexample satisfies

`E_nu[kappa(kappa+1)] < (2|S|/3) E_nu[kappa+1] < 3|S|/2`.     `(6.5)`

Thus the exact cut process has both a bounded mean and a second-moment bound tied to the incomparability degree of the first majority element.

**Application of the assigned partner result.** If the first strong-majority chain block is the singleton `{c}` and `y` is the next block element, fleet02/B10 r12 gives

`2/3 < Pr_P(c<y) < 7/9`.

Since `{c is first}` is contained in `{c<y}`,

`4/9 < pi(empty) < 7/9`,                                      `(6.6)`

hence

`9/7 < E_nu[kappa+1] < 9/4`.                                 `(6.7)`

Moreover that partner proves both canonical successor-blocker channels are genuinely active. In the present hitting-time picture those blockers are possible terminal labels at the stopping boundary where the initial `S`-prefix first meets a successor of `c`. Therefore an eventual endpoint proof may have to refine `kappa` by that terminal label; averaging to cut size alone can lose the two-channel sign information. The cut recurrence `(CUT0)-(CUT2)` retains enough state to make that refinement without changing the underlying uniform laws.

## 7. Genuine width-three counterexample to a tempting localization

The width-two nature of `S` suggests a tempting but false strengthening:

> If all pairs meeting the first element `c` are already strongly oriented, then the width-two ideal `S` itself must contain a balanced pair.

This is false.

Let `P` have elements `c,0,1,2,3,4,5` with Hasse covers

`c<0`, `0<2`, `0<4`, `1<2`, `2<3`.

Then `width(P)=3`. The elements incomparable with `c` are exactly

`S={1,5}`,

a two-element antichain and an ideal of `Q=P\{c}`. Exact enumeration gives

`e(Q)=42`, `e(P)=70`,

`Pr_P(c<1)=7/10`, `Pr_P(c<5)=57/70`,

so both cross pairs are strictly on the strong-majority side. Nevertheless

`Pr_P(1<5)=24/35>2/3`,

so the only incomparable pair inside `S` is not balanced.

The exact cut weights are

`I=empty: 42`, `I={1}:15`, `I={5}:7`, `I={1,5}:6`,

which sum to `70` and agree exactly with `e(I)e(Q\I)`. Under uniform `Q`,

`Pr_Q(1<5)=5/7`,

and `(CUT2)` gives its exact reweighted value `24/35` in `P`.

This is **not** a counterexample to POS3. For example `(0,1)` is balanced in `P`, with probability `2/5`. The example only proves that a successful induction cannot localize the replacement pair to the width-two incomparability ideal `S`; it must select globally in `Q`.

The deterministic verifier in this run independently checks width, all cut weights and the displayed rational probabilities. It ends with

`POS3_IDEAL_CUT_RECURRENCE_CHECK_PASS`.

Verifier Git blob: `60b04a6cb7ff6a8f466a8688cc6020801497ed05`.  
Verifier SHA-256: `ca5754304106c7714948b677e474afdfdb5d78dfdcee8b0296bb4c1a12dc8e87`.  
Captured-output Git blob: `d839e83aa4e79d7aa2d1425c956adf8094cf2bcf`.  
Captured-output SHA-256: `a779b67cc366965e1a717ffbbb4dc26637b43dfcb90d4dccf14ecfb9d532ea08`.

The finite computation verifies only this explicit regression example; the cut recurrence and covariance identities are proved symbolically above.

## 8. First essential missing implication after this run

The complete induction now reduces to a precise adaptive selection statement.

> **Width-two ideal-cut selection lemma (WICSL), open.** In the minimum-counterexample setup above, let `S` be the width-at-most-two incomparability ideal of the first strong-majority element `c`, let `nu` be uniform on `L(Q)`, and let `mu` be the exact cut mixture `(CUT1)-(CUT2)` (equivalently the `kappa+1` tilt (5.3)). Since `Q` is smaller, `nu` has at least one balanced incomparable pair. Prove that **some** incomparable pair of `Q` is `mu`-balanced, using the counterexample constraints `pi(z in I)<1/3` for every `z in S`, `pi(empty)>4/9`, the common strong-majority orientation, and where applicable the partner's two active endpoint blocker channels.

If WICSL holds, the minimal-counterexample induction closes immediately: the selected pair lies in `Q` and has exactly the same ordering probability in `P` as computed by `(CUT2)`, contradicting that `P` has no balanced pair.

Two stronger shortcuts are now source-validly ruled out:

1. fleet04/B11 refutes freezing an arbitrary uniform-balanced pair of `Q` before applying the insertion weights;
2. Section 7 refutes forcing the replacement pair to lie inside the width-two ideal `S`.

The exact remaining object is therefore a **global selection problem over the width-two ideal-cut ensemble**, or equivalently a statement that not every uniform-balanced pair indicator can have the extreme signed covariance with `kappa` required by `(5.5+)`/`(5.5-)`.

That is a narrower and more structured unpaid implication than the previous generic “weighted deletion law” obstacle.

## 9. Claim status and provenance

- `S` is a width-at-most-two ideal: **PROVED**.
- Ideal-cut convolution `(CUT0)-(CUT2)`: **PROVED** for arbitrary finite `P` with minimal deleted `c`.
- Hitting-time tilt/covariance identities (5.1)-(5.6): **PROVED**.
- Counterexample moment identities (6.2)-(6.5): **PROVED** under the inherited no-balanced-counterexample state.
- Partner endpoint refinement (6.6)-(6.7): **PROVED in the singleton-first-block subcase by applying fleet02/B10 r12**.
- Localization “a balanced pair must lie inside `S`”: **REFUTED** by the exact width-three example.
- WICSL: **OPEN / first essential missing implication**.
- Parent POS3: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, public posting, paid model/API/Codex execution, remote workflow, permission change, or production-brain mutation was used. No authenticated brain retrieval/context was used, so the run remains `WITHOUT_VERIFIED_BRAIN`.
