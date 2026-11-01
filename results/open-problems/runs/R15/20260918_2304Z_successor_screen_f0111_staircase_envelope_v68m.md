Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; current free-admission state remains `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the full ordered staircase block is now sandwiched exactly between the equal-gap decoupled kernel and a single heterogeneous cardinality-two threshold; for the first non-read-once block the dependence on the upper gap is an explicit increasing concave interpolation between those endpoints. Methods #4 PROVE SOMETHING WEAKER COMPLETELY, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS.**

# 1. Continuity, source fidelity, and ownership

This run continued from the newest R15 report

`runs/R15/20260918_2153Z_successor_screen_f0111_twogap_peeling_u67r.md`.

Before doing new mathematics I re-read/recovered current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest coordinator status `operations/task_health/runs/2026-09-18T215400Z/status.md`;
- the six-run I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest R15 report above;
- the newest neighboring F0111 admission screen `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T22-55-30Z__post-e0086-admission-delta-screen-9-f0111-peeling.md`;
- the canonical F0111 prior-attempt continuity `F0111-A001` in the probability attempt/catalog material.

The root queue still says explicitly that its listed candidates are not certified READY inventory and that newly certified READY entries are zero. The newest coordinator/admission screens likewise do not expose a source-current, ownership-clear free CLOSABLE successor for R15. F0111 remains PENDING / NOT READY, with R15's work only a retained screen and not a canonical source claim. I therefore created no successor claim and did not steal another track's source.

## Burdzy--Scheutzow native target remains frozen

I rechecked the primary source again, not a paraphrase. Burdzy--Scheutzow Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. such that every complete centered future from `S_n` is standard Brownian motion;
- BBM: time reversal is FBM;
- 2BM: there exists one random time `S` such that the complete centered future and past from `S` are **independent standard Brownian motions**.

Problem 7.2 assumes only FBM + BBM and existence of an arbitrary random time `T` for which the two complete centered half-paths are independent. It does **not** impose a stopping-time condition on `T` and does not separately assume that either seam half at `T` is Brownian.

The source-Theorem-6.1 candidate was eliminated because it has no source-valid independent real seam. The later Brownian-prefix/BES candidate was eliminated because the independent seam candidate is actually 2BM after the excursion/Palm argument. Hence there is no live frozen counterexample candidate; historical `2/4` is a retirement/handoff value only. The six-run handoff remains binding and I did not restart I0076 or Problem 7.5.

# 2. Retained F0111 setup

Talagrand's Definition 10.1 uses global positive multilinear polynomials with zero constant term. Problem 10.9 asks whether there exists one universal `gamma>0` such that every cardinality-threshold up-class

`A_{n,k}={X subset [n]: |X|>=k}`

belongs to `C_gamma`.

For a monotone event `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

The preceding R15 block factorization introduced independent Bernoulli variables `X_1,...,X_r` with hazards `u_1,...,u_r`, latent independent Bernoulli variables `Z_1,...,Z_r` with ordered hazards

`0 <= z_1 <= z_2 <= ... <= z_r`,

and the staircase event

`E_r={exists d<=r: Z_d=1 and M_X>=d}`,

where `M_X=sum_i X_i`.

Under the actual Pascal substitution, `z_d=G_{m,k-d+1}`, where

`G_{m,j}=F_{m,j-1}-F_{m,j}`

and the preceding gap-order theorem gives exactly the required ordering.

The last run peeled the common first gap. This run asks a different question: **if `z_1` is frozen, what is the entire range of possible staircase hazards as the higher gaps vary over all ordered values?**

# 3. Method #4 — complete theorem: the ordered staircase has two explicit extremal kernels

## Theorem R15-F0111-STAIR-ENV

Let `F_r(u;z)=F_{E_r}(u_1,...,u_r;z_1,...,z_r)` and put `g=z_1`. Then for every ordered `0<=z_1<=...<=z_r`,

`sum_{i=1}^r Phi(u_i,g)
 <= F_r(u;z)
 <= F_{r+1,2}(g,u_1,...,u_r),`                                  (3.1)

where

`Phi(a,b)=-log(e^{-a}+e^{-b}-e^{-(a+b)})`

and `F_{r+1,2}` is the hazard of the cardinality-two threshold on `r+1` independent Bernoulli coordinates with hazards `(g,u_1,...,u_r)`.

Both bounds are exact extremal values for fixed `(g,u)`:

- the lower endpoint is attained when `z_1=...=z_r=g`;
- the upper endpoint is approached monotonically as `z_2,...,z_r -> infinity`.

### Proof

Condition on `M_X=s`. The staircase fails exactly when

`Z_1=...=Z_s=0`.

Therefore the conditional failure probability is

`exp(-sum_{d=1}^s z_d)`,

with the empty sum interpreted as zero, and hence

`exp(-F_r(u;z))
 = E_u[ exp(-sum_{d=1}^{M_X} z_d) ].`                           (3.2)

Because `z_d>=g`,

`sum_{d=1}^{M_X}z_d >= g M_X`.

Thus

`exp(-F_r(u;z)) <= E[e^{-gM_X}]`

and so

`F_r(u;z)>=-log E[e^{-gM_X}].`

The `X_i` are independent, so

`E[e^{-gM_X}]
 = product_i [e^{-u_i}+(1-e^{-u_i})e^{-g}]`

and each factor equals `exp(-Phi(u_i,g))`. This proves the lower bound in (3.1), with equality when every `z_d=g`.

For the upper bound, increase each `z_d`, `d>=2`, to `+infinity`. This can only increase the event and hence its hazard. In the limit, every `Z_d`, `d>=2`, is identically one. The limiting staircase occurs precisely when

- `M_X>=2`, or
- `M_X=1` and `Z_1=1`.

This is exactly

`Z_1+M_X >= 2`,

the cardinality-two threshold on the `r+1` independent coordinates `(Z_1,X_1,...,X_r)`. Its hazard is `F_{r+1,2}(g,u)`. This proves the upper bound and the asserted sharpness. QED.

## Consequence

For fixed first gap `g`, **all higher-gap combinatorics can be worst-cased away**. The largest possible abstract staircase hazard is not a new family: it is simply the heterogeneous `k=2` threshold.

This is a structural reduction, not a `C_gamma` closure claim. Pointwise domination `F_r<=F_{r+1,2}` does not by itself transfer a Talagrand certificate, because a majorant for the larger kernel can have a base-point budget strictly larger than the actual staircase target.

# 4. Method #13 — the higher gaps are genuine monotone/concave coordinates

The preceding extremal statement is part of a stronger exact monotonicity fact.

## Lemma R15-F0111-STAIR-MONO

Fix all variables except one latent hazard `z_j`. Then

`z_j -> F_r(u;z)`

is increasing and concave on `[0,infinity)`.

### Proof

In (3.2), split according to whether `M_X<j` or `M_X>=j`. With all other hazards fixed,

`exp(-F_r)=A+B e^{-z_j}`

for constants `A,B>=0`. Hence

`F_r(z_j)=-log(A+B e^{-z_j})`.

Writing `x=B e^{-z_j}` gives

`F_r'(z_j)=x/(A+x)>=0`,

`F_r''(z_j)=-A x/(A+x)^2<=0`.                                  (4.1)

QED.

So the gap vector is not an uncontrolled high-curvature object: each higher gap moves the block hazard monotonically and with diminishing returns. This gives a clean interpretation of the previous low-curvature tangent bound.

# 5. Method #27 — swap the quantifiers: exact two-gap interpolation

For the first non-read-once block `r=2`, put

`g=z_1`, `h=z_2>=g`,

and write

`I(h)=F_{E_2}(u,v;g,h)`.

Define the two endpoint hazards

`R_0=Phi(g,u+v)`,                                                (5.1)

`M=F_{3,2}(g,u,v)`.                                              (5.2)

Here `R_0` is the read-once event `Z_1 AND (X_1 OR X_2)`, while `M` is the three-bit majority/cardinality-two event.

## Theorem R15-F0111-TWOGAP-INTERP

For every `h>=g`,

`exp(-I(h))
 = e^{-h} exp(-R_0) + (1-e^{-h}) exp(-M),`                       (5.3)

or equivalently

`I(h)
 = M - log(1+e^{-h}(exp(M-R_0)-1)).`                             (5.4)

Consequently `I` is increasing and strictly concave unless the two endpoints coincide. If

`Y(h)=e^{-h}(exp(M-R_0)-1)`,

then

`I'(h)=Y/(1+Y)`,

`I''(h)=-Y/(1+Y)^2`.                                             (5.5)

At the equal-gap endpoint `h=g`,

`I(g)=Phi(u,g)+Phi(v,g)`,                                        (5.6)

and, with

`T_g(x)=log(1+(e^x-1)e^{-g})`,

`I'(g)
 =(1-e^{-T_g(u)})(1-e^{-T_g(v)}).`                               (5.7)

### Proof

Condition on `Z_2`.

If `Z_2=0`, the event is exactly

`Z_1 AND (X_1 OR X_2)`,

whose hazard is `R_0` because `X_1 OR X_2` has hazard `u+v`.

If `Z_2=1`, the event is

`[Z_1 AND (X_1 OR X_2)] OR [X_1 AND X_2]`,

which is exactly the cardinality-two threshold on `(Z_1,X_1,X_2)`, with hazard `M`.

Since `P(Z_2=0)=e^{-h}`, averaging the two conditional failure probabilities gives (5.3), hence (5.4)--(5.5).

When `h=g`, (3.2) becomes

`E[e^{-gM_X}]`,

which factors into the two one-coordinate terms and proves (5.6).

For (5.7), differentiate the failure expectation with respect to `h` at the common-gap point. Under the common-gap failure tilt, the two `X` coordinates remain independent Bernoulli variables with tilted hazards `T_g(u),T_g(v)`. The derivative is exactly the tilted probability that both are one, giving (5.7). QED.

## Relation to the preceding common-gap correction

The preceding report wrote, for `h=g+delta`,

`I(h)=Phi(u,g)+Phi(v,g)
      +Phi(delta, Phi(T_g(u),T_g(v))).`                          (5.8)

The new result shows that this is not merely a useful decomposition: it is the exact concave interpolation between the two extremal kernels in (3.1). In particular, the old low-curvature estimate is just the tangent inequality for the concave function `I(h)` at `h=g`.

# 6. What changes under the actual Pascal substitution

For the threshold source,

`g=G_{m,k}=F_{m,k-1}-F_{m,k}`,

`h=G_{m,k-1}=F_{m,k-2}-F_{m,k-1}`,

with `h>=g`.

Therefore the exact two-coordinate increment satisfies

`Phi(u,g)+Phi(v,g)
 <= F_{m+2,k}(t,u,v)-F_{m,k}(t)
 <= F_{3,2}(g,u,v).`                                            (6.1)

More generally, the exact `r`-coordinate staircase increment lies below

`F_{r+1,2}(G_{m,k},u_1,...,u_r)`.                               (6.2)

This changes the diagnosis of the block route:

**The higher adjacent gaps are not the essential unresolved object. Once the first gap is fixed, their entire worst-case effect is a heterogeneous cardinality-two threshold.**

The actual remaining obstruction is the first gap itself,

`G_{m,k}=F_{m,k-1}-F_{m,k}`,                                    (6.3)

because substituting a positive polynomial for the difference in (6.2) is exactly where coefficient positivity can fail. The preceding nested-certificate no-go remains relevant here.

Thus the planned split into separate `delta/g` low- and high-curvature proof architectures is no longer the best next route. High curvature simply moves monotonically toward the `k=2` envelope. The more concentrated question is:

> Can the heterogeneous `k=2` certificate be coupled to the baseline `F_{m,k}` in such a way that the single difference (6.3) is never expanded coefficientwise?

That is strictly smaller than the previous two-gap staircase problem.

# 7. A useful exact conditional-deficit interpretation

There is a second way to see the same reduction that may be useful later.

Condition on the old threshold failure `N_m<k`. For the two-gap block define

`c=P(N_m=k-1 | N_m<k)`,

`b=P(N_m=k-2 | N_m<k)`,

`r=P(N_m<=k-3 | N_m<k)`.

Then

`c=1-e^{-g}`,

`b=e^{-g}(1-e^{-h})`,

`r=e^{-(g+h)}`,                                                  (7.1)

and `b+c+r=1`.

If `p=1-e^{-u}` and `q=1-e^{-v}`, the two-coordinate crossing probability conditional on old failure is exactly

`c(p+q-pq)+b pq`.                                               (7.2)

Sending the upper gap `h` to infinity makes `r->0` and `b->e^{-g}`, so (7.2) becomes exactly the three-bit majority probability with the old top-layer indicator having hazard `g`. This is the probability-level reason the upper envelope in (6.1) is sharp.

# 8. What is proved, what is not

Proved analytically in this run, SELF_CHECK_ONLY:

1. the exact staircase failure representation (3.2);
2. the sharp lower/upper staircase envelope (3.1);
3. coordinatewise increasing concavity in every higher latent gap;
4. the exact `r=2` read-once-to-majority interpolation (5.3)--(5.7);
5. the source-level pointwise reductions (6.1)--(6.2).

Not proved:

- no new result on native I0076;
- no universal `gamma` for Talagrand Problem 10.9;
- no transfer from the pointwise k=2 envelope to a positive source polynomial after substituting the first gap;
- no novelty/priority claim;
- no closure or posting claim.

No finite checker was created because these are parameter-uniform analytic identities/inequalities and their complete proofs are on the page. A numerical grid would not certify them.

# 9. Source/current-literature check, dated 2026-09-18 UTC

Primary sources rechecked:

- Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.
- Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

Fresh public queries also covered the exact titles/problem numbers, `C_gamma`, positive multilinear majorants, cardinality thresholds, later Talagrand threshold work, and later author/citing work for Burdzy--Scheutzow.

The search recovered current Talagrand-coauthored context:

- Ruben Ascoli, Xiaoyu He, Jinyoung Park, Michel Talagrand, *A reformulation of the discrete Convexity Conjecture via k-thresholds*, arXiv:2608.11183, submitted 2026-08-11.

That paper's advertised target is a k-threshold reformulation of the broader discrete convexity conjecture and graph-property cases. I found no source-authorized statement in the bounded search identifying it as a resolution of Talagrand's exact Definition-10.1 / Problem-10.9 positive-multilinear-majorant question.

For Burdzy--Scheutzow, the bounded search again recovered the original paper and citation trail but no accessible later primary paper explicitly claiming to settle exact Problem 7.2.

These are bounded negative searches, **not** proof of worldwide openness, novelty, or priority. The monotone-mixture mechanism in Sections 3--5 is elementary conditioning, so novelty is explicitly **UNVERIFIED**.

# 10. Admission and operational state

The newest NM13-12 admission screen after the last R15 report still labels F0111 PENDING / NOT READY and explicitly treats R15 as active retained screening rather than a free ownership release. It creates no F0111 claim and reports no new residue-11 successor. The newest coordinator status likewise says the controlling obstruction is admission inventory quality/lifecycle, not schedule count.

I therefore made no canonical claim, shared-root edit, peer-file edit, email/Drive action, public post, purchase, permission change, or scheduler change.

# 11. Model/scheduler control truth

The current exposed scheduled-task control surface still has task title/prompt, schedule or relative-start, timing mode, and enabled state. It has **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run applied-model/effort receipt, and no guaranteed-duration field**. Thus the text request `GPT-6 / maximum` is not a binding scheduler setting in this runtime.

The historical P26 `You cannot modify this task` event remains authorization-context-specific. Repository deployment history records that another authorized context later updated P26. The lawful workaround is the task-owning/otherwise authorized context or an authorized owner/admin/product/API/support surface; not duplication, a permission bypass, or a repository edit represented as a scheduler fix.

# 12. Route decision and next methods

The high-curvature two-gap route has now been compressed to a single-gap/k=2 coupling problem. The next genuinely different attacks should not derive another inequality in `delta/g`.

Next methods reserved:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** deform the single-gap coupled problem from arbitrary heterogeneous `k=2` base to the already-solved flat-support/homogeneous C1 sector and identify the first loss of positivity;
- **#10 DERANDOMIZE:** reinterpret the `k=2` kernel through a deterministic fractional cover/decision structure and search for a base-adaptive positive polynomial instead of another probabilistic upper bound;
- **#29 ADD THE POINTS AT INFINITY:** include zero and infinite coordinate hazards in the compactified base space, where the heterogeneous k=2 kernel reduces recursively, then determine whether an interior obstruction is forced.

```yaml
ledger_delta:
  track: R15
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "2/4 historical carried retirement value; no surviving frozen candidate"
  native_metric_after: "2/4 historical carried retirement value; no surviving frozen candidate"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: 6
  native_research_reopened: false
  free_admission_metric: E_READY_CLOSABLE
  free_admission_before: 0
  free_admission_after: 0
  retained_screen_source: "Talagrand, Are Many Small Sets Explicitly Small?, Definition 10.1 / Problem 10.9, F0111"
  retained_screen_status: "PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_movement: true
  retained_result: "ordered staircase hazard lies sharply between equal-gap sum_i Phi(u_i,g) and heterogeneous cardinality-two F_{r+1,2}(g,u); each higher gap acts monotonically and concavely; r=2 has exact read-once-to-majority interpolation"
  methods_tried: [4, 13, 27]
  next_methods: [6, 10, 29]
  remaining_obligation: "couple a heterogeneous k=2 positive polynomial to baseline F_{m,k} without coefficientwise expansion of G_{m,k}=F_{m,k-1}-F_{m,k}"
  checker: "none; analytic parameter-uniform proofs on page"
  audits: []
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_2153Z_successor_screen_f0111_twogap_peeling_u67r.md"
    - "proofnet24/NM13-12/runs/2026-09-18/2026-09-18T22-55-30Z__post-e0086-admission-delta-screen-9-f0111-peeling.md"
    - "Burdzy--Scheutzow arXiv:1302.6958v4, Definition 2.1 / Problem 7.2"
    - "Talagrand STOC 2010, Definition 10.1 / Problem 10.9"
    - "Ascoli--He--Park--Talagrand arXiv:2608.11183"
```
