disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first.

Task: the literature side of the containment problem, and exactly where the logarithm is lost.
The best general bound is Kelman-Kindler-Lifshitz-Minzer-Safra, "Towards a proof of the Fourier-Entropy Conjecture?"
(arXiv 1911.10579): H <= C sum_S fhat(S)^2 |S| log(|S|+1), with Theorems 1.2 and 1.3 phrased through the generalized
influences I_S[f] = sum_{U contains S} fhat(U)^2 (our up(S)).
1. Fetch the paper (arXiv source or PDF; if the network is refused, say so and work from what you can derive). Write
   the proof skeleton of Theorems 1.1-1.3 in our notation: every lemma, what it bounds, and the one step where the
   factor log(|S|+1) or log D enters. FLOW.md section 3 guesses that it is the count of r-subsets of a typical U,
   sum_{|R|=r} up(R) = E C(|U|,r), or the harmonic sum E[|U|; |U| >= r]/r. Confirm or correct that guess with the
   line of the paper.
2. Say precisely which of the statements in FLOW.md sections 1, 2 and 4 are in the literature, with the reference and
   the statement number: H = 2A1 + 2Gamma and the equivalence FEI <=> (P <= C I and Gamma <= C I); the level form
   B <= sum_d W_d log(E C(|U|,d)/W_d) (suspects: Keller-Mossel-Schlank 2012 "A note on the entropy/influence
   conjecture"; O'Donnell-Wright-Zhou 2011; Chakraborty-Kulkarni-Lokam-Saurabh; Shalev 2018; Arunachalam et al. 2020
   "Improved bounds on Fourier entropy and min-entropy"; Han arXiv 2312.08271); the generalized Talagrand bound
   m(R) <= up(R) min(1, r!/L^r); the level-1 theorem E_S log(1/min_{i in S} Inf_i) <= C I. Quote the nearest known
   statement for each; "not found in the papers read" is a valid answer if you list what you read.
3. Granularity test of the lossy step: D_S f takes values in 2^(1-|S|) Z. For the step found in 1, decide whether
   granularity (or Booleanity f^2 = 1 in the form sum_S fhat(S) fhat(S xor T) = 0 for T nonempty) can remove the
   logarithm, by computing both sides of that step exactly on all 4-variable functions, on tribes, majority, address,
   and on the 5-variable extremals 0x0000000e and 0x008eeeee (bit x set means f(x) = -1). Report the worst ratio and
   the function that attains it; if the step is tight on a Boolean family, that family is the obstruction: write it.
4. The Fourier min-entropy conjecture (FMEI: max_S fhat(S)^2 >= 2^(-C I)) is a consequence of FEI. Say what the split
   gives for it: is there a containment or cancellation statement that is equivalent to FMEI, or strictly between
   FMEI and FEI? Prove what you claim.
Deliverables: PROOFS.md (skeleton and any proofs), RESULTS.md (tables), REPORT.md with one verdict line per numbered
item and a list of every source actually read (title, identifier, the sections read).
Memory: each process under 3 GiB, at most 2 threads, nice 10.
