SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T09:06:05Z.
attacking: dense nonseparable Schur-bank localization—keep whole active product banks intact through curvature/volume payment, then condition only outside original coordinates; test whether high-leverage cancellation can be absorbed without support or moment assumptions.

# Early substantive checkpoint — critical |t|^{-1} Fourier decay pays the pair-log kernel

Status: supporting derivation; FULL QFORM OPEN; continuity separate.

## First unpaid implication

After completing an invertible indefinite physical pair B, the remaining rank-two *indefinite* Schur-bank branch is critical: its natural whole-bank Fourier decay is only |t|^{-1}, so it does not itself give an L1 Fourier density bound. The question is whether this critical decay is nevertheless strong enough for the logarithmic physical-pair kernel without any support, fragment, moment, or affine-shift restriction.

## New critical-Fourier-to-log lemma

Let Y be any real random variable with characteristic function satisfying

|phi_Y(t)| <= min(1,K/|t|),   t != 0.

Put

m0 = (sin(1/2)/(1/2))^2 = 4 sin^2(1/2),
cE = 2/m0 = 1/(2 sin^2(1/2)).

Then, uniformly in x and rho>0,

P(|Y-x|<=rho) <= min{1, cE K rho [1+log(1/(K rho))]}

when K rho<=1. Consequently, for every A>0,

sup_x E log_+(A/|Y-x|) <= Omega(KA),

where

Omega(y) = cE y [2+log(1/y)]  for 0<y<=1,
           log y + 2 cE       for y>=1.

Proof: use the squared-sinc majorant

k_rho(u) = [sin(u/(2rho))/(u/(2rho))]^2.

On |u|<=rho, k_rho(u)>=m0. Its Fourier transform is the triangular function, so

P(|Y-x|<=rho)
 <= m0^{-1} rho int_{-1/rho}^{1/rho} |phi_Y(t)| dt.

When K rho<=1 the integral is 2K[1+log(1/(K rho))], proving the concentration bound. Layer cake,

E log_+(A/|Y-x|)=int_0^infinity P(|Y-x|<A e^{-s}) ds,

then gives Omega exactly: for KA<=1 integrate cE KA e^{-s}[1+log(1/(KA))+s]; for KA>=1 use the trivial bound 1 until s=log(KA), and the preceding tail afterwards.

This is the critical bridge missing from a direct L1-Fourier argument: |t|^{-1} is nonintegrable, but it gives rho log(1/rho) concentration, which is integrable against the outer logarithmic pair kernel.

## Application to an indefinite rank-two Schur bank

Split original independent coordinates X=(U,V,Z), U in R^2, and let B=A_UU be invertible indefinite. Put D=|det B| and kappa=sigma_min(B). After exact physical-pair completion, condition only on the outside original coordinates Z=z. Suppose the V-Schur block S0 has rank exactly two and signature (+,-), with nonzero eigenvalues lambda_+, lambda_- and

P=|lambda_+ lambda_-|.

Let a,b be orthonormal eigenvectors of S0 in the original V-coordinate space and assume the whole rank-two eigenspace has coordinate leverage

max_i (a_i^2+b_i^2) <= 1/2.

The newest Claude Fresnel-Brascamp-Lieb theorem (FOURIER_ROUTE_REPORT.md, source family beginning math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837) applies to

R_z(V)=V^T S0 V+q(z)^T V+d(z)

with arbitrary q(z): linear terms are harmless twists. It gives uniformly in z

|phi_{R_z}(t)| <= min{1, K_F/|t|},
K_F = 4 pi / sqrt(P).

Therefore the new lemma yields

sup_{z,x} E[log_+(A/|x-R_z|) | Z=z] <= Omega(K_F A).

Insert this into the completed physical-pair logarithmic envelope used by the designated partner fleet03/B14 r31:

p_Q(t) <= 2sqrt(2)/r + D^{-1/2} E log_+(2r^2/(kappa |t-R|)).

With y=2 K_F r^2/kappa,

||p_Q||_infinity <= inf_{y>0} { 4 sqrt(K_F/(kappa y)) + D^{-1/2} Omega(y) }.

Choosing y=1 already gives the explicit bound

||p_Q||_infinity
 <= 4 sqrt(K_F/kappa) + 2cE D^{-1/2}
 = 8 sqrt(pi) kappa^{-1/2} P^{-1/4}
   + [sin(1/2)]^{-2} D^{-1/2}.

Numerically the two absolute coefficients are 14.179630807... and 4.350685299... .

Crucially, unlike the semidefinite partner branch, NO range-compatibility condition on q(z) is needed: arbitrary conditioning-generated affine terms are admitted by the Fourier theorem itself. No rotation of the input variables is declared independent.

## Partner composition

Fleet03/B14 r31 proves the complementary rank-two semidefinite Schur-bank branch, with exact zero-cost removal of range-compatible q(z), a 2D product-projection cap, and the optimized pair-log bound. Its canonical report is math-open-problems@1d80c85a03f6d442c7771e0df3313ec80aab8446, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T083627Z-fleet03-B14-QFORM-r31/REPORT.md`.

Thus after a controlled indefinite physical pair, rank-two Schur curvature now has two complementary paid exits:

- semidefinite rank two + range-compatible affine bank term: partner r31;
- indefinite rank two + eigenspace leverage <=1/2: the critical-Fourier-to-log compiler above, with completely arbitrary affine bank terms.

Remaining: high-leverage indefinite rank-two Schur curvature, semidefinite kernel-affine leakage, higher-rank/mixed-sign dense Schur curvature, or a structural N3 argument forcing another already-paid D'/D5/hub/ridge/bank exit. None is claimed solved here.
