Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime still has no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT on active D0030: `E_phi_rho = 0 -> 0`; unchanged count `0 -> 1`; status `OPEN / PARTIAL`; methods #2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #15 BREAK THE SYMMETRY.**

# R01 — D0030 / Bradley Question 2: scale-gadget reduction and the surviving counterexample architecture

Date: 2026-09-17 UTC.

Lane: **CLOSABLE OUTSIDE**.

## 1. Continuity, ownership, and source status

I did **not** reopen the native Aldous–Fill I0024 assignment. Its internally established exact flow characterization remains frozen at `C=1`. I also did not reopen I0113, G0012, D0057, or the retired R01 FEI assignment; P03 owns FEI. The active create-only R01 claim remains `operations/claims/D0030.md`.

Before new work I reread/recovered the required repository state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`; the current D0030 claim; the prior intake attempt `D0030-A001`; the previous R01 handoff/admission report; and the newest neighboring R02/D0031 report. R02 is in `OPEN / PARTIAL / STUCK-RECOVERY-1`, so there is no complete neighboring package eligible for the requested independent-audit budget.

The exact source remains Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys **2** (2005), Section 2.3, Question 2, journal p. 114 / PDF p. 8:

> If a given random sequence is phi-mixing, does it follow that it is rho*-mixing?

The active claim preserves the full **strictly stationary** sequence scope. Bradley records his own affirmative conjecture and Walter Philipp's negative expectation. In the same source, Theorem 2.1 states that for strictly stationary sequences `alpha*(n)->0` iff `rho*(n)->0`, and Theorem 5.1(b) gives exact Csaki–Fischer tensorization of maximal correlation across independent pairs of sigma-fields.

Primary source checked again this run:

- https://www2.stat.duke.edu/~scs/Projects/Stable/Conditions/BradleyStrongMixingSurvey2005.pdf

Fresh bounded literature queries on 2026-09-17/18 included exact combinations of `phi-mixing rho*-mixing`, `phi-mixing implies rho-star mixing`, `Bradley Question 2`, `interlaced rho-mixing phi-mixing`, and later work citing Bradley's interlaced-rho papers. They returned the source, Bradley's 1997 lower-psi Markov theorem, his 2001 rho-mixing-but-not-rho*-mixing Markov counterexample, his 2014 reversible-Markov examples, his 2015 INAR positive examples, and later copula/Markov work, but no paper claiming a source-matching proof or counterexample for arbitrary strictly stationary phi-mixing sequences. This is **bounded negative search evidence only**, not a worldwide openness or novelty certificate.

Relevant later/neighboring literature checked:

- R. C. Bradley, *Every lower psi-mixing Markov chain is interlaced rho-mixing*, Stochastic Processes and their Applications 72 (1997), 221–239, DOI 10.1016/S0304-4149(97)00090-2.
- R. C. Bradley, *A Stationary Rho-Mixing Markov Chain Which Is Not Interlaced Rho-Mixing*, Journal of Theoretical Probability 14 (2001), 717–727, DOI 10.1023/A:1017545123473.
- R. C. Bradley, *On Mixing Properties of Reversible Markov Chains*, arXiv:1403.4895.
- R. C. Bradley, *On Mixing Properties of Some INAR Models*, arXiv:1509.09303.
- M. Longla, M. M. Nthiani, F. D. Ndikwa, *Dependence and mixing for perturbations of copula-based Markov chains*, Statistics & Probability Letters 181 (2022), 109239.

No current source found turns the restricted Markov/coupla results into the full D0030 statement.

## 2. Frozen metric

The fixed quantity remains

\[
E_{\phi,\rho^*}\in\{0,1\},
\]

where it becomes `1` only after a full proof or a fully verified strictly stationary phi-mixing counterexample with `limsup rho*(n)>0`.

This run does not decide the full question:

\[
\boxed{E_{\phi,\rho^*}=0\longrightarrow0.}
\]

This is the first complete unchanged D0030 run after admission, so the D0030 unchanged count is `0 -> 1`.

## 3. Method #2 — ATTACK THE NEGATION FIRST

I attacked the negative direction before attempting a universal inequality. Three natural counterexample mechanisms were separated.

### 3.1 Global phase / marker mechanisms fail immediately

A phi-mixing construction cannot carry a nontrivial persistent phase which is exactly readable from both separated half-lines.

**Lemma 3.1 (common-event obstruction).** Let `A` and `B` be sigma-fields. If there is an event `C in A cap B` with `0<P(C)<1`, then

\[
\phi(A,B)\ge \frac12.
\]

**Proof.** Write `p=P(C)`. If `p<=1/2`, choose the conditioning event and target event both equal to `C`; then

\[
|P(C\mid C)-P(C)|=1-p\ge\tfrac12.
\]

If `p>1/2`, use `C^c` in both places and obtain `p>1/2`.  QED.

Hence any rare-marker, stationary random-phase, periodic-skeleton, or hidden-global-bit proposal in which the same nonconstant event is eventually reconstructible from both one-sided sigma-fields is disqualified before any rho* calculation. **Rarity does not help phi**, because phi takes a supremum over conditioning events rather than averaging over them.

This eliminates the most obvious way of preserving an interlaced common mode while making its occurrence rare.

### 3.2 Independent weak-pair amplification also fails

The second negative route was to place many weak correlations in parallel, hoping that an interlaced observer could aggregate them. Csaki–Fischer tensorization kills that route exactly. If `(A_j vee B_j)` are mutually independent, then Bradley's Theorem 5.1(b) gives

\[
\rho\!\left(\bigvee_j A_j,\bigvee_j B_j\right)
=
\sup_j \rho(A_j,B_j).
\]

Thus parallel repetition of independent weak HGR channels cannot amplify a small local maximal correlation into an order-one interlaced mode. Any genuine counterexample must use **non-product multiscale synergy**, not a bag of independent weak pairs.

### 3.3 A viable negative architecture survives: independent *scale gadgets*

Although independent weak pairs cannot amplify HGR inside one scale, independent **whole scale gadgets** can be used to assemble a counterexample if one can first build gadgets whose ordinary phi cost is summably small but whose interlaced rho is order one at their own increasing scales. This leads to the main exact reduction of the run.

## 4. Exact scale-gadget reduction

The following is a complete analytic reduction, not a closure claim.

**Proposition 4.1 (finite-range scale-gadget compiler).** Suppose there are independent strictly stationary processes

\[
Y^{(j)}=(Y^{(j)}_k)_{k\in\mathbb Z},\qquad j\ge1,
\]

numbers `epsilon_j>0` with

\[
\sum_{j\ge1}\epsilon_j<\infty,
\]

finite dependence ranges `m_j`, separations `n_j -> infinity` with `n_j <= m_j`, and a constant `c>0`, such that for every `j`:

1. `Y^(j)` is `m_j`-dependent;
2. `phi(Y^(j),1) <= epsilon_j`;
3. `rho*(Y^(j),n_j) >= c`.

Define the product-valued stationary process

\[
X_k=(Y^{(1)}_k,Y^{(2)}_k,\ldots).
\]

Then `X` is phi-mixing but is **not** rho*-mixing. Consequently, existence of such a gadget family would give a negative answer to D0030.

**Proof.** Strict stationarity is preserved under the independent coordinate product. For ordinary phi, Bradley's independent-pair inequality, applied at the past/future cut, gives

\[
\phi_X(n)
\le
1-\prod_{j\ge1}(1-\phi_j(n))
\le
\sum_{j\ge1}\phi_j(n).
\]

Because `Y^(j)` is `m_j`-dependent, `phi_j(n)=0` for `n>m_j`; and by monotonicity of phi,

\[
0\le\phi_j(n)\le\phi_j(1)\le\epsilon_j.
\]

Therefore

\[
\phi_X(n)
\le
\sum_{j:m_j\ge n}\epsilon_j.
\]

For each fixed `j`, the indicator `1_{m_j>=n}` tends to zero as `n->infinity`, while the summable sequence `(epsilon_j)` dominates. Dominated convergence gives

\[
\phi_X(n)\longrightarrow0.
\]

For interlaced maximal correlation, for any fixed admissible pair of index sets `S,T`, the sigma-fields generated by the different `j`-coordinates are independent. Csaki–Fischer therefore gives

\[
\rho\!\left(\sigma(X_k:k\in S),\sigma(X_k:k\in T)\right)
=
\sup_j
\rho\!\left(\sigma(Y^{(j)}_k:k\in S),\sigma(Y^{(j)}_k:k\in T)\right).
\]

Taking the supremum over admissible `S,T` yields

\[
\rho_X^*(n)=\sup_j\rho_{Y^{(j)}}^*(n).
\]

In particular,

\[
\rho_X^*(n_j)\ge\rho_{Y^{(j)}}^*(n_j)\ge c
\]

for all `j`, while `n_j->infinity`. Thus `X` is not rho*-mixing. QED.

This compiler is useful because it converts Philipp's negative intuition into a sharply finite target:

\[
\boxed{
\text{Build stationary finite-range gadgets with }\phi(1)\downarrow0
\text{ but }\rho^*(n_j)\ge c>0\text{ at }n_j\uparrow\infty.
}
\]

No such gadget is produced here; therefore the source remains OPEN. But the construction wall is now localized to one finite-scale object instead of an entire infinite counterexample.

## 5. Method #11 — DUALIZE: the missing operator inequality

For two sigma-fields `A,B`, let `P_A,P_B` denote conditional-expectation projections on centered `L^2`. Maximal correlation is the operator norm

\[
\rho(A,B)=\|P_A P_B\|_{L_0^2\to L_0^2}.
\]

The standard Bradley/Peligrad inequality gives, for the **single past/future cut**,

\[
\rho(\mathcal F_{-\infty}^0,\mathcal F_n^\infty)
\le 2\,\phi(n)^{1/2}.
\]

D0030 asks whether control of those one-cut operators forces

\[
\sup_{\operatorname{dist}(S,T)\ge n}
\|P_{\sigma(X_S)}P_{\sigma(X_T)}\|
\longrightarrow0.
\]

The number of alternations between `S` and `T` is unbounded. A naive telescoping through alternating cuts produces a bound growing with that number and therefore cannot settle the source.

The exact Csaki–Fischer identity explains why the obvious tensor approach also stalls: **independent** components tensorize by a supremum, which is excellent, but successive alternating pieces inside one process are not independent components. The required positive theorem would be a dimension-free operator/tensorization inequality for those noncommuting conditional-expectation projections. A universal estimate of the schematic form

\[
\rho^*(n)\le F(\phi(n)),\qquad F(t)\to0,
\]

would be stronger than necessary and would solve the source immediately. Proposition 4.1 shows the complementary pressure: a family of finite-range gadgets violating every such dimension-free principle at increasing scales can be compiled into a genuine negative example, provided their ordinary-phi costs are summable.

So the positive and negative programs meet at the same finite operator question rather than at two unrelated constructions.

## 6. Method #15 — BREAK THE SYMMETRY

The source itself warns against overly symmetric categories:

- Gaussian phi-mixing collapses to finite dependence, so Gaussian geometry cannot contain the desired pathology.
- A globally periodic/random-phase skeleton leaves a common tail event and fails Lemma 3.1.
- Independent weak pairs cannot amplify HGR by Csaki–Fischer.
- The known 2001 Markov example is rho-mixing but not rho*-mixing; replacing rho by phi is exactly the missing uniform conditional-probability control.

The surviving negative architecture therefore has to break all three symmetries at once: **finite range at each scale, no globally readable phase, and a genuinely collective interlaced mode inside each gadget**.

This is more restrictive than the prior D0030-A001 description. In particular, a successful gadget must not obtain its rho* witness from a single persistent latent variable which is recognizable from a one-sided half-line, and it must not be a product of independent weak correlations.

A useful exact rejection criterion for future candidates is now:

> Before computing rho*, test whether the candidate has a nontrivial event common to the two half-line sigma-fields or decomposes into independent weak pair channels. If either occurs, reject it immediately.

## 7. What moved conceptually, and what did not

The fixed source metric did **not** move. The useful progress is a precise dichotomy of construction mechanisms:

- global phase / rare marker: **ruled out** by the common-event phi obstruction;
- independent weak-pair aggregation: **ruled out** by exact HGR tensorization;
- independent summable **scale gadgets**: **viable**, and Proposition 4.1 proves that solving this finite gadget problem is sufficient for a full negative answer;
- positive direction: reduced to a dimension-free norm estimate for interlaced conditional-expectation projections, with the unbounded alternation count as the exact obstruction.

This is not labelled PROVED/REFUTED because neither side decides the source.

## 8. Simplest concrete unresolved laboratory

The next useful finite question is not another infinite construction. Fix `c=1/4`, say, and ask whether for arbitrarily large `N` there exists a strictly stationary `m`-dependent **finite-alphabet** process `Y` with `m>=N` such that

\[
\phi_Y(1)\le\varepsilon_N\to0,
\qquad
\rho_Y^*(N)\ge c.
\]

If such gadgets can be obtained with a summable subsequence of `epsilon_N`, Proposition 4.1 finishes the negative direction. Conversely, evidence of a lower bound

\[
\phi_Y(1)\ge G(\rho_Y^*(N))
\]

uniform in `N,m` for finite-range stationary gadgets would be the first genuinely dimension-free evidence for the affirmative side.

This is the finite exact-arithmetic search target for the next run, not a theorem asserted here.

## 9. Prior-art status and access limits

The primary source explicitly records:

- `alpha* -> 0` iff `rho* -> 0` for strictly stationary sequences;
- `rho <= 2 sqrt(phi)` for arbitrary sigma-field pairs (in the standard asymmetric sharper form in the source);
- exact Csaki–Fischer tensorization of rho across independent joins;
- arbitrary-rate construction machinery for alpha/rho/rho*, but no analogous exact phi prescription;
- Question 2 as unsolved in 2005.

The current bounded search found later work in special Markov/copula classes but no arbitrary-sequence source resolution. Full-text access to some older Bradley construction papers was limited to abstracts/metadata in the available web interfaces, so I do **not** claim to have audited every internal step of those papers. No novelty claim is made for Proposition 4.1; it is a clean synthesis of the independent-pair inequalities into the exact counterexample compiler needed by this track.

## 10. Audit budget

No independent audit was requested or supplied. The newest neighboring R02/D0031 package is explicitly `OPEN / PARTIAL / STUCK-RECOVERY-1`, not a complete package. D0030 itself has no complete theorem/counterexample package to audit.

## 11. Next three Section-B moves

The next run should not repeat #2/#11/#15. The planned triple is:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** formulate the finite-range gadget problem on the smallest binary/ternary stationary block models where phi can be computed exactly from conditional rows.
- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE:** only after fixing that gadget objective, perform exact-rational enumeration/optimization for small ranges and archive a checker if a nontrivial extremal pattern appears.
- **#24 FIND THE EXTREMAL OBJECT:** maximize interlaced HGR subject to a frozen ordinary-phi budget and stationarity/finite-range constraints; look for a structural extremizer rather than another ad hoc marker construction.

If these finite searches produce only checker output with no new extremal pattern or bound, the run should report the failed routes rather than manufacture certificates.

## 12. Model/scheduler control and protected-task boundary

The implementation limitation remains exactly the one recorded in `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`: the exposed scheduler interface has schedule/prompt/enabled/timing controls but **no model selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution control**. GPT-6 / maximum is therefore a prompt request only in this environment.

The same manifest records the historical P26 task ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` from that context. The legitimate workaround is an owning/authorized context or a platform/support ownership migration. Duplicating the task or bypassing permissions is not a valid workaround, and this run made no scheduler or permission changes.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R01
  active_target: D0030
  source: "Richard C. Bradley, Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions (2005), Question 2"
  metric: E_phi_rho
  before: 0
  after: 0
  status: OPEN/PARTIAL
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [2, 11, 15]
  remaining_obligation: "Decide the full strictly stationary phi-mixing => rho*-mixing question; negative route now reduces to summably-small-phi finite-range scale gadgets, positive route needs a dimension-free interlaced conditional-expectation norm inequality."
  evidence:
    - "Bradley 2005 Question 2 and Theorems 2.1, 5.1, 5.2 reread"
    - "D0030-A001 preserved"
    - "Common-event obstruction proved on page"
    - "Finite-range scale-gadget compiler Proposition 4.1 proved on page"
    - "Fresh bounded 2026-09-17/18 literature search found no source-matching resolution"
  audit_ids: []
```

No shared root, other-track file, email, Drive object, public post, permission, purchase, or scheduler configuration was modified.