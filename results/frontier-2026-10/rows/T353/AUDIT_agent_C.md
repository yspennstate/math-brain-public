# T353 audit of REFUTATION_T2 (agent C, 19 Oct 2026)

Verdict: CONFIRMED at T = 2, sigma = 1, eps = 1/2, every b, d = 1. The adaptive switch exceeds the conjectured pair's
hockey-stick in both orders' maximum, which is the quantity the paper's tight domination compares. One independent audit;
the row asks for two.

## Scope against the paper (arxiv.org/html/2403.17673, read 19 Oct 2026)

- Dominating pair (Def. 2.3): (P, Q) dominates (A, B) if D_{e^eps}(P||Q) >= D_{e^eps}(A||B) for all eps; the paper's
  delta(eps) for the pair is max{D(P||Q), D(Q||P)}. Zero-out adjacency is symmetric (one of x_i, x'_i is bottom), so the
  mechanism must be dominated in both orders. The example's D(M(x)||M(x')) = 0.22324 exceeds max(0.22127, 0.20511), so it
  breaks domination under either reading (one order or the symmetric max). One eps suffices: domination is "for all eps".
- ABLQ_S: n = bT, a secret random permutation cut into fixed slices, adaptive psi_t: X -> unit ball given g_1..g_{t-1},
  Gaussian noise sigma^2 I. The example uses exactly this: d = 1, |psi| <= 1, psi(bottom) = 0, the switch is a function of
  g_1 only.
- Conjecture 3.2 reads "(P_S, Q_S) tightly dominates ABLQ_S for all adaptive query methods". No restriction on b or d is
  stated; T = 2 is a value of T. b = 1 (n = 2) and every b >= 2 are in scope, and b drops out of the shifted outputs.
- The paper's own lower bound (Section 3) is a single non-adaptive instance and it says it does not rely on the
  conjecture; the adaptive case is exactly the conjecture's content.

## Model re-derived by hand

With the other 2b - 1 records equal to w and the shift g_t -> g_t - b psi_t(w) (an invertible map of the transcript
given g_1, so every divergence is preserved), batch 1 holds i with probability 1/2 and:
x : i in 1 -> (-2, 0); i in 2 -> (0, psi_2(u) - psi_2(w)). x' : i in 1 -> (-1, 0); i in 2 -> (0, -psi_2(w)).
ANTI (+1, -1) gives (0, 2) / (0, 1), a sign flip of coordinate 1 of (P_S, Q_S); SAME (+1, +1) gives (0, 0) / (0, -1).
This matches the write-up line for line.

## Independent numerics (audit_C/indep_check.py, output indep_check_s1_e05.txt)

Different method from the candidate's: the inner integral is exact (sign changes of the equal-variance Gaussian
mixture bracketed on a grid and refined by brentq, then normal CDFs between roots); the outer integral is Simpson on
1601 points with the policy taken pointwise.

    g1 = -2.5: I_anti 0.063577965245  I_same 0.064156087925  diff +5.781e-4   (candidate: +5.78e-4)
    g1 = -3.0: diff +4.531e-6 (candidate +4.53e-6);  g1 = -1, 0: SAME loses.
    P||Q: conjectured 0.221268, adaptive 0.223235, gain +0.001967; SAME wins on g1 in [-5.20, -2.01]
    Q||P: conjectured 0.205107, adaptive 0.211853
Control: the conjectured pair comes out at 0.221268 against the candidate's 0.221273 (2-D grid) and 0.221271.
I_same at -2.5 differs from the candidate's mpmath value in the 8th digit (0.0641560879 vs 0.0641560990), most likely
mpmath quad missing a kink at a root; the difference is 1e-8 against a gap of 6e-4.

## What remains open

- A second audit (the row asks for two), ideally one that rebuilds the transcript law from Algorithm 3 without reading
  this note.
- Novelty: I did not search for a later paper that already notes the conjecture fails for adaptive methods
  (2411.04205 and its successors should be read before anything is called new).
- Interval bounds on I_same - I_anti near g1 = -2.5 would make the one-point inequality rigorous rather than 30-digit
  numerics; the closed form (roots of a two-term Gaussian difference) is within reach.
- The gain is small (0.9 percent of delta here); whether it persists or grows with T, and in the Renyi sense, is open.
