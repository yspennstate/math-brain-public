Model actually ran: **GPT-5.6 Sol. Reasoning: UNVERIFIED by authenticated runtime metadata; GPT-6 / maximum was requested but is not verified. Metric moved `N_certified: 20 -> 21`. Section-B methods: #1 CHANGE THE CATEGORY, #3 PROVE SOMETHING STRONGER, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R05 — Aldous–Fill Open Problem 7.30 / I0030

Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity, source, scope, ownership, and frozen target

I continued from `runs/R05/20260917T032311Z_i0030_n20_stability_gap.md`. I did not restart the problem and did not alter the frozen graph class, continuous-time normalization, edge set covered, or fixed metric.

Before new research I re-read/rechecked the current controls and continuity state on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest R05 report above;
- the current R04 audit history and newest R04 handoff;
- the newest neighboring R06 report;
- exact repository searches for I0030 and for `P26-AUDIT-R05-I0030`.

`QUEUE.md` still assigns I0030 to R05. `POSTED.md` excludes the distinct Aldous–Fill 7.27 work but does not exclude 7.30. The intake/source mapping remains I0030 = Aldous–Fill Open Problem 7.30.

Primary source rechecked on 2026-09-17:
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch7.S3.html`.

Aldous–Fill Proposition 7.29 is explicitly for **continuous-time** random walk on a distance-regular graph and states, for fixed graph distance `d`, that `q(t,d)/q(t,0)` is nondecreasing in `t`. Open Problem 7.30 then asks:

> Does random walk on an arc-transitive graph have some monotonicity property stronger than that of Corollary 7.3?

The frozen R05 answer remains unchanged. For every finite simple connected arc-transitive `d`-regular graph,
\[
P=A/d,\qquad H_t=e^{t(P-I)},
\]
and every arc `x~y`,
\[
r_{xy}(t):=\frac{H_t(x,y)}{H_t(x,x)}
\]
is strictly increasing for finite `t>=0`, with `r(0)=0` and `r(t)->1`.

The retained proof is
\[
a(t)=H_t(x,x),\qquad b(t)=H_t(x,y),\qquad a'(t)=b(t)-a(t),
\]
hence
\[
r(t)=1+(\log a(t))'.
\]
If `L=I-P` and `nu_t` is the exponentially tilted local spectral law,
\[
r(t)=1-\mathbb E_{\nu_t}\lambda,\qquad
r'(t)=\operatorname{Var}_{\nu_t}(\lambda)>0.
\]

All thirty Section-B move numbers were exhausted once in the first cycle. This is therefore an honest second-cycle use of #1/#3/#23 in roles different from the preceding run's #18/#25/#13.

## 2. #1 CHANGE THE CATEGORY — transition-orbit symmetric chains

The graph proof is actually a special case of a chain statement which makes the mechanism more transparent.

Let `Q` be the generator of a finite irreducible **symmetric** continuous-time Markov chain on `n>1` states. Assume its automorphism group is transitive on the ordered pairs `(x,y)` for which `q_xy>0`. Equivalently, the positive-rate transition arcs form one automorphism orbit.

Arc transitivity of the support implies state transitivity. Every positive off-diagonal rate is therefore a common number `w`, every state has the same support degree `d`, and the common exit rate is
\[
c=dw=-q_{xx}>0.
\]
Let
\[
K_t=e^{tQ}.
\]
By transition-orbit symmetry there are common values
\[
a(t)=K_t(x,x),\qquad b(t)=K_t(x,y)\quad(q_{xy}>0).
\]
The heat equation gives
\[
a'(t)=\sum_z q_{xz}K_t(z,x)
      =-ca(t)+dw\,b(t)
      =c(b(t)-a(t)).
\]
Thus for every transition arc
\[
\boxed{
\frac{b(t)}{a(t)}
=1+\frac1c(\log a(t))'.
}
\tag{2.1}
\]

Because `-Q` is symmetric positive semidefinite, with local spectral measure `mu_x`,
\[
a(t)=\int e^{-t\lambda}\,d\mu_x(\lambda).
\]
Under the exponential tilt
\[
d\nu_t(\lambda)
=\frac{e^{-t\lambda}}{a(t)}\,d\mu_x(\lambda),
\]
(2.1) becomes
\[
\boxed{
r(t)=1-\frac1c\mathbb E_{\nu_t}\lambda,\qquad
r'(t)=\frac1c\operatorname{Var}_{\nu_t}(\lambda)>0.
}
\tag{2.2}
\]
Strictness holds because irreducibility on more than one state puts local spectral mass at `0` and also at positive spectrum.

So the source graph theorem is a transition-orbit theorem for symmetric CTMCs; the simple unweighted graph assumption is not the essential point. I label this auxiliary strengthening

`R05-I0030-TRANSITION-ORBIT-01: PROVED`.

This is a theorem-sized claim and the full proof is on the page. It does not change the frozen source target.

## 3. #3 PROVE SOMETHING STRONGER — a universal quantitative lower envelope

The same spectral representation gives a uniform quantitative strengthening depending only on the number of states.

Let
\[
m(t)=\mathbb E_{\nu_t}\lambda=c(1-r(t)).
\]
Since the chain is symmetric and irreducible, the stationary spectral projector is `J/n`; therefore the tilted spectral law has atom
\[
p(t):=\nu_t(\{0\})=\frac{1}{n\,a(t)}.
\]
As `a(t)=K_t(x,x)<=1`,
\[
p(t)\ge\frac1n.
\]

Condition on the event `lambda>0`. Jensen/Cauchy-Schwarz gives
\[
\mathbb E_{\nu_t}\lambda^2
\ge \frac{m(t)^2}{1-p(t)},
\]
hence
\[
\operatorname{Var}_{\nu_t}(\lambda)
\ge \frac{p(t)}{1-p(t)}m(t)^2
\ge \frac{m(t)^2}{n-1}.
\]
Using (2.2),
\[
\boxed{
r'(t)\ge \frac{c}{n-1}(1-r(t))^2.
}
\tag{3.1}
\]
Since `r(0)=0`,
\[
\frac{d}{dt}\frac1{1-r(t)}
=\frac{r'(t)}{(1-r(t))^2}
\ge\frac{c}{n-1},
\]
so
\[
\boxed{
r(t)\ge\frac{ct}{ct+n-1}.
}
\tag{3.2}
\]

For every nontrivial irreducible chain, `a(t)<1` for every `t>0`; hence `p(t)>1/n`, so the inequality is strict for every finite `t>0`:
\[
\boxed{
r(t)>\frac{ct}{ct+n-1}\qquad(t>0).
}
\tag{3.3}
\]

In the frozen graph normalization `Q=P-I`, the exit rate is `c=1`. Thus every source graph on `n` vertices satisfies
\[
\boxed{
\frac{H_t(x,y)}{H_t(x,x)}
>\frac{t}{t+n-1},\qquad x\sim y,\ t>0.
}
\tag{3.4}
\]

Combining this with the previous universal upper envelope gives the clean sandwich
\[
\boxed{
\frac{t}{t+n-1}
<
\frac{H_t(x,y)}{H_t(x,x)}
\le \tanh t.
}
\tag{3.5}
\]
The right-hand bound is sharp on `K_2`. The left-hand bound is a universal dimension-only comparison; it is not asserted sharp at a fixed positive time.

I label (3.2)--(3.4)

`R05-I0030-STATIONARY-ATOM-LOWER-02: PROVED`.

The only inequality input is conditional Jensen/Cauchy-Schwarz. I do not claim that ingredient as novel.

## 4. #23 DO WHAT THE PROPOSER DID NOT EXPECT — fixed-order extremizers reverse with time

The previous envelope result made complete graphs extremal after fixing the spectral ceiling `Lambda`. A tempting next guess is that a single familiar source graph might extremize the adjacent ratio for a **fixed number of vertices** at all times. The source class itself rules this out already for the two most natural candidates.

Fix `n>=4` and compare `C_n` and `K_n`, both source-valid arc-transitive graphs.

For any simple `d`-regular source graph,
\[
r'(0)=\operatorname{Var}_{\mu_x}(\lambda)=\frac1d.
\]
Therefore
\[
r'_{C_n}(0)=\frac12,\qquad
r'_{K_n}(0)=\frac1{n-1},
\]
and for all `n>=4`,
\[
r_{C_n}(t)>r_{K_n}(t)
\]
for all sufficiently small positive `t`.

At the other end, for a finite vertex-transitive graph let `gamma` be the smallest positive normalized-Laplacian eigenvalue and let `m_gamma` be its multiplicity. Because every spectral projector has constant positive diagonal,
\[
1-r(t)
\sim m_\gamma\,\gamma\,e^{-\gamma t}.
\tag{4.1}
\]
For the two graphs,
\[
\gamma(C_n)=1-\cos(2\pi/n),
\qquad
\gamma(K_n)=\frac{n}{n-1}.
\]
For every `n>=4`,
\[
1-\cos(2\pi/n)<\frac{n}{n-1}.
\]
Hence the cycle's defect from one decays strictly more slowly, and therefore
\[
r_{C_n}(t)<r_{K_n}(t)
\]
for all sufficiently large `t`.

By continuity the two source-valid curves cross at least once:
\[
\boxed{
\forall n\ge4,\quad
r_{C_n}-r_{K_n}
\text{ changes sign on }(0,\infty).
}
\tag{4.2}
\]

Thus the complete graph is neither a fixed-order all-time maximum nor a fixed-order all-time minimum relative even to the cycle. The fixed-`Lambda` extremal theorem from the prior run cannot be converted into a fixed-`n` extremal statement by simply dropping the spectral-ceiling constraint.

I label this exact source-valid obstruction

`R05-I0030-FIXED-N-EXTREMAL-REVERSAL-03: PROVED`.

## 5. Prior art / current literature

Fresh dated searches on 2026-09-17 included:

- exact `Open Problem 7.30` / `arc-transitive` / monotonicity queries;
- exact `H_t(x,y)/H_t(x,x)` queries with arc-/edge-transitive and transition-orbit terminology;
- `1-walk-regular heat kernel ratio`;
- current MNHD follow-ups around Regev--Shinkar, Price, Nica, Kubo--Namba, and Liu--Zhang;
- the dimension-only lower-envelope shape `t/(t+n-1)` with graph heat-kernel terms.

The primary Aldous--Fill source still displays Open Problem 7.30.

The current MNHD literature found remains the stronger **all-pairs** line. Liu--Zhang's 2025 Graphs and Combinatorics paper proves MNHD for a diameter-three distance-regular class and explicitly summarizes Regev--Shinkar's Cayley counterexample together with the positive Price/Nica/Kubo--Namba classes. Price proves the all-pairs statement for finite weighted Abelian Cayley graphs.

I did not locate an explicit published adjacent transition-orbit theorem, the stationary-atom lower envelope (3.2), or the cycle/complete fixed-order reversal packaged in this form. This is bounded negative evidence only. The proofs use elementary semigroup symmetry, spectral tilting and conditional variance, so publication novelty remains

`NOVELTY_UNVERIFIED`.

Access limit: public/indexed web and repository sources were checked; no subscription citation database was exhaustively reviewed.

## 6. Fixed metric: exact order-21 extension

The previous certified metric was
\[
N_{\rm certified}=20.
\]

For order 21 I again used the primary Conder connected symmetric (= arc-transitive) census rather than enumerating all labelled graphs. Its order-21 block contains exactly **13** classes, and the next block starts at order 22. The valencies are
\[
2,4,4,6,12,14,8,8,10,10,6,18,20.
\]
OEIS A286280 independently records `a(21)=13` connected arc-transitive graphs.

Only after freezing those 13 representatives did I run an exact/combinatorial certificate. It verifies:

- simplicity, connectivity, and the listed regular valency for every representative;
- pairwise non-isomorphism inside every repeated-valency class;
- constant diagonal and constant edge entries of `A^m` through `m=48`;
- the exact identity
  \[
  (A^{m+1})_{xx}=d(A^m)_{xy},\qquad x\sim y,
  \]
  through `m=48`;
- exact distance-regularity profiles and witnesses for every failure.

The certificate finds distance-regular classes
\[
1,3,6,9,10,12,13
\]
and **six** genuinely non-distance-regular source classes
\[
2,4,5,7,8,11.
\]
Thus the new coverage again includes cases outside Proposition 7.29.

Executed artifact:
- `artifacts/R05/20260917T041918Z_i0030_n21_exact.py`, create/read-back commit `8d7ccafc6c615441d75249bddf47b9d74c2a8acd`;
- `artifacts/R05/20260917T041918Z_i0030_n21_exact.out.txt`, create/read-back commit `af782bc3d3c9bc9a02a526a8f8862454108c99bf`.

The archived output ends
`metric_largest_fully_certified_vertex_count 21`
and
`RESULT PASS`.

Therefore
\[
\boxed{N_{\rm certified}:20\longrightarrow21.}
\]

## 7. Audit/closure state and neighboring reports

The source-matching C1 theorem retains the independent R04 verdict

`R04-AUDIT-R05-I0030-C1-20260916T130900Z: PASS_MATH / NOVELTY_UNVERIFIED`.

Later R04 checks are the same auditor and do not create a second independent source auditor.

A fresh exact repository search for `P26-AUDIT-R05-I0030` still returns only R05 reports recording that no such audit was found. Therefore the designated P26 source audit remains **PENDING**.

The newest R04 report is a retirement/handoff run on its own I0027 target and makes no new R05 claim. The newest R06 report is a mandatory stuck/thinking run on I0079 and explicitly makes no new theorem-sized claim. There is therefore no fresh neighboring theorem package that needs a new R05 audit in this invocation.

Accordingly the correct source status remains:

**PROVED mathematically / candidate positive answer to Aldous--Fill 7.30 / one independent source-level auditor / P26 audit pending / novelty UNVERIFIED / not repository-closed.**

No paper folder is created before the closure gate is met.

## 8. Model/scheduler escalation

The implementation limitation is unchanged. The exposed scheduler/task interface has prompt/title, schedule/timing, enabled-state and notification controls, but no per-task model-family selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` in prompt text is a request, not authenticated runtime configuration.

Actually fixing this requires explicit model and reasoning fields in the scheduler/backend or an authorized owner-facing UI, ideally with authenticated per-run applied-model telemetry.

The historical R-context attempt to modify P26 task ID
`6aa7b43682948191b697d72fec69d539`
returned `You cannot modify this task`. Current root state separately records that a later authorized P/C context successfully updated P26, so that denial is context/permission-specific rather than proof that P26 is globally immutable. The legitimate workaround is the authorized owner/P-C context or platform support; R05 does not bypass permissions and does not duplicate the task.

No scheduler, permission, email, Drive, public-posting, or shared-root mutation was performed in this run.

## 9. ledger_delta

```yaml
ledger_delta:
  worker: R05
  source: "David Aldous and James Fill, Reversible Markov Chains and Random Walks on Graphs (2002/2014), Open Problem 7.30 / I0030"
  frozen_target: "For every finite simple connected arc-transitive graph, rate-one CT SRW H_t=e^{t(P-I)}, and every arc x~y, H_t(x,y)/H_t(x,x) is strictly increasing for finite t>=0."
  metric: "largest vertex count through which every admissible graph in the frozen source class has been completely certified"
  before: 20
  after: 21
  movement: true
  unchanged_count: 0
  status: "PROVED_MATH / CANDIDATE_SOURCE_ANSWER / AUDIT_GATED / NOVELTY_UNVERIFIED"
  tried_moves:
    - 1
    - 3
    - 23
  new_claims:
    - "R05-I0030-TRANSITION-ORBIT-01: PROVED"
    - "R05-I0030-STATIONARY-ATOM-LOWER-02: PROVED"
    - "R05-I0030-FIXED-N-EXTREMAL-REVERSAL-03: PROVED"
  remaining_obligation: "Obtain an independent P26 end-to-end audit of the frozen source theorem and complete a deeper prior-art/novelty review before repository closure/publication."
  evidence:
    previous_report: "runs/R05/20260917T032311Z_i0030_n20_stability_gap.md"
    exact_checker: "artifacts/R05/20260917T041918Z_i0030_n21_exact.py"
    exact_checker_commit: "8d7ccafc6c615441d75249bddf47b9d74c2a8acd"
    exact_output: "artifacts/R05/20260917T041918Z_i0030_n21_exact.out.txt"
    exact_output_commit: "af782bc3d3c9bc9a02a526a8f8862454108c99bf"
    exact_output_result: "RESULT PASS"
  audits:
    - "R04-AUDIT-R05-I0030-C1-20260916T130900Z: PASS_MATH / NOVELTY_UNVERIFIED"
    - "P26-AUDIT-R05-I0030: NOT_FOUND / PENDING"
```
