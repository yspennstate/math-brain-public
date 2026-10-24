Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`, and no saturated zero is converted into a stuck count. This run uses **#4 PROVE SOMETHING WEAKER, COMPLETELY, #10 DERANDOMIZE, #27 SWAP THE QUANTIFIERS**. The strongest new result is an exact finite product formula for the clean fixed-root lower event, eliminating the remaining prose-level conditioning step in the lower joint-isolation bound.

# P03 / P0456 run report — exact clean lower factorization

Run timestamp: **2026-09-19T14:31:19Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity and audit-first screen

The exclusive ownership claim remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The user handoff entering this invocation named Claim 312 as newest, but the repository contains a later complete P03 report:

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T13-33-06Z__p0456-low-complexity-codimension.md`,

creation commit `a15604b754f58cf5401dafa6d67c6b3e3d92a46f`, blob `4d3620ae80f02bacba435571d11a6e1bf46ae743`; exact tail readback recovers `**End of complete run report.**`.

Therefore I continue from Claim 313 rather than redoing the stale requested `#2/#25/#30` triple. The current fleet rule forbids using the same triple twice consecutively, so this run uses the nonconsecutive audit/simplification triple **#4, #10, #27**.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--313. In particular:

- Claim 288 remains `PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 289 remains the interaction repair/strengthening.
- Claim 305 remains the sole finite Brun/Bonferroni total-variation conversion.
- Claim 308 remains the clean one-root analytic input at actual quota `h=k`.
- Claim 309's `r>=3` root-merge repair remains mandatory; the false shortcut “below both deleted-array kth thresholds implies bilaterally selected” is never restored.
- Claim 310's example `q_a^*<d_a` remains a mandatory guard against overclaiming exactness of the safe root suffix.
- Claim 311's complete incidence graph `Gamma_0` and canonical `K=c+p+q` remain the controlling positive-interaction skeleton.
- Claim 312 remains the auditor-facing fixed-C dependency DAG and source-failure upper cover.
- Claim 313 remains the exact low-complexity conditional codimension lemma; in particular source Lemma 10 is a strict subset of the canonical support taxonomy because canonical `q` also sees subdeadline support edges of selected-neighbor rank greater than `k`.

This run reread the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, current owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical P0456 claim, the newest complete P03 report, current task-health evidence, the newest P26 run, and neighboring `operations/claims/P0457.md` only for nonduplication. Several large control surfaces are connector-truncated; those are targeted current-path rereads, not claimed byte-for-byte reconstructions. P0457 remains a distinct diameter target owned by NM13-04.

### 1.1 Incoming outside-audit evidence

The newest P26 report recovered before the mathematical attack is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_17-00-50__run-report.md`.

It is a full independent audit of **P0459 bilateral-preference degree concentration**, not P0456. Fresh repository searches for `P0456 PASS`, `P26-AUDIT P0456`, Claim 313 terminology, and the repaired chain still recover no P26 or genuinely distinct OTHER-track end-to-end P0456 PASS. Therefore the gate remains exactly

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits never count. I do **not** label the source CLOSED and do **not** create a final paper package.

---

## 2. Fresh source/status/prior-art check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

The Cambridge PDF was freshly reopened and page images checked. Section 1.1 still states that connectivity is unknown throughout

`log n - (1/2) loglog n sqrt(log n) <= k <= log n + (1/2) loglog n sqrt(log n)`,

and says the gap likely comes from analytically simpler sufficient conditions, explicitly including the no-intersection condition in the isolation proof; the authors say a more elaborate or exact sufficient condition could close the gap.

The requested checkpoints remain unchanged on the current PDF. Lemma 10 proves `P(B)=O(k^3/n)` for the pairwise bad-interaction event. Lemmas 11--12 bound the bad isolation branch. Lemma 13 gives exact conditional independence on the source good event and Lemma 14 uses it for the pair second-moment ratio. Theorem 3 is the `t'<-1/2` disconnectedness result; Theorem 4 rules out bounded degree in the upper regime; Theorem 5 rules out medium/large components for `k=t log n`; and Theorem 6 gives connectivity for `t'>1/2`.

Fresh bounded searches dated 19 September 2026 for the exact DOI/title/authors, bilateral-preference connectivity, Poisson isolated vertices and 2026 follow-ups recovered the Cambridge publication and adjacent material but no later source-matching fixed-window connectivity / isolated-vertex Poisson theorem. This remains bounded negative evidence only. **Publication novelty is UNVERIFIED.**

---

## 3. Why attack the lower branch now

Claim 313 made the positive-cluster edge codimension literal. The remaining lower-bound sentence in Claim 306 was mathematically plausible but compressed several conditionings into prose: global proposal-label distinctness, late root-root edges, an absolute threshold guard, removal of all root/selected labels from the competitor pools, and the product over selected-label blocks.

The source theorem does not need a more ambitious interaction expansion here. It needs one completely explicit sufficient event whose probability is `e^{-rk}(1-o_C(1))`. This run proves exactly that event by a finite factorization identity.

---

## 4. #4 PROVE SOMETHING WEAKER, COMPLETELY — define one exact sufficient event

Fix `r,C<infinity`, deterministic distinct roots

`R={v_1,...,v_r}`,

and an integer `k` with `|k-log n|<=C`. Delete all root--root edges temporarily. Put

`N_0=n-r`.

For root `v_a`, order its `N_0` root-to-outside weights increasingly:

`X_{a,1}<...<X_{a,k}<...`,

and let `U_{a,j}` be the outside label attached to `X_{a,j}`. Let

`D = {all rk labels U_{a,j} are globally distinct}`.

On `D`, let `S={U_{a,j}:1<=a<=r,1<=j<=k}` and

`E=V\(R union S)`,  `N_1=|E|=n-r-rk`.

For a proposal deadline `x`, define

`q(x)=P(Bin(N_1,x)>=k)`,
`Q(x)=int_0^x q(s) ds`.

Choose the deterministic guard level

`t_n = 8k/N_0`.

For large `n`, `t_n<1`. Let

`G={X_{a,k}<=t_n for every root a}`,

and let

`H={every root--root raw edge has weight > t_n}`.

For each selected label `u=U_{a,j}`, let `C_u` be the event that at least `k` raw edges `{u,x}` with `x in E` have weight strictly less than `X_{a,j}`. Set

`C=intersection_u C_u`

and define the clean lower event

`L_R = D cap H cap G cap C`.

### Lemma 4.1 — deterministic sufficiency

`L_R subset {I_{v_1}=...=I_{v_r}=1}`.

#### Proof

On `G cap H`, every root--root edge is heavier than the deleted-array kth outside deadline at each endpoint where it is incident. Hence restoring root--root edges does not change any root's first `k` proposals: they remain exactly the `k` outside edges with deadlines `X_{a,1},...,X_{a,k}`.

Now fix one such proposal `{v_a,u}` of weight `X_{a,j}`. Event `C_u` supplies `k` distinct incident raw edges `{u,x}`, `x in E`, all lighter than this proposal. Therefore `{v_a,u}` is not among the `k` lowest-weight edges incident to `u`, so it cannot be retained bilaterally. Every edge outside the root's top `k` is already rejected at the root endpoint. Thus no edge incident to any root survives, and every root in `R` is isolated. `□`

This sufficiency statement does not ask whether any competitor edge itself survives the LK rule. Only its raw weight matters.

---

## 5. #10 DERANDOMIZE — exact finite factorization

The combinatorics and the raw-edge probability now separate exactly.

### 5.1 Exact distinct-label factor

For one root, its ordered first-`k` labels form a uniformly random ordered `k`-tuple without replacement from the `N_0` outside labels, independently of its ordered values. Different root arrays are independent after root--root deletion. Therefore

`P(D) = (N_0)_{rk}/(N_0)_k^r`.                               (5.1)

This is exact, not an asymptotic birthday approximation.

### 5.2 Conditional external-block product

Condition on any fixed globally distinct ordered label array satisfying `D`. Then `E` is deterministic with `|E|=N_1`. For every selected label `u`, the raw block

`B_u = {W({u,x}): x in E}`

contains exactly `N_1` iid Uniform[0,1] coordinates. If `u != z` are selected labels, the blocks `B_u` and `B_z` are disjoint raw-edge sets because the selected--selected edge `{u,z}` is excluded by `z notin E`. Every `B_u` is also disjoint from every root proposal edge and from every root--root edge.

Hence, conditional on the root proposal deadlines,

`P(C | D, all proposal values) = product_{a=1}^r product_{j=1}^k q(X_{a,j}).`  (5.2)

No residual dependence remains.

### 5.3 One-root truncated clean factor

Let `X_1<...<X_k` be the first `k` order statistics of `N_0` iid Uniform[0,1] variables. Define

`M_t(N_0,N_1;k)
 := E[ 1{X_k<=t} product_{j=1}^k q(X_j) ].`                  (5.3)

The joint density of the first `k` order statistics is

`(N_0)_k (1-X_k)^(N_0-k)`

on `0<X_1<...<X_k<1`. Integrating the first `k-1` coordinates gives the exact identity

`M_t
 = (N_0)_k/(k-1)! int_0^t q(x) Q(x)^(k-1)(1-x)^(N_0-k) dx`.  (5.4)

Since `d(Q(x)^k)=k q(x)Q(x)^(k-1)dx`, integration by parts yields

`M_t
 = (N_0)_k/k! Q(t)^k(1-t)^(N_0-k)
   + (N_0)_{k+1}/k! int_0^t Q(x)^k(1-x)^(N_0-k-1) dx`.       (5.5)

At `t=1` the boundary term vanishes, so

`M:=M_1
 = (N_0)_{k+1}/k! int_0^1 Q(x)^k(1-x)^(N_0-k-1) dx`.   (5.6)

This is exactly Claim 308's clean marked integral with `m=N_0`, competitor-pool parameter `N=N_1`, and actual quota `h=k`.

### 5.4 Exact joint formula

The root proposal arrays are independent across roots. Event `H` uses only the `binom(r,2)` root--root raw weights, which are independent of all root-to-outside arrays and all external blocks. Therefore (5.1)--(5.6) give the **exact finite identity**

`P(L_R)
 = [(N_0)_{rk}/(N_0)_k^r]
   (1-t_n)^{binom(r,2)}
   M_{t_n}(N_0,N_1;k)^r`.                                  (5.7)

There is no unrecorded conditioning factor in (5.7).

---

## 6. Quantitative comparison with Claim 308

We now show every prefactor in (5.7) is `1+o_C(1)` relative to the clean `e^{-rk}` scale.

### 6.1 Label distinctness

A union bound over cross-root rank pairs gives

`1-P(D) <= binom(r,2) k^2/N_0`,                              (6.1)

so

`P(D)=1+O_r(k^2/n)`.                                         (6.2)

### 6.2 Root--root lateness

Since `t_n=8k/N_0`,

`(1-t_n)^{binom(r,2)}=1+O_r(k/n)`.                           (6.3)

### 6.3 Full clean integral

Here

`|N_0-n|+|N_1-n| = O_r(k)`.

Thus Claim 308 applies uniformly on the fixed `C` window and gives

`M=e^{-k}[1+O_{C,r}(exp(-k/20))]`.                           (6.4)

The quota is exactly `h=k`; no shifted-quota centering error occurs.

### 6.4 Truncation at the absolute guard

Since `0<=product_j q(X_j)<=1`,

`0 <= M-M_{t_n} <= P(X_k>t_n)`.                              (6.5)

Now

`X_k>t_n` iff `Bin(N_0,t_n)<=k-1`.

The binomial mean is exactly `N_0 t_n=8k`. By the standard lower-tail Chernoff bound with `delta=7/8`,

`P(X_k>t_n)
 <= exp[-8k(7/8)^2/2]
 = exp[-49k/16]`.                                            (6.6)

Relative to `e^{-k}` this is `exp[-33k/16]`, much smaller than the Claim-308 error. Consequently

`M_{t_n}=e^{-k}[1+O_{C,r}(exp(-k/20))]`.                     (6.7)

Substituting (6.2), (6.3), and (6.7) into (5.7) gives

`P(L_R)
 = e^{-rk}[1+O_{C,r}(exp(-k/20)+k^2/n)]`.                   (6.8)

In particular,

`P(I_{v_1}=...=I_{v_r}=1)
 >= e^{-rk}(1-o_C(1))`.                                      (6.9)

The estimate is uniform over every deterministic tuple of `r` distinct roots.

---

## 7. #27 SWAP THE QUANTIFIERS — what is uniform, and why

The lower event can now be quantified in the strongest form actually needed by the source theorem:

> For every fixed `r,C`, uniformly over all integers `k` with `|k-log n|<=C` and **simultaneously over every deterministic tuple of `r` distinct roots**, (6.8) holds.

No averaging over root locations is used. The exact formula depends on the tuple only through the cardinalities

`N_0=n-r`, `N_1=n-r-rk`,

which are the same for every tuple. The label-distinctness factor, root-edge factor, one-root order-statistic integral, and truncation tail are therefore identical for all deterministic root tuples.

This is the useful quantifier swap. I do **not** extend the relative center `e^{-k}` to bounded quota shifts: Claim 307 already proves that such a statement is false (`h=k-1` changes the relative center by a factor tending to `e`). Positive clusters continue to use quota-aware exponential-scale Claim 303, not the lower event proved here.

---

## 8. New claim and effect on the source chain

### Claim `P03-P0456-CLEAN-LOWER-EXACT-FACTORIZATION-314`

**Status:** `PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed `r,C`, deterministic distinct roots `R`, and integer `|k-log n|<=C`, define `L_R` as in Section 4 with `t_n=8k/(n-r)`. Then `L_R` implies joint isolation and has the exact probability

`P(L_R)
 = [(n-r)_{rk}/(n-r)_k^r]
   (1-8k/(n-r))^{binom(r,2)}
   M_{8k/(n-r)}(n-r,n-r-rk;k)^r`,                            (8.1)

where `M_t` is the finite order-statistic integral (5.4)/(5.5). Uniformly,

`P(L_R)=e^{-rk}[1+O_{C,r}(exp(-k/20)+k^2/n)]`.               (8.2)

Therefore the lower fixed-root joint-isolation bound is `e^{-rk}(1-o_C(1))` with an exact raw-edge factorization and no hidden conditioning bias.

#### Consequence

Claim 314 replaces the prose probability calculation in Claim 306's lower branch. It uses Claim 308 only for the one-root integral and uses **none** of Claims 303, 309--313 except as conceptual safeguards. The upper fixed-root bound remains the canonical positive-cluster route through Claims 309--313 plus Claim 303. Hence Claim 312's fixed-C theorem remains candidate-complete with a strictly cleaner lower dependency DAG.

---

## 9. Literal component layer recheck

Claim 314 changes no component argument.

For `2<=s<=6`, internal candidate-component edges are deleted before external proposal ranking, so the internal spanning-tree raw-edge family is disjoint from the external rejection family. The product is exact after the global guard is dropped from the product factors.

For `7<=s<=12`, the fixed-size part of the single global threshold envelope uses the exponent `1-(5/32)s`, negative already at `s=7`. For `13<=s<=n/2`, the same global event and `(n-s)/(n-1)>=1/2` give the geometric exponent `1-(5/64)s`, negative from `s=13`. The global-envelope failure is paid once. No connectivity conclusion is inferred from mean degree.

Thus the internal fixed-C source theorem remains

`P(LK(n,k) connected)=exp(-n exp(-k))+o_C(1)`,

with the same outside-audit and publication-novelty qualifications.

---

## 10. Methods tried and what happened

### #4 PROVE SOMETHING WEAKER, COMPLETELY

Instead of strengthening the whole interaction theorem again, I isolated only the lower joint-isolation branch. This succeeded: the event `L_R` is a finite sufficient event with a complete exact probability formula (5.7). It no longer depends on any prose claim that label distinctness, root-edge lateness, and external rejection “essentially” factor.

### #10 DERANDOMIZE

Conditioning on a fixed globally distinct ordered proposal-label array turns the random support geometry into deterministic disjoint raw-edge blocks. The only remaining randomness is independent root proposal values, root-root weights, and external selected-label blocks. This gives the exact factorization rather than an approximate independence statement.

### #27 SWAP THE QUANTIFIERS

The exact formula shows the estimate is uniform simultaneously over every deterministic fixed root tuple and the whole fixed `C` window. The attempted stronger shift-uniform center remains false, exactly as Claim 307 records; this run does not revive it.

---

## 11. Cumulative status and ledger delta

Preserved without downgrade:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains PPP; Claims 291--300 remain historical support only.
- Claim 301 remains valid only with the explicit repairs/strengthenings through Claim 314.
- Claim 305 remains the sole TV conversion.
- Claim 308 remains the clean one-root saddle.
- Claims 309--313 remain controlling positive-interaction repairs/support.

New:

`P03-P0456-CLEAN-LOWER-EXACT-FACTORIZATION-314 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

The measurable coefficient metrics remain saturated:

`c_LK^cert=0`, `a_LK^fine=0`, `b_LK^sqrt=0`.

HARD recoveries remain `0/2`.

Current protocol state becomes

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_314_CLEAN_LOWER_FACTORIZATION_READY`.

---

## 12. Exact remaining obligation and `ledger_delta` for P26

The mathematical source chain remains **candidate complete, not CLOSED**. Closure still requires two genuinely independent full-proof audits of the repaired source chain: one by P26 and one by a distinct OTHER track. No P03 self-audit counts.

The next outside auditor should use the reduced route:

1. Claim 308 clean one-root integral;
2. Claim 314 exact clean lower factorization;
3. Claims 309--313 plus Claim 303 for the upper positive-interaction branch;
4. Claim 305 finite Brun TV conversion;
5. the literal component proof.

The `r=3` Claim-309 counterexample and Claim-310 `q_a^*<d_a` example remain mandatory visible safeguards.

`ledger_delta` for P26:

```text
P0456:
  state: ACTIVE_AUDIT_PENDING
  outside_audits: 0/2
  newest_support_claim: P03-P0456-CLEAN-LOWER-EXACT-FACTORIZATION-314
  theorem_status: SOURCE-MATCHING-CANDIDATE-COMPLETE / NOT CLOSED
  lower_branch: exact finite product formula; no Claim303 dependency
  upper_branch: repaired canonical K=c+p+q route with Claims309-313 + Claim303
  required_P26_action: full independent audit of reduced repaired route, including literal component chain
  closure_request: NONE until P26 PASS plus one distinct OTHER-track PASS
  shared_root_edits_by_P03: NONE
```

I do not edit shared root ledgers or peer files.

---

## 13. Next concrete P03 attack

Audit-first remains controlling. At the next run, first reread every new P26/OTHER-track P0456 audit and repair any exact objection before new self-audit work. If no outside audit has arrived, the highest-value self-check is no longer the lower branch: attack the **upper positive-cluster glue** at the interface between Claim 313's conditional edge codimension and Claim 303's arbitrary-rank omission saddle. State one finite conditioning sigma-field for a complete fixed skeleton and verify that every factor used by Claim 303 remains independent of the codimension variables after all root suffixes/collision/support deletions.

Do not compute additional Poisson correction coefficients, enlarge coefficient windows, optimize component cuts, or restore the false `r>=3` root-root shortcut unless an outside auditor identifies a source-level need.

---

**End of complete run report.**