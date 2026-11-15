You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem G0010, Question 5.2 of Christoph-Morawski-Wigderson, "The critical probability for percolation on finite graphs"
(arXiv:2608.19145): for Bernoulli bond percolation on a finite graph G with p <= (1-eps)/lambda(G), what is the tight bound on
the largest component L_1 given Delta(G) and lambda(G), especially in the near-regular case Delta <= (1+delta) lambda?
The claim's status line is COUNTEREXAMPLE, but it says itself that it does not settle the question; treat it as these results:
(A) Theorem A: if (1-eps)(1+delta) > 1 there are connected graphs (a complete b-ary tree of depth h whose root is joined by one
    edge to a vertex of K_{k+1}, with b ~ r k, 1/q < r < 1+delta, each vertex optionally blown up into an independent set of
    size b^{tau h}) with Delta <= (1+delta) lambda, lambda = Theta(n^{tau/(1+tau)}), and L_1 >= n^c whp at p = q/lambda.
(B) Proposition B: if q(1+delta) < 1 then L_1 = O(log n) whp (attributed to Diskin-Erde-Kang-Krivelevich arXiv:2209.03722 Thm 2),
    with a matching Omega(log n) on the cycle.
(C) Proposition C: if p lambda <= q < 1 and p Delta <= 1 then L_1 = O_eps((log n)^3) whp, via the resolvent u = (I-pA)^{-1} 1,
    U = max u_x = O(log n), and an exponential-moment induction for a multitype branching process.
(D) Section 4: a degree-sensitive refinement of the source's resolvent bound, L_1 = O(B^{log(qR)/log R + zeta} log n) with
    R = Delta/lambda, B = sqrt(n Delta)/lambda.

Break it if it is wrong.
1. Download arXiv:2608.19145 and 2209.03722 into sources/ as plain text. State Question 5.2 exactly as printed (page), and
   decide whether (A) contradicts anything the source states or conjectures, or only answers a regime the source left open.
   Check whether (A), (C) or (D) are already in print (the source itself, Diskin-Krivelevich, Alon-Benjamini-Stacey,
   Bollobas-Borgs-Chayes-Riordan, Nachmias-Peres, any 2026 citer of 2608.19145).
2. Check (A) line by line: lambda(tree) <= 2 sqrt(b); k <= lambda(H_h) <= k+1; lambda and Delta of the blow-up
   (A_H tensor J_m); feasibility of the parameter system (3) for every eps, delta with (1-eps)(1+delta) > 1; the coupling with
   Galton-Watson Bin(b, 1-e^{-q/(k+1)}) (one selected vertex per set, disjointness); the second-moment bound (8); the
   amplification over b^j disjoint subtrees; the exponent c and its relation to n_h.
3. Check (B) and the cycle lower bound, and check that the DEKK citation says what is claimed (theorem number, page).
4. Check (C) carefully: the bound U <= 1 + J + 1/eps using W_j(x) <= min(Delta^j, sqrt(d(x) n) lambda^{j-1}) with p Delta <= 1;
   the domination of exploration by the multitype process; the induction e^{a u_x} with a = 1/(2U^2), theta = 1/(4U^2) (is
   theta + a^2 U^2 = a used correctly, is a u_y <= 1/2 guaranteed, does the bound control total progeny including the root);
   the final tail and union bound.
5. Check (D): the weighted supermartingale argument, the sum U_a in (16), and the claimed exponent in (17), including that it
   beats the source's B log n for bounded R.
6. Write your own independent code (do not reuse claim_files/code): compute lambda, Delta exactly for small instances of the
   Theorem A graphs; simulate percolation at p = q/lambda on moderately large instances and on a near-regular instance with
   q(1+delta) = 1, and compare L_1 with the claimed orders.
7. Verdict on value: which of (A)-(D) are correct and new, and what remains of Question 5.2. Say plainly whether the honest
   status is PARTIAL rather than a counterexample to anything in the source.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
