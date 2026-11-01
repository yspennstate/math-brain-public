# Creative proof campaign: Lyons entropy concavity

Date: 2026-09-15. User requested 100 NEW GPT-6 agents at max reasoning, exclusively creative proof methods (no audit assignments). Root coordinates and archives; workers do not spawn or push.

For every finite n, Hermitian positive contractions K0,K1, and t in [0,1], prove or refute H(P_((1-t)K0+tK1)) >= (1-t)H(P_K0)+t H(P_K1). P_K is the determinantal subset law P(S subset X)=det K_S. Natural-log entropy. Primary source: Russell Lyons, Determinantal Probability: Basic Properties and Conjectures (2014), Conjecture 2.6, https://arxiv.org/abs/1406.2707 (original 2003).

Existing complete partial results are in /workspace/scratch/f042dae27852/research-session/LYONS_PARTIAL_RESULTS.md and agents/ there. Newer frontier sources in sources/old-097.md, old-104.md, old-107.md are prior campaign mathematics, not new results. Do not count rederivations as discoveries. Yuzhou Gu's rank-one/scalar/zero endpoint cases are established prior work, https://sevenkplus.com/data/dpp.pdf.

Exact interior atom formula p_S=det M_S, with column j K e_j for j in S and (I-K)e_j otherwise. Along A=A*, R_S=M_S^-1 D_S with D columns +/-A, p'_S=p_S tr R_S, p''_S=p_S[(tr R_S)^2-tr R_S^2]. H''=-sum(p'_S)^2/p_S-sum p''_S log p_S. No general sign known in this project.

Most advanced low-dimensional route: sources/old-097.md derives exact three-site criterion b^T C^-1 b >=2. Universal proof still missing. sources/old-104.md proves diagonal-direction concavity for normalized L condition number <=3, not general. sources/old-107.md derives diamond coupling criterion and real-frame equalization, not general coupling.

Each assigned task is a bounded creative attempt to solve a precise mathematical obstruction. Develop a full proof, a useful new restricted theorem, or an exact counterexample to a proposed method. No audit-only output. Do not assume that a promised solution exists. Separate numerical evidence, proved statements, proposed lemmas, and open obligations. Do not present unsupported claims as theorems. Save full report agents/CNNN.md and any reproducible code/results under computations/CNNN/. Root will integrate and push all substantive output. Read this file, PRIOR_FRONTIER.md, and only relevant source sections; no broad repository scan. Do not modify other workers' files.
