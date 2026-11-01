# Alternative routes for a ten-day full-FEI research campaign

**Prepared 11 October 2026. Scope:** mathematical strategy and bounded research assignments; no repository, scheduler, or account changes. The proposed allocation is a research design, not evidence that 100 agents are running. This report uses the recovered Brain as an existing body of work, with its proof status and counterexamples preserved. It does not claim a proof of full FEI.

## 1. Recommendation

Run several genuinely different approaches, with an independent falsification team attached to each. Concentrate most proof effort on three bounded targets: a sharper decision-tree covariance bound; a new exact conditional-product class with two spectral address coordinates; and the Brain's unresolved weighted correlation-lifetime inequality. Keep actual-source entropy transfer and adaptive physical restriction trees as higher-risk routes to full FEI. Reserve a small structural-reduction team to check whether promising-looking restricted problems already encode arbitrary Boolean functions.

The mathematical objective is

\[
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2}
\le C\sum_S |S|\widehat f(S)^2=C I(f)
\]

with one absolute constant for every Boolean sign function on every finite uniform cube. A new parameter-dependent bound or a proper new class is substantial progress, but it must retain its parameter or hypothesis in every summary. Numerical evidence, a new equivalent formulation, and a proof for threshold functions are different deliverables from this universal theorem.

The recent threshold argument is a useful audited building block and potential stopping class. It should not consume the entire campaign: arbitrary Boolean derivatives have no desirability order, and a successful coding construction for addressing does not pay the analogous cost for an arbitrary selector cell.

## 2. Established baselines to credit before launching workers

Wan–Wright–Wu already formulate FEI as coding the entire spectral set. Their prefix-code method and tree covariance analysis give a read-\(k\) decision-tree result; “read-\(k\)” counts the nodes querying each variable across the entire tree. Thus whole-set coding itself is established prior art. A new contribution must identify a better valid code and prove its expected cost. [S1]

Shalev improves the dependence for those trees to \(O(\sqrt{k})\). His paper also proves FEI for \(I(f)\le2^{-cn}\), with \(C=4(c+1)/c\), and shows that a uniform FEI bound throughout \(I(f)\le2^{-s(n)}\), \(s(n)=o(n)\), implies full FEI. Extremely low influence is therefore a known tractable endpoint, while relaxing its exponential scale is a full-strength problem. [S2]

Arunachalam–Chakraborty–Koucký–Saurabh–de Wolf prove FMEI for all constant-read-\(k\) DNFs, not just the narrower regular-DNF family in an earlier paper. They prove \(H(f)\le2\operatorname{aUC}^{\oplus}(f)\), where the parameter is average unambiguous parity certificate complexity. Those results prevent counting rediscovered parity-certificate coding or constant-read DNF min-entropy as a new milestone. [S3]

O'Donnell–Tan's biased, strengthened FEI composition theorem covers disjoint composition and bounded-arity read-once formulas. Ordinary uniform-cube FEI for the components is not the exact hypothesis of that theorem; the induced biases and variance correction matter. A new overlap theorem must handle the interference created by shared variables. [S4]

González–MacManus–Pereyra explicitly use entropy decrements under physical coordinate restrictions, selected branching coordinates, and stopping trees. The Brain's erasure/JS language should be credited as a reformulation and refinement of this framework unless a separate novelty check establishes more. [S5]

For general spectra, Keller–Mossel–Schlank already give a marginal-entropy/influence bound. The 2025 Li–Han note announcing the same elementary inequality is withdrawn and expressly credits that antecedent. Bounds valid for all real unit-norm functions cannot remove the Boolean difficulty: a normalized sum of \(n\) characters has entropy \(\log_2 n\) and influence one. [S6]

Kelman–Kindler–Lifshitz–Minzer–Safra obtain improved spectral concentration, including a \(2^{O(I\log I)}\) scale at constant variance. A proposal to remove logarithmic losses must specify the exact entropy or concentration theorem, its error dependence, and the indicator/sign normalization; concentration on most of the mass is not automatically a Shannon-entropy bound. [S7]

## 3. Route A: adaptive physical restrictions, retaining the actual mismatch

### Exact starting point

Let \(S\) have the squared Fourier law and let \(g,h\) be the two physical restrictions at coordinate \(i\). The recovered proof gives

\[
\Delta_i H:=H(f)-\tfrac12(H(g)+H(h))
=H(S_i\mid S_{-i})+\operatorname{JS}(\widehat g^2,\widehat h^2),
\]

\[
0\le\operatorname{JS}\le\frac{2}{\ln2}\min\{\operatorname{Inf}_i,1-\operatorname{Inf}_i\},
\qquad I(f)=\operatorname{Inf}_i+\tfrac12(I(g)+I(h)).
\]

These are complete identities/inequalities in `recovered_brain/erasure_reduction.md`; full aggregate erasure control is open.

The newer local bound retains the discrepancy of the *actual* child amplitudes. Write \(a_T=\widehat g(T)\), \(b_T=\widehat h(T)\),

\[
q_T=(a_T^2+b_T^2)/2,\quad
m_T=(|a_T|-|b_T|)^2/4,\quad M=\sum_Tm_T,\quad\nu_T=m_T/M.
\]

For \(M>0\),

\[
\Delta_iH\le M\left[\log_2(1/M)-D_2(\nu\Vert q)+3/\ln2\right].
\]

At \(M=0\) the entropy decrement is exactly zero. This captures isospectral restrictions and avoids a substantial overcharge on symmetric and tensor examples. See the route map, Sections 2–3.

### Concrete work

Build a dynamic program over actual restrictions of small Boolean functions. Its objective is the upper bound from the displayed mismatch expression plus entropy bounds at certified stopping leaves. Record which coordinate or block pays each amount. Compare greedy choice with globally optimized trees and identify the smallest family where greedy selection fails. Test extensions of the already known semi-separated cases to one controlled cycle of shared variables; state the gate family, overlap graph, and inherited stopping hypothesis explicitly before attempting induction.

The intended analytical target for a declared class is

\[
\sum_{v\in\mathrm{internal}(T)}2^{-d(v)}M_v
 \left[\log_2(1/M_v)-D_2(\nu_v\Vert q_v)\right]
\le A I(f),
\]

with a separately paid terminal influence/entropy term. The \(3M_v/\ln2\) part is paid by the consumed physical influence because \(M_v\le\operatorname{Inf}_{i_v}(f_v)\). A proof for all Boolean functions would establish full FEI; it is not a weaker already-paid lemma. Computing exact entropy decrements and summing them to \(H(f)\) is a tautological diagnostic, not a new bound.

For a physical block \(A\), the Brain also proves

\[
H(f)-\mathbb E_XH(f_X)=H(S_A\mid S_{A^c})+I(X;S_{A^c}^{\rm restriction}),
\]

where the last variable is sampled from the restriction's spectrum. The channel term costs at most \((2/\ln2)I_A(f)\). This gives an exact way to test whether combining several related queries avoids a bad single-coordinate charge. A universal constant-cost proper-block selection theorem is still full-FEI strength; permitting the entire cube as the block simply restates FEI.

### Mandatory falsifiers and stop rule

Use the Brain's sparse activated bent perturbation, where both child influences tend to zero but \(H(S_i\mid S_{-i})/\operatorname{Inf}_i\) diverges. Any local multiplier bounded as the child influences vanish is dead. Also test bent/parity erasure synergy: one selector bit can create dimension-sized aggregate erasure while both children have zero erasure. A potential that discounts the complementary entropy cannot be justified by a fixed local selector charge.

Stop the proposed lemma immediately on either failure. If after two days no hypothesis distinguishes the candidate class from these examples, move the workers to another route rather than rename the residual. Useful success is a new hereditary class, a provably better coordinate-selection criterion, or an exact obstruction to a specific potential.

## 4. Route B: coding whole Fourier sets through tree covariance

### Target

Seek an explicit bound

\[
\operatorname{Cov}[T]
=\sum_{v}2^{-d(v)}\operatorname{Cov}(g_v,h_v)
\le A\log_2(k+1)I(f)
\]

for a read-\(k\) decision tree, or first for a carefully specified proper subclass. The logarithmic covariance target was already proposed in the coding literature; it is a meaningful improvement over the square-root baseline, not a new conjecture. [S1, S2]

The Brain separately records \(H(f)\le[\log_2\log_2 s+6.078\ldots]I(f)\) for at most \(s\) leaves. Do not repackage that as a read-\(k\)-only bound: \(s\) can still grow with the number of variables. Compare each candidate against the minimum of the existing parameter bounds.

### Concrete work

Partition repeated occurrences of a queried variable by their common-ancestor structure. Try to charge an occurrence *cluster* once, using covariance signs and cancellation; do not take absolute values at every node without proving the loss is necessary. First target trees in which repeated-occurrence subtrees form a laminar family or the variable-incidence graph has a single cycle. Determine whether those restrictions are substantive or just another encoding of a known read-once theorem.

The new queue witness in `joint_charging/variational_witness.tex` is a useful comparison tool: it prices roots, attachments, gate subsets, and ranks for an entire spectral set. Its addressing application is complete. The campaign should search for other explicitly defined families where these *particular* terms are paid together, rather than posit an arbitrary optimal reference law. Choosing the true spectral law as a reference gives entropy back; it does not construct an inexpensive code.

The code must be a valid normalized or subprobability law, or a decodable prefix code. Include its empty-set convention, rare-root normalization, and every attachment/label choice. Shared-variable products are coherent Fourier convolutions; \(H(fg)\le H(f)+H(g)\) is false there, although disjoint tensor additivity is valid.

### Success and stop rule

A logarithmic read parameter, a proved new overlap class, or an explicit joint-witness improvement beyond addressing is a significant result. End any argument that silently replaces coherent sums by a mixture, charges one root label for each coordinate, or drops the normalization cost. Record a counterexample to that step, not a claim that coding itself fails.

## 5. Route C: exact two-address product structure and collective wringing

Let \(A\) be a set of spectral coordinates. Consider genuine Boolean functions for which the conditional law of \(S_{A^c}\), given each positive-probability value of \(S_A\), is a product distribution.

The Brain already classifies zero-address product Boolean spectra: they are character translates of bent spectra and satisfy \(H\le2I\). It also proves the one-address endpoint with constant two. Two addresses already invalidate that constant: a recorded six-variable Boolean example has \(H=5\), \(I=17/8\), hence ratio \(40/17\). See route map Sections 9.1 and 9.4. None of these is a new campaign result.

**Candidate intermediate theorem:** prove \(H(f)\le C_2I(f)\) with some explicit finite \(C_2\), under the two-address hypothesis, or disprove a proposed finite parameter formula. More generally seek a controlled \(C(r)\) for \(|A|\le r\). Fixed \(r\) imposes an exact structural restriction; no reduction making the fixed-two-address problem equivalent to full FEI has been established in the recovered material. Verify this and prior art before claiming novelty. A constant independent of unrestricted \(r\) would of course recover full FEI by taking \(A\) to be all coordinates.

Work with the coupled partial Walsh projections \(g_T(x)\), not separately with their normalized spectra. They obey the exact pointwise identities

\[
\sum_Tg_T(x)g_{T\triangle U}(x)=\mathbf1_{U=\varnothing}.
\]

There is already a counterexample to bounding a *single* product projection's entropy by its normalized influence plus its own mass surprisal. Such a projection is multivalued, not Boolean. One-address arithmetic arguments also cannot be applied automatically after a normalization that destroys dyadic amplitudes.

The full collective wringing target from Section 9.3 is

\[
\sum_Tw_TH(q_T)\le K[I_{A^c}(f)+H(w)]+L\sum_Tw_T\operatorname{TC}(q_T),
\]

with \(w_T=\|g_T\|_2^2\). This sufficient target would yield full FEI with suitable constants in the existing wringing argument. Label it a full-strength open route. Proving its exact-product endpoint for two address bits is a more bounded question; it does not prove the approximate-product version needed for arbitrary functions.

**Experiments:** enumerate actual Boolean truth tables with the conditional-product property, using exact rank-one identities for probability arrays. Search larger examples through constructions preserving Booleanity. Record all row norms, signed all-shift equations, and conditional parameters. Never replace these equations by fixed-order moment constraints: the Brain contains dyadic, nearly Boolean nonexamples passing any preselected finite cancellation order while their entropy ratios diverge.

**Stop rule:** reject independent-row entropy arguments and approximate-independence claims based only on total variation or Hellinger error. The rare bent marker has tiny dependence but an unbounded local erasure/influence ratio. A useful ten-day outcome is a genuine two-address theorem, a sharp obstruction to a proposed \(C(r)\), or a necessary coupled arithmetic condition that excludes a previously admitted false proxy.

## 6. Route D: a bounded transport target at the existing noise-flow frontier

This is the most concrete auxiliary inequality left by the late Brain work. It should receive dedicated workers instead of starting another generic noise-semigroup derivation.

Use exactly the decaying-threshold policy in route map Sections 11.19–11.20: rate-one observations of occupied spectral coordinates, with a full reveal and removal when a posterior marginal reaches \(\epsilon e^{-2t}\). Both reveal outcomes count, cascades remove coordinates, and every history uses the same forward time parameter. Let \(P_t\) be the posterior active spectral law and \(J_0=\mathbb E|S_0|\). In this subsection, all entropies use **natural logarithms**. Set

\[
\operatorname{TC}(P)=\sum_iH(S_i)-H(S),\qquad
\operatorname{DTC}(P)=H(S)-\sum_iH(S_i\mid S_{-i}).
\]

**Candidate auxiliary theorem:** for fixed admissible \(\epsilon\),

\[
\int_0^\infty e^t\,\mathbb E\operatorname{TC}(P_t)\,dt
\le A_\epsilon[\operatorname{DTC}(P_0)+J_0].
\]

The existing weaker weighted bounds are already paid. The exact remaining identity is

\[
\int e^t\mathbb E\operatorname{TC}(P_t)dt
=\operatorname{DTC}(P_0)+\int e^t\mathbb E\Gamma(P_t)dt
-\mathbb E\sum_{\rm forced}e^\tau I(S_i;S_{-i}\mid\text{pre-reveal history}),
\]

where \(\Gamma=\sum_i\operatorname{Ent}(1-r_i)\) and
\(r_i=\Pr(S_i=1\mid S_{-i})\). The source already bounds the dissipation of \(\Gamma\); a bound on dissipation is not a bound on its lifetime. The refund at forced observations is essential.

This target can first be attacked for arbitrary small finite bit laws using rational probabilities. A uniform one-hot law has lifetime \(\Theta(\log n)\), but it also has \(\operatorname{DTC}(P_0)=\log n\); it does not refute the stated inequality. Search sparse-support laws, unequal one-hot laws, correlated rare clusters, and tensor products before introducing Boolean restrictions.

**Why it is worth doing:** the proposed result would strengthen a usable correlation budget. It does not by itself establish entropy transfer, actual Boolean source restoration, or FEI. This is a genuine auxiliary target rather than an equivalent renaming of the full conclusion. A proved counterexample would also be useful because it would identify the precise lifetime/refund interaction that future transport proposals must retain.

**Stop rule:** halt any proof that replaces the signed right-hand side by fresh per-ancestor influence budgets or discards the negative forced-information term while continuing to claim the same target. Distinguish finite-mesh algebra verification from proof of the infinite-horizon limit.

## 7. Route E: actual-source entropy transfer, with a strict scope boundary

The fixed-one-clock history route already has an exact full-strength remainder. For a Boolean source and its true history cost \(C_{\rm path}\), the Brain proves, in natural units,

\[
H_{\rm nat}(f)-3I(f)\le C_{\rm path}\le H_{\rm nat}(f)+I(f).
\]

It also has an equivalent integral of erasure entropies of actual biased-Boolean laws, \(Q_{\rm bias}\), and proves that its difference from \(C_{\rm path}\) is \(O(I)\). A universal linear bound for either is FEI-equivalent. The fixed-time laws preserve the full weighted Boolean identities and common ancestry; the individual evolving wavefunctions generally are not Boolean restrictions. See Sections 11.13–11.16.

The next step should be a source-sensitive transfer theorem that spends the already paid correlation reserve exactly once. It must preserve history probabilities, physical ancestry, the inverse condition number when undoing noise, and the error in the high-degree tail. Proposed scalar replacements already fail on actual late histories of small one-point defects and on addressing histories. Tiny current \(\operatorname{TC}\) does not imply inexpensive recovery of the initial source.

For a bounded intermediate target, extend the proven actual-history profiles for parity-address selectors with character leaves to a precisely defined non-character leaf family with a proved profile under every relevant bias. The current Brain already handles distinct overlapping data characters; that case is not new. A closure lemma for non-character leaves would test whether the history refund can survive genuine internal spectral entropy without assuming full FEI for the leaf.

The work product must display a profile whose time integral is finite, such as a proved bound by \(A e^{-t}(1+t)I(f)\) on the specified family, or another explicit integrable envelope. Testing only a fixed time or bounding the pivotal Jensen envelope is insufficient: on AND the envelope can cost order \(nI\), while the actual history refund is essential.

**Stop rule:** kill pointwise error estimates already defeated by the actual-history guards. Do not infer that integrated or ratio-critical variants fail unless the counterexample meets those additional hypotheses. After two days without a source-sensitive lemma beyond the existing paid bounds, keep this as a small high-risk team and move capacity to Routes B–D.

## 8. Structural reductions: useful screening, limited proof allocation

An equivalence team should inspect every “easier special case” before agents invest days in it. The recovered material gives the following classifications.

| Proposed restriction or payment | Correct classification |
|---|---|
| Aggregate erasure \(\sum_iH(S_i\mid S_{-i})\le K I\) for all Boolean functions | FEI-equivalent up to an explicit additive constant |
| Arbitrary rare activation or the subexponential low-influence class above | Full FEI retained; cite the existing reduction |
| Two physical selector cells with an arbitrary Boolean selector | Full FEI retained; the new exact selector identities give a tensor reduction |
| Even spectral support, or \(\sum_iH(S_i\mid S_{-i})=0\) | Not an easy terminal class: parity lifting embeds arbitrary functions with at most twice the influence |
| Full support and one Walsh-numerator valuation | Full FEI retained through padding and one-point surgery |
| Exact product spectrum | Already solved, constant two |
| Product conditional spectra after one spectral address bit | Already solved in the Brain, constant two |
| Exact two-spectral-address conditional-product class | Proper candidate class; constant two refuted; a finite general bound remains a bounded research target |
| Read-\(k\) covariance \(O(\log(k+1))I\) | Genuine parameter improvement over the existing bound |
| Weighted TC lifetime in Route D | Auxiliary technical conjecture; even success leaves entropy transfer unpaid |
| Universal min-entropy bound \(H_\infty\le C I\) | A weaker conjectural conclusion; no general equivalence to Shannon FEI is established here |

For minimal-counterexample arguments, state minimality precisely: immediate-child optimality, all-physical-descendant optimality, and minimum dimension are different. Signed-translation symmetries can be removed by zero-cost physical queries in the retained restriction framework. However, criticality does not pay the Brain's full-degree rare-row moment, and connected support does not justify Fourier entropy subadditivity. A proposed maximum-component *ratio* theorem was not refuted by the recorded component entropy counterexample, but needs its own normalization and proof. It is a lower-priority exploratory target, not an established reduction.

Do not allocate many workers to indiscriminate searches for high \(H/I\). The Brain already records millions of scored structured states with no new record. New searches should maximize the violation of a specified intermediate inequality; that gives a discriminating result even when the actual FEI ratio is modest.

## 9. Twenty mathematical cells, with five distinct roles per cell

This is a proposed allocation for 100 logical research roles. Each cell has a theorem author, an adversarial falsifier, a symbolic/computational worker, a prior-art/equivalence reviewer, and an independent proof reviewer. They should not all produce interchangeable prose about the same idea. Twenty recurring task identities can coordinate these cells if the platform actually permits the requested delegation; the operational plan must separately report observed concurrency and execution limits.

| Cells | Focus | Concrete checkpoint |
|---|---|---|
| 01–02 | Exact restriction mismatch; adaptive trees | An executable tree optimizer and one falsifiable structural lemma |
| 03–04 | Proper blocks and controlled overlap | A precise new class and a complete block/leaf budget |
| 05–07 | Read-\(k\) covariance and joint codes | Improved subclass theorem or certified obstruction to the proposed charge |
| 08–09 | Two-address conditional products | Exact feasible spectra, candidate \(C_2\), coupled arithmetic proof attempt |
| 10 | Collective wringing | One valid coupled-row estimate beyond the solved endpoints |
| 11–13 | Weighted TC lifetime | A proof or explicit finite-law counterexample with the refund retained |
| 14–15 | Actual-source entropy/history transfer | A new conditional profile or a counterexample meeting the advertised source scope |
| 16 | Minimal counterexamples and equivalences | Reduction map that rules out false shortcuts |
| 17 | General FMEI/concentration alternative | A precisely normalized improvement target with current literature checked |
| 18 | Exact experiment infrastructure | Reusable independent certificates for all route witnesses |
| 19 | Formal proof and dependency audit | Formalized reusable core and a reviewed hypothesis graph |
| 20 | Integration and adversarial review | Daily evidence-based reprioritization and final independent acceptance |

Roles can be serialized or reassigned. The number 100 is a capacity hypothesis, not a success metric. Correlated reasoning errors are a central risk; independence of formulation and verification matters more than the number of agents agreeing.

## 10. Ten-day sequence and acceptance criteria

**Days 1–2: recover and discriminate.** Freeze the theorem/dependency ledger, replay the exact counterexample corpus, and clear the prior art. Each proof cell must produce a fully quantified lemma, a smallest serious test family, and a statement of the missing payment. At the end of day two, pause duplicate formulations, known results, and claims already refuted by the corpus.

**Days 3–5: prove bounded results.** Invest most effort in the two-address class, read-parameter improvements, and the lifetime inequality. Route E remains a high-risk exploration. Every claimed lemma gets an independent derivation and a search specifically aimed at its hypotheses and limiting regimes. A failed lemma should produce a minimized exact witness and a narrower surviving question.

**Days 6–8: assemble or falsify.** Combine compatible lemmas only after checking units, bias conventions, physical versus spectral conditioning, and whether each budget has already been spent. Escalate a route toward a universal proof only if the final remaining term is explicitly bounded rather than renamed. Otherwise finish the proper-class theorem and record the full-scope gap.

**Days 9–10: freeze and audit.** Independent readers reconstruct proofs from definitions without author hints. Execute certificates from a clean environment, check serialized numeric enclosures, and produce a complete source/dependency index. Any proposed universal proof must survive the entire obstruction corpus and an independent line-by-line audit; empirical success alone does not qualify.

Meaningful possible outcomes are: a new class satisfying FEI with a complete proof; a sharper read-parameter theorem; a valid transport/correlation inequality; a formalized reusable analytic core; or a new exact obstruction eliminating an otherwise plausible universal approach. Full FEI remains the aim, but cannot responsibly be promised on a ten-day schedule.

## 11. Exact experiments and proof certification

Use direct Boolean truth tables or a construction with a proved Boolean output invariant. Integer Walsh transforms provide exact coefficients \(W_S/2^n\); all squared masses and influences are rational. Logarithmic inequalities need outward rational/interval enclosures and independently checked serialization. The Brain already found exported decimal intervals excluding the true values even when the underlying internal rational comparison was sound. Reproducing those bytes would not certify them.

Complete enumeration through four variables is feasible: there are \(2^{16}=65{,}536\) four-variable sign tables. Five variables already give \(2^{32}\) tables; do not describe an unperformed search as exhaustive. For larger dimensions use justified symmetry reduction, exact structured formulas, SAT/SMT enumeration with certified model reconstruction, or targeted randomized discovery followed by deterministic certification.

Every witness should include its full defining truth table or finite symbolic construction, coordinate and Fourier conventions, exact hypothesis checks, rational influence, certified entropy/inequality interval, and a minimal replay script. Distinguish discovery seeds from proof certificates and exhaustive domains from sampled families. A counterexample must satisfy the candidate's *full* scope, including criticality or source ancestry if asserted.

Formalization should start with high-reuse exact identities: Walsh Parseval, restriction coefficient identities, signed all-shift Booleanity, entropy chain rules, tensorization, and the local scalar inequalities. Continuous-time theorems additionally require their generator, finite-horizon identity, cascade treatment, and terminal limit. Formalizing a finite checker does not formalize the analytic theorem it supports.

Maintain a typed claim registry: **established literature**, **recovered proved result**, **new proof awaiting independent review**, **proper-class candidate**, **full-FEI-equivalent target**, **refuted**, and **finite evidence only**. Each claim has dependencies, scope, a source pin, and an owner. Publish progress by accepted claims and eliminated alternatives, not pages, agent-hours, or undifferentiated test counts.

## Sources and recovered starting files

Primary research, checked during this task:

- **S1.** Wan, Wright, Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture* (2013 preprint; 2014 conference paper): https://arxiv.org/abs/1312.3003 ; author-hosted full text https://www.cs.cmu.edu/~jswright/papers/readk.pdf . Browser references `turn33view0`, `turn29view2`.
- **S2.** Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, revised 24 January 2019: https://arxiv.org/html/1806.03646v2 . The arXiv version date, rather than a later date rendered inside the HTML body, identifies the revision. Browser reference `turn29view0`.
- **S3.** Arunachalam, Chakraborty, Koucký, Saurabh, de Wolf, *Improved bounds on Fourier entropy and Min-entropy*, revised 2021: https://arxiv.org/abs/1809.09819 . Browser reference `turn32view0`.
- **S4.** O'Donnell, Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (2013): https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf ; https://arxiv.org/abs/1304.1347 . Browser references `turn30search7`, `turn30search13`.
- **S5.** González, MacManus, Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (2026): https://arxiv.org/html/2606.00246v2 . Browser reference `turn29view1`.
- **S6.** Keller, Mossel, Schlank, *A Note on the Entropy/Influence Conjecture*: https://arxiv.org/abs/1105.2651 . Attribution confirmation and withdrawal notice: https://arxiv.org/abs/2512.03117 . Browser references `turn32view2`, `turn30search11`.
- **S7.** Kelman, Kindler, Lifshitz, Minzer, Safra, *Towards a Proof of the Fourier–Entropy Conjecture?*, revised 7 May 2020: https://arxiv.org/html/1911.10579v2 . Browser reference `turn32view1`.

Local recovered evidence, not claimed as newly replayed by this report:

- `recovered_brain/erasure_reduction.md`, `erasure_synergy.md`, `erasure_rigidity.md`, and `log_allocation.md`.
- `recovered_brain/solo-2026-09-17/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md`.
- `recovered_brain/research_pushes/2026-09-30-fei-current-route-map/REPORT.md`, especially Sections 2–6, 9.1–9.4, and 11.13–11.23. Its individual proof links pin the relevant source commits and distinguish unmerged draft results from published material.
- The two addenda in that directory on the critical rare-degree moment and connected-component entropy counterexamples.
- `joint_charging/selector_results.tex` and `joint_charging/variational_witness.tex`, which distinguish proved selector identities and addressing bounds from their universal unpaid obligations.

This report intentionally recommends work on the frontier left by these documents. It does not count rederiving their already established endpoints as a new mathematical result.
