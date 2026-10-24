# POS3 account02/B19 — majority-late conditioning trap

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the **uniform law on all linear extensions** lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run uses a materially different mechanism from the preceding autonomous-chain/ideal-block construction: an exact two-child conditioning calculation on a six-point asymmetric Hasse corridor. It attacks the current **majority-late strict-corridor** selector directly. It does not resume brain-installation or benchmark work and makes no novelty/priority claim.

## 1. Source-bound state consumed

The live collective target and B19 assignment were read from the current owner-controlled research allocation. The scientific work below consumes these completed POS3 inputs.

1. **Campaign lead account04/B10, latest complete version:**  
   `proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, report blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`.  
   It proves that at the first sibling fork the predecessor sets are nested, their proper difference is a chain with top `d` a Hasse predecessor, and in the majority-late branch `b prec_* a` either `(b,d)` is a strict span descent or a minimal successor blocker `u` of `b` incomparable with `a` must exist. In the no-descent subbranch such a blocker lies after `a` in the strong-majority order.

2. **Named partner account03/B10, latest complete version:**  
   `proofnet24/collective-POS3/account03/B10/20260922T031643Z-a03-b10-pos3-r11/REPORT.md`, report blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`.  
   In the majority-early strict branch it conditions on the top relation `d<b`, obtaining an exact decomposition into two genuine uniform child laws. The `+` child has equal predecessor sets and the selected probability scales exactly by the conditioning mass. Its report states the next source-valid target for the still-unpaid majority-late branch: obtain an analogous two-child squeeze or force a span descent.

The construction below applies that exact conditioning move to the majority-late geometry and shows a sharp obstruction: the equal-predecessor child can land **inside the balanced band while the same original pair remains strictly unbalanced**. Thus child balance cannot simply be lifted back on the same pair; an additional side-channel transport argument is essential.

## 2. Compact conditional end-to-end route and first missing implication

A current conditional route to POS3 is:

1. take a cardinality-minimal hypothetical counterexample and its transitive strong-majority order;
2. use the lead's first-boundary fork and predecessor nesting;
3. majority-early strict corridors are handled by the partner's exact `d<b` conditioning plus channel analysis;
4. in the majority-late strict corridor, either obtain span descent or condition on `d<b` to the equal-predecessor child;
5. transfer whatever contradiction/balance is found in that child back to the original law;
6. iterate descent/fork escalation until the width-three geometry cannot continue.

The first essential missing implication is step 5. A tempting same-pair version is false:

> **False candidate.** In the majority-late no-descent local geometry, if conditioning on `d<b` makes the equal-predecessor child pair `(a,b)` balanced, then `(a,b)` is balanced in the original poset.

The exact witness below refutes this candidate while satisfying the lead's local majority-late/no-descent inequalities. It does **not** satisfy the global hypothesis “no balanced pair anywhere”; indeed it exhibits where the required balance migrates. Therefore no lead/partner theorem is refuted. What is refuted is the local same-pair conditioning shortcut.

## 3. Exact width-three witness

Let `P` have ground set

`{d,a,b,r1,r2,u}`

and Hasse covers

`d<a,  d<r1,  r1<r2,  r2<u,  b<u`.

Equivalently, there is a four-point chain

`d<r1<r2<u`

with a leaf `a` above `d` and a leaf `b` below `u`.

### Width

`{a,r1,b}` is a 3-antichain. The three chains

`(d<a), (r1<r2), (b<u)`

cover all vertices, so `width(P)=3` exactly.

### Local strict-corridor geometry

For the incomparable pair `(a,b)`,

`Pred(b)=empty`, `Pred(a)={d}`,

so the proper predecessor difference is the singleton chain

`D={d}`,

with top `d lessdot a`. Also `b lessdot u` and `u||a`, so `u` is exactly the minimal successor blocker required by the campaign lead's majority-late continuation.

The exact uniform probabilities are

`Pr(a<b)=6/19 < 1/3`,

`Pr(d<b)=15/19 > 2/3`,

`Pr(a<u)=15/19 > 2/3`.

Thus the selected local strong-majority order is

`d prec_* b prec_* a prec_* u`

on the relevant incomparable comparisons. In particular:

- `(b,d)` is **not** the lead's span-descent case, because `d prec_* b`;
- the forced successor blocker is on the **no-descent side**, because `a prec_* u`.

So this six-point poset realizes precisely the local majority-late branch that remains after the current lead/partner work.

## 4. Exact two-child decomposition

Condition on the incomparable relation `d||b` exactly as in the partner mechanism:

`P^+ = P + (d<b)`,

`P^- = P + (b<d)`.

Every linear extension of `P` lies in exactly one child, and conditioning the finite uniform set gives genuine uniform laws on both children.

### Counts

In `P^-`, `b<d` forces `b,d` first in that order; the remaining element `a` may be inserted in four positions around the chain `r1<r2<u`. Hence

`e(P^-)=4`.

In `P^+`, `d` is first. On the remaining five points, ignoring the free point `a`, the poset on `{b,r1,r2,u}` has exactly three extensions:

`b,r1,r2,u`,

`r1,b,r2,u`,

`r1,r2,b,u`.

Insert `a` in any of five positions, giving

`e(P^+)=15`.

Therefore

`e(P)=19`,

and the exact conditioning mass is

`gamma=Pr_P(d<b)=15/19`.

### Equal predecessors in the `+` child

Adding `d<b` gives

`Pred_{P^+}(a)=Pred_{P^+}(b)={d}`.

Among the three base orders above, the numbers of insertion slots placing `a` before `b` are respectively `1,2,3`. Hence

`#{L in L(P^+):a<b}=1+2+3=6`,

so

`Pr_{P^+}(a<b)=6/15=2/5`.

This is strictly inside the balanced band.

In `P^-` we have `b<d<a`, so `a<b` is impossible. Consequently the exact scaling identity is

`Pr_P(a<b)=gamma Pr_{P^+}(a<b)`

`=(15/19)(2/5)=6/19<1/3`.

This is the promised conditioning trap: the equal-predecessor child has the **same pair balanced at `2/5`**, yet the original same pair is strictly below `1/3`.

## 5. Where the original balance actually migrates

The parent POS3 theorem is not threatened. Exact enumeration of **every incomparable pair** in `P` gives:

| pair orientation | exact probability |
|---|---:|
| `d<b` | `15/19` |
| `a<b` | `6/19` |
| `a<r1` | `5/19` |
| `a<r2` | `10/19` |
| `a<u` | `15/19` |
| `b<r1` | `9/19` |
| `b<r2` | `14/19` |

Hence the original law has balanced pairs, notably

`Pr(b<r1)=9/19`,

`Pr(a<r2)=10/19`.

The balance created/seen in the conditioned equal-predecessor child does not lift on `(a,b)`; it is paid by **side-corridor pairs** in the original poset. Any proof of the majority-late branch therefore needs a source-valid balance-transport/flux lemma that sees those side channels, not only the scalar pair `(p,gamma)` and not only the equal-predecessor child.

This is exactly the distinction the current selector must preserve: `Law(P^+)` is a genuine uniform child law, but it is not the original uniform law, and balance of a child pair is not invariant under unconditioning.

## 6. Arbitrarily large finite adversaries by ordinal padding

For arbitrary `p,q>=0`, form

`C_p op P op C_q`,

where `op` denotes ordinal sum and an empty chain is allowed. Every linear extension is forced to concatenate the unique prefix-chain order, one linear extension of `P`, and the unique suffix-chain order. Therefore:

- width remains exactly three;
- the incomparable pairs are exactly the incomparable pairs internal to `P`;
- every probability in the table above is unchanged;
- the same conditioning trap persists for arbitrarily large finite orders.

Thus the obstruction is not a small-order accident and no finite census closes it.

## 7. Accepted gate before/after

**Before.** The latest lead and named partner had reduced the unresolved majority-late strict branch to a bounded predecessor corridor plus a desired analogue of the exact two-child conditioning mechanism. It was still possible that the equal-predecessor child could be used by a same-pair lifting shortcut.

**After.** The six-point exact witness proves that shortcut false, even in the precise local majority-late/no-descent geometry:

`Pr_P(a<b)=6/19<1/3`, `Pr_P(d<b)=15/19>2/3`, `Pr_P(a<u)=15/19>2/3`,

but

`Pr_{P^+}(a<b)=2/5`.

The first essential missing implication is therefore sharpened to:

> **Majority-late side-channel transport.** Under the full hypothetical-counterexample hypotheses, if `d<b` conditioning reaches an equal-predecessor child whose selected pair is balanced (or whose channel identity forces a balanced event), prove that the mass lost to the opposite child forces **some possibly different original incomparable pair** into `[1/3,2/3]`; the proof must use the width-three side-corridor/fork geometry rather than same-pair scalar scaling alone.

The witness identifies the correct phenomenon: the compensating original balance can sit on the side chain (`b||r1` and `a||r2`).

## 8. Exact executable evidence

`CHECKER.py` enumerates the complete uniform linear-extension sets of `P`, `P^+`, and `P^-`, verifies width exactly three, checks the full incomparable-pair table, verifies the local majority-late/no-descent inequalities, and checks the exact law partition/scaling identity.

Executed checker SHA-256: `89bb329a335fe78a0ea137ab633652525e3b936052778be5cc0e7b24a77d2d69`.  
Checker Git blob: `b73561b042a9f084790daed7e30f6232b9e7a5b3`.  
Executed output SHA-256: `5cdee105a19f699b092ca06b15d924c5be89f780b3d815b871a82703f7a081e7`.  
Output Git blob: `ccf89f1b71dfadc00539e85fc8a7e633be64a959`.

The executable terminates with `POS3_MAJORITY_LATE_CONDITIONING_TRAP_PASS`.

## 9. Integrity and status

This report is `CANDIDATE_REFUTED`, not a POS3 counterexample and not a full proof candidate. The global no-balanced-pair hypothesis is deliberately **not** claimed for this witness; the exact table exhibits balanced pairs. Therefore the witness cannot refute a theorem that essentially uses that global hypothesis. It refutes only the proposed/local same-pair conditioning shortcut and identifies what additional global geometry must do.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex, remote workflow, permission change, or brain installation was used. Historical artifacts are preserved.
