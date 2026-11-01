Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT: `E_geom = 1 -> 1`; literal D0057 remains REFUTED at owner-proof level but NOT CLOSED pending `0/2` independent source-level audits; unchanged count `4 -> 5`; second recovery after STUCK-1; methods #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT, #30 ONE SCALE AT A TIME.**

# R01 — D0057 recovery 2: an exact dissipation potential and a static extremal obstruction to moment-only anti-dip proofs

Run date: 2026-09-17 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`. Delivery: private GitHub only.

## 0. Continuity, ownership, exclusions, and current repository state

I continued from the newest complete R01 report

`runs/R01/20260917T1807Z_d0057_cegm_bridge_41c7d6a2.md`

rather than restarting the stale native title.

- `I0024` / Aldous--Fill Open Problem 3.44 remains frozen at exact distortion `C=1`; its right-inverse flow formula, discarded-candidate counterexamples, and two independent PASS audits are preserved and were not reopened.
- `I0113` remains rotated.
- `G0012` remains rotated after its six-run handoff.
- The old R01 FEI assignment remains retired; P03 owns FEI.
- The active create-only claim remains `operations/claims/D0057.md`, owned exclusively by R01.

Before doing mathematics I refreshed the required repository surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the D0057 claim, the newest own report above, the D-intake history, and the newest neighboring R02 report. R02 has retired its current Frankl target after its sixth unchanged run and is on successor-admission hold; there is no complete neighboring closure package to audit, so no audit budget was spent.

The scheduler/model limitation is unchanged. The exposed task surface has prompt/title/schedule/timing/enabled controls, but no model selector, no reasoning selector, no authenticated applied-model telemetry, and no guaranteed one-hour execution control. The historical P26 message `You cannot modify this task` was authorization-context-specific; another authorized context later succeeded. Enforcing GPT-6/maximum requires a product/backend surface that exposes those fields or an authorized ownership/support migration. No scheduler modification or permission workaround was attempted here.

## 1. Source, literal verdict, and frozen metric

Active source: Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787 / Springer Proc. Math. Stat. 300 (2019), source conditional-geometric conjecture.

For fixed integer `m>=2`,

\[
X_{n+1}=\bigl(X_n^{(1)}+\cdots+X_n^{(m)}-1\bigr)_+,
\]

with independent copies on the right, under the printed critical condition

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty.
\]

The source asks for

\[
\mathbf P(X_n=k\mid X_n>0)\longrightarrow \frac{m-1}{m^k},\qquad k\ge1.
\]

The fixed metric is

`E_geom in {0,1}`.

It moved `0 -> 1` in `runs/R01/20260917T1358Z_d0057_lacunary_refutation_4c8e21ab.md` by a source-valid critical lacunary counterexample. Therefore the literal source statement remains **REFUTED at owner-proof level**. Protocol closure remains unavailable because there are still `0/2` independent source-level audits. This run does not relabel the source and does not substitute a stronger repaired conjecture for D0057.

The natural repaired laboratory, explicitly anticipated by the source authors, adds

\[
\mathbf E[X_0^3m^{X_0}]<\infty.
\tag{1.1}
\]

The previous run recovered Collet--Eckmann--Glaser--Martin's 1984 formal critical profile for `m=2` and proved that making their smoothness-in-iteration step rigorous would imply both `q_n~4/n^2` and the geometric Yaglom law. It also derived the exact conditioned-law shift identity and isolated the missing issue as local regularity of `q_{n+1}/q_n`.

## 2. Dated literature/status check

Searches refreshed on 2026-09-17 included the exact source title/conjecture, `Derrida-Retaux conditional limit geometric fixed m critical`, later-author work, sustainability probability, generalized/geometric-offspring models, and the CEGM 1983/1984 paper.

Primary/current items checked:

1. Chen--Derrida--Hu--Lifshits--Shi, arXiv:1705.04787. The paper states the stronger critical assertions as conjectures. Under (1.1), its Theorem 1.7 gives two-sided `epsilon_n \asymp 1/n` bounds for `epsilon_n=G_n(m)-1`; later in the paper it obtains harmonic/averaged information rather than the full pointwise survival constant.
2. Chen--Hu--Shi, *The sustainability probability for the critical Derrida-Retaux model*, arXiv:2108.05610 / PTRF 2022. It proves `P(X_n>0)=n^{-2+o(1)}` at criticality using pivotal vertices/open paths and coupling, not the exact fixed-`m` conditional geometric limit.
3. Li--Zhang, *Asymptotic behavior of the generalized Derrida-Retaux recursive model*, arXiv:2411.13068 / J. Stat. Phys. 2025. Its conditional limit result is for a generalized model with geometric offspring, not the deterministic `m`-offspring source recursion.
4. X. Chen, *Infinite Differentiability of the Free Energy for a Derrida--Retaux System*, Acta Math. Sinica, published online 2026-05-07 / 2026 volume. Its target is free-energy differentiability, not the source conditional Yaglom law.
5. Collet--Eckmann--Glaser--Martin, *Study of the Iterations of a Mapping Associated to a Spin Glass Model*, Comm. Math. Phys. 94 (1984), with the 1983 Numdam/CERN preprint. Their final critical profile uses an explicitly assumed smoothness in the iteration index.

A bounded search still did not surface a theorem closing the arbitrary deterministic-`m`, finite-third-weighted-moment conditional geometric limit. That is only negative search evidence, not a novelty or openness certificate. I did not perform a complete citation-graph audit.

## 3. Setup: exact generating-function recursion

Write

\[
G_n(s):=\mathbf E[s^{X_n}],\qquad
q_n:=\mathbf P(X_n>0)=1-G_n(0),\qquad
\epsilon_n:=G_n(m)-1.
\]

The recursion gives exactly

\[
G_{n+1}(s)
=s^{-1}G_n(s)^m+(1-s^{-1})G_n(0)^m.
\tag{3.1}
\]

At `s=m`, define

\[
f_m(x):=\frac{(1+x)^m-1}{m},
\tag{3.2}
\]

\[
\sigma_n:=\frac{m-1}{m}\bigl[1-(1-q_n)^m\bigr],
\tag{3.3}
\]

and

\[
h_m(x):=f_m(x)-x
=\frac{(1+x)^m-1-mx}{m}.
\tag{3.4}
\]

Then (3.1) becomes

\[
\boxed{\epsilon_{n+1}=f_m(\epsilon_n)-\sigma_n}
\tag{3.5}
\]

or equivalently

\[
\boxed{\sigma_n=\epsilon_n-\epsilon_{n+1}+h_m(\epsilon_n).}
\tag{3.6}
\]

Because

\[
q\le 1-(1-q)^m\le mq,\qquad 0\le q\le1,
\]

we have the uniform comparison

\[
\boxed{
\frac{m-1}{m}q_n\le \sigma_n\le (m-1)q_n.
}
\tag{3.7}
\]

Also `h_m(x)>=0` for `x>=0`, and

\[
h_m(x)=\frac{m-1}{2}x^2+O_m(x^3)
\quad (x\downarrow0).
\tag{3.8}
\]

These identities are the starting point for all three methods in this run.

## 4. Method #13 — a genuine monovariant: cumulative dissipation plus the current critical excess

### Proposition R01-D0057-C006 — exact monotone potential

Define

\[
M_N:=\epsilon_N+\sum_{n=0}^{N-1}\sigma_n.
\tag{4.1}
\]

Then

\[
\boxed{M_{N+1}-M_N=h_m(\epsilon_N)\ge0.}
\tag{4.2}
\]

Hence `M_N` is nondecreasing. Under the repaired hypothesis (1.1), `M_N` converges to a finite limit.

#### Proof

By definition and (3.6),

\[
M_{N+1}-M_N
=(\epsilon_{N+1}-\epsilon_N)+\sigma_N
=h_m(\epsilon_N),
\]

which is nonnegative by (3.4). Under (1.1), the source's Theorem 1.7 gives

\[
\epsilon_N\asymp \frac1N.
\tag{4.3}
\]

For all sufficiently large `N`, (3.8) therefore gives `h_m(epsilon_N)=O_m(N^{-2})`, so `sum_N h_m(epsilon_N)<infinity`. Equation (4.2) then shows that the monotone sequence `M_N` has finite total increment and therefore a finite limit. `square`

The useful form is the tail identity obtained by summing (3.6).

### Corollary R01-D0057-C007 — exact tail-dissipation identity

Under (1.1), for every sufficiently large `N`,

\[
\boxed{
\Sigma_N:=\sum_{n=N}^{\infty}\sigma_n
=\epsilon_N+\sum_{n=N}^{\infty}h_m(\epsilon_n).
}
\tag{4.4}
\]

Moreover there are constants `0<c<C<infinity`, depending on the initial law and `m`, such that

\[
\boxed{
\frac cN\le \Sigma_N\le\frac CN,
\qquad
\frac{c'}N\le\sum_{n=N}^{\infty}q_n\le\frac{C'}N.
}
\tag{4.5}
\]

#### Proof

Sum (3.6) from `n=N` to `R`:

\[
\sum_{n=N}^{R}\sigma_n
=\epsilon_N-\epsilon_{R+1}+
\sum_{n=N}^{R}h_m(\epsilon_n).
\]

Under (4.3), `epsilon_{R+1}->0`; letting `R->infinity` proves (4.4). Again by (4.3) and (3.8), for sufficiently large `n`,

\[
c_0n^{-2}\le h_m(\epsilon_n)\le C_0n^{-2}.
\]

Thus both `epsilon_N` and the tail `sum_{n>=N}h_m(epsilon_n)` are of order `1/N`, which proves the first comparison in (4.5). The second follows from (3.7). `square`

### Why this helps

The exact pointwise conjecture predicts `q_n` of order `n^{-2}`. Corollary C007 rigorously gives its integrated/Tauberian precursor:

\[
\boxed{
\sum_{n\ge N}q_n\asymp N^{-1}.
}
\tag{4.6}
\]

Thus the missing pointwise theorem is no longer merely `derive the correct average order`: it is a regularity theorem for how the exact dissipation `sigma_n` is distributed inside its monotone tail potential `Sigma_N`.

## 5. Method #30 — one dyadic scale at a time: bad times have small density, and macroscopic downward shocks are sparse

Corollary C007 immediately yields for every sufficiently large `N`

\[
\sum_{n=N}^{2N}q_n\le\frac{C'}N.
\tag{5.1}
\]

### Proposition R01-D0057-C008 — dyadic density control

For every `K>0`,

\[
\boxed{
\#\left\{n\in[N,2N]:q_n>\frac{K}{N^2}\right\}
\le \frac{C'N}{K}.
}
\tag{5.2}
\]

Equivalently, the fraction of times in `[N,2N]` for which `N^2q_n>K` is at most `C'/K`.

#### Proof

If `A_N` denotes the set in (5.2), then by (5.1)

\[
\frac{|A_N|K}{N^2}
<\sum_{n\in A_N}q_n
\le\sum_{n=N}^{2N}q_n
\le\frac{C'}N.
\]

Rearranging gives (5.2). `square`

This is a natural-density tightness statement for the rescaled survival probability on each dyadic block. It is weaker than pointwise tightness, but it rules out a positive-density population of very large spikes.

There is also a stronger statement for **downward shocks of `epsilon_n`**. Since `h_m>=0`, (3.6) gives

\[
(\epsilon_n-\epsilon_{n+1})_+\le\sigma_n.
\tag{5.3}
\]

Therefore

\[
\boxed{
\sum_{n=N}^{2N}(\epsilon_n-\epsilon_{n+1})_+
\le\frac{C}{N}.
}
\tag{5.4}
\]

Consequently, for each fixed `eta>0`,

\[
\boxed{
\#\left\{n\in[N,2N]:
\epsilon_n-\epsilon_{n+1}\ge\frac{\eta}{N}
\right\}
\le \frac C\eta.
}
\tag{5.5}
\]

So CEGM's missing smoothness cannot fail through order-`1/n` downward jumps at many times: there are only `O_{m,law,eta}(1)` such jumps per dyadic scale. What remains possible is oscillation on the **natural `1/n^2` scale**, exactly the scale at which the conjectured survival constant lives. This is the first place the current route genuinely runs out of resolution.

A related one-sided reciprocal estimate is immediate from `sigma_n>=0`:

\[
\epsilon_{n+1}\le f_m(\epsilon_n).
\]

On any bounded `epsilon` range, `f_m(x)<=x+C_mx^2`, hence

\[
\frac1{\epsilon_{n+1}}\ge\frac1{\epsilon_n}-C_m.
\tag{5.6}
\]

For `m=2` this is exact with `C_m=1/2`, because `f_2(x)=x+x^2/2`. It gives another monovariant, `1/epsilon_n+C_m n`, but (4.4) is the more informative object because it directly contains survival mass.

## 6. Method #24 — the static extremal problem shows why moment-only anti-dip proofs cannot close

The obvious next hope would be a one-time critical inequality forcing `q` to be comparable to `epsilon^2`, perhaps using the same third-derivative scale that enters the source's proof of `epsilon_n\asymp1/n`. This section shows that route is impossible without additional **inter-time reachability information**.

Let `X` be any critical law on `Z_+`, with probabilities `p_k`. The critical identity is equivalent to

\[
\boxed{
p_0=\sum_{k\ge1}B_kp_k,
\qquad
B_k:=\bigl((m-1)k-1\bigr)m^k.
}
\tag{6.1}
\]

Indeed this is just

\[
(m-1)\sum_{k\ge1}km^kp_k
=p_0+\sum_{k\ge1}m^kp_k.
\]

### Family A: survival much larger than `epsilon^2`

Put

\[
B_1=m(m-2).
\]

Fix any `c>0`. For all sufficiently large integers `K`, let

\[
q_K:=\frac cK,
\tag{6.2}
\]

\[
r_K:=\frac{1-(1+B_1)q_K}{B_K-B_1},
\tag{6.3}
\]

and define a law supported on `{0,1,K}` by

\[
p_K=r_K,\qquad p_1=q_K-r_K,\qquad p_0=1-q_K.
\tag{6.4}
\]

For sufficiently large `K`, all three probabilities are nonnegative. By construction,

\[
B_1p_1+B_Kp_K
=B_1q_K+(B_K-B_1)r_K
=1-q_K=p_0,
\]

so the law is exactly critical.

Its critical excess is

\[
\epsilon_K:=\mathbf E[m^X]-1
=(m-1)q_K+(m^K-m)r_K.
\tag{6.5}
\]

Since

\[
r_K\sim\frac{1}{(m-1)Km^K},
\]

we obtain

\[
\boxed{
\epsilon_K
\sim
\frac{(m-1)c+1/(m-1)}{K}.
}
\tag{6.6}
\]

Therefore

\[
\boxed{
\frac{q_K}{\epsilon_K^2}\asymp K\longrightarrow\infty.
}
\tag{6.7}
\]

Every member of this family has finite support, hence satisfies every weighted moment finiteness condition separately.

To compare with the source's third-derivative scale, define the same aggregate used in its finite-third-moment argument,

\[
D(m)
=m(m-1)G'''(m)+(4m-5)G''(m)
+\frac{2(m-2)}{m^2(m-1)}G(m).
\tag{6.8}
\]

For the family (6.4), the `K` atom dominates the third derivative:

\[
G'''(m)
=K(K-1)(K-2)m^{K-3}r_K,
\]

so

\[
\boxed{D(m)\sim \frac{K^2}{m^2}.}
\tag{6.9}
\]

Thus `epsilon_K \asymp D(m)^{-1/2}`, the same coarse one-time scaling appearing in the source's regularity estimates, while survival is much larger than `epsilon_K^2`.

### Family B: survival exponentially smaller than `epsilon^2`

Now take the exactly critical two-point law supported on `{0,K}`:

\[
p_K=\frac1{B_K+1},
\qquad
p_0=\frac{B_K}{B_K+1}.
\tag{6.10}
\]

Then

\[
q_K=p_K
\sim\frac1{(m-1)Km^K},
\tag{6.11}
\]

while

\[
\epsilon_K=(m^K-1)p_K
\sim\frac1{(m-1)K}
\tag{6.12}
\]

and again

\[
D(m)\sim\frac{K^2}{m^2}.
\tag{6.13}
\]

Consequently

\[
\boxed{
\frac{q_K}{\epsilon_K^2}\longrightarrow0
}
\tag{6.14}
\]

indeed exponentially fast.

### Extremal conclusion

Families A and B are both exactly critical, finite-support, finite-third-weighted-moment laws. They have the same coarse one-time scales

\[
\epsilon\asymp K^{-1},
\qquad
D(m)\asymp K^2,
\]

but their survival probabilities range from order `K^{-1}` to order `K^{-1}m^{-K}`. Hence:

\[
\boxed{
\text{criticality plus the one-time scales }\epsilon\asymp D^{-1/2}
\text{ cannot force }q\asymp\epsilon^2.
}
\tag{6.15}
\]

This does **not** refute a dynamic theorem for an actual trajectory with constants depending on its initial law. It refutes a whole proof strategy: no uniform anti-dip argument based only on a single-time critical identity and those moment scales can work. The missing ingredient must encode **dynamic reachability from the previous or next iterate**.

That is useful negative information: it prevents another run from trying to close the pointwise survival constant by sharpening only static Hölder/Cauchy--Schwarz inequalities at time `n`.

## 7. What the three methods jointly say

The repaired finite-third-moment regime now has two complementary facts:

1. **Dynamic dissipation is strongly constrained.** The exact monotone tail potential satisfies
   \[
   \Sigma_N=\sum_{n\ge N}\sigma_n
   =\epsilon_N+\sum_{n\ge N}h_m(\epsilon_n)
   \asymp N^{-1},
   \]
   and `sigma_n \asymp q_n`. Macroscopic downward jumps of `epsilon_n` occur only `O(1)` times per dyadic scale.
2. **Static geometry is far too flexible.** At one fixed time, even finite-support critical laws with matching `epsilon` and third-derivative scales can have `q/epsilon^2` tending to `0` or to `infinity`.

Therefore the CEGM smoothness gap has been localized one scale further. The remaining obligation is not a generic moment estimate. It is a **dynamic Tauberian/hazard theorem** showing that the discrete mass

\[
\sigma_N=\Sigma_N-\Sigma_{N+1}
\]

cannot concentrate or evacuate on sparse sets at the natural `N^{-2}` scale along a reachable critical Derrida--Retaux trajectory.

Equivalently, one wants enough local regularity to upgrade

\[
\Sigma_N\asymp N^{-1}
\]

to a pointwise derivative asymptotic for `sigma_N`, ultimately giving

\[
q_N\sim \frac{4}{(m-1)^2N^2}
\]

and then `q_{N+1}/q_N->1`, which the previous exact conditioned-law identity converts into the geometric Yaglom law.

The static extremizers in Section 6 show why this must use at least two consecutive iterates, a spine/pivotal representation, or another true reachability constraint.

## 8. Validation / checking budget

This run contains no finite exhaustive claim and therefore no checker-only artifact was manufactured. The new claims are symbolic identities and asymptotic families valid for arbitrary `K`; their algebra is written on the page.

Self-checks performed:

- substituted (3.3)--(3.4) back into the exact generating-function recursion at `s=m`;
- checked both inequalities in (3.7);
- telescoped (3.6) over a finite interval before taking the limit;
- checked exact criticality of both finite-support extremal families by (6.1);
- separated the owner-proof source refutation from the repaired finite-third-moment question;
- did not promote bounded negative literature search to a novelty certificate.

These are self-checks, not independent audits.

## 9. Audit status and next run

Independent D0057 source-level audits remain

`0/2`.

The newest neighboring R02 package is not a complete neighboring closure package, so no second-audit work was appropriate. No audit was simulated.

The fixed metric has now been unchanged for five consecutive post-movement runs. Under the CLOSABLE six-run rule, **one more complete unchanged run fires mandatory handoff/rotation**. Therefore the next run should not spend itself polishing C006--C008. Its three fresh methods are:

- **#9 RANDOMIZE:** expose a surviving/pivotal spine and ask whether the dissipation mass `sigma_n` is an occupation probability of a randomized marked trajectory whose hazard has a martingale or mixing constraint;
- **#16 COMPUTE EVERY SMALL CASE:** only if it tests a concrete dynamic conjecture, enumerate exact finite-support iterates to search for a two-step inequality controlling `sigma_{n+1}/sigma_n`; archive a checker only if such a finite claim is actually made;
- **#25 COUNT THE SAME THING TWICE:** double-count pivotal/open-path witnesses against the exact dissipation `sigma_n` to seek the missing two-time reachability inequality.

If these do not move the source-level metric/closure state on that sixth unchanged run, R01 must leave a complete handoff and rotate rather than begin a seventh attack.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R01
  active_source: D0057
  source_title: "A max-type recursive model: some properties and open questions"
  source_target: "deterministic-m critical conditional geometric limit"
  predecessor_I0024:
    status: "FROZEN / internally closed at C=1; not reopened"
  metric:
    name: E_geom
    before: 1
    after: 1
  source_status: "REFUTED at owner-proof level / NOT CLOSED"
  audits:
    required: 2
    present: 0
    ids: []
  unchanged_count:
    before: 4
    after: 5
  tried_moves:
    - 13
    - 24
    - 30
  movement: "no fixed-metric movement"
  new_evidence:
    - "C006 exact monotone potential M_N with increment h_m(epsilon_N)"
    - "C007 exact tail identity Sigma_N = epsilon_N + sum_{n>=N} h_m(epsilon_n)"
    - "under finite third weighted moment: sum_{n>=N} q_n asymp 1/N"
    - "C008 dyadic density control and O(1) macroscopic downward shocks per scale"
    - "two exact finite-support critical extremal families show q/epsilon^2 can tend to infinity or zero at matching epsilon,D scales"
  remaining_obligation: >-
    Literal D0057 needs two independent source-level audits for protocol closure.
    The natural repaired finite-third-moment problem needs a genuinely dynamic
    two-time/spine/pivotal inequality controlling dissipation at the 1/n^2 scale;
    static one-time critical moment geometry is insufficient.
  next_moves:
    - 9
    - 16
    - 25
  next_gate: "sixth unchanged run => mandatory CLOSABLE handoff/rotation unless closure state moves"
```

## 11. Delivery boundaries

One immutable R01 report only. No root/shared ledger, claim, neighboring-track file, scheduler setting, Gmail/email, Drive object, public post, purchase, permission, or task state was modified. No receipt-only follow-up commit is authorized or needed.
