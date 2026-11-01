Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#4 PROVE SOMETHING WEAKER, COMPLETELY, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS**. The main new result is an auditor-facing fixed-window implication map with every dependence statement attached to its raw-edge sigma-field, together with an exact obstruction showing why the current one-global threshold/cut envelope cannot replace the separate size-2--6 component argument.

# P03 / P0456 run report — auditor implication map and the cut-envelope barrier

Run timestamp: **2026-09-19T06:27:17Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T05-27-10Z__p0456-explicit-brun-boundary-crosscheck.md`,

creation commit `7844680b944eea576efa6d2488a5ee47a6a7d6ab`, blob `a3c01d2f46b62b85047a3ce0cc095cfb3fb7deef`; exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--305. Claims 288/289 remain internally source-matching candidate-complete but outside-audit pending. Claim 301 remains valid only with the explicit repairs/packaging in Claims 302--305. This run adds Claim 306 below; it does not change any saturated coefficient metric.

This invocation reread/recovered the root README, hourly protocol, current fleet rules / owner directive, campaign INDEX and RANKING, root POSTED/RESULTS/QUEUE, the canonical P0456 claim, the complete newest P03 report, the relevant Claim-301/304 proof surfaces, current P26 directory/newest P26 report and readback sidecar, and neighboring P0457 only for nonduplication. Large root/policy surfaces rendered by the connector are truncated, so those are targeted exact-path reads rather than claims of byte-for-byte visual rereading.

The exposed task-control surface still has title/prompt/schedule/enablement/timing fields but no binding model-family or reasoning-effort selector. `GPT-6 / maximum` therefore remains prompt-only. Runtime identity for this report is GPT-5.6 Sol; reasoning level is UNVERIFIED.

### 1.1 Incoming outside-audit screen

There is a newer P26 report than the one named in the incoming handoff:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_09-01-52__run-report.md`,

creation commit `5ca4c322654a39ad46d61713b91b6400bec3de1b`, blob `172e08714b27b25c11f665551994a529902c6b99`.

It is an independent audit of **P21 / I0104, direct vector-coordinate degree-four MUB obstruction**, not P0456. Its sidecar records P26's own metric movement `50 -> 51` for that unrelated package. Fresh repository searches for P0456 together with PASS/audit/Claims 288--305 still recover no P26 or genuinely distinct OTHER-track end-to-end proof audit of the repaired P0456 source theorem.

Therefore the P0456 closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. No source-CLOSED label and no final paper package are created.

### 1.2 Fresh primary-source and literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 verifies Section 1.1 unchanged: the authors explicitly say connectivity is not known throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and attribute the gap to analytically simpler sufficient conditions, specifically including the no-intersection condition in the isolated-vertex argument. They say a more elaborate or exact set of sufficient conditions could close the gap.

The source's Lemmas 10--14 remain as previously recorded: Lemma 10 gives `P(B)=O(k^3/n)` for the pair bad-interaction event; Lemma 11 bounds isolation on one-sided bad events; Lemma 12 combines them; Lemma 13 gives the conditional independence on `B^c`; Lemma 14 yields the pair-ratio bound for `t'<-1/2`. Theorem 3 remains the lower disconnectedness theorem for `t'<-1/2`, and Theorem 6 the upper connectivity theorem for `t'>1/2`.

Fresh bounded searches for the exact DOI/title/authors and for 2026 bilateral-preference connectivity / Poisson / isolated-vertex updates recovered the Cambridge article, bibliographic mirrors and author records but no later source-matching constant-window theorem. This is dated bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

Neighbor P0457 remains a separate diameter problem under NM13-04 ownership and is not duplicated here.

---

## 2. #4 PROVE SOMETHING WEAKER, COMPLETELY — the fixed-C auditor implication map

The correction and fixed-fraction strengthening claims are not needed to audit the source theorem. The smallest proof surface needed for the fixed window is the following chain.

### Claim `P03-P0456-AUDITOR-MAP-CUT-BARRIER-306`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix `C<infinity`. Uniformly for integers `|k-log n|<=C`, put `lambda_n=n e^-k`. Then the repaired source proof can be organized into the following implication map:

1. for every fixed `r` and every deterministic tuple of distinct roots `R=(v_1,...,v_r)`,
   `P(I_{v_1}=...=I_{v_r}=1)=e^-rk(1+o_C(1))`;
2. hence every fixed factorial moment of the isolated count `Z_n` is `lambda_n^r+o_C(1)`;
3. Claim 305's finite Brun inequality alone implies
   `d_TV(Law(Z_n),Poisson(lambda_n))->0` uniformly on the fixed C-window;
4. components of sizes 2--6 vanish by the internal-tree / external-rejection argument, while components of sizes 7--`n/2` vanish under one global two-sided kth-threshold envelope;
5. therefore
   `P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.

Every conditional law and factorization in item 1 can be attached to a literal set of independent raw edge weights, as follows.

### 2.1 Raw-edge sigma-fields for the fixed-root proof

Write `R={v_1,...,v_r}` and temporarily remove the `binom(r,2)` root--root edges. For each root `v_a`, expose only the first `p_a=k+O_r(1)` root-to-outside order statistics, their labels, and the terminal exposed threshold. Let

`F_a^prop`

be the sigma-field generated by those exposed data. The underlying raw edge sets `{ {v_a,x}: x notin R }` are disjoint for different roots, hence the `F_a^prop` are independent. By iid exchangeability, ordered labels are independent of ordered values.

If an outside label `u` is absent from the first `p_b` exposed slots of root `v_b`, then conditional on `F_b^prop` and terminal threshold `T_b=t`, its unexposed raw root edge has the exact tail law

`W(v_b,u) | (F_b^prop, u absent) ~ Uniform[t,1]`.             (2.1)

This is the only conditional law used to charge a selected-label / nonowner-root active edge. It is integrated **before** residual factorization.

Let `S` be the set of distinct selected nonroot labels after the label partition is fixed, and put

`E = V \ (R union S)`.

For each `u in S`, let

`F_u^ext = sigma( W({u,x}) : x in E )`.                       (2.2)

For distinct `u,z in S`, the raw undirected edge sets in (2.2) are disjoint: the edge `{u,z}` is excluded because `z notin E`. They are also disjoint from all root proposal edges because `E` contains no root. Thus the `F_u^ext` are mutually independent and independent of the exposed root proposal arrays.

The only remaining raw edges capable of coupling two rejection tests are selected--selected edges, selected-label / nonowner-root edges, and root--root edges. These are exactly the active edges/root-edge patterns recorded in Claim 304. A unique raw active edge is charged once; **every** deadline it can contaminate is omitted. Claim 302's minimum-deadline rule handles repeated selected labels. After these operations every surviving rejection constraint is measurable using one proposal deadline together with exactly one block `F_u^ext`, and the residual blocks are literally disjoint.

This sigma-field map is the complete factorization statement. No recursive bilateral-survival exploration occurs: rejection asks only for raw incident weights lighter than the proposal edge.

---

## 3. #15 BREAK THE SYMMETRY ON PURPOSE — upper and lower fixed-root bounds use different mechanisms

The earlier word “clean” can hide that the two inequalities in the joint-isolation asymptotic are logically different. They should be audited separately.

### 3.1 Upper bound: this is where bounded omissions are needed

Joint isolation forces every exposed root proposal to be rejected at its selected neighbor. Decompose the realized proposal-label configuration into the repaired finite cluster data of Claim 304.

- On the zero cluster, isolation forces the clean outside rejection event. The clean marked-saddle upper bound gives `e^-rk(1+o_C(1))`.
- On every positive bounded-complexity cluster, integrate active edges by (2.1), retain the minimum deadline in each collision block, omit every contaminated/displaced deadline, and use the disjoint residual blocks (2.2). Claim 303 then gives residual rejection probability
  `exp[-rk+O_{C,r}(k^(2/3)+log k)]`.
  The cluster itself costs `n^-K+o(1)` with `K>=1`, so the sum is `o(e^-rk)`.
- Claim 305's high-complexity summation and the threshold-guard Chernoff tail are also `o(e^-rk)`.

Therefore, uniformly for each fixed tuple,

`P(I_{v_1}=...=I_{v_r}=1) <= e^-rk(1+o_C(1)).`              (3.1)

**This is the half of the proof that genuinely needs Claim 303's arbitrary-rank bounded-omission estimate.**

### 3.2 Lower bound: bounded omissions are not needed

For the reverse inequality use one explicit sufficient event `L_R`.

Temporarily delete root--root edges and expose exactly k root-to-outside proposals at every root. Require simultaneously:

1. all `rk` proposal labels are distinct;
2. every root--root raw edge is later than `Lk/n`;
3. every root terminal threshold is at most `Lk/n`;
4. for every selected outside label `u`, there are at least k raw edges `{u,x}`, `x in E=V\(R union S)`, lighter than its root proposal deadline.

On this event, every root proposal is rejected at the selected neighbor, and the late root--root edges cannot enter a root top-k list; hence all r roots are isolated. No selected--selected or cross-root active edge can invalidate the conclusion because condition 4 already supplies k lighter **external** competitors.

The probability calculation uses no bounded omissions. Conditional on the distinct label array and proposal deadlines, condition 4 is a product over the disjoint blocks `F_u^ext`. The clean marked-saddle calculation gives `e^-k(1+o_C(1))` per root. Removing the `O_r(k)` roots/selected labels from the competitor pool changes the clean exponent by only `O_r(k^2/n)=o(1)`. Label distinctness costs `1-O_r(k^2/n)`, root--root lateness costs `1-O_r(k/n)`, and the root-threshold guard loses `o(e^-rk)` mass at the joint scale. Thus

`P(L_R)=e^-rk(1-o_C(1))`,                                    (3.2)

and hence

`P(I_{v_1}=...=I_{v_r}=1) >= e^-rk(1-o_C(1)).`              (3.3)

The bound is uniform over **every deterministic tuple of r distinct roots**. Nothing is averaged over root locations: the complete graph with iid edge weights gives exactly the same raw-edge cardinalities for every tuple, and every displayed error constant depends only on `C,r,L`. Vertex exchangeability may be noted, but it is not a hidden proof step.

Equations (3.1) and (3.3) prove the fixed-r joint-isolation asymptotic. An auditor does not need the zero-cluster purification argument for the lower bound at all; the sufficient event (3.2) is logically simpler.

### 3.3 Factorial moments and TV use only Claim 305

Summing over ordered distinct r-tuples gives

`E[(Z_n)_r]=(n)_r e^-rk(1+o_C(1))=lambda_n^r+o_C(1)`          (3.4)

for every fixed r, uniformly on the C-window.

Set `Lambda=e^C`. Claim 305 gives, for any `J>=0` and even `T>=0`, with `delta_m=|E[(Z_n)_m]-lambda_n^m|`,

`d_TV(Law(Z_n),Poi(lambda_n))`
` <= (2Lambda+delta_1)/(2(J+1))`
` + 1/2 sum_{j=0}^J 1/j! [ sum_{t=0}^T delta_{j+t}/t!`
` + (Lambda^(j+T+1)+delta_{j+T+1})/(T+1)! ]`.               (3.5)

Choose J, then even T, then n. Equation (3.4) makes the finitely many `delta_m` vanish uniformly, proving TV convergence. No subsequence/Scheffe argument and no black-box Poisson theorem are used.

---

## 4. #20 FIND WHY THE ALGORITHM FAILS — the component interfaces

### 4.1 Re-audit of the size-12 / size-13 transition

Claim 301 uses one global event

`H={ a k/(n-1) <= T_v <= b k/(n-1) for every v }`,

with

`a=5/32`, `b=32/5`.

The lower- and upper-threshold Chernoff rates are

`I(a)=a-1-log a >1`, `I(b)=b-1-log b>1`,                    (4.1)

so `P(H^c)=o(1)` by one union bound over vertices. This global failure event is paid **once**:

`P(exists nontrivial component of size >=7)`
` <= P(H^c) + sum_{s=7}^{floor(n/2)} P(exists s-component,H)`. (4.2)

On H, a size-s component has a spanning tree with every tree edge at most `bk/(n-1)`, and every crossing edge at least `ak/(n-1)`. Hence

`P(exists s-component,H)`
` <= C(n,s) s^(s-2) [bk/(n-1)]^(s-1)`
`    * [1-ak/(n-1)]^(s(n-s)).`                               (4.3)

For each fixed s, (4.3) has leading n-exponent

`1-a s`.                                                      (4.4)

Thus all fixed `s=7,...,12` vanish; already at s=7,

`1-7a = 1-35/32 = -3/32`.

For the **uniform** tail `13<=s<=n/2`, using only `(n-s)/(n-1)>=1/2` changes (4.4) to the conservative exponent

`1-(a/2)s`.                                                   (4.5)

At s=12 this is `1/16>0`, so that crude uniform geometric estimate cannot begin there. At s=13 it is

`1-65/64=-1/64<0`,                                           (4.6)

which is exactly why the geometric tail begins at 13. The 12/13 transition is therefore an accounting transition caused by the `1/2` cut-size lower bound, not a model threshold. Equation (4.2) confirms again that `P(H^c)` is not replicated for every size.

### 4.2 Why the same one-global cut envelope cannot replace the size-2--6 proof

This failure has an exact explanation.

Consider the same class of global lower-threshold envelopes with a constant `0<a<1`. To certify

`T_v >= a k/(n-1)` for every vertex

by the vertexwise Chernoff estimate plus a union bound, the route requires

`I(a)=a-1-log a > 1`,                                        (4.7)

because `k=log n+O(1)` and the bound is `n exp[-(I(a)+o(1))k]`.

For a fixed size-s component, the corresponding tree/cut estimate has leading exponent `1-a s`, so this route also requires

`a s > 1`.                                                    (4.8)

For `s<=6`, (4.8) forces `a>1/6`. But `I` is strictly decreasing on `(0,1)`, and

`I(1/6)=log 6-5/6 <1`.                                       (4.9)

For an entirely elementary verification of the strict inequality, the positive exponential series gives

`e^(11/6) > 1+11/6+(11/6)^2/2+(11/6)^3/6+(11/6)^4/24`
`          =186985/31104 > 6`,

so `log 6<11/6`, which is exactly (4.9). Hence **no constant a can satisfy both (4.7) and (4.8) for any s<=6** within this one-global Chernoff-envelope proof route.

For s=7 the obstruction disappears. The actual choice `a=5/32` has `7a=35/32>1` and, as already certified in Claim 301/302, `I(5/32)>1`. Thus size 7 is the first fixed component size that this particular one-global threshold/cut mechanism can certify.

This is the exact obstruction sought by #20. It does **not** prove that every imaginable cut functional must split at 7; it proves that the current global kth-threshold envelope plus vertexwise Chernoff/union-bound mechanism cannot subsume the size-2--6 argument. The small-component external-proposal proof is therefore structural for the present route, not merely cosmetic bookkeeping.

### 4.3 Sizes 2--6 remain literal-LK and independent after the correct deletion

For completeness, fix `2<=s<=6`, a candidate set S, and a labelled spanning tree. Drop the global guard from the product factors after using it only to deduce the necessary light-tree condition. Delete all internal S-edges before ranking external proposals. The internal-tree sigma-field

`sigma(W_e : e subset S)`

is disjoint from the external proposal/rejection raw-edge sigma-field. Hence the light-tree probability `(Lk/n)^(s-1)` multiplies the external rejection bound from Claims 303--305. The resulting union bound is

`n^{1-s+o(1)} k^(s-1) + n^{-2+o(1)}k^(s-1)=o(1)`.

No mean-degree inference enters.

Combining this with (4.2)--(4.6) proves disappearance of every component of size 2 through `n/2` under the literal bilateral-preference definition.

---

## 5. Source theorem from the implication map

A disconnected graph either contains an isolated vertex or a component of size between 2 and `n/2`. Section 4 gives

`P(disconnected and Z_n=0)=o_C(1)`.                           (5.1)

Claim 305 plus (3.4) gives

`P(Z_n=0)=exp(-lambda_n)+o_C(1)`.                            (5.2)

Therefore

`P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`,                (5.3)

uniformly for `|k-log n|<=C`. In particular, if `k-log n->c`, the limit is `exp(-e^-c)` and the isolated count converges in total variation to `Poisson(e^-c)`.

This is the fixed-C source theorem only. None of the first-/second-correction or fixed-fraction strengthening claims is logically needed in this auditor map.

---

## 6. Failures, limitations, and what was learned

The #4 compression succeeded: the source theorem reduces to the one-root clean saddle, Claim 303 only on the **upper** positive-cluster branches, exact residual edge-block dissociation, Claim 305's finite Brun inequality, and the two component mechanisms. The correction claims 295--300 are unnecessary to source matching.

The #15 asymmetry matters. The lower joint-isolation bound is cleaner than the upper bound and does not need arbitrary-rank omissions at all. Any future audit objection to Claim 303 therefore threatens the upper interaction control but does not automatically invalidate the lower isolation construction.

The #20 attempted unification of component sizes failed for an exact reason: the simultaneous inequalities `I(a)>1` and `as>1` are incompatible for `s<=6` in the current one-global threshold-envelope proof. The current size split is therefore technically justified. The separate 12/13 transition inside the large-component proof is merely caused by replacing `(n-s)/(n-1)` by `1/2` for a uniform geometric sum.

Large connector-rendered repository surfaces are truncated; all such reads are disclosed as targeted/exact-path recovery, not byte-for-byte visual rereads.

---

## 7. Claim ledger delta and exact remaining obligation

New claim:

`P03-P0456-AUDITOR-MAP-CUT-BARRIER-306`

Status:

`PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

It packages the repaired fixed-C source proof and proves the exact barrier of the present global cut-envelope mechanism. It is a P03 self-audit and does not count toward either outside-audit slot.

Frozen metrics remain:

- `c_LK^cert=0` — SATURATED;
- `a_LK^fine=0` — SATURATED;
- `b_LK^sqrt=0` — SATURATED;
- HARD recoveries `0/2`.

The exact closure obligation remains:

1. one genuine P26 end-to-end full-proof PASS on the repaired 288/289/301--306 source chain;
2. one genuinely distinct OTHER-track end-to-end full-proof PASS on the same source theorem;
3. only after both passes, create the self-contained source-matching paper folder and request P26 closure through the shared-ledger mechanism.

Self-audits, repeated P03 derivations, and P26 audits of other sources do not count.

```yaml
ledger_delta:
  track: P03
  source: P0456
  source_claims:
    P03-P0456-POISSON-CRITICAL-WINDOW-288: "PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289: "PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-SOURCE-AUDIT-CAPSULE-301: "PROVED / SELF-AUDIT-CAPSULE / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / CLUSTER-TV-PACKAGED-BY-304 / BRUN-BOUNDARY-CROSSCHECKED-BY-305 / AUDITOR-MAP-BY-306 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-AUDITOR-MAP-CUT-BARRIER-306: "PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
  metrics:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    saturation: true
    hard_recoveries: "0/2"
  outside_audits:
    P26: 0
    OTHER_distinct: 0
  newest_P26_screened:
    path: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_09-01-52__run-report.md
    creation_commit: 5ca4c322654a39ad46d61713b91b6400bec3de1b
    blob: 172e08714b27b25c11f665551994a529902c6b99
    target: P21/I0104, not P0456
  next_state: "P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_306_AUDITOR_MAP_CUT_BARRIER_READY"
  paper_package: "NOT_CREATED"
```

---

## 8. Next concrete attack

Audit-first remains mandatory. Before any new mathematics, reread every incoming P26/OTHER-track audit of Claims 288--306 and repair any identified gap immediately.

If no outside audit arrives, do not return to correction coefficients or saturated window frontiers. The next useful internal audit should target the only two black-box analytic inputs still visible in the compressed implication map: (i) rederive the fixed-window clean one-root saddle from an exact finite order-statistic identity with a two-sided relative `1+o_C(1)` bound, and (ii) test whether Claim 303's upper bounded-omission estimate can be replaced, for source matching only, by a monotone domination that requires fewer rank details. Separately, seek a distinct-track auditor rather than manufacturing another P03 “independent” proof.

Do not label P0456 CLOSED and do not create the final paper package until P26 plus one distinct OTHER track pass the repaired full chain.

**End of complete run report.**