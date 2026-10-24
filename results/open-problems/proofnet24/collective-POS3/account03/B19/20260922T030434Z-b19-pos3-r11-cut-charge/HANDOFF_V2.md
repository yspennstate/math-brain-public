# POS3 B19 handoff v2 — latest partner integrated

**Status:** `ESSENTIAL_STEP_APPLIED`; parent POS3 **OPEN / NOT PROVED**; `WITHOUT_VERIFIED_BRAIN`.

## Source-bound peer state consumed

- Named partner account04/B10 latest: run `20260922T031005Z-B10-POS3-r11`, report blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`. It proves first-boundary sibling predecessor sets are nested and their proper difference is a delayed chain, and imports the exact endpoint exchange.
- account01/B11 endpoint exchange blob `5fdf6f70d35fee1011b67c217b9e177fb197e81a`.
- preceding B19 weighted-deletion report blob `07b199a92b9493193bfa7d847c1d41011975a822`.
- account02/B11 bi-connected hard-core report blob `a8e5e6dc7fc402c714d87da86b4b833a7efa0c38`.

## New exact results to reuse

### 1. Deletion cut-charge identity

For any finite `P`, deleted set `C`, retained `x,y`,

`sum_{c in C}(B_P(x,c)-B_P(y,c)) = 2(R_P(x,y)-R_Q^C(x,y))`.

For a chain deletion, fiberwise:

`B_tau(x,c_t)-B_tau(y,c_t)=2 sum_{r=k_x}^{k_y-1}H_t^tau(r)`

for `k_x<k_y`, with the opposite sign when reversed. This is an exact conversion of the corridor/rank defect into genuine original-law pair numerators.

### 2. Delayed predecessor-difference chain correction

For the latest partner's strict nested predecessor state, relabel

`Pred(b) subseteq Pred(a)`, `D=Pred(a)\Pred(b)={d_1<...<d_k}`.

Deleting `D` makes the predecessor sets equal in the remaining poset, but the induced law stays weighted. Exactly:

`R_Q^D(a,b)-R_P(a,b)=sum_{d in D}N_P(b<d)`.

The probabilities `p_j=Pr(b<d_j)` are nondecreasing and

`p_{j+1}-p_j=Pr(d_j<b<d_{j+1})`.

Hence, absent a balanced `b,d_j`, the chain is all below `1/3`, all above `2/3`, or has one adjacent gap event of probability `>1/3`.

### 3. Majority-early strict nesting has the same span/fork alternative

Let `M=Min{z:a<z,z||b}`, with endpoint count `Q=#{L:b precedes every m in M}`. If the larger-predecessor sibling is majority-early, `a prec_* b`, then exact endpoint exchange gives `Q<2E/3` and `M!=empty`. Minimality plus width three gives `1<=|M|<=2`.

- If some `m prec_* b`, then `a prec_* m prec_* b`: strict span descent.
- Otherwise every `m` lies after `b`. `|M|=1` is impossible because then `Q=Pr(b<m)E>2E/3`. Therefore `|M|=2`, `{b,m_1,m_2}` is an antichain, `|C_{m_1}|+|C_{m_2}|=E-Q>E/3`, and one canonical channel has mass `>E/6`.

Thus the partner's equal-predecessor span/fork mechanism extends to **all nested-predecessor first-boundary pairs in the majority-early orientation**.

### 4. No-successor majority-late subbranch is >5/6 extreme

If there is no successor distinguisher, then `M=empty`, `Q=E`, and with `d_top=max D`,

`R/E=Pr(b<d_top)`,

`Pr(a<b)=(1-Pr(b<d_top))/2`.

A no-balanced candidate therefore forces `Pr(b<d_top)>2/3` and

`Pr(b<a)>5/6`.

This is an exact new threshold, not a heuristic.

### 5. Clean equal-predecessor fork escalation is finite

Under the account04/B10 equal-predecessor theorem, span descent immediately creates unequal predecessors (old left endpoint is the distinguisher); a clean fork recursion strictly raises the left endpoint in the poset. Therefore it must reach unequal predecessors after finitely many steps.

## Exact regression evidence

Verifier Git blob `6828b47d32f82879f26ca0e63afd254868be23ef`; output blob `6afa33b8d1065d5964b30b77bb04e1be5650774b`, terminal marker `POS3_B19_CUT_CHARGE_FORK_COLLAPSE_CHECK_PASS`.

On the 349-extension prior B19 witness, cut charge passes for every ordered retained pair and exposes the two known balanced chain-interface escapes. On the 79-extension Hasse-fork witness, the positive channels are `{5:10,6:23}` and the first blocker pair already has unequal predecessor sets.

## Earliest remaining global implication

The majority-early nested-predecessor branch is now reduced to span descent or a quantitative two-blocker fork. The clean equal-predecessor recursion is also finite. Concentrate on the **majority-late nested-predecessor corridor**, using:

- partner endpoint polarity `Q+R>4E/3` and `Q>2E/3` when `M` is nonempty;
- the delayed-chain correction/crossing trichotomy above;
- the `>5/6` endpoint threshold when there is no successor distinguisher;
- the `>1/81` pinned-rank and simultaneous heavy-slice constraints.

Force a balanced chain-touching pair, a strict span descent, a four-antichain, a proper autonomous nonchain, or a contradiction in the next boundary flux. Do not uniformize the induced chain-deletion law.
