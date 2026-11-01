Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the fixed four-obligation metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the exact equal-subset face cone extends to **every nonnegative ray**, and any exact interior quadratic contact is automatically globally safe on its own radial ray. Methods #18 SAY IT IN ANOTHER LANGUAGE, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS.**

# R15 retained screen — exact cone on every nonnegative ray and radial saturation

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below about Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED / PENDING / NOT READY**. It does not reopen I0076, claim F0111, establish novelty, solve Talagrand Problem 10.9, or satisfy the fleet's two-independent-audit closure rule.

## 1. Continuity, source fidelity, ownership and exclusions

I continued from the newest own immutable report

`runs/R15/20260919_1913Z_successor_screen_f0111_exact_face_cone_d89w.md`

at commit `09e2e7d0051a29d9fbe517ebf925597c5c0ab883`, rather than restarting.

Before new mathematics I read/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling I0076 handoff, the newest R15 report, current neighboring/successor-gate evidence, the current coordinator status, the newest material R14/R17 transitions, and the current new-methods deployment manifest. I also queried the intake/repository for I0076 and its prior attempts rather than treating a missing bulk rendering of the large JSONL corpus as a reset.

The current coordinator status still records no newly certified **free** READY+CLOSABLE successor for the targetless gates. A subsequently visible CLOSABLE admission, Shpectorov--Zhao `srg(69,20,7,5)`, was created together with an exclusive owner assignment to native slot `6aa7b46f70a8819184095c277974c256`; it is therefore not free R15 inventory. The current NM13-12 screen independently classifies F0111 as `PENDING / SELF_CHECK_ONLY / NOT READY` with no canonical F0111 claim. I therefore neither stole a claimed source nor promoted a PENDING item to READY.

### I0076 source rechecked exactly

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. for which every centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM iff time reversal is FBM;
- `X` is 2BM iff there exists one random time `S` for which the complete centered future and past are independent **standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` for which

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as complete half-processes forces 2BM. The source does **not** require `T` to be a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is a different question and remains excluded.

The controlling six-run I0076 handoff remains unchanged. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but fails the exact independent-seam obligation. The later Brownian-prefix/BES independent-seam candidate was proved actually 2BM. Hence there is no surviving frozen counterexample candidate on which the user's four obligations can honestly be rescored; the historical positive-route `2/4` is only the retired handoff value.

Dated public searches on 2026-09-19 for the exact title, exact Problem 7.2 wording, the authors, later work and citations recovered the original paper/current publication page and related Brownian path-splitting work, but no accessible later primary source explicitly claiming to resolve exact Problem 7.2. This is bounded negative evidence, not a worldwide openness certificate.

### Retained F0111 current-literature check

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Problem 10.9, specialized to the `k=2` cardinality-threshold hazard used in preceding R15 reports.

Dated 2026-09-19 searches for the exact source title, `k=2`, quadratic/polynomial majorants, the discrete Convexity Conjecture, and the specific log-sum-exp ray form recovered the original Talagrand source, older threshold literature, Ascoli--He--Park--Talagrand arXiv:2608.11183 (2026-08-11), and Park arXiv:2609.14681 (2026-09-13). The August paper reformulates the broader discrete Convexity Conjecture via `k`-thresholds and proves substantial classes; Park gives a dimension-free bound explicitly described as progress toward the conjecture. I found no accessible primary source stating the all-ray theorem below. Because the mechanism is elementary convex/moment calculus, novelty is **UNVERIFIED** and should not be advertised without a dedicated literature review.

### Section-B methods

The preceding run used #11/#24/#29. Earlier retained F0111 history has already used all 30 method numbers at least once, so a globally unused triple is impossible without falsifying history. This run uses a nonconsecutive triple in new roles:

- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite arbitrary-ray curvature as one dimensionless moment functional `K(z)`;
- **#20 FIND WHY THE ALGORITHM FAILS:** prove that testing the radial ray through an exact contact is guaranteed to pass, so radial failure hunting is structurally useless;
- **#27 SWAP THE QUANTIFIERS:** replace the finite family of equal-coordinate subset rays by one theorem valid for **every** nonnegative direction.

The idea was written before the symbolic checker in

`artifacts/R15/f0111_allray_idea_e90x.md`

at creation commit `c2b2b2f4af804173b8c9e66c600e3e857e05c3a4`.

---

## 2. Setup from the preceding exact-face theorem

For the `k=2` threshold hazard,

`F_n(t)=sum_i t_i-log(sum_i exp(t_i)-(n-1)).`                 (2.1)

A nonnegative quadratic candidate is

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,              (2.2)

with `A_i,B_ij>=0`.

The preceding run solved the exact majorant cone only on equal-coordinate rays `t=s 1_J`. The new question is whether there is an exact one-variable cone on an **arbitrary** nonnegative ray.

Let `c=(c_1,...,c_n)>=0`. Zero coordinates can be discarded, because for `m=|supp(c)|`

`F_n(s c)=s sum_{i in supp(c)}c_i`
`          -log(sum_{i in supp(c)}exp(s c_i)-(m-1)).`        (2.3)

Hence assume from now on that `m>=2` and every active `c_i>0`. Set

`f_c(s)=F_m(s c)`,
`g_c(s)=f_c(s)/s`,                                           (2.4)

for `s>0`.

The central new theorem is that `g_c` is **strictly concave for every such c**.

---

## 3. Method #18 — a dimensionless moment functional controls every ray

Write

`L_c(s)=log(sum_i exp(s c_i)-(m-1)).`                        (3.1)

Then

`g_c(s)=sum_i c_i-L_c(s)/s`.                                (3.2)

Thus strict concavity of `g_c` is equivalent to strict convexity of `L_c(s)/s`.

Put

`z_i=s c_i`,
`T(z)=sum_i exp(z_i)-(m-1)`,
`r_i=exp(z_i)/T(z)`,                                         (3.3)

and define

`M_1=sum_i r_i z_i`,
`M_2=sum_i r_i z_i^2`,                                       (3.4)

`K_m(z)=2 log T-2M_1+M_2-M_1^2`.                            (3.5)

Since

`s L_c'(s)=M_1`,
`s^2 L_c''(s)=M_2-M_1^2`,                                   (3.6)

direct differentiation gives

`boxed:  d^2/ds^2 [L_c(s)/s] = K_m(s c)/s^3.`               (3.7)

So it remains to prove `K_m(z)>0` for all `m>=2` and all `z_i>0`.

### Theorem R15-F0111-ALLRAY1 — strict positivity of K

For every `m>=2` and `z in (0,infinity)^m`,

`boxed: K_m(z)>0.`                                           (3.8)

#### Proof

We prove nonnegativity by induction on `m` and then exclude an interior zero.

**Boundary reduction.** For `m=1`, `T=e^{z_1}`, `r_1=1`, and `K_1=0`. If, for some `m>=2`, one coordinate tends to zero, say `z_m=0`, then

`T_m(z_1,...,z_{m-1},0)`
`=sum_{i<m}e^{z_i}+1-(m-1)`
`=sum_{i<m}e^{z_i}-(m-2)=T_{m-1}`.                           (3.9)

The zero coordinate contributes nothing to `M_1,M_2`; hence

`K_m(z_1,...,z_{m-1},0)=K_{m-1}(z_1,...,z_{m-1}).`           (3.10)

Thus every finite boundary face has nonnegative `K` by induction.

**The boundary at infinity.** Let

`E=sum_i e^{z_i}`,
`epsilon=(m-1)/E`,
`p_i=e^{z_i}/E`,
`R=1/(1-epsilon)`.                                           (3.11)

Then `p` is an honest probability vector, whereas `r_i=R p_i`. Put

`mu=sum_i p_i z_i`,
`V=sum_i p_i(z_i-mu)^2`,
`H=-sum_i p_i log p_i`.                                      (3.12)

Because `log E=mu+H`, substitution into (3.5) gives the exact decomposition

`K_m`
`= R V +2H+2log(1-epsilon)`
`  -2(R-1)mu-R(R-1)mu^2.`                                   (3.13)

If `M=max_i z_i -> infinity`, then `E>=e^M`, so

`0<=epsilon<=(m-1)e^{-M}`, `0<=mu<=M`.                      (3.14)

Consequently all three correction terms involving `epsilon` tend to zero, while `R V>=0` and `H>=0`. Therefore every escaping sequence satisfies

`liminf K_m >=0`.                                            (3.15)

This is the useful entropy/variance invariant hidden by the original coordinates.

**No negative interior minimum.** Suppose, toward a contradiction, that `K_m<0` somewhere. By (3.10), the induction hypothesis, and (3.15), a negative sublevel set is compactly contained in the positive orthant. Hence `K_m` attains a negative global minimum at an interior point.

Differentiate. The elementary identities

`partial_i M_1 = r_i(z_i+1-M_1)`,
`partial_i M_2 = r_i(z_i^2+2z_i-M_2)`                        (3.16)

give

`partial_i K_m = r_i Q(z_i)`,                               (3.17)

where the **same quadratic** appears for every coordinate:

`Q(x)=x^2-2M_1 x+2M_1^2-M_2.`                              (3.18)

At an interior critical point `r_i>0`, so `Q(z_i)=0` for every `i`. Therefore the coordinates take at most two distinct values.

If all coordinates equal `a>0`, let

`R_0=sum_i r_i = m e^a/[m e^a-(m-1)]>1.`                    (3.19)

Then `M_1=R_0 a`, `M_2=R_0 a^2`, and

`Q(a)=a^2(R_0-1)(2R_0-1)>0`,                               (3.20)

contradicting criticality.

If the coordinates take exactly two distinct values `a!=b`, let `x` and `y` be the aggregate `r`-masses of the `a`- and `b`-coordinates. Subtracting `Q(a)=Q(b)=0` gives

`2M_1=a+b`.                                                  (3.21)

Using either root in (3.18) then gives

`M_2=(a^2+b^2)/2`.                                           (3.22)

But also

`M_1=xa+yb`, `M_2=xa^2+yb^2`.                              (3.23)

Since `a!=b`, the unique solution of (3.21)--(3.23) is

`x=y=1/2`.                                                    (3.24)

Hence `x+y=1`. This is impossible because

`x+y=sum_i r_i`
`=sum_i e^{z_i}/[sum_i e^{z_i}-(m-1)]>1.                    (3.25)

Thus no negative interior minimum exists, proving `K_m>=0`.

Finally, if an interior point had `K_m=0`, nonnegativity would make it a global minimum, hence an interior critical point, and the same one-value/two-value contradiction applies. Therefore `K_m>0`. QED.

Combining (3.7) and (3.8):

### Corollary R15-F0111-ALLRAY2 — strict arbitrary-ray concavity

For every nonnegative direction with at least two positive coordinates,

`boxed: g_c(s)=F_n(s c)/s is strictly concave on s>0.`       (3.26)

The one-positive-coordinate case is trivial: `F_n(s c)=0` identically.

---

## 4. Method #27 — exact quadratic cone on **every** nonnegative ray

Let

`C=sum_i c_i`, `M=max_i c_i`,
`N(c)=sum_{i<j}c_i c_j`.                                    (4.1)

Taylor expansion at zero and exponential dominance at infinity give

`g_c(0+)=0`,
`g_c'(0+)=N(c)`,                                             (4.2)

`g_c(infinity)=C-M`,
`g_c'(infinity)=0`.                                          (4.3)

Strict concavity implies that `g_c'` decreases strictly from `N(c)` to `0`.

Now restrict any quadratic to the ray:

`Q_c(s)=A s+B s^2`, `A,B>=0`.                               (4.4)

Dividing `Q_c(s)>=f_c(s)` by `s>0` gives

`A+B s>=g_c(s)`.                                             (4.5)

Define the exact dual boundary

`Phi_c(B)=sup_{s>0}[g_c(s)-B s].`                            (4.6)

Then:

### Theorem R15-F0111-ALLRAY3 — exact all-ray cone

For every nonnegative `c`,

`boxed: A s+B s^2 >= F_n(s c) for all s>=0`

if and only if

`boxed: A>=Phi_c(B).`                                        (4.7)

For at least two active coordinates:

- if `B>=N(c)`, then `Phi_c(B)=0`;
- if `B=0`, then `Phi_c(0)=C-M`;
- if `0<B<N(c)`, there is a unique `s_B>0` with

`g_c'(s_B)=B`,                                               (4.8)

and

`Phi_c(B)=g_c(s_B)-B s_B`.                                  (4.9)

The proof is immediate from strict concavity. In particular, the preceding equal-coordinate subset cone is only the special case `c=1_J`.

For the full quadratic (2.2), put

`A(c)=sum_i A_i c_i`,
`B(c)=sum_{i<j}B_ij c_i c_j`.                               (4.10)

Every global certificate must therefore satisfy the **continuum** of exact constraints

`boxed: A(c)>=Phi_c(B(c)) for every c>=0.`                   (4.11)

This is strictly more informative structurally than checking only the `0/1` subset rays, because asymmetric directions are now admissible test faces.

---

## 5. Method #20 — why the obvious radial-failure algorithm cannot work

The all-ray theorem gives a clean invariant at an exact interior contact.

Suppose `P>=F_n` globally and

`P(q)=F_n(q)`                                                 (5.1)

for an interior base `q>0`. Since `P-F_n` is differentiable and has a global minimum at `q`,

`grad P(q)=grad F_n(q)`.                                     (5.2)

On the radial ray `t=s q`, write

`P(sq)=A_q s+B_q s^2`,                                      (5.3)

where

`A_q=sum_i A_i q_i`,
`B_q=sum_{i<j}B_ij q_i q_j`.                                (5.4)

Let `f(s)=F_n(sq)` and `g(s)=f(s)/s`. Value and radial-gradient contact give

`A_q+B_q=f(1)=g(1)`,                                         (5.5)

`A_q+2B_q=f'(1)`.                                             (5.6)

Hence

`B_q=f'(1)-f(1)=g'(1)`,
`A_q=g(1)-g'(1)`.                                             (5.7)

Therefore

`A_q+B_q s`
`=g(1)+g'(1)(s-1)`,                                          (5.8)

the tangent line to the strictly concave `g` at `s=1`.

A tangent to a concave function lies above it. Thus:

### Theorem R15-F0111-RADIAL — radial saturation

Every nonnegative quadratic global certificate exact at an interior base automatically satisfies

`boxed: P(sq)>=F_n(sq) for every s>=0,`                      (5.9)

with strict inequality for every `s>0`, `s!=1`, and equality also at the common origin `s=0`.

In particular, **the radial ray through the contact can never be the first place where a candidate exact contact fails global majorization.** Searching harder along `sq` is therefore a dead algorithmic route, not merely an unsuccessful numerical experiment.

This pinpoints where the next attack belongs: nonradial asymmetric rays `c`, especially two-level rays adapted to the positive and negative blocks of a candidate Hessian-null vector. The exact constraint (4.11) is now available for every such choice.

---

## 6. What moved and what did not

The source task I0076 did not move and was not reopened. Its source-matching status remains `OPEN / PARTIAL / RETIRED-HANDOFF`, and because there is no surviving frozen candidate the user's fixed four-obligation metric remains non-scoreable in the current state.

The retained F0111 screen did move mathematically:

1. exact face duality is no longer confined to equal-coordinate subsets;
2. strict concavity is proved for every nonnegative ray by the new `K_m` extremal/entropy argument;
3. global majorization yields a continuum of exact ray-cone inequalities;
4. exact value-and-gradient contact forces the radial restriction to sit exactly on the all-ray cone boundary at tangent point `s=1`;
5. hence radial testing is proved structurally incapable of detecting a failure of an exact contact.

This still does **not** prove the `k=2` specialization globally, much less Talagrand Problem 10.9. The unresolved obstruction is genuinely nonradial: one must combine (4.11), coefficient nonnegativity, exact contact, and the mixed-sign Hessian-null/second-contact normal forms developed in preceding runs.

A particularly concrete next move is to take

`c=lambda 1_J + mu 1_K`, `lambda,mu>0`,                     (6.1)

for the two sign blocks of the surviving null-flow candidate, optimize `Phi_c(B(c))` over `lambda/mu`, and ask whether every surviving scalar null regime violates at least one such asymmetric ray inequality. This is now an analytic one-parameter separation problem rather than an unconstrained continuum search.

---

## 7. Validation kept subordinate to the research

Only after the idea and proof route were written did I add a small exact symbolic self-check:

- `artifacts/R15/f0111_allray_exact_e90x.py`
- `artifacts/R15/f0111_allray_exact_e90x.out`

The archived execution ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

It checks only the finite algebra used inside the written theorem: the common quadratic formula for `partial_i K`, the all-equal critical factor, the two-root aggregate solution `x=y=1/2`, the radial tangent identities, and the entropy/variance decomposition at infinity. It is a **SELF-CHECK**, not a substitute for the written proof and not an independent audit.

---

## 8. Model / scheduler-control truth

The installed prompt asks for GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol**. The runtime does not expose authenticated reasoning-effort telemetry, so reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum.

The current deployment manifest still says the exposed scheduler surface provides title/prompt, schedule/timing mode, enabled state and ordinary updates, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution setting**. GPT-6/maximum therefore remains prompt-only in this exposed surface.

The historical P26 `You cannot modify this task` event was authorization-context-specific rather than a universal task immutability theorem: current root `RESULTS.md` records that a later full P26 update succeeded from an authorized context. The lawful workaround for a denied edit is the owning/authorized product/workspace/API/admin context or supported ownership repair; it is not permission bypass or duplicate scheduling. No scheduler, permission, notification, email, Drive, public-posting or paid-compute action was attempted here.

---

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  native_source:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4, Problem 7.2"
    exact_target: "FBM + BBM + independence of complete centered past/future at an arbitrary random time T => 2BM?"
    exclusions:
      - "Problem 7.5"
      - "deterministic-time independence as a substitute"
      - "stopping-time strengthening"
  fixed_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
    after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
    movement: false
    historical_positive_route_value_only: "2/4"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: 6
  retained_screen:
    id: F0111
    status: "PENDING / SELF_CHECK_ONLY / NOT CLAIMED / NOT READY"
    movement:
      - "strict arbitrary-nonnegative-ray concavity theorem"
      - "exact quadratic majorant cone for every nonnegative ray"
      - "continuum ray-cone necessary conditions for a global certificate"
      - "radial saturation theorem: exact interior contact is automatically globally safe on its own radial ray"
    closure: false
    novelty: UNVERIFIED
  tried_moves: [18, 20, 27]
  previous_triple: [11, 24, 29]
  remaining_obligation: "Use asymmetric nonradial two-level rays to separate the surviving mixed-sign Hessian-null / second-contact regimes; native I0076 stays retired until lawful reassignment."
  evidence:
    - "runs/R15/20260919_1913Z_successor_screen_f0111_exact_face_cone_d89w.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "artifacts/R15/f0111_allray_idea_e90x.md"
    - "artifacts/R15/f0111_allray_exact_e90x.py"
    - "artifacts/R15/f0111_allray_exact_e90x.out"
    - "Burdzy--Scheutzow arXiv:1302.6958v4, Definition 2.1 and Problem 7.2"
    - "Ascoli--He--Park--Talagrand arXiv:2608.11183"
    - "Park arXiv:2609.14681"
  audit_ids: []
  closure: false
```

No shared root or peer file was edited. No email, Drive operation, public posting, purchase, permission change, scheduler change or extra receipt-only commit was made.
