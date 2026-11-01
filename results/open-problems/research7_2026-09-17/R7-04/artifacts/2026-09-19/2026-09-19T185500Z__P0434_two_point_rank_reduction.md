Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0434 — exact two-point M-SERPT/Gittins rank reduction

Target: Scully--Harchol-Balter--Scheller-Wolf (2020), Conjecture 8.1: the all-load M/G/1 approximation ratio of M-SERPT relative to optimal Gittins is 2. Harchol-Balter (2021), Section 7.1.2, asks whether the credited factor 5 can be improved.

This artifact does **not** solve the source conjecture. It proves an exact finite-support structural theorem that reduces the complete two-point case to a one-threshold feedback comparison and identifies a nontrivial region where the two policies are sample-path identical.

## Setup

Let

`P(X=a)=p`, `P(X=b)=q=1-p`, with `0<a<b`,

and put

`d=b-a`, `m=E[X]=a+q d`.

Jobs arrive as in the source M/G/1 model, but the rank calculations below are load-independent. Lower rank means higher priority and ties are FCFS, as in the source SOAP convention.

For a job of age `t`, the Gittins rank can equivalently be written

`r_G(t)=inf_{Delta>0} E[min(X-t,Delta) | X>t] / P(X-t<=Delta | X>t)`.

SERPT has rank `r_S(t)=E[X-t|X>t]`, and M-SERPT has the nondecreasing envelope `r_MS(t)=max_{0<=u<=t} r_S(u)`.

## B2 — attack the negation first: solve the complete two-point rank geometry

### Lemma 1 (exact Gittins rank)

For `0<=t<a`,

`r_G(t)=min{(a-t)/p, m-t}`,

while for `a<=t<b`,

`r_G(t)=b-t`.

### Proof

Fix `t<a`. Conditional on survival to age `t`, the residual size is

- `a-t` with probability `p`,
- `b-t` with probability `q`.

If `Delta<a-t`, completion probability by `Delta` is zero, so this stopping horizon is inadmissible/infinite in the rank ratio.

If `a-t<=Delta<b-t`, the completion probability is `p` and

`E[min(X-t,Delta)]=p(a-t)+q Delta`.

Therefore the ratio is

`[(p(a-t)+q Delta)]/p`,

which is strictly increasing in `Delta`; its minimum on this interval occurs at `Delta=a-t` and equals `(a-t)/p`.

If `Delta>=b-t`, every surviving job completes and the smallest numerator is obtained at `Delta=b-t`, giving `m-t`.

Taking the better of the only two candidate stopping horizons proves the first formula. If `a<=t<b`, survival reveals that the job has deterministic residual size `b-t`, so the Gittins rank is exactly `b-t`. QED.

### Lemma 2 (exact M-SERPT rank)

For `0<=t<a`, `r_S(t)=m-t`. For `a<=t<b`, `r_S(t)=b-t`. Hence

`r_MS(t)=m` for `0<=t<a`,

and

`r_MS(t)=max{m,d}` for `a<=t<b`.

Moreover,

`d<=m  <=>  p d<=a`,

and

`d>m  <=>  p d>a`.

### Proof

The SERPT formulas are the conditional residual means. Before age `a`, `m-t` decreases from `m`; at age `a` the rank jumps to `d` and then decreases. Its increasing envelope is therefore `m` before `a` and `max(m,d)` thereafter. Since `m=a+q d`,

`d-m = p d-a`,

which proves the equivalences. QED.

## B18 — translate the statement: the two-point problem is a phase-priority problem

The scalar

`theta := p(b-a)/a = p d/a`

completely determines the qualitative rank geometry.

### Theorem 3 (subcritical gap: exact policy equality)

If `theta<=1` (equivalently `p(b-a)<=a`), then **M-SERPT and Gittins are sample-path identical and both equal FCFS**. Consequently, for every stable load,

`E[T_MS]=E[T_G]`

for this two-point distribution.

### Proof

By Lemma 2, `r_MS(t)=m` for every possible attained age, so M-SERPT is FCFS under the source tie rule.

For Gittins, a fresh job has

`r_G(0)=min{a/p,m}=m`,

because `p d<=a` is equivalent to `a/p>=m`:

`a/p>=m`
`<=> a>=p(a+q d)`
`<=> q a>=p q d`
`<=> a>=p d`.

For every `0<t<a`, Lemma 1 gives `r_G(t)<=m-t<m`. At age `a`, the revealed long job has rank `d<=m`, and thereafter its rank `b-t` only decreases. Therefore, once Gittins begins serving a job, that job's rank never becomes worse than the rank `m` of any fresh waiting arrival. By induction over service completions, no later arrival can preempt the currently served job. Hence Gittins serves jobs to completion in arrival order, exactly FCFS. QED.

This is an all-load theorem, not a light-traffic or finite-horizon diagnostic.

### Theorem 4 (supercritical gap: exact H-L-H versus H-L reduction)

If `theta>1` (equivalently `p d>a`), define

`c := b-a/p`.

Then `a<c<b`. M-SERPT and Gittins have the following exact phase interpretation.

**M-SERPT:**

- phase `H0=[0,a)`: high priority;
- phase `L=[a,b)`: low priority.

Every job is served continuously through `H0`; if it survives to age `a`, it is demoted and its entire residual `d` is served only when no `H0` work is present. Low-phase jobs are FCFS in demotion order.

**Gittins:**

- phase `H0=[0,a)`: high priority;
- phase `L=[a,c)`: low priority;
- phase `H1=[c,b)`: high priority.

The middle low phase has length

`c-a = d-a/p = a(theta-1)/p`,

and the terminal rescued phase has length

`b-c = a/p`.

Thus, on every two-point law where the policies can differ, their **only** structural difference is that Gittins promotes the final `a/p` units of a long job back above fresh work, whereas M-SERPT leaves the whole residual `d` below fresh work.

### Proof

Because `p d>a`, we have `a/p<m`. For `t<a`, compare the two candidates from Lemma 1. At `t=0`, `(a/p)<m`, and

`[(a-t)/p]-(m-t) = (a/p-m) - (q/p)t <0`,

so throughout `[0,a)`,

`r_G(t)=(a-t)/p`.

This decreases as the job is served, so a job in its initial phase cannot be preempted by a fresh job of rank `a/p`.

At age `a`, its rank jumps to `d`. The condition `p d>a` is exactly `d>a/p`, so any fresh work has higher priority. For `t>=a`, Lemma 1 gives `r_G(t)=b-t`. This exceeds the fresh rank `a/p` precisely when

`t < b-a/p = c`,

and falls below it precisely when `t>c`. Hence `[a,c)` is low priority and `[c,b)` is terminal high priority. Once a low-phase job receives service, its rank decreases; no newly demoted low job can overtake it. Once it reaches `c`, its rank is no worse than a fresh job and thereafter strictly improves, so it completes without being preempted by fresh work.

For M-SERPT, Lemma 2 gives young rank `m` and old rank `d`, with `d>m`, so all `[0,a)` work strictly outranks every `[a,b)` residual. Ties within the residual class are FCFS. QED.

## B25 — constructive coupling / bijection consequence

The preceding theorem yields an explicit pathwise encoding. Replace each original job by deterministic service phases:

- every arrival contributes an `H0` phase of length `a`;
- independently, with probability `q`, it contributes a continuation of total length `d`.

When `theta<=1`, both policies simply concatenate each continuation to its own `H0` phase and the arrival-order service path is identical.

When `theta>1`, split a long continuation as

`d = (d-a/p) + a/p`.

M-SERPT labels both pieces low. Gittins labels the first piece low and the last piece high. This is a deterministic bijection between an original two-point job trajectory and a two- or three-phase feedback trajectory; no approximation, simulation, or queue-length limiting argument is involved.

### Corollary 5 (where a two-point counterexample must live)

Any two-point distribution that witnesses a strict M-SERPT/Gittins mean-response gap must satisfy

`p(b-a)>a`.

In that region the source conjecture restricted to two support points is exactly the comparison between the two feedback disciplines above. The complete two-point search can therefore be normalized by `a=1` and reduced to the three dimensionless parameters

`p in (0,1)`, `theta>1`, and load `rho in (0,1)`.

This reduction does **not** prove that two-point laws have approximation ratio at most 2, nor that the source's known three-point near-2 construction has minimal support. Those are open consequences to test next.

## Relation to recovered source work

The source 2020 paper proves the universal interval

`2 <= sup E[T_MS]/E[T_G] <= 5`

and its lower construction uses three support points. The repository's earlier P0434 intake attempt only gave a finite two-job example illustrating why expected residual size misses Gittins' probing option; it did not characterize the stationary two-point M/G/1 policies. The rank-phase theorem above is therefore a genuine new internal reduction relative to the recovered repository history, but **no novelty claim is made** without a dedicated literature review.

## Frozen metric / status

Frozen source metric before: `W_MS=5-2=3`.

Frozen source metric after: `W_MS=3` — **NO MOVEMENT**, because the theorem is restricted to two-point distributions and supplies neither a universal upper bound below 5 nor a source-valid ratio above 2.

Status: **OPEN / PARTIAL**.

Next attack should derive an exact stationary mean-response formula or a certified global bound for the normalized supercritical two-point phase model before moving to three/four support points. A numerical grid alone is not enough.