# T060 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 01:06:28 Asia/Tbilisi (2026-11-14 21:06:28 UTC).

## 1. Read-only orientation and literature check

Read the earlier folder's REPORT.md, LOG.md, SOLVED_ELSEWHERE.md and file listing. There is no PROOF.md and there are no scripts in that folder. No earlier proof or computation is available to rerun. Read the brain index/startup memory index and the compute governor. The governor reports `warn`, `owner_away_open`, CPU saturation and swap activity. No heavy computation will be run. The task-specific instruction to write only here overrides shared brain/mesh/checklist writes; those tools were not run. No git or subagents.

Read commands used `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 ... nice -n 15 /bin/sh -c '...'`. The sandbox emits `nice: setpriority: Operation not permitted` but executes the small reads. This means the requested priority has not been verified; no numerical workload will be launched.

The initial `pwd` / `rg --files` directory discovery preceded that wrapper and was not run under nice. It was read-only and launched no numerical workload; subsequent shell reads used the wrapper above.

Web search queries, within the first five minutes:

- `Haldane conjecture "2026" "Tasaki" "Lu"`
- `"2610.34330" "2611.11049" Haldane`
- `"Heisenberg" "nontranslation-invariant" "2026" ground states uniqueness`
- `"Haldane" "November" "2026" proof ground state uniqueness integer spin`

Primary sources opened:

- Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, arXiv:2610.34330v2: https://arxiv.org/abs/2610.34330v2 and https://arxiv.org/html/2610.34330v2 . Theorem 2.1 asserts translation-invariant uniqueness and purity. The final discussion explicitly leaves arbitrary nontranslation-invariant states unresolved.
- Sirui Lu, *Bridging Gaps with Tensor Networks: From the Haldane Gap and Beyond*, arXiv:2611.11049v1: https://arxiv.org/abs/2611.11049v1 and https://arxiv.org/pdf/2611.11049 . Checked the periodic-gap deduction in Sec. SI.F against the earlier report.
- Hal Tasaki, *OpenAI's proof of the Haldane gap in the S=1 antiferromagnetic Heisenberg chain: Continuous-time version*, October 18–19, 2026: https://haltasaki.github.io/writings/AI/OpenAI_Haldane_CT.pdf . Opened full PDF.

The original manuscript's mirror failed in this session: https://mathcommunity.github.io/oai-math-revised/papers/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf . No claim to have reopened it. No newly found resolution of the remaining unrestricted uniqueness question. The periodic result is the already-known earlier finding, not a new reason to repeat that session's stop branch.

## 2. Independent re-check of the earlier main claim

The earlier result is a literature finding, not a computed certificate. Independently check its load-bearing implication directly from Gibbs probabilities, rather than merely restating an abstract. If purity is at least 1-u, its largest weight w0 is at least 1-u; if u<1/2 this excludes a degenerate lowest eigenvalue (energies counted with multiplicity). Moreover exp(-beta Delta)=w1/w0 <= u/(1-u). Substituting the published dyadic purity estimate u=(3/5)20^(-2^j), beta=784*2^j gives u/(1-u) <= (60/97)20^(-2^j) < 20^(-2^j), hence Delta>log(20)/784. This checks the analytic implication and the multiplicity issue independently. The finite trace inputs and transfer inequalities remain cited hypotheses; they have not been recomputed. The earlier scope claim holds to this extent.

## 3. Choice of one extension, before proof

Prove a general consequence of a unique translation-invariant ground state which is pure as a state on the full observable algebra: every competing ground state's translates approach that state in uniform density on every finite block; in particular, no competing state can have a finite translation period. This directly narrows the remaining nontranslation-invariant possibility. It requires no finite numerical certificate. The proof will use compactness of the ground-state set, translation averages, and extremality of a pure state; it will not assume that an arbitrary competing state is itself translation invariant. A separate counterexample will test whether the averaging argument can incorrectly be promoted to full uniqueness.

## 4. Proof completed

Wrote PROOF.md. The main statement is uniform over both the competing ground state and the starting point of each averaging interval. For any fixed finite block and epsilon>0, the fraction of translates at trace distance at least epsilon from the known state's marginal tends to zero. The mean trace distance also tends to zero. Finite translation periods are excluded as a corollary. This is a consequence of the cited uniqueness-and-purity theorem; no claim that this abstract consequence is new in the literature is made.

The proof first derives uniform convergence of translation averages using an endpoint error of at most 2||A||/N. It then conditions on a hypothetical positive-density set of signed discrepancies. A subsequential limit would give a nontrivial convex decomposition of the pure state with a component that differs on A, which is impossible. A finite self-adjoint matrix basis converts this to the block trace-norm statement.

Readback command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,240p" PROOF.md'
```

Output before the final audit addition: LOG.md 33 lines / 4235 bytes; PROOF.md 203 lines / 10653 bytes. Full proof read back. The priority warning recurred. No numerical experiment.

## 5. Attempt to break the result

- Independently checked finite-period exclusion by averaging exactly one period and applying purity directly. This does not rely on the density argument.
- Checked the p=1 endpoint in the conditioned decomposition separately, and defined the complementary state even when its averaging set is empty. No division by an empty complement.
- Purity is needed on the full algebra, not on a finite block. Restriction to a block can be mixed; the proof does not use block purity.
- Re-derived the trace-norm estimate in a second way from Hilbert–Schmidt norm and Cauchy–Schwarz. The first estimate is ||D||_1<=d^2 max_F|Tr(DF)|; the second gives the stronger d^(3/2) factor. The basis count is independently d+2*binomial(d,2)=d^2. For ell spin-1 sites, d=3^ell, hence d^2=9^ell.
- Verified the earlier gap's strictness another way: put t=20^(-2^j)<=1/20. The inequality ((3/5)t)/(1-(3/5)t)<t is equivalent to t<2/3, so strictness does not depend on decimal rounding or the prefactor 60/97. The stated prefactor itself is (3/5)/(1-3/100)=60/97.
- Tried to infer full uniqueness from the averaging result. This inference fails for a compact convex translation-invariant set consisting of the closed convex hull of a product vacuum and its single-defect translates. Proved that this set has only the pure vacuum as an invariant state. Nevertheless it has noninvariant states. Rechecked the example uniformly over its entire convex hull: block mean trace distance is at most 2*ell/N. The number two is also obtained from the two eigenvalues +1 and -1 of the difference of orthogonal rank-one density matrices.
- The example is not a Heisenberg ground state and is not represented as a counterexample to the Haldane assertion. It isolates the missing use of local stability beyond compactness/convexity. No rate for actual Heisenberg competitors is proved.

Literature phase ended before 21:10 UTC, within five minutes of the 21:06:28 UTC start. All later work is the selected proof and audit, not further searching.

## 6. Final artifacts

Wrote REPORT.md with the required first-line verdict and explicit external premise, limitations, failed full-uniqueness inference, and next lemma. Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

Exit status 0. Output: REPORT.md 22 lines / 3695 bytes; PROOF.md 203 lines / 11246 bytes; LOG.md 61 lines / 7810 bytes before this appended entry. The first line is `VERDICT: PARTIAL uniform-density restriction on competing ground states, assuming the published translation-invariant uniqueness and purity theorem`. The priority-adjustment warning remains. The proof and report accurately distinguish the conditional deduction from finite-certificate verification and from the still-missing unrestricted uniqueness argument.
