# C0052: exact source statement, before proof exchange

Primary source: Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, arXiv:1707.00520v1 (2017), Conjecture 6 on printed page 94; equations (7.1)-(7.2) on that page and Exercise 61 on printed page 95. Public source: https://arxiv.org/pdf/1707.00520 .

Source quote: "Prove that the three-dimensional Ising model is non-trivial" (Conjecture 6, first clause).

Use the zero-field ferromagnetic nearest-neighbor Ising model on Z^3 with unit edge couplings and its infinite-volume free Gibbs state at 0 < beta < beta_c. Write

G_beta(x) = <sigma_0 sigma_x>_beta,
chi(beta) = sum_(x in Z^3) G_beta(x),
xi(beta) = [lim_(n->infinity) -(1/n) log G_beta(n e_1)]^(-1).

Thus xi is the exponential correlation length along a coordinate direction, NOT a second-moment correlation length. Let

U4_beta(x1,x2,x3,x4) = <sigma_x1 sigma_x2 sigma_x3 sigma_x4>_beta
  - G_beta(x2-x1)G_beta(x4-x3)
  - G_beta(x3-x1)G_beta(x4-x2)
  - G_beta(x4-x1)G_beta(x3-x2).

The source uses the signed coupling

g(beta) = [sum_(x,y,z in Z^3) U4_beta(0,x,y,z)]/[chi(beta)^2 xi(beta)^3].

The exact first-clause target is that g(beta) does NOT tend to zero as beta approaches beta_c from below. Since U4 <= 0, define lambda(beta)=-g(beta)>=0. The target is equivalently limsup_(beta->beta_c) lambda(beta)>0; a uniform liminf lower bound would be a stronger sufficient conclusion. Existence of a limit of g is not assumed.

The source calls a model trivial when g tends to zero. Its broader discussion concerns Gaussian factorization of a scaling spin field. The source does not specify a distribution topology, uniqueness of a limit, conformal invariance, or a strict positive anomalous exponent. Those are separate requirements, and we will not silently add them or assert that the signed-coupling definition alone proves them.

Current openness as of this session: UNKNOWN. The September intake reports an attempted-unsolved result; the bounded primary-literature search recovered the 2017 source, the 2022 surveys, and results for dimensions at least four, without a verified resolution of the 3D first clause. That is not an exhaustive status certification. No novelty or solved claim.

Lane: attempt a lower bound for the source's normalized coupling through an average under the ORIGINAL two sourced-current laws. The uniform critical overlap estimate will remain an explicit unproved input unless established. A statement-only packet is sent to adversary w469 before the full proof packet goes to referee w470.

NEXT: Pin down the exact endpoint-weighted overlap probability and its second-moment input.
