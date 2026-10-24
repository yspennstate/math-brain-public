# Saved derivation checkpoint — 2026-10-11

Promising result, to be fully written and refereed:
For centered unit-variance iid entries X with finite second moment, let
A=N/sqrt(n), B=(N_R-E X1{|X|<=R} J)/sqrt(n), coupled by entrywise
truncation at R. On any fixed disk K, expected L1 difference of their
logarithmic potentials should satisfy

 E||U_A-U_B||_L1 <= C_K,D [(n P(|X|>R)+1/n) log n + n^-D].

Reason: rank(A-B)<=number of changed entries+1; singular-value rank
interlacing controls log determinant wherever all singular values are
between n^-B and n^L. Tao–Vu (0708.2895v5) Theorem 2.5 is UNIFORM in
entry laws with controlled second moment. After the phase from Lemma 2.4,
raw truncations preserve exactly the same controlled-second-moment
inequality: on the old central event they agree with X, and the new zero
atoms only add a nonnegative term. Centering is absorbed into the
deterministic shift in Theorem 2.5. Hence very small singular values have
probability n^-Q uniformly in R and bounded z.

Bad z are handled in probability x planar area by Cauchy–Schwarz,
using a deterministic L2 log-potential bound with expected square bounded
under ONLY E||A||_F^2/n<=1. Negative log contributions have full-plane
L2 norm sqrt(pi/2) per eigenvalue; positive log mean is bounded by
one half log(1+2||A||_F^2/n+2K^2). This avoids demanding fourth moments.

This would be an unconditional truncation stability theorem for smooth
linear eigenvalue statistics. It still does not give a circular-law rate
for the n-dependent bounded laws, or optimal rectangle discrepancy.
