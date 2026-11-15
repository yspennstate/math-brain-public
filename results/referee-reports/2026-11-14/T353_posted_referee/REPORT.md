VERDICT: ACCEPT WITH ONE MINOR CORRECTION (made and pushed, 685321f)

Independent post-posting referee pass on "Shuffled adaptive batch linear queries: the conjectured dominating pair
fails", https://github.com/yspennstate/shuffled-ablq-dominating-pair (paper/main.tex at f3f538a, read in full
14 Nov 2026 laptop time). Referee: an agent (Claude Opus 5.5), a session that did not write the paper.
Lane: T-20261112-017 independent referee passes on posted papers.

Independent numerics (t353_check.py, written from the paper's statements only; plain scipy quadrature of the
hockey-stick integrand max(alpha phi(s) + beta phi(s-a) - e^eps (gamma phi(s) + beta phi(s-c)), 0), sigma = 1,
eps = 1/2, T = 2 weights (phi(z-2), phi(z), phi(z-1))/2):
- z1 = 2.5: I_ANTI = 0.0635779652453, I_SAME = 0.0641560879254, both equal to the paper's 13 digits.
- T = 2: pair H(P||Q) = 0.221269, reverse H(Q||P) = 0.205107, both as printed. Best-of-two: my quadrature
  gave 0.223235; the repository's independent_check gives 0.2232343935, so the paper's 0.223234 is right and my
  sixth digit was quadrature error (a split run at z1 = 2 to 10 digits is in t353_digits.out).
- Certificate interval [2.1, 2.6]: integral of I_SAME - I_ANTI = 1.5146e-3 >= the claimed 1.04e-4 (which is the
  certified minimum 2.0828e-4 times the length); grid minimum 2.3915e-4 >= 2.0828e-4.
- T = 3 point y = (-0.1, 2.25): diff 1.535260930e-3, equal to the paper's ten digits; the four corners of the box
  give 0.94e-3 .. 1.74e-3, all positive.
- z1 = 1.7: diff -9.96e-3 (SAME loses there, as the paper says).

Correction made (685321f, author the author, SHA256SUMS lines for paper/main.tex and paper/main.pdf rebuilt
from the staged blobs; a clean clone with core.autocrlf=false passes sha256sum -c on all 106 lines):
1. Section 3 said "The numerical grid detects a transition near z1 = 2.005." The transition is exactly z1 = 2.
   At z1 = 2 the weights give alpha = sqrt(e) gamma; the ANTI integrand is then positive exactly on s > 2 and the
   SAME integrand exactly on s > 0, and both integrals equal beta(1/2 - sqrt(e)(1 - Phi(1))). Bisection of the
   difference lands on 2.0000 (t353_trans.py); 2.005 was the first point of a 0.005 grid. The sentence now states
   the exact value and its reason. The rest of the paragraph (no upper cutoff; the analytic argument at z1 >= 3)
   is unchanged.

Not changed, noted: the lint's W19 flags \cite{code} as "own earlier work"; it is the code repository, so it stands.
Not checked: the Renyi and KL certificates of Section 5 were not re-run (their outputs are in code/outputs and were
replayed independently on 22 October, reviews/2026-10-22/); the analytic argument of the last section was read once
for its logic, with no second independent derivation.

## Addendum, 08:40: the sixth digit of the best-of-two value

The integrand max(alpha phi(s) + beta phi(s-a) - e^eps (gamma phi(s) + beta phi(s-c)), 0) is phi(s) times a sum of three
exponentials in s, so it has at most two sign changes and its integral is a combination of normal CDF differences
(t353_exact.py). With that inner integral the outer quadrature gives pair 0.221268545320, gain 1.966041048453e-3 and best
0.223234586369; integrating max(SAME, ANTI) directly gives the same twelve digits, and the earlier split quadrature gave
0.2232345857. The value is 8.6e-8 above the rounding edge, so it is 0.223235 to six digits, not the printed 0.223234. The
repository's independent_check.py prints 0.2232343935 because it is a Riemann sum on a grid of step 0.005.

Fixed in yspennstate/shuffled-ablq-dominating-pair 9e54e0c: lines 71 and 211 read 0.223235; the sentence on
independent_check.py says it works on a grid of step 0.005 and quotes 0.22323; the funding paragraph gains the standing
Google Cloud line it lacked. PDF rebuilt (0 overfull, no undefined references); SHA256SUMS lines 94-95 taken from the
committed blobs; a fresh clone with autocrlf off passes all 106 lines.
