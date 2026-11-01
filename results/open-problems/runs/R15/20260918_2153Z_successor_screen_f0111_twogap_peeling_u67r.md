Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; current free-admission state remains `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111 an exact exponential-tilt / common-gap peeling identity reduces the two-coordinate staircase obstruction from two ordered gaps to one common gap plus the nonnegative adjacent-gap curvature `delta=G_{m,k-1}-G_{m,k}`; a natural coefficientwise nested-certificate lift is proved impossible already in the two-variable endpoint pair. Methods #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS.**

# R15 retained screen — exact common-gap peeling and the two-gap curvature obstruction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematics below is **SELF_CHECK_ONLY**. The identities and inequalities are proved on the page, but there is no independent fleet audit and no novelty certificate. I do **not** mark Burdzy–Scheutzow Problem 7.2, Talagrand Problem 10.9, or any larger source problem closed.

## 1. Continuity, repository controls, and exact I0076 source scope

Before doing new mathematics I reread/recovered the current campaign and fleet controls rather than restarting from the scheduler title:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- current coordinator status `operations/task_health/runs/2026-09-18T215400Z/status.md`;
- controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- immediately preceding own report `runs/R15/20260918_2058Z_successor_screen_f0111_staircase_cgamma_t66p.md`;
- the preceding staircase/block/coupled-Pascal reports used below;
- current repository searches for I0076, F0111, ownership, and newly admitted CLOSABLE targets.

The newest coordinator status still reports that no additional source-current, ownership-clear free CLOSABLE successor crossed admission. The root queue likewise distinguishes listed/PENDING candidates from READY candidates. Therefore the bounded admission metric remains

`E_READY_CLOSABLE: 0 -> 0`.

I create no successor claim and do not promote any PENDING item.

### Exact Burdzy--Scheutzow statement remains unchanged

Primary source rechecked directly on 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

- FBM: there are random times `S_n -> -infinity` a.s. from each of which the complete centered future is standard Brownian motion.
- BBM: time reversal is an FBM.
- 2BM: there is one random time `S` for which the complete centered future and past are **independent standard Brownian motions**.
- Problem 7.2 assumes FBM + BBM and only the existence of an arbitrary random time `T` for which the two complete centered half-paths are independent, and asks whether this forces 2BM.

The source imposes **no stopping-time condition on `T`** and does **not** separately assume Brownianity of either seam half. Problem 7.5 is distinct and remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 non-2BM candidate was eliminated because it does not supply a source-valid independent real seam. The later Brownian-prefix/BES candidate supplies the seam but was proved actually 2BM by the excursion/Palm argument. There is therefore no surviving frozen counterexample candidate. The carried `2/4` is a historical retirement value, not a score on a live construction; its unchanged count stays frozen at six after mandatory CLOSABLE rotation.

Fresh public searches dated 2026-09-18 for the exact title, exact `Problem 7.2` wording, later Burdzy/Scheutzow material and citing papers again recovered the original publication and citation trail but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

## 2. Retained F0111 state

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9. For an up-class `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

Talagrand's `C_gamma` requires, at every base `q>=0`, a positive multilinear polynomial with zero constant term which globally majorizes `F_A` and satisfies the scaled budget at `gamma q`. Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold

`A_{n,k}={X subset[n]: |X|>=k}`.

The preceding R15 chain is SELF_CHECK_ONLY and includes:

- exact `C_1` contact for the two-variable endpoint kernel
  `Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-(u+v)})`;
- a `C_1` compiler for monotone read-once classes;
- ordered Pascal gaps
  `G_{m,j}=F_{m,j-1}-F_{m,j}`;
- the finite-dimensional bound `A_{n,k} in C_{1/(n-k+1)}`;
- the exact block factorization
  `F_{m+r,k}=F_{m,k}+F_{E_r}`
  through the staircase event
  `E_r={exists d<=r: Z_d=1 and M_X>=d}`;
- the staircase theorem `E_{r,j} in C_{1/(r-j+1)}`.

The preceding run showed that the scalar gap bound is asymptotically sharp for that compiler. This run therefore does not try to improve the same inequality. It changes representation.

## 3. Method #11 — DUALIZE: exponential tilt of the failure measure

The useful object is the **failure probability**, not the hazard itself.

Let `X_1,...,X_r` be independent Bernoulli coordinates with hazards `u_1,...,u_r`, i.e.

`P(X_i=1)=1-e^{-u_i}`,

and put `M=sum_i X_i`. Let independent latent coordinates `Z_d`, `1<=d<=r`, have hazards `z_d`. Recall

`E_r={exists d<=r: Z_d=1 and M>=d}`.

Conditional on `M=s`, the staircase fails exactly when `Z_1,...,Z_s` all fail. Hence

`exp(-F_{E_r}(u;z))
 = E_u exp(-sum_{d=1}^M z_d)`.                              (3.1)

This elementary identity exposes an exact Esscher/exponential tilt.

For `g>=0` define

`T_g(u)=log(1+(e^u-1)e^{-g})`.                              (3.2)

Also

`C_g(u)=e^{-u}+(1-e^{-u})e^{-g}`.                           (3.3)

The endpoint kernel satisfies

`C_g(u)=exp(-Phi(u,g))`,                                    (3.4)

and direct algebra gives

`T_g(u)=u-Phi(u,g)`.                                        (3.5)

If the Bernoulli law of `X_i` is tilted by the factor `e^{-g X_i}`, its normalizing constant is `C_g(u_i)`, and after normalization it is again Bernoulli, now with hazard `T_g(u_i)`. Thus the product Bernoulli family is exactly closed under the tilt.

The transform has the semigroup law

`e^{T_g(u)}-1=e^{-g}(e^u-1)`,                               (3.6)

hence

`T_{g+h}=T_h o T_g`.                                        (3.7)

This odds-contraction semigroup is the conserved structure produced by the change of measure.

## 4. Exact common-gap peeling theorem

The source staircase gaps are ordered. The following theorem uses only that ordering and (3.1).

### Theorem R15-F0111-PEEL

Assume

`0<=z_1<=z_2<=...<=z_r`.

Let `E_{r,2}` denote the tail staircase using thresholds `d=2,...,r`. Then

`F_{E_r}(u_1,...,u_r; z_1,...,z_r)`
` = sum_{i=1}^r Phi(u_i,z_1)`
`   + F_{E_{r,2}}(`
`       T_{z_1}(u_1),...,T_{z_1}(u_r);`
`       z_2-z_1,...,z_r-z_1).`                              (4.1)

Thus the entire common part of all ordered latent hazards can be removed exactly. The residual staircase sees only the **spread of the gaps above the smallest gap**.

### Proof

Set `g=z_1`. For a realization with `M=s`,

`sum_{d=1}^s z_d
 = g s + sum_{d=2}^s (z_d-g)`.                              (4.2)

Insert (4.2) into (3.1). The factor `e^{-gM}` tilts the independent `X_i` coordinates. Its product normalizing constant is

`prod_i C_g(u_i)
 = exp(-sum_i Phi(u_i,g))`.                                 (4.3)

Under the normalized tilted law the `X_i` remain independent and have hazards `T_g(u_i)`. The remaining conditional factor is

`exp(-sum_{d=2}^M (z_d-g))`,                                (4.4)

which is exactly the failure probability of the tail staircase `E_{r,2}` with latent hazards `z_d-g`. All of these hazards are nonnegative by the ordering assumption. Taking `-log` proves (4.1). QED.

This is an exact distributional identity, not a sampled or asymptotic statement.

## 5. Method #15 — BREAK THE SYMMETRY: the two-gap obstruction is curvature, not scale

Apply Theorem PEEL to the first genuinely non-read-once block, `r=2`. Write

`g=z_1`,
`delta=z_2-z_1>=0`.

The tail event `E_{2,2}` is simply the intersection of its residual latent bit with both tilted `X` bits. Therefore

`boxed:`

`F_{E_2}(u,v;g,g+delta)`
` = Phi(u,g)+Phi(v,g)`
`   + Phi(delta, Phi(T_g(u),T_g(v))).`                       (5.1)

For the actual threshold block substitution,

`g=G_{m,k}`,                                                (5.2)

`delta=G_{m,k-1}-G_{m,k}`                                  (5.3)

and hence

`delta
 = F_{m,k-2}-2F_{m,k-1}+F_{m,k}`.                        (5.4)

So the new residual is precisely the nonnegative adjacent **gap curvature** / second difference. Formula (5.1) yields the exact source-level decomposition

`F_{m+2,k}(t,u,v)`
` =F_{m,k}(t)`
`  +Phi(u,G_{m,k}(t))+Phi(v,G_{m,k}(t))`
`  +Phi(`
`      G_{m,k-1}(t)-G_{m,k}(t),`
`      Phi(T_{G_{m,k}(t)}(u),T_{G_{m,k}(t)}(v))`
`    ).`                                                    (5.5)

This is stronger information than the previous generic staircase representation: the large **common** part of the two old gaps is completely peeled away. Only their difference remains in the non-read-once correction.

Two checks are immediate and exact.

1. **Equal-gap face.** If `G_{m,k-1}=G_{m,k}`, then the last term vanishes and the two-coordinate block decouples exactly:

   `F_{m+2,k}=F_{m,k}+Phi(u,g)+Phi(v,g)`.                    (5.6)

2. **Odds contraction.** Large common `g` does not make the residual `X` variables larger; by (3.6), it multiplies every tilted success odds by `e^{-g}`. Thus high common activity is damped before the curvature term is evaluated.

### A quantitative curvature bound

Define

`p_u^g=1-e^{-T_g(u)}`,
`p_v^g=1-e^{-T_g(v)}`.                                     (5.7)

For fixed `B>=0`, the map `x -> Phi(x,B)` has derivative

`d/dx Phi(x,B)
 =(1-e^{-B})/[1+(e^x-1)e^{-B}]`,                            (5.8)

which decreases from `1-e^{-B}`. Hence

`Phi(delta,B)<=delta(1-e^{-B})`.                            (5.9)

For

`B=Phi(T_g(u),T_g(v))`,

the event interpretation gives

`1-e^{-B}=p_u^g p_v^g`.                                    (5.10)

On the other hand

`partial_g Phi(u,g)=p_u^g`,                                 (5.11)

and this derivative decreases in `g`, so

`Phi(u,g)=int_0^g p_u^s ds >= g p_u^g`.                    (5.12)

The same holds for `v`. Since `p_u^g p_v^g <= (p_u^g+p_v^g)/2`, for `g>0` the curvature remainder `R` in (5.1) obeys

`0<=R`
` <= delta p_u^g p_v^g`
` <= (delta/(2g)) [Phi(u,g)+Phi(v,g)].`                      (5.13)

Consequently

`F_{E_2}(u,v;g,g+delta)`
` <= (1+delta/(2g))[Phi(u,g)+Phi(v,g)]`.                    (5.14)

This does **not** prove a universal `C_gamma`: the ratio `delta/g` can be arbitrarily large on heterogeneous old bases. It does, however, cleanly separate a low-curvature regime from the genuinely hard high-curvature regime.

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS: nested exact-contact certificates cannot carry the gaps

A tempting way to substitute the source differences

`G_{m,k}=F_{m,k-1}-F_{m,k}`

into positive polynomials is to seek exact-contact certificates nested coefficientwise, so that the difference of consecutive certificates is again positive. This fails already for the smallest endpoint pair.

Let

`L(u,v)=u+v`,
`H(u,v)=Phi(u,v)`.

Fix an interior base `(u_0,v_0)>0`.

### Proposition R15-F0111-NEST-NOGO

There do not exist positive multilinear global majorants `P_L,P_H` with exact contact at `(u_0,v_0)` such that `P_L-P_H` has nonnegative coefficients.

### Proof

Any positive multilinear polynomial in two variables has the form

`a u+b v+cuv`, `a,b,c>=0`.

First consider a global majorant of `L` with exact contact. Restricting to the axes forces `a>=1`, `b>=1`. At the positive base,

`a u_0+b v_0+c u_0v_0=u_0+v_0`.

All terms are nonnegative, so necessarily

`a=b=1`, `c=0`.

Thus

`P_L=L`.                                                    (6.1)

Now let

`P_H=a u+b v+cuv`

be a positive global majorant of `H` with exact interior contact. I claim `c>0`. If `c=0`, put `m=min(u_0,v_0)`. Since the intersection event is strictly smaller than either factor event at a positive finite base,

`H(u_0,v_0)<m`.                                             (6.2)

Contact would imply

`(a+b)m <= a u_0+b v_0=H(u_0,v_0)<m`,

so `a+b<1`. But along the diagonal,

`H(R,R)=R-log(2-e^{-R})`,                                   (6.3)

and global majorization by `aR+bR` requires, after dividing by `R` and sending `R->infinity`,

`a+b>=1`,

a contradiction. Hence `c>0`.

By (6.1), the coefficient of `uv` in `P_L-P_H` is `-c<0`. Therefore the difference cannot be a positive polynomial. QED.

This is a route-level impossibility theorem, not a negative answer to Problem 10.9. It says that one cannot lift the exact `C_1` compiler simply by demanding coefficientwise nested contact polynomials for consecutive thresholds. The cancellations in the differences have to be preserved until later in the construction.

### Another tempting shortcut that does not automatically work

I also tested the idea of forcing a staircase latent coordinate to be present by sending its hazard to infinity and then claiming closure of `C_gamma` under this restriction. At the hazard level the restriction limit is valid. At the **certificate** level, however, substituting an infinite/large forced coordinate into a zero-constant multilinear polynomial creates a positive constant term from monomials containing only that coordinate. Talagrand's Definition 10.1 explicitly forbids a constant term. Without a separate renormalization lemma, this limit therefore does not furnish a valid `C_gamma` certificate. I do not count this as a theorem or use it to claim equivalence with Problem 10.9.

## 7. What this changes and what remains

The preceding block program treated the staircase as a four-variable (then `2r`-variable) microkernel. The new identity says that, for the source-ordered gaps, the first two-gap obstruction has a much sharper state description:

- the common gap `g=G_{m,k}` is handled by an exact product exponential tilt;
- all new-coordinate odds are contracted by the semigroup `T_g`;
- the genuinely non-read-once residual depends on the old block through the single curvature
  `delta=G_{m,k-1}-G_{m,k}`.

So the next proof should not attack an arbitrary four-variable `E_2` again. It should attack the **high-curvature regime** of (5.5), where `delta/g` is large, while using (5.13) in the complementary low-curvature regime. In old-count language, high curvature means the consecutive lower-tail ratios are very different; that should be translated into a structural imbalance of the `k-2` and `k-1` layers and then coupled to the three consecutive threshold certificates `F_{m,k},F_{m,k-1},F_{m,k-2}` without coefficientwise subtraction.

No source-level metric moves in this run. Talagrand Problem 10.9 remains `PARTIAL / NOT CLAIMED`; the new exact identities are retained-screen mathematics only.

## 8. Prior-art/current-literature pass

Dated public queries on 2026-09-18 covered:

- exact title `Are Many Small Sets Explicitly Small?`, `Problem 10.9`, `C_gamma`, cardinality thresholds;
- later papers explicitly titled *Note on a problem of M. Talagrand*, *On a problem of M. Talagrand*, and later down-set/threshold work;
- exact-title and Problem-7.2 searches for *Forward Brownian Motion* plus later author/citation material.

The search recovered Talagrand's 2010 source, DeMarco--Kahn (2015), Frankston--Kahn--Park (2022), Gunby--He--Narayanan (2023), Warnke (2024), and the Burdzy--Scheutzow source/citation trail. I found no accessible source explicitly stating the common-gap peeling identity (4.1)/(5.1), the nested-certificate no-go above, or a resolution of exact Definition-10.1 Problem 10.9; and no accessible later primary paper explicitly claiming to settle Burdzy--Scheutzow Problem 7.2. These are **bounded negative searches only**. The change-of-measure mechanism is elementary exponential tilting/Esscher tilting and should be treated as folklore machinery; **novelty is UNVERIFIED**.

## 9. Scheduler/model-control truth

The exposed task-control surface still offers task identity/title/prompt, schedule or relative-start fields, timing mode, and enabled state. It still exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed-duration field**. Thus `GPT-6 / maximum` remains prompt text only in this environment.

The historical P26 `You cannot modify this task` response was authorization-context-specific. Repository deployment records show that another authorized P/C context later updated P26 successfully. The legitimate remedy for model control is an owner/admin/product/API scheduler surface that persists model-family and reasoning-effort fields into routing and returns trustworthy run attestation. It is not task duplication or a permission bypass. No scheduler change is attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2 / I0076"
  source_target: "FBM + BBM + source-exact independence of centered half-processes at an arbitrary random time T => 2BM?"
  fixed_metric: "number of the four source obligations proved for one frozen counterexample candidate"
  source_metric_before: "historical carried 2/4; no surviving frozen candidate"
  source_metric_after: "historical carried 2/4; no surviving frozen candidate"
  source_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  source_unchanged_count: 6
  source_unchanged_count_policy: "frozen after mandatory six-run CLOSABLE rotation; not incremented"
  admission_metric: "E_READY_CLOSABLE: 0 -> 0"
  tried_moves: [11, 15, 20]
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small? (STOC 2010), Definition 10.1 / Problem 10.9, F0111"
    status: "PARTIAL / NOT CLAIMED / SELF_CHECK_ONLY"
    movement:
      - "exact common-gap exponential-tilt peeling identity for ordered staircase hazards"
      - "exact two-gap decomposition with residual curvature delta=G_{m,k-1}-G_{m,k}"
      - "quantitative curvature bound R <= delta/(2g) [Phi(u,g)+Phi(v,g)] for g>0"
      - "coefficientwise nested exact-contact certificate lift ruled out already for L=u+v versus H=Phi(u,v)"
  remaining_obligation: "Use the exact two-gap decomposition to handle the high-curvature regime without coefficientwise subtraction; no active I0076 obligation is resumed unless lawfully reassigned after handoff."
  evidence:
    - "full analytic proofs in this immutable report"
    - "primary Burdzy-Scheutzow PDF rechecked at Definition 2.1 / Problem 7.2"
    - "primary Talagrand PDF rechecked at Definition 10.1 / Problem 10.9"
    - "current coordinator status and root reserve reread"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY; no independent P26/OTHER audit requested or counted"
  novelty: "UNVERIFIED"
```

No checker is created: every new claim is an analytic parameter-uniform identity/inequality with its proof on the page, not a finite census. The next genuinely different methods should be **#4 PROVE SOMETHING WEAKER COMPLETELY, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS**, applied to the high-curvature regime isolated in (5.5).