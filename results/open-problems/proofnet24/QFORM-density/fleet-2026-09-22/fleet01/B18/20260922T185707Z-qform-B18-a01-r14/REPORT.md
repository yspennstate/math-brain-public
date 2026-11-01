SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B18, 2026-09-22T18:57:07Z.
attacking: literature-to-proof transfer for the rank-one one-sided Schur branch, replacing two coarse L-infinity-to-half-Riesz steps by sharp rearrangement plus the uniform negative-moment theorem.

# fleet01/B18 — Rogozin/CKT half-Riesz transfer and improved rank-one Schur payment

Programme: QFORM-DENSITY-3EIG-20260922.  Full target status: OPEN / NOT PROVED.  Continuity is tracked separately and is not claimed by the theorem below.

Control source at startup: yspennstate/math-research-brain main 9b1ac42c5c80793bb4633c765cbd15c0a135101c, owner control revision 2026-09-22.11. Before publication I refreshed the control branch and consumed the newer corrections QFORM-EXACT-BANK-SEPARATION-NOT-FORCED-v1 and QFORM-SCALAR-LEAKAGE-CONDITIONAL-23-MOMENT-FALSE-v1. Neither is used as a premise; this run makes no structural-exhaustion or scalar-fiber claim.

Execution context: WITHOUT_VERIFIED_BRAIN. Repository retrieval/coordination is genuine; native learned-memory receiver use was not verified.

## 1. Primary literature transferred

(1) T. Juskevicius and J. D. Lee, "Small ball probabilities, maximum density and rearrangements", arXiv:1503.09190, Theorem 1. For independent real random variables Yi whose densities are bounded by Ki, the probability that sum Yi lies in an arbitrary measurable set S is at most the probability that the sum of independent centered uniform comparators Ui lies in the centered interval of the same Lebesgue measure, where Ui has density Ki on [-1/(2Ki),1/(2Ki)]. In dimension one this is the sharp Rogozin rearrangement principle.

(2) G. Chasapis, H. Konig, T. Tkocz, "From Ball's cube slicing inequality to Khinchin-type inequalities for negative moments", J. Funct. Anal. 2021, arXiv:2011.12251, Theorem 1. If Uk are iid Uniform[-1,1], p in (0,1), then

  E |sum ak Uk|^{-p} <= Cp (sum ak^2)^{-p/2},

with Cp=max(c2(p),cinf(p)). Since p=1/2 is below their transition p0=0.793..., Cp=cinf(p), hence

  C_{1/2}=(3/2)^{1/4} Gamma(1/4)/sqrt(pi).

These hypotheses are an exact source match after scaling: no moments, centering, support, log-concavity or identical laws are imposed on the original QFORM inputs.

## 2. New sharp source-valid projection half-Riesz bound

Let X1,...,Xn be independent real variables with probability densities bounded by one, and let a in R^n be nonzero. Define L_a=sum ai Xi. Then

  sup_{s in R} E |L_a-s|^{-1/2}
  <= K_* ||a||_2^{-1/2},                                      (2.1)

where

  K_* = 6^{1/4} Gamma(1/4)/sqrt(pi)
      = 3.2014295649052241089... .                              (2.2)

Proof. Omit zero coefficients. Each ai Xi has density cap 1/|ai|. For r>0 and arbitrary s, Juskevicius-Lee gives

  P(|L_a-s|<r)
  <= P(|sum ai Vi|<r),                                         (2.3)

where Vi are iid Uniform[-1/2,1/2]; signs of ai are immaterial by symmetry. Layer cake for the kernel |x|^{-1/2} yields

  E|L_a-s|^{-1/2}
  = integral_0^infinity P(|L_a-s|<u^{-2}) du
  <= E|sum ai Vi|^{-1/2}.                                      (2.4)

Write Vi=Ui/2 with Ui Uniform[-1,1]. Chasapis-Konig-Tkocz at p=1/2 gives

  E|sum ai Vi|^{-1/2}
  = sqrt(2) E|sum ai Ui|^{-1/2}
  <= sqrt(2) C_{1/2} ||a||_2^{-1/2}
  = K_* ||a||_2^{-1/2}.                                       (2.5)

This proves (2.1). The uniform-comparator negative-moment constant is sharp in the cited theorem; no density-cap-to-bathtub relaxation has been inserted after (2.3). QED.

## 3. Apply the completed fleet02/B18 result to an actual inequality

Consume the exact completed partner source:

  yspennstate/math-open-problems@aa0b07137085e1b6e948c00052ff0689343a0cee
  proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260922T181504Z-fleet02-B18-QFORM-r12/REPORT.md

and its late-correction supplement at commit 55114f49ab8188c8a90cf998c66d8627d655dec4.

The partner proved the one-sided-cross setup and the fractional square transducer. I keep that exact architecture, but replace the two coarse LPP-density-cap half-Riesz estimates by (2.1).

Let U and V be mutually independent physical coordinate families, all coordinate densities <=1. Let B have rank one,

  B=sigma u v^T,

with sigma>0 and unit vectors u,v. Let G(U) be arbitrary measurable and beta arbitrary. Put

  T=G(U)+2 U^T B V+beta^T V.                                  (3.1)

Condition on U. With W=u^T U and

  c(U)=2 sigma W v+beta,

we have, by (2.1) applied to the original V bank,

  sup_t E_V[|T-t|^{-1/2}|U]
  <= K_* ||c(U)||_2^{-1/2}.                                  (3.2)

Since ||c(U)|| >= |<v,c(U)>|,

  ||c(U)||^{-1/2}
  <= |2 sigma W+<v,beta>|^{-1/2}.                             (3.3)

Apply (2.1) again, now to the genuine original-product linear form W=u^T U, including the arbitrary translation <v,beta>/(2sigma):

  E |2 sigma W+<v,beta>|^{-1/2}
  <= K_* / sqrt(2 sigma).                                     (3.4)

Therefore

  boxed: sup_t E|T-t|^{-1/2}
  <= C_R1 sigma^{-1/2},                                       (3.5)

where

  C_R1 = K_*^2/sqrt(2)
       = sqrt(3) Gamma(1/4)^2/pi
       = 7.2472443566803678827... .                           (3.6)

This improves the completed fleet02/B18 rank-one constant 8 by about 9.4094455 percent, while preserving all of its arbitrary G(U), arbitrary beta, arbitrary dimension and arbitrary cap-one-law hypotheses. There is no post-rotation independence claim.

## 4. Improved physical Schur consequence

Use the partner's proved half-Riesz square transducer exactly as stated. Take an original physical pivot Y with a=A_YY !=0 and Schur complement

  S=A_{-Y,-Y}-A_{-Y,Y} A_{Y,-Y}/a.                            (4.1)

Partition the residual physical coordinates into disjoint I,J,O. Assume S[J,J]=0 and rank S[I,J]=1 with singular value sigma>0; all S[I,I], all O blocks/couplings, affine terms and additional ambient spectrum are arbitrary.

Conditioning on X_O puts the Schur residual into (3.1) uniformly. Completing the physical pivot gives

  Q=a(Y+a^{-1}A_{Y,-Y}X_{-Y})^2+R.                            (4.2)

Given R=r, the shifted pivot is a mixture of translations of the original independent physical Y density, hence its conditional density cap is still one. Applying fleet02/B18's fractional square transducer to (3.5) gives

  boxed:
  ||p_Q||_infinity
  <= [sqrt(3) Gamma(1/4)^2/pi]
     / sqrt(|a| sigma)
  = 7.247244356680368... / sqrt(|a| sigma).                   (4.3)

Call this QFORM-ONE-SIDED-SCHUR-RANK1-CKT-v1.

This is a target-level supporting theorem, not the full conjecture. Essential boundedness is proved in this branch. Continuity is not asserted.

## 5. Concrete target-valid application

Apply (4.3) to the exact family already used by the partner. Let I,J be disjoint m-coordinate banks, choose orthonormal u,w in R^I and unit v in R^J, set

  S_II=ww^T,  S_IJ=u v^T,  S_JJ=0,

and add an independent physical scalar pivot a=1. In the orthonormal basis (u,w,v), the residual matrix is

  [[0,0,1],[0,1,0],[1,0,0]],

so the full nonzero spectrum is {1,1,1,-1}; this is inside the owner's target for every m>=2. Here sigma=1. Thus for every admissible independent product law,

  boxed: ||p_Q||_infinity <= 7.247244356680368... .            (5.1)

The previous partner theorem gave 8 on the same family. This improvement is dimension-free and comes entirely from source-valid rearrangement/negative-moment transfer.

## 6. Corrections and exact remaining gap

This theorem does not use: arbitrary-joint coarea, positive moments of conditional spectral densities, worst scalar Q_rest fibers, exact spectral bank separation, a universally good physical minor, post-rotation independence, or a pointwise characteristic-function decay. It is therefore compatible with the current correction ledger, including the fresh QFORM-EXACT-BANK-SEPARATION-NOT-FORCED-v1 and QFORM-SCALAR-LEAKAGE-CONDITIONAL-23-MOMENT-FALSE-v1 events.

The unpaid full-target implication is still structural/nonperturbative:

  from s_3(A)>=1, outside the already-paid ridge-window and quantitatively invertible indefinite-pair branches, obtain a product-preserving grouped-coordinate certificate that can be paid without assuming exact bank separation, or prove a different global averaging theorem that covers the overlap between nonzero self-curvature and cross curvature.

The fresh bank-separation counterexample shows that the certificate cannot require an exact spectral 1+2 decomposition with disjoint physical supports. The present theorem instead says that whenever an exact one-sided-zero rank-one Schur packet is obtained by some valid reduction, its payment is now 7.247244... rather than 8.

Full QFORM remains OPEN / NOT PROVED.

## Source pins

- Juskevicius--Lee, arXiv:1503.09190, Theorem 1.
- Chasapis--Konig--Tkocz, arXiv:2011.12251 / JFA 2021, Theorem 1, p=1/2.
- fleet02/B18 partner report: math-open-problems@aa0b07137085e1b6e948c00052ff0689343a0cee, path above.
- fleet02/B18 late correction: math-open-problems@55114f49ab8188c8a90cf998c66d8627d655dec4.
- fresh structural correction QFORM-EXACT-BANK-SEPARATION-NOT-FORCED-v1: math-research-brain commit 6976b2fad428ef44c76125a6ab34339b5a5d9b44.
- fresh conditional-moment correction QFORM-SCALAR-LEAKAGE-CONDITIONAL-23-MOMENT-FALSE-v1: math-research-brain commit 594599ea6dbb5baf53bd4090501c89211c66fae7.
