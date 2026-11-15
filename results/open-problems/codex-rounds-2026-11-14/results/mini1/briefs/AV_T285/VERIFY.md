# T285: comparison with the OpenAI math release

Checked 14 November 2026. Verdict: NOT-THIS for all three supplied candidates. Each paper names its author as OpenAI and is dated September 24, 2026. The actual TeX sources were opened through the read-only GitHub connector; quotes below reproduce the theorem environments exactly, including TeX notation and line breaks.

## 1. A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling

OpenAI, September 24, 2026. [Theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/paper.tex); [paper PDF](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf).

```tex
\begin{theorem}\label{thm:main}
Let an explicitly listed finite directed acyclic graph specify the
precedence constraints on \(n\ge1\) nonpreemptive unit-length jobs
on three identical machines. There is a uniform deterministic algorithm
that constructs a feasible schedule of minimum makespan.
Given also an integer deadline \(1\le T\le n\), it decides feasibility
exactly and returns a schedule whenever the answer is affirmative.
Both tasks can be performed in
\(O((L+2)^{150020})\) steps on a deterministic multitape Turing machine,
where \(L\) is the total binary input length.
\end{theorem}
```

## 2. Infinitely many closed geodesic images on every Riemannian sphere

OpenAI, September 24, 2026. [Theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/introduction.tex); [paper PDF](https://raw.githubusercontent.com/openai/math/main/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf).

```tex
\begin{theorem}\label{thm:spheres}
For every integer $n\ge2$ and every smooth Riemannian metric on the standard
smooth sphere $S^n$, there are infinitely many prime closed geodesics with
pairwise different images.
\end{theorem}
```

## 3. The normalized-volume gap in dimension four

OpenAI, September 24, 2026. [Theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/build/paper.tex); [paper PDF](https://raw.githubusercontent.com/openai/math/main/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf).

```tex
\begin{theorem}\label{thm:main}
Let \(x\in X\) be a singular closed point of a normal complex algebraic variety of dimension four. Suppose that \(K_X\) is \(\Q\)-Cartier and that \(X\) is klt near \(x\), with boundary zero. Then
\[
\nvol(x,X)\le 162.
\]
Equality holds if and only if the analytic germ \((X,x)\) is isomorphic to
\[
\left(\left\{z_0^2+z_1^2+z_2^2+z_3^2+z_4^2=0\right\}\subset\C^5,0\right).
\]
\end{theorem}
```

## Comparison with every requirement in our row

| Requirement of T285 | Scheduling preprint | Geodesic preprint | Volume preprint |
|---|---|---|---|
| Teacher-student committee machine, two layers, K hidden sign units, fixed second layer | Finite DAG of unit jobs on three processors; no statistical learning model | Smooth Riemannian metric on a sphere; no network | Complex algebraic klt singularity with zero boundary; no network |
| n = alpha d samples and ambient dimension d | n counts jobs; L is binary input length; no samples or dimension d | n is sphere dimension, with n >= 2; no samples | Complex dimension is fixed at four; no samples |
| Bayes-optimal prediction error and fixed-K replica formula | Exact makespan and deadline feasibility | Infinitude of distinct prime geodesic images | Normalized volume <= 162, with an equality characterization |
| Rigorous large-K information threshold of order K | No information threshold and no limit in hidden-unit count | No such parameter or threshold | No such parameter or threshold |
| Rigorous AMP specialization threshold of order K^2 | No AMP, overlaps, or specialization | None | None |
| Polynomial-time or low-degree impossibility below order K^2 samples per dimension | Polynomial-time upper bound for a scheduling problem; no learning lower bound | No computational claim | No computational claim |

The shared words do not identify the same objects. In particular, three scheduling machines are three processors, not hidden units; sphere dimension is not the teacher-student feature dimension; and normalized-volume gap is an algebraic-geometric gap, not a statistical-computational gap. None of the three main theorems is a bound, asymptotic, special case, or generalization of any requested threshold or hardness conclusion. The fixed-K background replica result in our row is not reproved or strengthened by these theorems.

## Follow-ups and formalisation

### Scheduling: later papers, comments, and Lean

- David Niedbala Giraudin, *Three-machine unit-job scheduling in time \(O((L+2)^{276})\)*, 3 November 2026, [PDF opened](https://hexagonmath.org/pdf/2611.00060v1). The paper claims a smaller exponent by restricting the description family. It expressly takes correctness of the original dynamic program and structural proof as inputs; it is not an independent verification of the original proof. This is a Hexagon manuscript, not an arXiv version of OpenAI's paper.
- Klaus Jansen, *Precedence Constraint Scheduling on a Fixed Number of Machines*, submitted 6 November 2026, [arXiv:2611.09392 abstract](https://arxiv.org/abs/2611.09392) and [full HTML](https://arxiv.org/html/2611.09392v1) opened. It claims exact polynomial-time scheduling for every fixed machine count \(m\ge3\). Its introduction explicitly discusses and extends the OpenAI construction. It concerns scheduling throughout.
- The [community revision page](https://mathcommunity.github.io/oai-math-revised/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/) records an October 27, 2026 contribution by @ziangni-sys: added classical references and corrected cross-reference type names. This records editorial changes, not a refutation.
- The directly opened [Hacker News comment by NotOscarWilde](https://news.ycombinator.com/item?id=49985622), a self-described TCS/scheduling person, discusses the claim and exponent but expressly says they cannot check correctness. The comment does not establish the author's identity or constitute a referee report.
- The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/124-three-machine-scheduling/), last checked October 30, reports a Lean artifact and says it has not run the check. It reports no expert or peer review; that is the exposition's report, not a comprehensive certification search.
- Primary Lean materials opened: [scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/124.md), [comparator statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/ThreeMachine.lean), [configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/ThreeMachine.json), and [solution entry point](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Computability/Scheduling/Main.lean). The statement describes a single deterministic multitape machine returning exact scheduling answers within \(C(L+2)^{150020}\) steps. The challenge file's sorry is a placeholder in the comparator target; the configuration selects the separate solution module OAI.Computability.Scheduling.Main, whose main_theorem has a proof body. A build and full dependency audit were not performed here. These are scheduling artifacts, with no committee-machine conclusion.

### Geodesics: later paper and exposition

Zhiqi Chen, Shaoqiang Deng, Hui Zhang, *Infinitely many closed geodesic images on simply connected compact rank-one symmetric spaces*, submitted 15 October 2026, [arXiv:2610.21054 abstract](https://arxiv.org/abs/2610.21054) and [full HTML](https://arxiv.org/html/2610.21054v1) opened. The paper claims the corresponding infinitude for arbitrary smooth metrics on spheres and complex, quaternionic, and Cayley projective spaces. Section 1.3 credits OpenAI's sphere paper as antecedent and source of the finite-cut/doubling strategy, while saying its proof assumes neither that theorem nor its intermediate lemmas; the acknowledgements disclose Codex assistance. This is a later related paper, not an arXiv upload of the OpenAI manuscript, and its existence does not certify either proof.

The [Latent Seminar exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/345-closed-geodesic-infinitude), dated October 7, 2026, was opened. It expressly limits its review to statements, introductions, and selected mechanisms and disclaims independent full verification. No referee report, refutation, or concrete error report for the OpenAI sphere manuscript was found among the opened sources.

### Volume: exposition and notes

The [OpenAI Math Digest guide](https://masataka123.github.io/OpenAI-Math-Digest/en/papers/normalized-volume-gap-four/) was opened; it identifies itself as AI-generated and says it is not an independent verification of every proof. The [community manuscript page](https://mathcommunity.github.io/oai-math-revised/papers/The-normalized-volume-gap-in-dimension-four-September-24-2026/) had no contributed notes and displayed automated, unreviewed literature/exposition links. No later arXiv version of this OpenAI manuscript, referee report, refutation, or concrete error report was located in the opened sources. The catalogue also lists a same-date companion, *The ordinary-double-point gap in every dimension*; its paper was not opened and no theorem from it is relied upon here.

### Release documentation and limits of negative searches

Opened the repository [README](https://raw.githubusercontent.com/openai/math/main/README.md), [history](https://raw.githubusercontent.com/openai/math/main/history.md), [manuscript map](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), [Lean README](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [formalization catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [Lean root import file](https://raw.githubusercontent.com/openai/math/main/lean/OAI.lean), [comparator instructions](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md), and the lean/ and lean/docs/ directory listings. The manuscript map identifies these as families 124 (scheduling), 345 (geodesics), and 037 (volume); only scheduling has a linked Lean scope note. No geodesic or fourfold-volume formalisation was located in these records. The YAML omits scheduling despite its separately present Lean files, so YAML absence alone is not evidence of nonexistence.

The opened release history reports corrections and withdrawals of other manuscripts, but names none of these three. Exact-title searches and searches combining each title/subject with “OpenAI”, “arxiv”, “error”, “refutation”, and “review” produced the leads recorded above. Repository issue searches for repo:openai/math is:issue three-machine, geodesic, and normalized-volume each returned zero results. These are search outcomes, not a claim that no criticism exists anywhere.

As a background check, opened [arXiv:1806.05451](https://arxiv.org/abs/1806.05451), *The committee machine: Computational to statistical gaps in learning a two-layers neural network*, by Benjamin Aubin, Antoine Maillard, Jean Barbier, Florent Krzakala, Nicolas Macris, Lenka Zdeborová. Its abstract distinguishes AMP failure from the suggested failure of all efficient algorithms; the latter is not stated there as a theorem. No new matching committee-machine result appeared in the release manuscript-map keyword check or the targeted web searches. This verification does not replace a complete survey of the separate committee-machine literature.

## Recommended “where it stands”

Open: the September 24, 2026 OpenAI preprints *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, *Infinitely many closed geodesic images on every Riemannian sphere*, and *The normalized-volume gap in dimension four* concern different problems. None claims the large-\(K\) specialization thresholds or the polynomial-time/low-degree lower bound requested here, so these candidates give no reason to change the row's open status.

## Spot check

Selected Lemma 8.1 (source label lem:global-child) in the scheduling paper, the central conversion from recursively defined interval jobs to global bounded formulas. [Opened source](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/descriptions.tex). Also opened [construction](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/construction.tex), [boundary invariants](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/boundary.tex), [lists](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/lists.tex), and [separators](https://raw.githubusercontent.com/openai/math/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/separators.tex). The point of this lemma is that intersecting every ancestor's description could destroy the constant formula-size bound.

Write \(Q=\mathcal Q(\mathbf K')\), \(W'=(a',b')\), and let \(S\) be the shared cutoff. The two claimed global formulas are
\[
W'\setminus S=Q\cap P_{b'}\cap(J\setminus\widehat P_{a'}),\qquad
W'\cap S=D_{a'}\cap P_b\cap(J\setminus\widehat D_{b'})
 \cap(J\setminus\widehat D_v)\cap\widetilde S.
\]
The cone definitions use an existential predecessor/successor in a boundary triple; weak cones include the triple itself. This inclusion is necessary to exclude jobs scheduled exactly at a boundary.

For the high formula, the edge-label lemma places every high child job in \(P_{b'}\), and the child list selects precisely high jobs inside \(W'\). Such a job cannot precede or belong to the earlier slot \(a'\), by feasibility. Conversely, a job passing \(P_{b'}\) is strictly before the actual boundary \(b'\); if at or before \(a'\), Invariant I2 would put this global qualifier in \(\widehat P_{a'}\), contrary to the exclusion. Thus it is in \(W'\), where the list classification applies. The positive upper-bound cone is valid because the edge lemma says \(b'\) is an actual slot.

For the low formula, the positive cones first put a selected job strictly inside \(W=(a,b)\): it is after \(a'\ge a\) and before \(b\). Only then may one use the locally valid identity \(\widetilde S\cap W=S\). A job in this cutoff at or after the center \(v\) belongs to \(\widehat D_v\), by the center separator. Within the open side before \(v\), one at or after \(b'\) belongs to \(\widehat D_{b'}\), by its separator. The exclusions therefore put it inside \(W'\). In the reverse direction the edge-label lemma supplies \(D_{a'}\cap P_b\), and temporal feasibility supplies both weak-cone exclusions. The left-sentinel convention \(D_{a'}=J\) gives the harmless lower test when \(a'=a\) is virtual; reversal gives the other frame.

The two inclusions follow conditionally from the stated separator and construction invariants. This checks the localization step, not the substantial earlier induction that constructs and preserves those invariants. The adjacent leaf arithmetic is consistent: five entries of fewer than 40 leaves give at most 195; high and low formulas use at most 197 and 209 leaves, hence their union at most 406, below 500. No error was identified in this local implication; it does not establish correctness of the paper or of the Lean dependency graph.

