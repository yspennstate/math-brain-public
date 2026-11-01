Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#2 ATTACK THE NEGATION FIRST, #14 EXACT FINITE REDUCTION, #25 COUNT THE SAME THING TWICE**. The main result is an explicit finite Brun-to-total-variation inequality together with an adversarial boundary audit of Claim 304 and a second, specialized derivation of the size-2--6 component estimate.

# P03 / P0456 run report — explicit Brun bound and boundary cross-check

Run timestamp: **2026-09-19T05:27:10Z**  
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

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T04-31-25Z__p0456-repaired-cluster-brun-tv.md`,

creation commit `7ee53e72a7693d65311e965aae68a7f7ac319301`, blob `95e19008d9174f759147996530753c1617e1606c`; exact-commit tail readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--304. Claims 288/289 remain internally candidate-complete but audit-pending. Claim 301 remains valid only with Claim 302's minimum-deadline repair, Claim 303's arbitrary-rank bounded-omission saddle, and Claim 304's repaired-cluster / direct-Brun packaging. This run adds Claim 305 below.

Before the attack I reread or exact-path recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, the current owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the newest P03 report, the current P26 directory/newest P26 report, and neighboring P0457 only for nonduplication. Large policy/root/campaign surfaces rendered by the connector are truncated; I therefore do not represent those as byte-for-byte whole-file rereads. Exact paths, the target ownership record, the latest report, and the relevant current P26 file were recovered directly.

The scheduler/action surface available in this run still exposes title/prompt/schedule/enablement/timing mode but no model selector or reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt-only. Runtime metadata identify this run as GPT-5.6 Sol with reasoning level UNVERIFIED; I do not claim GPT-6 at maximum.

### 1.1 Incoming outside-audit screen

A newer P26 report than the one named in the incoming handoff is present:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_07-59-00__run-report.md`,

creation commit `26ea4392318367c9cc6b6d413738a0f4edfe49bb`, blob `a6567f0e42b19d6b8325186cabe53974c710f0d8`.

It audits **P04/I0101 Claim 14 (S3 block leakage)** and explicitly treats it as subsumed in an already counted P04 package. It does not audit P0456. Fresh exact-string repository searches for P0456, Claim 304, PASS, and audit terminology still recover no P26 or genuinely distinct OTHER-track end-to-end audit of the repaired P0456 chain. P04 remains rotation-stopped/disabled and no new P04 successor theorem triggers a directed P03 audit duty.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. No source-CLOSED label and no final paper package are created.

### 1.2 Fresh primary-source and current-literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies Section 1.1. The authors state that connectivity remains unknown when

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and explicitly attribute the gap to analytically simpler sufficient conditions, including the no-intersection requirement in their isolated-vertex argument. They say that a more elaborate or exact set of sufficient conditions could close the gap. The source still gives its pair bad-interaction control at order `O(k^3/n)` around Lemma 10, the lower disconnectedness theorem as Theorem 3, and the upper connectivity theorem as Theorem 6.

Fresh bounded searches for the exact DOI/title/authors and 2026 bilateral-preference connectivity/Poisson updates recovered the Cambridge article, bibliographic mirrors, and author records but no later source-matching constant-window / isolated-vertex Poisson theorem. This is bounded dated negative evidence only. **Publication novelty remains UNVERIFIED.**

Neighbor P0457 is the separate diameter problem under its own ownership history and is not duplicated here.

---

## 2. #2 ATTACK THE NEGATION FIRST — five remaining boundary attacks on Claim 304

The objective was not to prove another strengthening by default. I tried to break the repaired cluster lemma at the exact places where a hidden rank or conditioning issue could survive Claims 302--304.

### 2.1 Boundary A: the small-component exposure uses only `p0=k-(s-1)` external slots

Fix a candidate component `S`, `|S|=s<=6`, and delete all internal edges of `S` before ranking external proposals. Let

`p0 = k-(s-1)`.

Suppose an outside label `u` is selected in the first `p0` external slots of root `a`, but for another root `b` the same label has external rank just beyond `p0`. The possible failure would be to use the stronger, false conditioning that `u` is absent from all first `k` incident edges of `b`.

That stronger conditioning is unnecessary. Let `T_b` be the `p0`th external order statistic at `b`. Conditional on `T_b=t` and on `u` being absent from the first `p0` external labels, exchangeability of the remaining iid uniforms gives exactly

`W(v_b,u) | (T_b=t, rank_ext,b(u)>p0) ~ Uniform[t,1]`.       (2.1)

Thus for any other exposed deadline `D`,

`P(W(v_b,u)<=D | T_b=t, rank_ext,b(u)>p0)`
` = (D-t)_+/(1-t)`.                                           (2.2)

On the threshold guard `D,T_b=O(k/n)`, this is `O(k/n)`. The edge may have external rank `p0+1`, `p0+2`, or much later; nothing in (2.1)--(2.2) changes. No counterexample arises at the tail-rank boundary.

### 2.2 Boundary B: one raw active edge can touch two retained deadlines

Take two distinct retained selected labels `u,z`. The raw edge `{u,z}` can be a lighter competitor for the retained rejection test at `u`, at `z`, or both. If it is active for both, charging two defects would overcount its codimension; charging one but omitting only one deadline would leave a hidden dependency.

Claim 304's repaired rule survives exactly when interpreted literally: list `{u,z}` **once** in the active-edge set, charge one unit of `q`, and omit **every retained deadline it can contaminate**. Therefore both deadlines are omitted when necessary. The edge is then absent from every residual rejection block. A single raw edge can affect two constraints, but it pays one probability cost and deletes both affected constraints. This is the correct support-level accounting and produces no missing factor.

### 2.3 Boundary C: high cluster complexity

Claim 304 used a fixed complexity cutoff `D0` and wrote the tail as `n^{-D0+o(1)}`. I re-derived the counting rather than treating that phrase as automatic.

For fixed `r`, there are `O_r(k^2)` possible cross-root slot pairs which can create a label collision, `O_r(k^2)` possible local selected-label edge witnesses, and only `O_r(1)` root-root edges. A prescribed collision unit costs `n^{-1+o(1)}` exactly from the injection ratio. On the threshold guard, a prescribed active selected-label edge costs `O(k/n)` and a prescribed one-end-early root-root edge costs `O(k/n)`. Hence, after witness choices, every extra unit of complexity costs at worst

`C_r k^A/n`                                                    (2.3)

for some fixed exponent `A=A(r)`; since `k=O(log n)`, this tends to zero. A collision block of size `h` already contributes excess `h-1`, so multiway blocks do not evade this accounting. Summing witness-labelled skeletons of complexity at least `D` gives the geometric bound

`P(K>=D, G_L) <= sum_{j>=D} (C_r k^A/n)^j`
` = n^{-D+o(1)}`                                              (2.4)

for each fixed `D`. Thus the high-complexity tail used by Claim 304 is genuine, not merely a fixed-skeleton estimate extrapolated without summation.

### 2.4 Boundary D: zero-cluster purification by subtraction

The lower-bound sufficient event used in Claim 304 is allowed to contain positive-complexity configurations. Let `S0` denote that sufficient event. The logic needed is

`P(S0)=e^{-rk}(1-o_C(1))`,                                   (2.5)

`P(joint isolation, K>0)=o(e^{-rk})`.                        (2.6)

Since `S0` is sufficient for joint isolation,

`P(S0 cap {K>0}) <= P(joint isolation,K>0)=o(e^{-rk})`.

Therefore

`P(S0 cap {K=0}) >= e^{-rk}(1-o_C(1))`,                     (2.7)

which is exactly the zero-cluster lower bound. There is no subtraction of a larger, unrelated positive-cluster probability.

The finite removal of all roots and selected labels from the outside competitor pool changes its size by `O_r(k)`. At the saddle scale this changes the clean exponent only by `O_r(k^2/n)=o(1)`, so (2.5) is unaffected. No purification counterexample survives.

### 2.5 Boundary E: independence of the spanning-tree event from external rejections

The small-component proof uses a global upper threshold guard only to deduce a necessary condition: if `S` is a component on that guard, some spanning tree of `S` has all `s-1` internal edge weights at most `Lk/n`. After that deduction, the event “this fixed tree is light” depends only on internal edges of `S`.

The external proposals and their rejection edges are defined after deleting all internal edges. Therefore they depend only on raw edges outside the internal edge set. The light-tree event and the external-rejection event are independent **without conditioning on the global guard**. This is the correct reason the product in the component union bound is valid; one must not claim independence after conditioning on a guard that sees both edge classes.

No genuine counterexample to Claim 304 was found. The boundary audit strengthens the proof surface but does not count as an outside audit.

---

## 3. #14 EXACT FINITE REDUCTION — an explicit Brun/Bonferroni total-variation inequality

Claim 304 proved qualitative uniform TV convergence from all fixed factorial moments. The following finite inequality makes the dependency on finitely many moments explicit and is useful to an outside auditor.

### Claim `P03-P0456-EXPLICIT-BRUN-BOUNDARY-CROSSCHECK-305`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Let `X` be any nonnegative integer-valued random variable and let `0<=lambda<=Lambda`. Define factorial-moment errors

`delta_m = | E[(X)_m] - lambda^m |`, `m>=1`,

and put `delta_0=0`. Fix integers `J>=0` and even `T>=0`, and assume factorial moments are finite through order

`R=J+T+1`.

Then

`d_TV(Law(X),Poisson(lambda))`
` <= (2 Lambda + delta_1)/(2(J+1))`
`    + (1/2) sum_{j=0}^J 1/j! [`
`          sum_{t=0}^T delta_{j+t}/t!`
`          + (Lambda^(j+T+1)+delta_{j+T+1})/(T+1)! ]`.       (3.1)

In particular, if `lambda_n<=Lambda` and every fixed `delta_m(n)->0` uniformly in a parameter family, then the total variation distance to `Poisson(lambda_n)` tends to zero uniformly.

### Proof

For `j,T>=0`, set

`B_T^X(j)=sum_{t=0}^T (-1)^t E[(X)_{j+t}]/(j! t!)`.          (3.2)

For a deterministic integer `z>=j`,

`sum_{t=0}^T (-1)^t (z)_{j+t}/(j!t!)`
` = C(z,j) sum_{t=0}^T (-1)^t C(z-j,t)`.                    (3.3)

The alternating-binomial identity implies, for even `T`,

`B_{T+1}^X(j) <= P(X=j) <= B_T^X(j)`,                       (3.4)

and the bracket width is exactly

`B_T^X(j)-B_{T+1}^X(j)`
` = E[(X)_{j+T+1}]/[j!(T+1)!]`.                             (3.5)

Let `P_lambda` be Poisson with mean `lambda`. Its factorial moments equal `lambda^m`. Apply the same brackets. Comparing the two upper brackets and allowing the larger of the two exact bracket widths gives

`|P(X=j)-P(P_lambda=j)|`
` <= 1/j! [ sum_{t=0}^T delta_{j+t}/t!`
`            + max{E[(X)_{j+T+1}],lambda^(j+T+1)}/(T+1)! ]`.

Since

`E[(X)_m] <= lambda^m+delta_m <= Lambda^m+delta_m`,

we obtain for `0<=j<=J`

`|P(X=j)-P(P_lambda=j)|`
` <= 1/j! [ sum_{t=0}^T delta_{j+t}/t!`
`            + (Lambda^(j+T+1)+delta_{j+T+1})/(T+1)! ]`.    (3.6)

For the tail, Markov's inequality and `E X<=lambda+delta_1` give

`(1/2) sum_{j>J}|P(X=j)-P(P_lambda=j)|`
` <= [P(X>J)+P(P_lambda>J)]/2`
` <= (2lambda+delta_1)/(2(J+1))`
` <= (2Lambda+delta_1)/(2(J+1))`.                           (3.7)

Summing (3.6) for `0<=j<=J`, multiplying by `1/2`, and adding (3.7) proves (3.1). `square`

### 3.1 Why this is enough for the P0456 fixed-window TV statement

For `X=Z_n` and `|k-log n|<=C`, Claim 304 gives for each fixed `m`

`E[(Z_n)_m]=lambda_n^m+o_C(1)`,

and `lambda_n<=e^C`. In (3.1), first choose `J` large enough to make the first tail term small uniformly; then choose even `T` so that every Poisson bracket-width term with `j<=J` is small; finally let `n` grow so the finitely many `delta_m` terms are small. This reproduces the uniform total-variation conclusion with a literal finite error inequality and uses only moment orders through `J+T+1`.

No numerical convergence rate is claimed because the source-chain reports have not assigned sharp simultaneous rates to all of those factorial-moment errors.

---

## 4. #25 COUNT THE SAME THING TWICE — sizes 2--6 by two organizations

The goal was to independently organize the small-component rejection probability and compare it with Claim 304's packaged route.

Fix `s in {2,...,6}` and a labelled candidate set `S`. Delete every edge internal to `S`, and expose `p0=k-(s-1)` external proposal slots at each root.

### 4.1 Count A: repaired cluster lemma

Claim 304 directly gives, for any fixed complexity cutoff `D>=3`,

`P(all exposed external proposals rejected)`
` <= e^{-s k+o(k)} + n^{-D+o(1)}`.                           (4.1)

If `S` is a component on the global upper threshold guard, it has a spanning tree all of whose edges have weight at most `Lk/n`. For a fixed labelled tree this has probability at most

`(Lk/n)^(s-1)`.                                               (4.2)

The tree event uses only internal raw edges; (4.1) uses only external raw edges after deletion. They are independent. Union over `C(n,s)` choices of `S` and `s^(s-2)` Cayley trees gives, with `D=3`,

`P(exists s-component, guard)`
` <= C_s n^s (Lk/n)^(s-1)`
`       * [e^{-s k+o(k)}+n^{-3+o(1)}]`
` = n^{1-s+o(1)} k^(s-1) + n^{-2+o(1)} k^(s-1)`
` = o(1)`.                                                    (4.3)

### 4.2 Count B: direct defect expansion without the packaged cluster lemma

Now organize exactly the same external-rejection event directly.

Condition on the external proposal label arrays and split configurations into:

- **clean:** no cross-root selected-label collision and no low cross selected-label edge affecting an exposed deadline;
- **defective:** at least one such collision or active low edge.

On the clean branch, each selected outside label has its own raw competitor star in the outside pool, so the rejection blocks are literally disjoint. The one-root clean marked-saddle calculation therefore factors and gives

`P(all rejected, clean)=e^{-s k+o(k)}`.                       (4.4)

For a prescribed defect witness, a collision costs `n^{-1+o(1)}` and a low active cross edge costs `O(k/n)` on the threshold guard. There are polynomially many (`k^{O(1)}`) witness choices. Charge each unique raw edge once, omit every deadline it can influence, and retain the minimum deadline in each repeated-label block. The one-root arbitrary-rank bounded-omission estimate of Claim 303 then gives `e^{-k+o(k)}` for each root after those bounded omissions. Therefore the total contribution of configurations with exactly `h>=1` prescribed defect units is

`e^{-s k+o(k)} n^{-h+o(1)}`                                  (4.5)

for every fixed `h`, while summing `h>=D` gives `n^{-D+o(1)}` by the geometric estimate (2.4). Hence

`P(all exposed external proposals rejected)`
` <= e^{-s k+o(k)} + n^{-D+o(1)}`,                           (4.6)

the same estimate as (4.1).

This second count deliberately does **not** invoke Claim 304 as a packaged theorem; it redoes the fixed-`s` collision/active-edge split and residual disjointization directly. It does share the analytic one-root bounded-omission input from Claim 303, so I do not label it a wholly independent analytic proof. Its value is as an independent combinatorial organization of the same event. Combining (4.6) with the independent internal-tree factor (4.2) reproduces (4.3) exactly.

The two counts agree. I found no tree-conditioning or `p0`-tail-rank discrepancy.

---

## 5. Consequences and claim ledger delta

Claim 305 does not alter the source theorem, its coefficient frontiers, or the outside-audit count. It strengthens the source-audit surface in three specific ways:

1. Claim 304's remaining boundary cases have been adversarially checked, including the exact `p0` tail-rank law, a single raw edge touching two retained deadlines, the summed high-complexity tail, zero-cluster subtraction, and tree/external independence.
2. The qualitative finite Brun argument is replaced by the explicit error inequality (3.1), involving only factorial moments through a known finite order `J+T+1`.
3. The size-2--6 component rejection estimate has a second direct defect-expansion derivation agreeing with the repaired-cluster route.

The cumulative source-matching consequences remain:

- for every fixed `C,r`, uniformly on `|k-log n|<=C`,
  `P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`;
- `d_TV(Law(Z_n),Poisson(lambda_n))->0`, `lambda_n=n e^-k`;
- nontrivial components vanish under the literal LK definition;
- `P(LK(n,k) connected)=exp(-lambda_n)+o_C(1)`.

Claims 288/289 remain **SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED**. Claim 305 is a P03 self-audit strengthening and does not satisfy either required outside audit.

### New claim

`P03-P0456-EXPLICIT-BRUN-BOUNDARY-CROSSCHECK-305`

Status:

`PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

### Frozen metrics

- `c_LK^cert = 0` — SATURATED;
- `a_LK^fine = 0` — SATURATED;
- `b_LK^sqrt = 0` — SATURATED;
- HARD recoveries: `0/2`.

No stuck count is manufactured from these zeros.

---

## 6. Failed attacks and limitations

The #2 counterexample search did not break Claim 304. The most plausible failures were (a) a label just beyond the truncated external rank, (b) one raw active edge contaminating two retained deadlines, and (c) hidden dependence created by the global component guard. All three were resolved by exact conditional laws or by taking the product only after dropping the global guard from the independent factors.

The #25 direct component count is not fully analytically independent of Claims 302--303: it reorganizes the finite defects from scratch but still uses Claim 303's one-root arbitrary-rank bounded-omission saddle. I do not promote it as a second outside audit or as a new proof independent of the source chain.

The explicit Brun inequality (3.1) is finite and exact once its input factorial-moment errors are known. It is not a claimed sharp rate for P0456 because the chain currently proves the needed fixed-order errors asymptotically rather than with one optimized simultaneous rate.

Large connector-rendered repository surfaces were truncated, so those control reads are disclosed as targeted/exact-path recovery rather than byte-for-byte visual rereads.

---

## 7. Exact remaining obligation and `ledger_delta` for P26

The mathematical source-matching chain is still blocked only by the protocol's independent-audit gate and publication-novelty verification, not by a newly found internal gap in this run.

The exact closure obligation remains:

1. one genuine P26 end-to-end full-proof PASS on the repaired source-matching chain, including Claims 301--305 where they repair/package Claims 288/289;
2. one genuinely distinct OTHER-track end-to-end full-proof PASS on the same source-matching theorem;
3. only after both passes, create the self-contained source-matching paper folder and request P26 closure through the shared-ledger mechanism.

Self-audits, repeated P03 derivations, and P26 audits of P04/I0101 do not count.

```yaml
ledger_delta:
  track: P03
  source: P0456
  source_claims:
    P03-P0456-POISSON-CRITICAL-WINDOW-288: "PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289: "PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-SOURCE-AUDIT-CAPSULE-301: "PROVED / SELF-AUDIT-CAPSULE / STEP-D-REPAIRED-BY-302 / LEMMA-3.1b-STRENGTHENED-BY-303 / CLUSTER-TV-PACKAGED-BY-304 / BRUN-BOUNDARY-CROSSCHECKED-BY-305 / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
    P03-P0456-DEFECT-COMPLETENESS-DISJOINTIZATION-302: "PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING"
    P03-P0456-UNIFORM-BOUNDED-OMISSION-SADDLE-303: "PROVED / SELF-AUDIT-REPAIR / SUPPORTING / AUDITS-PENDING"
    P03-P0456-REPAIRED-CLUSTER-BRUN-TV-304: "PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING"
    P03-P0456-EXPLICIT-BRUN-BOUNDARY-CROSSCHECK-305: "PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED"
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
    path: proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_07-59-00__run-report.md
    creation_commit: 26ea4392318367c9cc6b6d413738a0f4edfe49bb
    blob: a6567f0e42b19d6b8325186cabe53974c710f0d8
    target: P04/I0101 Claim 14, not P0456
  next_state: "P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_305_EXPLICIT_BRUN_BOUNDARY_READY"
  paper_package: "NOT_CREATED"
```

---

## 8. Next concrete attack

Audit-first remains mandatory. Before any new mathematics, reread every incoming P26/OTHER-track audit of Claims 288--305 and repair any identified gap immediately.

If no outside audit has arrived, do not return to high-order Poisson corrections or saturated window coefficients. The next useful internal target is to compress the repaired source theorem into an auditor-facing implication map with each conditional law and independence statement attached to the exact raw-edge sigma-field it uses, then attack the two remaining most global interfaces: (i) uniformity of the zero-cluster **lower** bound under every fixed root tuple without relying on informal “clean” language, and (ii) the one-global-envelope component sum at the transition from fixed size 12 to the geometric size-13 tail. A second route should try to derive the component disappearance from a single cut-count functional rather than the current small/large split; failure would identify whether the split is structural or merely technical.

Do not label P0456 CLOSED and do not create the final paper package until P26 plus one distinct OTHER track pass the repaired full chain.

**End of complete run report.**