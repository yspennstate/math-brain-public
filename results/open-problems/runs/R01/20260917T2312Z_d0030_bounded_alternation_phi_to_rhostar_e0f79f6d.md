Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector, so I do not claim GPT-6/maximum. **NO FIXED-METRIC MOVEMENT on active D0030: `E_phi_rho = 0 -> 0`; unchanged count `2 -> 3`; status `OPEN / PARTIAL / STUCK THRESHOLD REACHED FOR NEXT RUN`; methods #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.**

# R01 — D0030 / Bradley Question 2: bounded-alternation phi-to-rho-star theorem and the escape-to-infinite-alternation obstruction

Date: 2026-09-17 UTC / 2026-09-18 Asia/Jerusalem.

Lane: **CLOSABLE OUTSIDE**.

## 1. Continuity, ownership, exclusions, and repository state

I did **not** reopen Aldous–Fill I0024. Its internally established exact flow characterization remains frozen at `C=1`, with its preserved audit/history. I also did not reopen I0113, G0012, D0057, or the retired R01 FEI assignment; P03 owns FEI.

The active create-only R01 ownership claim remains `operations/claims/D0030.md`, status `CLAIMED / READY / CLOSABLE OUTSIDE`.

Before new research I reread/recovered the required repository state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/D0030.md`;
- intake record/attempt material for D0030, including `D0030-A001` under `probability_1000_intake_D_20260908/attempts.jsonl`;
- newest own report `runs/R01/20260917T2241Z_d0030_phi_regrouping_4e2b7c91.md`;
- newest neighboring R02/D0031 report `runs/R02/20260917T2204Z_a3f71c9d.md`;
- newest neighboring R7-01/D0033 report `research7_2026-09-17/R7-01/runs/2026-09-18/2026-09-17T220156Z__report.md`.

R02/D0031 remains `OPEN / PARTIAL / STUCK-RECOVERY-1 CONTINUATION`. R7-01/D0033 is a Markov-only `PROVED CANDIDATE / protocol closure open`, with its independent audits still missing in that report. Neither is a complete neighboring package eligible for R01's requested independent-audit budget, so I spent no audit budget.

## 2. Exact outside source and fresh current-status check

The source remains Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys **2** (2005), 107–144, arXiv `math/0511078`, Question 2, Section 2.3, printed p. 114 / PDF p. 8:

> If a given random sequence is phi-mixing, does it follow that it is rho-star-mixing?

The active claim preserves the full strictly stationary random-sequence scope. Markov, Gaussian, finite-memory, finite-alphabet, or bounded-alternation results are **PARTIAL** unless they decide the arbitrary-sequence source question.

Primary source re-read this run:

- https://arxiv.org/abs/math/0511078
- https://www2.stat.duke.edu/~scs/Projects/Stable/Conditions/BradleyStrongMixingSurvey2005.pdf

The source defines

\[
\phi(\mathcal A,\mathcal B)
=
\sup_{A\in\mathcal A,\,B\in\mathcal B,\,P(A)>0}
|P(B\mid A)-P(B)|
\]

and maximal correlation `rho`, and records Peligrad's inequality

\[
\rho(\mathcal A,\mathcal B)
\le
2\sqrt{\phi(\mathcal A,\mathcal B)\phi(\mathcal B,\mathcal A)}
\le
2\sqrt{\phi(\mathcal A,\mathcal B)}.
\tag{2.1}
\]

The same source explicitly says Question 2 remained unsolved there, with Bradley expecting YES and Walter Philipp expecting NO.

Fresh bounded searches on 2026-09-17 UTC / 2026-09-18 local used exact combinations of:

- `"If a given random sequence is phi-mixing, does it follow that it is rho*-mixing?"`;
- `"phi-mixing" "rho-star-mixing" sequence`;
- `"phi-mixing" "interlaced maximal correlation" Bradley`;
- Bradley later work on `rho`, `rho-prime`, `rho-star`, and random fields;
- strong-data-processing / maximal-correlation tensorization literature.

They recovered Bradley's 2005 source, his 2001 rho-mixing-but-not-rho-star Markov example, the 1997 lower-psi Markov positive theorem, the 2011 random-field dependence constructions, and later uses of the coefficients, but no paper explicitly claiming a source-matching arbitrary-sequence proof or counterexample. This is **bounded negative search evidence only**, not a worldwide openness or novelty certificate.

The most relevant neighboring literature shape remains Bradley's 2011 three-variable random-field gadget: it can make two sequential **rho** coefficients arbitrarily small while keeping a regrouped rho coefficient fixed. The previous R01 report asked whether a phi analogue exists. The theorem below shows that this exact local architecture cannot work with phi.

## 3. Frozen source metric

The metric remains

\[
E_{\phi,\rho^*}\in\{0,1\},
\]

with value `1` only after a rigorous universal proof or a fully verified strictly stationary phi-mixing counterexample with `limsup rho*(n)>0`.

This run proves a new bounded-alternation theorem but does **not** decide the unbounded interlaced supremum. Therefore

\[
\boxed{E_{\phi,\rho^*}=0\longrightarrow0.}
\]

This is the third consecutive complete D0030 run without fixed-metric movement, so the unchanged count is `2 -> 3`. Under Section I, the **next** D0030 invocation must be a thinking-only stuck/recovery run rather than another ordinary lemma run.

## 4. Idea before code

The previous run reduced a negative solution to a local three-variable question. For a triple `V=(V1,V2,V3)` it defined

\[
\delta_1
=\phi(\sigma(V_3),\sigma(V_1,V_2)),
\qquad
\delta_2
=\phi(\sigma(V_3,V_2),\sigma(V_1)),
\]

\[
R
=\rho(\sigma(V_1,V_3),\sigma(V_2)),
\]

and showed that if one could have `delta_1,delta_2 -> 0` while `R>=c>0`, a moving-window compiler would yield finite-range scale gadgets and then a full D0030 counterexample.

The exact denominator-10 search instead showed `R^2` on the same scale as `phi`, suggesting that the square-root conversion in Bradley/Peligrad's (2.1) is not merely a two-field coincidence.

The new idea is to **condition one chronological block at a time**. Conditioning can worsen the next one-sided phi coefficient, but only by an explicit factor. This yields a rigorous theorem for every fixed number of alternating blocks, and it identifies the only place a negative solution can escape: the number of alternations must diverge.

No code was written before this argument. The new claim is analytic/theorem-sized, so the validation obligation is the full proof on the page rather than another finite checker.

## 5. Method #17 — the square-root constant reappears under conditional peeling

### Lemma 5.1 — conditional phi after revealing one left block

Let `G_1,...,G_K` be sigma-fields in chronological order. Write

\[
H_i=\bigvee_{j\le i}G_j,
\qquad
K_i=\bigvee_{j>i}G_j.
\]

Assume

\[
\phi(H_i,K_i)\le\varepsilon
\qquad (1\le i<K).
\tag{5.1}
\]

Fix `i>=2`. If `D` is an atom of a finite sub-sigma-field of `G_1` with `P(D)>0`, then under the conditional law `P_D=P(.|D)`,

\[
\phi_{P_D}\!\left(igvee_{j=2}^{i}G_j,\ K_i\right)
\le2\varepsilon.
\tag{5.2}
\]

**Proof.** For an event

\[
B\in\bigvee_{j=2}^{i}G_j,
\qquad C\in K_i,
\qquad P(D\cap B)>0,
\]

we have `D cap B in H_i`. Hence (5.1) gives

\[
|P(C\mid D\cap B)-P(C)|\le\varepsilon.
\]

Also `D in G_1 subset H_1` and `C in K_i subset K_1`, so

\[
|P(C\mid D)-P(C)|\le\varepsilon.
\]

Subtracting,

\[
|P_D(C\mid B)-P_D(C)|
\le2\varepsilon.
\]

Taking the supremum proves (5.2). `square`

This is the exact mechanism behind the constants below: a one-cut phi bound survives one revealed chronological block, at the cost of at most a factor two.

## 6. Main theorem — arbitrary fixed alternation complexity

For `K>=2`, define the odd and even joins

\[
\mathcal O_K=\bigvee_{1\le j\le K,\ j\ \mathrm{odd}}G_j,
\qquad
\mathcal E_K=\bigvee_{1\le j\le K,\ j\ \mathrm{even}}G_j.
\]

### Theorem 6.1 — bounded-alternation phi-to-rho inequality

Under (5.1),

\[
\boxed{
\rho(\mathcal O_K,\mathcal E_K)^2
\le
\min\left\{1,\ 4\bigl(2^{K-1}-1\bigr)\varepsilon\right\}.
}
\tag{6.1}
\]

Equivalently,

\[
\rho(\mathcal O_K,\mathcal E_K)
\le
\min\left\{1,\ 2\sqrt{(2^{K-1}-1)\varepsilon}\right\}.
\tag{6.2}
\]

#### Proof

It is enough to prove the assertion when every `G_i` is finite. Indeed, for fixed finite `K`, the union of joins of finite sub-sigma-fields of the `G_i` is dense in the relevant `L^2` spaces; `phi` can only decrease when sigma-fields are restricted. Passing to `L^2` limits then gives the general case.

Let `r_K(epsilon)` be the supremum of the left side's maximal correlation over all finite ordered `K`-block systems satisfying (5.1).

For `K=2`, Bradley/Peligrad (2.1) gives

\[
r_2(\varepsilon)^2\le4\varepsilon,
\tag{6.3}
\]

which is (6.1).

Assume the claim for `K-1`. Let `g` be centered, `mathcal E_K`-measurable, and normalized by `||g||_2=1`. The squared norm of its orthogonal projection onto `L^2(mathcal O_K)` is the quantity whose supremum gives maximal correlation. Write

\[
M=E[g\mid\mathcal O_K],
\qquad
u=E[g\mid G_1],
\qquad
v=M-u.
\]

Since `E[v|G_1]=0`, the two terms are orthogonal:

\[
\|M\|_2^2=\|u\|_2^2+\|v\|_2^2.
\tag{6.4}
\]

Because `mathcal E_K subset K_1`, monotonicity and (2.1) give

\[
\|u\|_2^2
\le
\rho(G_1,\mathcal E_K)^2\|g\|_2^2
\le4\varepsilon.
\tag{6.5}
\]

Now condition on an atom `D` of `G_1`. Under `P_D`, the remaining ordered block system is

\[
G_2,G_3,\ldots,G_K.
\]

By Lemma 5.1 every one of its chronological prefix/suffix phi coefficients is at most `2 epsilon`. Its two alternating joins are precisely the original even join and the original odd join with `G_1` removed, with their names swapped; maximal correlation is symmetric, so the induction hypothesis applies.

On `D`, the function

\[
g_D:=g-E[g\mid G_1]
\]

is centered and measurable with respect to the appropriate alternating join. Also, the restriction of `v` to `D` is its conditional orthogonal projection onto the other alternating join. Hence

\[
E_D[v^2]
\le
r_{K-1}(2\varepsilon)^2\,\operatorname{Var}_D(g).
\]

Averaging over the atoms `D`,

\[
\|v\|_2^2
\le
r_{K-1}(2\varepsilon)^2 E[\operatorname{Var}(g\mid G_1)]
\le
r_{K-1}(2\varepsilon)^2.
\tag{6.6}
\]

Therefore

\[
r_K(\varepsilon)^2
\le
4\varepsilon+r_{K-1}(2\varepsilon)^2.
\tag{6.7}
\]

Using the induction hypothesis,

\[
4\varepsilon
+4(2^{K-2}-1)(2\varepsilon)
=
4(2^{K-1}-1)\varepsilon.
\]

Finally maximal correlation never exceeds one, proving (6.1). `square`

### A sharper three-block form

For three chronological fields `A,B,C`, set

\[
a=\phi(A,B\vee C),
\qquad
b=\phi(A\vee B,C).
\]

Repeating the first induction step while observing that

\[
\phi(A,C)\le\min\{a,b\}
\]

gives the nonuniform bound

\[
\boxed{
\rho(A\vee C,B)^2
\le
4\left(a+b+\min\{a,b\}\right).
}
\tag{6.8}
\]

Indeed the first projection onto `A` costs at most `4a`; conditioned on an atom of `A`, the `B`-to-`C` phi coefficient is at most `b+min(a,b)`, and another application of (2.1) gives the remaining term. The same finite-subfield approximation removes the finiteness assumption.

## 7. Consequence: the preceding three-variable counterexample compiler is impossible

Apply (6.8) to the previous run's triple in chronological order

\[
A=\sigma(V_3),\qquad B=\sigma(V_2),\qquad C=\sigma(V_1).
\]

Then `a=delta_1`, `b=delta_2`, and

\[
R^2
\le
4\left(\delta_1+\delta_2+\min\{\delta_1,\delta_2\}\right)
\le12\max\{\delta_1,\delta_2\}.
\tag{7.1}
\]

Recall the previous local extremal quantity

\[
\eta(c)
=
\inf_{R(V)\ge c}\max\{\delta_1(V),\delta_2(V)\}.
\]

Equation (7.1) proves

\[
\boxed{\eta(c)\ge c^2/12>0\qquad(c>0).}
\tag{7.2}
\]

Thus the entire previous negative architecture based on a **fixed three-variable phi-regrouping gadget with vanishing local phi cost and fixed positive regrouped HGR** is impossible, over arbitrary alphabets and arbitrary probability spaces. The denominator-10 exact search was seeing a genuine universal obstruction rather than a small-alphabet accident.

This does **not** refute Bradley's expected-negative possibility. It only says that a counterexample cannot be compiled from fixed-complexity local regrouping gadgets of that form.

## 8. Method #29 — add the points at infinity: a counterexample must escape through unbounded alternation

For a stationary sequence `X`, define `rho_K^*(n)` as the supremum of maximal correlations over interlaced index pairs `S,T` with `dist(S,T)>=n` whose chronological union has at most `K` maximal monochromatic runs (alternating `S`-blocks and `T`-blocks).

Every boundary between consecutive runs is a physical gap of at least `n`. For the induced chronological sigma-fields `G_1,...,G_K`, each prefix/suffix pair is contained in a past/future half-line cut separated by at least `n`. Hence

\[
\phi(H_i,K_i)\le\phi_X(n).
\]

Theorem 6.1 therefore yields

\[
\boxed{
\rho_K^*(n)
\le
\min\left\{1,\ 2\sqrt{(2^{K-1}-1)\phi_X(n)}\right\}.
}
\tag{8.1}
\]

Consequently, for **every fixed `K`**, ordinary phi-mixing implies

\[
\rho_K^*(n)\longrightarrow0.
\tag{8.2}
\]

The full source question differs only because `rho-star` takes the supremum over **unbounded** alternation complexity.

More quantitatively, if a finite interlaced witness at separation `n` has correlation at least `r>0` and uses `K` monochromatic runs, then

\[
r^2\le4(2^{K-1}-1)\phi_X(n),
\]

so necessarily

\[
\boxed{
K
\ge
1+\log_2\left(1+\frac{r^2}{4\phi_X(n)}\right).
}
\tag{8.3}
\]

Thus if a negative D0030 example has `rho-star(n_j)>=c>0` along a subsequence, any finite-coordinate witnesses approaching that lower bound must have alternation complexity tending to infinity, at least logarithmically in `1/phi(n_j)` (up to replacing `c` by any fixed smaller witness level if the supremum is not attained).

This is the useful compactification statement from method #29: **growing alphabet, rare events, or weak local correlations are not by themselves an escape route. The obstruction must run off to the point at infinity corresponding to unbounded interlacing complexity.**

## 9. Method #21 — who else has this shape, and why the Markov neighbor is different

Bradley's 2011 random-field construction has almost exactly the local regrouping shape, but for sequential **rho** rather than sequential **phi**. Equation (7.2) proves that its fixed-local mechanism cannot simply be upgraded to phi.

The neighboring R7-01/D0033 work on Bradley's **Markov-chain** Question 5 is even more informative. Its current candidate proof uses the Markov property to create actual separators between nonadjacent alternating blocks and then invokes maximal-correlation tensorization. That structure can make the interlaced bound dimension-free in the number of alternations. An arbitrary stationary sequence has no such conditional separator; R01's general induction instead pays a factor two each time another chronological block is exposed.

The strong-data-processing/maximal-correlation literature supplies the same operator language: maximal correlation is an `L^2_0` conditional-expectation norm, and one-cut phi supplies square-root contraction through (2.1). What remains genuinely source-specific is whether those one-cut contractions can be tensorized **uniformly in an arbitrarily long alternating word without a Markov separator**.

I found no external theorem in the bounded search that gives this exact dimension-free conclusion for arbitrary phi-mixing sequences. That is negative search evidence only; no novelty claim is made for Theorem 6.1.

## 10. What the run actually learned

The source question is now isolated more sharply than in the previous R01 reports:

1. the fixed three-variable counterexample compiler is rigorously dead by (7.2);
2. every bounded-alternation version of Bradley Question 2 is affirmative, with the explicit bound (8.1);
3. any negative source example must exploit an unbounded number of alternating blocks, quantitatively at least (8.3);
4. the adjacent Markov problem can plausibly avoid this accumulation because Markov separators kill nonlocal subjective correlations; arbitrary stationary sequences cannot use that argument automatically.

The exact remaining mathematical obstruction is therefore a **dimension-free alternating tensorization problem**:

\[
\boxed{
\sup_{K\ge2}
\sup_{\substack{G_1<\cdots<G_K\\
\phi(H_i,K_i)\le\varepsilon\ \forall i}}
\rho\left(\bigvee_{i\ \mathrm{odd}}G_i,
           \bigvee_{i\ \mathrm{even}}G_i\right)
\stackrel{?}{\longrightarrow}0
\quad(\varepsilon\downarrow0).
}
\tag{10.1}
\]

A YES answer to an appropriately process-compatible version of (10.1) would close D0030 positively. A NO family with `K -> infinity`, if stationarized across scales while preserving the one-cut phi bounds, would be the right raw material for a counterexample.

The present proof gives only

\[
\rho^2\le4(2^{K-1}-1)\varepsilon,
\]

which is intentionally useless when `K` grows like `log(1/epsilon)` or faster. That is now the precise wall rather than a vague failure of the local gadget search.

## 11. Stuck threshold and next-run obligation

Because the fixed binary source metric has now stayed at zero for three complete D0030 runs, Section I triggers. **The next R01 invocation must be a thinking-only stuck/recovery report**, not another ordinary theorem-extension run.

The blocker to display there is (10.1). The simplest still-unresolved regime is not any fixed `K` — Theorem 6.1 settles all fixed `K` — but a scaling window such as

\[
K=\Theta(\log(1/\varepsilon))
\]

where the present induction first becomes noninformative.

The three methods to consider in that mandatory thinking run, without repeating this run's triple or the preceding run's #8/#16/#24, are:

- **#20 FIND WHY THE ALGORITHM FAILS:** identify whether the factor-two conditional-phi loss is real or only an artefact of peeling;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** assume Philipp's negative direction and deliberately construct a long alternating finite law saturating the conditional losses;
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** freeze `epsilon`, optimize the smallest `K` at which high alternating HGR is possible, and only then ask about stationarization.

The stuck run must choose exactly one recovery action under Section I after comparing those routes; this report does not pre-empt that required choice.

## 12. Prior-art and checking discipline

Established ingredients, not claimed new:

- Bradley's definitions of phi, rho and rho-star;
- Peligrad's inequality (2.1), as recorded by Bradley;
- Bradley's 2011 rho/rho-prime/rho-star random-field constructions;
- maximal correlation as an `L^2` conditional-expectation/operator norm and its strong-data-processing interpretation;
- the neighboring D0033 Markov-specific tensorization work is repository work by another track and is not an independent audit of D0030.

New R01 route claim proved on the page here: Theorem 6.1 and its D0030 consequences (7.2), (8.1), (8.3). I did not locate these exact statements in the bounded literature search, but **novelty is UNVERIFIED**. A negative search is not a priority certificate.

No new finite claim required a checker this run. The exact denominator-10 checker from the preceding report remains historical evidence for that preceding finite search and is not repackaged as evidence for the analytic theorem here.

## 13. Model / reasoning control status

The runtime limitation is unchanged in the evidence available to this track: the exposed control surface does not provide an authenticated model selector, reasoning-effort selector, completed-run model telemetry, or a guaranteed hour-long execution control. The prompt can request GPT-6/maximum but cannot certify it. Enforcing those settings requires an authorized product/backend surface that exposes them.

The historical P26 `You cannot modify this task` error was context-specific: repository deployment evidence records later successful P26 modification from an authorized context. The legitimate remedy for any future permission refusal is the owning/authorized context or platform ownership support, not task duplication or permission bypass.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  source:
    id: D0030
    citation: "Richard C. Bradley, Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions, Probability Surveys 2 (2005), Question 2"
    target: "Does phi-mixing imply rho-star-mixing for the full strictly stationary sequence scope?"
  metric:
    name: E_phi_rho
    before: 0
    after: 0
  status: OPEN / PARTIAL
  unchanged_count:
    before: 2
    after: 3
    consequence: "STUCK threshold reached; next invocation must be thinking-only Section-I recovery"
  tried_moves: [17, 21, 29]
  movement_note: "No source-metric movement. New bounded-alternation theorem proves rho_K^*(n)^2 <= 4(2^(K-1)-1) phi(n) for fixed K and kills the fixed three-variable phi-regrouping compiler via eta(c) >= c^2/12."
  remaining_obligation: "Decide the dimension-free unbounded-alternation problem (10.1), then either prove full rho-star mixing or construct/stationarize a high-alternation counterexample."
  evidence:
    - "full proof of Theorem 6.1 in this immutable report"
    - "fresh Bradley source check and bounded literature search dated 2026-09-17 UTC / 2026-09-18 local"
    - "prior exact D=10 finite search remains in preceding R01 artifacts"
  audits:
    P26: null
    second_other_track: null
    audit_budget_spent_this_run: false
```

No shared root, peer-track file, email, Drive item, public posting, purchase, permission, or scheduler setting was changed in this run.
