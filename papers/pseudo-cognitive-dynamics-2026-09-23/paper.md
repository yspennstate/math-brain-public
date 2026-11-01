# Mathematics of Pseudo-Cognitive Dynamics

Persistent memory, error learning, and verifiable mathematical research in AI systems

23 September 2026

## Abstract

Mathematical research with language models requires continuity across finite contexts, preservation of failed arguments, reliable retrieval of assumptions, and evidence appropriate to each proof claim. We introduce *Mathematics of Pseudo-Cognitive Dynamics* as a proposed framework for studying the interaction between an active model context, called the conscious layer, and persistent external memory and control mechanisms, called the subconscious layer. These terms describe information flow and control; they do not assert subjective experience. Math Brain provides a concrete case study comprising typed mathematical objects, signed association graphs, mistake memories, retrieval hooks, consolidation proposals, audit records, and interfaces to Lean.

An artifact-based study of the available repositories finds substantial value for recalling project-specific knowledge and preserving corrections, together with important limits on claims of general reasoning improvement. A recent two-agent comparison scored 27/27 versus 1/27 on retained project-result questions and 27/27 in both arms on safeguard questions, at reported list-price costs of \$22.7979 and \$4.3693. Other proof-audit comparisons show small gains, null results, or contamination; an earlier favorable result was undermined by a placebo control. The archived usage ledger contains 375,282,198 output tokens and 123,820,924,963 input-token events over 32 days, mostly cache reads, but does not identify the all-time construction cost of Math Brain. Research case studies distinguish complete candidate arguments, partial results, rejected routes, and problems remaining open. Formal verification is scoped to the exact checked statement and cannot substitute for statement fidelity. We develop conditional mathematical results for bounded retrieval, stable activation, correction propagation, and cost amortization, and specify an evaluation protocol separating knowledge access, inference, reliability, and resource cost.

**Keywords:** external memory; mathematical reasoning; retrieval; proof verification; Lean; agent evaluation; error memory; cognitive architecture.

## Scope and research questions

An AI-assisted mathematical project often outlives the context in which its best ideas were found. Definitions change, an attractive proof route fails, a constant is corrected, and a later session encounters a similar problem without knowing which part of the earlier work survived. Persistent memory is valuable when it restores the relevant argument together with its conditions and verification state. Its value is reduced when it restores an obsolete conclusion, floods the context with unrelated material, or encourages an agent to treat repeated assertions as independent evidence.

This paper studies Math Brain as an engineered response to that problem. The mathematical subsystem stores claims, proof attempts, counterexamples, dependencies, sources, and verification records. The surrounding memory system provides session initialization, retrieval, salience, reminders, mistake detection, consolidation, and agent coordination. The active model performs the reasoning; the external system chooses what prior information and control signals become available to it. The repositories describe these mechanisms in executable code as well as design documents, and contain a substantial experimental history ([Math Brain project archive 2026d](#ref-mathreadme), [2026c](#ref-matharchitecture); [Brain project archive 2026e](#ref-broadarchitecture), [2026c](#ref-canonical)).

### The proposed field

We use *Mathematics of Pseudo-Cognitive Dynamics* for the study of coupled processes in which finite-context inference interacts with persistent, structured, selectively retrieved memory. Its objects include context states, memory revisions, retrieval policies, attention budgets, error histories, verification transitions, and resource costs. Its central questions are mathematical and empirical:

1.  Which stored information should enter the current context under a finite token budget?

2.  How should associations and recency affect retrieval without changing the evidentiary status of a claim?

3.  When does a remembered error prevent a new error, and when does it produce a false alarm?

4.  How should corrections propagate through a network of mathematical dependencies?

5.  What benefit remains after controlling for access to answers, extra computation, model identity, and evaluation leakage?

6.  Can the additional cost of retrieval, hooks, consolidation, and verification be justified by better research outcomes?

The field name is a proposal. The underlying ideas connect to established work in information retrieval, cognitive architectures, verification, optimization, and experimental design. Introducing a unified vocabulary does not establish priority over those fields. The mathematical results in Section <a href="#sec:dynamics" data-reference-type="ref" data-reference="sec:dynamics">3</a> are explicitly conditional models and adaptations of standard arguments; they are not offered as new solutions of the external conjectures discussed later.

### Conscious and subconscious layers

The *conscious layer* is the context actually available to the model for its current inference: instructions, selected history, retrieved records, tool outputs, and the current task. The *subconscious layer* is the persistent external machinery that stores, indexes, associates, filters, and proposes information for later inference. A stored fact becomes active when its representation is delivered into the context. A stored fact can also influence an external controller without its full text being delivered.

This definition follows an information-access boundary, not a filename. Some legacy files label high-priority external memories *conscious* and lower-priority external memories *subconscious*. In this paper both remain external memory until a particular representation is admitted to the current context. Conversely, a context can contain text about a dormant memory without containing its full proof. Context availability also does not prove that the model attended to, used, or understood that text ([Brain project archive 2026f](#ref-consciousness), [2026c](#ref-canonical)).

The analogy is functional. Human global-workspace theories study access and broad availability within biological cognition; complementary-learning-systems theory distinguishes rapid acquisition from slower integration ([Dehaene and Changeux 2011](#ref-dehaene2011); [McClelland, McNaughton, and O’Reilly 1995](#ref-mcclelland1995); [Shanahan and Baars 2005](#ref-shanahan2005)). Those theories motivate questions about selective broadcast and consolidation. They do not establish that a database is a hippocampus, a prompt is a human conscious experience, or an automated replay script implements sleep.

### Evidence and snapshot method

Three private source collections supply the principal artifact evidence: the mathematical memory repository, the broader memory and functionality repository, and the mathematical open-problems repository. The full frozen revision identifiers appear in Appendix <a href="#app:reproducibility" data-reference-type="ref" data-reference="app:reproducibility">9</a>. Individual source references identify the relevant file and revision. These repositories continue to change; the paper is a dated account, not a real-time dashboard.

The review examined architectural specifications and their implementation, benchmark reports and available row-level grades, token-ledger generation and aggregates, proof and audit artifacts, and current coordination records. Selected grade totals and usage sums were independently recomputed. A concrete defect in the current benchmark scorer was reproduced and a minimal correction tested with a synthetic fixture. Formal-source and build-log inspection was supplemented by small local parser and routing checks; no new language-model benchmark cohort and no fresh Lean kernel run are claimed.

The coverage is substantial but finite. The supplied research inventory preserves 1,391 physical catalog records from eight retrieved catalogs, with 1,168 distinct recorded identifiers and 223 repeated identifier occurrences. Identifier counts are not counts of unique mathematical problems: formulations overlap, versions recur, and deduplication keys can combine distinct clauses. Selected named cases receive substantive discussion, while the complete retrieved catalog is supplied as a machine-readable supplement. Source years in that catalog are not silently converted into conjecture-origin years.

Five evidentiary distinctions govern the analysis. A design specification establishes intended behavior; source code establishes an implemented path; an execution record establishes a particular observed run; a graded experiment estimates a performance contrast under its design; and a proof establishes precisely its stated mathematical conclusion. A status label or commit hash identifies a record without independently certifying its truth. These distinctions are already central to the project’s operating contract ([Brain project archive 2026c](#ref-canonical); [Math Brain project archive 2026c](#ref-matharchitecture)).

### Related computational methods

Retrieval-augmented generation connects language-model generation with retrieved external passages ([Lewis et al. 2020](#ref-rag2020)). Math Brain specializes this idea by representing assumptions, counterexamples, dependency relations, and evidence status alongside text. Reflexion uses linguistic feedback and episodic memory to improve later attempts ([Shinn et al. 2023](#ref-reflexion2023)); the mistake and scar layers serve a related purpose, with a stronger emphasis on explicit failure conditions and provenance. MemGPT studies management of limited context through external memory ([Packer et al. 2023](#ref-memgpt2023)). Generative Agents combine stored experience, reflection, and retrieval in a simulation setting ([Park et al. 2023](#ref-generative2023)). These are relevant precedents rather than controlled baselines for this particular system.

LeanDojo connects premise retrieval to formal theorem proving ([Yang et al. 2023](#ref-leandojo2023)). It illustrates why selecting relevant lemmas and checking a proof are distinct computational tasks. Research on long-context language models also shows that making information available in a large context does not guarantee uniform use of it ([Liu et al. 2024](#ref-lostmiddle2024)). Together these precedents support a research programme centered on useful selection, auditable feedback, and verification. They do not justify a claim that the present implementation is superior without a matched comparison.

## Architecture of the persistent mathematical brain

### The complete information cycle

The central mechanism is a feedback loop. A question activates retrieval cues. The external system finds candidate memories, follows selected associations, checks eligibility and provenance, and renders a bounded set of cards or warnings. The model then reasons with the resulting context. Its work produces new conjectures, proofs, calculations, failures, or corrections. Those outputs can become new persistent records, but mathematical status changes require evidence covering the corresponding claim ([Math Brain project archive 2026c](#ref-matharchitecture); [Brain project archive 2026c](#ref-canonical)).

<figure id="fig:cycle">
<p>The architecture diagram shows task and lifecycle events driving bounded retrieval; retrieved memory enters the active model context; reasoning produces actions and verification records; corrections and validated records return to persistent memory.</p>
<figcaption>Operational conscious–subconscious cycle. Consolidation proposes work; verification controls the evidentiary status of what returns to memory. Arrows describe the architecture, not proof that every deployment completes every stage.</figcaption>
</figure>

The surrounding system and the specialized Math Brain should be distinguished. The former includes broad memory, user context, operational reminders, and coordination. The latter isolates mathematical objects and verification rules. A comparison of the entire surrounding system against a minimal context measures a bundled intervention. It does not isolate the contribution of mathematical memory or any particular hook.

### Memory layers

| Layer                  | Representation                                                     | Function and evidentiary boundary                                                                    |
|:-----------------------|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| Layer                  | Representation                                                     | Function and evidentiary boundary                                                                    |
| Episodes and history   | Session records, prompts, prior revisions                          | Recover what happened. An utterance is evidence that it was made, not that it was correct.           |
| Reusable memory        | Dated topic records with descriptions and metadata                 | Preserve methods, decisions, rationale, and corrections across contexts.                             |
| Navigation             | Indexes, topic maps, links, backlinks                              | Find the relevant record without loading the whole archive.                                          |
| Salience               | Recency, curation, type, graph centrality, consequence scores      | Allocate attention. High importance does not raise truth status.                                     |
| Mistakes and scars     | Failure mechanism, minimal failing step, repair, counterexample    | Preserve negative knowledge and prevent a refuted route from being rediscovered as new.              |
| Instincts and reflexes | Cue, ordered checks, required evidence, stop condition             | Turn a lesson into a targeted action at the time it matters.                                         |
| Mathematical objects   | Definitions, claims, examples, lemmas, conjectures, proof attempts | Preserve quantifiers, hypotheses, constants, regimes, and exact dependencies.                        |
| Evidence               | Calculations, proof artifacts, citation locators, formal receipts  | Support a particular claim revision at a stated scope.                                               |
| Consolidation          | Review agenda, gists, link proposals, counterexample tasks         | Compress and connect records; proposed content remains subject to verification.                      |
| Coordination           | Leases, identities, handoffs, current work                         | Identify present ownership and progress. This state is distinct from durable mathematical knowledge. |

Memory layers and their computational purpose. Sources: ([Brain project archive 2026e](#ref-broadarchitecture), [2026f](#ref-consciousness), [2026c](#ref-canonical); [Math Brain project archive 2026c](#ref-matharchitecture)).

This layering addresses different failure modes. Episodic history prevents a summary from erasing the reason for a correction. Typed mathematics prevents a theorem from losing an essential hypothesis. Scar memory prevents a counterexample from becoming an inaccessible footnote. Navigation and salience keep useful material accessible under a finite context. Coordination reduces duplicated effort but cannot certify the mathematics produced by the workers.

### Hooks and delivery

A hook is a program invoked at a lifecycle event. The inspected settings route session start, prompt submission, pre-tool activity, post-tool activity, and session termination to appropriate handlers. A wake routine supplies continuity at session start. Prompt hooks can surface a relevant memory or mathematical card. Pre-tool hooks can warn before an action with a known failure mode. Post-tool hooks observe errors or co-read memories. Stop hooks retain unresolved obligations and continuation information ([Brain project archive 2026i](#ref-dispatcher), [2026t](#ref-wake), [2026k](#ref-instincts), [2026m](#ref-mathsense); [Cognitive Architecture repository 2026](#ref-proofhooks)).

These event boundaries are useful because the same information has different value at different times. A warning about a denominator is useful immediately before division; a warning about an unproved exchange of limits belongs near the limiting argument; a reminder to bind a proof to its source revision belongs near verification and publication. Repeating every warning in every prompt wastes context and can reduce attention to the relevant one.

The source records a concrete delivery limit: 646 of 1,009 prompt merges in one historical interval exceeded an inline bound, with a median payload near 53 KB. The revised dispatcher uses a 9,800-character inline allocation and retains overflow separately. Its water-filling policy preserves short messages and shortens large ones to available shares. Wake output is divided into two bounded parts ([Brain project archive 2026i](#ref-dispatcher), [2026t](#ref-wake)). These are character budgets, which must not be reported as model-token counts without a specified tokenizer.

The pipeline must be evaluated at successive boundaries: stored, indexed, retrieved, emitted, delivered, acted on, and outcome verified. Passing an early boundary does not establish the later ones. The mathematical-card hook illustrates the importance of this distinction. Its September 22 source diagnosis records 710 silent real-session invocations between September 15 and 22 because NumPy was unavailable under the dispatcher’s invocation mode, while ordinary-Python harness tests served cards. A source repair was added. This supports a documented deployment-path failure and repair; current end-to-end recovery still requires an observed delivery record ([Brain project archive 2026m](#ref-mathsense)).

### Salience and memory precedence

The implemented salience rule combines recency and persistence using a noisy-OR form: $$\begin{aligned}
R_i &= \exp(-a_i/\tau),&
P_i &= 1-\prod_j(1-c_{ij}),&
S_i &= 100\bigl[1-(1-R_i)(1-P_i)\bigr].

\end{aligned}$$ Here $a_i$ is age in days, and the components $c_{ij}\in[0,1]$ encode such signals as curation, backlinks, record type, and lexical consequence. The default recency parameter in the inspected code is $\tau=1.3$ days, with a rollback option to an earlier 45-day parameter. Example component values include 0.80 for curation and type priors of 0.90 for feedback/user records, 0.16 for reference records, and 0.07 for project records. Supersession reduces priority while preserving history ([Brain project archive 2026a](#ref-salience)).

The shape gives an enduring record a persistence floor even when its recency fades. These bounded scores are ranking heuristics, not calibrated probabilities of truth. Their historical calibration used 1,391 deliberate recall reads over 26 days, joined to 2,523 creation dates. Reported rates decrease sharply for new memories and then flatten, with a nominal short timescale of 1.3 days and a much slower tail. The study itself notes that observed reads depend on the existing retrieval policy ([Brain project archive 2026s](#ref-recency)). Thus the fitted curve estimates use under that policy; it is not an intrinsic forgetting law.

An audit also found a mismatch between the salience parameter and the legacy precedence classifier. A fixed recency threshold of 0.72, documented under $\tau=45$ days, corresponds under $\tau=1.3$ to an age of $-1.3\log(0.72)\approx0.427$ days. A threshold of 0.40 corresponds to about 1.191 days. Eligible short, uncurated project memories could therefore be demoted much sooner than the older comments imply. Curation and other exception paths limit the affected set ([Brain project archive 2026j](#ref-consciousnesscode), [2026a](#ref-salience)). This is an example of parameter coupling that a formal dynamics model can make explicit.

### Associations and pattern recognition

Co-reading provides one association signal. The inspected fold procedure keeps at most 40 distinct memories per session. A fold decays existing weights by 0.98 and adds $\min(1,6/n_s)$ to a co-read pair from a session containing $n_s$ memories, followed by a pruning floor. It uses stable identities and receipts to avoid replaying the same fold as fresh evidence ([Brain project archive 2026d](#ref-coactivation)). The decay is event-based. A busier fleet can therefore change the wall-clock retention rate even if the same decay parameter remains in the code.

The live general association hook performs two hops of degree-normalized propagation. In a source-faithful abstraction, an edge contribution is $$f_{i\to j}^{(h+1)}
=0.5\,a_i^{(h)}
\frac{w_{ij}}{\sum_k w_{ik}}
(1+0.4s_j)\gamma_j,$$ where $s_j$ is a severity signal and $\gamma_j$ is a possible topic gain. Repetition controls, salience thresholds, winner margins, supersession routing, and near-duplicate suppression determine whether a candidate is shown. Its trace retains the contributing bridge ([Brain project archive 2026p](#ref-spread)). Multiplying every outgoing weight at a node by the same positive constant leaves its normalized transition probabilities unchanged. More stored edge weight is consequently not, by itself, more effective retrieval.

Mathematical retrieval adds notation-normalized tokens, alpha-renamed formula fingerprints, and typed graph edges. Normalization helps match different variable names; it is not a theorem that two expressions are mathematically equivalent. An optional semantic channel uses normalized embedding vectors and positive standardized cosine scores. The live mathematical-card hook also uses lexical prefiltering and compact rendering, and labels population-store cards with their secondary or unverified provenance ([Math Brain project archive 2026b](#ref-mathretrieval), [2026g](#ref-semantic); [Brain project archive 2026m](#ref-mathsense)).

The system makes a valuable distinction between *discovery* and *proof dependency*. Discovery may traverse analogy and semantic similarity. A proof must identify exact assumptions and directed premises. The exact dependency-closure routine follows only the designated dependency edges and rejects missing nodes or cycles. Negative edges such as refutations receive positive visibility but retain a negative evidentiary meaning. A nearby counterexample should be easy to find without being mistaken for support ([Math Brain project archive 2026c](#ref-matharchitecture)).

### Scars, instincts, and calibrated warnings

A scar is a persistent record of a failure and its generating condition. An instinct is a compiled cue-to-check policy. The mathematical mistake schema includes the claim, failure class, minimal bad step, cause, repair, affected assumptions, and optional counterexample. Its reflex schema adds activation cues, ordered checks, required evidence, and an explicit stopping condition ([Math Brain project archive 2026h](#ref-mistakes), [2026e](#ref-triggers)).

Examples include requiring a nonzero denominator, checking a sign after squaring, naming the convergence theorem before exchanging limits, writing quantifiers and their negations, and distinguishing a finite computation from a universal argument. A useful scar says why a step fails and when that reason applies. A vague instruction to be careful has little diagnostic value.

Warnings can also be harmful. They can interrupt a sound proof, retrieve an analogy whose hypotheses differ, or cause an agent to reject a valid argument because it resembles an old failure. The broad instinct layer ranks and limits warnings, records the triggering channel, and suppresses repeated delivery ([Brain project archive 2026k](#ref-instincts)). In an internal study of 91 corrections, graph clustering produced groups whose modularity was not unusual under a degree-preserving null (reported $z\approx-0.9$). Those groups can organize records without constituting established natural classes of mistakes ([Brain project archive 2026r](#ref-mistakegraph)).

### Familiarity, forecasts, and self-monitoring

The feeling-of-knowing probe searches descriptions and filenames before reading complete memory bodies. It uses distinctive terms, bounded typo correction, and a cluster threshold, with salience as a secondary ranking signal. Its appropriate interpretation is that the corpus appears to contain relevant material. It is not evidence that the model knows a theorem or can prove it. The inspected probe is expressly silent on mathematical arguments, leaving that task to specialized proof routing ([Brain project archive 2026g](#ref-fok)).

The forecasting component stores dated probabilities and resolves them against observed outcomes. It uses Brier loss $(p-o)^2$ and realized self-information $-\log_2 p_o$. A per-scope hit rate is shrunk toward a global base rate $g$ as $(h+4g)/(n+4)$, with small samples marked provisional ([Brain project archive 2026n](#ref-prediction)). These scores can evaluate forecasts about runtime reliability or a task outcome. They are not proof probabilities for mathematical theorems.

The architecture also uses signals described as affect, charge, surprise, danger, or conscience. Their operational roles are attention, routing, rechecking, persistence, and stopping. This separation matters: a high-consequence failure may warrant stronger review without making the remembered factual claim more probable. Repeated surprise can justify examining an alternative model; it cannot determine a theorem’s truth by itself ([Brain project archive 2026e](#ref-broadarchitecture), [2026c](#ref-canonical), [2026o](#ref-reconsolidation)).

### Consolidation and coordination

The general system uses background agendas and model-assisted synthesis to produce gists, links, and review tasks. The mathematical package imposes a stricter boundary: its deterministic consolidation function returns quarantined proposals. Contradictions, missing evidence, reflex rehearsal, isolated nodes, and hub review receive explicit priorities. Analogy proposals use abstract mathematical structure, but cannot promote themselves to verification evidence ([Math Brain project archive 2026f](#ref-consolidation)).

The agent mesh separately tracks identities, leases, current tasks, messages, and acceptance of handoffs. Durable lessons pass through a memory-writing interface; routine activity remains transient coordination. A separate global-workspace component has source and design documentation, but its wiring record still reports an uncompleted integration gate. Current broadcast deployment is therefore not established by those files ([Brain project archive 2026b](#ref-mesh), [2026h](#ref-globalworkspace)).

The current mathematical repository describes itself as a coordination archive and explicitly does not claim native ingestion of newly produced research across all scheduled runtimes. This is compatible with historical experiments using a local populated store. Version, corpus, runtime, and delivery evidence must therefore accompany any assertion that an agent was connected to Math Brain ([Math Brain project archive 2026d](#ref-mathreadme)).

## A mathematical framework for pseudo-cognitive dynamics

This section formalizes the architecture and derives consequences under stated assumptions. Some equations describe implemented rules; other operators are proposed abstractions. None of the propositions establishes an empirical improvement in mathematical ability. Their purpose is to make budgets, stability, evidence flow, and possible failure modes explicit.

### State, retrieval, and external learning

<div class="definition">

**Definition 1** (Pseudo-cognitive state). *At event time $t$, let $$Z_t=(C_t,M_t,W_t,G_t,L_t).$$ Here $C_t$ is the active context, $M_t$ the persistent memory records, $W_t$ an association graph, $G_t$ the mathematical claim and evidence graph, and $L_t$ an append-only event and resource ledger. The context has serialized token length $\ell(C_t)\leq B$. A memory record contains content, applicability conditions, provenance, a revision identifier, and an evidence state.*

</div>

An event $e_t$ may be a question, tool result, error, checkpoint, or scheduled review. A hook generates a query and available memory budget. Retrieval and packing give $$q_t=H(e_t,C_t),\qquad
R_t=\mathcal{R}(q_t,M_t,W_t,G_t;b_t),\qquad
\widetilde C_t=\operatorname{Pack}_{B}(C_t,R_t).$$ The model generates an action $a_t\sim\pi_\theta(\,\cdot\mid\widetilde C_t)$; observations and checks then update external state: $$(M_{t+1},W_{t+1},G_{t+1},L_{t+1})
=U(Z_t,e_t,R_t,a_t,y_t,V(y_t)).$$ In this model $\theta$ is fixed. Learning occurs through external records, associations, retrieval policies, and procedures. External learning and model-weight training are different resource and attribution categories.

A retrieval budget should include the serialized wrapper and metadata, not only the body of a memory. If mandatory context has length $m_t$ and response reserve $o_t$, the available budget is $b_t=B-m_t-o_t$. It exists only when this quantity is nonnegative. A packing operator that accepts a block only after checking the length of the full resulting serialization preserves $\ell(\widetilde C_t)+o_t\leq B$ by induction over accepted blocks. This simple invariant prevents silent budget overflow; it says nothing about the quality of what was retained.

### Salience is bounded and saturating

<div class="proposition">

**Proposition 2** (Noisy-OR salience). *For $c_1,\ldots,c_m\in[0,1]$, let $F(c)=1-\prod_{j=1}^m(1-c_j)$. Then $F\in[0,1]$, is coordinatewise nondecreasing, and the increment from adding a further component $d\in[0,1]$ is $$F(c_1,\ldots,c_m,d)-F(c_1,\ldots,c_m)
=d\prod_{j=1}^m(1-c_j).$$ This increment decreases when any existing component increases.*

</div>

<div class="proof">

*Proof.* Every factor $1-c_j$ lies in $[0,1]$, proving the bounds. Increasing a component decreases the residual product. The displayed identity follows by factoring that product, and proves the final assertion. ◻

</div>

Equation <a href="#eq:salience" data-reference-type="eqref" data-reference="eq:salience">[eq:salience]</a> is of this form, with recency as an additional component and a scale factor of 100. A union-probability interpretation would require suitable independence assumptions; the ranking rule does not supply them. In particular, backlinks, repeated reading, and curation can be correlated consequences of the same original attention. Treating their combined salience as independent verification would count the same evidence repeatedly.

### Association growth and time

<div class="proposition">

**Proposition 3** (Forgetting with bounded reinforcement). *Let $w_{t+1}=\rho w_t+\eta_t$, where $0\leq\rho<1$, $w_0\geq0$, and $0\leq\eta_t\leq K$. Then $$w_t=\rho^tw_0+\sum_{j=0}^{t-1}\rho^{t-1-j}\eta_j
\leq \rho^tw_0+K\frac{1-\rho^t}{1-\rho}.$$*

</div>

<div class="proof">

*Proof.* Repeated substitution gives the equality. Bounding each reinforcement by $K$ and summing the geometric series gives the inequality. ◻

</div>

For a single-session reinforcement bounded by one and decay $\rho=0.98$, the limiting bound is 50. If a fold processes several sessions, $K$ must bound their total contribution; one must not apply the single-session numerical bound to an arbitrarily large batch. Pruning can reduce the bound but does not establish a fixed wall-clock forgetting rate.

Suppose an unreinforced weight undergoes $N(T)$ folds during a physical interval of length $T$. Its value becomes $\rho^{N(T)}w_0$. Thus two fleets with different fold counts forget at different rates even under identical parameters. A proposed time-normalized alternative is $w(t+\Delta)=e^{-\lambda\Delta}w(t)+\eta(t,\Delta)$. This keeps the passive decay independent of event frequency, but the usefulness of either rule requires a matched comparison.

### Stable activation under a sufficient condition

<div class="proposition">

**Proposition 4** (Contractive activation). *Let $P$ be a nonnegative matrix with every row sum at most one. Let $\sigma:\mathbb{R}^d\to\mathbb{R}^d$ be coordinatewise clipping to $[0,1]$. For fixed $b$ and $0\leq\alpha<1$, define $$T_b(a)=\sigma(\alpha Pa+b).$$ Then $T_b$ has a unique fixed point $a^\ast(b)$, iterations converge to it, and $$\left\lVert a^\ast(b)-a^\ast(b')\right\rVert_\infty
\leq \frac{\left\lVert b-b'\right\rVert_\infty}{1-\alpha}.$$*

</div>

<div class="proof">

*Proof.* Clipping is nonexpansive and $\left\lVert P\right\rVert_\infty\leq1$. Therefore $\left\lVert T_b(a)-T_b(a')\right\rVert_\infty\leq\alpha\left\lVert a-a'\right\rVert_\infty$. The cube $[0,1]^d$ is complete, so the contraction theorem gives a unique fixed point and convergence. For two fixed points, the triangle inequality gives $\left\lVert a^\ast(b)-a^\ast(b')\right\rVert_\infty
\leq\alpha\left\lVert a^\ast(b)-a^\ast(b')\right\rVert_\infty+\left\lVert b-b'\right\rVert_\infty$. Rearranging proves the sensitivity bound. ◻

</div>

This is a sufficient-condition model, not a convergence theorem for every inspected hook. The actual two-hop rule contains severity and topic gains, which can destroy the stated row-sum bound; it also stops after a finite number of hops. The distinction is useful: a proposed indefinitely iterated activation process must control total gain, while a finite-depth search must control depth, candidate count, and score sensitivity.

If all final candidate scores change by at most $\varepsilon$, a unique winner whose original margin exceeds $2\varepsilon$ remains the winner. Indeed, its decrease is at most $\varepsilon$ and a competitor’s increase is at most $\varepsilon$. This elementary fact explains why explicit winner margins can stabilize retrieval, although it does not establish that the chosen memory is correct.

### Selecting useful context under a budget

Consider a finite set of candidate cards and a task with a finite set of nonnegative-weight obligations $u\in\mathcal U$. A memory card $i$ is assigned coverage $a_{ui}\in[0,1]$. As a proposed approximation to useful coverage, define $$F(S)=\sum_{u\in\mathcal U}v_u\max_{i\in S}a_{ui},
\qquad F(\varnothing)=0,\quad v_u\geq0.$$ Repeated cards about the same obligation produce diminishing gains. This model does not include misleading cards or synergistic proofs requiring several premises simultaneously; those effects require a richer objective.

<div class="proposition">

**Proposition 5** (A standard greedy guarantee for the coverage model). *For an integer $k\geq1$, repeatedly add a card of largest marginal increase in $F$, until $k$ cards have been selected or no candidate remains. Early stopping is also allowed when every remaining marginal gain is zero. If $S_g$ is the resulting set and $S^\ast$ maximizes $F$ among sets of size at most $k$, then $$F(S_g)\geq\bigl[1-(1-1/k)^k\bigr]F(S^\ast)
\geq(1-e^{-1})F(S^\ast).$$*

</div>

<div class="proof">

*Proof.* The maximum for each obligation is nondecreasing as cards are added. Its marginal gain from adding a fixed card decreases as the selected set grows. Hence $F$ is monotone and submodular. At any step with selected set $S_j$, submodularity and monotonicity give $F(S^\ast)-F(S_j)\leq\sum_{i\in S^\ast\setminus S_j}
[F(S_j\cup\{i\})-F(S_j)]$. There are at most $k$ terms. Greedy therefore gains at least $(F(S^\ast)-F(S_j))/k$. Iterating the resulting deficit inequality from $F(S_0)=0$ proves the first bound. The inequality $(1-1/k)^k\leq e^{-1}$ proves the second. ◻

</div>

This is the classical cardinality-constrained submodular argument ([Nemhauser, Wolsey, and Fisher 1978](#ref-nemhauser1978)), applied to a proposed context-selection model. It is not a new optimization theorem and not an established model of this system’s real utility. It applies directly to equal-cost slots. Arbitrary token lengths create a knapsack constraint, for which the same simple cardinality proof does not apply. Harmful or complementary information can also violate monotonicity or submodularity. These limitations matter more than the attractive approximation constant.

### Proof dependencies and correction propagation

<div class="proposition">

**Proposition 6** (Compositional assumption tracking). *Let a finite acyclic graph represent exact formal propositions. Suppose each node $v$ has a checked derivation of $P_v$ from its immediate premises and a recorded assumption set $A_v$. Then $P_v$ follows from the union of $A_u$ over the premise ancestors of $v$, including $v$.*

</div>

<div class="proof">

*Proof.* Order the graph topologically. At a node without premises, the conclusion follows from its own assumptions by hypothesis. At a later node, substitute the already established premise derivations into its checked derivation. The required assumptions are contained in its own set and the ancestor sets of its premises. Induction proves the claim. ◻

</div>

This standard composition principle clarifies why the memory representation must preserve hypothesis direction and statement identity. A formally checked implication containing the desired theorem as a hypothesis is still conditional.

When a premise revision is refuted or withdrawn, the appropriate response is to flag the derivations that depend on that revision for revalidation. The smallest such set closed under downstream dependency is its reachable dependent set: reachability is closed, and any closed set containing the changed node must contain every node along each path. Marking that set does not prove all those conclusions false. Another proof may survive, a stronger premise may be unnecessary, or a replacement revision may repair the derivation. Revision-specific dependency tracking preserves those distinctions.

### When a scar can help

Suppose a narrowly defined warning is relevant with probability $p$ on a specified task distribution. Conditional on relevance, it prevents a failure with probability $r$ and avoided loss $L$. On irrelevant cases it causes a harmful intervention with probability $f$ and loss $H$. If delivery has cost $c$ in the same utility units, its expected net value in this simplified model is $$V=prL-(1-p)fH-c.$$ The warning is beneficial exactly when this expression is positive. This identity makes specificity, uptake, false alarms, and overhead separate measurable quantities. A count of delivered warnings does not estimate any one of them.

There is no general theorem that more memory improves reasoning. For a single task, take a baseline policy that answers correctly and a memory-conditioned policy that follows an incorrect retrieved statement. Retrieval lowers correctness from one to zero. Any improvement guarantee therefore needs assumptions about admissibility, applicability, selection, and the model’s response. The empirical studies below test particular interventions under particular conditions.

## Lean, algorithms, and mathematical audits

### The division of responsibility

Memory helps a mathematical audit by recovering relevant definitions, theorem hypotheses, earlier failures, and precise source locations. The model still has to decide whether they apply. Numerical tools test examples and find counterexamples; symbolic tools establish identities within their domains; Lean checks an encoded statement against its formal dependencies; a fidelity review compares that statement with the intended mathematics. These activities support different conclusions ([Lean Language Reference 2026](#ref-leanref); [Math Brain repository 2026b](#ref-leanarchitecture)).

For example, a finite search can refute a universal statement by finding one valid counterexample. A finite search with no counterexample proves a universal claim only if it exhausts the admissible domain or a complete reduction to that search is established. A failed Lean tactic can reflect an unavailable lemma, syntax error, timeout, or poor proof search; it does not refute the target theorem. A successful Lean proof can establish a weaker or different theorem than the prose if the translation is wrong.

The archive’s specialized proof hook converts recurring failure types into a small audit packet. It selects cues involving named-theorem applicability, inequality direction, quantifiers, constants, load-bearing assumptions, and limiting targets, and produces a step inventory. It limits repeated delivery and explicitly warns that retrieved notes themselves require applicability checks ([Cognitive Architecture repository 2026](#ref-proofhooks)). This is a direct operational example of subconscious-to-conscious transfer: previous errors determine what the next audit is prompted to inspect.

### The isolated mathematical authority

The isolated package has an unusually strict formal-verification path. Its inspected project pins Lean 4.30.0 and accepts a narrowly defined local source graph. It stable-reads and snapshots source bytes, uses a direct pinned executable, compiles in dependency order, records exact declaration names, and binds source, toolchain, execution, and output identities. The authority route requires canonical axiom reports for the named declarations and an empty reported axiom set ([Math Brain repository 2026b](#ref-leanarchitecture), [2026d](#ref-leanimplementation)).

This policy is stricter than common Mathlib use. It is therefore misleading to merge the package’s rule with every research companion and call the whole project an axiom-free Lean system. The package’s own small formal library contains three elementary natural-number controls. Those controls exercise the verification mechanism; they are not a formalization of the research programme ([Math Brain project archive 2026a](#ref-leannatural); [Math Brain repository 2026c](#ref-leancontrols)).

The package separates automated kernel evidence from formalization-fidelity evidence. The latter records review of quantifiers, domains, definitions, assumptions, conclusions, boundary cases, and extra assumptions. The records are bound to exact claim and source revisions. Cryptographic receipts can bind those fields to an issuance path, but do not make an inaccurate human translation correct. Imported peer reports remain discovery material until the appropriate local verification path supplies evidence ([Math Brain repository 2026d](#ref-leanimplementation); [Math Brain project archive 2026c](#ref-matharchitecture)).

### The broader Mathlib checker

The surrounding brain has a different checker using a local Mathlib project. Its parser permits the conventional Lean axioms `propext`, `Classical.choice`, and `Quot.sound`, while rejecting placeholders such as `sorryAx` and custom axioms. Its receipt retains an unverified translation-fidelity field. This path supplies valuable formal evidence, but its assurance conditions differ from those of the isolated package ([Brain project archive 2026l](#ref-leanbroad), [2026q](#ref-leanparser)).

The distinction can be expressed as three questions. Did the intended executable check the exact source? What proposition and assumptions did it check? Does that proposition faithfully express the research claim? The first is execution provenance, the second formal correctness, and the third semantic fidelity. A rigorous audit records all three.

<div class="tabularx">

p0.25rYY Inspected companion & Named reports & Checked content & Remaining scope  
Free unimodality & 13 & Polynomial/rational identities, profile bounds, equality cases & Probability measures, free convolution, parametrization, full theorem  
Arc-transitive graphs & 17 & Blow-up arithmetic, cycle sums, hitting-mass formulas & Identification with stochastic quantities and graph hypotheses  
Degree counts & 17 & Stage arithmetic, mass and centering bounds, exponent identities & Full conditional probability argument and limiting statement  
Bernoulli convolution & 25 & Separate seven-file summary of conditional algebra/analysis & One-copy absolute continuity and the unresolved contraction step  

</div>

These companions show a practical use of formalization even when an entire research proof is not encoded. A delicate coefficient identity or polynomial inequality can be isolated and checked. That removes one class of algebraic uncertainty and allows the informal review to focus on measure-theoretic hypotheses, conditioning, limiting arguments, and interpretation. The value comes from knowing which part was checked.

### Environment-specific integration

Inspected scheduled records from September 21 report missing Lean and mathematical-package dependencies in several Linux accounts. Some records show zero of three genuine formal controls completed while a synthetic containment or executable-transport test passed. The production POSIX lease in the inspected isolated implementation also marks executable locking as unenforced, which prevents authority eligibility under its own rules ([Math Brain repository 2026a](#ref-leanblocked), [2026d](#ref-leanimplementation)).

These are dated, environment-specific observations. They coexist with successful research-companion build logs elsewhere. They justify neither a claim that Lean never worked nor a claim that all workers were fully connected. A formal-system audit must identify the machine or runtime, exact toolchain, source revision, named declarations, dependency assumptions, and receipt.

For this paper, 11 local receipt-parser controls and a proof-hook routing check with one positive and two negative inputs were run successfully. These checks test parsing and routing. A Lean executable was unavailable in the review environment, so the historical kernel checks were inspected rather than rerun. The reproduction supplement records that boundary.

### A complete audit workflow

A useful workflow begins with an exact mathematical statement and an obligation inventory. Each obligation receives an appropriate check, and each check records its scope. A proof that depends on an external theorem retains that theorem’s source, statement, and hypotheses. A counterexample is stored with admissibility conditions. A formalization retains its informal counterpart and any extra assumptions. A correction creates a new revision and triggers review of dependent derivations.

Independent review is strongest when the reviewer reconstructs a load-bearing step from the original assumptions or uses a different method. Several agents repeating the same derivation can detect typographical errors, but agreement does not eliminate a shared conceptual mistake. Likewise, a majority vote is a record of opinions, not a proof. The architecture’s evidence graph is useful precisely because it can preserve the source of each review instead of reducing all agreement to one confidence score ([Brain project archive 2026c](#ref-canonical); [Math Brain project archive 2026c](#ref-matharchitecture)).

Memory supports this workflow through continuity and targeting. It can warn that a previous argument reversed an inequality, that a formal lemma assumed the desired conclusion, or that a conditioning step destroyed independence. The audit must then test the warning against the current argument. A sound use of scars is to focus attention on a possible failure, followed by a mathematical decision.

## Evaluation methods and observed performance

### What each kind of test measures

The archive contains several different evaluation families. Retrieval tests ask whether a target record appears in the returned set. Private-knowledge tests ask for facts or source locations available in the project’s memory. Proof-audit tests ask whether a mathematical argument is valid and, if not, where it first fails. Scar tests ask whether an agent avoids a known practical trap. Infrastructure tests exercise schemas, isolation, parsers, provenance, or runtime delivery.

These endpoints should not be merged into one accuracy number. A system can retrieve a remembered answer perfectly without improving deduction on an unseen theorem. It can pass a parser test while a production hook fails to import a dependency. It can improve recall while increasing total cost. The methodology must preserve the question each test was designed to answer.

A planted-error bank typically begins with a correct proof, changes a line or assumption, and asks the solver to identify validity and the first error. Mutation operators include sign changes, quantifier swaps, altered hypotheses, theorem substitutions, limit changes, and constant errors. A valid key must establish that the mutation actually creates an error. Cosmetic changes, equivalent statements, or a renamed standard theorem are not necessarily mathematical defects. Clean items are essential because a detector that rejects everything can appear successful on a bank containing only invalid arguments.

The current 30-pair protocol illustrates this validity work. Its 20 proof audits were selected from a 4,144-item multidomain bank; the author reports excluding 13 of 28 flawed candidates because their changes did not create genuine errors. Ten further questions concern the project’s own mathematical results. These two strata intentionally measure different functions ([Math Brain project contributors 2026d](#ref-ab30prereg)).

### Interventions and control conditions

At least four comparisons occur in the records:

1.  Baseline context versus an added mathematical note.

2.  Relevant memory versus an irrelevant or generic placebo note.

3.  Extra retrieval versus no extra retrieval when both arms inherit ambient memory.

4.  The full surrounding brain, with hooks and broader tools, versus a restricted or safe-mode configuration.

The first measures the added-note intervention. The second helps distinguish note content from posture or formatting. The third measures incremental retrieval beyond a shared preload. The fourth measures a bundled assistance policy. A large difference in the fourth comparison does not identify the causal contribution of typed mathematical memory alone.

Controls in several earlier studies inherited standing files or indexes from the parent session. Asking a solver to ignore them is weaker than preventing access. The newest protocol starts the control outside the usual home directory in safe mode and probes the absence of automatic hooks and memory files in the starting context. However, the script permits local files and retains shell/read tools, so initialization separation alone does not establish filesystem isolation. Per-run access traces are still necessary ([Math Brain project contributors 2026d](#ref-ab30prereg), [2026b](#ref-ab30analyze), [2026e](#ref-benchmark_ab30run), [2026q](#ref-benchmark_contamination)).

### Comparative results

<div class="longtable">

\>

p2.75cm\>

p2.45cm\>

p2.35cm\>

p7.65cm

  
Date / study & Comparator & Brain / intervention & Interpretation and evidence  
  
Date / study & Comparator & Brain / intervention & Interpretation and evidence  
  
Jul 13; sealed repair & Empty packet; mean & Added packet; mean & Ten paired processes; weighted means, not success counts. Initial failed dispatch excluded; served identity unresolved. ([Math Brain project contributors 2026v](#ref-benchmark_jul13)).  
Aug 9; V5 & No notes/135 & Relevant notes/135 & 11 helped, 0 harmed. Store originals may occur in notes; later placebo test limits content attribution. ([Math Brain project contributors 2026aq](#ref-benchmark_v5raw)).  
Aug 9; V5 placebo & Deranged notes/48 & Relevant notes/48 & Same 48-item subset; both at ceiling. Not an independent replication of the full 135. ([Math Brain project contributors 2026ap](#ref-benchmark_v5)).  
Aug 9; MI-b1 & Deranged notes/14 & Relevant notes/14 & No-notes arm 10/14; clean 7/7 in all arms. Near ceiling and exploratory screening. ([Math Brain project contributors 2026ap](#ref-benchmark_v5)).  
Aug 9; WA-b1 & Deranged notes/10 & Relevant notes/10 & No-notes arm 8/10; clean 6/6 in all arms. Weight absence not established for every item. ([Math Brain project contributors 2026ap](#ref-benchmark_v5)).  
Aug 9; PR-b1 & Deranged notes/23 & Relevant notes/23 & No-notes arm 20/23; clean 12/12 in all arms. Exact fault localization; no content advantage. ([Math Brain project contributors 2026ap](#ref-benchmark_v5)).  
Aug 10; hard-b1 & No notes/8 & Relevant notes/8 & Faulted half only; 4 helped, 1 harmed. Clean 8/8 in every arm. ([Math Brain project contributors 2026u](#ref-benchmark_hardb1)).  
Aug 10; hard-b1 & Deranged notes/8 & Relevant notes/8 & Same eight faulted pairs; 3 helped, 1 harmed. One relevant note induced a false approval. ([Math Brain project contributors 2026u](#ref-benchmark_hardb1)).  
Aug 10; crossed c1 & No/deranged notes/6 & Relevant notes/6 & Faulted 6/6 and clean 2/2 in every arm; ceiling diagnostic. ([Math Brain project contributors 2026p](#ref-benchmark_c1)).  
Aug 17; analytical & Deranged notes/80 & Relevant notes/80 & 80 faulted pairs; 8 helped, 1 harmed. Only 18 no-notes fault items scored; not a complete off comparison. ([Math Brain project contributors 2026f](#ref-benchmark_analytic)).  
Aug 17; archive150 & Deranged notes/98 & Relevant notes/98 & 98 instance pairs from 150-item archive; 14 helped, 8 harmed. No valid no-notes arm; clean 21/24 on,24/24 comparator. ([Math Brain project contributors 2026g](#ref-benchmark_arch150)).  
Aug 22; bank300 & No notes/181 & Relevant notes/181 & 181 instance pairs within 300-item sample; 14 helped, 9 harmed. Bank not exhaustively tested. ([Math Brain project contributors 2026o](#ref-benchmark_bank300)).  
Aug 22; bank300 & Deranged notes/181 & Relevant notes/181 & Same 181 pairs; 18 helped, 8 harmed. Clean false positives 1/41 on,2/41 in both controls. ([Math Brain project contributors 2026o](#ref-benchmark_bank300)).  
Aug 22; packetB & No notes/24 & Relevant notes/24 & 24 faulted pairs after leakage-control exclusion; clean 24/24 all arms. ([Math Brain project contributors 2026ae](#ref-benchmark_packetb)).  
Aug 22; packetB & Deranged notes/24 & Relevant notes/24 & Same 24 faulted pairs; 0 helped, 3 harmed. Not an additional independent sample. ([Math Brain project contributors 2026ae](#ref-benchmark_packetb)).  
Aug–Sep; powered & Nominal no notes/358 & Relevant notes/358 & 358 instance pairs within 600 serves/arm; 21 helped, 19 harmed. Hooks in 407 off and 422 on serves; prespecified stop. ([Math Brain project contributors 2026af](#ref-benchmark_powered), [2026ai](#ref-benchmark_sterility)).  
Aug 22 campaign; B12 & No notes/179 & Base retrieval/179 & 179 complete fault pairs; 14 helped, 19 harmed. Marginal completion differed; clean FP 3/52 both. ([Math Brain project contributors 2026j](#ref-benchmark_b12)).  
B12; embedded & No notes/172 & Embedded retrieval/172 & 172 complete pairs; 12 helped, 17 harmed. Overlapping bank; comparison-specific denominator. ([Math Brain project contributors 2026k](#ref-benchmark_b12embed)).  
B12; embedded & Base retrieval/176 & Embedded retrieval/176 & 176 complete pairs; 17 helped, 18 harmed. Both have brain access. ([Math Brain project contributors 2026k](#ref-benchmark_b12embed)).  
B12; framing & No notes/178 & Framed retrieval/178 & 178 complete pairs; 11 helped, 21 harmed. Same developing bank. ([Math Brain project contributors 2026l](#ref-benchmark_b12frame)).  
B12; top-one & No notes/178 & Top-one retrieval/178 & 178 complete pairs; 16 helped, 15 harmed. Same developing bank. ([Math Brain project contributors 2026n](#ref-benchmark_b12k1)).  
Sep 7; literature100 & Nominal no brain/67 & Brain workflow/67 & 67 flawed items, ten shard agents/arm; 5 helped, 6 harmed. Clean FP 5/33 on,6/33 off. ([Math Brain project contributors 2026z](#ref-benchmark_lit100)).  
Sep 11; bank100 & Nominal no brain/100 & Brain workflow/100 & 5 helped, 2 harmed; clean FP 0/52 both. Bank reused in later runs. ([Math Brain project contributors 2026h](#ref-benchmark_b100_11)).  
Sep 11; harder35 & Nominal no brain/35 & Brain workflow/35 & 0 helped, 1 harmed; flawed 16/19 both. One on-arm clean false positive. ([Math Brain project contributors 2026r](#ref-benchmark_h35_11)).  
Sep 12; bank100 & Nominal no brain/100 & Brain workflow/100 & Same bank rerun; 4 helped, 1 harmed. Clean FP 1 on,0 off. ([Math Brain project contributors 2026i](#ref-benchmark_b100_12)).  
Sep 12; harder35 & Nominal no brain/35 & Brain workflow/35 & Same bank rerun; 5 helped, 1 harmed. On-arm clean shortfall was uncertainty, not a false accusation. ([Math Brain project contributors 2026s](#ref-benchmark_h35_12)).  
Sep 12; M3 v1 & Baseline posture/103 & v1 posture/103 & All arms have notes. 2 helped, 2 harmed; clean FP 0 baseline,1 v1. Selected reused 103-item set. ([Math Brain project contributors 2026aa](#ref-benchmark_m3posture)).  
Sep 12; M3 v3 & Baseline posture/103 & v3 posture/103 & All arms have notes. 5 helped, 5 harmed; clean FP 0 baseline,3 v3. Same 103 items as v1. ([Math Brain project contributors 2026aa](#ref-benchmark_m3posture)).  
Sep 12; M3 batching & 15-item shards/103 & 5-item shards/103 & Notes present with baseline posture in both. 3 helped, 0 harmed; item-level exact p=.25. ([Math Brain project contributors 2026ab](#ref-benchmark_m3shard)).  
Sep 11–12; locateL1 & Nominal no brain/60 & Final r5 retrieval/60 & 60 stored-value questions; 54 helped, 0 harmed. Tuned repeatedly on same bank; final on trajectory 38 to 57. ([Math Brain project contributors 2026w](#ref-benchmark_l1raw)).  
Sep 12; locateL2 & Nominal no brain/40 & Final r5 retrieval/40 & 40 page-location questions; wording/routing revised during same-bank development. ([Math Brain project contributors 2026x](#ref-benchmark_l2raw)).  
Sep 12; locateL3 & Nominal no brain/30 & Final r3 retrieval/30 & 30 two-source subtraction questions; same-bank on progression 4,13,30. ([Math Brain project contributors 2026y](#ref-benchmark_l3raw)).  
Sep 13; mixed1000 & Captured control/1000 & Inline brain notes/1000 & Eight agents total. All 462 gains in private page operations; proof audits 77/77 and SAW 300/300 both. ([Math Brain project contributors 2026ad](#ref-benchmark_onekraw)).  
Sep 22; harder35 & Nominal no brain/35 & Brain workflow/35 & Same harder bank; no discordant items. Both 18/19 flawed and 16/16 clean. ([Math Brain project contributors 2026t](#ref-benchmark_h35_22)).  
Sep 22; B12 H & Dbm25b retrieval/158 & Checklist H/158 & 158 complete pairs; 13 helped, 19 harmed. Both brain variants, not an off comparison. ([Math Brain project contributors 2026m](#ref-benchmark_b12h)).  
Sep 22; B12 H & No notes/155 & Checklist H/155 & 155 complete pairs; 10 helped, 17 harmed. Overlapping tasks with preceding contrast. ([Math Brain project contributors 2026m](#ref-benchmark_b12h)).  
Sep 22; W7 raw & Restricted control/79 & Full brain/79 & Initial blind grades; one contaminated item removed. 49 stored results,10 RMT-card questions,20 standard controls. ([Math Brain project contributors 2026at](#ref-benchmark_w7raw)).  
Sep 22; W7 final & Restricted control/79 & Full brain/79 & Same 79 items; six rows adjudicated after unmasking. Standard 20/20 both; RMT questions ask card contents, not conjecture solutions. ([Math Brain project contributors 2026ar](#ref-benchmark_w7adj), [2026as](#ref-benchmark_w7audit)).  
Sep 22; recall200 & Restricted control/200 & Full brain/200 & Private facts across domains; 134 helped, 4 harmed. Absolute wrong counts 17 on,16 off; ambient preload. ([Math Brain project contributors 2026ag](#ref-benchmark_recall200)).  
Sep 22; scars100 & Earlier NONE pass/100 & Later BRAIN pass/100 & One agent, sequential passes; 28 helped, 0 harmed. Order/carryover confounded; credits 77.5 vs 93.5/100. ([Math Brain project contributors 2026ah](#ref-benchmark_scars100)).  
Sep 22; two Opus & Restricted control/27 & Full brain/27 & 27 eligible scar items, three excluded. One 60-item batch agent per arm; shared ambient context. ([Math Brain project contributors 2026an](#ref-benchmark_tworesult)).  
Sep 22; two Opus & Restricted control/27 & Full brain/27 & 27 eligible house-math items, three excluded. Off also one partial and 25 abstentions; 26 helped, 0 harmed. ([Math Brain project contributors 2026an](#ref-benchmark_tworesult)).  
Sep 23; T1 facts & Restricted control/44 & Full brain/44 & Credit points. Full answers 13 vs 44; math subset 2.5 vs 8 credits. 40 answerable questions plus 4 false premises. ([Math Brain project contributors 2026aj](#ref-benchmark_t1)).  
Sep 23; T2 scars & Restricted control/16 & Full brain/16 & Credit points; both at ceiling. Preregistered house-score gain of at least 3 failed. ([Math Brain project contributors 2026ak](#ref-benchmark_t2)).  
Sep 23; T3 deep scars & Restricted control/16 & Full brain/16 & Strict credit points; core 15 vs 15.5. Preregistered four-point advantage failed; both inherit ambient context. ([Math Brain project contributors 2026al](#ref-benchmark_t3)).  

</div>

The table preserves the units, denominators, and qualifications of the recovered reports. Results are descriptive unless their experimental design supports stronger inference. The supplement expands the result inventory, source paths, and selected recomputations. Reused banks and related reruns are reported separately rather than pooled into a grand total.

### Knowledge access versus mathematical inference

The most striking score improvements occur where the answers depend on local project knowledge. In the September 22 two-agent comparison, the retained mathematical-result questions scored 27/27 with the brain and 1/27 in the restricted control, with an additional partial control answer and 25 control abstentions. Safeguard questions scored 27/27 in both arms. Six of the original 60 questions were removed as preload-contaminated. The experiment used one batch-answering agent per arm and unequal assistance/tool access ([Math Brain project contributors 2026am](#ref-twoopus)).

This is strong descriptive evidence that the configured system makes project-specific information available. It does not show that a model with access to the same source documents would be unable to derive or locate those answers. Nor does it show an improvement on the separate safeguard set, where both arms reached the ceiling.

A 1,000-item run similarly reports 1,000 full-correct answers in the brain arm versus 538 in the control. The inspected grades place all 462 gains in store-page metadata questions, while the proof and self-avoiding-walk slices were already perfect in both arms. That composition explains the aggregate; it cannot be described as 462 new mathematical deductions ([Math Brain project contributors 2026ac](#ref-benchmark_onek)).

The 200-question recall comparison reports 142 full-correct answers versus 12, but also 17 wrong answers versus 16 and 24 abstentions versus 127. The assisted system answered more questions. Its lower wrong-answer fraction among attempted answers conditions on a different subset and therefore is not a paired demonstration that every answered problem became safer. Ambient context contamination also limits the interpretation of the control ([Math Brain project contributors 2026ag](#ref-benchmark_recall200), [2026q](#ref-benchmark_contamination)).

### Mixed results on proof audits and scars

Several proof-audit comparisons have small favorable differences, while others show no reliable separation or a harmful effect. Ceiling effects make some apparent successes uninformative about the intervention. In the early 135-pair experiment, a perfect assisted arm initially suggested a benefit; a later placebo arm also reached the ceiling on its 48-item subset, undermining attribution to relevant mathematical content ([Math Brain project contributors 2026ap](#ref-benchmark_v5), [2026aq](#ref-benchmark_v5raw)).

The harder-35 comparisons show why clean and flawed items, false alarms, and exact localization must be retained. A warning tuned to an old failure can incorrectly flag a legitimate weakening of assumptions when that weakening is the theorem being proved. The proof hook’s own correction history records this mechanism ([Cognitive Architecture repository 2026](#ref-proofhooks)). Error memory must be tested for false positives as well as successful warnings.

The September 23 safeguard trials likewise separate recalled detail from changed behavior. A 16-item trial scored 16/16 in both arms. A second 16-item trial scored 15.5 versus 14 on a strict rubric, and 15.5 versus 15 on the core safeguard alone; its preregistered four-point advantage was not achieved. The brain arm often supplied more local history, but additional detail and additional safety are distinct outcomes ([Math Brain project contributors 2026ak](#ref-benchmark_t2), [2026al](#ref-benchmark_t3)).

### Statistical interpretation

For binary outcomes on the same $n$ tasks, let $b$ be the number solved only by the brain arm and $c$ the number solved only by the control. The paired accuracy difference is $(b-c)/n$. Under independent paired observations and the null that either arm is equally likely to win a discordant pair, conditioning on $b+c$ gives the two-sided exact sign/McNemar calculation $$p=\min\left\{1,\;
2\sum_{j=0}^{\min(b,c)}
\binom{b+c}{j}2^{-(b+c)}
\right\}.$$ For fractional rubric scores, a sign test on positive versus negative paired score differences addresses the frequency of wins rather than their magnitude. A zero stored after decimal rounding is not a mathematically zero probability.

The calculation alone does not validate the experiment. Hundreds of items answered by a few batch agents share context and prompting; variants from the same proof share content. Their effective units of replication are not necessarily independent items. Repeated tuning on a bank, selection after inspecting failures, unmasked adjudication, and contamination all affect interpretation. A small nominal item-level $p$ cannot repair those issues. Conversely, a nonsignificant difference does not establish equivalence.

The appropriate reporting unit includes the model and version, prompt and tool policy, memory snapshot, independent sessions, item families, clean/flawed counts, missing outcomes, grading process, exclusions, and costs. A future confirmatory analysis should use independent session replications and hold out problem families or sources, not merely renumber existing variants.

### The current 30-pair study and its audit

The current campaign preregisters one headless session per item per arm, 20 proof audits and 10 project-result questions, masked grading, token recording, and contamination exclusions. Its repository snapshot contains the protocol, bank, tools, and deviation record, but not final run summaries or graded results. The number of completed pairs cannot be recovered from that snapshot, and the study is not counted as a completed performance result ([Math Brain project contributors 2026a](#ref-ab30readme), [2026d](#ref-ab30prereg)).

The deviations are informative. A network-using pilot was stopped and excluded. Both arms were placed under a lower process priority. The cost analyzer was changed to read session-level `modelUsage`, because one example’s last-chain usage reported 912 output tokens whereas session-level usage reported 25,528. A live hook was changed during the study, and other sessions could alter the assisted system. Those facts require version and latency qualifications; unchanged output format alone does not prove that tokens or answers were unaffected ([Math Brain project contributors 2026c](#ref-ab30deviation)).

The present review reproduced a concrete scorer defect: it attempted a set union after converting the family names into a sorted list, causing a type error. Moving the union inside the sorting operation repairs this specific failure. A synthetic fixture verified both the combined and family summaries, and a separate check verified aggregation of session-level usage over two model entries. These are software checks, not additional mathematical trials.

Other analysis risks remain explicit in the handoff. The scorer does not automatically consume the contamination report, silently omits incomplete pairs, and permits duplicate grades to overwrite earlier entries. The main token summary includes successful runs, so a complete end-to-end cost report needs failed attempts, restarts, and pilots separately. These matters should be resolved or documented before final performance claims are made ([Math Brain project contributors 2026b](#ref-ab30analyze)).

## Construction effort and operating efficiency

### What the construction ledger actually measures

The available usage ledger covers Claude Code activity on one machine from August 9 through September 9, 2026. It combines construction, maintenance, research, evaluation, and other uses. Its values were recomputed from the stored daily and session TSV files. These aggregates agree exactly in all four token categories; the half-hour file independently reproduces the output total ([“<span class="nocase">Daily Claude Code usage ledger</span>” 2026](#ref-ledgerdaily); [“<span class="nocase">Session-level Claude Code usage ledger</span>” 2026](#ref-ledgersessions); [“<span class="nocase">Half-hour Claude Code output usage ledger</span>” 2026](#ref-ledgerhalf); [“<span class="nocase">Transcript-derived usage ledger construction program</span>” 2026](#ref-ledgerbuilder)).

<div id="tab:ledger">

| Recorded category               |    Token events |
|:--------------------------------|----------------:|
| Uncached input                  |       9,932,399 |
| Cache read                      | 122,293,331,806 |
| Cache creation                  |   1,517,660,758 |
| Generated output                |     375,282,198 |
| All input categories            | 123,820,924,963 |
| All input and output categories | 124,196,207,161 |

Exact totals in the available 32-day machine-wide ledger. These are not a Math Brain construction-only total.

</div>

The combined count describes token events. Cached prefixes can be processed repeatedly, so 124.196 billion events do not mean 124.196 billion distinct tokens of generated knowledge. Cache reads account for about 98.468% of the combined count; that is a token-event share, not a monetary cost share. The provider distinguishes uncached input, cache creation, and cache reads, and their prices differ ([Anthropic 2026](#ref-cacheofficial)).

The ledger represents 244,194 usage messages and 11,774 session rows. The documentation’s 11,999 transcripts scanned is a different quantity. Of the session rows, 2,124 have a synthetic model label and zero recorded token use; they must not be counted as paid inference sessions. The daily count of active sessions also cannot be summed to obtain a distinct-session total ([“<span class="nocase">AI usage ledger: scope and first-build documentation</span>” 2026](#ref-ledgerreadme); [“<span class="nocase">Session-level Claude Code usage ledger</span>” 2026](#ref-ledgersessions)).

The exact all-time cost of constructing Math Brain is *unidentified*. The ledger excludes dates outside its window and other providers or machines, and it does not label every request as construction, maintenance, or use. A generic home working directory accounts for approximately 79.976% of output, so directory names cannot recover the missing allocation.

The explicitly mathematical evaluation directories contain 22,689,548 output tokens. Explicit cognitive-architecture improvement directories contain 50,539,727, totaling 73,229,275 output tokens. These are identifiable directory-associated subtotals, not lower bounds on construction alone: evaluations and operation are included. They may overlap token costs reported by benchmark studies and should not be added to them without request-level deduplication ([“<span class="nocase">Session-level Claude Code usage ledger</span>” 2026](#ref-ledgersessions)).

### Accounting method and limitations

The builder scans local transcript files, accepts assistant records with usage and message identifiers, deduplicates globally by identifier, parses timestamps, and aggregates usage by session, day, and half-hour ([“<span class="nocase">Transcript-derived usage ledger construction program</span>” 2026](#ref-ledgerbuilder)). This is a useful privacy-preserving design because the exported ledger need not retain prompt or response text.

Its completeness is limited. The first observed duplicate wins without reconciling later usage updates. Identifiers are marked as seen before timestamp validation, so an invalid first record can suppress a later valid duplicate. The traversal order is not sorted. Missing files or invalid records are omitted, and a rebuild overwrites the aggregate from surviving transcripts rather than merging preserved historical coverage. The session model label is the most frequent label in that session, not a per-request allocation of mixed-model costs. These facts prevent exact invoice reconstruction from the aggregate.

An internal explanatory claim also failed reproduction: a 30,000-output-token cap per session per half-hour was said to affect 9% of active half-hours. The stored file instead contains 4,230 rows above that threshold, representing 22.862% of all 18,502 rows or 26.424% of the 16,008 positive-output rows. The 9% denominator is not identified by these files ([“<span class="nocase">AI usage ledger: scope and first-build documentation</span>” 2026](#ref-ledgerreadme); [“<span class="nocase">Half-hour Claude Code output usage ledger</span>” 2026](#ref-ledgerhalf)). This is an accounting correction, not a mathematical benchmark result.

### Measured cost of the completed two-agent comparison

The September 22 two-agent comparison provides an explicit operating-cost record. It contains one session per arm, each answering a batch. The brain arm had broader assistance and access, so the contrast is not an isolated intervention on one mathematical-memory component ([Math Brain project contributors 2026am](#ref-twoopus), [2026ao](#ref-twoopususage)).

<div id="tab:opcost">

| Category                 | Brain-assisted | Restricted control |
|:-------------------------|---------------:|-------------------:|
| Uncached input tokens    |            182 |                 16 |
| Cache-creation tokens    |      1,642,459 |            453,543 |
| Cache-read tokens        |     21,101,755 |            513,921 |
| Output tokens            |         79,228 |             51,104 |
| Total token events       |     22,823,624 |          1,018,584 |
| Reported list-price cost |      \$22.7979 |           \$4.3693 |

Session-level operating usage from the completed comparison. Total token-event ratio is approximately 22.407; list-price cost ratio is approximately 5.218; output-token ratio is approximately 1.550. These are different units.

</div>

These session totals cover the original 60-item batches, including the six subsequently excluded questions and the recorded outage/resumption effects. They are not costs allocated solely to the 27 retained mathematical questions. The records show a large private-result recall contrast together with higher token-event volume and API-equivalent cost. Whether that tradeoff is worthwhile depends on the task distribution. Recovering an unavailable theorem or avoiding a week of duplicated proof work may justify considerable overhead. A routine proof audit already solved by the control may not. These examples motivate a value analysis; they do not provide a measured monetary value for a theorem.

The ongoing 30-pair study reports approximately 100,000 starting-context tokens for the brain-on configuration and a much smaller safe-mode probe, as well as substantial hook latency on a saturated machine. Its README gives an example in which the mathematical answer card occupies only 1,818 of 45,227 hook characters. These are diagnostic observations in an unfinished campaign, not completed per-item cost estimates ([Math Brain project contributors 2026a](#ref-ab30readme), [2026d](#ref-ab30prereg)).

### A consistent efficiency criterion

Let $B_0$ be construction cost in a fixed unit, $D_i$ baseline cost to attain an accepted quality criterion, $S_i$ cost saved by useful memory, and $R_i$ extra retrieval, injection, consolidation, and verification cost. Then total memory-system cost is $$B_0+\sum_{i=1}^n(D_i-S_i+R_i).$$ It is lower than baseline exactly when $$\sum_{i=1}^n(S_i-R_i)>B_0.$$ This follows by subtracting the baseline sum. Under a stationary expected net saving $\delta>0$, expected break-even requires $n\delta>B_0$. Neither $B_0$ nor $\delta$ is identified for the full system by the available data, so no empirical break-even horizon is reported.

If the two systems have different success rates, cost alone is insufficient. Under a specified repeated-task distribution and ordinary law-of-large-numbers conditions, mean cost $c$ and acceptance probability $p>0$ yield long-run cost per accepted result $c/p$. The ratio must be evaluated on the same quality criterion and task population. A recall benchmark with private answers, a proof-audit bank, and an open-problem campaign do not share an interchangeable denominator.

Future accounting should attach request identifiers, provider and model versions, treatment arm, memory snapshot, cache categories, activity type, retries, failures, and review costs to every run. Solver-only and end-to-end costs should both be reported. List-price API-equivalent estimates should remain distinct from actual subscription expenditure or invoices. Deterministic retrieval may use no model-generation call, but its emitted text still occupies and may be billed as model context.

## Research programme and historical open problems

### What the research catalogue establishes

The recovered research programme includes exact finite certificates, restricted theorems, candidate answers to source questions, counterexamples, imported known results, and substantial unresolved conjectures. Its eight inspected intake queues contain 1,391 physical records and 1,168 distinct problem identifiers. Multiple identifiers can describe related or identical mathematical questions; an identifier count is neither a count of independent conjectures nor a count of solutions. The supplementary catalogue preserves original statements, versions, inherited status labels, source locations, and an explicit source-reported/unverified annotation. The 87 top-level ProofNet directories likewise include administrative and reused tracks.

Four claims must be kept separate: a result exists in a repository associated with the Brain; a worker queried the Brain; the retrieved content changed a research step; and a controlled comparison demonstrates improved research success. The first is common, the second is sometimes logged, the third has a few direct traces, and the fourth remains insufficiently measured for long-form original theorem proving. The isolated Math Brain’s own current deployment description distinguishes repository handoffs from verified native memory ingestion ([Math Brain project archive 2026d](#ref-mathreadme)).

### Open problems ordered by documented age

Table <a href="#tab:chronology" data-reference-type="ref" data-reference="tab:chronology">[tab:chronology]</a> orders prominent tracks by the documented formulation or publication date. Approximate age means 2026 minus that date, not time spent by this project. An older background theory does not make a recent specialized target equally old. Where the original formulation was not recovered, the date is qualified or left unknown. Status describes the inspected project and literature evidence; candidate manuscript claims have not all been independently refereed by this review.

<div class="longtable">

p0.17p0.26p0.51

  
Date / approximate age & Problem or track & Scope, mathematics, and remaining status  
Date / approximate age & Problem or track & Scope, mathematics, and remaining status  
  
/ 93 years & Hadamard existence & Explicit Paley formulation; 1893 determinant background is older. Full target open. Exact multiplier-orbit and row-sum sieves eliminate restricted circulant constructions ([Paley 1933](#ref-Paley1933); [“Hadamard P15 Exact-Construction Run, 16 September 2026” 2026](#ref-CaseHadamard2026)).  
1950 / 76 years & Hadwiger–Nelson & Plane chromatic number remains open. Exhausted 1,175 exact distance-three pairs in one gadget route; no six-chromatic graph in inspected run ([Exoo and Ismailescu 2018](#ref-Exoo2018NelsonHistory); [“Hadwiger–Nelson P19 Exact Gadget Exhaustion, 16 September 2026” 2026](#ref-CaseHadwigerNelson2026)).  
1964 / about 62 years & Černý reset words & Conventional origin; attribution has historical nuance. Canonical augmentation and extension sieves; full conjecture and complete four-letter size-eight cell unresolved ([Černý 1964](#ref-Cerny1964); [“Cerny P16 Exact-Enumeration Run, 16 September 2026” 2026](#ref-CaseCerny2026)).  
1964 background & Arnold diffusion & Exact project formulation is recent. Abstract transition/shadowing results retain a conditional global implantation bridge ([“Earlier Mathematical Research Solved Register” 2026](#ref-CaseBroadSolvedRegister2026)).  
1975 / 51 years & Binary LCS constant & Exact $\gamma_2$ open. Finite-state dependency-preserving bounds; microscopic strictification is not a substantial practical improvement ([Chvátal and Sankoff 1975](#ref-ChvatalSankoff1975); [“Ten-Track Mathematical Progress Register, 20 September 2026” 2026](#ref-CaseProgress2026)).  
1970s background; exact origin unknown & Bass–Quillen specialization & Original ramification/parameter scope unrecovered. Four-dimensional laboratory and kernel desaturation remain conditional; full target open ([“Bass–Quillen P02 All-Exponent Desaturation Report” 2026](#ref-CaseBassQuillen2026)).  
1991 publication / 35 years & Sidorenko & Date is documented publication, not proven first circulation. Exact three-block regular-host stability for $K_{5,5}\setminus C_{10}$; general target open ([Sidorenko 1991](#ref-Sidorenko1991); [“Quantitative Sidorenko Inequality for Equal Three-Block Regular Hosts” 2026](#ref-CaseSidorenko2026)).  
1994 chapters / 32 years & Aldous–Fill questions & Candidate counterexamples to specified arc-transitive and flow-diameter formulations; not every question in the monograph ([Aldous and Fill 2002](#ref-AldousFillBook); [“Arc-Transitive Aldous–Fill Counterexample Research Package” 2026](#ref-CaseArcTransitive2026); [“Aldous–Fill 4.49(ii) Ramanujan-Cone Counterexample Package” 2026](#ref-CaseFlowDiameter2026)).  
1994 source; earlier history & Baum–Connes & Universal target open. Fixed wreath-product degree-one subgroup already known and rank-two saturated ([“Baum–Connes P01 Terminal Handoff: Fixed Target Saturated” 2026](#ref-CaseBaumConnes2026)).  
1995 documented folklore / at least 31 years & Sharp Rademacher singularity & Exact prefactor open. Rank/entropy tools, finite geometry, and a retracted circuit lemma preserved in typed memory ([Kahn, Komlós, and Szemerédi 1995](#ref-KahnKomlosSzemeredi1995); [“Sharp Rademacher Singularity Campaign: Typed Mathematical Memory” 2026](#ref-CaseRademacherMemory2026)).  
1996 / 30 years & Fourier entropy–influence & Full conjecture open. Read-once $6.4573$ certificate; composition identities and counterexamples to stronger potentials ([O’Donnell and Tan, n.d.](#ref-ODonnellTanFEI); [“FEI Read-Once Interval Certificate” 2026](#ref-CaseFEIReadOnce2026)).  
1996 / 30 years & Nonamenable Cayley percolation & Universal $p_c<p_u$ open. Quantitative selected-generator family for $\mathrm{SL}_n(\mathbb Z)$ is a restricted project claim ([Benjamini and Schramm 1996](#ref-BenjaminiSchramm1996); [“Ten-Track Mathematical Progress Register, 20 September 2026” 2026](#ref-CaseProgress2026)).  
May 1999 manuscript / 27 years & Uniform-forest negative correlation & General finite-graph target open. Partition functions, deletion/contraction, and restricted proofs; forest and spanning-tree measures differ ([Pemantle 2000](#ref-PemantleNegativeDependence); [Grimmett and Winkler 2003](#ref-GrimmettWinklerForests); [“Ten-Track Mathematical Progress Register, 20 September 2026” 2026](#ref-CaseProgress2026)).  
2002 preprint / 24 years & Lyons entropy concavity & Conjecture 8.2 verified in the 2002 first preprint; later 9.2. Full target open. Four-site/Fourier cases and exact refutations of stronger auxiliary claims ([Lyons 2002](#ref-Lyons2002Preprint), [2003](#ref-Lyons2003); [“Lyons Entropy Continuation and Certificate Scope” 2026](#ref-CaseLyons2026)).  
2005 / 21 years & Bradley strong-mixing Q7 & Literal-question counterexample recorded; complete memo not independently rederived in this review ([Bradley 2005](#ref-Bradley2005); [“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2008 preprint / 18 years & Planar-percolation spectral entropy & Candidate $H(f_R)=O(R^2\alpha_4(R))$ from quadtree coding and spectral estimates; separate from full FEI ([Garban, Pete, and Schramm 2010](#ref-GarbanPeteSchramm2010); [“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2011 preprint / 15 years & Janson zero-radius condensation & Candidate negative answer to published 19.41/preprint 18.40 via uniform subsequential near-total windows; positive-boundary-mean question untouched ([Janson 2012](#ref-Janson2012); [“Uniform Condensation Windows for Zero-Radius Random Allocations” 2026](#ref-CaseJanson2026)).  
2011–2012 source / 14–15 years & Other Janson questions & Mixed candidate degree/width/allocation results and imported known height theorems. Numbering, moments, and subsequences require individual checks ([Janson 2012](#ref-Janson2012); [“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2013 / 13 years & Burdzy–Scheutzow 7.5 & Source-reported filling-scheme resolution; novelty constrained by related 2011 stationary-transport work ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2017 preprint / 9 years & Free-Brownian unimodality & Candidate sharp $t\geq D^2$; curvature, extreme-point reduction, subordination. Full analytic proof separate from Lean cores ([Hasebe and Ueda 2018](#ref-HasebeUeda2018); [“Sharp Free Brownian Unimodality Research Package” 2026](#ref-CaseFreeUnimodality2026)).  
2018 preprint / 8 years & Thévenin degree counts & Candidate non-Gaussian mixture counterexamples in two specified offspring regimes ([Thévenin 2018](#ref-TheveninDegreeCounts); [“Degree-Count Counterexample Research Package” 2026](#ref-CaseThevenin2026)).  
2020–2021 / 5–6 years & Multiplicative free Brownian motion & Source-reported two-atom counterexample; distinct from additive threshold question ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2022 / 4 years & Modulated queues; quasi-stationary distributions & Literal queue-comparison and rank-two distribution counterexamples; separate restricted positive comparison results ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2025 / 1 year & Salez cutoff formulation & Literal target retired after discovering the author’s later result; bounded-degree transitive-expander cutoff remains open ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026); [“Ten-Track Mathematical Progress Register, 20 September 2026” 2026](#ref-CaseProgress2026)).  
2025 / 1 year & Critical Allen–Cahn endpoint & Candidate Bessel-4 counterexample; analytic endpoint scope and checked algebraic core kept separate ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
2025 / 1 year & Wasserstein copula extremizers & External September 20, 2026 Ansari preprint claims resolution. Brain’s earlier attempted route receives no solution credit ([Ansari 2026](#ref-Ansari2026Copula); [“G0013 Mathematical Brain Usage Trace” 2026](#ref-CaseBrainUsageG0013)).  
2026 / weeks–months & Fresh urn, Lévy, frog and tree intakes & Mixed reductions, narrow refutations and pending proofs. Intake year need not be original problem year ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026)).  
Owner handoff September 22, 2026; external origin unknown & Three-eigenvalue quadratic-form density & Full indefinite product-density target open. September 23 scoped semidefinite and controlled-mixture theorems; correction ledger identifies missing bridges ([“Bounded Densities of Quadratic Forms: Scoped Research Release, 23 September 2026” 2026](#ref-CaseQFORMRelease2026)).  

</div>

### A direct trace of subconscious-to-conscious promotion

Four recorded retrieval events during the September 12 attack on a Wasserstein copula question illustrate both useful and unproductive memory access. One recalled scar about reversing an inequality direction led the worker to recheck whether a perimeter comparison supplied a lower or upper bound. The log records a changed local research step, with no change of overall route. The other three events produced no reported proof change, with silence or unrelated material among the responses. This is an observable instance of a persistent mistake record becoming a context-visible checking action. Four observational calls do not estimate a theorem-solving success rate or net token savings ([“G0013 Mathematical Brain Usage Trace” 2026](#ref-CaseBrainUsageG0013); [“G0013 Second Mathematical Brain Usage Trace” 2026](#ref-CaseBrainUsageG0013Q2)).

The same case illustrates why literature reconciliation belongs in memory maintenance. Jonathan Ansari’s independent September 20, 2026 preprint claims the sharp inequality $W_2^2(C,\Pi)\leq 1/10$ for bivariate copulas, with equality at the Fréchet–Hoeffding extremizers. The paper attributes the conjecture to Catalano–Lavenant (2025). This external claimed resolution must receive external credit, even if an older project queue still lists the question as open ([Ansari 2026](#ref-Ansari2026Copula)).

### Fourier entropy–influence: composition and preserved counterexamples

For a Boolean function $f:\{-1,1\}^n\to\{-1,1\}$ under the uniform measure, let $p_f(S)=\widehat f(S)^2$. Parseval’s identity makes $p_f$ a probability distribution. Define $$H(f)=\sum_S p_f(S)\log_2\frac1{p_f(S)},\qquad
I(f)=\sum_S |S|p_f(S),$$ with the usual zero-term convention. The 1996 FEI conjecture asks whether $H(f)\leq C I(f)$ for a universal constant $C$. The retrieved current project state leaves the full conjecture open ([O’Donnell and Tan, n.d.](#ref-ODonnellTanFEI); [“FEI Current Shared Research and Correction State” 2026](#ref-CaseFEICurrent2026)).

The September 21 package reports an interval-certified bound $H(f)\leq6.4573I(f)$ for read-once formulas over AND, OR, and NOT. Its argument reduces composition to a two-variable inequality and covers the required domain with certified intervals. Read-once bounded-arity FEI is established prior mathematics; the project’s particular numerical certificate and scope should be assessed against that literature. A sharper numerical candidate near $6.4547837$ is not a proved optimal constant. A later attempted margin certificate fails at a displayed degenerate cell, so success on other cells cannot authorize the stronger theorem ([“FEI Read-Once Interval Certificate” 2026](#ref-CaseFEIReadOnce2026); [O’Donnell and Tan, n.d.](#ref-ODonnellTanFEI)).

The general research develops restriction identities expressing entropy changes through Jensen–Shannon divergence and conditional binary entropy. A potential-based induction would require, for an appropriate coordinate $i$, $$\Delta_i H\leq C\operatorname{Inf}_i(f)+\Psi(f)
-\tfrac12\{\Psi(f_{i=-1})+\Psi(f_{i=1})\},
\qquad 0\leq\Psi(f)\leq K I(f).$$ An admissible recursive choice and telescoping would yield $H(f)\leq(C+K)I(f)$. The existence of a universally valid potential is the central unpaid obligation, not a consequence of writing the template. Current records retain an 18-input counterexample to candidate coefficients $0.337/0.34$, a rare-suspension obstruction to an unweighted convolution payment, and a primitive-terminal counterexample to a raw $U_4$ inequality ([“FEI Current Shared Research and Correction State” 2026](#ref-CaseFEICurrent2026)).

The scientific value of the scar layer here is precise: it preserves the orientation, bias, and exceptional configurations that defeat attractive induction schemes. A short memory saying only that a potential “almost works” would actively damage future reasoning. A useful memory stores the failed inequality, its hypotheses, an exact obstruction, and the remaining valid subcase.

### Sharp Rademacher singularity: dependency graphs and retraction

The campaign targets $$\mathbb{P}(\det B_n=0)\sim 2n^2 2^{-n}$$ for an $n\times n$ matrix of independent symmetric signs. Repeated or opposite row and column pairs suggest the leading term. The unresolved issue is showing that all other dependencies contribute negligibly at that scale. The weaker exponential-base statement $(1/2+o(1))^n$ does not determine this prefactor ([Kahn, Komlós, and Szemerédi 1995](#ref-KahnKomlosSzemeredi1995); [“Sharp Rademacher Singularity Campaign: Typed Mathematical Memory” 2026](#ref-CaseRademacherMemory2026)).

The inspected local memory snapshot reports 325 mathematical objects and 602 dependency edges. Its object types include certificates, counterexamples, failed routes, lemmas, open gaps, and theorem objects; its status labels separately distinguish audited, exact, conditional, numerical, disproved, and open entries. Those database counts do not measure independent novel theorems. Reported mathematical tools include the entropy-sharpened residual-rank bound $d_{\mathrm{cb}}(A)\leq9\cdot4^\ell+\ell$, bounded-congestion quotient estimates, exact small-support geometry, and selector/transversality arguments. The final entropy-rigidity and probabilistic-transfer bridges remain open ([“Sharp Rademacher Singularity Campaign: Typed Mathematical Memory” 2026](#ref-CaseRademacherMemory2026)).

A Pasch counterexample invalidated an earlier audited-pass circuit claim and a counting consequence by an unbounded factor. The recorded response downgraded the relevant objects and retained the replacement gap. This is a concrete reason to make negative dependency edges and revision history first-class data. A retrieval engine that repeatedly serves the old audited label without the later counterexample would turn accumulated work into accumulated error.

### Lyons entropy concavity: the target survives failed sufficient conditions

For a finite positive contraction $Q$, write $P_Q$ for its determinantal-process law. Lyons’s conjecture asks whether $H(P_{(1-t)Q_0+tQ_1})$ is concave in $t$. Along a differentiable probability path $p_x(t)$ with positive coordinates, direct differentiation gives $$\frac{d^2H}{dt^2}
=-\sum_x\frac{(p_x')^2}{p_x}
-\sum_xp_x''\log p_x,$$ for natural-log entropy. The first term is nonpositive; the second has no automatic sign. The identity explains why a Fisher-information argument alone does not establish the conjecture ([Lyons 2003](#ref-Lyons2003), [2014](#ref-Lyons2014); [“Lyons Entropy Continuation and Certificate Scope” 2026](#ref-CaseLyons2026)).

The September 17 continuation reports restricted four-site/Fourier results, coupling concavity at fixed pair spectral means, and exact coefficient certificates. Its collection includes 75 polynomial identities and an extension with 21 more identities and 36 rational checks. Exact counterexamples refute stronger shuffle, resolvent, and partial-integral positivity statements. Those counterexamples invalidate routes toward the conjecture; they do not refute the original conjecture. The correct graph relation is “counterexample refutes auxiliary lemma used by target,” with the target still open ([“Lyons Entropy Continuation and Certificate Scope” 2026](#ref-CaseLyons2026)).

### Quadratic forms: new scoped bounds and the unrestricted gap

The current owner target concerns $$Q=X^\mathsf{T}AX+b^\mathsf{T}X+c,$$ where the coordinates of $X$ are independent with densities bounded by one, $A$ is real symmetric, and at least three eigenvalues satisfy $|\lambda_j(A)|\geq1$. The desired conclusion is a universal bound on $\left\lVert p_Q\right\rVert_\infty$. The September 23 release explicitly retains the unrestricted indefinite problem as open, despite a directory name containing “full-proof-paper.” Its manuscript presents complete proofs of scoped partial theorems and separate remaining endpoint problems ([“Bounded Densities of Quadratic Forms: Scoped Research Release, 23 September 2026” 2026](#ref-CaseQFORMRelease2026); [“Quadratic-Form Manuscript Source Scope and Correction Policy” 2026](#ref-CaseQFORMScope2026)).

##### Gaussian mixtures with controlled component peaks.

The release proves a bound for independent coordinate mixtures $$X_i=M_i+\sqrt{T_i}G_i,\qquad T_i>0,\qquad
\mathbb{E}T_i^{-1/2}\leq\sqrt{2\pi},$$ where the pairs $(M_i,T_i)$ are independent and the $G_i$ are mutually independent standard Gaussians, jointly independent of all mixture pairs. For $3\leq k\leq\operatorname{rank}A$, put $$Z_k=e_k(A^2)=\sum_{|I|=|J|=k}\det(A_{IJ})^2,
\qquad
\mathcal I_k=\int_0^\infty(1+u^{2k})^{-1/4}\,du.$$ The source theorem states $$\left\lVert p_Q\right\rVert_\infty\leq\mathcal I_k Z_k^{-1/(2k)},\qquad
\mathcal I_k=\frac1{2k}B\!\left(\frac1{2k},\frac14-\frac1{2k}\right)
<\frac{k}{k-2}.
$$ Thus the three-large-eigenvalue condition gives a constant strictly below three in this class ([“Gaussian Mixtures with Controlled Average Component Peaks” 2026](#ref-CaseQFORMGaussian2026)).

The proof conditions on the mixture variables, bounds the Gaussian quadratic characteristic function by a determinant, expands its elementary symmetric coefficient into squared minors using Cauchy–Binet, and combines weighted arithmetic–geometric mean with independent fractional moments. The resulting coordinate weights satisfy $0\leq\alpha_i\leq2$ and $\sum_i\alpha_i=2k$, so the moment exponents are at most $2/k<1$. This supplies the integrability needed for Fourier inversion. The beta integral follows from $v=u^{2k}$; splitting at one gives the simple bound $1+2/(k-2)=k/(k-2)$.

The average component-peak hypothesis is essential to the stated argument. For deterministic centers, a Gaussian scale mixture’s density cap is equivalent to the displayed negative moment condition. For random centers, many very narrow, widely separated components can produce a bounded marginal density while their average component peaks are large. Approximation by Gaussian mixtures therefore does not extend the theorem to every bounded density without an additional uniform estimate.

##### Semidefinite and other partial results.

The same release proves the dimension- and rank-independent bound $$\left\lVert p_Q\right\rVert_\infty\leq \frac{17100}{\lambda_3(A)}$$ for positive semidefinite $A$ with third largest eigenvalue positive, arbitrary affine term, and independent cap-one input densities. A negative-semidefinite analogue follows by sign reversal. Other scoped results concern an $O(\sqrt n)$ bound for arbitrary signatures, rank-two Riesz-potential estimates, physical-coordinate determinant bounds, spectral spread, hub conditioning, and fixed-matrix continuity. These do not yet close the universal indefinite target ([“Semidefinite Quadratic Forms and Spectral Spread” 2026](#ref-CaseQFORMSemidefinite2026); [“Bounded Densities of Quadratic Forms: Scoped Research Release, 23 September 2026” 2026](#ref-CaseQFORMRelease2026)).

##### What the mistake layer must preserve.

A bounded joint density in three dimensions is insufficient for the indefinite claim: a thin, volume-normalized shell around a quadratic cone can concentrate the pushforward on an arbitrarily short interval. This refutes a proposed joint-density coarea argument while violating the target’s product-law assumption. Rotating independent coordinates generally destroys independence. An unconditional projection cap is not a cap for every conditional distribution. Further corrections distinguish $\operatorname{diag}|A|$ from $|\operatorname{diag}A|$, interval estimates from domination on all Borel sets, and a singular-minor inequality from an invalid identity. Rough bounded densities also obstruct a proposed uniform pointwise Fourier-decay bound ([“Quadratic-Form Manuscript Source Scope and Correction Policy” 2026](#ref-CaseQFORMScope2026)).

These corrections are mathematically valuable because they locate the exact missing hypotheses. They explain why a memory system must retain a theorem’s domain, quantifiers, and exceptions alongside its conclusion. Their existence does not prove that a deployed hook reliably delivered each correction to every worker.

### Janson condensation: improving the statement as well as the proof

For nonnegative weights $w_j$ with $w_0>0$, a random allocation of $m$ balls into $n$ boxes has probability proportional to $\prod_iw_{y_i}$. Zero convergence radius means $\limsup_j w_j^{1/j}=\infty$. The September 17 draft claims that for every $\varepsilon\in(0,1)$ and $0<\alpha<\beta<\infty$, there are $\delta>0$ and supported $k_r\to\infty$ such that $$\sup\mathbb{P}\{Y_{(1)}\leq(1-\varepsilon)m\}\longrightarrow0,$$ where the supremum is over admissible integer pairs with $(1+3\delta)k_r\leq m\leq(1+5\delta)k_r$ and $\alpha\leq m/n\leq\beta$. Consequently, every full admissible path with $m_n/n\to\lambda\in(0,\infty)$ has a subsequence along which $Y_{(1)}/m_n\to1$ in probability and $L^1$. The draft identifies a universal sampling criterion $N_{j+1}/N_j\to1$ and explicitly leaves the distinct positive-boundary-mean problem untouched ([Janson 2012](#ref-Janson2012); [“Uniform Condensation Windows for Zero-Radius Random Allocations” 2026](#ref-CaseJanson2026)).

After normalizing $w_0=1$, its insertion argument preserves the entire truncated small-box partition function rather than comparing a large numerator with one selected denominator configuration. The finite insertion lemma specifies additional size and supported-residual hypotheses so that the falling-factorial count pays for the added boxes. Record-dependent tilts and record margins then create uniform mass windows. An older all-balls claim $\mathbb{P}(Y_{(1)}=m)\to1$ was false: factorial weights give a nontrivial limit $e^{-1/\lambda}$. Replacing it with a subsequential near-total-fraction statement changes the theorem, not merely its presentation ([“Uniform Condensation Windows for Zero-Radius Random Allocations” 2026](#ref-CaseJanson2026)).

The archive reports 18,000 sharp-insertion checks, 13,240 coarse checks, three labelled double counts, 84 tail checks, and 23,713 plane trees with 422 conditional-root identities. Such finite checks can detect wrong coefficients and boundary cases; they do not prove the limiting theorem. Five sequential same-assistant reviews are not five independent referees ([“Zero-Radius Condensation Audit Summary” 2026](#ref-CaseJansonAudit2026)).

### Further candidate contributions and exact certificates

##### Free-Brownian unimodality.

The Hasebe–Ueda source proves a sufficient threshold $t\geq4D^2$ for initial support diameter $D$. The project draft claims the sharp $t\geq D^2$, attained by a symmetric two-atom example. Cauchy-profile curvature and extreme-two-atom reductions feed into Biane subordination. This review distinguishes the full analytic claim from checked algebraic cores; the latter do not certify subordination or measure-theoretic regularity. The source’s displayed lower constant also requires normalization care: its support $\{-1,1\}$ has $D=2$ and transition $t=4$, yielding a ratio one ([Hasebe and Ueda 2018](#ref-HasebeUeda2018); [“Sharp Free Brownian Unimodality Research Package” 2026](#ref-CaseFreeUnimodality2026)).

##### Conditioned Galton–Watson degree counts.

The Thévenin campaign constructs two candidate counterexamples: a subcritical law with finite third moment and no exponential moment, and a critical law with infinite variance. Two giant-degree alternatives separated by order $\sqrt n$ induce an opposite-mean mixture of Gaussian limits for a normalized degree-one count. The mechanism shows why conditioning and rare-tail geometry cannot be inferred from a few finite moments alone. Exact small-$n$ dynamic programming and large-index arithmetic checks support internal calculations; the asymptotic analytic bridge requires its own proof ([Thévenin 2018](#ref-TheveninDegreeCounts); [“Degree-Count Counterexample Research Package” 2026](#ref-CaseThevenin2026)).

##### Sidorenko on a restricted continuum.

For $H=K_{5,5}\setminus C_{10}$ and symmetric nonnegative three-block host matrices with normalized row sums three, the project reduces a homomorphism inequality to a degree-at-most-15 polynomial with 664 monomials. After boundary parametrization and a fourth-order factor, 12,288 exact rational Bernstein coefficients have minimum $725117/3179904>1/5$. Bernstein basis functions are nonnegative and sum to one, so coefficient bounds certify every point of the covered cubes. This yields quantitative stability, including the reported bound $t_H(A)\geq1+\frac1{20}\left\lVert A-\mathbf 1\right\rVert_2^4$ in the source’s normalized coordinates. It is a continuum certificate in a restricted domain, not a solution for every graphon ([“Quantitative Sidorenko Inequality for Equal Three-Block Regular Hosts” 2026](#ref-CaseSidorenko2026)).

##### Aldous–Fill counterexamples.

Cycle blow-ups give explicit hitting and commute formulas for the precise arc-transitive source questions. A distinct Ramanujan-cone construction makes a flow/relaxation/diameter ratio unbounded. This is stronger than exhibiting one ratio slightly above two, which would only refute the constant two. Source-question fidelity determines what each construction resolves ([Aldous and Fill 2002](#ref-AldousFillBook); [“Arc-Transitive Aldous–Fill Counterexample Research Package” 2026](#ref-CaseArcTransitive2026); [“Aldous–Fill 4.49(ii) Ramanujan-Cone Counterexample Package” 2026](#ref-CaseFlowDiameter2026)).

### Remaining frontiers and the value of negative results

The September 20 frontier register records a binary LCS upper bound $0.8262759427622826$ and reference lower bound $0.792665992$, without determining the constant. For the negative spherical perceptron at $\kappa=-1$, it reports lower $6.30297437506$ and upper $12.3196348278$; a proposed third-lift value $12.28722223$ still needs its comparison theorem and root certificate. A random-3SAT candidate bound $4.3888762$ and integrated fractional-Brownian estimate $0.171587<\theta\leq1/4$ likewise retain their stated scope and unresolved exact targets. Selected Galton–Watson, Cayley percolation, and cutoff families do not settle the universal conjectures. For exponential first-passage percolation, the required strict defect $2\mu(e_1)-\mu(1,1)>0$ still has reported lower bound zero ([“Ten-Track Mathematical Compute Strategy, 20 September 2026” 2026](#ref-CaseComputeStrategy2026); [“Ten-Track Mathematical Progress Register, 20 September 2026” 2026](#ref-CaseProgress2026)).

Several exact research metrics remained unchanged: the inspected Hadamard run added no unresolved order; the Černý complete-size metric stayed seven; the tracked five-chromatic unit-distance graph remained at 509 vertices; and a fixed Baum–Connes subgroup was already saturated at rank two. Recording these outcomes prevents repeated expenditure on a completed restricted task or an exhausted search family ([“Hadamard P15 Exact-Construction Run, 16 September 2026” 2026](#ref-CaseHadamard2026); [“Cerny P16 Exact-Enumeration Run, 16 September 2026” 2026](#ref-CaseCerny2026); [“Hadwiger–Nelson P19 Exact Gadget Exhaustion, 16 September 2026” 2026](#ref-CaseHadwigerNelson2026); [“Baum–Connes P01 Terminal Handoff: Fixed Target Saturated” 2026](#ref-CaseBaumConnes2026)).

The broader archive also contains source-reported phase-retrieval exponents, minimum-square-submatrix asymptotics, overlap identities, and Plücker-coordinate extremal calculations. Its non-Gaussian transfer and conditional-overlap bridges remain explicit. Imported results on tree height, queue variability, or known finite constructions receive literature credit. Later adjudication corrects older minimal-spanning-forest and gossip-game cards, demonstrating that a “solved” label can become stale ([“Earlier Mathematical Research Solved Register” 2026](#ref-CaseBroadSolvedRegister2026); [“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026); [“Round-Five W7 Mathematical Benchmark Adjudication” 2026](#ref-CaseW7Adjudication2026)).

The mathematics therefore supports several distinct forms of value: stronger scoped bounds, exact certificates, reusable counterexamples, clarified conjectures, explicit missing bridges, and avoidance of false novelty. The paper supplies a research history and an evaluation programme for these benefits. It does not assign a monetary value to each theorem or attribute all associated mathematical progress causally to Math Brain.

## Discussion and a confirmatory research programme

### What the evidence supports

Math Brain provides a concrete setting for studying the proposed Mathematics of Pseudo-Cognitive Dynamics. Its central object is the interaction between an active context and a persistent external system. The conscious layer is the information presently available to inference; the subconscious layer retains and selects information that may become useful later. These names identify computational roles. The present evidence concerns availability, selection, action, correction, and verification, and does not establish subjective experience.

The strongest recovered performance contrasts concern access to project-specific knowledge. They show that the assisted configurations can recover information that restricted controls often lack. Proof-audit results are more heterogeneous, with favorable, null, ceiling-limited, and adverse outcomes. The measured operating comparison also incurs higher cost in the assisted condition ([Math Brain project contributors 2026am](#ref-twoopus), [2026ac](#ref-benchmark_onek), [2026ag](#ref-benchmark_recall200), [2026al](#ref-benchmark_t3), [2026ao](#ref-twoopususage)). Together these observations support a bounded claim: persistent mathematical memory can make accumulated research usable across sessions, while the size and direction of its contribution to new reasoning depend on the task, selected content, delivery, and verification policy.

The available studies do not establish universal token savings, uniformly better mathematical judgment, or a causal contribution to every result in the research archive. Nor does the existence of a sophisticated memory mechanism imply that it was active during a particular proof attempt. The recorded mismatch between successful harness retrieval and failed production injection makes that distinction operationally important ([Brain project archive 2026m](#ref-mathsense)). A useful explanation of success must follow the entire chain: a relevant record was retrieved, its representation reached the context, the agent used it appropriately, and the resulting claim survived verification.

### The scientific value of retaining conditions and corrections

The most valuable unit of mathematical memory is often a conditional argument. A lemma becomes reusable when its assumptions, conclusion, source, and proof obligations travel together. A counterexample becomes reusable when it identifies the precise generalization that fails. A correction becomes reusable when later sessions can distinguish the superseded revision from the statement that survived review. These properties make the archive useful even when it contains no solution of a major conjecture.

The separation between association and proof dependency is particularly important. A resemblance can suggest a method without licensing its application. A remembered concentration estimate may motivate an attack on a quadratic form, but its independence assumptions, normalization, and range must be checked in the new setting. Similarly, an earlier failed proof can expose a missing hypothesis without showing that every superficially related argument fails. The typed graph and scoped evidence records provide a way to retain these distinctions ([Math Brain project archive 2026c](#ref-matharchitecture), [2026b](#ref-mathretrieval), [2026h](#ref-mistakes)).

Formal checking strengthens this process when it is attached to an exact claim. A kernel-accepted identity can remove uncertainty from an algebraic step while leaving the surrounding analytic argument open. A checked implication can establish a reduction while leaving its principal hypothesis unproved. Formalization fidelity therefore remains a separate obligation: the domains, quantifiers, boundary cases, and assumptions in the formal statement must match the mathematical claim ([Math Brain repository 2026d](#ref-leanimplementation); [Brain project archive 2026l](#ref-leanbroad), [2026q](#ref-leanparser)). Scientific value comes from identifying what the certificate establishes and what further work remains.

The failure history is also part of the contribution. Rejected parameter changes, irrelevant warnings, invalid planted errors, and delivery outages reveal mechanisms that aggregate success counts conceal. Preserving them makes the next evaluation more informative and reduces the chance that a later agent repeats a previously refuted approach. Such records are evidence about a process; their repeated retrieval must not be counted as independent evidence for a theorem.

### A controlled content–delivery experiment

A confirmatory study should separate the value of the supplied information from the reliability of the machinery that supplies it. We propose a preregistered $2\times2$ design crossing *content* with *delivery*. Content is either a relevant, independently checked memory packet or a sham packet. Delivery is either manual provision or automatic hook provision.

The sham should contain mathematically sound but irrelevant material, matched as closely as possible for token length, formatting, source-label structure, and imperative tone. Deliberately false memories belong in a separately labeled robustness experiment. Otherwise, a treatment contrast can conflate useful memory with the control’s exposure to misinformation.

For the primary experiment, manual provision copies a frozen packet into context at a registered decision point; automatic provision relies on the hook to supply the same packet at the same point. Within each content condition the intended bytes are identical. This tests delivery reliability and overhead without silently changing the information or its timing. An additional no-packet control can estimate the burden of the sham itself. A later study may allow adaptive retrieval or voluntary memory consultation, but its treatment is then a broader selection-and-delivery policy.

The model version, reasoning configuration, tool set, source-access permissions, output allowance, and total compute envelope should be identical across cells. Memory, embeddings, indexes, hooks, and grading keys must be frozen before confirmatory runs. Both conditions should receive the same authorized mathematical reference materials except for the assigned packet. Private-result retrieval and unfamiliar proof reasoning require separate strata: withholding a private source creates a legitimate knowledge-access test, but does not identify an improvement in deduction.

Control cleanliness must be verified at runtime. Separate starting directories are insufficient if tools can still read a shared memory store. The harness should record loaded instruction files, effective hook settings, readable memory paths, tool accesses, and the exact context actually delivered. A receipt of emitted text is useful, but where the runtime permits it, the test should also verify what entered the model’s request. Delivery failures remain outcomes of the automatic policy rather than disappearing from the analysis. A secondary analysis restricted to successful delivery may diagnose the mechanism, but must not replace the randomized comparison.

### Replication, scoring, and cost

The evaluation bank should contain valid and invalid arguments, including boundary cases on which a broad warning could reject a correct proof. Independent mathematical review must establish the keys before treatment assignment. Holdouts should separate source documents and problem families, so a renamed variant of a tuned example does not become a new test.

Each item should receive repeated, independently initialized sessions in every condition, with randomized allocation and run order. No session should retain another condition’s answers or generate memories subsequently used by a paired run. Session replicas and problem families should remain visible in the analysis, instead of treating every answer from one long batch as an independent trial. Sample size, exclusion rules, stopping rules, and primary contrasts should be chosen before confirmatory outcomes are inspected.

Scoring should distinguish validity classification, localization of the first consequential error, explanation of the violated assumption, corrected conclusion, and confidence. Clean-proof false positives and incorrect confident answers should be reported alongside successful detections and abstentions. Retrieval hit rate, card delivery, and appropriate uptake are intermediate outcomes. Final mathematical correctness requires a separately reviewed rubric; where formal checking is used, statement fidelity must also be assessed. Graders should be masked to treatment, and disagreements should retain an adjudication record.

Every attempt should retain uncached input, cache creation, cache reads, generated output, provider-reported reasoning categories where available, tool computation, and wall-clock latency. Retries, failed hooks, restarts, timeouts, and adjudication should remain in an end-to-end account, with solver-only costs reported separately. The accounting boundary must prevent a retry from being counted as a new independent task or omitted because it produced no accepted answer. The recovered scorer and usage-analysis problems show why these requirements affect substantive conclusions ([Math Brain project contributors 2026b](#ref-ab30analyze), [2026c](#ref-ab30deviation); [“<span class="nocase">Transcript-derived usage ledger construction program</span>” 2026](#ref-ledgerbuilder)).

A prospective deployment study can then estimate net value on a declared task distribution. It should compare cost to reach the same acceptance standard, including the cost of false alarms, verification, and duplicated work. Construction and continuing maintenance can be amortized over the observed volume of use, with sensitivity analyses for future workload and model prices. Section <a href="#sec:costs" data-reference-type="ref" data-reference="sec:costs">6</a> supplies the accounting criterion; the present archive does not identify the parameters needed for an empirical break-even date.

### Questions for the proposed field

Several research questions follow from the implemented system. First, context selection must balance relevance against interruption and redundancy. A highly relevant lemma may be unusable if its hypotheses are clipped, while a short counterexample may be more valuable than a long affirmative summary. Models of context utility should therefore represent proof obligations and completeness, rather than equating similarity with usefulness.

Second, memory quality changes with use. Retrieval affects which records are read, reads affect association weights, and those weights influence later retrieval. This feedback can reinforce a useful method or a misleading hub. Evaluations should measure stability under corpus growth, new corrections, and changes in fleet activity, including the distinction between event-based and elapsed-time forgetting ([Brain project archive 2026d](#ref-coactivation), [2026p](#ref-spread), [2026a](#ref-salience)).

Third, error memory requires discrimination. A warning should identify a relevant failure condition and a concrete check. Its precision, uptake, and resulting correction can differ: a correct warning may be ignored, and an irrelevant warning may still induce extra work. These stages need separate observables before reflex quality can be optimized.

Finally, provenance and correction propagation deserve formal treatment. A system should make a withdrawn premise visible wherever its exact revision supports a derivation, while preserving conclusions supported by independent proofs. Consolidation should propose new connections without changing their evidentiary status ([Math Brain project archive 2026f](#ref-consolidation), [2026c](#ref-matharchitecture)). A mature mathematical memory system would combine this discipline with measured gains in accepted research output. The proposed field provides a language for investigating that combination; its success will depend on reproducible experiments and precisely stated mathematics.

## Reproducibility and evidence index

### Snapshot identity and coverage

The supplement records the evidence used for this paper at the following repository revisions. File-level citations and manifests identify the relevant paths and, where retained, content hashes. The two adjacent hexadecimal fragments in each table entry form one commit identifier.

<div class="tabularx">

p0.43Y Repository under `yspennstate/` & Frozen commit  
`math-research-brain` & `a4c99b43a044c127787c``26997ed942f41591aac6`  
`<private-repo>` & `bcff9346b68959f4cf33``0fdf9ca0e64a21c77d3e`  
`math-open-problems` & `b4745ece98fa3839cf7a``fe35d829d08384c815b4`  

</div>

The review used retrieved directories, source files, catalogs, reports, and selected row-level records. It does not claim that every file in these repositories, every historical revision, or every research proof was read or independently verified. Catalog completeness below refers to the eight retrieved input catalogs, not the entire research archive. Private repository citations remain subject to the reader’s access. The supplied aggregate data and offline software fixtures support a narrower, independently inspectable set of checks.

### Comparative evaluation records

The files `benchmark_comparisons.csv` and `benchmark_comparisons.json` contain 45 comparative rows. A row is a reported contrast or stratum, not necessarily an independent experiment. Related rows can reuse items, agents, controls, grading records, or intermediate versions. They must not be pooled as 45 independent trials or summed to obtain a unique task count.

Each row retains its endpoint, denominator, comparator, experimental unit, source URL, and design caveat. Where available, it also records discordant outcomes, score differences, nominal probabilities, and selected local recalculations. The source map and `recomputed_grade_totals.json` distinguish reported summaries from locally recounted grades. Recounting verifies arithmetic against a grade file; it does not independently establish the mathematical correctness of its key, the independence of responses, or the absence of contamination.

The principal design limitations remain attached to individual rows: ambient memory in a control, unequal tools or context, batch-level replication, reused banks, ceiling effects, and incomplete operating-cost telemetry. W7 retains the distinction between initially masked grading and later adjudication after unmasking. The posture comparisons retain their notes-present baseline rather than relabeling it brain-off ([Math Brain project contributors 2026at](#ref-benchmark_w7raw), [2026ar](#ref-benchmark_w7adj), [2026as](#ref-benchmark_w7audit), [2026aa](#ref-benchmark_m3posture)). The unfinished AB30 study contributes protocol and software evidence, not a completed performance contrast ([Math Brain project contributors 2026a](#ref-ab30readme), [2026d](#ref-ab30prereg)).

### Usage reconstruction

The aggregate-only usage package contains `daily_usage.tsv`, `token_summary.json`, `half_hour_output_histogram.tsv`, and `recompute_usage.py`. Running the script verifies the daily file against its pinned Git blob, recomputes the four token categories and message total, and checks the output sum and cap calculation using the anonymous histogram ([“<span class="nocase">Daily Claude Code usage ledger</span>” 2026](#ref-ledgerdaily); [“<span class="nocase">Half-hour Claude Code output usage ledger</span>” 2026](#ref-ledgerhalf)). The histogram contains output amounts and frequencies without session identifiers or local project paths.

The script reports which quantities cannot be reconstructed from these sanitized inputs. Distinct-session counts, directory attribution, original deduplication, and provider billing require further source records. Agreement between aggregates is evidence of arithmetic consistency, not complete transcript coverage. No all-time, cross-provider, or construction-only Math Brain token total is recoverable from the supplied record. Benchmark operating costs may already be represented in the broader ledger and cannot be added without request-level deduplication ([“<span class="nocase">Transcript-derived usage ledger construction program</span>” 2026](#ref-ledgerbuilder); [“<span class="nocase">Session-level Claude Code usage ledger</span>” 2026](#ref-ledgersessions)).

### Research inventory and chronology

The research supplement preserves 1,391 physical records from eight catalogs, a projection with 1,168 distinct recorded identifiers, and 223 occurrences beyond one per identifier. The last figure measures repeated records or versions, not 223 additional problems. Seven mirrored catalog files were excluded from a second count because their Git blobs matched the corresponding source files exactly. A separate inventory records 87 top-level ProofNet directories.

The identifier projection retains inherited status fields, source locators, version counts, and the explicit review label `SOURCE_REPORTED_UNVERIFIED`. Selecting the final observed row for an identifier does not certify that it is mathematically correct or globally current. Similarly, the directory inventory describes stored organization rather than solved-problem counts ([“Probability Campaign Index and Scope Ledger” 2026](#ref-CaseCampaignIndex2026); [“ProofNet Archival Manifest” 2026](#ref-CaseProofnetManifest2026)).

The reviewed chronology is separate from the full catalog. A source-publication year is not automatically the year an open problem was posed. Unverified origin years remain blank; documented formulation dates and uncertainty are retained. The case discussion distinguishes existence of a candidate proof, mathematical scope, novelty, verification, and evidence of actual memory-system use. A catalog status cannot replace any of those judgments.

### Fresh local controls and their limits

The `lean_controls/` package reproduces 11 receipt-parser controls and a proof-hook routing check with one positive and two negative inputs. Its result record is `lean_parser_controls_20260923.json`. These are fresh local Python checks. A parser accepting a supplied successful-build record does not establish that a Lean kernel ran; translation fidelity remains a separate field. The historical formal-companion logs were inspected, but no Lean recompilation was performed for this paper ([Math Brain repository 2026b](#ref-leanarchitecture); [Mathematical Research repository 2026c](#ref-freelean), [2026a](#ref-arclean), [2026b](#ref-degreelean)).

The `ab30_repair/` package retains the original analyzer, a one-line correction, a patch, source hashes, and a synthetic regression fixture. The fixture reproduces the original list–set `TypeError`, then confirms combined and family summaries after moving the union inside sorting. It also checks session-level token aggregation over two fabricated model entries. Its scores are deliberately synthetic and are not added to any benchmark denominator ([Math Brain project contributors 2026b](#ref-ab30analyze)).

The supplement README supplies commands and interpretation boundaries. Held-out answer keys, private transcripts, and raw session histories are excluded. Releasing an evidence package enables inspection; it does not demonstrate that another agent has read it, adopted its corrections, or completed the outstanding study.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ledgerreadme" class="csl-entry">

“<span class="nocase">AI usage ledger: scope and first-build documentation</span>.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/usage_ledger/README.md>.

</div>

<div id="ref-AldousFillBook" class="csl-entry">

Aldous, David, and James Fill. 2002. “Reversible Markov Chains and Random Walks on Graphs.” <https://www.stat.berkeley.edu/~aldous/RWG/book.html>.

</div>

<div id="ref-CaseFlowDiameter2026" class="csl-entry">

“Aldous–Fill 4.49(ii) Ramanujan-Cone Counterexample Package.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/paper_af449_ramanujan_cone_refutation/README.md>.

</div>

<div id="ref-Ansari2026Copula" class="csl-entry">

Ansari, Jonathan. 2026. “Copulas Farthest from Independence in Quadratic Wasserstein Distance.” <https://arxiv.org/abs/2609.23940>.

</div>

<div id="ref-cacheofficial" class="csl-entry">

Anthropic. 2026. “<span class="nocase">Prompt caching: tracking cache performance</span>.” <https://platform.claude.com/docs/en/build-with-claude/prompt-caching>.

</div>

<div id="ref-CaseArcTransitive2026" class="csl-entry">

“Arc-Transitive Aldous–Fill Counterexample Research Package.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_arc_transitive_2026_09_15/README.md>.

</div>

<div id="ref-CaseBassQuillen2026" class="csl-entry">

“Bass–Quillen P02 All-Exponent Desaturation Report.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P02-bass-quillen/runs/2026-09-16/2026-09-16_14-20-31__run-report.md>.

</div>

<div id="ref-CaseBaumConnes2026" class="csl-entry">

“Baum–Connes P01 Terminal Handoff: Fixed Target Saturated.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P01-baum-connes/runs/2026-09-18/2026-09-18T01-11-22Z__run-report.md>.

</div>

<div id="ref-BenjaminiSchramm1996" class="csl-entry">

Benjamini, Itai, and Oded Schramm. 1996. “Percolation Beyond $\mathbb{Z}^d$, Many Questions and a Few Answers.” *Electronic Communications in Probability* 1: 71–82. <https://doi.org/10.1214/ECP.v1-978>.

</div>

<div id="ref-CaseQFORMRelease2026" class="csl-entry">

“Bounded Densities of Quadratic Forms: Scoped Research Release, 23 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/README.md>.

</div>

<div id="ref-Bradley2005" class="csl-entry">

Bradley, Richard C. 2005. “Basic Properties of Strong Mixing Conditions: A Survey and Some Open Questions.” *Probability Surveys* 2: 107–44. <https://doi.org/10.1214/154957805100000104>.

</div>

<div id="ref-salience" class="csl-entry">

Brain project archive. 2026a. “<span class="nocase">Affective salience: implemented recency and persistence scoring</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/salience.py>.

</div>

<div id="ref-mesh" class="csl-entry">

———. 2026b. “<span class="nocase">Agent mesh: coordination, liveness, leases, and handoffs</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/agent_mesh/README.md>.

</div>

<div id="ref-canonical" class="csl-entry">

———. 2026c. “Canonical Brain Improvement Prompt and Evidentiary Operating Contract.” <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/CANONICAL_PROMPT.md>.

</div>

<div id="ref-coactivation" class="csl-entry">

———. 2026d. “<span class="nocase">Coactivation folding: decay, focus weighting, and exactly-once receipts</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/coactivation_end.py>.

</div>

<div id="ref-broadarchitecture" class="csl-entry">

———. 2026e. “<span class="nocase">Cognitive architecture: external memory, faculties, and their development</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/COGNITIVE_ARCHITECTURE.md>.

</div>

<div id="ref-consciousness" class="csl-entry">

———. 2026f. “<span class="nocase">Conscious and unconscious memory tiers and steerable dreams</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/CONSCIOUSNESS.md>.

</div>

<div id="ref-fok" class="csl-entry">

———. 2026g. “<span class="nocase">Feeling-of-knowing probe: memory accessibility before retrieval</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/fok_probe.py>.

</div>

<div id="ref-globalworkspace" class="csl-entry">

———. 2026h. “<span class="nocase">Global workspace: shared current state and intent ledger</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/global_workspace/README.md>.

</div>

<div id="ref-dispatcher" class="csl-entry">

———. 2026i. “<span class="nocase">Hook dispatcher: runtime execution, context allocation, and delivery accounting</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/hook_dispatch.py>.

</div>

<div id="ref-consciousnesscode" class="csl-entry">

———. 2026j. “<span class="nocase">Implementation of foreground and latent memory tiers</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/consciousness.py>.

</div>

<div id="ref-instincts" class="csl-entry">

———. 2026k. “<span class="nocase">Instinct priming: precision-aware warnings, graph cues, and repetition control</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/instinct_prime.py>.

</div>

<div id="ref-leanbroad" class="csl-entry">

———. 2026l. “Local Mathlib Checker and Execution Scope.” <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/lean_check.py>.

</div>

<div id="ref-mathsense" class="csl-entry">

———. 2026m. “<span class="nocase">Mathematical memory injection from the populated Math Brain</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/math_sense.py>.

</div>

<div id="ref-prediction" class="csl-entry">

———. 2026n. “<span class="nocase">Prediction scoring and calibrated feedback</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/predict.py>.

</div>

<div id="ref-reconsolidation" class="csl-entry">

———. 2026o. “<span class="nocase">Reconsolidation routing by surprise and memory strength</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/reconsolidate.py>.

</div>

<div id="ref-spread" class="csl-entry">

———. 2026p. “<span class="nocase">Spreading-activation recall: live association retrieval and attention gates</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/spread_recall.py>.

</div>

<div id="ref-leanparser" class="csl-entry">

———. 2026q. “Structural Lean Receipt Parser.” <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/proof_receipt.py>.

</div>

<div id="ref-mistakegraph" class="csl-entry">

———. 2026r. “<span class="nocase">The corrections corpus as a graph: recurrence, coverage, and null-model comparison</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/MISTAKE_GRAPH.md>.

</div>

<div id="ref-recency" class="csl-entry">

———. 2026s. “<span class="nocase">The measured recency kernel</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/RECENCY_KERNEL.md>.

</div>

<div id="ref-wake" class="csl-entry">

———. 2026t. “<span class="nocase">Wake routine: bounded context assembly and delivery evidence</span>.” Versioned repository source. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/wake_brain.ps1>.

</div>

<div id="ref-CaseCerny2026" class="csl-entry">

“Cerny P16 Exact-Enumeration Run, 16 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P16-cerny/runs/2026-09-16/2026-09-16_18-40-14__run-report.md>.

</div>

<div id="ref-Cerny1964" class="csl-entry">

Černý, Ján. 1964. “Poznámka k Homogénnym Experimentom s Konečnými Automatmi.” *Matematicko-Fyzikálny časopis* 14 (3): 208–16. <https://dml.cz/handle/10338.dmlcz/126647>.

</div>

<div id="ref-ChvatalSankoff1975" class="csl-entry">

Chvátal, V., and D. Sankoff. 1975. “Longest Common Subsequences of Two Random Sequences.” *Journal of Applied Probability* 12 (2): 306–15. <https://www.jstor.org/stable/3212444>.

</div>

<div id="ref-proofhooks" class="csl-entry">

Cognitive Architecture repository. 2026. “Proof-Sense Audit Hook.” <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/dreaming/proof_sense.py>.

</div>

<div id="ref-ledgerdaily" class="csl-entry">

“<span class="nocase">Daily Claude Code usage ledger</span>.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/usage_ledger/daily.tsv>.

</div>

<div id="ref-CaseThevenin2026" class="csl-entry">

“Degree-Count Counterexample Research Package.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_thevenin_2026_09_15/README.md>.

</div>

<div id="ref-dehaene2011" class="csl-entry">

Dehaene, Stanislas, and Jean-Pierre Changeux. 2011. “Experimental and Theoretical Approaches to Conscious Processing.” *Neuron* 70 (2): 200–227. <https://doi.org/10.1016/j.neuron.2011.03.018>.

</div>

<div id="ref-CaseBroadSolvedRegister2026" class="csl-entry">

“Earlier Mathematical Research Solved Register.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/Open%20problem%20project/solved_register.md>.

</div>

<div id="ref-Exoo2018NelsonHistory" class="csl-entry">

Exoo, Geoffrey, and Dan Ismailescu. 2018. “The Chromatic Number of the Plane Is at Least 5: A New Proof.” <https://arxiv.org/abs/1805.06055>.

</div>

<div id="ref-CaseFEICurrent2026" class="csl-entry">

“FEI Current Shared Research and Correction State.” 2026. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md>.

</div>

<div id="ref-CaseFEIReadOnce2026" class="csl-entry">

“FEI Read-Once Interval Certificate.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/README.md>.

</div>

<div id="ref-CaseBrainUsageG0013" class="csl-entry">

“G0013 Mathematical Brain Usage Trace.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_1000_attempts_H_20260912/BRAIN_USAGE.jsonl>.

</div>

<div id="ref-CaseBrainUsageG0013Q2" class="csl-entry">

“G0013 Second Mathematical Brain Usage Trace.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_1000_attempts_H_20260912/BRAIN_USAGE_q2.jsonl>.

</div>

<div id="ref-GarbanPeteSchramm2010" class="csl-entry">

Garban, Christophe, Gábor Pete, and Oded Schramm. 2010. “The Fourier Spectrum of Critical Percolation.” *Acta Mathematica* 205: 19–104. <https://arxiv.org/abs/0803.3750>.

</div>

<div id="ref-CaseQFORMGaussian2026" class="csl-entry">

“Gaussian Mixtures with Controlled Average Component Peaks.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/gaussian_mixture.tex>.

</div>

<div id="ref-GrimmettWinklerForests" class="csl-entry">

Grimmett, Geoffrey, and Peter Winkler. 2003. “Negative Association in Uniform Forests and Connected Graphs.” <https://arxiv.org/abs/math/0302185>.

</div>

<div id="ref-CaseHadamard2026" class="csl-entry">

“Hadamard P15 Exact-Construction Run, 16 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P15-hadamard/runs/2026-09-16/2026-09-16_19-23-52__run-report.md>.

</div>

<div id="ref-CaseHadwigerNelson2026" class="csl-entry">

“Hadwiger–Nelson P19 Exact Gadget Exhaustion, 16 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/P19-hadwiger-nelson/runs/2026-09-16/2026-09-16_18-58-33__run-report.md>.

</div>

<div id="ref-ledgerhalf" class="csl-entry">

“<span class="nocase">Half-hour Claude Code output usage ledger</span>.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/usage_ledger/half_hours.tsv>.

</div>

<div id="ref-HasebeUeda2018" class="csl-entry">

Hasebe, Takahiro, and Yuki Ueda. 2018. “Large Time Unimodality for Classical and Free Brownian Motions with Initial Distributions.” *ALEA* 15: 353–74. <https://doi.org/10.30757/ALEA.v15-15>.

</div>

<div id="ref-Janson2012" class="csl-entry">

Janson, Svante. 2012. “Simply Generated Trees, Conditioned Galton–Watson Trees, Random Allocations and Condensation.” *Probability Surveys* 9: 103–252. <https://arxiv.org/abs/1112.0510>.

</div>

<div id="ref-KahnKomlosSzemeredi1995" class="csl-entry">

Kahn, Jeff, János Komlós, and Endre Szemerédi. 1995. “On the Probability That a Random $\pm1$-Matrix Is Singular.” *Journal of the American Mathematical Society* 8 (1): 223–40. <https://www.jstor.org/stable/2152887>.

</div>

<div id="ref-leanref" class="csl-entry">

Lean Language Reference. 2026. “Validating a Lean Proof.” <https://lean-lang.org/doc/reference/latest/ValidatingProofs/>.

</div>

<div id="ref-rag2020" class="csl-entry">

Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, et al. 2020. “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.” In *Advances in Neural Information Processing Systems*. Vol. 33. <https://arxiv.org/abs/2005.11401>.

</div>

<div id="ref-lostmiddle2024" class="csl-entry">

Liu, Nelson F., Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics* 12: 157–73. <https://aclanthology.org/2024.tacl-1.9/>.

</div>

<div id="ref-CaseLyons2026" class="csl-entry">

“Lyons Entropy Continuation and Certificate Scope.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/lyons-entropy/continuation-2026-09-17/README.md>.

</div>

<div id="ref-Lyons2002Preprint" class="csl-entry">

Lyons, Russell. 2002. “Determinantal Probability Measures.” <https://arxiv.org/pdf/math/0204325v1>.

</div>

<div id="ref-Lyons2003" class="csl-entry">

———. 2003. “Determinantal Probability Measures.” *Publications Mathématiques de l’IHÉS* 98: 167–212. <https://doi.org/10.1007/s10240-003-0016-0>.

</div>

<div id="ref-Lyons2014" class="csl-entry">

———. 2014. “Determinantal Probability: Basic Properties and Conjectures.” <https://arxiv.org/abs/1406.2707>.

</div>

<div id="ref-leannatural" class="csl-entry">

Math Brain project archive. 2026a. “Basic Natural-Number Formal Controls.” <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/formal/MathBrain/Basic.lean>.

</div>

<div id="ref-mathretrieval" class="csl-entry">

———. 2026b. “<span class="nocase">Deterministic lexical, formula, semantic, and signed-graph retrieval</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/src/math_brain/retrieval.py>.

</div>

<div id="ref-matharchitecture" class="csl-entry">

———. 2026c. “<span class="nocase">Math Brain architecture: structured records, typed graphs, verification, and consolidation</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/docs/architecture.md>.

</div>

<div id="ref-mathreadme" class="csl-entry">

———. 2026d. “<span class="nocase">Mathematical Research Brain: repository scope and current deployment status</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/README.md>.

</div>

<div id="ref-triggers" class="csl-entry">

———. 2026e. “<span class="nocase">Mathematical review triggers</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/config/triggers.toml>.

</div>

<div id="ref-consolidation" class="csl-entry">

———. 2026f. “<span class="nocase">Quarantined mathematical replay and association proposals</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/src/math_brain/consolidation.py>.

</div>

<div id="ref-semantic" class="csl-entry">

———. 2026g. “<span class="nocase">Semantic retrieval channel for the Math Brain</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/src/math_brain/semantic.py>.

</div>

<div id="ref-mistakes" class="csl-entry">

———. 2026h. “<span class="nocase">Structured mathematical mistakes and executable review reflexes</span>.” Versioned repository source. <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/src/math_brain/mistakes.py>.

</div>

<div id="ref-ab30readme" class="csl-entry">

Math Brain project contributors. 2026a. “AB30: README.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/README.md>.

</div>

<div id="ref-ab30analyze" class="csl-entry">

———. 2026b. “AB30CODE: Analyze.py.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py>.

</div>

<div id="ref-ab30deviation" class="csl-entry">

———. 2026c. “AB30DEV: DEVIATION.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/DEVIATION.md>.

</div>

<div id="ref-ab30prereg" class="csl-entry">

———. 2026d. “AB30PRE: PREREG.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md>.

</div>

<div id="ref-benchmark_ab30run" class="csl-entry">

———. 2026e. “AB30RUN: Ab30_run.py.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py>.

</div>

<div id="ref-benchmark_analytic" class="csl-entry">

———. 2026f. “ANALYTIC: THREE_ARM.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/analytical_10x_v1/results/THREE_ARM.json>.

</div>

<div id="ref-benchmark_arch150" class="csl-entry">

———. 2026g. “ARCH150: README.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/bank10k/results/archive/2026-08-17_run1_150item/README.md>.

</div>

<div id="ref-benchmark_b100_11" class="csl-entry">

———. 2026h. “B100_11: GRADE.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-11_bank100_rerun/GRADE.txt>.

</div>

<div id="ref-benchmark_b100_12" class="csl-entry">

———. 2026i. “B100_12: GRADE.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_bank100_rerun2/GRADE.txt>.

</div>

<div id="ref-benchmark_b12" class="csl-entry">

———. 2026j. “B12: PRIMARY.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/B12_bank_research/run_b12/results/PRIMARY.md>.

</div>

<div id="ref-benchmark_b12embed" class="csl-entry">

———. 2026k. “B12EMBED: THREE_ARMS.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/B12_bank_research/run_b12/results/THREE_ARMS.md>.

</div>

<div id="ref-benchmark_b12frame" class="csl-entry">

———. 2026l. “B12FRAME: PRIMARY_FRAME.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/B12_bank_research/run_b12/results/PRIMARY_FRAME.md>.

</div>

<div id="ref-benchmark_b12h" class="csl-entry">

———. 2026m. “B12H: ARM_h.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/B12_bank_research/run_b12_hyp/results/ARM_H.md>.

</div>

<div id="ref-benchmark_b12k1" class="csl-entry">

———. 2026n. “B12K1: PRIMARY_K1.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/B12_bank_research/run_b12/results/PRIMARY_K1.md>.

</div>

<div id="ref-benchmark_bank300" class="csl-entry">

———. 2026o. “BANK300: RESULTS_bank10k.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/COORD_realtest/RESULTS_bank10k.md>.

</div>

<div id="ref-benchmark_c1" class="csl-entry">

———. 2026p. “C1: RESULTS_c1.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/bank2x2/RESULTS_c1.json>.

</div>

<div id="ref-benchmark_contamination" class="csl-entry">

———. 2026q. “CONTAMINATION: a_no_brain_control_is_impossible_here_2026_09_22.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/01_ai_consciousness/claude/memory/a_no_brain_control_is_impossible_here_2026_09_22.md>.

</div>

<div id="ref-benchmark_h35_11" class="csl-entry">

———. 2026r. “H35_11: GRADE.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-11_harder35_rerun/GRADE.txt>.

</div>

<div id="ref-benchmark_h35_12" class="csl-entry">

———. 2026s. “H35_12: GRADE.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_harder35_rerun2/GRADE.txt>.

</div>

<div id="ref-benchmark_h35_22" class="csl-entry">

———. 2026t. “H35_22: GRADE.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_harder35_rerun3/GRADE.txt>.

</div>

<div id="ref-benchmark_hardb1" class="csl-entry">

———. 2026u. “HARDB1: HEAD_TO_HEAD.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/hard_b1/results/HEAD_TO_HEAD.json>.

</div>

<div id="ref-benchmark_jul13" class="csl-entry">

———. 2026v. “JUL13: Math-Brain-Private-Codex-Study-2026-07-13.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/01_ai_consciousness/claude/memory/math-brain-private-codex-study-2026-07-13.md>.

</div>

<div id="ref-benchmark_l1raw" class="csl-entry">

———. 2026w. “L1RAW: GRADE_ROWS_r5.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-11_20h_mathbrain/locate_bank/GRADE_ROWS_r5.json>.

</div>

<div id="ref-benchmark_l2raw" class="csl-entry">

———. 2026x. “L2RAW: GRADE_ROWS_L2_r5.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-11_20h_mathbrain/locate_bank/GRADE_ROWS_L2_r5.json>.

</div>

<div id="ref-benchmark_l3raw" class="csl-entry">

———. 2026y. “L3RAW: GRADE_ROWS_L3_r3.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-11_20h_mathbrain/locate_bank/GRADE_ROWS_L3_r3.json>.

</div>

<div id="ref-benchmark_lit100" class="csl-entry">

———. 2026z. “LIT100: REPORT_100Q.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-06_prob_lit_bank/run_agents100_0907/REPORT_100Q.md>.

</div>

<div id="ref-benchmark_m3posture" class="csl-entry">

———. 2026aa. “M3POSTURE: GRADE_v1_v3_complete.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_ultracode_mathbrain/lanes/m3_proofsense/GRADE_v1_v3_complete.txt>.

</div>

<div id="ref-benchmark_m3shard" class="csl-entry">

———. 2026ab. “M3SHARD: GRADE_shardsize_5_vs_15.txt.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_ultracode_mathbrain/lanes/m3_proofsense/GRADE_shardsize_5_vs_15.txt>.

</div>

<div id="ref-benchmark_onek" class="csl-entry">

———. 2026ac. “ONEK: CAMPAIGN.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_opus_1k/CAMPAIGN.md>.

</div>

<div id="ref-benchmark_onekraw" class="csl-entry">

———. 2026ad. “ONEKRAW: GRADE_ROWS.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-12_opus_1k/runs/GRADE_ROWS.json>.

</div>

<div id="ref-benchmark_packetb" class="csl-entry">

———. 2026ae. “PACKETB: RESULTS_packetB.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/COORD_realtest/RESULTS_packetB.md>.

</div>

<div id="ref-benchmark_powered" class="csl-entry">

———. 2026af. “POWERED: PRIMARY_STAGE1.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/bank10k/run_powered/results/PRIMARY_STAGE1.json>.

</div>

<div id="ref-benchmark_recall200" class="csl-entry">

———. 2026ag. “RECALL200: The_brain_is_worth_65_points_of_accuracy_2026_09_22.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/01_ai_consciousness/claude/memory/the_brain_is_worth_65_points_of_accuracy_2026_09_22.md>.

</div>

<div id="ref-benchmark_scars100" class="csl-entry">

———. 2026ah. “SCARS100: The_brain_is_worth_28_scars_in_100_and_the_gain_is_the_measured_ones_2026_09_22.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/01_ai_consciousness/claude/memory/the_brain_is_worth_28_scars_in_100_and_the_gain_is_the_measured_ones_2026_09_22.md>.

</div>

<div id="ref-benchmark_sterility" class="csl-entry">

———. 2026ai. “STERILITY: PRIMARY_STAGE1_STERILITY_ADDENDUM.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/bank10k/run_powered/results/PRIMARY_STAGE1_STERILITY_ADDENDUM.json>.

</div>

<div id="ref-benchmark_t1" class="csl-entry">

———. 2026aj. “T1: RESULT.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t1/RESULT.md>.

</div>

<div id="ref-benchmark_t2" class="csl-entry">

———. 2026ak. “T2: RESULT.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t2/RESULT.md>.

</div>

<div id="ref-benchmark_t3" class="csl-entry">

———. 2026al. “T3: RESULT.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t3/RESULT.md>.

</div>

<div id="ref-twoopus" class="csl-entry">

———. 2026am. “TWOOPUS: README.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_two_opus_with_without/README.md>.

</div>

<div id="ref-benchmark_tworesult" class="csl-entry">

———. 2026an. “TWORESULT: RESULT.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_two_opus_with_without/runs/RESULT.json>.

</div>

<div id="ref-twoopususage" class="csl-entry">

———. 2026ao. “TWOUSAGE: Usage.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_two_opus_with_without/runs/usage.json>.

</div>

<div id="ref-benchmark_v5" class="csl-entry">

———. 2026ap. “V5: METRIC.md.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/METRIC.md>.

</div>

<div id="ref-benchmark_v5raw" class="csl-entry">

———. 2026aq. “V5RAW: CUMULATIVE.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/06_math_research/probability_open_problem_campaign_2026_08_09/eval/CUMULATIVE.json>.

</div>

<div id="ref-benchmark_w7adj" class="csl-entry">

———. 2026ar. “W7ADJ: RESULT_ADJUDICATED.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_opus55_round5/w7_math_test/grade/RESULT_ADJUDICATED.json>.

</div>

<div id="ref-benchmark_w7audit" class="csl-entry">

———. 2026as. “W7AUDIT: ADJUDICATION.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_opus55_round5/w7_math_test/grade/ADJUDICATION.json>.

</div>

<div id="ref-benchmark_w7raw" class="csl-entry">

———. 2026at. “W7RAW: RESULT.json.” Private repository research artifact. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_opus55_round5/w7_math_test/grade/RESULT.json>.

</div>

<div id="ref-leanblocked" class="csl-entry">

Math Brain repository. 2026a. “Account 04 B14 Formal Backend Acceptance Record.” <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/scheduled_tasks/runs/fleet04/B14/B14-20260921T081150Z-r11/formal_backend_acceptance.json>.

</div>

<div id="ref-leanarchitecture" class="csl-entry">

———. 2026b. “Formal Verification: Local Authority and Statement Fidelity.” <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/docs/formal-verification.md>.

</div>

<div id="ref-leancontrols" class="csl-entry">

———. 2026c. “Lean Authority and Formalization-Fidelity Regression Tests.” <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/tests/test_lean.py>.

</div>

<div id="ref-leanimplementation" class="csl-entry">

———. 2026d. “Local Lean Verification and Evidence Authority Implementation.” <https://github.com/yspennstate/math-research-brain/blob/a4c99b43a044c127787c26997ed942f41591aac6/src/math_brain/lean.py>.

</div>

<div id="ref-arclean" class="csl-entry">

Mathematical Research repository. 2026a. “Arc-Transitive Graphs: Arithmetic Build and Axiom Reports.” <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_arc_transitive_2026_09_15/build_and_axioms.log>.

</div>

<div id="ref-degreelean" class="csl-entry">

———. 2026b. “Degree Counts in Conditioned Trees: Arithmetic Build and Axiom Reports.” <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_thevenin_2026_09_15/build_and_axioms.log>.

</div>

<div id="ref-freelean" class="csl-entry">

———. 2026c. “Free Unimodality: Named Lean Axiom Reports.” <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_free_unimodality_2026_09_14/build3.log>.

</div>

<div id="ref-mcclelland1995" class="csl-entry">

McClelland, James L., Bruce L. McNaughton, and Randall C. O’Reilly. 1995. “Why There Are Complementary Learning Systems in the Hippocampus and Neocortex: Insights from the Successes and Failures of Connectionist Models of Learning and Memory.” *Psychological Review* 102 (3): 419–57. <https://doi.org/10.1037/0033-295X.102.3.419>.

</div>

<div id="ref-nemhauser1978" class="csl-entry">

Nemhauser, George L., Laurence A. Wolsey, and Marshall L. Fisher. 1978. “An Analysis of Approximations for Maximizing Submodular Set Functions—i.” *Mathematical Programming* 14: 265–94. <https://doi.org/10.1007/BF01588971>.

</div>

<div id="ref-ODonnellTanFEI" class="csl-entry">

O’Donnell, Ryan, and Li-Yang Tan. n.d. “A Composition Theorem for the Fourier Entropy-Influence Conjecture.” <https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf>.

</div>

<div id="ref-memgpt2023" class="csl-entry">

Packer, Charles, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez. 2023. “MemGPT: Towards LLMs as Operating Systems.” <https://arxiv.org/abs/2310.08560>.

</div>

<div id="ref-Paley1933" class="csl-entry">

Paley, R. E. A. C. 1933. “On Orthogonal Matrices.” *Journal of Mathematics and Physics* 12: 311–20. <https://doi.org/10.1002/sapm1933121311>.

</div>

<div id="ref-generative2023" class="csl-entry">

Park, Joon Sung, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023. “Generative Agents: Interactive Simulacra of Human Behavior.” In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*. <https://arxiv.org/abs/2304.03442>.

</div>

<div id="ref-PemantleNegativeDependence" class="csl-entry">

Pemantle, Robin. 2000. “Towards a Theory of Negative Dependence.” <https://arxiv.org/pdf/math/0404095>.

</div>

<div id="ref-CaseCampaignIndex2026" class="csl-entry">

“Probability Campaign Index and Scope Ledger.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/INDEX.md>.

</div>

<div id="ref-CaseProofnetManifest2026" class="csl-entry">

“ProofNet Archival Manifest.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/MANIFEST.md>.

</div>

<div id="ref-CaseQFORMScope2026" class="csl-entry">

“Quadratic-Form Manuscript Source Scope and Correction Policy.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/README.md>.

</div>

<div id="ref-CaseSidorenko2026" class="csl-entry">

“Quantitative Sidorenko Inequality for Equal Three-Block Regular Hosts.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/C30-sidorenko/contributions/2026-09-17_three-block-stability/README.md>.

</div>

<div id="ref-CaseW7Adjudication2026" class="csl-entry">

“Round-Five W7 Mathematical Benchmark Adjudication.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/brain_improvement/campaign_2026-09-22_opus55_round5/w7_math_test/grade/ADJUDICATION.json>.

</div>

<div id="ref-CaseQFORMSemidefinite2026" class="csl-entry">

“Semidefinite Quadratic Forms and Spectral Spread.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex>.

</div>

<div id="ref-ledgersessions" class="csl-entry">

“<span class="nocase">Session-level Claude Code usage ledger</span>.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/usage_ledger/sessions.tsv>.

</div>

<div id="ref-shanahan2005" class="csl-entry">

Shanahan, Murray, and Bernard Baars. 2005. “Applying Global Workspace Theory to the Frame Problem.” *Cognition* 98 (2): 157–76. <https://doi.org/10.1016/j.cognition.2004.11.007>.

</div>

<div id="ref-CaseFreeUnimodality2026" class="csl-entry">

“Sharp Free Brownian Unimodality Research Package.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_campaign_2026_09/paper_free_unimodality_2026_09_14/README.md>.

</div>

<div id="ref-CaseRademacherMemory2026" class="csl-entry">

“Sharp Rademacher Singularity Campaign: Typed Mathematical Memory.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/probability_1000/sharp_rademacher_campaign_2026_08_18/mathbrain/README.md>.

</div>

<div id="ref-reflexion2023" class="csl-entry">

Shinn, Noah, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2023. “Reflexion: Language Agents with Verbal Reinforcement Learning.” In *Advances in Neural Information Processing Systems*. Vol. 36. <https://arxiv.org/abs/2303.11366>.

</div>

<div id="ref-Sidorenko1991" class="csl-entry">

Sidorenko, A. F. 1991. “Inequalities for Functionals Generated by Bipartite Graphs.” *Diskretnaya Matematika* 3 (3): 50–65. <https://www.mathnet.ru/eng/dm804>.

</div>

<div id="ref-CaseComputeStrategy2026" class="csl-entry">

“Ten-Track Mathematical Compute Strategy, 20 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/operations/COMPUTE_STRATEGY_2026-09-20.md>.

</div>

<div id="ref-CaseProgress2026" class="csl-entry">

“Ten-Track Mathematical Progress Register, 20 September 2026.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/operations/PROGRESS20_2026-09-20.md>.

</div>

<div id="ref-TheveninDegreeCounts" class="csl-entry">

Thévenin, Paul. 2018. “Vertices with Fixed Outdegrees in Large Galton–Watson Trees.” <https://arxiv.org/abs/1812.07365>.

</div>

<div id="ref-ledgerbuilder" class="csl-entry">

“<span class="nocase">Transcript-derived usage ledger construction program</span>.” 2026. <https://github.com/<private-repo>/blob/bcff9346b68959f4cf330fdf9ca0e64a21c77d3e/12_cognitive_architecture/usage_ledger/build_usage_ledger.py>.

</div>

<div id="ref-CaseJanson2026" class="csl-entry">

“Uniform Condensation Windows for Zero-Radius Random Allocations.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/paper_zero_radius_condensation_2026_09_17/main.tex>.

</div>

<div id="ref-leandojo2023" class="csl-entry">

Yang, Kaiyu, Aidan M. Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan Prenger, and Anima Anandkumar. 2023. “LeanDojo: Theorem Proving with Retrieval-Augmented Language Models.” In *Advances in Neural Information Processing Systems*. Vol. 36. <https://arxiv.org/abs/2306.15626>.

</div>

<div id="ref-CaseJansonAudit2026" class="csl-entry">

“Zero-Radius Condensation Audit Summary.” 2026. <https://github.com/yspennstate/math-open-problems/blob/b4745ece98fa3839cf7afe35d829d08384c815b4/paper_zero_radius_condensation_2026_09_17/audits/SUMMARY.md>.

</div>

</div>
