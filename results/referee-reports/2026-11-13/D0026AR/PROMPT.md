You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0026, Martinelli-Shapira-Toninelli, "Long time behaviour of one facilitated kinetically constrained models: results
and open problems", arXiv:2510.20461, Conjecture 1, Section 1.1, PDF p. 2: for FA-1f on Z, every q in (0,1), every local f,
E_nu f(eta_t) -> pi(f) whenever nu(there is an infected vertex) = 1. The claim says PARTIAL: Theorem A, for every q in (1/2,1),
every deterministic eta with at least one zero and every local f, P_t f(eta) -> pi(f), exponentially fast uniformly over eta with
eta_z = 0 for fixed z; hence convergence for every law nu supported on configurations with a zero. It is proved by a reduction
from one zero to Blondel-Cancrini-Martinelli-Roberto-Toninelli 2013, Theorem 2.1 (arXiv:1205.4584, pp. 4-5), which needs
sup_x mu(theta^{d_x}) <= K, a hypothesis a single zero fails.

Break it if it is wrong.
1. Download arXiv:2510.20461, arXiv:1205.4584, Mountford-Valle arXiv:1609.01364 into sources/ as plain text. Read Conjecture 1,
   what the survey says is known (p. 2 and Section 4), BCMRT Theorem 2.1 with its exact hypotheses and constants, and
   Mountford-Valle Theorem 1.1 and Remark 1.2.
2. Check the reduction line by line: how the process started from one zero produces, at some intermediate time s, a law with
   uniformly bounded exponential gap moments (the choice 1 < theta < q/p, the drift of the infected region for q > 1/2, every
   probability bound, whether the Markov property is applied at a stopping time or deterministic time correctly, whether the
   BCMRT constants stay uniform), and whether the far-away part of the line (healthy, unreached by time s) is handled. Check
   that the final mixture over nu needs no moment assumption, as claimed.
3. Simulate independently with your own code (do not reuse claim_files/code): FA-1f from a single zero, q = 0.55 and 0.7,
   E f(eta_t) for f = 1{eta_0 = 0}, as evidence.
4. Verdict on value: is Theorem A correct; is it already in print (BCMRT, Mountford-Valle, Blondel, Ertul, Shapira, Hartarsky,
   2025-2026 papers citing 2510.20461); does it genuinely settle Conjecture 1 for q > 1/2? What remains open?
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
