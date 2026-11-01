Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this is not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric `B_R13(n)`; explicit finite obstruction MOVED: `K_6^* >= 36907093/20000000 = 1.84535465`, hence the same lower bound holds for every exact column count `n>=6` by zero padding. Methods actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY; #7 TAKE THE LIMIT; #26 HUNT THE SPORADIC CASE.**

# R13 — Boolean Komlos: an exact six-column rational obstruction at 1.84535465

Run ID: `20260917T1903Z_n6-rational-obstruction-3b7e`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, policy, source scope

The target remains the real Boolean Komlos signing problem. For a real `m x n` matrix `A` whose columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

R13's fixed tracked quantity is the complete rigorously certified **upper** envelope `B_R13(n)`. I did not replace that metric by a lower-bound quantity. The owner also gave this particular hard track an explicit continuation condition: retain it while a source-matching upper bound **or an explicit finite obstruction** can move. This run moves the latter.

Before research I reread/recovered the required current repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042/Bandeira Komlos intake entry, the newest complete R13 report, and current adjacent sign-matrix discrepancy ownership/search state. The current queue continues to reserve Boolean Komlos to R13; I did not edit shared roots, claims, peer tracks or scheduler state.

The newest complete R13 report before this one is

`runs/R13/20260917T1742Z_k5-template-ceiling-recovery2-5f8c.md`.

It is `STUCK_RECOVERY_2` for the five-column route. It proves that every at-most-five-row **full-alignment** clause-template construction at `n=5` has lower-bound ceiling

\[
T=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
 =1.79244719148\ldots,
\]

attained by the preceding exact matrix `A_*`; beating `T` at five columns would require genuine partial-alignment threshold cells. I do **not** add another lemma to that exhausted blocker in this run.

The fixed upper envelope remains

\[
B_{R13}(1)=1,
\quad B_{R13}(2)=\sqrt2,
\quad B_{R13}(3)=\frac{\sqrt{11}+\sqrt2}{3},
\quad B_{R13}(4)=\sqrt3,
\]

\[
B_{R13}(n)\le
\min\left\{
\sqrt{\frac{3n}{4}},
\left(\sqrt2+\frac12\right)\sqrt{\left\lceil\frac n5\right\rceil}
\right\},
\qquad 5\le n\le75,
\]

and Guo--Fang--Lu gives the current dimension-free real-Boolean certificate

\[
B_{R13}(n)<3\sqrt{2\pi},\qquad n\ge76.
\]

Thus the official upper metric is unchanged again. The same five-column blocker is not being recycled, however: the explicit finite obstruction itself moves to a strictly larger value at `n=6`.

## 2. Fresh source/prior-art check, 17 September 2026

The dated source picture remains:

1. Nikhil Bansal and Haotian Jiang, arXiv:`2508.03961v2`, give the earlier full real-Boolean `\widetilde O((\log n)^{1/4})` Komlos bound.
2. Eren Ercan, arXiv:`2609.08885`, gives an explicit `(log n)^{1/4}`-type Boolean bound with coefficient `2395` plus the final `2sqrt2` rounding term.
3. Shengtao Guo, Ethan X. Fang and Junwei Lu, arXiv:`2609.11189v1`, submitted 10 September 2026, state the unrestricted real-Boolean theorem with universal constant `3sqrt(2pi)`. The current search again found the September 10/11 surface and no correction or withdrawal.
4. Nestor Guillen and Vladimir Kobzar, arXiv:`2609.15071`, allow unit-complex phases / rank-two vector colorings and are not a substitute for Boolean signs.
5. Dmitriy Kunisky's 2023 unsatisfiable-matrix/SOCP framework already supplies much stronger **asymptotic universal** lower bounds, approaching `1+sqrt2`. The result below is therefore not a new universal lower record. Its content is a concrete exact small-`n` obstruction.
6. Targeted current searches for `Komlos n=6`, `six vectors`, the decimal `1.84535463/65`, and the exact rational below did not locate a matching finite-six certificate. A negative search is not a novelty certificate; novelty of this finite instance remains **UNVERIFIED**.

The 2024 Belhaouari--AlQudah paper was also rechecked in search results. Its advertised five-dimensional value was already refuted exactly by the preceding R13 matrix. I found no reliable source basis in this run for attributing a particular exact `K(6)` value to that paper, so I make no such claim.

## 3. Why the method triple changed

The preceding report proposed #15,#27,#30. R13 history had already used #27 and #30 earlier. The owner asks each run to get out of the box rather than recycle an exhausted triple, so I instead used the three remaining section-B moves not previously represented in the R13 history: **#4, #7, #26**.

### #26 HUNT THE SPORADIC CASE

The five-column partial-alignment optimization is now a large global threshold-cell problem. Rather than spend a third recovery on it, I asked whether the immediately adjacent sporadic dimension `n=6` has a stronger explicit obstruction. A broad numerical search over normalized `6 x 6` matrices found a stable value near `1.84535`, strictly above the five-column obstruction `T`.

The important point was not the decimal. The optimizer repeatedly collapsed to the same sparse two-row-type pattern, which can be written with only five positive magnitudes.

### #7 TAKE THE LIMIT

For discovery only, consider the continuous family

\[
A(a,e,f,g,d)=
\begin{pmatrix}
-a&d&0&-e&0&-a\\
a&0&e&0&d&-a\\
0&0&-f&f&0&-g\\
a&d&0&e&0&a\\
-a&0&-e&0&d&a\\
-g&0&f&f&0&0
\end{pmatrix}.
\tag{3.1}
\]

The saturated column conditions are

\[
4a^2+g^2=1,\qquad 2d^2=1,\qquad e^2+f^2=\frac12.
\tag{3.2}
\]

Four rows have `l1` norm

\[
L_A=2a+d+e,
\]

and two rows have

\[
L_B=2f+g.
\]

The Boolean sign-cover pattern depends only on the signs/supports, not on these positive magnitudes. Numerically maximizing `min(L_A,L_B)` inside (3.2) equalizes the two row types. At an interior stationary point one obtains `eg=af`; writing `r=a/g=e/f` gives the diagnostic polynomial

\[
64r^8-256r^7+288r^6-192r^5+340r^4-192r^3+60r^2-40r+7=0,
\]

with relevant root `r≈0.6064574866229` and continuous value

\[
L_A=L_B\approx1.8453546509671987.
\]

I do **not** claim here that this polynomial root is a globally optimal six-column Komlos obstruction, or even the globally optimal member of every possible six-row support pattern. It was used only as the limiting target for rationalization.

Taking rational lattice approximants with denominator tending to infinity produced a particularly clean denominator-`10^9` point at which the two row types equalize **exactly in integer arithmetic**. That is the theorem-sized finite output.

## 4. #4 PROVE SOMETHING WEAKER, COMPLETELY — exact rational six-column obstruction

Let

\[
D=10^9,
\]

and define the integer matrix

\[
M=
\begin{pmatrix}
-385788865&707106781&0&-366670139&0&-385788865\\
 385788865&0&366670139&0&707106781&-385788865\\
0&0&-604609799&604609799&0&-636135052\\
385788865&707106781&0&366670139&0&385788865\\
-385788865&0&-366670139&0&707106781&385788865\\
-636135052&0&604609799&604609799&0&0
\end{pmatrix}.
\tag{4.1}
\]

Set

\[
A_6=D^{-1}M.
\]

Define

\[
Q=\frac{1845354650}{10^9}
 =\boxed{\frac{36907093}{20000000}}
 =\boxed{1.84535465}.
\tag{4.2}
\]

### 4.1 Exact column-norm check

The six squared column-norm numerators are

\[
\begin{aligned}
&999999997814995604,\\
&999999999472363922,\\
&999999999762199444,\\
&999999999762199444,\\
&999999999472363922,\\
&999999997814995604.
\end{aligned}
\]

Each is strictly below

\[
D^2=10^{18}.
\]

Therefore every column of `A_6` has Euclidean norm strictly less than one, so this is an admissible real Boolean Komlos instance.

### 4.2 Every row has the same exact `l1` norm

The integer identities are

\[
2(385788865)+707106781+366670139
 =1845354650,
\]

and

\[
2(604609799)+636135052
 =1845354650.
\]

Hence all six rows of `A_6` have `l1` norm exactly `Q`. Consequently, for every Boolean signing,

\[
\|A_6\varepsilon\|_\infty\le Q.
\tag{4.3}
\]

### 4.3 Exact exhaustive lower check

There are only `2^6=64` Boolean signings. The exact integer checker evaluates all of them. For **every one of the 64 signings**, the infinity-norm numerator is exactly

\[
1845354650.
\]

The witness-row incidence counts are

\[
(8,8,16,8,8,16),
\]

so every signing fully saturates at least one row. Thus (4.3) is equality for every signing:

\[
\boxed{
\|A_6\varepsilon\|_\infty=Q
\quad\text{for every }\varepsilon\in\{\pm1\}^6.
}
\tag{4.4}
\]

In particular

\[
\boxed{
\operatorname{disc}(A_6)=Q
=\frac{36907093}{20000000}
=1.84535465.
}
\tag{4.5}
\]

Therefore

\[
\boxed{K_6^*\ge1.84535465.}
\tag{R13-C36}
\]

By appending zero columns, the same statement immediately gives

\[
\boxed{K_n^*\ge1.84535465\qquad(n\ge6).}
\tag{4.6}
\]

This padding statement is only a finite lower obstruction. It is not competitive with Kunisky's asymptotic universal lower record, and it does not change the upper-envelope `B_R13(n)`.

## 5. Exact comparison with the preceding five-column obstruction

No floating-point comparison is needed. For the preceding

\[
T=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\]

use the elementary rational bounds

\[
\sqrt2<\frac{71}{50},\qquad
\sqrt3<\frac{87}{50},\qquad
\sqrt6<\frac{49}{20},
\]

and

\[
\sqrt{51+3\sqrt6}<\frac{191}{25}.
\]

The checker verifies each squared comparison exactly. Hence

\[
T<\frac{1167}{650}<\frac95.
\]

On the other hand

\[
Q=\frac{36907093}{20000000}>\frac95.
\]

Thus

\[
\boxed{T<Q}
\]

with a fully rational separation. The best explicit small-`n` obstruction on the R13 record therefore moves from `n=5`, `1.792447...`, to `n=6`, `1.84535465`.

## 6. Exact checker and archived execution

The exact checker is

`artifacts/R13/20260917T1903Z_n6-rational-obstruction-3b7e_checker.py`

created at commit

`8f3797a30b924c1964d14d0303204b7692a201ba`.

It uses only Python integer arithmetic and `Fraction`; it checks the six column energies, row `l1` identities, all 64 Boolean signings, the exact discrepancy, and the exact inequality chain separating the new obstruction from `T`.

I executed that checker before archival. The archived output is

`artifacts/R13/20260917T1903Z_n6-rational-obstruction-3b7e_output.txt`

at commit

`24730ad6ff6e5cdd9aaca5db8497b75390c91989`.

It terminates

`R13_N6_RATIONAL_OBSTRUCTION_EXACT_PASS`

and records

`maxima_distribution = {1845354650: 64}`.

Both artifacts were read back at their actual creation commits. These are **self-checks**, not independent outside audits.

## 7. Failed/negative routes this run

The discovery work also tested routes that did not produce a claim:

- A large perturbative search around the five-column extremizer `A_*` did not find any five-column matrix above `T`; this is diagnostic only and does not prove local or global optimality.
- Smooth optimization of unconstrained square matrices did not produce a rigorous five-column improvement.
- I explored a possible `K_5^*<1.9` upper proof through weighted downward ideals of bad Boolean sign classes. The numerical shape set is small, but I do not yet have an exact global classification plus column-energy certificate, so no upper claim is made.

Those failures are why the run moved to the adjacent sporadic `n=6` obstruction rather than filing another five-column auxiliary lemma.

## 8. Status and continuation discipline

The fixed upper envelope has not changed; its supported unchanged count increases by one. The two same-blocker five-column recovery cycles are **exhausted** and are not reopened by this result. This run is nevertheless not a third failed recovery because the owner's R13-specific continuation condition was met by a genuinely stronger explicit finite obstruction with an exact certificate.

The next run must not return to the old five-column full-alignment ceiling or merely add a checker to it. Productive continuations are now sharply limited to one of:

1. improve the actual upper envelope `B_R13(n)`;
2. find an explicit finite obstruction strictly above `36907093/20000000`, preferably at `n=6` or the next sporadic dimension;
3. turn the six-row continuous family into a **global** exact optimization theorem rather than another local/stationary calculation;
4. if none of these moves, write the hard-target handoff and rotate to an eligible outside source rather than accumulating same-step lemmas.

Status: **PARTIAL / fixed upper metric unchanged / explicit finite obstruction moved / exact self-check PASS / finite-six novelty UNVERIFIED / outside audit pending**.

## 9. Runtime/model-control status

The scheduler/runtime control limitation is still real. The exposed automation update surface permits task title/prompt/schedule/enablement/timing controls but exposes **no native model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` is a prompt request, not authenticated telemetry, and this report does not claim it ran.

The repository's current `RESULTS.md` adds an important correction to the older P26 permission note: P26's full native update later **succeeded in an authorized P/C context**, so the historical `You cannot modify this task` result was context/ownership-specific rather than an immutable property of that job. The same ledger records that R-series edits were denied from that P/C context. The legitimate remedy for a denied task is therefore the authorized owner/workspace task context, or platform support exposing the required controls — not duplication, permission bypass or a repository-only edit. No scheduler modification was attempted in this run.

```yaml
ledger_delta:
  track: R13
  source: "Boolean Komlos; current navigation Bansal-Jiang arXiv:2508.03961v2; Guo-Fang-Lu arXiv:2609.11189v1"
  target: "complete real Boolean unit-column discrepancy upper envelope B_R13(n)"
  fixed_metric_before: "B_R13(1)=1; B_R13(2)=sqrt2; B_R13(3)=(sqrt11+sqrt2)/3; B_R13(4)=sqrt3; B_R13(n)<=min(sqrt(3n/4),(sqrt2+1/2)sqrt(ceil(n/5))) for 5<=n<=75; B_R13(n)<3sqrt(2pi) for n>=76"
  fixed_metric_after: "unchanged"
  movement: "NO upper-metric movement"
  auxiliary_explicit_obstruction_before: "K_5^* >= (2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13 = 1.79244719148..."
  auxiliary_explicit_obstruction_after: "K_6^* >= 36907093/20000000 = 1.84535465; same lower bound for every n>=6 by zero padding"
  status: PARTIAL
  exact_check: PASS
  outside_audits_for_new_claim: 0
  novelty: UNVERIFIED
  five_column_recovery_cycles: 2
  five_column_same_blocker: "EXHAUSTED; do not reopen without genuine quantitative movement"
  methods_used: [4, 7, 26]
```
