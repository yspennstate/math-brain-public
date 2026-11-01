# C0029 referee packet, checkpoint 1

Exact target and the 2025 theorem are in SOURCE_STATUS.json. Current exact openness is UNKNOWN. I checked the actual inequalities, not a source hash.

## w573-C0029-001: KEEP for the logical statement; FIX the source wording

The claim that a bound with a positive o(1) multiplier does not imply coefficient one plus an exponential additive error is correct. Independently, let X_n be uniform on [0,n/(n+1)]. Then F_n(t)=min((1+1/n)t,1) and at t=1/n (n>=2), F_n(t)-t=1/n^2, larger than C exp(-a n) for every fixed a,C>0 eventually. This checks the load-bearing implication failure. The arXiv abstract is a source for the theorem's multiplier, but the abstract itself does not prove the logical nonimplication; use this explicit counterexample as proof. The original C0029 statement in Bordenave-Chafai is for large n and small t; the 2025 paper states all epsilon>=0 asymptotically. All-n equivalence in STATEMENT.md needs an argument for finitely many n.

## S1.w574.1: KEEP, preliminary mathematical content

I independently recomputed the CDF and the witness threshold above, including n>=2 and all t>=0. The distribution is continuous. The assertion is solely about removing a positive multiplier from an abstract tail estimate. It is not a counterexample to C0029. Served-model identity of this referee thread is not available to me, so the coordinator must treat this as preliminary until that gate is checked.

## Prior intake correction: FIX

The C0029-A001 row in the 2026-09-07 intake calls 1-exp(-t-t^2/2) the exact finite-n real Gaussian law. At n=1 the law is 2Phi(t)-1 and the two derivatives at t=0 differ: sqrt(2/pi) versus 1. Keep Edelman's finite-n inequality P(sqrt(n)s_min(G_n)<=t)<=t (Sah-Sahasrabudhe-Sawhney, Theorem 9.4), and label 1-exp(-t-t^2/2) as the limiting law.

NEXT: Check finite-n Gaussian slack and the math-brain retrieval; define the smallest Bernoulli-specific comparison estimate needed.
