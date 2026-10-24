Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains OPEN / PARTIAL / RETIRED-HANDOFF at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission `E_ready: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the previous homogeneous `k=2` result is strengthened from the restricted `n=3` / `gamma=1` theorem and the all-`n` `gamma=1/4` theorem to an exact **all `n>=2`, homogeneous-base `C_1` certificate**, with a further flat-support extension. Methods #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS.**

# R15 successor screen — exact all-n homogeneous C1 certificate for Talagrand k=2

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source material. The complete proofs are written on the page. No independent fleet audit or novelty claim is asserted.

## 1. Continuity, required repository read, source fidelity, and rotation state

Before doing mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the latest coordinator admission delta `operations/task_health/runs/2026-09-18T160500Z/admission_delta.md`, the controlling six-run R15 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`, the immediately preceding R15 report `runs/R15/20260918_1553Z_successor_screen_f0111_paircycle_g61q.md`, and the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`. I also recovered the intake/search history for I0076 rather than restarting the target.

I rechecked the primary Burdzy--Scheutzow PDF, arXiv:1302.6958v4. Definition 2.1 says that `X` is FBM if there are random origins `S_n -> -infinity` a.s. from which the complete centered future is standard Brownian motion; BBM means time reversal is FBM; 2BM means that at one random origin `S` the complete centered forward and backward half-paths are **independent standard Brownian motions**. Problem 7.2 assumes only FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-paths are independent. The source does **not** assume that `T` is a stopping time and does **not** assume either seam half is itself Brownian. Problem 7.5 remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate was eliminated because no source-valid independent seam survived. The later Brownian-prefix/BES candidate had exact seam independence but was proved actually 2BM. There is therefore **no surviving frozen counterexample candidate**. The historical `2/4` is a carried retirement value, not the score of an active candidate. I do not reopen I0076 in this run.

Fresh dated searches on 2026-09-18 again recovered the original Burdzy--Scheutzow paper, the University of Washington publication page, and citation/mirror material, but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

The latest coordinator admission delta still records `E_READY_SUCCESSOR=0 -> 0`. I therefore create no successor claim and do not promote any PENDING queue item to READY.

## 2. Retained screen: exact Talagrand target

The retained screening problem is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`). For

`A_{n,k}={X subset[n]: |X|>=k}`

with independent coordinate inclusion probabilities `1-exp(-t_i)`, write

`F_{n,k}(t)=-log P_t(|X|<k)`.

Talagrand's `C_gamma` requirement asks, for a fixed `gamma>0`, that at every base point `q>=0` there be a multilinear polynomial with nonnegative coefficients and zero constant term,

`P(t)=sum_{empty != I subset[n]} beta_I t_I`, `beta_I>=0`,

such that

`F_{n,k}(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_{n,k}(q)`.

Problem 10.9 asks whether one universal positive `gamma` works for all cardinality thresholds. The source PDF still states this exact problem. Dated 2026-09-18 searches for the exact title / `Problem 10.9` / `C_gamma` recovered Talagrand's source and related later DeMarco--Kahn / threshold literature, but no accessible theorem explicitly resolving this Definition-10.1 positive-multilinear-majorant problem. Again, this is bounded negative evidence only.

The preceding R15 work proved: all `n`, homogeneous `k=2` at `gamma=1/4`; then `n=3,k=2`, homogeneous base, at the exact budget `gamma=1`; then increasingly strong weak-dual no-go theorems. This run returns to the primal side and removes both the `n=3` restriction and the loss in `gamma`.

## 3. Method #3 — a stronger global two-moment envelope for every n

For the rest of the theorem fix `n>=2` and `k=2`. The exact hazard is

`F_{n,2}(t)=T-log(1+sum_i(exp(t_i)-1))`,                          (3.1)

where

`T=e_1(t)=sum_i t_i`,

`E=e_2(t)=sum_{i<j} t_i t_j`.

If `T=0`, then `F=0`. Assume `T>0` and define the normalized pair scale

`s = 2E / ((n-1)T).`                                             (3.2)

Since

`E=(T^2-sum_i t_i^2)/2 <= (n-1)T^2/(2n)`,

we have

`0<=s<=T/n`.                                                     (3.3)

Define

`A_n(s)=1-[1/(n s)] log(n exp(s)-n+1)` for `s>0`,

and set `A_n(0)=0` by continuity.                                (3.4)

### Theorem R15-F0111-MOM1 — global two-moment envelope

For every `t in R_+^n`,

`F_{n,2}(t) <= T A_n(s)`,                                        (3.5)

with `s` as in (3.2). Equality holds on every homogeneous ray `t=c 1_n`.

### Proof

Put

`g(x)=(exp(x)-1)/x` for `x>0`, `g(0)=1`.

The integral representation

`g(x)=int_0^1 exp(u x) du`

shows that `g` is convex on `[0,infinity)`.

Using weights `w_i=t_i/T`, Jensen gives

`sum_i (exp(t_i)-1)
 = T sum_i w_i g(t_i)
 >= T g(sum_i w_i t_i)
 = T g((sum_i t_i^2)/T).`                                       (3.6)

If `s=0`, then at most one coordinate is positive and both sides of (3.5) are zero, so assume `s>0`. By (3.2),

`(sum_i t_i^2)/T = T-2E/T = T-(n-1)s.`                          (3.7)

Write

`p = T/s-(n-1).`                                                 (3.8)

By (3.3), `p>=1`, and (3.7) becomes

`(sum_i t_i^2)/T = p s`,

while `T=(p+n-1)s`. Hence (3.6) implies

`1+sum_i(exp(t_i)-1)
 >= 1+[(p+n-1)/p](exp(p s)-1).`                                 (3.9)

We now prove the scalar inequality

`1+[(p+n-1)/p](exp(p s)-1)
 >= (n exp(s)-n+1)^((p+n-1)/n)`                                 (3.10)

for every `p>=1`, `s>=0`.

Set `z=exp(s)-1>=0`. The two sides of (3.10) become

`L(z)=1+[(p+n-1)/p]((1+z)^p-1)`,

`R(z)=(1+n z)^((p+n-1)/n)`.

They satisfy `L(0)=R(0)=1`, and

`L'(z)=(p+n-1)(1+z)^(p-1)`,

`R'(z)=(p+n-1)(1+n z)^((p-1)/n).`

Bernoulli's/binomial inequality `(1+z)^n>=1+n z` gives `L'(z)>=R'(z)` because `(p-1)/n>=0`. Thus `L>=R`, proving (3.10).

Combining (3.9)--(3.10) and using `T=(p+n-1)s`,

`log(1+sum_i(exp(t_i)-1))
 >= [T/(n s)] log(n exp(s)-n+1).`                               (3.11)

Subtracting from `T` gives exactly (3.5).

If `t=c1_n`, then `s=c`, Jensen in (3.6) is equality and `p=1`, so (3.10) is also equality. Therefore (3.5) is exact on every homogeneous ray. QED.

This strictly generalizes the preceding `n=3` moment-ratio envelope. The proof is not dimension-specific.

## 4. Concavity of the profile

The envelope becomes a positive polynomial certificate because `A_n` is increasing and concave.

### Lemma R15-F0111-MOM2

For every `n>=2`, `A_n(0)=0`, `A_n'(s)>0` for `s>0`, and `A_n''(s)<0` for `s>0`.

### Proof

Let

`H(s)=log(n exp(s)-n+1)`.

Then `H(0)=0` and

`A_n(s)=1-H(s)/(n s).`                                          (4.1)

Since `H` is concave, `H(s)/s` is decreasing, so `A_n` is increasing.

For concavity set

`u(s)=H'(s)=n exp(s)/(n exp(s)-n+1).`

For `s>0`, `u(s)>1`. Direct differentiation gives

`H''=u(1-u)<0`,

`H'''=u(1-u)(1-2u)>0`.                                          (4.2)

Now

`d^2/ds^2 [H(s)/s]
 = [s^2 H''(s)-2sH'(s)+2H(s)]/s^3.`                            (4.3)

Let the numerator be `K(s)`. Then

`K'(s)=s^2 H'''(s)>0`,

and `K(s)->0` as `s downarrow 0`. Hence `K(s)>0` for `s>0`, so `H(s)/s` is strictly convex. By (4.1), `A_n` is strictly concave. QED.

Because `A_n` is concave, increasing and satisfies `A_n(0)=0`, every tangent line at `c>0` has nonnegative intercept and slope.

## 5. Exact all-n homogeneous C1 certificate

Fix a homogeneous base

`q=c 1_n`, `c>0`.

Define

`a_{n,c}=A_n(c)-c A_n'(c) >=0`,

`b_{n,c}=[2/(n-1)] A_n'(c) >0`.                                (5.1)

Consider the positive multilinear polynomial

`P_{n,c}(t)=a_{n,c} e_1(t)+b_{n,c} e_2(t).`                     (5.2)

### Theorem R15-F0111-C1HOM — homogeneous k=2 has exact C1 budget in every dimension

For every `n>=2`, every `c>0`, and every `t>=0`,

`F_{n,2}(t)<=P_{n,c}(t)`,                                      (5.3)

and at the prescribed base

`P_{n,c}(c1_n)=F_{n,2}(c1_n).`                                 (5.4)

Therefore the cardinality-two threshold satisfies Talagrand's `C_1` requirement at every strictly positive homogeneous base point, in every dimension.

### Proof

Concavity gives the tangent inequality

`A_n(s)<=A_n(c)+A_n'(c)(s-c)=a_{n,c}+A_n'(c)s.`                (5.5)

Multiply by `T` and use `T s=2E/(n-1)`. The global envelope (3.5) yields

`F_{n,2}(t)
 <=T A_n(s)
 <=a_{n,c}T+[2A_n'(c)/(n-1)]E
 =P_{n,c}(t).`

This proves (5.3). At `t=c1_n`, the envelope (3.5) is equality and `s=c`, while the tangent (5.5) is equality at its tangency point. Thus (5.4) follows. Since `a_{n,c},b_{n,c}>=0`, this is a source-valid positive multilinear majorant. At `gamma=1`, the Talagrand budget is exactly (5.4). QED.

### What moved

The earlier all-`n` theorem only obtained a fixed `gamma=1/4`, and the exact `gamma=1` theorem was only proved at `n=3`. This run proves `gamma=1` for **all `n>=2`** at every homogeneous positive base.

No weak-dual restriction remains in this homogeneous sector: this is a direct primal certificate, so it automatically handles full-support atoms, arbitrarily many atoms, and every support topology that the preceding weak-dual screens were trying to eliminate individually.

## 6. Method #15 — break full symmetry: flat-support bases also have C1 certificates

The preceding theorem extends beyond full homogeneous vectors. Let `S subset[n]`, `m=|S|`, and let

`q_i=c` for `i in S`,

`q_i=0` for `i notin S`.                                       (6.1)

Thus the positive coordinates are equal but the full `S_n` symmetry is broken.

### Theorem R15-F0111-C1FLAT — every equal-on-support base has exact C1 budget

For every `q` of the form (6.1), there exists a positive multilinear polynomial `P_q` such that

`F_{n,2}(t)<=P_q(t)` for all `t>=0`,

and

`P_q(q)=F_{n,2}(q).`                                           (6.2)

Hence `C_1` holds at every flat-support base.

### Proof

First suppose `m>=2`. Apply Theorem C1HOM on the coordinates of `S` to obtain a polynomial `P_S(t_S)` with

`F_{m,2}(t_S)<=P_S(t_S)`,

and equality at `c1_S`.

Write

`A=1+sum_{i in S}(exp(t_i)-1)`,

`B=sum_{j notin S}(exp(t_j)-1)`,

`T_out=sum_{j notin S} t_j`.

From the exact formula (3.1),

`F_{n,2}(t)-F_{m,2}(t_S)
 =T_out-log((A+B)/A)
 <=T_out.`                                                      (6.3)

Therefore

`P_q(t)=P_S(t_S)+sum_{j notin S}t_j`                            (6.4)

is a positive multilinear global majorant. At `q`, every outside coordinate vanishes, so (6.2) holds.

If `m=1`, then the event that every coordinate outside `S` is absent guarantees fewer than two successes. Its probability is `exp(-T_out)`, hence

`F_{n,2}(t)<=T_out=sum_{j notin S}t_j`.                          (6.5)

This polynomial vanishes at `q`, as does `F(q)`.

If `m=0`, use the trivial global bound

`F_{n,2}(t)<=sum_i t_i`,                                        (6.6)

which follows from retaining only the all-absent event in `P(|X|<2)`. Both sides vanish at `q=0`. QED.

Thus the exact `C_1` sector now contains every base whose nonzero entries have one common level, not only strictly positive homogeneous vectors.

## 7. Method #20 — exact reason the two-moment algorithm does not solve heterogeneous q

The new envelope is sharp on homogeneous rays but it cannot by itself prove the full heterogeneous-base `k=2` problem for any universal `gamma>0`.

Indeed, take for example

`q^(M)=(M,epsilon,0,...,0)`

with fixed `epsilon>0` and `M->infinity`. Then only two coordinates are active at the base, so

`F_{n,2}(q^(M))
 = -log(exp(-M)+exp(-epsilon)-exp(-M-epsilon))
 -> epsilon.`                                                   (7.1)

On the other hand,

`T_M=M+epsilon`,

`E_M=M epsilon`,

`s_M=2M epsilon/((n-1)(M+epsilon))
 -> 2epsilon/(n-1)>0.`                                         (7.2)

Any certificate obtained solely by taking a tangent to the global envelope `T A_n(s)` and evaluating it at `gamma q^(M)` has optimized envelope budget proportional to

`gamma T_M A_n(gamma s_M)`,                                    (7.3)

which grows linearly in `M`, while the target budget `gamma F(q^(M))` stays bounded by (7.1).

So the two-statistic state `(e_1,e_2)` is exactly the right object for homogeneous/flat-support bases but loses the coordinatewise information needed in extreme heterogeneous configurations. This is not a numerical counterexample to Talagrand; it is an analytic obstruction to this **proof algorithm**. The next viable route must use coordinate-adaptive coefficients or a richer hierarchy of invariants, rather than another refinement of the same symmetric two-moment envelope.

## 8. Prior art / current literature

Dated 2026-09-18 searches performed this run:

- Burdzy--Scheutzow exact title, `Problem 7.2`, later citing/author material;
- Talagrand exact title, `Problem 10.9`, `C_gamma`, cardinality threshold, positive multilinear majorant;
- related DeMarco--Kahn / later threshold work.

The searches recovered the original sources and related threshold literature, but I found no accessible publication explicitly stating the all-`n` homogeneous `k=2`, exact-`C_1` theorem above, nor a source resolving Talagrand Problem 10.9 in its full heterogeneous-`q`, all-`k` form. The mechanism here is elementary enough that prior occurrence is plausible. **Novelty is UNVERIFIED.** Non-retrieval is not evidence of novelty.

## 9. Validation / artifacts

No checker was created. The new claims are theorem-sized analytic statements, and their complete proofs are on this page. Creating a grid or floating-point certificate would not strengthen them and would violate the 90/10 instruction. No Brownian path samples are used.

No independent audit is claimed. The retained screen remains PARTIAL with respect to Talagrand's full Problem 10.9.

## 10. Model / scheduler control status

The exposed task-management schema still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. It exposes prompt/title/schedule-or-relative-start/timing-mode/enabled fields only. Therefore GPT-6 / maximum remains prompt-only here, and this run is honestly labelled GPT-5.6 Sol / UNVERIFIED.

The repository's current `RESULTS.md` also corrects an older operational point: one historical P26 edit did return `You cannot modify this task`, but a later authorized P/C context records that the full P26 update succeeded. Thus the earlier denial was context/authorization-specific, not a permanent property of that task ID. The legitimate remedy for a denied task remains the owning/admin-authorized context or platform support; no duplication, permission bypass, or scheduler mutation is attempted here.

## 11. Next route

The next fresh method triple should not repeat this run's `#3,#15,#20`. The mathematically minimal next targets are:

1. coordinate-adaptive positive coefficients for the two-threshold hazard at a genuinely two-level heterogeneous base;
2. a proof or exact obstruction for bases with two positive levels, starting with `q=(a,b,0,...,0)` and then `q=(a,b,b,...,b)`;
3. only after that, investigate whether the structure lifts through the Pascal recursion to `k>=3`.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  source: "Burdzy-Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4, Problem 7.2 / intake I0076"
  source_metric:
    name: "four source-matching obligations for one frozen counterexample candidate"
    before: "historical carried 2/4; no surviving frozen candidate"
    after: "historical carried 2/4; no surviving frozen candidate"
    movement: false
  source_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "frozen at six-run retirement handoff; not incremented during successor screening"
  admission_metric:
    name: E_ready
    before: 0
    after: 0
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
    status: PARTIAL
    before: "all-n homogeneous k=2 gamma=1/4; n=3 homogeneous k=2 gamma=1"
    after: "all n>=2 homogeneous k=2 exact C1; all equal-on-support bases exact C1"
    theorem_ids:
      - R15-F0111-MOM1
      - R15-F0111-MOM2
      - R15-F0111-C1HOM
      - R15-F0111-C1FLAT
  tried_moves: [3, 15, 20]
  remaining_obligation: "full heterogeneous-q k=2, then k>=3; I0076 source remains retired handoff"
  evidence:
    - "primary Burdzy-Scheutzow PDF Definition 2.1 and Problem 7.2 rechecked 2026-09-18"
    - "Talagrand source Problem 10.9 rechecked in current literature pass"
    - "complete analytic proofs in this immutable report"
  audit_ids: []
  novelty: UNVERIFIED
```
