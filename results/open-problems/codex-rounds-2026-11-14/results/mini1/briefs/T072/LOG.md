# T072 work log

Task: “push this problem forward by one checkable piece.” Session started 2026-11-14, approximately 20:51 local machine time (Asia/Tbilisi in the supplied environment).

## 1. Orientation and literature check

The folder initially contained only PROMPT.md. Read the startup memory and compute governor state; the governor reported `status: ok`. No subagents, git operations, external messages, or installs were used. The task-specific rule to write only in this folder supersedes global checklist/mesh/memory updates, so none of those updates will be made.

Commands included `pwd`, `rg --files ...`, `cat ~/.claude/brain_startup.md`, and `cat ~/.claude/compute/compute_state.json`. An initial `OMP_NUM_THREADS=1 nice -n 15 python3 .../brain.py recall "planted clique low degree lower bound"` returned no useful planted-clique memory. The sandbox printed `nice: setpriority: Operation not permitted`; no numerical computation will rely on running without the requested priority. A read-only `ps` priority inspection was also denied by the sandbox. Do not interpret these as successful priority verification.

Web searches (2026-11-14):

- `planted clique conjecture 2026 breakthrough polynomial time lower bound`
- `planted clique 2025 2026 low degree sum of squares algorithms advance`
- `site.arxiv.org planted clique 2026 November lower bounds`
- `site.arxiv.org planted clique 2025 2026 low-degree likelihood ratio threshold`

Opened the actual arXiv abstract pages https://arxiv.org/abs/2609.24780 and https://arxiv.org/abs/2604.07278. Search results alone are not used as citations. The first is a September 2026 algorithmic advance at the square-root scale; the second concerns multiple planted structures and does not settle the stated single-clique conjecture. Next: read the first paper's theorem statements to determine precisely whether it triggers the instruction to report substantial progress elsewhere and stop.

## 2. Choice: verify and report an advance elsewhere

Opened the full HTML of Dmitriy Kunisky and Songtao Mao, *Improved polynomial-time algorithms for detecting and recovering planted Θ(√n)-cliques*, arXiv:2609.24780v1, 21 September 2026, https://arxiv.org/html/2609.24780v1. Section 1.4, Theorem 1.12 gives an improved matrix-multiplication-time algorithm at a constant signal threshold less than 0.3320. This is an advance in the runtime/signal tradeoff, not a solution or refutation of the sub-square-root conjecture. It predates the supplied November 2026 status date, but is missing from the listed state of the art. Interpret the requested “substantially advanced” branch as including this directly relevant algorithmic improvement and stop after reporting it, rather than start a separate result. The report will make this interpretation and its date limitation explicit.

Also opened https://arxiv.org/abs/2611.11701: Riddhi Ghosal, Isaac M Hair, Aayush Jain, Amit Sahai, *Using the Planted Clique Conjecture for Cryptography: Public-Key Encryption from Planted Clique and Noisy k-LIN Over Expanders*, 8 November 2026. Its abstract assumes planted-clique hardness; it supplies no proof or refutation of that hardness. Further queries `planted clique low degree likelihood ratio degree log squared sharp constant epsilon` and `planted clique conjecture November 2026 solved polynomial` produced no verified resolution of the stated conjecture. Opened https://arxiv.org/abs/2608.06279 only to inspect its title/date; no theorem from it is used here.

Next verification: compare Theorem 1.12 against the PDF, check the definitions of its runtime exponents and success criterion, and avoid presenting the improved runtime as a newly solvable clique-size regime.

## 3. Verification and scope audit

Opened https://arxiv.org/pdf/2609.24780 and located Theorem 1.12 on printed page 8 / PDF page 11. Its displayed inequalities and strict numerical threshold agree with the HTML. Read Definition 1.1 in HTML: the runtime exponent is an infimum with arbitrary fixed positive slack; this is why SOLVED_ELSEWHERE.md uses O(n^{ω+η}) for every fixed η>0 rather than claiming that the infimum is necessarily attained. Read Definition 1.4: strong detection means total error o(1), and strong recovery means returning exactly the planted set with probability 1−o(1).

Independent scope checks, done symbolically rather than by a numerical program:

1. k=n^{1/2−ε} gives k/√n=n^{−ε}→0, outside any fixed positive signal threshold.
2. Solving the theorem's necessary premise n^{1/2−ε}≥λ√n for n gives n≤λ^{−1/ε}. Thus that premise eventually fails for every fixed ε,λ>0. This reaches the same conclusion by an explicit inequality.

Checked the main interpretation trap: the improvement is computational runtime at fixed square-root-scale signal, not a new polynomially solvable scaling regime. It is not a lower bound and does not imply P≠NP. No original proof or finite computation was substituted for the source theorem, and its complete proof was not audited. No rounded matrix multiplication exponent is used in the deliverable.

## 4. Saved deliverables

Created SOLVED_ELSEWHERE.md and REPORT.md with the patch tool. REPORT.md begins with the required `VERDICT: PARTIAL` line. The filename SOLVED_ELSEWHERE.md is explicitly disclaimed as a solution certificate. The report states both limitations of the stopping decision: the advance is at √n and it predates the supplied November status date. The literature check and decision were completed within the requested ten-minute window. No separate research computation was started.

## 5. Correction to the stopping decision; concrete mathematical choice

The proposed stopping interpretation above was too broad: a September paper at the existing √n scale is not progress after the supplied November status check. The literature search is now closed (within ten minutes); it did not verify a qualifying post-status advance. Remove the provisional SOLVED_ELSEWHERE.md to avoid a false signal and replace the provisional report after finishing the following piece.

Choice, recorded before developing the proof: derive an explicit finite-n upper bound for the degree-D likelihood-ratio norm in the fixed-size planted-clique model, and match its leading degree threshold when k=floor(n^{1/2−ε}). Group Fourier coefficients by their incident vertex sets, bound the number of edge sets of size at most D by binary entropy, and match the exponent with fixed-density edge sets. This is a cleaner, checkable restricted-model statement; no novelty over the established low-degree literature is claimed. The goal is a sharp leading constant specified by a one-variable entropy optimization, not a lower bound for arbitrary polynomial-time algorithms.

No numerical program is needed: all inequalities and small checks will be symbolic or exact hand arithmetic. This also avoids the unverified process-priority issue. A complete proof will go in PROOF.md; REPORT.md will state the limited success notion. The two main independent checks will be a second derivation of the Fourier norm from the overlap of two random planted sets and a small exact case checked by both formulas.

## 6. Finite bound proved and saved

Created PROOF.md with the exact Fourier coefficients and a finite-n bound. With H the binary entropy and A=max_{0<p≤1/2} H(p)/√(2p), the proof gives S_D≤exp(q)−1−q≤q²exp(q)/2, q=(k²/n)2^{A√D}. It uses a generating-function bound on binomial sums and only upper bounds graph counts by allowing isolated vertices. For k=floor(n^{1/2−ε}), this already proves vanishing norm excess below (1−δ)(4/A²)ε²(log₂n)². No numerical constants or numerical run are involved. The theorem's matching lower side is stated and remains to be completed next.

## 7. Matching bound and independent derivations saved

Completed the lower side in PROOF.md: fixed-density m-edge graphs with v=O(log n) and no isolated vertices contribute exponentially in (log n)² above the cutoff. The fraction with an isolated vertex is o(1) by a direct union bound. The binomial entropy lower bound is proved using the mode of a Binomial(M,m/M) distribution, rather than assumed. Falling-factorial errors vanish because v²/k→0. Rounding was tracked explicitly.

The optimizing density p_* is the unique root of (1+p)ln(1−p)−p ln p=0. Exact sign checks give 1/5<p_*<1/4: 5F(1/5)=ln(4096/3125)>0 and 4F(1/4)=ln(243/256)<0. The leading cutoff coefficient C_*=8p_*/H(p_*)² agrees with a second derivation optimizing the fixed-density exponent −2εa+a²H(p)/2 against the edge budget pa²/2.

Derived the norm again by first sampling two independent planted sets and counting surviving monomials in their intersection. This gives 1+S_D=E[sum_{j≤D} binom(binom(R,2),j)] for hypergeometric R. The exact finite identity is saved in PROOF.md, Section 5. The interpretation section proves the normalized mean-gap statement and explicitly excludes arbitrary polynomial thresholds and recovery claims.

## 8. Attempts to break the result

All calculations below are exact hand calculations, not output from a numerical program.

**Small fixed-size model, n=4,k=2.** There are six edges. A single edge is forced uniformly, so L=1+(1/6)sum_e X_e. Thus ||L_{≤0}||²=1 and ||L_{≤D}||²=7/6 for D≥1. Independently, the overlap probabilities at R=0,1,2 are 1/6,4/6,1/6; the overlap formula gives (1+4+2)/6=7/6. A third check uses the actual edge count E: L=E/3, E_QE=3, Var_Q(E)=3/2, so E_Q(L²)=1+(3/2)/9=7/6.

**Overlapping planted sets, n=5,k=3.** The ten singleton-edge coefficients are 3/10. Of the 45 pairs of edges, 30 share a vertex and have coefficient 1/10; the other 15 have coefficient zero. At degree three the ten triangles have coefficient 1/10; every other triple has zero coefficient. The squared norms for D=0,1,2,3 are therefore 1,19/10,11/5,23/10. Independently the overlap law has probabilities 3/10,6/10,1/10 at R=1,2,3. The corresponding binomial sums are (1,2,4) at D=1, (1,2,7) at D=2, and (1,2,8) at D=3, yielding exactly the same norms.

A third full-degree check in the same case uses the triangle count T: L=(4/5)T. In T², the ten diagonal terms contribute 10/8, the 60 ordered distinct pairs sharing an edge contribute 60/32, and the remaining 30 ordered distinct pairs contribute 30/64. Thus E_QT²=115/32 and E_QL²=(16/25)(115/32)=23/10. This checks the normalization without using sign-monomial orthogonality.

**Degree and size endpoints.** For D=0 the norm is exactly one. For k=0 or 1, P=Q and every nonconstant coefficient is zero. At k=n, p_v=1 and the norm is the full binomial sum B(binom(n,2),D), agreeing with the deterministic overlap R=n. Terms v>k vanish exactly; they are only retained when overcounting the upper bound. If D exceeds the number of possible edges, the exact norm saturates and the upper bound remains an overestimate.

**Potential asymptotic failure modes.** The lower bound uses fixed ε∈(0,1/2), fixed δ>0, and v=O(log n); it does not extend as written to ε depending on n. The exact critical window at δ=0 is not settled. Small factorial corrections are controlled with v²/k→0; replacing the fixed-size model by independent vertex planting without this check would not be justified. The lower graph count excludes isolated vertices by an explicit probability bound, rather than silently treating all labelled graphs as incident on all v vertices. The entropy bound splits at D=M/2, not D=M, which is essential for the leading constant.

**Interpretation failure modes.** Small projected norm controls normalized polynomial mean separation and bounded polynomial acceptance probabilities, not every threshold of a polynomial. Large projected norm is not by itself strong detection. No recovery lower bound or unrestricted computational lower bound follows. The theorem is a self-contained restricted-model derivation; novelty over existing low-degree results has not been established.

## 9. Final files

PROOF.md contains the finite bound, matching asymptotic cutoff with fixed multiplicative slack, exact one-variable characterization of its constant, the overlap identity, and the precise polynomial-statistic implication. REPORT.md replaces the provisional literature-only report. The provisional SOLVED_ELSEWHERE.md was removed because the search did not establish a qualifying post-status advance. No numerical script, numerical output, git operation, network upload, external message, or subagent was used for the mathematical work.

Final audit added a separate asymptotic lower derivation from the exact overlap mass: Pr[R=v]=((k)_v²/(v!(n)_v))((n−k)_{k−v}/(n−v)_{k−v}). The second factor is between 1−(k−v)²/(n−k+1) and 1, hence tends to one. Using a single overlap event and a single binomial term reproduces the positive exponent above the cutoff without the no-isolated-vertices count. This checks the most delicate lower-bound contribution by a different counting route. Read back PROOF.md and REPORT.md; corrected the display formatting of the two threshold implications. All theorem steps are complete, with no pending computation.
