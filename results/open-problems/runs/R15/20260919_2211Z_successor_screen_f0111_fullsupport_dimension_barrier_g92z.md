Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: no surviving frozen counterexample candidate, so `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`; status `OPEN / PARTIAL / RETIRED-HANDOFF`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, every full-support two-level Hessian-null exact global quadratic contact is now ruled out in dimensions `n<=29`; the `z<-1` branch is ruled out through `n<=49`. Methods #3, #25, #29.**

# R15 retained screen — projective full-support dimension barrier

Date checked: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`. All F0111 mathematics newly proved below is **SELF_CHECK_ONLY / NOT CLAIMED / PENDING**. It does not reopen I0076, make F0111 READY, establish novelty, solve Talagrand Problem 10.9, or satisfy closure/audit requirements.

## 1. Source fidelity, lifecycle, whole-repository continuation

I continued from

`runs/R15/20260919_2056Z_successor_screen_f0111_projective_quartic_f91y.md`

rather than restarting. I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current NEW-METHODS implementation manifest, the controlling I0076 six-run handoff, the newest R15 report, current successor-gate/claim deltas, and the newest visible neighboring R17 handoff. The current queue is still an admission inventory, not automatic dispatch authority.

Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2 were checked again from the primary PDF on 2026-09-19 UTC. The source definitions are:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that every centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM iff `t -> X_{-t}` is FBM;
- `X` is 2BM iff there is a random time `S` for which the complete centered future and centered past are independent standard Brownian motions.

Problem 7.2 assumes FBM + BBM and only that, at some arbitrary random time `T`, the two complete half-processes

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent. It does **not** say `T` is a stopping time and does **not** separately assume either seam half is Brownian. Problem 7.5 is separate and remains excluded.

The six-run I0076 handoff remains controlling. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent real seam. The later Brownian-prefix/BES candidate has an exact independent seam but was proved to be 2BM. Thus no frozen counterexample candidate survives. The source-matching four-obligation candidate metric is therefore not honestly scoreable; the historical `2/4` is only the retired positive-route handoff metric, not a score for a current candidate.

Fresh exact-title/problem searches on 2026-09-19 UTC recovered the source and related splitting/shift literature but no accessible later primary source explicitly claiming a resolution of exact Problem 7.2. This is bounded negative evidence only.

The newest pre-run successor-gate commit visible in the repository explicitly reports **no free CLOSABLE successor**. F0111 remains separately recorded by successor screening as `PENDING / SELF_CHECK_ONLY / NOT READY`. I therefore did not steal an owned source, promote a PENDING item, or create a successor claim.

## 2. Section-B moves and idea-first order

The preceding R15 run used #5/#11/#24. The long retained-screen history has already exhausted all 30 move numbers at least once, so I do not falsely call this triple globally unused. I use a different nonconsecutive triple in new roles:

- **#3 PROVE SOMETHING STRONGER** — replace elimination of one `n=4` local candidate by a uniform dimension theorem for an entire full-support two-level null class;
- **#25 COUNT THE SAME THING TWICE** — sum every pair-difference Hessian energy inside a sign block to obtain a sharp block-capacity inequality without assuming block symmetry;
- **#29 ADD THE POINTS AT INFINITY** — compactify the surviving scalar branches at `z=+1` and `z=-1`, where the sharp dimension constants emerge.

The route was written before validation in

`artifacts/R15/f0111_fullsupport_dimension_barrier_g92z_idea.md`

at commit `c1b944990a6b9e939bb6b40db4d54817e2c4456f`. The first idea note used a block-symmetrization route; during the proof I found the stronger pair-difference argument below, which removes that symmetry assumption entirely. The subsequent symbolic checker tests only the scalar algebraic core; the PSD/pseudoinverse argument is proved here on the page.

## 3. Setup inherited from the preceding null-curve work

Consider the F0111 `k=2` hazard

`F(t)=sum_i t_i-log S(t)`,  `S(t)=sum_i exp(t_i)-(n-1)`,

on the positive orthant. Let a nonnegative-coefficient quadratic polynomial `P` globally majorize `F` and be exact at an interior point `q`, and put

`G=P-F`,  `H=D^2G(q)>=0`.

Suppose `H` has a **full-support two-level** null vector. After changing its sign and relabeling the two blocks if necessary, write

`h=a 1_J-b 1_K`,  `J disjoint union K=[n]`,  `a>=b>0`,

with `M=|J|`, `N=|K|`, `M+N=n`. Put

`m=(a+b)/2`,  `delta=(a-b)/(a+b) in [0,1)`,

`r_i=exp(q_i)/S(q)`,  `x=sum_{i in J} r_i`,  `y=sum_{i in K}r_i`,

and

`p=sum_i r_i h_i`,  `z=p/m-delta`.

Because the support is all coordinates, the constant term in the signed log-partition measure is

`k=-(n-1)/S(q)<0`,

and `x+y+k=1`.

The prior cubic-null calculation, which is necessary at every Hessian-null local minimum, gives exactly

`k = 2 z(1-z^2)/((1-delta^2)(delta+3z))`,

`x = ((delta+z)(1+z)(1+delta+2z))/(2(1+delta)(delta+3z))`,

`y = ((delta+z)(1-z)(1-delta-2z))/(2(1-delta)(delta+3z))`.

The preceding strict fourth-order classification showed that, when `k<0`, the only surviving scalar regimes are

`z>1` or `z<-1`.

Define

`K2=((delta+z)(1-z^2))/(delta+3z)`,

`t_J=(1-z)^2-K2`,  `t_K=(1+z)^2-K2`,

and

`R=-2(delta+z)(1-z^2)(delta^2 z+3 delta z^2+delta+3z^3)/(delta+3z)^2`.

On the two surviving branches `R>0`, and

`D_h^4 log S(q)=m^4 R`.

The cubic covector from the preceding projective theorem is

`bcal(v)=D^3 log S(q)[v,h,h]`.

Since differentiating the signed variance with respect to one coordinate gives

`bcal_i=r_i((h_i-p)^2-D_h^2 log S(q))`,

we obtain the exact block sums

`bcal(1_J)=x m^2 t_J`,

`bcal(1_K)=y m^2 t_K`.

## 4. New symmetry-free block-capacity lemma

The preceding projective theorem says that a Hessian-null exact global certificate necessarily has `bcal` annihilating `ker H` and

`D_h^4 log S(q) >= 3 bcal^T H^+ bcal`.                 (4.1)

For every vector `v`, the PSD pseudoinverse Cauchy inequality therefore gives

`(bcal(v))^2 <= (bcal^T H^+ bcal)(v^T H v)`.           (4.2)

The new point is that `1_J^T H 1_J` has a certificate-independent upper bound. Since `P` has no square monomials,

`H_ii=r_i-r_i^2`.

Now count all pair-difference energies inside `J`:

`0 <= sum_{i<j in J} (e_i-e_j)^T H(e_i-e_j)`

`   = M sum_{i in J} H_ii - 1_J^T H1_J`.

Hence

`1_J^T H1_J <= M(x-sum_{i in J}r_i^2)`

`              <= M(x-x^2/M)=x(M-x)`,                 (4.3)

where the second inequality is Cauchy. Exactly the same proof gives

`1_K^T H1_K <= y(N-y)`.                                (4.4)

This is stronger than the preliminary symmetry argument in the idea note: no equality of the `q_i` inside a block and no equality of polynomial coefficients is assumed.

Combine (4.1)--(4.4) with `v=1_J`. Without dividing by a potentially zero Hessian energy,

`m^4 R * x(M-x) >= 3 x^2 m^4 t_J^2`.

Since `x>0` and `R>0`,

`boxed: M >= x(1+3 t_J^2/R).`                           (4.5)

Likewise

`boxed: N >= y(1+3 t_K^2/R).`                           (4.6)

These are new block-size necessary conditions for every full-support two-level Hessian-null exact global quadratic contact.

## 5. Interior positivity turns block capacity into a dimension inequality

Because `q` is interior, every `q_i>0`, hence `exp(q_i)>1`. Since full support gives

`S(q)=-(n-1)/k`,

we have

`M < sum_{i in J} exp(q_i)=x S(q)=-x(n-1)/k`,           (5.1)

`N < sum_{i in K} exp(q_i)=y S(q)=-y(n-1)/k`.           (5.2)

Combining (4.5) with (5.1), and (4.6) with (5.2), cancels `x` and `y` and gives two purely scalar necessary inequalities:

`n-1 > Q_J := -k(1+3 t_J^2/R)`,                        (5.3)

`n-1 > Q_K := -k(1+3 t_K^2/R)`.                        (5.4)

The rest of the proof is now an exact two-variable inequality on `0<=delta<1` and the two outer `z` branches.

## 6. Sharp scalar barrier on the `z>1` branch

Set `z=1+s`, `s>0`. Exact simplification gives

`Q_K-256/9 = -2 P_+(delta,s) / [9(delta-1)(delta+1)(delta+s+1)T_+(delta,s)]`,

where

`T_+=delta^2 s+delta^2+3delta s^2+6delta s+4delta+3s^3+9s^2+9s+3>0`.

Write `P_+=sum_{j=0}^6 c_j(delta)s^j`. Its coefficients are

`c_0=8(delta+3)(2delta-1)^2(4delta^2+12delta+11)`,

`c_1=2(64delta^5+512delta^4+1152delta^3+265delta^2-766delta+645)`,

`c_2=512delta^4+2304delta^3+1837delta^2-864delta+2763`,

`c_3=12(64delta^3+131delta^2+29delta+271)`,

`c_4=3(131delta^2+141delta+712)`,

`c_5=9(7delta+78)`,  `c_6=81`.

Only `c_1,c_2` are not visibly positive from their displayed coefficients. Put `delta=t/(1+t)`, `t>=0`. After clearing the positive powers `(1+t)^5` and `(1+t)^4`, respectively, their coefficient lists in increasing powers of `t` are

`c_1: [1290,4918,7302,7602,7544,3744]`,

`c_2: [2763,10188,15823,14438,6552]`.

Thus every `c_j>=0` on `0<=delta<1`, and for `s>0`, `P_+>0`. The denominator above is negative because `delta-1<0` and every other factor is positive. Hence

`boxed: Q_K>256/9` for `0<=delta<1`, `z>1`.             (6.1)

The constant is sharp only at the compactified boundary. Indeed

`lim_{z downarrow 1} Q_K = 48/((1-delta)(1+delta)^3)`,

and subtracting `256/9` factors as

`-16(2delta-1)^2(4delta^2+12delta+11) / [9(delta-1)(delta+1)^3] >=0`,

with equality only at `delta=1/2`.

From (5.4) and (6.1),

`n-1>256/9`,

so the integer dimension must satisfy

`boxed: n>=30` on the `z>1` branch.                     (6.2)

## 7. Sharp scalar barrier on the `z<-1` branch

Set `z=-1-s`, `s>0`. Exact simplification gives

`Q_J-48 = -2 P_-(delta,s) / [(delta-1)(delta+1)(1+s-delta)T_-(delta,s)]`,

where

`T_-=delta^2s+delta^2-3delta s^2-6delta s-4delta+3s^3+9s^2+9s+3`.

To see the sign of `T_-`, put `delta=1-r`, `r>0`. Then

`T_-=r^2s+r^2+3rs^2+4rs+2r+3s^3+6s^2+4s>0`.

For `P_-=sum_{j=0}^6 d_j(delta)s^j`, substitute again `delta=t/(1+t)` and clear the corresponding positive denominator powers. The coefficient lists, in increasing powers of `t`, are

`j=0: [0,144,528,576,264,48]`,
`j=1: [26,486,1782,2258,1176,216]`,
`j=2: [131,796,1943,1590,408]`,
`j=3: [244,752,1064,412]`,
`j=4: [208,369,234]`,
`j=5: [78,71]`,
`j=6: [9]`.

All are nonnegative and, because `s>0`, `P_->0`. Again the denominator is negative, so

`boxed: Q_J>48` for `0<=delta<1`, `z<-1`.               (7.1)

At the compactified boundary,

`lim_{z uparrow -1}Q_J = 48/((1+delta)(1-delta)^3) >=48`,

with equality only at `delta=0`. Explicitly the difference from `48` is

`-48 delta(delta^3-2delta^2+2)/[(delta-1)^3(delta+1)]`,

which is nonnegative on `[0,1)` (the cubic decreases from `2` to `1`).

Thus (5.3) and (7.1) imply

`n-1>48`,

hence

`boxed: n>=50` on the `z<-1` branch.                    (7.2)

## 8. New theorem and what it actually settles

Combining the two branches gives the following restricted but uniform theorem.

**R15-F0111-DIMENSION-BARRIER.** Suppose a nonnegative-coefficient quadratic global certificate for the F0111 `k=2` hazard is exact at an interior point and its contact Hessian has a full-support two-level mixed-sign null direction. Then, after orienting that direction as above:

- if its cubic-null scalar parameter satisfies `z>1`, necessarily `n>=30`;
- if `z<-1`, necessarily `n>=50`.

Consequently,

`boxed: no full-support two-level Hessian-null first-bifurcation mechanism exists in dimensions n<=29.}`

Moreover, in `30<=n<=49`, only the `z>1` outer branch can remain.

This strictly strengthens the preceding run, which eliminated one exact `n=4` locally feasible candidate by a projective fourth-order test but did not provide a uniform dimension range.

The theorem is **not** a solution of the retained F0111 problem. It addresses only the Hessian-singularity first-bifurcation mechanism, only for full-support two-level null directions, and only `k=2`. Non-two-level mixed directions, directions with zero coordinates, the second-contact mechanism, and the full Talagrand quantifiers remain unresolved.

## 9. Exact validation, after the idea

After the research route was recorded, I ran one exact symbolic checker for the scalar algebra only:

- `artifacts/R15/f0111_fullsupport_dimension_barrier_g92z.py`, creation commit `d1ad333bab6f270ea53174c932acccb58bd2d790`;
- `artifacts/R15/f0111_fullsupport_dimension_barrier_g92z.out`, creation commit `e1d6fd43be3177789ee04d2cda838e4795d2e8c0`.

It checks the exact `Q_J,Q_K` simplifications, both polynomial decompositions, the two boundary constants, and the integer implications. The archived execution ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This is a self-check, not an independent audit. No numerical path sampling is used for any Brownian-law claim, and no numerical grid is being treated as proof of the F0111 inequalities.

## 10. Literature and novelty status

Current primary-literature queries dated 2026-09-19 checked the original Burdzy--Scheutzow source/title/Problem 7.2 and the current Talagrand-convexity line. Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulate the discrete Convexity Conjecture through `k`-thresholds and prove substantial classes. Jinyoung Park, arXiv:2609.14681 (2026-09-13), proves a dimension-free expectation/fractional-expectation comparison explicitly described as progress toward the conjecture. These do not supply a full resolution of Talagrand Problem 10.9.

I found no accessible source in this bounded search stating the dimension barrier proved above. **Novelty remains UNVERIFIED.** The underlying higher-order tangent/pseudoinverse optimality mechanism is generic prior art and should not be advertised as intrinsically new; any eventual novelty claim would have to concern the F0111 specialization and scalar classification after a deeper search.

## 11. Next mathematical cursor

The uniform barrier identifies a much sharper remaining front. For full-support two-level Hessian-null directions:

- dimensions below `30` are gone completely;
- the negative outer branch is gone below `50`;
- the first possible dimension is therefore `30`, necessarily on `z>1`.

The next useful attack is not another derivative of the same one-dimensional log partition. It is to combine the exact value-contact equation and the previously proved arbitrary-ray majorant cone with the new block-size inequalities, concentrating first on the near-sharp `z downarrow 1` regime. A second, more structural route is to prove a compression theorem that any mixed-sign null direction violating global certification can be replaced by a two-level one; that would make the dimension barrier relevant to the general mixed-sign mechanism.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  actual_model: "GPT-5.6 Sol"
  reasoning_level: "UNVERIFIED; not GPT-6 maximum"
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "retired after six-run handoff; do not increment"
  native_remaining_obligation: "future reassignment would need a new frozen candidate satisfying all four source obligations or a proof of the full source implication; no stopping-time strengthening"
  successor_gate: "no newly free READY+CLOSABLE successor found in latest bounded repository gate; no claim created"
  retained_screen: "Talagrand F0111 Problem 10.9, k=2; SELF_CHECK_ONLY / NOT CLAIMED / PENDING"
  retained_aux_metric: "largest uniform dimension range excluded for full-support two-level Hessian-null exact contacts"
  retained_aux_before: "UNMEASURED (only isolated/local candidates eliminated)"
  retained_aux_after: 29
  retained_secondary_result: "z<-1 branch impossible for n<=49"
  tried_moves: [3,25,29]
  remaining_obligation: "eliminate/realize the z>1 full-support branch from n=30 upward; extend beyond two-level/full-support null directions; separately control second-contact mechanism"
  evidence:
    idea_commit: "c1b944990a6b9e939bb6b40db4d54817e2c4456f"
    checker_commit: "d1ad333bab6f270ea53174c932acccb58bd2d790"
    checker_output_commit: "e1d6fd43be3177789ee04d2cda838e4795d2e8c0"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY; no independent audit requested or counted"
```

## 13. Model / scheduler / denied-task boundary

The platform limitation remains unchanged in the exposed task surface. The interface exposes prompt/title, schedule/timing, enabled state and ordinary task updates, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field. GPT-6 / maximum therefore remains prompt-only here.

The operative implementation record preserves the historical P26 ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` in one authorization context. Root `RESULTS.md` records that a later full P26 update succeeded in an authorized P/C context. Thus the compliant workaround for an edit-denied task is the owning/authorized workspace/account/API/admin context or platform support, not a permission bypass or duplicate task. Actually guaranteeing GPT-6 / maximum would require a supported scheduling/product/backend/API surface that persists those routing controls and returns authenticated runtime attestation.
