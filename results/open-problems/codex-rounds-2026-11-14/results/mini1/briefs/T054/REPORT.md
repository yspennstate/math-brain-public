VERDICT: PROVED a finite-N reduction from complete delocalization to relative QUE on deterministic mesoscopic vertex sets

For a permutation-invariant real symmetric random matrix, suppose every unit eigenvector has squared coordinates at most L/N, except on an event of probability q. For any M deterministic vertex sets, each of size at least s, the probability that some eigenvector has relative mass error greater than epsilon on some set is at most

\[
 q+2MN(N+1)9^{\lfloor L\rfloor}
       \exp\left(-\frac{\epsilon^2s}{10L}\right),
 \qquad 0<\epsilon\leq1.
\]

PROOF.md proves this bound, including every unit vector in repeated eigenspaces. The main observation for multiplicities is that the delocalization hypothesis bounds every spectral projection's diagonal by L/N and hence bounds each eigenspace dimension by L.

For uniform simple labelled d-regular graphs, every fixed d >= 3, the published complete delocalization theorem of Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3, Theorem 1.4](https://arxiv.org/html/2102.00963v3#S1.SS3), supplies L = (log N)^{C_d} and q = o(1). Thus relative QUE holds, uniformly over all eigenvectors, on any deterministic polynomial-size family of vertex sets of sizes at least N^alpha, for every fixed alpha > 0. Formula (11) in PROOF.md gives an explicit error and failure bound. This is an elementary consequence of existing delocalization, not a new random-graph estimate or a claim of novelty for deterministic-observable QUE.

The literature check lasted under three minutes. Opened the arXiv pages and HTML for Yukun He, Jiaoyang Huang and Xiaoyu Wang, *Bulk universality of random regular graphs*, [arXiv:2610.08127](https://arxiv.org/abs/2610.08127), confirming the brief's October bulk result. Also opened Roland Bauerschmidt, Jiaoyang Huang and Horng-Tzer Yau, *Local Kesten--McKay law for random regular graphs*, [arXiv:1609.09052](https://arxiv.org/abs/1609.09052). No later result settling a specified stronger QUE formulation was found. The brief omits the earlier all-degree delocalization theorem used above. No SOLVED_ELSEWHERE.md was created because no post-brief resolution of the remaining unspecified stronger problem was established.

AUDIT.md records two derivations of finite-population variance, an exact six-subset hand check, an independent choice of exponential parameter recovering the constant 10, the net and multiplicity checks, and endpoint cases. The unconditional exceptional probability from Huang–Yau is retained; it is not silently strengthened to overwhelming probability. A Walsh-matrix construction shows that the abstract reduction fails for eigenvector-dependent sets.

Commands and artifacts: LOG.md contains the web queries, opened primary-source links, shell reads, and the decision made before proving the result. Read-only shell commands used `nice -n 15` with OMP_NUM_THREADS=1 and the BLAS thread variables set to 1 after the initial orientation. Files were written with apply_patch. No computation script, simulation, or numerical data file is needed: this contribution is a proof, and the finite hand enumeration appears in AUDIT.md. No git or external writes were used. The sandbox refused setpriority and ps; no heavy program was run.

What did not follow: the argument cannot handle observables chosen from the realized graph, and does not prove Gaussian eigenvector fluctuations or an optimal mesoscopic scale. The dimension net costs an extra factor in the sufficient scale s >> L(L+log(MN)). No attempt was made to claim this scale is sharp. The input delocalization theorem was checked in its statement but not reproved. The short literature search is not an exhaustive classification of QUE results.

Next worker: first choose an observable class stronger than deterministic label sets. One concrete candidate is mass on graph-metric balls B_G(x, floor(alpha log_{d-1}N)), with a fixed alpha in (0,1/2), uniformly over centers and bulk eigenvectors, normalized by the realized ball size. Determine its correct asymptotic and check the literature before attacking it. Relabelling alone cannot settle this candidate because the ball moves with the graph. Alternatively, if deterministic sets are the intended observables, treat the qualitative question as a consequence of known delocalization and ask for a sharper rate or fluctuation law.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 20:46 Asia/Tbilisi.
