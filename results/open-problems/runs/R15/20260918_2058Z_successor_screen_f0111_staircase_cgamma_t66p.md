Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; free admission `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111 the exact staircase microkernel from the preceding block factorization is proved to lie in `C_{1/r}` (more generally its level-`j` tail lies in `C_{1/(r-j+1)}`), the first non-read-once kernel `E_2` is therefore in `C_{1/2}`, and every zero-coordinate base of `E_2` actually has a `C_1` contact certificate. Methods #7 TAKE THE LIMIT, #8 DISCRETIZE, #26 HUNT THE SPORADIC CASE.**

# R15 retained screen — staircase `C_gamma` theorem and the first interior obstruction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source material or as a previously proved R15 lemma. I do not mark Burdzy–Scheutzow Problem 7.2, Talagrand Problem 10.9, or any larger source problem solved. Novelty is not claimed.

## 1. Continuity and exact source fidelity

Before doing new mathematics I reread or recovered the current campaign controls and exclusions:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest coordinator status `operations/task_health/runs/2026-09-18T205500Z/status.md`;
- controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- immediately preceding R15 report `runs/R15/20260918_1956Z_successor_screen_f0111_staircase_block_b65n.md`;
- the preceding coupled-Pascal theorem `runs/R15/20260918_1924Z_successor_screen_f0111_coupled_pascal_cgamma_s64x.md`;
- the preceding read-once compiler `runs/R15/20260918_1917Z_successor_screen_f0111_readonce_c1_s64w.md`;
- current repository searches for I0076/F0111 and nearby ownership.

The newest coordinator status still says that the reserve has listed candidates but no additional source-current, ownership-clear free READY CLOSABLE successor. The newly admitted CLOSABLE finite target is owned by another native slot. Therefore the bounded admission metric for R15 remains

`E_READY_CLOSABLE: 0 -> 0`.

I create no successor claim and do not promote a PENDING queue entry.

### Burdzy–Scheutzow Problem 7.2 remains retired from active attack

Primary source rechecked on 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

- FBM means there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion.
- BBM means the time reversal is an FBM.
- 2BM means there is one random time `S` for which the complete centered forward and backward half-paths are **independent standard Brownian motions**.
- Problem 7.2 assumes FBM + BBM and merely the existence of an arbitrary random time `T` at which those two complete centered half-paths are independent; it asks whether this forces 2BM.

There is no stopping-time assumption on `T`, and neither seam half is separately assumed Brownian. Problem 7.5 is different and remains excluded.

The six-run handoff is still controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but was eliminated because no source-valid independent real seam exists. The later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually 2BM by the excursion-Palm argument. Hence there is no surviving frozen counterexample candidate. The carried `2/4` is the historical retirement value of the positive-route metric, not a score on a live candidate. The unchanged count remains frozen at six after mandatory CLOSABLE rotation.

Fresh public queries dated 2026-09-18 for the exact title, Problem 7.2 wording, later Burdzy/Scheutzow material and citing pages again recovered the original paper/publication and no accessible later primary paper explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not an openness certificate.

## 2. Retained F0111 state and the exact staircase from the preceding run

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9. For an up-class `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

Talagrand's class `C_gamma` asks, at every base `q>=0`, for a positive multilinear polynomial `P` with no constant term such that

`F_A(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for all cardinality thresholds

`A_{n,k}={X subset[n]: |X|>=k}`.

The preceding R15 chain proved, SELF_CHECK_ONLY:

1. the two-variable endpoint kernel

`Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-(u+v)})`

has exact `C_1` contact at every base;
2. all monotone read-once classes are consequently in `C_1`;
3. the Pascal gaps

`G_{m,k}=F_{m,k-1}-F_{m,k}`

are ordered and satisfy

`G_{m,k}>=F_{m,k-1}/(m-k+2)`;                              (2.1)

4. every finite threshold obeys

`A_{n,k} in C_{1/(n-k+1)}`                                 (2.2)

at arbitrary heterogeneous bases;
5. splitting off `r` new coordinates gives the exact staircase factorization

`F_{m+r,k}(t,u)`
` =F_{m,k}(t)`
`  +F_{E_r}(u_1,...,u_r; G_{m,k},...,G_{m,k-r+1}),`         (2.3)

where, with independent latent Bernoulli variables `Z_d` and new-block indicators `X_i`,

`E_r={exists d<=r: Z_d=1 and M_X>=d}`,                     (2.4)

`M_X=sum_i X_i`.

The first non-read-once microkernel is

`E_2=[Z_1 and (X_1 or X_2)] or [Z_2 and X_1 and X_2]`.      (2.5)

The preceding run left (2.5) as the smallest exact block target. This run attacks that target rather than returning to the coarse block envelope that was already proved invalid.

## 3. The coupled closure lemma used below

I restate the exact form because it is the only compiler used in the new proof.

### Lemma 3.1 — coupled one-coordinate closure

Let `0<=H<=L` be nonnegative hazard functions of one block, put `g=L-H`, fix `0<gamma<=1`, and suppose `H` and `L` have `C_gamma` certificates at a prescribed base `q`. Define, with a fresh hazard coordinate `s`,

`K(t,s)=H(t)+Phi(s,L(t)-H(t)).`                             (3.1)

If

`g(q)>=gamma L(q)`,                                         (3.2)

then `K` has a `C_gamma` certificate at every prescribed new-coordinate base `s_0`.

### Proof

At the scalar base `(s_0,g(q))`, use the endpoint `C_1` theorem to choose `a,b,c>=0`, with `b<=1`, such that

`Phi(s,z)<=a s+b z+c s z`                                   (3.3)

for all `s,z>=0`, with equality at `(s_0,g(q))`.

If `P_H,P_L` are the two block certificates, set

`P_K=a s+bP_L+(1-b)P_H+c sP_L`.                            (3.4)

This is positive multilinear because `s` is fresh. Globally,

`K<=H+a s+b(L-H)+cs(L-H)`
` =a s+bL+(1-b)H+csL-csH`
` <=a s+bP_L+(1-b)P_H+csP_L=P_K`.                          (3.5)

At the base, the certificate budgets and exact scalar contact reduce the excess over `gamma K(q,s_0)` to

`gamma c s_0( gamma L(q)-g(q))<=0`                          (3.6)

by (3.2). QED.

No separate positive-polynomial certificate for the difference `L-H` is used.

## 4. Method #8 — DISCRETIZE: solve the four-variable `E_2` kernel exactly

The four-variable truth table can be compressed to the two states of `Z_1`; no grid or sampled inequality is needed.

Let the hazards of `(X_1,X_2,Z_1,Z_2)` be `(u,v,g,h)`. Put

`L(u,v)=F_{2,1}(u,v)=u+v`.                                 (4.1)

If `Z_1=0`, the event (2.5) reduces to

`Z_2 and X_1 and X_2`,

whose hazard is

`H(u,v,h)=Phi(h,Phi(u,v)).`                                 (4.2)

If `Z_1=1`, the second branch is redundant and (2.5) reduces to

`X_1 or X_2`,

whose hazard is exactly `L`. Consequently the elementary two-state conditioning identity is

`F_{E_2}(u,v,g,h)=H(u,v,h)+Phi(g,L(u,v)-H(u,v,h)).`          (4.3)

This is an exact equality.

Both `H` and `L` are monotone read-once hazards, hence are in `C_1` and therefore in `C_{1/2}`. It remains only to verify the coupled gap condition.

Since

`{Z_2 and X_1 and X_2} subset {X_1 and X_2}`,

monotonicity of event hazard gives

`H(u,v,h)<=Phi(u,v)`.                                       (4.4)

Also

`Phi(u,v)<=(u+v)/2`.                                        (4.5)

For completeness, (4.5) is equivalent to

`e^u+e^v-1>=e^{(u+v)/2}`,                                   (4.6)

and AM-GM gives `e^u+e^v>=2e^{(u+v)/2}`, while `e^{(u+v)/2}>=1`.

Therefore

`L-H>=L-Phi(u,v)>=L/2`.                                     (4.7)

Applying Lemma 3.1 with `gamma=1/2` to (4.3) proves:

### Theorem 4.1 — first staircase microkernel

`E_2 in C_{1/2}`                                            (4.8)

for **every heterogeneous base** `(u_0,v_0,g_0,h_0)>=0`.

This closes the exact abstract microkernel left open in the preceding run. It does **not** yet close the source threshold block substitution, because in (2.3) the latent hazards `g_d` are differences `G_{m,*}` rather than independent original coordinates. Substituting an arbitrary positive polynomial in the formal `g_d` would destroy the required positive-multilinear structure in the original variables.

## 5. Stronger theorem — every staircase tail has an explicit `C_gamma`

The same argument is not special to `r=2`.

For `1<=j<=r`, define the tail staircase

`E_{r,j}`
` ={exists d in {j,...,r}: Z_d=1 and M_X>=d}`,              (5.1)

and set `E_{r,r+1}=emptyset` with hazard zero. Thus `E_r=E_{r,1}`.

### Theorem 5.1 — staircase tail theorem

For every `1<=j<=r`,

`E_{r,j} in C_{1/(r-j+1)}`.                                (5.2)

In particular,

`E_r in C_{1/r}`.                                           (5.3)

### Proof

Proceed downward in `j`. Fix `j` and condition on the single coordinate `Z_j`.

If `Z_j=0`, the event is `E_{r,j+1}`; let its hazard be `H_j`.

If `Z_j=1`, then `E_{r,j+1}` is redundant whenever it occurs because it already implies `M_X>=j+1`, while the new `Z_j` branch needs only `M_X>=j`. Thus the event becomes the pure threshold `{M_X>=j}`; let

`L_j=F_{r,j}(u)`.                                           (5.4)

Exactly as in (4.3),

`F_{E_{r,j}}=H_j+Phi(z_j,L_j-H_j).`                         (5.5)

Moreover

`E_{r,j+1} subset {M_X>=j+1}`,

so

`H_j<=F_{r,j+1}`                                            (5.6)

and therefore

`L_j-H_j`
` >=F_{r,j}-F_{r,j+1}`
` =G_{r,j+1}`
` >=L_j/(r-j+1)`                                            (5.7)

by the previously proved Pascal gap fraction (2.1), with `m=r` and `k=j+1`.

Put

`gamma_j=1/(r-j+1)`.                                       (5.8)

The threshold theorem (2.2) gives

`L_j in C_{gamma_j}`.                                       (5.9)

For the downward induction, `E_{r,j+1}` lies in `C_{1/(r-j)}`. Since `gamma_j<=1/(r-j)`, monotonicity of the classes as `gamma` decreases implies

`H_j in C_{gamma_j}`.                                      (5.10)

For the base `j=r`, `H_r=0` and `L_r` is the all-elements endpoint, so the same statement holds directly.

Now (5.7) is exactly the gap condition of Lemma 3.1. Applying that lemma to (5.5) proves `E_{r,j} in C_{gamma_j}`. Descending to `j=1` gives (5.3). QED.

The theorem is conditional only on the already-written SELF_CHECK_ONLY R15 endpoint/coupled-Pascal chain; no new numerical assumption enters.

## 6. Method #7 — TAKE THE LIMIT: the `1/(r-j+1)` loss is sharp for this compiler

The staircase theorem gives a complete small theorem, but the limit identifies exactly what it cannot do.

Fix a level `j`. Send all later latent hazards

`z_{j+1},...,z_r -> infinity`.                              (6.1)

Then the later staircase `E_{r,j+1}` converges pointwise to the pure threshold `{M_X>=j+1}`. Consequently

`H_j -> F_{r,j+1}`                                          (6.2)

and the coupled gap in (5.5) converges to

`L_j-H_j -> G_{r,j+1}`.                                     (6.3)

Now take the homogeneous high-activity ray

`u_1=...=u_r=c`, `c->infinity`.                             (6.4)

The exact binomial tail asymptotics are

`F_{r,j}(c 1)`
` =(r-j+1)c-log binom(r,j-1)+o(1)`,                         (6.5)

`F_{r,j+1}(c 1)`
` =(r-j)c-log binom(r,j)+o(1)`.                             (6.6)

Hence

`G_{r,j+1}(c1)`
` =c+log((r-j+1)/j)+o(1)`,                                  (6.7)

and therefore

`(L_j-H_j)/L_j -> 1/(r-j+1)`.                              (6.8)

Thus the gap hypothesis used by Lemma 3.1 is asymptotically tight at every staircase level. In particular the `E_2` proof cannot improve `1/2` merely by sharpening (4.7): the limiting worst case is `h->infinity`, `u=v->infinity`.

There is also a useful Boolean interpretation of that limit. When `Z_2` is forced present, (2.5) contracts to

`(X_1 and X_2) or [Z_1 and (X_1 or X_2)]`,                  (6.9)

which is exactly the three-variable majority / cardinality threshold

`THR_{3,2}(X_1,X_2,Z_1)`.                                  (6.10)

So the first staircase kernel interpolates between read-once boundary regimes and the first interior cardinality threshold. This explains structurally why the same `1/2` constant appears in Theorem 4.1 and in the preceding heterogeneous theorem `A_{3,2} in C_{1/2}`.

This is a sharpness statement about the **present compiler**, not a proof that `E_2` or `THR_{3,2}` fails to belong to `C_gamma` for larger `gamma`.

## 7. Method #26 — HUNT THE SPORADIC CASE: all coordinate-boundary bases of `E_2` are actually `C_1`

The asymptotic limit above suggests searching for a sporadic obstruction. Before looking in the interior, all four coordinate faces can be eliminated exactly.

### Lemma 7.1 — zero-coordinate lift

Let `A` be any monotone up-class, and let `i` be one coordinate. Let `A_0` be the restriction with coordinate `i` forced absent. If `A_0` has a `C_1` contact certificate at a base `q` on the remaining coordinates, then `A` has a `C_1` contact certificate at the base `(q,0)`.

### Proof

Write `Q_0(t)` for the failure probability when `i` is absent and `Q_1(t)` when it is present. Monotonicity gives `Q_1<=Q_0`. At hazard `s` in coordinate `i`,

`Q_A(t,s)=e^{-s}Q_0(t)+(1-e^{-s})Q_1(t)>=e^{-s}Q_0(t)`.     (7.1)

Therefore

`F_A(t,s)<=s+F_{A_0}(t)`.                                   (7.2)

If `P_0` is a global positive multilinear `C_1` contact majorant for `A_0` at `q`, then

`P(t,s)=s+P_0(t)`                                           (7.3)

is a global positive multilinear majorant for `A`, and at `(q,0)` it contacts exactly:

`P(q,0)=F_{A_0}(q)=F_A(q,0)`. QED.

For `E_2`, every coordinate-deletion restriction is read-once:

- `Z_1=0`: `Z_2 and X_1 and X_2`;
- `Z_2=0`: `Z_1 and (X_1 or X_2)`;
- `X_1=0`: `Z_1 and X_2`;
- `X_2=0`: `Z_1 and X_1`.

The preceding read-once theorem places each restriction in `C_1`. Applying Lemma 7.1 yields:

### Corollary 7.2 — no boundary sporadic obstruction

At every base `(u_0,v_0,g_0,h_0)` for which at least one coordinate is zero, `E_2` admits a **global `C_1` contact certificate**.                 (7.4)

Therefore any failure of `E_2 in C_1`, if such a failure exists at all, must occur at a fully interior base

`u_0 v_0 g_0 h_0>0`.                                        (7.5)

This is stronger than the `C_{1/2}` theorem on the boundary and sharply narrows the next negative search. It is not evidence that an interior obstruction actually exists.

## 8. What moved and what remains

The preceding block report left `E_2` as the first explicit non-read-once obstruction. This run resolves that abstract obstruction at a quantitative constant:

`E_2 in C_{1/2}`.                                           (8.1)

More generally it resolves the entire staircase family at

`E_r in C_{1/r}`.                                           (8.2)

But this is **not yet a block proof of Talagrand Problem 10.9**. The exact source recursion (2.3) substitutes

`z_d = G_{m,k-d+1}(t)`                                      (8.3)

into the abstract staircase. These `z_d` are differences of two threshold hazards. A positive polynomial in formal staircase variables may contain monomials in the `z_d`; substituting (8.3) creates alternating terms and is not an admissible positive multilinear polynomial in the original hazard coordinates.

So the remaining block problem is now more precise:

> Lift the **coupled proof** of Theorem 5.1 through the substitutions (8.3), preserving its cancellations until the original threshold certificates are inserted, rather than substituting the final staircase polynomial.

The direct scalar coupled lemma does exactly this for one gap. A successful multi-gap analogue would have to keep two or more adjacent differences coupled simultaneously. Merely certifying `E_r` as an abstract class, even at a better constant, is not enough.

For `r=2`, the fully explicit next target is to build a two-gap coupled closure for

`F_{m+2,k}`
` =F_{m,k}`
`  +F_{E_2}(u,v; G_{m,k},G_{m,k-1})`                        (8.4)

without ever majorizing either `G_{m,k}` or `G_{m,k-1}` independently.

## 9. Prior-art and current-status pass

Fresh 2026-09-18 public queries covered:

- exact Burdzy–Scheutzow title + Problem 7.2 + random-time independent halves, later author material and citing pages;
- Talagrand exact title + Problem 10.9 + `C_gamma` + cardinality threshold;
- later related threshold work including DeMarco–Kahn, Frankston–Kahn–Park, Gunby–He–Narayanan, Park–Pham and Warnke;
- exact/nearby searches for the staircase Boolean class, Pascal-gap hazard factorization and the constants `1/r` / `1/(r-j+1)`.

The searches recovered Talagrand's STOC source and later papers on expectation/fractional/down-set threshold formulations, but no accessible source explicitly stating the staircase theorem above or resolving exact Definition-10.1/Problem-10.9 in this positive-multilinear-majorant formulation. For Burdzy–Scheutzow they recovered the original publication/source and no accessible later primary source explicitly claiming to settle exact Problem 7.2.

These are bounded negative searches. The staircase conditioning argument is elementary enough that it may be folklore in reliability/Poisson-binomial language. **Novelty remains UNVERIFIED.**

## 10. Validation discipline

No finite-search theorem is claimed. The discrete `Z_j=0/1` split in Sections 4–5 is an exact symbolic conditioning proof, not an enumeration result, so I did not manufacture a checker. No numerical path samples, Brownian simulations, or sampled inequality grids are counted as evidence.

The new theorems inherit the SELF_CHECK_ONLY status of the preceding endpoint-`C_1`, gap-order and coupled-Pascal chain. Before any promotion they require:

1. a P26 independent full-proof audit;
2. a second genuinely independent OTHER-track audit;
3. a dedicated prior-art/citation-graph audit;
4. only then a source-scoped paper package if the result is judged new and useful.

Full Talagrand Problem 10.9 remains open-looking/PARTIAL in this repository because no dimension-free positive constant has been proved. Burdzy–Scheutzow Problem 7.2 remains OPEN/PARTIAL/RETIRED-HANDOFF.

## 11. Methods outcome and next route

### #7 TAKE THE LIMIT

Succeeded. The later-latent/high-activity limit proves that the stage constant `1/(r-j+1)` is sharp for the present coupled-gap compiler and identifies `THR_{3,2}` as the limiting `E_2` core.

### #8 DISCRETIZE

Succeeded. Conditioning on the single bit `Z_1` reduces the first four-variable non-read-once staircase to the exact two-hazard recursion (4.3), which yields `E_2 in C_{1/2}` with a complete analytic proof.

### #26 HUNT THE SPORADIC CASE

Succeeded as a reduction, not as a counterexample. Every coordinate-boundary base of `E_2` is `C_1`; hence any `C_1` obstruction must be fully interior. No sporadic counterexample is claimed.

The next pass should attack the substitution problem itself rather than improve the abstract staircase theorem. Fresh useful choices are:

- #11 DUALIZE — derive a dual characterization of a two-gap coupled certificate before expanding either gap;
- #15 BREAK THE SYMMETRY ON PURPOSE — freeze a strongly heterogeneous old base so the two adjacent gaps separate and see which cancellation survives;
- #20 FIND WHY THE ALGORITHM FAILS — identify the exact sign pattern produced when the `E_2` contact polynomial is naively substituted, then design a coupled replacement that cancels those terms before positivity is imposed.

## 12. Model / scheduler / denied-task boundary

The exposed task-management surface still provides task identity/title/prompt, scheduling/timing and enabled-state controls, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run model/effort receipt, and no guaranteed-duration field**. GPT-6 / maximum therefore remains prompt text only here; actual reasoning level is UNVERIFIED.

The historical P26 response `You cannot modify this task` was authorization-context-specific. Repository continuity records that a later authorized P/C context successfully updated P26. The lawful workaround is the owning/authorized task context or an owner/admin/product/backend/support surface exposing the desired controls — not duplication, permission bypass, or representing a repository edit as scheduler repair.

No scheduler, permission, email, Drive, public-posting, purchase or external-side-effect action was taken in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  native_source:
    id: I0076
    source: Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2
    metric: four source-matching obligations on one frozen counterexample candidate
    before: 2/4  # historical carried retirement value, not a live candidate score
    after: 2/4
    status: OPEN / PARTIAL / RETIRED-HANDOFF
    surviving_frozen_candidate: NONE
    unchanged_count: 6
    remaining_obligation: common-re-rooting relative-phase/cocycle obstruction from six-run handoff
    evidence:
      - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
    audits: []
  free_admission:
    metric: E_READY_CLOSABLE
    before: 0
    after: 0
    note: newest coordinator status has no additional free source-current ownership-clear READY CLOSABLE successor for R15
  retained_screen:
    id: F0111
    source: Talagrand, Are Many Small Sets Explicitly Small?, Definition 10.1 / Problem 10.9
    parent_status: PARTIAL / NOT CLAIMED
    before: exact block staircase factorization; E_2 first unresolved non-read-once microkernel; A_{n,k} in C_{1/(n-k+1)} SELF_CHECK_ONLY
    after:
      - E_2 in C_{1/2} at arbitrary heterogeneous bases
      - E_{r,j} in C_{1/(r-j+1)} and E_r in C_{1/r}
      - compiler constant asymptotically sharp at every staircase stage
      - all zero-coordinate E_2 bases have global C_1 contact certificates
      - remaining obstruction is positive-multilinear lifting through adjacent-gap substitutions, not the abstract staircase class itself
    status: SELF_CHECK_ONLY / NOVELTY_UNVERIFIED
    audits: []
  tried_moves: [7, 8, 26]
  next_moves: [11, 15, 20]
  checker_created: false
  checker_reason: no finite-enumeration theorem; parameter-uniform analytic proofs are written on the page
  scheduler_model_binding: UNAVAILABLE_ON_EXPOSED_SURFACE
  requested_model: GPT-6 maximum
  actual_model_reported: GPT-5.6 Sol
  reasoning_effort: UNVERIFIED
```
