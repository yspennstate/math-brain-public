# Worker FEIB29 (account acc2)

disk: small

# FEIB29 - the summed B-direction: prove or break  sum_i E_i <= C (I - W_1)

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Everything you need is in this brief; background, if wanted, is ~/fei_solve_agent/FLOW.md section
12(z) (the last section) and 12(y); code in ~/fei_solve_agent/code (predictor.py has a fast Walsh transform and
the standard families; `export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`, python3 has numpy). There is no math
store on this machine; do not look for one.

Setting. f: {-1,1}^n -> {-1,1}, mu(S) = fhat(S)^2, U ~ mu, I = E|U| = total influence, W_1 = sum_i mu({i}),
H = H(mu). Erasure entropy of coordinate i:
    E_i = H(1[i in U] | U - i) = sum_{T not containing i} Phi(mu(T), mu(T+i)),   Phi(p, q) = (p+q) h2(p/(p+q)).
Facts: H - (2/ln 2) I <= sum_i E_i <= H, so FEI <=> sum_i E_i <= C I. E_i = 0 for odd functions and for parities.

Round 8 (FEIB27) searched local dictionaries on a census of 33.6 million functions and found that the only
right-hand side that survives in SUMMED form besides Inf_i itself is B_i = Inf_i - fhat({i})^2:
    (B)   sum_i E_i <= C (I - W_1) = C sum_{|S| >= 2} |S| mu(S),      census optimum C about 4.094.
(B) is stronger than FEI near dictators (a dictator has I = 1, I - W_1 = 0, sum E_i = 0). My hand check: f = x_1
except on a subcube of measure eps where f = +1 gives ratio about 2; AND_2 gives 4.

The job, in order.
1. Reproduce: compute R(f) = sum_i E_i / (I - W_1) for AND_n, OR-of-ANDs (tribes of widths 2..4), majority-like
   thresholds with one heavy weight, address functions, PM(K33) (f = -1 iff the 9-edge subset of K_{3,3} contains a
   perfect matching), random functions, and find which function gives 4.094 (is it AND_2-like? is the supremum
   over the census attained or approached?).
2. Break it. Hill-climb R(f) by truth-table bit flips at n = 6..12 from many starts (random, near-dictators
   x_1 perturbed on small sets, thresholds with one dominant weight, "x_1 if g(x) = 1 else h(x)" selectors, towers
   F(psi,...,psi) of small bases - for towers use exact composition, not brute force, when n > 14). The danger zone:
   level-1 weight spread over several coordinates, W_1 close to I, yet many pairs (T, T+i) with comparable mass.
   Friedgut-Kalai-Naor says W_{>=2} small forces closeness to a dictator; quantify whether that is enough.
   Also try biased near-constants (I - W_1 is about I there) and functions of the form x_1 * g(x_2..x_n) (then
   W_1 can vanish) and x_1 XOR-free mixtures. Report the largest R found with the truth table (hex) and n.
3. If R stays bounded (say under 6): prove (B) for classes - (a) every function at distance delta from a dictator
   with an explicit constant as delta -> 0 (expand E_i around the dictator: the pairs (empty, {1}), ({j}, {1,j}),
   (S, S+1); use fhat(empty)^2 <= 4 delta^2, W_{>=2} >= c delta); (b) symmetric functions; (c) read-once
   formulas / towers (is R multiplicative-bounded under composition? derive the composition rule for
   sum_i E_i and for I - W_1: W_1(F o psi) = W_1(F) W_1(psi) for balanced psi); (d) decision trees of depth d.
4. Decide the logical status: does FEI (sum_i E_i <= C I) IMPLY (B) with another constant, via a stability
   argument near dictators (FKN, Kindler-Safra, Jendrej-Oleszkiewicz-Wojtaszczyk: exact constants for
   closeness to dictators)? If yes (B) is equivalent to FEI and says nothing new; say so plainly with the proof.
   If a function has I - W_1 << I it is close to a dictator: so the whole question is the asymptotics of
   sum_i E_i near a dictator. Settle that asymptotics exactly: sup over f at distance delta of
   sum_i E_i / (I - W_1) as delta -> 0.

Rules: one compute process at a time, at most 2 threads, nice 10, under 3 GiB; before any run longer than a
minute read `uptime` and use 1 thread if the 1-minute load is above 9. Folder under 60 MB (this disk is at its
floor: keep tables in memory, delete scratch as you go, no large outputs). Mark each statement PROVED, CHECKED
NUMERICALLY (with the command) or HEURISTIC. Check a claim of novelty against the literature before making it.
RESULTS.md as you go; REPORT.md at the end, verdict first (broken with the function / proved for which classes /
equivalent to FEI or not).

