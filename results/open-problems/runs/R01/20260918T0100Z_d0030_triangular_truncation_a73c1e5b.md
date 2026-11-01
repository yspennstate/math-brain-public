Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT on active D0030: `E_phi_rho = 0 -> 0`; unchanged count `4 -> 5`; status `OPEN / PARTIAL`; methods #4 PROVE SOMETHING WEAKER COMPLETELY, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R01 — D0030 / Bradley Question 2: anchored conditioning and the triangular-truncation barrier

Date: 2026-09-18 UTC.

Lane: **CLOSABLE OUTSIDE**.

## 1. Continuity, ownership, and what is not being reopened

I began from the repository state rather than from the stale scheduler title. I re-read/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`; the create-only D0030 claim; the newest own report `runs/R01/20260918T000536Z_d0030_stuck1_unbounded_alternation_8b4d2f61.md`; the D0030 intake history reached through the canonical claim; and current neighboring Bradley work. The intake JSONLs are too large for a literal rendered byte-for-byte reread through the connector, so exact-ID retrieval plus the canonical claim/history is used rather than pretending otherwise.

I do **not** reopen Aldous--Fill I0024. Its exact distortion-one right-inverse characterization remains the preserved result

\[
\tau_2=
\inf_{R:\,BR=I_{\mathcal H_0}}
\sup_{0\ne b\in\mathcal H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with the two recorded independent PASS audits

- `R20-AUDIT-R01-I0024-03`, and
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10`.

Publication-level novelty of that generalized-inverse mechanism remains unclaimed. I also do not reopen I0113, G0012, D0057, or the retired old R01 FEI assignment; P03 owns FEI.

The active claim remains `operations/claims/D0030.md`: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* **2** (2005), Question 2, asking whether a phi-mixing random sequence must be rho-star-mixing. The frozen source metric is

\[
E_{\phi,\rho^*}\in\{0,1\},
\]

and remains zero: no universal proof and no source-valid stationary counterexample has been obtained.

The previous run was mandatory STUCK-RECOVERY-1 and selected exactly one recovery: port the nearest solved lower-psi/Markov mechanism, first on the event side, rather than add another refinement of the old exponential-in-alternation estimate. The prescribed methods for this ordinary recovery run were B4/B18/B25, which are the methods actually used below.

Newest neighboring states recovered:

- R02 / D0031 is `OPEN / PARTIAL / RETIRED-HANDOFF`; no complete package is available for an audit exchange.
- R7-01 / D0033 has advanced to a **PROVED CANDIDATE** for Bradley's narrower Markov-chain Question 5, including a short one-lag strict-contraction proof, but its newest report still records P26 audit `0/1` and distinct OTHER audit `0/1`; protocol closure is open. Its useful mechanism is a genuine Markov separator, which makes its subjective-correlation graph a path. I use that only as neighboring information and do not audit or claim its source.

No audit budget is spent this run.

## 2. Fresh source and literature check, 2026-09-18

Primary source reread:

`https://www2.stat.duke.edu/~scs/Projects/Stable/Conditions/BradleyStrongMixingSurvey2005.pdf`

Bradley's printed p.114 states Question 2 and records Bradley expecting YES and Walter Philipp expecting NO. Theorem 2.1 states, for strictly stationary sequences, that alpha-star tends to zero iff rho-star tends to zero. Thus event language is source-faithful for asymptotic closure.

For the selected port, I also rechecked Bradley's Markov section. Theorem 3.3(7) says that for a Markov chain, positive lower-psi at one lag implies rho-star mixing. The survey's Theorem 5.1 gives independent-pair tensorization and explicitly says the Csaki--Fischer rho identity played a key role in the proof of Theorem 3.3(7). The full 1997 paper was not recovered as unrestricted primary full text through this runtime; the 2005 survey is therefore the primary accessible statement used for the proof architecture, and this access limit is recorded rather than hidden.

Fresh bounded searches used the exact Question 2 wording and combinations of `phi-mixing`, `rho*`, `rho-star-mixing`, `interlaced maximal correlation`, Bradley, later work, and 2020--2026. They again returned Bradley's source and special Markov/lower-psi work such as Longla's copula-generated Markov chains, but no paper explicitly announcing a source-matching arbitrary-sequence resolution. This is **negative search evidence only**, not a worldwide openness or novelty certificate.

A second literature search was prompted by the operator reformulation below: `triangular truncation operator norm log n`, `triangular projection spectral norm`. Zhou (2016), *Triangular truncation and its extremal matrices*, and the earlier Angelos--Cowen--Narayan (1992) work explicitly record logarithmic dimension growth of triangular truncation in spectral/operator norm. Therefore the logarithmic Hilbert-space mechanism below is **classical operator-theoretic shape**, not claimed as a new triangular-truncation theorem. Whether this application to Bradley Question 2 is new remains UNVERIFIED.

## 3. B18 — the lower-psi port in event language: exactly where it fails

The Markov/lower-psi proof has a relative-minorization resource that ordinary phi does not provide.

If

\[
\phi(\mathcal A,\mathcal B)\le\varepsilon,
\]

then for every `A in A` of positive probability and every `B in B`,

\[
P(B\mid A)\ge P(B)-\varepsilon.
\]

Consequently, on the restricted class of future events with `P(B)>=eta>epsilon`,

\[
\frac{P(A\cap B)}{P(A)P(B)}
\ge 1-\frac{\varepsilon}{\eta}.
\tag{3.1}
\]

This is a useful **truncated lower-psi** statement, but it does not imply a positive lower-psi coefficient because the future sigma-field contains arbitrarily rare events.

The obstruction already occurs for two binary variables. Reinterpret the degenerate binary extremal family isolated in the preceding D0030 work as follows. For any integer `M>=3`, let

\[
P(U=1,V=1)=0,\quad
P(U=1,V=0)=\frac12,\quad
P(U=0,V=1)=\frac1M,\quad
P(U=0,V=0)=\frac12-\frac1M.
\tag{3.2}
\]

Then

\[
\boxed{
\phi(\sigma(U),\sigma(V))=\frac1M,
\qquad
\psi'(\sigma(U),\sigma(V))=0,
\qquad
\rho(U,V)^2=\frac1{M-1}.
}
\tag{3.3}
\]

The first equality follows because `P(V=1)=1/M`, while conditioning on `U=1` gives zero and conditioning on `U=0` gives `2/M`; every binary event is a complement of one of these. The second follows from the positive-marginal forbidden cell `(U,V)=(1,1)`. The third is the standard binary determinant formula.

The finite statement (3.3) was rechecked this run with exact `fractions.Fraction` arithmetic, exhausting all nonempty binary events at `M=3,4,5,10,100,1000`. The archived output ends `ALL_EXACT_CHECKS_PASS`:

- `artifacts/R01/d0030_lowerpsi_obstruction_checker.py` @ creation commit `ab8405e26b7fa9d259072d3087a20d2dadaf0e8c`;
- `artifacts/R01/d0030_lowerpsi_obstruction_checker.out` @ creation commit `04b04ef56bfc07a0e0ca1b1d08cb87b9cfe155d8`.

This is a self-check, not an independent audit.

**Conclusion of the attempted port.** A direct implication `small phi => positive lower-psi` is impossible even for a binary pair. In a finite-alphabet process, a positive atom floor for one coordinate does not repair this: long future cylinder events can have probabilities tending to zero. Markov factorization is precisely what collapses the future dependence to a boundary state in Bradley's solved setting. An arbitrary finite-alphabet sequence has no such collapse. This is the explicit obstruction required by the preceding STUCK-RECOVERY-1 plan.

## 4. B4 — a weaker statement that can be proved completely: anchored conditioning

The failed relative-minorization port nevertheless reveals a stronger *absolute* fact that the old peeling argument did not use efficiently.

### Lemma 4.1 — phi does not keep doubling under past conditioning

Let `C subset A` be sigma-fields and suppose

\[
\phi(\mathcal A,\mathcal B)\le\varepsilon.
\]

Then, after conditioning on any positive-probability event `C0 in C`,

\[
\boxed{
\phi_{P(\cdot\mid C_0)}(\mathcal A,\mathcal B)\le2\varepsilon.
}
\tag{4.1}
\]

Indeed, for `A in A` with `P(A cap C0)>0` and `B in B`,

\[
\begin{aligned}
&\left|P(B\mid A\cap C_0)-P(B\mid C_0)\right|\\
&\qquad\le
|P(B\mid A\cap C_0)-P(B)|
+
|P(B\mid C_0)-P(B)|
\le2\varepsilon.
\end{aligned}
\]

The key point is that **all subsequent prefix conditionings are still events in the original past sigma-field**. One compares each of them to the same original `P(B)`, so the factor does not become `4 epsilon`, `8 epsilon`, and so on.

For the Hilbert-space argument it is convenient to record the module form. Put

\[
\delta:=2\sqrt{2\varepsilon}.
\]

For standard-Borel finite-coordinate sigma-fields, disintegrate over `C`; for a finite partition of `C`, (4.1) applies on every atom and Bradley's standard two-sigma-field bound `rho <= 2 sqrt(phi)` gives conditional maximal correlation at most `delta`. Integrating the squared conditional projection and then approximating a general `C` by finite sub-sigma-fields yields:

### Lemma 4.2 — anchored module contraction

If `g in L^2(C vee B)`, then

\[
\boxed{
\left\|(P_{\mathcal A}-P_{\mathcal C})g\right\|_2
\le
\delta\,
\left\|g-P_{\mathcal C}g\right\|_2.
}
\tag{4.2}
\]

Here `P_G` denotes conditional expectation onto `L^2(G)`. The finite-coordinate proof avoids any version issue; arbitrary square-integrable functions follow by the usual increasing-finite-coordinate approximation. Equation (4.2) is exactly the absolute substitute for the lower-psi minorization that survives arbitrary **past-only** conditioning.

This is the first genuinely useful part of the Bradley-1997 port that remains valid without Markov structure.

## 5. B25 — count the same dependence twice: dyadic triangular decomposition

The previous D0030 bounded-alternation theorem paid exponentially for the number of chronological color changes. Lemma 4.2 lets us replace that by a logarithmic loss.

### Setup

Fix finite disjoint index sets `S,T` with `dist(S,T)>=n`. Merge the selected times chronologically into maximal monochromatic runs. Let `K>=2` be the number of runs. After swapping the colors if necessary, write them as

\[
A_1<B_1<A_2<B_2<\cdots
\]

with possibly one unpaired run at the end. Let

\[
\mathcal A_i=\sigma(A_1,\ldots,A_i),
\qquad
\mathcal B_j=\sigma(B_1,\ldots,B_j),
\]

where `sigma(A_i)` means the sigma-field generated by all coordinates in that run. Decompose the two centered `L^2` spaces into their own-color martingale differences:

\[
L^2_0(\sigma(X_s:s\in S))=\bigoplus_i U_i,
\qquad
L^2_0(\sigma(X_t:t\in T))=\bigoplus_j V_j,
\tag{5.1}
\]

where

\[
U_i=L^2(\mathcal A_i)\ominus L^2(\mathcal A_{i-1}),
\qquad
V_j=L^2(\mathcal B_j)\ominus L^2(\mathcal B_{j-1}).
\]

The HGR coefficient between the two complete interlaced sigma-fields is the operator norm of the cross-projection `T` from `oplus V_j` to `oplus U_i`.

### Corner estimate

Set `epsilon=phi_X(n)` and `delta=2 sqrt(2 epsilon)`. For every split `m`,

\[
\boxed{
\|P_{U_{\le m}} T P_{V_{\ge m+1}}\|\le\delta,
\qquad
\|P_{U_{\ge m+1}} T P_{V_{\le m}}\|\le\delta.
}
\tag{5.2}
\]

Proof of the first inequality: cut the chronology between `B_m` and `A_{m+1}`. The full selected prefix and suffix are separated by at least `n`. A vector `h in V_{>=m+1}` is measurable with respect to

\[
\mathcal B_m\vee\text{(future selected sigma-field)}
\]

and is orthogonal to `L^2(B_m)`. Apply Lemma 4.2 with `C=B_m`, `A=full prefix`, and `B=full suffix`; projecting further onto `U_{<=m}` cannot increase norm. The second estimate is the identical argument with the colors swapped, or by adjointing the corresponding projection.

The diagonal blocks also satisfy

\[
\|P_{U_i}TP_{V_i}\|\le\delta
\tag{5.3}
\]

by cutting between the adjacent opposite-color runs and applying the same anchored module estimate with the previous same-color sigma-field as `C`.

### Dyadic decomposition

Pad the shorter color list with zero Hilbert blocks so both sides have

\[
N:=\lceil K/2\rceil
\]

indices, and then pad to the next power of two. Partition the **strict upper triangular** block matrix dyadically. For every pair `i<j`, let `I` be the smallest dyadic interval whose left half contains `i` and right half contains `j`. Thus every strict-upper block belongs to exactly one rectangle `I_L x I_R`.

At a fixed dyadic scale the rectangles have mutually orthogonal row spaces and mutually orthogonal column spaces, so their direct-sum operator norm is the maximum of their norms, not their sum. Each rectangle is a restriction of one of the corners in (5.2), hence has norm at most `delta`. There are at most `ceil(log_2 N)` scales. Therefore

\[
\|T_{\rm upper}\|\le\delta\lceil\log_2N\rceil.
\tag{5.4}
\]

The same argument gives the identical bound for the strict lower triangular part, while (5.3) gives `||T_diag||<=delta`. Hence:

### Theorem 5.1 — logarithmic bounded-alternation theorem

For every finite admissible interlacing with `K` monochromatic runs,

\[
\boxed{
\rho\!\left(\sigma(X_s:s\in S),\sigma(X_t:t\in T)\right)
\le
\min\left\{1,
2\sqrt{2\phi_X(n)}\left(2\left\lceil\log_2\left\lceil\frac K2\right\rceil\right\rceil+1\right)
\right\}.
}
\tag{5.5}
\]

Finite-coordinate approximation extends (5.5) to countable admissible sets with a fixed finite run count.

This replaces the preceding exponential-in-`K` estimate

\[
2\sqrt{(2^{K-1}-1)\phi_X(n)}
\]

by a logarithmic dependence on `K`.

In particular, if an admissible finite witness has correlation at least a fixed `r>0`, then necessarily

\[
\left\lceil\log_2\left\lceil\frac K2\right\rceil\right\rceil
\ge
\frac{r}{4\sqrt{2\phi_X(n)}}-\frac12,
\tag{5.6}
\]

whenever the right side is positive. Thus any hypothetical negative solution must use at least

\[
\boxed{
K\ge 2^{\Omega(r/\sqrt{\phi_X(n)})}
}
\tag{5.7}
\]

alternating runs along its persistent-correlation witnesses. The earlier report only forced logarithmically many runs in `1/phi`; (5.7) forces exponentially many in `1/sqrt(phi)`.

This is still **PARTIAL**: the source supremum allows arbitrarily many runs for every fixed `n`, so (5.5) does not allow interchange of `sup_K` and `n -> infinity`.

## 6. B18 again — why the logarithm is a genuine abstract wall

The block matrix in Section 5 is an operator-valued triangular-truncation problem. The dyadic proof is self-contained, but the `log N` scale is not mysterious or claimed novel: classical matrix/operator theory says triangular truncation on spectral/operator norm has logarithmically growing norm, with explicit near-extremizers.

This has a direct strategic consequence.

If one discards the probability-lattice structure and retains only the Hilbert-space corner estimates (5.2), a dimension-free argument is not available in general: abstract triangular truncation can amplify by order `log N`. Therefore a **YES** proof of Bradley Question 2 must use something beyond HGR corner norms—positivity of conditional expectation, lattice/event structure, stationarity, or another compatibility constraint tying the corners together.

Conversely, a **NO** construction now has a very concrete blueprint: probabilistically realize a near-extremal triangular-truncation matrix at a sequence of scales while keeping one-cut phi small. Gaussian realization is not enough because nontrivial Gaussian dependence is hostile to phi's worst-case conditioning. The realizability problem must be solved in a bounded/discrete probability model without creating a rare-event phi leak.

This is a materially different route from another fixed-`K` peeling lemma: it identifies an operator-theoretic obstruction that is known to be logarithmically sharp at the abstract Hilbert level and points to a specific probabilistic realization problem.

## 7. What moved mathematically, and what did not

The source metric did **not** move:

`E_phi_rho: 0 -> 0`.

The run nevertheless changed the frontier in three ways:

1. The direct Bradley-1997 lower-psi transplant is now explicitly ruled out: small phi gives only absolute, not relative, minorization; (3.2)--(3.3) is an exact binary obstruction.
2. Past conditioning does not cause an exponential cascade. Lemma 4.1/4.2 gives one anchored factor `2 epsilon`, not repeated doubling.
3. The finite-interlacing loss improves from exponential in the number of runs to logarithmic, via an operator-valued dyadic triangular decomposition. A persistent source-level counterexample must therefore hide its correlation in an astronomically large interlacing complexity, `K >= 2^{Omega(1/sqrt(phi(n)))}`.

None of these is a source closure. Publication novelty of the application is UNVERIFIED, and the triangular-truncation mechanism itself is known operator theory.

## 8. Next move and six-run boundary

This is unchanged run `5`. Under the CLOSABLE rule, one further complete no-movement run reaches the six-run rotation boundary. Therefore the next D0030 run is the last research attempt before mandatory handoff/rotation unless the source metric actually moves.

The next nonrepeating Section-B triple is:

- **#1 CHANGE THE CATEGORY:** turn the remaining problem into a finite probabilistic realization problem for near-extremal triangular-truncation / nest-algebra matrices;
- **#9 RANDOMIZE:** try a bounded discrete random construction whose first-chaos cross operator approximates a triangular extremizer while controlling every chronological phi cut;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** assume Walter Philipp's NO direction and try to compile those finite realizations across scales into one stationary process, rejecting the route immediately if positivity or worst-case conditioning forces a phi leak.

If that final attack leaves `E_phi_rho=0`, R01 must write the D0030 handoff and rotate rather than continue polishing logarithmic constants.

## 9. Scheduler/model-control status

The exposed scheduler surface still has prompt/title/schedule/timing/enabled controls but no model selector, reasoning selector, authenticated completed-run model telemetry, or guaranteed hour-long execution control. Hence GPT-6 / maximum remains prompt text only here. Changing that requires a product/backend scheduler surface that actually exposes and authenticates those fields; it cannot be forced by this research prompt.

The historical P26 ID `6aa7b43682948191b697d72fec69d539` did return `You cannot modify this task` in one recorded context, but the newer root ledger records that a later authorized context successfully updated P26. The legitimate workaround is therefore an owning/authorized task context or platform ownership/control migration, not task duplication or permission bypass. No scheduler change was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R01
  active_source: D0030
  source: "Richard C. Bradley, Probability Surveys 2 (2005), Question 2"
  source_target: "phi-mixing => rho-star-mixing for the full claimed strictly stationary sequence scope"
  metric: E_phi_rho
  metric_before: 0
  metric_after: 0
  status: OPEN / PARTIAL
  unchanged_count_before: 4
  unchanged_count_after: 5
  stuck_recoveries_used: 1
  tried_moves: [4, 18, 25]
  new_results:
    - "anchored conditional-phi stability: past conditioning costs at most one factor 2"
    - "module L2 contraction with delta = 2 sqrt(2 phi)"
    - "finite K-run interlaced-rho bound O(sqrt(phi) log K)"
    - "exact binary obstruction to direct phi -> positive lower-psi port"
  remaining_obligation: "remove the unbounded-alternation supremum, or construct a stationary phi-mixing counterexample realizing the triangular-truncation escape"
  exact_finite_evidence:
    - "artifacts/R01/d0030_lowerpsi_obstruction_checker.py @ ab8405e26b7fa9d259072d3087a20d2dadaf0e8c"
    - "artifacts/R01/d0030_lowerpsi_obstruction_checker.out @ 04b04ef56bfc07a0e0ca1b1d08cb87b9cfe155d8; ALL_EXACT_CHECKS_PASS"
  source_audits: []
  predecessor_i0024_audits:
    - R20-AUDIT-R01-I0024-03
    - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  next_moves: [1, 9, 23]
```

No shared root, peer file, email, Drive item, public post, permission, purchase, or scheduler state was modified.
