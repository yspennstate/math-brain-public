---
name: t264_minnorm_relu_sphere_risk_tail_exponent_d_minus_1_over_2_2026_11_15
description: "Min-norm ReLU interpolant on the sphere, mean risk finite? Fixed n: P(R>t) ~ t^{-(d-1)/2}, E R infinite in d=2,3, finite d>=4 (T264 rounds 5+7, proofs read)"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T18:44:10+02:00
  status: verified
  evidence: "06_math_research/codex_op_1114/round7/VETTED_ROUND7.md (line-by-line read of round5 and round7 PROOF.md, 15 Nov)"
---

Fixed-n risk of minimum-norm two-layer ReLU interpolants (no biases) on S^(d-1), iid uniform inputs, Rademacher labels,
zero regression function: P(R_n > t) = Theta_{n,d}(t^{-(d-1)/2}) for every fixed n >= 3, so E R_n^r < infinity iff
r < (d-1)/2. Mean risk infinite in d = 2, 3, finite in d >= 4.

- Lower half (Codex round 5, T264): a close opposite-label pair at angle theta with the other n-2 points in one
  hemisphere of the pair's difference direction (probability 2^(3-n)) forces theta f -> -2 sigma(-e2.x), so
  R ~ (2/d) theta^{-2}. Localization by sum theta|gamma_j| ||u_j - t_j e2||^2 <= 4(M - theta/b).
- Upper half (Codex round 7, 15 Nov, mini1 acc2, 14 min): three-ReLU tent sigma(s+t)+sigma(s-t)-2sigma(s) =
  (|t|-|s|)_+ with s = L z.x, t = x_i.x, z perpendicular to x_i chosen by a Gaussian union bound so |z.x_j| >=
  s_ij / (8(n-1) sqrt(d-1)); cost <= H K_{n,d} / delta, delta = min projective sine; R <= Q^2/(2d) by Minkowski.
  E sin^{-2} of a spherical pair = (d-2)/(d-3).
- Read line by line by an agent 15 Nov (round7/VETTED_ROUND7.md); both halves check. Round 6: antipodal extra
  points cancel the blow-up (finite collision-limit risk), so the hemisphere geometry matters.
- Open: n -> infinity (tempered vs catastrophic in probability), GD selection, biases. Constants: lower 2^(2-n),
  upper ~ n^4 d, so nothing uniform in n.
- Files: brain-repo/06_math_research/codex_op_1114/round5, round6, round7 /T264. Write-up candidate.
How to apply: for a min-norm interpolation "catastrophic vs tempered" question, separate in-expectation (driven by rare
close opposite-label pairs, exponent (d-1)/2) from in-probability; the expectation answer is now settled at fixed n.

