# FOREST / account02 B01 — Cocks-free two-cut scalar obstruction with exact outside response

**Run:** `B01-20260922T050132Z-forest-r15`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Role:** alternative separator/deletion-contraction proof, retaining the actual boundary-connectivity distribution and induced weights.

## 1. Fresh source state and correction to the previous local route

Fresh owner control was read from `yspennstate/math-research-brain` main at invocation; owner revision `2026-09-22.2` keeps account02/B01 on FOREST and stops new installation/benchmark work.

The latest complete campaign-lead report read in this run is account01/B01
`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T043718Z-b01-forest-auto11/report.md`, blob `adc332e97b112525d92cf601ad1493f2e1745987`.
It withdraws the earlier `FOREST-KN-COCKS-RECONCILED-v3` chain **as written**. The precise issue is the previously used fixed-graph upgrade

`unit pNC on one graph G => M(G) is independence correlated for all positive weights`.

The final Semple--Welsh paper literally records that statement in its post-submission Note, but the lead's source chronology found that later detailed descriptions and the accessible constructive globalization support only a class-level equivalence; the full primary Cocks proof body was not available. The fixed-graph theorem is therefore not used here. This report does not assert that Semple--Welsh or Cocks is mathematically wrong; it follows the campaign's fail-closed source rule.

This corrects one dependency of my preceding r14 report. The r14 three-terminal `K4` response-synthesis theorem remains exact algebra, but **its use as a negative-correlation closure through arbitrary induced positive weights is no longer credited**. The present run builds a unit-weight separator reduction that does not need that bridge.

Named OTHER-account results consumed and applied:

1. **account03/B02**, `20260922T025856Z-b02-forest-r12`, report blob `c60fbadfe8abd2e5b3afcf93c6b5ae45900c3de6`. Its exact theta-3 simulator proves that the unit FOREST target for simple graphs is equivalent to the unit target for finite loopless multigraphs, with covariance scaled by `4/81` across distinct gadgets. This lets edge-minimality pay both deletion and contraction strata without importing positive weights.
2. **account03/B02**, `20260922T032505Z-account03-B02-r11`, source-review blob `75028150088c9c6b931032a22760e762c58daffb`. I retain its direct check of the Semple--Welsh definitions and complete-graph algebra, but its fixed-Cocks conclusion is superseded for this run by the later lead correction above.
3. **account04/B01**, `account04-b01-20260922T043827Z-forest-r13`, report blob `759684087c34ffa3a92a7f26d2d4e9584b8c5c30`. I reuse its exact two-cut bridge algebra, but not its Section 5 weighted closure, which also depends on the disputed fixed-graph step.
4. **account01/B20**, `20260922T022012Z-b20-forest-r11`, report blob `6cd587f800b871eb30b029e18db4077875b24a01`, theorem `FOREST-QUADRATIC-SIMPSON-BRIDGE-20260922`. Its one-coordinate Rayleigh identity is specialized below to the actual separator fugacity rather than used as a generic weighted theorem.

Primary source reference for the source distinction: Semple--Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), DOI `10.1017/S0963548307008978`, especially the all-positive-weight definition of independence correlation and the final Section 5 Note. Cocks: *Correlated Matroids*, CPC 17(4) (2008), DOI `10.1017/S0963548308009152`. No access control was bypassed.

## 2. Unit minimality in the loopless-multigraph universe

Assume the source conjecture is false. By account03/B02's exact theta-3 theorem, choose a **loopless multigraph** counterexample `M` with the minimum number of labelled nonloop edges, and a violating pair `e,f`.

This enlargement is source-equivalent to the simple target and has one crucial advantage: deleting or contracting a third edge stays in the same unit-law universe after loops are discarded. Thus every proper deletion/contraction minor has nonnegative unit Rayleigh gaps by minimality.

Ordinary component and one-vertex-cut factorization still excludes disconnected or 1-sum obstructions. The question addressed here is what a genuine 2-vertex cut would have to look like without any fixed-graph unit-to-weight theorem.

## 3. Exact two-cut setup with the real outside response

Let `{u,v}` be a genuine 2-vertex cut. Separate every original direct `uv` edge as its own singleton bridge. For every non-singleton `uv`-bridge `B_i`, let

- `D_i` be the unit forest count in `B_i` with `u,v` disconnected;
- `C_i` be the unit forest count in `B_i` with `u,v` connected.

For a singleton direct `uv` edge, set `D_i=C_i=1` at unit weight. Since two distinct bridges cannot both connect `u` to `v` inside one forest, the global partition function is

`Z_M = prod_i D_i + sum_i C_i prod_{j!=i} D_j`.

For a fixed non-singleton bridge `B_i`, define the **actual outside response**

`lambda_i = sum_{j!=i} C_j/D_j > 0`

and the outside scale `K_i=prod_{j!=i}D_j`. Then

`Z_M = K_i [ C_i + (1+lambda_i) D_i ]`.

No normalization has replaced `lambda_i`; it is the exact boundary-connectivity odds supplied by the other bridges.

## 4. Cross-bridge marked pairs close without Cocks

For an edge `h` in a non-singleton bridge `B_i`, write derivatives of `C_i,D_i` with respect to its unit activity and set

`Q_i(h)=D_i (C_i)_h - C_i (D_i)_h`.

For a singleton direct separator edge, set `Q_i(h)=1`.

If `e in B_i` and `f in B_j` with `i!=j`, direct differentiation of the bridge formula gives the exact cancellation

`R_M(e,f) = (prod_{k notin {i,j}} D_k)^2 Q_i(e) Q_j(f)`.          (4.1)

Now augment a non-singleton `B_i` by one new labelled edge `g_i=uv` at **unit** weight. Because all original direct `uv` edges were separated as singleton bridges, this augmented loopless multigraph `H_i=B_i+g_i` has fewer edges than `M`. Its Rayleigh gap for `(h,g_i)` is exactly

`R_Hi(h,g_i)=Q_i(h)`,                                               (4.2)

independent of the activity assigned to `g_i`.

Minimality therefore gives `Q_i(h)>=0`; singleton responses equal `1`. Equation (4.1) proves:

> **Cocks-free cross-bridge lemma.** In an edge-minimal unit loopless-multigraph counterexample, no violating marked pair can lie in two distinct bridges of a 2-cut.

This removes half of the previous two-cut dependence on a positive-weight upgrade.

## 5. Same-bridge pairs reduce to one exact scalar Simpson window

The only remaining two-cut possibility has both marked edges `e,f` in one non-singleton bridge `B=B_i`. Drop the subscript and put

`D=D_i`, `C=C_i`, `Z=C+D`, `lambda=lambda_i`.

Add one virtual edge `g=uv` with activity `s>0`. The augmented bridge has forest polynomial

`P(s)=C+(1+s)D = Z+sD`.

For the marked pair define the two endpoint gaps

`d0 = Z_e Z_f - Z Z_ef`,

`d1 = D_e D_f - D D_ef`,

and the boundary-response derivatives

`Q_e = D C_e - C D_e`,

`Q_f = D C_f - C D_f`.

Here `d0` is the unit gap in `B`, while `d1` is the unit gap after contracting `g` (equivalently identifying `u,v`, with loops discarded). Both are nonnegative by loopless-multigraph minimality. Also `Q_e,Q_f>=0` by (4.2).

Write

`R(s)=P_e(s)P_f(s)-P(s)P_ef(s)=d0+m s+d1 s^2`.

Specializing account01/B20's exact mixed-coefficient identity gives

`Z D m = D^2 d0 + Z^2 d1 - Q_e Q_f`.                              (5.1)

For every `s>0`, rearranging (5.1) yields the exact equivalence

`R(s)>=0`

iff

`Q_e Q_f <= T(s)`,                                                 (5.2)

where

`T(s)=D(D+Z/s)d0 + Z(Z+D s)d1`.                                  (5.3)

The original graph uses the **actual outside value** `s=lambda`, so its same-bridge gap is

`R_M(e,f)=K_i^2 R(lambda)`.

The smaller augmented bridge `H_i` is unit-good by minimality, so `R(1)>=0`, equivalently

`Q_e Q_f <= T(1)=(Z+D)(D d0+Z d1)`.                              (5.4)

The difference between what unit minimality pays and what the real outside response demands is exactly

`T(lambda)-T(1)
 = (Z D/lambda)(lambda-1)(lambda d1-d0)`.                          (5.5)

Therefore a two-cut violation in an edge-minimal counterexample must satisfy **all** of

`Q_e>0`, `Q_f>0`,

`T(lambda) < Q_e Q_f <= T(1)`,                                    (5.6)

and hence the strict orientation mismatch

`(lambda-1)(lambda d1-d0) < 0`.                                  (5.7)

This is the main new reduction of the run.

### Safe region already closed

If

`(lambda-1)(lambda d1-d0) >= 0`,

then `T(lambda)>=T(1)`, and (5.4) automatically implies (5.2) at the true outside response. Thus the same-bridge case closes at unit weight without any Cocks theorem whenever

- `lambda>=1` and `lambda d1>=d0`, or
- `lambda<=1` and `lambda d1<=d0`.

Only the opposite Simpson orientation remains.

Degenerate consequences are immediate: if `d0=d1=0`, no same-bridge violation is possible; if `d1=0<d0`, an obstruction requires `lambda>1`; if `d0=0<d1`, it requires `lambda<1`.

## 6. Compact conditional end-to-end separator argument

The alternative route can now be stated without a positive-weight fixed-graph assumption.

1. Use account03/B02 theta-3 simulation to work with an edge-minimal unit loopless-multigraph counterexample.
2. Components and 1-sums factor.
3. At a 2-cut, cross-bridge marked pairs are impossible by the unit augmented-bridge gaps (4.1)--(4.2).
4. A same-bridge violating pair must satisfy the exact narrow window (5.6) and orientation mismatch (5.7) at the **actual** outside response `lambda=sum C_j/D_j`.
5. Therefore the first unpaid 2-separator implication is no longer “upgrade the smaller bridge to every positive weight.” It is the strictly narrower, source-unit statement:

> **`FOREST-2CUT-SCALAR-DEBT-v1`.** For every source-realizable unit `uv`-bridge/outside pair occurring in the minimal loopless-multigraph setup, prove
> `Q_e Q_f <= T(lambda)`
> in the only unresolved region `(lambda-1)(lambda d1-d0)<0`.

Closing that implication would rule out every 2-cut and leave the graph-global 3-connected obstruction. It preserves the real boundary distribution and induced response instead of normalizing it away.

## 7. Deletion-contraction warning for the r14 three-terminal cone

The previous r14 response-synthesis cone used the signature

`v=(d,a,b,c,t)`

and conditions

`tau=d t-(ab+ac+bc)>=0`,

`abc-tau*t>=0`.

A tempting next induction would prove these inequalities for deletion and contraction children and then add their signatures. That is false even at the level of genuine unit graph signatures.

- The edgeless three-terminal graph has `v0=(1,0,0,0,0)` and `(tau,gap)=(0,0)`.
- The two-edge `V` on terminals with edges `12,13` has `v1=(1,1,1,0,1)` and `(tau,gap)=(0,0)`.
- Their coordinatewise sum is `(2,1,1,0,1)`, for which `tau=1` but `abc-tau*t=-1`.

So the K4-synthesizable signature cone is **not closed under arbitrary addition**. This is a source-valid refutation of the naive cone-additivity lemma, not a counterexample to the FOREST target.

I then retained the actual single-edge partition-transition support: an addable deletion forest may coarsen only

`D -> D/A/B/C`, `A -> A/T`, `B -> B/T`, `C -> C/T`, `T -> T`.

Even those support restrictions plus child cone inequalities are not sufficient abstractly. The nonnegative transition table archived in the checker gives deletion signature `(27,8,8,8,8)` with cone values `(24,320)` and contraction signature `(7,3,8,5,12)` with `(5,60)`, while their parent sum `(34,11,16,13,20)` has `(tau,gap)=(153,-772)`.

That table is **not asserted graph-realizable**. Its purpose is narrower and rigorous: any deletion-contraction proof of the r14 cone must use a genuine endpoint/terminal realizability law, not just the allowed partition-transition support and the two child inequalities.

## 8. Exact executable regression

Artifact: `separator_scalar_bridge_check.py`  
SHA-256: `37d12c31b2885122853f38cc3c3658ee69a3730facd2a25d89a37c95c91273b4`.

Captured stdout: `separator_scalar_bridge_check.out`  
SHA-256: `99c96a6a289da4ed17940ad2e551beaec41bb08c7240233083a4d7818d2079a0`.

It checks (5.2)--(5.5) over 112,500 exact rational parameter cases and verifies both cone counterexamples. Exact stdout:

```text
PASS scalar_threshold_identity cases=112500
PASS threshold_difference_identity cases=112500
CONE_ADD_COUNTEREXAMPLE child0=(1, 0, 0, 0, 0) cone=(0, 0)
CONE_ADD_COUNTEREXAMPLE child1=(1, 1, 1, 0, 1) cone=(0, 0)
CONE_ADD_COUNTEREXAMPLE sum=(2, 1, 1, 0, 1) cone=(1, -1)
ABSTRACT_TRANSITION_TABLE (7, 3, 8, 3, 0, 0, 0, 4, 2, 4, 4, 6, 8, 4, 2, 4)
ABSTRACT_TRANSITION child_delete=(27, 8, 8, 8, 8) cone=(24, 320)
ABSTRACT_TRANSITION child_contract=(7, 3, 8, 5, 12) cone=(5, 60)
ABSTRACT_TRANSITION parent_sum=(34, 11, 16, 13, 20) cone=(153, -772)
NOTE abstract transition table is not asserted graph-realizable
PASS
```

The algebraic derivation above is the proof; the script is regression evidence only.

## 9. Status

**Classification: `ESSENTIAL_STEP_APPLIED`.** A subsidiary induction candidate was also refuted, but the surviving two-cut route materially advanced: cross-bridge pairs are closed Cocks-free, and every remaining same-bridge obstruction is localized to the exact scalar window (5.6)--(5.7) at the true outside boundary response.

The parent FOREST conjecture remains **OPEN**. This is not a `FULL_PROOF_CANDIDATE` and makes no novelty, priority or publication claim. The immediate next mathematical action is to attack `FOREST-2CUT-SCALAR-DEBT-v1` from source-realizable bridge structure, preferably by expressing `Q_e,Q_f,d0,d1` as a common switching/path-cut flow and proving the required upper bound only in the unsafe orientation region. Account01/B20's path-cut flux theorem is a natural input, but no unproved flow inequality is assumed here.

No brain installation, benchmark work, scheduler mutation, benchmark material, credentials, unrelated private data, email, Drive, public posting, paid model/API/Codex call, remote workflow, permission change, or production activation occurred.
