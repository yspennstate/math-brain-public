You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem E0065, Problem 12 of Ganikhodzhaev-Rozikov, "Quadratic stochastic operators: results and open problems"
(arXiv:0902.4207v2, Section 9, PDF p. 7; Problem 2.29 / Theorem 2.28 of the 2011 IDAQP version with Mukhamedov): find the exact
threshold lambda_m (alpha_m) such that every quadratic stochastic operator on the (m-1)-simplex with all heredity coefficients
P_{ij,k} > lambda_m is regular (every orbit converges to one common point). The survey's Theorem 7 states lambda_m <= 1/(2m) and
gives a binary value. The claim (PARTIAL) asserts:
(a) for m = 2, under exactly the survey's coefficient normalization, the threshold is (3 - sqrt 7)/4, half of the printed value;
    proof via the fixed-point discriminant D = (2b-1)^2 + 4c(1-a), the factorisation f(f(x)) - x = (f(x)-x) H(x), and an explicit
    two-cycle of f_delta(x) = delta + (1-2 delta)(1-x)^2 below the threshold;
(b) for every m >= 3: (1 - 1/sqrt(m+1))/(2m) <= lambda_m <= 2/(3m + 2 + sqrt(m^2+12m+4)) < 1/(2m), so 2m lambda_m -> 1; the upper
    bound via a Fisher-Rao contraction (Lemma 1: |DW(x)h|^2_{W(x)} <= 2|h|^2_x, then a floor on the coefficients improves the
    factor below 1), the lower bound via explicit strictly positive operators with proper two-cycles.

Break it if it is wrong.
1. Get arXiv:0902.4207 (v1 and v2) into sources/ as plain text, and find the IDAQP 2011 version's statement if accessible. State
   Theorem 7 / Problem 12 exactly, including the coefficient normalization (is P_{12,k} = P_{21,k}, does the binary map carry a
   factor 2 on the mixed term) and strict versus non-strict inequality. Decide whether the "printed value is twice the true
   value" claim is a genuine discrepancy or a normalization mismatch on the claim's side. Search for the cited source [17]
   (Ganikhodzhaev) and any later paper determining lambda_m exactly or improving 1/(2m) (Rozikov, Mukhamedov, Jamilov,
   Zhamilov, Saburov, Khamraev, 2009-2026).
2. Check (a) line by line: the discriminant bound and its extremiser a = b = delta, c = 1 - delta; the identity for H(x); the
   convergence argument via the extreme limit points; the two-cycle formula (8) and that all coefficients are >= delta.
3. Check Lemma 1 and the passage from it to the upper bound C_m: how the coefficient floor enters, whether contraction in the
   Fisher-Rao metric really gives a unique global attractor on the closed simplex (boundary points, completeness), and the
   algebra producing 2/(3m+2+sqrt(m^2+12m+4)). Check the m = 2 instance (2 - sqrt 2)/4 is consistent with (a).
4. Check the lower-bound operators for m >= 3: strict positivity, the floor, and the existence of a proper two-cycle, for
   m = 3, 4, 5 exactly (rational or algebraic arithmetic) and the general formula.
5. Write your own independent code (do not reuse claim_files/code): verify (a) numerically and symbolically; for m = 3, 4 search
   for non-regular operators with floor above L_m (random and optimised) and confirm none are found above C_m.
6. Verdict on value: which parts are correct, which are new, and what remains (the exact lambda_m for m >= 3).
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
