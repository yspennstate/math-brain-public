You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/, sources/ of another run):
open problem I0006B, the borderline case gamma = d/2 left open in A. Bou-Rabee and C. Panagiotis, "Quantitative explosion and
percolation of the divisible sandpile", arXiv:2609.02829v1 (Theorem 1.3(iii)(b), p.6, excludes gamma = d/2; proof overview p.10 says
the borderline is not treated). Companion: "Sharpness and critical scaling of parking", arXiv:2609.02820v1, Theorem 3.4, p.14.
Model: d >= 5, P f(x) = (2d)^(-1) sum_{y~x} f(y), u_0 = 0, u_{n+1} = (eta + P u_n)_+, eta i.i.d. with mean zero, positive finite
variance, an exponential moment of |eta|.
The claim is PROVED: if exp(-C t^p) <= P(eta(0) < -t) <= exp(-c t^p) for t >= t_0 with p = d/2, then
    E u_n(0) is of order (log n)^(2/d) (log log n)^(1-2/d)   (two-sided bounds, constants not universal),
with rare-event cost Phi(m) = (1+m)^p / [log(e+m)]^(p-1). Secondary claim: for 0 < gamma < 1, two-sided stretched-exponential lower
tail exp(-C t^gamma) <= P(eta < -t) <= C exp(-c t^gamma) and an exponential upper-tail bound give E u_n(0) of order (log n)^(1/gamma).
The argument (REPORT sections 1-2 and onward): the companion's Lemma 6.4 (pp.53-54, eq. (92)) is where gamma = d/2 is excluded,
because sum_y G(0,y)^q with q = d/(d-2) diverges logarithmically; truncating at the crossover radius L ~ lambda^(1/(d-2)) gives a
log Laplace term lambda^(d/(d-2)) log lambda whose Legendre transform costs s^(d/2)/(log s)^(d/2-1); Theorem 6.6 (pp.55-56, (93)-(98))
is rerun with Phi in place of s^min(gamma,d/2); the lower bound comes from a variational configuration of holes with depths
a_y ~ (m/log L)(1+|y|)^(-2) in a ball (REPORT (5)-(6)), not a single hole or a constant-depth ball.

Break it if it is wrong.
1. Get both arXiv sources into sources/ as plain text (check the listings for later versions). State exactly the companion's
   Theorem 1.3 (all parts), assumption (85), (86)-(87), Theorem 6.1, Corollary 6.2, Proposition 6.3, Lemma 6.4, Lemma 6.5 and
   Theorem 6.6 with every hypothesis and constant, and say which steps use gamma != d/2.
2. Upper bound: check the modified Lemma 6.4 at gamma = d/2 line by line: the Green function asymptotics, the truncation radius,
   the Laplace transform bound uniform in lambda, the Legendre transform and its inversion, and that the rest of Theorem 6.6
   ((94)-(98): smoothing, time windows, concentration from Lemma 6.5) goes through with Phi with constants independent of n.
   Is the loglog power exactly 1 - 2/d after inverting Phi at level log n? Recompute it yourself.
3. Lower bound: check the hole configuration: that it is admissible for the tail (1) (cost sum of a_y^p with the lower tail bound
   only for depths above t_0; what happens to the many sites with depth below t_0?), that its probability is at least
   exp(-C Phi(m)), that it forces E u_n(0) >= c m at the stated n (how the deficit propagates into the odometer: is a Green-weighted
   deficit sum_y G(0,y) a_y >= m really enough, with the time truncation of G at time n?), and the independence or FKG steps used.
4. The secondary (log n)^(1/gamma) claim for gamma < 1: is it new, or already in the companion or in the parking paper? Check its
   proof, in particular the claim that no exponential moment of |eta| is needed.
5. Ask the hard question: if the borderline is a routine truncation, why did the authors exclude it? Search for any later version
   or paper (2026) that treats gamma = d/2. Compare with analogous borderline loglog corrections in the literature (random walk
   in random scenery, Donsker-Varadhan large deviations, the "Swiss cheese" or Lifshitz-tail borderline).
6. Write your own independent code (do not reuse claim_files/code): check the finite-ball variational problem (5)-(6) numerically
   and the growth of sum_{|y|<=L} G(0,y)^(d/(d-2)) for d = 5, 6. Evidence only; keep runs small.
7. Verdict on value: correct or not, novel or not, exactly what is proved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
