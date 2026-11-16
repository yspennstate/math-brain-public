You are working on one case of a graph inequality. Work in this folder only and write as you go.

FILES HERE
- PREVIOUS_RESULT_STRAT4.md: the n = 5 result. It derives a closed form for T on the D = 2 stratum and proves T >= 0 for every disconnected 5-vertex graph on that stratum, with equality at the balanced triangle plus two isolated vertices and at two equal disjoint edges plus one isolated vertex.
- PREVIOUS_RESULT.md: the later n = 5 result (connected classes); read its notation section.
- terms.py: a numerical reference for the quantities below (function terms(W)). Use it to test your formulas, never as a proof.

THE QUANTITY
W is a symmetric nonnegative weight matrix on N vertices with zero diagonal, normalised so the weights of the edges i<j sum to 1. L = diag(W1) - W, lambda = the top eigenvalue of L, D its multiplicity, Pi the orthogonal projection on its eigenspace, G = lambda(I - J/N) - L, c = 2N/(N-2), beta = (1 - lambda)/(N-2).
X1 = D(lambda tr G - tr G^2), X2 = c tr(G (Pi o G)) (o = entrywise product), X3 = beta(D tr G - c sum_i Pi_ii G_ii),
S5 = sum_{i<j} W_ij (Pi_ii + Pi_jj - 2 Pi_ij)(G_ii + G_jj - 2 G_ij), T = X1 + X2 + X3 - 2 S5.
The conjecture is T >= 0 for every W. It is proved for D >= 4, and for N = 5 with D = 3.

TASK
Prove T >= 0 for every DISCONNECTED weighted graph on N = 6 vertices with D = 2 (top Laplacian eigenvalue of multiplicity exactly two). Then, if the method allows, extend it to every N >= 6.
Suggested order:
1. Numerical exploration first (allowed for discovery only): sample disconnected 6-vertex graphs with D = 2 by component structure (sizes 5+1, 4+2, 4+1+1, 3+3, 3+2+1, 3+1+1+1, 2+2+2, 2+2+1+1 and so on), including graphs where both top eigenvalues come from one component and graphs where each of two components contributes one. Record the least quotient T/(X1+X2+X3) per structure and the minimisers. If you find T < 0 at any graph, stop, verify it in exact rational arithmetic, and report it as the main result.
2. Reduce by component structure as STRAT4 did for N = 5 (an isolated vertex, components that carry no top eigenvector, the two-components-each-one-eigenvalue case, the one-component-carries-both case). Prove each case by a written argument or by exact rational or interval arithmetic.
3. Identify the equality cases for N = 6.

RULES
- Mark every statement PROVED or NUMERICAL. A floating optimiser, SDP or sampler never proves anything; a proof needs exact rational or interval arithmetic, or a written argument.
- Write a replay script for every exact certificate and run it. Use one thread for any solver (OMP_NUM_THREADS=1), and keep memory under 1 GB.
- Keep LOG.md current every 15 minutes or so (what you tried, what worked, what failed).
- Finish with RESULT.md: the theorems, the full derivations, the certificate construction and replay commands, and exactly what is left. Plain text, no bold.
- Do not use language-model workers or the network. Do not write outside this folder.
