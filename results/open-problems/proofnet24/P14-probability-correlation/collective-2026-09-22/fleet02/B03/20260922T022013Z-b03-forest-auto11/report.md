# FOREST fleet02/B03 — exact parallel aggregation and sharp book-graph separator adversary

**Run:** `20260922T022013Z-b03-forest-auto11`  
**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** **ESSENTIAL_STEP_APPLIED**  
**Parent FOREST target:** **OPEN / not promoted**  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source snapshot

The active assignment is to construct exact adversaries to the current counting/separator route, especially overlapping cycles and induced parallel-edge intermediates, then replace the false intermediate with a correct sufficient statement.

Fresh coordination controls were read from `yspennstate/math-research-brain` main initially at `6f007489092924b3360b74fb5e72e0f7dba09747`; a later refresh before scientific publication saw main `6591b0ef29d2f1f1645ce0f5a2cdbf17cb615402` with the same active owner control `2026-09-22.2`, programme and FOREST allocation. No later applicable stop/pause was present.

The latest complete campaign-lead handoff consumed was fleet01/B01 run `20260922T010823Z-b01-forest-auto11`, handoff blob `032497949594326305913cb8871c00ab7d0dc528`, candidate `FOREST-KN-COCKS-REDUCTION-v2`. Its compact conditional chain is:

1. exact unit-weight forest pNC for every complete graph `K_n` by the lead's Hermite calculation;
2. the fixed-graph Cocks upgrade `unit pNC on G => M(G) independence-correlated for all positive weights`;
3. Semple--Welsh Proposition 3.5 weighted minor closure;
4. delete the nonedges of `K_n` and specialize surviving weights to one.

This run independently source-checked the final Semple--Welsh paper. Its final note explicitly attributes to Cocks the fixed-graph statement in step 2, and Proposition 3.5 explicitly states weighted minor closure. Cocks's 2008 Cambridge abstract states the class-level equivalence and that it answers Semple--Welsh open questions. The gated Cocks proof body was not obtained in this run, so this report is **not** an owner-gate end-to-end review of the lead full candidate. The local separator mathematics below is independent of whether the citation review is ultimately accepted.

Relevant published sources:

- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423--435, DOI `10.1017/S0963548307008978`; final note on p.13 and Proposition 3.5 on pp.6--7.
- C. C. Cocks, *Correlated Matroids*, CPC 17 (2008), 511--518, DOI `10.1017/S0963548308009152`.

The named OTHER-account result actually consumed and applied is fleet03/B01 run `20260922T003307Z-fleet03-B01-r11`, report blob `4bfacc593182b192e927df9a5bde6e14caa7e4de`. It gives the exact activity-cube representation of the original unrooted uniform forest law and, for an ordered pair `x<y`,

`4 Delta_G(x,y) = W_x (W_y + q_xy) - W W_xy`.

I use this below to rewrite the remaining separator cross-term in source-law activity variables.

## 2. Correct parallel-class aggregation lemma

Let `M` be a loopless multigraph and

`Z_M(y) = sum_{F forest} product_{h in F} y_h`.

Let `C` range over parallel classes and let `Q` be the simple quotient obtained by replacing each parallel class `C` with one edge. Put

`Y_C = sum_{h in C} y_h`.

Then exactly

`Z_M({y_h}) = Z_Q({Y_C}).`                                      (2.1)

### Proof

A forest contains at most one edge from any parallel class. After selecting the set of parallel classes used, cyclehood depends only on their endpoint pairs and not on which representative was chosen. For each used class `C`, summing the weights of all possible representatives contributes exactly `Y_C`. Summing over quotient forests proves (2.1). Loops may be deleted because no forest contains them.

A marked original edge `e in C` is represented by the **derivative operator** `partial/partial Y_C`, not by the event that the aggregate quotient edge is selected. In particular,

`partial_e Z_M = partial_C Z_Q`.

For marked `e in C`, `f in D` with `C != D`,

`partial_e partial_f Z_M = partial_C partial_D Z_Q`.

If `e,f` are distinct members of the same class, the mixed derivative is zero. Therefore the derivative-Rayleigh bracket has exactly the same sign after aggregation (up to the obvious positive marked-weight factors if one uses inclusion-weight rather than derivative conventions). This is the precise way to simplify a contraction-created multigraph.

**Correction to my preceding run.** Keeping every marked parallel member as a separate variable is sufficient but unnecessarily strong. Exact aggregation is safe provided the class weight is the **sum** of member weights and a marked original member is tracked by the corresponding derivative, rather than reinterpreted as the aggregate-class event.

For a simple graph `G`, contracting one edge `g=uv` creates only parallel classes of size one or two: a size-two class occurs exactly at a common neighbor `x`, from the old edges `ux,vx`. Thus a one-edge contraction of a unit simple graph is exactly a simple quotient with weights in `{1,2}`, together with the marked-member derivative convention above. Replacing those `2`'s by `1` is not legitimate.

## 3. Infinite overlapping-cycle adversary: the book graphs

For `k>=2`, let `B_k` be the simple **book graph** consisting of `k` triangles sharing a common spine edge

`g=01`.

For page `i`, let its other vertex be `x_i` and its two spokes be

`a_i=0 x_i`, `b_i=1 x_i`.

Mark

`e=a_1`, `f=a_2`.

These are genuine simple-graph adversaries with overlapping cycles. Conditioning on `g` also produces exactly the induced parallel-edge intermediate that a deletion/contraction or separator proof must handle.

Give only `g` an external weight `w>0`, all other edges weight one, and write

`Z=A+wB`,
`Z_e=a0+w a1`,
`Z_f=b0+w b1`,
`Z_ef=c0+w c1`.

### 3.1 Exact counts

When `g` is present, each page may be in exactly three states: neither spoke, only `a_i`, or only `b_i`. Hence

`B=3^k`,
`a1=b1=3^(k-1)`,
`c1=3^(k-2)`.

When `g` is absent the graph is `K_{2,k}`. A selected edge set is a forest iff at most one page contains both spokes. Hence

`A = 3^k + k 3^(k-1) = 3^(k-1)(k+3)`,

`a0=b0 = 2 3^(k-1) + (k-1)3^(k-2) = 3^(k-2)(k+5)`,

and, for `k>=3`,

`c0 = 3*3^(k-2) + (k-2)3^(k-3) = 3^(k-3)(k+7)`;

for `k=2` the same value is `c0=3` by direct count.

Define the endpoint gaps and mixed coefficient

`D0=a0 b0-A c0`,
`D1=a1 b1-B c1`,
`M=a0 b1+a1 b0-A c1-B c0`.

Then the formulas collapse to

`D0 = 4*3^(2k-4)`,
`D1 = 0`,
`M  = 0`.

Therefore

`Q(w)=Z_e Z_f-Z Z_ef = 4*3^(2k-4)`                       (3.1)

for **every** finite `w>0`.

The two edge-vs-spine cross gaps are

`P_e = B a0-A a1 = 2*3^(2k-2)`,
`P_f = B b0-A b1 = 2*3^(2k-2)`.                          (3.2)

### 3.2 Exact parallel contraction versus the false unit simplification

Contracting `g` identifies vertices `0` and `1`. Each page becomes a parallel class of size two. By (2.1), the exact simple quotient is a star with **class weight 2 on every spoke**. Thus

`B=(1+2)^k=3^k`,

and a fixed original marked member is represented by the class derivative, giving

`a1=b1=3^(k-1)`, `c1=3^(k-2)`,

exactly as above.

If multiplicity is falsely forgotten and the quotient star is made unit-weight, then instead

`B_naive=2^k`, `a1_naive=2^(k-1)`.

Feeding this false contraction state into the deletion/contraction cross-gap gives

`P_e^naive = B_naive a0 - A a1_naive`
`           = 2^(k-1) 3^(k-2) (1-k) < 0`                  (3.3)

for every `k>=2`, whereas the true `P_e` in (3.2) is positive. Thus the naive unit-simple contraction reverses the sign of a load-bearing separator quantity on an infinite family of simple source graphs.

The smallest member `B_2=K_4-{x_1x_2}` is already decisive: true affine counts are

`(A,B,a0,a1,b0,b1,c0,c1)=(15,9,7,3,7,3,3,1)`,

with `P_e=P_f=18`; the naive unit contraction gives `B'=4`, `a1'=b1'=2`, and the hybrid cross gaps become `-2,-2`.

This refutes the mechanism, not the FOREST conjecture.

## 4. Correct sharp separator statement: the Simpson budget

The clean form of the one-edge separator obstruction is a conditional-covariance identity, not a coefficientwise positivity claim.

Let `mu_w` be the forest law in which only `g` has weight `w>0`. Its conditional laws given `g=0` and `g=1` do not depend on `w`; call them `mu_0,mu_1`. Put

`alpha=P_w(g=0)=A/(A+wB)`,
`beta =P_w(g=1)=wB/(A+wB)`.

For `i=0,1` let

`c_i = -Cov_{mu_i}(1_e,1_f)`,

and define the conditional drifts

`d_e = P_0(e)-P_1(e)`,
`d_f = P_0(f)-P_1(f)`.

The law of total covariance gives the exact identity

`Cov_w(1_e,1_f) = -alpha c0 - beta c1 + alpha beta d_e d_f`.  (4.1)

Hence, whenever the two endpoint conditional laws are pairwise negatively correlated (`c0,c1>=0`), the full law is negatively correlated for this pair at the actual response `w` iff

`d_e d_f <= c0/beta + c1/alpha`.                         (4.2)

If `d_e d_f<=0`, this is automatic. If a separator proof must tolerate **every** positive response `w`, then `beta` ranges over `(0,1)` and minimizing the right side yields the exact all-response criterion

`d_e d_f <= (sqrt(c0)+sqrt(c1))^2`.                      (4.3)

In count variables,

`c0=D0/A^2`, `c1=D1/B^2`,
`d_e=P_e/(AB)`, `d_f=P_f/(AB)`,

so (4.3) is exactly

`P_e P_f <= (B sqrt(D0)+A sqrt(D1))^2`.                  (4.4)

This gives a corrected sufficient statement with no hidden weighting convention.

### 4.1 The book family is sharp

For `B_k`,

`P_0(e)=P_0(f)=(k+5)/(3(k+3))`,
`P_1(e)=P_1(f)=1/3`,

so

`d_e=d_f=2/(3(k+3))`.

Moreover

`c0=4/(9(k+3)^2)`, `c1=0`.

Therefore

`d_e d_f = (sqrt(c0)+sqrt(c1))^2`                        (4.5)

**exactly for every `k>=2`**.

Thus the all-response separator criterion is sharp: no universal multiplicative reserve `<1` can replace its right side. For each finite `w`, (3.1) is still strictly positive; equality in the normalized all-response envelope is approached in the boundary regime `w -> infinity` (`beta -> 1`).

This is stronger than a one-off sign counterexample: the same infinite overlapping-cycle family simultaneously (i) forces exact parallel weights after contraction, (ii) reverses the naive cross-gap sign, and (iii) saturates the corrected Simpson budget.

## 5. Applying the named fleet03/B01 activity result

For the original unit simple graph, fleet03/B01 gives, after choosing the pair order appropriately,

`Xi_eg := W_e(W_g+q_eg)-W W_eg = 4 Delta_G(e,g) = 4 P_e`,

and similarly

`Xi_fg = 4 P_f`.

Therefore the sharp all-response separator obligation (4.4) is equivalently

`Xi_eg Xi_fg <= 16 (B sqrt(D0)+A sqrt(D1))^2`.            (5.1)

This is an exact use of the partner's activity coupling: the dangerous cross-stratum Simpson term is now represented entirely by source-law activity-weighted tree/exchange masses, while `D0,D1` are the conditional forest gaps. The book family has equality in (5.1), so any activity argument seeking a fixed strict factor below the right side is impossible.

This identifies the first essential missing implication for the separator route very tightly:

> under the minimal-counterexample / separator geometry, prove (5.1) **at constant 1**, or find a source-valid graph violating it. Strict-slack variants are already refuted by the book family.

The remaining issue is not how to simplify contraction-created parallel edges: (2.1) resolves that exactly. It is the quantitative exchange-vs-conditional-covariance budget in (5.1).

## 6. Exact certificate

The exact enumerator beside this report checks `B_k` for `k=2,...,6`, including all affine counts, the constant Rayleigh polynomial, the conditional-covariance equality, exact weighted contraction, and the naive sign reversal.

- `book_parallel_certificate.py`, blob `b45ac9891420cd8b6062b1753a72ea200e31c008`.
- `book_parallel_certificate.out`, blob `e2e5048be294e62bdcb5a75f575483e36d679303`.

The output ends `STATUS=PASS`. The finite checker is regression evidence only; the displayed formulas above are proved for all `k>=2` by direct counting.

## 7. Status, failures, and next exact action

**Status: ESSENTIAL_STEP_APPLIED.** Parent FOREST remains open in this report. I did not promote the campaign lead's global candidate because this run did not inspect the gated Cocks proof body and therefore is not a complete owner-gate end-to-end review.

Refuted intermediate mechanisms:

- simplifying contraction-created parallel classes to unit simple edges;
- any all-response separator bound with a graph-independent multiplicative reserve strictly below the exact Simpson envelope.

Corrected mechanisms retained:

- exact parallel-class aggregation by summed class weights plus marked-member derivative tracking;
- exact Simpson budget (4.2) at the actual response and (4.3)/(4.4) for all responses;
- partner activity translation (5.1).

The next mathematical action on this SAME target is to attack (5.1) at constant one using the fleet03/B01 exchange-class structure together with the lead's minimal-counterexample matching/external-negative constraints, or to produce a source graph that violates that exact implication. No further work should use a unit simplification of induced parallel classes.

## 8. Operational record

Fleet02 managed inventory was inspected only for this account: 20/20 managed slots were enabled and hourly-valid, B03 was role-aligned, quiet delivery was preserved, and no scheduler mutation was made. No deficit requiring a B20 report was observed.

Model self-report: **GPT-5.6 Sol**. Requested effort: **maximum actually supported**. Configured effort: **UNKNOWN_NOT_EXPOSED**. Known/self-reported effort: **UNKNOWN**. Provider reasoning usage/time: **null / NOT_EXPOSED**. Observed elapsed execution at report finalization: **546.593 seconds**; this is wall-clock work including source reads, derivation, computation and connector time, not pure thinking.

Scoped privacy/secret review: this artifact contains mathematical statements, public-source references, immutable repository revisions/blobs and non-sensitive operational status only. It contains no credentials, scheduler identifiers, machine paths, private transcripts, benchmark gold, unrelated private data, email/Drive material, or production-brain state.
