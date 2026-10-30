# T392 What classifier-free guidance does to the sampled distribution

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
09:4x-10:2x).

## STATEMENT
Repaired (per the audit of 16 Oct 05:08): fix a mixture of K Gaussians with common nondegenerate covariance Sigma, positive
weights and centers mu_1..mu_K; the Ornstein-Uhlenbeck forward process started from it; exact conditional and unconditional
scores; the guided score s_uncond + w (s_cond - s_uncond) with w > 1; and the reverse SDE (DDPM) in continuous time, run from
the stationary Gaussian at a stated horizon T (or T -> infinity). Ask for (a) the law of the output, or two-sided bounds on its
differential entropy, and (b) a bound on its distance (TV or W2) to the tilted law p(x)^(1-w) p(x | c)^w, each as an explicit
function of w and of the separation min_{j != c} |Sigma^(-1/2)(mu_c - mu_j)|; and compare with the probability-flow (DDIM)
endpoint. Finite-step error is a separate question; the DDIM entropy comparison of Wu et al. is taken as known.

## FRONTIER
- Wu, Chen, Li, Wang, Wei arXiv:2403.01639: for Gaussian mixtures, guidance raises classification confidence and lowers the
  differential entropy of the output; per the abstract the analysis covers DDPM and DDIM. (The row says the entropy result is
  for DDIM; the abstract says both samplers are covered, so the open part is the explicit dependence, not the sign.)
- Bradley, Nakkiran arXiv:2408.09000: neither DDPM nor DDIM with CFG samples the gamma-powered law; in the SDE limit CFG equals
  a DDIM predictor for the conditional law combined with a Langevin corrector for a gamma-powered law with a specific gamma.
- Chidambaram, Gatmiry, Chen, Lee, Lu arXiv:2409.13074: guidance does not sample the tilted law; fine-grained dynamics for
  mixtures of compactly supported laws and for mixtures of Gaussians: larger guidance pushes samples toward the boundary of
  the conditional support, and with any score error large guidance leaves the support.
- Fu, Yang, Wang, Chen arXiv:2403.11968: sample complexity of conditional diffusion models (statistics, not guidance's law).
- In this repository: T392_Gaussian_diagnostic.md reproduces the exact single-Gaussian endpoint equations of Bradley and
  Nakkiran (per the audit).

## ARCHITECTURE
For a single Gaussian the guided reverse SDE is linear and its endpoint is Gaussian with a computable covariance. For a mixture
the guided drift is the single-Gaussian drift plus a posterior-weighted sum over components; along the reverse path the
posterior on the class sharpens, and the endpoint is a mixture whose components are guided Gaussians reweighted by the
path-dependent posterior.

## FAILURE POINT
The posterior weights along the guided path are themselves driven by the guided process, so the endpoint is not a mixture with
fixed weights; the comparison-inequality method of 2403.01639 gives signs (entropy down) but not the size as a function of w
and separation.

## SHAPE
Days: two components on the line, equal variance, exact scores: write the guided reverse SDE, compute the endpoint law by a
one-dimensional Fokker-Planck solve on a grid for a range of w and separations, and fit the large-separation asymptotics; then
prove the asymptotic form (component variance shrinks like a known function of w; cross-component leakage like
exp(-c(w) separation^2)).

## OBSTRUCTION
A closed or two-sided explicit form for the class posterior along the guided DDPM path; without it, entropy and distance to the
tilted law are only signed, not sized.

## TARGETS
1. One dimension, two components, separation m: numerically exact DDPM and DDIM guided endpoints for w in {1.5, 2, 4, 8}
   and m in {1, 2, 4}; entropy and TV to the tilted law.
2. Prove the large-m limit: each guided component's variance and the leakage exponent c(w).
