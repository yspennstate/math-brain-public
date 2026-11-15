# Round 7 vetting (an agent)

## T264, 15 Nov 2026 (mini1, acc2, started 19:25:54, exit 0 at 19:39:30 mini time)

Verdict as written: PROVED finite mean risk at every fixed n in d >= 4 for homogeneous minimum-norm ReLU interpolation
on the sphere (iid uniform inputs, labels bounded by H, any measurable selection of minima, unrestricted width or any
m >= n). Combined with round 5's lower theorem (Rademacher labels), for every fixed n >= 3 and d >= 2:
E R^r < infinity iff 0 < r < (d-1)/2, and P(R > t) = Theta_{n,d}(t^{-(d-1)/2}).

Read line by line, 15 Nov. Each step checks:
- Section 1: f = sum gamma_j sigma(u_j.x) with sum |gamma_j| <= Q (AM-GM), and ||sigma(u.X)||_2^2 = 1/(2d), so
  R^{1/2} <= Q / sqrt(2d) by Minkowski.
- Lemma (9): Gaussian G in V, P(|G.v_j| < 1/(4N)) <= sqrt(2/pi)/(4N), union < 1/4; Markov P(|G|^2 > 4k) <= 1/4;
  so |z.v_j| >= 1/(8N sqrt k). Correct (also a second proof by the uniform-direction density).
- Tent identity (11): sigma(s+t) + sigma(s-t) - 2 sigma(s) = (|t| - |s|)_+, checked in both cases. With s = L z.x,
  t = x_i.x: value 1 at x_i (z perpendicular to x_i), 0 at x_j because L|z.x_j| >= s_ij/delta_i >= 1 >= |x_i.x_j|.
  Cost 2 sqrt(1+L^2) + 2L <= 2 + 4L. K = n(2 + 32(n-1) sqrt(d-1)) matches 2 + 4C with C = 8(n-1) sqrt(d-1).
- Caratheodory-style reduction to n atoms without raising the cost; existence by compactness of the sublevel set.
- delta^{-2r} <= sum over pairs; E sin(Theta)^{-2r} = B((d-1-2r)/2, 1/2) / B((d-1)/2, 1/2); at r = 1 this is
  (d-2)/(d-3) (re-derived here from the Gamma ratio: (2/(d-3)) ((d-2)/2)).
- Upper tail: R > t forces delta < sqrt(A/t); two caps of the angle, measure O(u^{d-1}). Matches round 5's lower tail
  power, so the threshold (d-1)/2 is sharp at fixed n.

No step fails. The lower half is round 5's Theorem 2 (codex_op_1114r5/briefs/T264/PROOF.md on mini1), not re-read in
this pass. What stays open: n to infinity (tempered vs catastrophic in probability), typical risk, gradient descent,
biases. The constant K grows like n^2, so nothing uniform in n follows.

Write-up candidate (rounds 5, 6, 7): "fixed-n risk of minimum-norm ReLU interpolants on the sphere has tail exponent
(d-1)/2; mean infinite in d = 2, 3, finite in d >= 4". Before writing: re-read round 5 Theorem 2 in full, and check the
literature after arXiv:2307.15396 (Joshi, Vardi, Srebro: univariate case) and arXiv:2602.00825 (Sobolev case) for a
multivariate fixed-n statement.
