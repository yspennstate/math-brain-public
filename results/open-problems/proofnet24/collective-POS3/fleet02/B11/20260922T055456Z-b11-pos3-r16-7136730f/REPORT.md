# POS3 fleet02/B11 — exact incomparability-leaf splice and the residual nonchain-side obstruction

**Run:** `20260922T055456Z-b11-pos3-r16-7136730f`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run changes mechanism from the preceding fork/corridor charge analysis to an exact graph-separator/series-splice reduction. Every probability below is under the original uniform law on all linear extensions of the full poset.

## 1. Exact state consumed

The latest complete campaign-lead result consumed is fleet04/B10 run `20260922T051259Z-B10-POS3-r14` (source report commit `ecfee91d04858608546fc37fcf253959b1a71131`, blob `50bac494667235f3630991a512438eac42c30521`). It turns the bridged small-minority branch into a `>E/3` cover-gap flux and, using fleet01/B19, forces at least two external relation-distinguisher channels. Its first unpaid step is global recycling of those heavy channels.

The named OTHER-account partner result applied here is fleet03/B19 run `20260922T045925Z-b19-pos3-r12` (source report commit `50d05434bf5ee4da8a89559c2a655a97194c06d8`, blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`). It proves that two consecutive exact-two corridor states carry an exact latent mass `K` with `E/3<K<2E/3`, and gives the explicit width-three family `P_m` with
`E_m=3*C(m+3,3)+4*C(m+2,2)+(m+1)` and `K_m/E_m -> 1/3` from above. Section 5 below applies the new splice theorem to that exact family.

Inherited reductions used as hypotheses, not reproved here: a cardinality-minimal counterexample is width exactly three, its incomparability graph is connected (ordinal-sum reduction), and its comparability graph is connected (parallel-sum reduction). Thus the remaining target is series- and parallel-indecomposable.

## 2. Exact leaf-splice factorization

Let `P` be any finite poset and suppose `x` has exactly one incomparable neighbor, called `b`. Put

`D = Pred(x)`,  `U = Succ(x)`,

and let `L=P[D union {b}]`, `R=P[U union {b}]`.

### Theorem 2.1 — leaf splice

The following hold.

1. `P\{x,b} = D direct_ordinal_sum U`; in particular every `d in D` satisfies `d<u` for every `u in U`.
2. `Pred(b) subseteq D` and `Succ(b) subseteq U`.
3. With `e(Q)` denoting the number of linear extensions,
   
   `N_P(b<x) = e(L)e(U)`,                                      (2.1)
   
   `N_P(x<b) = e(D)e(R)`,                                      (2.2)
   
   `e(P) = e(L)e(U)+e(D)e(R)`.                                 (2.3)
4. Conditional on `b<x`, the restriction to `L` and the restriction to `U` are independent uniform linear extensions. Conditional on `x<b`, the restrictions to `D` and `R` are independent uniform linear extensions.

#### Proof

Every element other than `b` is comparable with `x`, hence lies in exactly one of `D,U`. Transitivity through `x` gives `D<U`. If `z<b` and `x<z`, then `x<b`, impossible, so `z in D`; dually every successor of `b` lies in `U`.

Now take an extension with `b<x`. Every member of `D` is before `x`, every member of `U` is after `x`, and `b` is before `x`; therefore the extension is uniquely

`(an extension of L), x, (an extension of U)`.

Conversely every such concatenation respects all relations of `P`. This is a bijection and proves (2.1). The event `x<b` similarly gives the unique concatenation

`(an extension of D), x, (an extension of R)`,

proving (2.2). The two events partition `L(P)`, proving (2.3). The same bijections give the conditional product laws. `square`

Thus the leaf pair itself has the exact extension-ratio formula

`Pr(b<x) =
 [e(L)/e(D)] / ([e(L)/e(D)] + [e(R)/e(U)])`.                  (2.4)

No deletion-induced distribution is renamed uniform.

## 3. A chain-side branch cannot survive ordinal indecomposability

Write

`lambda = Pr_P(b<x)`.

The next statement converts the exact splice into a genuine minimal-counterexample reduction.

### Theorem 3.1 — majority-facing chain side collapses

Assume `P` has no balanced incomparable pair.

(a) If `lambda>2/3` and `D` is a chain, then `Pred(b)=D`.

(b) Dually, if `lambda<1/3` and `U` is a chain, then `Succ(b)=U`.

Consequently, if in addition `P` is ordinally indecomposable, then

- `lambda>2/3` implies `D` is empty or nonchain;
- `lambda<1/3` implies `U` is empty or nonchain.                (3.1)

#### Proof of (a)

Because `Pred(b) subseteq D` and `D` is a chain, `Pred(b)` is an initial segment of `D`. Suppose it is proper. Let

`t_1 < ... < t_m`

be the nonempty final segment `D\Pred(b)`. Every `t_j` is incomparable with `b`: the only other possible orientation, `b<t_j`, would imply `b<x`.

Conditioned on `b<x`, Theorem 2.1 gives the uniform law on the chain-with-one-extra-element `L`. The element `b` may be inserted in exactly the `m+1` gaps around the tail `t_1,...,t_m`, all equally often. Hence

`Pr(t_j<b | b<x) = (m-j+1)/(m+1)`.

Conditioned on `x<b`, every element of `D` precedes `b`, so

`Pr(t_j<b) = 1 - lambda*j/(m+1)`.                              (3.2)

If `m=1`, this lies strictly between `1/2` and `2/3` because `2/3<lambda<1`.

If `m>=2`, the values in (3.2) decrease in steps
`lambda/(m+1)<1/3`; the first value is above `2/3`, while the last is below `2/3`. Therefore the first value at or below `2/3` is still above `1/3`. In all cases some incomparable pair `(t_j,b)` is balanced, contradiction. Thus `Pred(b)=D`.

If `D` is nonempty and `Pred(b)=D`, then every element of `D` lies below every element outside `D`: it lies below `x`, below `b`, and below every member of `U`. Hence `P=D direct_ordinal_sum (P\D)`, contradicting ordinal indecomposability. This proves the first bullet of (3.1). Part (b) and the second bullet follow by order duality. `square`

### Corollary 3.2 — exact residual leaf geometry in a minimal hard core

In a cardinality-minimal series-indecomposable POS3 counterexample, an incomparability leaf cannot point its strong-majority orientation through a nonempty chain side. If `b prec_* x` (`Pr(b<x)>2/3`), the predecessor side `Pred(x)` is either empty or a genuine nonchain. If `x prec_* b`, the successor side `Succ(x)` is either empty or a genuine nonchain.

This is an arbitrary-size reduction. It does **not** claim that incomparability leaves are impossible.

## 4. Compact conditional end-to-end route and first unpaid implication

The ordinal and parallel decompositions leave a width-three series/parallel-indecomposable minimal candidate. Theorem 3.1 now removes every leaf branch whose majority-facing side is a nonempty chain.

For a surviving leaf with, say, `Pr(b<x)>2/3`, the only non-boundary case is therefore that `D=Pred(x)` is nonchain. The dominant branch `L=D union {b}` and the minority branch `D` are both strictly smaller width-at-most-three posets, and Theorem 2.1 keeps their laws exact.

The first unpaid implication is therefore the following **dominant-side balance-transfer lemma**:

> In the exact two-branch mixture (2.1)--(2.3), when the majority-facing side is a nonchain of width at most three, show that a balanced pair supplied by minimality in the corresponding smaller branch survives in `P`, or forces `(x,b)` itself to be balanced, or yields a proper ordinal reduction.

This is genuinely stronger than replacing a deletion projection by a uniform law: the two branches have different smaller uniform factors and are mixed with the exact extension-count weights in (2.4). Proving this implication would eliminate incomparability leaves from the minimal hard core; it would not by itself settle the lead's module-prime/heavy-flux core.

## 5. Application to the named fleet03/B19 `P_m` family

The partner's r12 family has core relations

`e<x, e<y, d<y, d<u, x<u`

and, for `m>=1`, the chain

`e<r_1<...<r_m<u`.

Put

`p=C(m+3,3)`, `q=C(m+2,2)`, `r=m+1`.

The partner proved

`E_m=3p+4q+r`,  `K_m=p+2q`,  and `K_m/E_m -> 1/3+`.

The element `e` is an incomparability leaf with unique neighbor `d`. Applying Theorem 2.1 gives the exact branch counts

`N(e<d)=3p+2q`,                                                (5.1)

`N(d<e)=2q+r`.                                                 (5.2)

For every `m>=1`, `Pr(e<d)>2/3`. The majority-facing successor side of `e` is a **nonchain of width three**, exactly the residual branch allowed by Corollary 3.2. Dually, `u` is an incomparability leaf with unique neighbor `y` and exhibits the symmetric nonchain-side residue.

Thus the named partner family is a sharp regression guard against two tempting strengthenings:

1. “an incomparability leaf must itself give a balanced pair” is false;
2. “the majority-facing side of every width-three leaf is a chain” is false.

At `m=8`, `E=684`, the new exact leaf counts are `N(e<d)=585` and `N(d<e)=99`, while the partner's latent mass is `K=255`. The example has balanced pairs elsewhere and is not a POS3 counterexample. Its `K/E` approaching `1/3` also rules out importing a fixed-slack argument into the residual leaf-transfer problem.

## 6. Exact regression

A deterministic exact-arithmetic verifier enumerated all distinct transitively closed naturally labelled posets through order six and restricted to width at most three.

It checked:

- `3701` width-at-most-three posets;
- `3192` incomparability-leaf states;
- all `3192` exact splice factorizations (2.1)--(2.3);
- `49` lower-chain strong-majority cases covered by Theorem 3.1(a);
- `49` upper-chain dual cases;
- the partner family `P_m` for `m=0,...,8`, including formulas (5.1)--(5.2) and the nonchain width-three residual for `m>=1`.

The run terminated `POS3_LEAF_SPLICE_V1_PASS`.

Verifier SHA-256: `a4386af35e0f12f6a714cb1afc7886fe01d8efdd7d0e7bf196970e0aad27a3f2`  
Captured-output SHA-256: `bc8c77840afe0ecbb6dc84ce09e7ae949dd36c80a50ce4fa00062ddbb25ec80a`

This finite computation is a regression check for the symbolic proof, not closure for arbitrary sizes.

## 7. Status

- Exact incomparability-leaf splice/product law: **PROVED**.
- Majority-facing nonempty chain side excluded in an ordinally indecomposable no-balanced poset: **PROVED**.
- Incomparability leaves excluded altogether: **NOT PROVED**.
- Dominant-side nonchain balance transfer: **OPEN; first residual implication from this mechanism**.
- POS3: **OPEN / NOT PROVED**.
- Finite frontier `n_bal=14`: unchanged.

No benchmark or brain-installation work was performed. No held-out material, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive content, paid or remote compute, workflow dispatch, public posting, or permission changes were used.
