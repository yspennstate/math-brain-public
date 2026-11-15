disk: small

Read ~/fei_solve_agent/FLOW.md first (sections 7, 9, 10). Scripts: the code folder beside it.
Earlier literature notes: ~/codex_fleet/20261108_pro/workers/FEIB11/LITERATURE.md. Extend them, do not repeat them.

Setting. f Boolean on n bits, mu = fhat^2, U ~ mu, I = E|U|, H = H(mu).
  Erasure entropy H^- = sum_i H(1[i in U] | U - i) = sum over edges {T, T+i} of (p+q) h(p/(p+q)), p = mu(T), q = mu(T+i).
  Claim of FLOW 7 and 10: FEI <=> H^- <= C I, with sup H^-/I <= C* <= sup H^-/I + 2/ln 2, by induction along a
  decision tree using D_i(f) = H(f) - H(f_{i->1})/2 - H(f_{i->-1})/2 = E_i + JS_i, 0 <= JS_i <= (2/ln 2) Inf_i.

Task A (literature, with exact citations: authors, title, year, theorem number; quote the statement).
1. Is the equivalence FEI <=> erasure entropy O(I), or the one-coordinate form (every Boolean function has a
   coordinate with H(1[i in U] | U - i) <= C Inf_i), in the literature? Check: Wan-Wright-Wu (Decision trees,
   protocols and the FEI conjecture), O'Donnell-Wright-Zhou (FEI for symmetric functions), Chakraborty-Kundu-
   Lokam-Saurabh (Upper bounds on Fourier entropy), Kelman-Kindler-Lifshitz-Minzer-Safra (Towards a proof of the
   Fourier-Entropy conjecture?), Gopalan-Servedio-Tal-Wigderson (degree and sensitivity), Das-Pal-Visavaliya,
   Shalev (FEI for read-once / low-rank), Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf (Improved bounds on
   Fourier entropy and min-entropy), Keller-Mossel-Schlank, Hod. Say plainly: known / partly known / not found.
2. What is the best general bound today (H <= C I log I? in which exact form), and the best lower bound on the
   constant (ours is 6.5218 from PM(K33); Hod's 6.278; check for anything newer)?
3. Erasure entropy (Verdu-Weissman) and pseudo-likelihood: any inequality bounding erasure entropy of a random
   subset by its mean size under a structural hypothesis (negative association, strong Rayleigh, determinantal,
   log-concave) that a Boolean spectral sample could satisfy or fail? Test the hypotheses numerically on the
   n <= 4 census (is the spectral sample ever negatively associated? log-submodular on which functions?).

Task B (KKLMS in edge form).
4. Write out the proof skeleton of the KKLMS bound from the paper's statements, then translate it: what does it give
   for the edge quantities (which edges it controls, where the log I is lost)? State as a precise open inequality
   what would have to be improved to remove the log.
5. Prove directly in the edge form the weak bounds: H^- <= I log2(e n/I) (Jensen) and H^- <= C I log(I+2)-type or
   H^- <= C I^2 from KKL/Friedgut (FLOW 9(e) sketches why: an element of U of influence delta comes with
   c log(1/delta) others). Write full proofs; these are the base camp.

Deliverables: LITERATURE.md (Task A, each item with its verdict), PROOFS.md (Task B; PROVED / CHECKED / OPEN),
scripts with outputs for item 3, REPORT.md with one verdict line per item. Write as you go. No web page may be
quoted from memory: if you cannot open a source, say so and mark the item UNVERIFIED.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
