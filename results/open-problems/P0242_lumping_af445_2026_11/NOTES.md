# P0242: lumping and the stopping-rule mixing time (Aldous-Fill Open Problem 4.45)

Status: RESOLVED IN THE LITERATURE (negative), plus a note of ours on what the literature leaves open.
Aldous and Fill ask (Open Problem 4.45) whether tau_1^(2) of an induced (lumped) chain is at most an absolute
constant times tau_1^(2) of the original reversible chain. Hermon and Peres, "On sensitivity of mixing times and
cutoff", Electron. J. Probab. 23 (2018), paper no. 25, DOI 10.1214/18-EJP154, arXiv:1610.04357 (Problem 1.6,
Theorem 3(c), Remark 1.8) answer no: on bounded-degree graphs the factor can be of order log |V|, and no more.
The October row of the ledger ("partially solved, K = 1 fails, sharp constant open") was written without that paper.

Paper: "Lumping and the mixing time of a reversible chain: the dependence on the number of states",
public repo https://github.com/yspennstate/lumping-mixing-time (commit e9c2c6353e3680e8f8443c63bd1afd6a71d5b640, 12 Nov 2026).
Ledger row: open-problems-repo master affd7c1a164f79f81638be9ac5386cad339b1133. Public copy and table row: math-brain-public main a9d616ac080413cffd0dacfb8c5a65749cb05616.

## What is proved

K(n) = sup of tau_1^(2)(induced) / tau_1^(2)(original) over reversible chains with at most n states.
tau_1^(2) = max_{i,j} (E_i T_j - E_pi T_j) (Lovasz-Winkler).

1. max(1, floor((n-2)/2)) <= K(n) <= n-1.
2. tau_2 <= tau_1^(2) for every reversible chain, constant one. Proof: for an eigenfunction g with eigenvalue
   lambda < 1 normalised so g(i) = 1 = max |g|, M_t = g(X_t) + (1-lambda) sum_{s<t} g(X_s) is a martingale;
   stop at a stationary stopping time U, E g(X_U) = 0, so 1 <= (1-lambda) E_i U. Equality for two-state chains and
   for the complete graph. Aldous and Fill ask this as Open Problem 4.48(b). Seven web searches, an arXiv search and
   the Lovasz-Winkler survey (Theorem 3.5: only "equivalent up to constants") turned up no earlier statement; the
   paper does not call it new, it says where it is asked and proves it. The brain already held this proof as part (b) of P0243 (card claim_58a424cb31744ae4b4b1134d0b319492, Dynkin's formula at the peak of the eigenfunction, Sept 2026); P0243 has no public repo, so this paper is where the proof is public. Part (a) of P0243 (tau_1 <= tau_0 fails) is not in it.
3. Upper bound of 1: tau_1^(2)(hat X) <= tau_0(hat X) <= tau_0(X) <= (m-1) tau_2(X) <= (m-1) tau_1^(2)(X).
   Also, from Aldous-Fill Lemma 4.23, K <= C (1 + log(1/pi_*)), which is the Hermon-Peres order on bounded-degree
   graphs.
4. Lower bound: a weighted comb with 2N+2 states (spine z_0..z_N, teeth y_0..y_{N-1} with heavy loops, a heavy
   end c). Lump y_k with z_k. Original tau_1^(2) <= max(B, M+B-rho), about h; induced >= pi_c N h alpha/(1+alpha).
   With alpha = h = t, r = 1 + t^3 and a heavy end the ratio tends to N. Exact values at t = 256:
   N = 1: 0.9961, N = 2: 1.9806, N = 4: 3.9268, N = 8: 7.7304.
5. Hitting times of sets: max_b hat E_b T_{hat A} <= (n - |A|) max_y E_y T_A (Green function, Rayleigh), and a
   factor close to (n-2)/2 occurs on the comb.
6. Four states: an exact chain with ratio 419679620/329408453 = 1.2740 (the October example).

Open: the true order of K(n) between (n-2)/2 and n-1; whether the comb is extremal.

## Checks

- code/lumping_checks.py (exact rationals, standard library): every inequality of the comb proposition for N up to
  8, the chain of inequalities in 3 and the hitting-time bound on 400 random networks, the four-state example.
- Independent referee (Codex, gpt-6.1-sol, Mac mini 1, 12 Nov 2026): every numbered statement and proof step
  CORRECT; its own exact code: 3,840 comb parameter sets with no violation, 600 networks for the hitting-time bound,
  21,000 chains (2 to 7 states, periodic, negative lambda_2, uneven weights) for tau_2 <= tau_1^(2), Table 1 and
  the four-state fractions reproduced, the Lovasz-Winkler formula checked by linear programming on three tiny
  chains. Overall verdict SOUND. Its nine wording points were applied before posting (increment bound 2 not 4; "ratios below one" for N = 1 holds for
  the table's parameters, not for every comb; "non-empty proper subset"; the regime of a heuristic sentence; hitting times defined with time zero; randomization independent of the future; "approached" for "attained"; two clearer sentences in the comb proof).
- Bibliography: five DOIs checked against Crossref; Aldous-Fill statements (Section 4.6.1, Proposition 4.44,
  Open Problems 4.45 and 4.48(b), Lemmas 4.23 and 4.24) read in the book's text.

## Where things are

- Work folder on the laptop: ~\agent_run\p0242 (repo/, lit/, referee/).
- Referee log and report: referee/LOG.md, referee/REPORT.md in this folder of the brain repo.
