# T352 agent_B/NOTE.md, audit 2 (agent C, 20 Oct 2026 02:31)

Objects: the reading of Chien-Wang-Chen-Li 2401.10371 Thm 3.3 (the row answered), the Doeblin-on-torus variant (i)-(iii)
and its numbers. The Chien-Li 2410.01068 floor was audited by agent A; I did not redo it.

Verdict: CONFIRMED, with one index slip in the final chi2 bound and two sharpenings of the wording. The numbers reproduce to
every printed digit by a different method.

## 2401.10371 Thm 3.3 (read 20 Oct 02:3x, arxiv.org/html/2401.10371v7)

The quotation in NOTE.md is right: projected noisy GD on the ball C_R, noise sqrt(2 eta sigma^2) W_t, every loss L-smooth and
M-Lipschitz, no convexity, initialisation C_0-LSI; eps_0 <= (2 alpha eta S^2 M^2/(sigma^2 n^2)) sum_{t<T} prod_{t'=t}^{T-1}
(1 + eta sigma^2/C_{t',1})^{-1}, with C_{t,1} <= min((1+eta L)^2 C_t + eta sigma^2, C-bar) and C-bar = 6(4(R+eta M)^2 + eta sigma^2)
exp(4(R+eta M)^2/(eta sigma^2)). v7's acknowledgments say two calculation errors in the non-strongly-convex results were fixed
in that version; quote v7 only.
Sharpening. Every factor is at most q = (1 + eta sigma^2/C-bar)^{-1}, so the sum is at most 1/(1-q) = (C-bar + eta sigma^2)/(eta sigma^2)
and the limit is at most 2 alpha S^2 M^2 (C-bar + eta sigma^2)/(sigma^4 n^2). The eta cancels: the plateau is
O(alpha M^2 C-bar/(sigma^4 n^2)), and the "T-free constant c" of the paper is about eta sigma^2/C-bar, exponentially small.
In the row's units (per-step noise variance s^2 = 2 eta sigma^2) the exponent is 8(R + eta M)^2/s^2. The 1/n^2 claim stands.

## Doeblin on the torus, (i)-(iii)

(i) Correct. Doeblin: P_S(x, .) >= m Leb = gamma Unif gives Dobrushin coefficient <= 1 - gamma on zero-mass measures. The second
term is at most sup_x ||k(. - a) - k(. - b)||_1, |a - b| <= delta = 2 eta K/n; wrapping does not increase L1, and the unwrapped
Gaussian L1 distance is 2(2 Phi(|a-b|/(2s)) - 1) <= 2 |a-b|/(s sqrt(2 pi)) = delta sqrt(2/pi)/s = beta, since 2 Phi(x) - 1 <= 2x phi(0).
Holds in d dimensions with the Euclidean norm. u_t <= beta sum_{j<t} (1-gamma)^j <= beta min(t, 1/gamma).
(ii) Correct: subtract (M+m)/2 from the kernel in the first term; |k(y-a) - k(y-b)| <= ||grad k||_inf |a-b| in the second.
(iii) Correct: f'_t >= m for t >= 1, so chi2 <= w u/m. Renyi: with X = f/f' - 1, E_{f'} X = 0, |X| <= rho, Taylor gives
E(1+X)^alpha <= 1 + alpha(alpha-1)/2 (1+rho)^{alpha-2} chi2 for alpha >= 2, and log(1+y) <= y gives the stated bound.
Index slip: the outer factor is u_T <= beta min(T, 1/gamma), not min(T-1, 1/gamma) (at T = 1 the note's form gives 0, but
u_1 can equal beta). The inner u_{T-1} <= beta min(T-1, 1/gamma) is right. The plateau and its 1/n^2 rate are unchanged.
Wording: "the exponent is milder" than 2401.10371 holds only for small d. Theirs is 8R^2/s^2 = 2D^2/s^2 with D = 2R, ours
d D^2/(8 s^2) on the torus, so ours is milder only for d < 16. The box version (atoms on faces, edges, corners; reference
measure = product of Lebesgue plus two atoms per coordinate) is plausible but stated, not proved.

## Numbers (audit_C/indep_d2.py, indep_d2.txt)

Different method: push the grid mass through phi by linear interpolation, then a circular FFT convolution with the wrapped
kernel, at N = 2048 and 8192, T = 300. n^2 D_2 = 0.00011, 0.00485, 0.00801, 0.00942, 0.00956 at n = 10, 30, 100, 1e3, 1e4: the
note's values to every digit, at both grid sizes. The limit equals 4 I with I = 2.395e-3 the Fisher information of the law in c
(4 I = 0.00958). The n = 10 value is not a bug: D_2 between the c = 1 and c = 1 - 2/n laws is not monotone in the gap (n = 30
gives a larger D_2 than n = 10). The Gibbs heuristic exp(-2 eta F/s^2) puts the Fisher information at 0.41, 170 times the true
one, at eta = 0.1: it is a heuristic for the rate in n, not for the constant.

## Not covered
The Liang et al. and Asoodeh-Diaz readings; the box version; the small-noise run (doeblin_torus_meta).
