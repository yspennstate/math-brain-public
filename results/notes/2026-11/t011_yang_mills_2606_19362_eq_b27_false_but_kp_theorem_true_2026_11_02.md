---
name: t011_yang_mills_2606_19362_eq_b27_false_but_kp_theorem_true_2026_11_02
description: T011 arXiv:2606.19362 Eq. B.27 false (sum_T x^deg1 = x(x+n-1)^(n-2)), B.28 series diverges; but it only breaks a re-proof of the true Kotecky-Preiss theorem, not the paper's main claim
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T09:59:59+04:00
  status: verified
  evidence: "brain-repo 06_math_research/frontier/rows/T011/moves.jsonl 42d9c9eb"
---

T011 (Yang-Mills mass gap / confinement), first move m011a (moves.jsonl 42d9c9eb, 2 Nov): an audit of the row's rejection of arXiv:2606.19362v1 (Faizal and Shabir, 593 pages). Eq. (B.27) on PDF p. 164 claims (1/n!) sum_T x^deg(1) <= x^(n-1)/(n-1)!. Exactly, sum_T x^deg(1) = x (x+n-1)^(n-2) (Pruefer; enumerated for n <= 7). So the row's n 4, x 1 counterexample (2/3 vs 1/6) is right, and for any fixed x > 0 the inequality fails for all large n. The series in (B.28), claimed to equal e^x, diverges (2.6e21 by n 60 at x 1). The appendix's proof of its Theorem B.1 is broken. But Theorem B.1 is the standard Kotecky-Preiss criterion, which is true, and it is used only at strong coupling, where convergence is classical. So this error alone does not refute the paper, and the row's rejection should rest on the weak-coupling or continuum steps, which are not yet audited. Lesson: a false lemma in a proof of a known theorem is not a refutation of the paper; check what the lemma is used for before calling it decisive. Code: scratchpad t011/b27.py; t011/extract.py (pypdf, run with -P because -I drops the user site).


Addendum (2 Nov, m011b, moves.jsonl f4f32463): the load-bearing gap chain (Theorems 5.4 and 5.6, printed pp. 51-55) fails as written. To linearise (5.34), the proof says a_k is 'geometric with ratio b, so e^{a_{k+1}} <= c2', but a_k = b^k a_0 is unbounded. It also uses Delta_k <= 1 without justification. Worse, (5.34) with geometric ||E_k|| and geometric a_k can certify at most log(1/||E_k||)/a_{k+1} = O(k/b^k), which tends to 0; iterating it from Delta_0 1 with C0 1e-6 gives 0.0004 by k 16, where Theorem 5.6 would claim about 1. Theorem 5.6's 'Delta_0 - sum eps > 0' also does not follow from its hypotheses. So the rejection now rests on a load-bearing step, not just the appendix lemma. This is a gap in the proof, not a disproof. Not yet checked: whether Sections 10-11 reach the gap independently of Sec. 5.

Addendum (2 Nov, m011c, moves.jsonl 8f109997): Theorem 11.1 (the stated spectral gap, printed pp. 128-130) takes the same summable-defect interlacing as hypothesis (ii). Its proof uses that lower bound on T_{k+1} as an upper bound. (11.7) also drops the factor a_k/a_{k+1} = 1/b, so even with zero defect it gives only Delta_k >= Delta_0/b^k. And it again calls e^{a_k Delta_k}/a_{k+1} uniformly bounded. The 'Tauberian route' assumes the uniform clustering of Theorem 5.7, whose proof goes through the per-scale gap (read to (5.50)). Every route found to the uniform gap passes through the broken mechanism, so the mass-gap claim is unproved as written. Lesson: when a multiscale proof compares T_{k+1} with one step of T_k, check the time-step ratio; a gap in physical units loses a factor b per step unless T_k^b is used.
