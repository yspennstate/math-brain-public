# C0021 - the revealment exponent of iterated 3-majority

Status: partial. The exponent is not determined. What is new: the problem is reduced exactly to the growth rate of the uniform-distribution decision-tree cost of recursive 3-majority; the first three values of that cost are computed exactly (the depth-2 value agrees with an independent 2023 computation, the depth-3 value appears to be new); the rigorous window for sigma is tightened on the algorithmic side from 0.1660 to 0.1778; and the other side is corrected from the ledger's 0.369 to 0.2619 using the source's own Theorem VIII.6. The window is now sigma in [0.17784, 0.26186].

## 1. The problem as the source states it

Garban and Steif, *Noise sensitivity of Boolean functions and percolation*, arXiv 1102.5761, exercise sheet of Chapter VIII, printed page 95 (page 97 of the PDF):

> **Exercise VIII.5.** What can you say about the sequence of revealments for the Iterated 3-Majority function? [It can be shown that the sequence of revealments decays like 1/n^sigma for some sigma but it is an open question what sigma is.]

The objects (Definition VIII.1, same chapter): for a randomized algorithm A that always determines f, J_A is the random set of queried bits, delta_A = max_i P(i in J_A), and delta_f = inf_A delta_A. Example 4: n = 3^k, the bits sit at the leaves of a rooted ternary tree of depth k, and f is the majority applied level by level up to the root. The ledger row's paraphrase ("the revealments decay like n^{-sigma}; determine sigma") is faithful.

## 2. Finding

Write D_k for the minimum, over deterministic decision trees that always determine f_k, of the expected number of queried leaves when the 3^k leaves are i.i.d. uniform. (In the language of Jansson and Jansson this is the level-1/2 complexity of f_k.)

**Theorem A (exact reduction).** delta_{f_k} = D_k / 3^k for every k. The sequence D_k is submultiplicative, so c := lim D_k^{1/k} = inf_k D_k^{1/k} exists, and the revealment exponent is

    sigma = 1 - log c / log 3.

**Theorem B (values).** D_1 = 5/2, D_2 = 393/64 = 6.140625, D_3 = 15796051/1048576 = 15.06428..., and D_4 <= U_4 := 20871140813662641/562949953421312 = 37.07459... (the exact expected cost of an explicit depth-4 policy). In particular the natural greedy recursion, which costs (5/2)^k, is not optimal from depth 2 on.

**Corollary C (the window).**

    0.17784 < 1 - log(U_4^{1/4}) / log 3 <= sigma <= log(4/3) / log 3 < 0.26186.

The lower end replaces 0.16596 (greedy). The upper end replaces the 0.36907 recorded in attempt C0021-A001, which used the weaker bound delta >= Var(f)/(n max_i I_i); the source's Theorem VIII.6 (O'Donnell-Servedio) gives delta >= I(f)^2/n.

DEPTH5_PLACEHOLDER

## 3. Proofs

**Theorem A.** The automorphism group of the rooted ternary tree acts transitively on the leaves and preserves f_k. Given any algorithm A that determines f_k, let A' first draw a uniform automorphism g and then run A on the relabelled input. A' still determines f_k, and P(i in J_{A'}) = E|J_A| / n for every leaf i, so delta_{f_k} <= inf_A E|J_A| / n. Conversely max_i P(i in J_A) >= (1/n) sum_i P(i in J_A) = E|J_A| / n for every A. Since E|J_A| is an average over the coins of the costs of deterministic trees, inf_A E|J_A| = D_k. Hence delta_{f_k} = D_k / 3^k.

Submultiplicativity D_{k+m} <= D_k D_m: run the optimal depth-k tree on the 3^k depth-m subtrees as virtual leaves, evaluating a virtual leaf, when it is queried, with an optimal depth-m tree. The values of the depth-m subtrees are i.i.d. uniform (a majority of uniform bits is uniform), and the decision to query subtree j depends only on the other subtrees, so E[cost] = sum_j P(j queried) E[cost_j] = D_k D_m. Fekete's lemma gives the limit. Then delta_{f_k} = 3^{-k(1 - log_3 c) + o(k)}, which is the "decays like 1/n^sigma" of the exercise with sigma = 1 - log_3 c; and for each fixed m and every k, delta_{f_k} <= C_m n^{-(1 - log_3 D_m^{1/m})}.

**Theorem B.** D_k is a finite dynamic programme. A state is a partial assignment of the leaves; a determined subtree can be collapsed to its value (an optimal tree never queries inside a determined subtree: deleting such a query and keeping the better of its two continuations gives a correct tree that costs no more). Because the unrevealed leaves stay i.i.d. uniform after conditioning, V(state) = 0 if f is determined and otherwise V = 1 + min over unqueried leaves of (V(leaf = +) + V(leaf = -)) / 2. Two states that differ by a tree automorphism have the same V, so a state is stored as a canonical type: a leaf is u, + or -; an undetermined node is the sorted multiset of its children's types; a determined node is + or -. At depth 3 there are 17,254 types, and the DP (dp_exact.py, exact rationals) gives the three values. The depth-4 bound is the exact rational cost (policy_heur.py, reproduced by policy_heur2.py) of an explicit deterministic policy: inside a child use a V_3-optimal query; choose the child by one-step lookahead against the value of the game in which each child can be bought outright at price V_3(child) with its current posterior. The exact cost of any fixed policy is an upper bound on D_4.

**Corollary C.** delta_{f_k} <= D_k / 3^k <= const * (U_4/81)^{k/4}, and log(81/U_4) / log 81 = 0.17784... For the other side: f_k is monotone, the influence of a leaf is 2^{-k} (a leaf is pivotal iff at each of its k ancestors the two other children disagree, probability 1/2 each), so I(f_k) = (3/2)^k, and Theorem VIII.6 gives delta_{f_k} >= I(f_k)^2 / n = (3/4)^k, i.e. sigma <= log_3(4/3). The identity (3/2)^{2k} / 3^k = (3/4)^k and the rational inequalities behind the numbers are certified in U_C0021.lean.

## 4. What is not done

The exponent itself. The data suggest c is close to 2.45 (successive ratios D_2/D_1 = 2.456, D_3/D_2 = 2.453; the roots D_k^{1/k} are 2.5, 2.478, 2.4697, <= 2.4676), which would put sigma near 0.18-0.19, but the proved lower bound on c is only 9/4. A better lower bound needs an argument that charges the partial information an algorithm buys inside a child subtree. The all-or-nothing relaxation (a child determined with probability p costs at least p V(child), proved by completing the algorithm from its stopping state, whose optimal cost is at most V(child)) only yields D_k >= 2 D_{k-1}, weaker than the influence bound. I do not expect a closed form for sigma: the analogous worst-case constant for recursive majority (Magniez, Nayak, Santha, Sherman, Tardos, Xiao 2016) is only known to lie in [2.57143, 2.64944].

Exact D_4 is out of reach of the type DP (about 10^12 depth-4 types).

## 5. Checks

* D_2 = 393/64 three ways: the type DP; a DP over raw partial assignments of the 9 leaves with a brute-force determinacy test and no symmetry (check_bruteforce.py); and the polynomial P* = [4,4,6,9,-61,23,67,-64,16] of Jansson and Jansson (arXiv 2302.02473, Fig. 4.3: "the maximum of P* is about 6.14"), which evaluates at p = 1/2 to exactly 393/64.
* D_3: Monte Carlo of the DP's optimal policy, 200,000 runs, mean 15.0605 +- 0.013 against 15.0643 (check_bruteforce.py). The depth-4 number was reproduced by two code paths (policy_heur.py and policy_heur2.py).
* Theorem A sanity: D_1/3 = 5/6, the known revealment of MAJ_3 (Exercise VIII.1). Theorem VIII.6 side: the total influence at k = 2 by brute force is 9/4, and D_2/9 = 131/192 >= 9/16 (check_identification.py).
* Lean (U_C0021.lean, compiled clean; axioms propext, Classical.choice, Quot.sound only): the influence identity, 393/64 < (5/2)^2, D_3 < 2.4698^3, U_4 < 2.4676^4, U_4^3 < D_3^4 (depth 4 beats the depth-3 composition bound), and the monotonicity of the computed roots.
* Strongest case that I am wrong. (i) The identification delta = D_k / 3^k could fail if the exercise's revealment were meant for bounded-error algorithms, or if collapsing determined subtrees lost an optimal tree. The first is excluded by Definition VIII.1 (algorithms "for f" determine f); the second by the raw-assignment DP, which collapses nothing and returns the same 393/64. (ii) The direction of the exponent: smaller cost means smaller revealment means larger sigma, so upper bounds on D_k give lower bounds on sigma; the k = 2, 3 revealments 0.682 and 0.558 sit above the (3/4)^k floor, as they must. (iii) A tie-breaking or float error in the heuristic policy would not make its exact cost wrong, only suboptimal; the cost itself is computed in exact rationals.

## 6. Prior art

Web search was unavailable in this session (budget exhausted), so the search ran through arXiv's front end, Semantic Scholar's API (including the citation list of Magniez et al.) and direct PDF reads.

* Garban and Steif 2012 (the source), Exercise VIII.5: open; no later update found.
* Jayram, Kumar, Sivakumar 2003; Leonardos 2013; Magniez, Nayak, Santha, Sherman, Tardos, Xiao, arXiv 1309.7565 (Random Structures and Algorithms 2016): worst-case randomized complexity of recursive 3-majority, constant in [2.57143, 2.64944]. Their lower bounds use a hard distribution (one dissenting child at every node), not the uniform one, so they say nothing about sigma.
* Jansson and Jansson, "Level-p-complexity of Boolean functions using thinning, memoization, and polynomials", arXiv 2302.02473 (JFP 2023): computes the level-p complexity of maj_3^2 as a piecewise polynomial; its value at p = 1/2 is 393/64, matching D_2. They say the 27-bit case was out of reach and being explored with Sattler and Hughes; no follow-up on arXiv as of this search. No connection to revealment or to the Garban-Steif exercise is made there.
* The 34 papers citing 1309.7565 on Semantic Scholar contain nothing on the uniform-distribution exponent.

Nothing found settles sigma. The query that found the closest work was "recursive majority decision tree complexity" on Semantic Scholar, via the citation list of 1309.7565.

## Files

dp_exact.py (the type DP), policy2.py (prints the optimal depth-2 policy), check_bruteforce.py, check_identification.py, policy_heur.py and policy_heur2.py (depth-4/5 policies, exact costs), policy_heur2_K5.log, sigma_numbers.py, U_C0021.lean.
