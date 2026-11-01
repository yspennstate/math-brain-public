# C0021: exact depth-two decision tree and composition

Status: exact computational certificate plus a proved composition lemma; pending w346 KEEP. No novelty or full solution is claimed. Local status source is Garban and Steif, *Noise Sensitivity of Boolean Functions and Percolation* (2012), Exercise VIII.5 note, p. 97. The 7 September intake still labels the exponent unverified and unresolved.

Let f_k be iterated majority of three on 3^k independent fair bits. Algorithms query bits and must always return the exact output. Revealment is the largest probability that an individual bit is queried, under the uniform input and internal randomization.

For k=2, the minimum expected number of queries is 393/64 = 6.140625. Its minimum revealment is 131/192 = 0.6822916667. The usual recursive algorithm has expected cost 25/4 and revealment 25/36. Thus the verified finite-block cost decreases by 1.75%.

The certificate in check_majority.py examines all 19,683 partial assignments. At a partial assignment with m free bits, let A(s) be the sum of the remaining query counts over its 2^m compatible complete inputs. A(s)=0 if the function is forced; otherwise A(s)=2^m+min_i[A(s with bit i=0)+A(s with bit i=1)]. Every zero-error decision tree must choose an unqueried bit at a nonterminal state, so induction on m proves this recurrence gives the optimum. Randomization cannot beat the minimum of its deterministic trees. All computations use integers; the only division is by 2^9 at the root.

The independent checks use the 512-entry truth table to verify the terminal condition in every partial assignment, verify every Bellman residual and chosen action, and execute the complete policy on every input. All three error counts are zero; all outputs are correct and the sum of the 512 query counts is 3144. The policy is in majority_policy.json.

Randomize the policy by a uniform automorphism of the full ternary tree. This finite group preserves f_2 and acts transitively on its nine leaves. Each leaf then has revealment (393/64)/9 = 131/192. Conversely, any algorithm's maximum revealment is at least its expected query count divided by nine. This proves the finite-block optimum, subject to audit of the certificate.

For any k, evaluate each logical bit requested by this depth-two policy using a recursively composed policy on an independent descendant subtree. A logical subtree is selected before any of its own inputs are examined, so its selection event is independent of its bits and fresh internal randomness. At each block, the nine outputs are independent fair bits. A fixed leaf's query probability is consequently the product of the block probabilities. Hence

    delta_k <= (131/192)^floor(k/2) * (5/6)^(k mod 2).

For even k=2m this is n^(-0.17399134015245032), improving the exponent 0.16595623285353023 of the usual recursive construction. It is an achievable bound, not the exact asymptotic exponent. The former influence lower bound delta_k >= (2/3)^k still applies.

Command: python -X utf8 ~/brain_workers/w338/check_majority.py. Recorded runtime: 0.570578 seconds. Full measurements are in majority_measurements.json. The correctness checks concern fair independent inputs, zero error, and single-bit query cost; changing those assumptions changes the problem.
