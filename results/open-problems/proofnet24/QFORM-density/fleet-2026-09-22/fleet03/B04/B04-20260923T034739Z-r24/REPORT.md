# QFORM fleet03/B04 r24 — leverage/tail tradeoff for the spectral-window ridge branch

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T03:47:39Z.

attacking: independent verification of the ridge-perturbation/MSS spectral-window step and a sharper two-parameter leverage-versus-tail Fourier gate.

## Status

Full QFORM remains OPEN. This report proves a supporting theorem for genuinely rotated indefinite matrices. It gives a continuous C_0 density in its stated scope. It does not assume Gaussianity, moments, log-concavity, compact support, connected support, or independence after rotation.

The proof uses original-coordinate product structure through the completed ridge Fourier theorem and MSS frame partitioning. It does not use the false law-uniform pointwise van-der-Corput estimate.

## Dependency checked and used

We use the completed supporting theorem `QFORM-RIDGE-DENSITY-v1` from

- repository `yspennstate/math-open-problems`
- commit `9c1167db05c7b0f520f060796fde921ed769a4e7`
- path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a physical cross block B, gamma>0,

K_gamma = B B^T (gamma^2 I + B B^T)^(-1),

theta_gamma = tr K_gamma.

If max_i (K_gamma)_ii <= 1/2 and theta_gamma>2, the theorem gives a bounded continuous C_0 density and, in particular,

||p_Q||_infty <= sqrt(e)/(sqrt(2) gamma) * theta_gamma/(theta_gamma-2).

All self-blocks and outside couplings are unrestricted.

I independently checked the two pieces assigned to fleet03/B04:

1. Perturbation lemma. If B=B0+F, S=range(B0), ||F||<=eta, then for v perpendicular to S,

v^T K_gamma v = ||(gamma^2 I+B^T B)^(-1/2) B^T v||^2 <= (eta/gamma)^2 ||v||^2,

because B0^T v=0. Since 0<=K_gamma<=I, decomposing e_i=P_S e_i+(I-P_S)e_i gives

sqrt((K_gamma)_ii) <= sqrt((P_S)_ii) + (eta/gamma) sqrt(1-(P_S)_ii).

Hence the stated coarser bound [sqrt(ell)+eta/gamma]^2 is valid whenever max_i(P_S)_ii<=ell.

2. MSS spectral-window application. Let U have orthonormal columns and rows u_i with ||u_i||^2<=mu. The two-part MSS partition gives I,J with

L I <= U_I^T U_I, U_J^T U_J <= (1-L) I,

where

L = 1/2 - mu - sqrt(2 mu).

Indeed the MSS upper bound is (1/sqrt(2)+sqrt(mu))^2=1/2+mu+sqrt(2mu), and the lower bound follows because the two Gram matrices sum to I. This is positive for mu<(1-1/sqrt(2))^2.

The rest of this report strengthens the fixed constants in the supplied spectral-window application by keeping mu and the tail threshold tau free.

## Theorem: two-parameter spectral-window ridge gate

Let A be real symmetric and have at least three eigenvalues of absolute value at least 1. Fix tau in [0,1). Let P_tau be the spectral projection onto the direct sum of eigenspaces with |lambda(A)|>=tau, and assume

mu := max_i (P_tau)_ii.

Put

L(mu) := 1/2 - mu - sqrt(2mu).

Assume L(mu)>tau and

sqrt(mu/L(mu)) + sqrt(6) tau/(L(mu)-tau) <= 1/sqrt(2).      (G)

Then for every product input X with independent one-dimensional densities bounded by one, Q=X^T A X has a continuous C_0 density and

||p_Q||_infty <= [9 sqrt(3e)]/[2 (L(mu)-tau)].               (1)

The same conclusion survives arbitrary real coordinate-separable measurable additions finite almost surely, exactly as in the ridge theorem.

### Proof

Write A=A_H+E, where A_H=P_tau A P_tau and ||E||<=tau. Choose U with orthonormal columns spanning range(P_tau), so A_H=U Lambda U^T. Because A has at least three eigenvalues of modulus >=1, the third singular value of Lambda is at least 1.

By MSS, partition the original coordinates into I,J so that both restricted Gram matrices satisfy

U_I^T U_I >= L I,    U_J^T U_J >= L I.

Let B0=A_H[I,J]=U_I Lambda U_J^T. Since U_I and U_J have smallest singular value at least sqrt(L), the singular-value product inequality gives

s_3(B0) >= sqrt(L) * s_3(Lambda) * sqrt(L) >= L.             (2)

Because U_J^T is onto and Lambda is invertible on the high spectral subspace,

range(B0)=range(U_I)=:S.

The orthogonal projector onto S is

P_S=U_I (U_I^T U_I)^(-1) U_I^T.

For every physical coordinate i in I,

(P_S)_ii = u_i^T (U_I^T U_I)^(-1)u_i <= ||u_i||^2/L <= mu/L.    (3)

For the full physical cross block B=A[I,J], write B=B0+F with F=E[I,J]. Compression cannot increase operator norm, so ||F||<=tau. Weyl's inequality and (2) give

s_3(B) >= sigma := L-tau >0.                                  (4)

Choose

gamma = sigma/sqrt(6).

Then at least three singular values of B are >=sigma, hence

theta_gamma = sum_j s_j(B)^2/(gamma^2+s_j(B)^2)
            >= 3 sigma^2/(sigma^2+sigma^2/6)
            = 18/7 >2.                                        (5)

Applying the checked perturbation lemma with eta=tau and (3),

max_i (K_gamma)_ii
 <= [sqrt(mu/L)+(tau/gamma)]^2
 =  [sqrt(mu/L)+sqrt(6) tau/sigma]^2
 <= 1/2                                                     (6)

by (G). Therefore `QFORM-RIDGE-DENSITY-v1` applies with q=1. Its simplified density bound is

||p_Q||_infty <= sqrt(e)/(sqrt(2)gamma) * theta/(theta-2).

Since theta/(theta-2) decreases for theta>2 and theta>=18/7,

theta/(theta-2) <= (18/7)/(4/7)=9/2.

Using gamma=sigma/sqrt(6),

||p_Q||_infty
 <= sqrt(e) * sqrt(6)/(sqrt(2)sigma) * 9/2
 = 9 sqrt(3e)/(2 sigma),

which is (1). Fourier integrability in the ridge theorem gives the continuous C_0 representative. QED.

## Optimality of the chosen gamma inside this coarse three-singular-value gate

Keep q=1 and use only the information that three singular values are at least sigma. Write x=gamma/sigma. Then theta>=3/(1+x^2), so the simplified ridge bound is at most

C(x)= [3 sqrt(e)]/[sqrt(2) sigma x(1-2x^2)],   0<x<1/sqrt(2).

The denominator x(1-2x^2) has derivative 1-6x^2 and is maximized at x=1/sqrt(6). Thus gamma=sigma/sqrt(6) is the exact optimizer of this coarse branch. The previous fixed choice was therefore not accidental.

## Explicit broadened corollary

Take tau=1/256 and assume

max_i (P_{1/256})_ii <= 1/20.

Then

L = 9/20 - 1/sqrt(10) = 0.133772233983162...,

sigma=L-1/256 = 0.129865983983162...,

and

sqrt((1/20)/L) + sqrt(6)(1/256)/sigma
 = 0.685045437939713... < 1/sqrt(2).

Therefore every such target matrix has a continuous C_0 output density with

||p_Q||_infty <= 98.9520900203 < 99.                         (7)

This strictly enlarges the leverage range of the earlier `1/64`-window, `1/32`-leverage theorem, at the cost of a narrower spectral window and a larger constant.

## Genuinely rotated indefinite full-rank family newly covered by (7)

Let H be a 64x64 Sylvester Hadamard matrix and let U be any three columns of H/8. Then U^T U=I_3 and every row of U has squared norm 3/64. Put

Lambda=diag(1,1,-1),

A = U Lambda U^T + (1/1024)(I-UU^T).

Then A is full rank, indefinite, and genuinely rotated in the original coordinates. Its spectrum is

{1,1,-1, 1/1024 (multiplicity 61)}.

For the window tau=1/256, the high spectral projector is exactly P=UU^T and

max_i P_ii = 3/64,

which is larger than 1/32, so the earlier `1/32` spectral-window theorem does not apply. The new gate does apply. Here

L = 29/64 - sqrt(6)/8 = 0.146938782152102...,

sigma = L-1/256 = 115/256 - sqrt(6)/8 = 0.143032532152102...,

and the gate left side is

0.631706163685925... < 1/sqrt(2).

Consequently, for every admissible product input law,

||p_{X^T A X}||_infty <= 89.8432709282.                       (8)

Continuity is proved for this family.

## Structural consequence for the remaining branch

If the new spectral-window gate fails because the large-eigenvalue projection itself has a heavy coordinate, there is at least a quantitative physical-row obstruction. Let P_1 project onto |lambda(A)|>=1. If (P_1)_ii>=m, then

||A e_i||_2^2 = e_i^T A^2 e_i >= e_i^T P_1 e_i >= m.

Hence either

|A_ii| >= sqrt(m/2)

or

(sum_{j!=i} A_ij^2)^(1/2) >= sqrt(m/2).

Thus failure of a diffuse spectral projection forces a genuine physical pivot or star at aggregate scale. This does not by itself close the arbitrary two-sided leakage branch, but it localizes the next unpaid implication to routing that heavy row without selecting a vanishing individual entry.

## Partner/dependency record

The designated fleet04/B04 current-QFORM canonical report/handoff was not visible in fresh direct repository lookup, so no partner result is invented. The completed ridge-window theorem above was applied at equation level after checking the two fleet03/B04-assigned steps.

## Remaining debt

Full QFORM remains OPEN. The next B04 target is the high-leverage complement: combine the heavy-row alternative with the already-paid scalar-square, rank-two half-Riesz, grouped-bank, and ridge branches in aggregate original-coordinate currency, without demanding a uniformly large individual minor.

Essential boundedness and continuity are both proved only under the gate (G), not for the unrestricted conjecture.
