# T249 crossover: a depth-uniform formula with an error term

Status (11 Nov 2026, an agent): the Theorem has been read line by line by two independent readers with no gap found (an agent, 02:37Z, note at 06_math_research/lean_checks_agent/t249_referee/README.md, brain main f92fbef7; and a Codex referee, gpt-6.1-sol high on Mac mini 1, 07:22-07:4x Mac time, session 01a1c8a1-4b13-7b22-aa77-2f84c9e040d9, AUDIT2_CODEX_REPORT.md and AUDIT2_CODEX_LOG.md). The second reader found the Corollary false as first written (at L = 1 with n = 2, c_1 = 0) and Remark 2 overstated; both are restated below. The restated Corollary and Remark 2 were then read by an agent (04:32Z, 06_math_research/lean_checks_agent/t249_corollary/README.md, brain main 419fdae0): both correct, so each has one independent reader. Its own numerics (tanh and sin, eps from 0.1 to 0.0001, depth to 20/eps): the scaled error max_L |D_L/F_L - 1| N_L/(1 + log N_L) stays below 7.52.
Numerical check: `uniform_check.py`, `uniform_tanh.out`; the order condition of the Corollary: `corollary_order_check.py`, `.out`. Not submitted anywhere.

## Setting

Fully connected network, infinite width, NTK parametrisation, activation phi, weight variance sw2, bias variance
sb2 > 0. Inputs lie on the sphere on which the first-layer variance equals the fixed point q* of
q -> sw2 E[phi(sqrt(q) z)^2] + sb2. For two inputs let c_l be the correlation of their layer-l pre-activations,
delta_l = 1 - c_l. Then c_{l+1} = f(c_l) with

    f(c) = ( sw2 E[phi(u1) phi(u2)] + sb2 ) / q*,   (u1,u2) centred Gaussian, variances q*, correlation c.

Write chi = f'(1) = sw2 E[phi'(sqrt(q*) z)^2] = 1 - eps, beta = f''(1) = sw2 q* E[phi''(sqrt(q*) z)^2],
6M >= f'''(1) = sw2 q*^2 E[phi'''(sqrt(q*) z)^2].

NTK recursion (Theta_1 = Sigma_1):  Theta_{l+1}(x,x') = q* c_{l+1}(x,x') + f'(c_l(x,x')) Theta_l(x,x').
Diagonal: T_l := Theta_l(x,x) = q* (1 - chi^l)/eps.  For a pair, D_l := T_l - Theta_l(x,x'), and

    D_1 = q* delta_1,    D_{l+1} = f'(c_l) D_l + q* delta_{l+1} + (chi - f'(c_l)) T_l.            (1)

Hypotheses (H). phi is C^3 with polynomially bounded derivatives and is not affine. The parameters (sw2, sb2) range
over a family with eps in (0, eps_0] on which q*, beta, 1/beta, 1/q*, M are bounded, and a_0 >= a_- > 0,
1 - a_0 >= gamma > 0, where a_0 = f(0) = (sw2 (E phi)^2 + sb2)/q*. (Example: with sb2 > 0 fixed and sw2 in a compact
interval ending at a critical value sw2_c at which the fixed point q* is finite, positive and stable, and beta > 0
there, these hold by continuity. Compactness of the parameter set alone does not give such a critical point.)

Facts used. f(c) = sum_k a_k c^k on [-1,1] with a_k >= 0, sum a_k = 1 (Hermite expansion). Hence on [0,1]:
f, f', f'', f''' are nonnegative and nondecreasing, and 0 <= f''' <= 6M.

## Statement

Put N_L = min(L, 1/eps), S_L = sum_{j=1..L} (1 - chi^j)^2 = L - 2 chi (1 - chi^L)/eps + chi^2 (1 - chi^{2L})/(1 - chi^2), and

    F_L = 2 q* chi^L S_L / (1 - chi^L)^2.

Theorem. Assume (H) and fix eta > 0. There are C and eps_0 > 0, depending only on eta and the bounds in (H), such
that for every eps in (0, eps_0], every pair with delta_1 in [eta, 2 - eta] and every L >= 1,

    | D_L / F_L - 1 |  <=  C (1 + log N_L) / N_L.

So the error is O(log L / L) up to depth 1/eps and O(eps log(1/eps)) at every larger depth.

Three regimes of F_L.
- L eps -> 0:  F_L = (2/3) q* L (1 + O(L eps) + O(1/L))   (critical line).
- L = t/eps:   (eps/q*) F_L -> g(t) = e^{-t} (2t - 3 + 4 e^{-t} - e^{-2t}) / (1 - e^{-t})^2.
- L eps -> infinity:  F_L = 2 q* L chi^L (1 + O(1/(L eps)))   (ordered phase).

Corollary (spectrum). Let n >= 2 inputs have pairwise delta_1 in [eta, 2 - eta], and put r_L = (1 + log N_L)/N_L.
Then Theta_L = B + E with B = F_L I + (T_L - F_L) 1 1^T, E symmetric, E_aa = 0 and |E_ab| <= C F_L r_L, so
||E|| <= (n - 1) C F_L r_L (maximum row sum). B has the eigenvalue F_L with multiplicity n - 1 and the eigenvalue
lambda_par = n T_L - (n - 1) F_L on the vector 1. By Weyl's inequality the sorted eigenvalues of Theta_L and of B
differ by at most (n - 1) C F_L r_L, at every depth.

Suppose in addition T_L >= F_L and a := (n - 1) C r_L <= 1/2. Then lambda_par >= F_L is the top eigenvalue of B, the
n - 1 smallest eigenvalues of Theta_L lie in F_L [1 - a, 1 + a], the largest lies within a F_L of lambda_par, and

    cond(Theta_L) = [ n (1 - chi^L)^3 / (2 eps chi^L S_L) - (n - 1) ] (1 + theta),   |theta| <= 4a.

(The bracket is lambda_par / F_L >= 1, so the ratio of (lambda_par + a' F_L)/(F_L (1 + a'')) to it lies between
(1 - a)/(1 + a) and (1 + a)/(1 - a).)

The condition T_L >= F_L fails at small depth: T_L/F_L = (1 - chi^L)^3/(2 eps chi^L S_L) tends to
3L^2/((L+1)(2L+1)) as eps -> 0, which is 1/2, 4/5, 27/28 for L = 1, 2, 3 and 16/15 for L = 4. At L = 1 with n = 2 and
c_1 = 0 the matrix is q* I while B has eigenvalues 2 chi q* and (2 - 2 chi) q*. For L >= 4 the ratio is at least
16/15 on the grid of `corollary_order_check.py` (eps from 1e-6 to 0.99, L up to 60/eps). That T_L >= F_L holds for
every L >= 4 and every chi in (0, 1) is proved in the note of an agent cited in the status line: with
x = chi, [j] = 1 + x + ... + x^(j-1) and h_L the numerator of T_L - F_L, h_(L+1) = x h_L + G(x, [L]) with
G = (1 - 2x) + (5x - 6x^2) y + (7x^2 - 6x^3) y^2 - x (1-x)^2 (1 + 2x) y^3, and G >= 0 for y in [[4], 1/(1-x)]
(certified by Sturm sequences and by Bernstein coefficients), base case h_4 >= 0. Not reproduced here. The condition a <= 1/2 needs N_L large against n, so the corollary says nothing for
n of order N_L / log N_L or more.

In the limit eps -> 0 with L = t/eps, t > 0 and n, eta fixed, cond(Theta_L) ->
n (1 - e^{-t})^3 / (e^{-t}(2t - 3 + 4e^{-t} - e^{-2t})) - (n - 1), and this limit function tends to (n+2)/2 as t -> 0.

## Proof

Constants C, C_1, ... depend only on the bounds in (H) unless eta is named. Let
delta_* = min( beta/(16M), 1/(4 beta), 1/2 ) and assume eps_0 <= 1/2, so chi >= 1/2.

Step 0: a bounded transient.
(a) For c < 0: even powers contribute at least a_0 and c^k >= c for odd k, so f(c) >= a_0 + (1 - a_0) c, i.e.
1 - f(c) <= (1 - a_0)(1 - c). Hence after at most l_a = 1 + log 2 / a_- steps c_l >= 0.
(b) [0,1) is invariant and f(c) >= c there (f convex, f(1) = 1, f'(1) < 1).
(c) For c = 1 - delta in [0,1), Taylor at 1 with f''' in [0, 6M]:

    delta_{l+1} = chi delta_l - (beta/2) delta_l^2 + r_l,   0 <= r_l <= M delta_l^3,                 (2)

so f(c) - c >= (beta/2) delta^2 - M delta^3 >= (beta/4) delta^2 for delta <= delta_*. Since f(c) - c is
nonincreasing on [0,1] (its derivative is f' - 1 <= chi - 1 < 0), f(c) - c >= m := (beta/4) delta_*^2 on
[0, 1 - delta_*]. So at most 1/m further steps bring delta_l <= delta_*, and delta_l is nonincreasing afterwards.
(d) |f(c)| <= f(|c|) <= 1 - (1 - a_0)(1 - |c|), so min(delta_l, 2 - delta_l) >= gamma^{l-1} eta.
Conclusion: with l_1 = l_a + 1/m + 2 (independent of eps and eta), c_l in [0,1) and delta_l <= delta_* for
l >= l_1, and v_{l_1} := 1/delta_{l_1} <= gamma^{-l_1} / eta.

Step 1: the correlation gap. For l >= l_1 put v_l = 1/delta_l. From (2),
v_{l+1} = (v_l/chi) / (1 - x_l) with x_l = beta delta_l/(2 chi) - r_l/(chi delta_l). The choice of delta_*
gives beta delta_l/(4 chi) <= x_l <= 1/2. Expanding 1/(1-x) = 1 + x + x^2/(1-x),

    v_{l+1} = v_l/chi + beta/(2 chi^2) + rho_l,   |rho_l| <= C_1 delta_l,   rho_l >= -4M delta_l >= -beta/4.   (3)

Since beta/(2 chi^2) >= beta/2, (3) gives v_{l+1} >= v_l + beta/4, hence delta_j <= (4/beta)/(j - l_1) for j > l_1.
Solving (3) with a = 1/chi and V_l := (beta/(2 chi eps)) (chi^{-l} - 1):

    v_l - V_l = a^{l-l_1} ( v_{l_1} - V_{l_1} ) + sum_{j=l_1}^{l-1} a^{l-1-j} rho_j.

The first term is at most a^l C/eta in absolute value. The sum is at most
a^l C_1 ( delta_* + (4/beta) sum_{i>=1, i<l} chi^i / i ) <= C a^l Lambda_l with Lambda_l := 1 + log N_l
(use sum_{i>=1} chi^i/i = log(1/eps)). Also (1 - chi^l)/eps = sum_{j<l} chi^j >= N_l/4. Therefore

Lemma A. For l >= l_1:  delta_l = (2 chi eps / beta) chi^l / ((1 - chi^l)(1 + theta_l)),
|theta_l| <= E_l := C_5 (1/eta + Lambda_l)/N_l.

Choose l_2 >= l_1 (depending on eta) and eps_0 so that C' E_l <= 1/2 for all l >= l_2 and the constants C' that
appear below; then also delta_l <= C chi^l / N_l for l >= l_2. Note E_l is nonincreasing in l, 1/N_l <= E_l, and

    sum_{i>j} chi^i E_i / N_i <= C E_j        (split at i = 1/eps).                                   (4)

Step 2: the source term. For l >= l_1, Taylor gives f'(c_l) = chi - beta delta_l + s_l with 0 <= s_l <= 3M delta_l^2.
In (1), (chi - f'(c_l)) T_l = (beta delta_l - s_l) q* (1 - chi^l)/eps, and by Lemma A
beta delta_l q* (1 - chi^l)/eps = 2 q* chi^{l+1}/(1 + theta_l). The remaining pieces, q* delta_{l+1} and s_l T_l,
are at most C chi^l / N_l for l >= l_2. Hence (1) reads

    D_{l+1} = A_l D_l + G_l,   A_l = chi - beta delta_l + s_l,   G_l = 2 q* chi^{l+1} (1 + e_l),  |e_l| <= C E_l.   (5)

Step 3: the product of the A_i. Put y_i = 2 eps chi^i/(1 - chi^i), so beta delta_i/chi = y_i/(1 + theta_i) and
y_i <= 8 chi^i/N_i. For i >= l_2,

    log A_i = log chi - y_i + O( chi^i E_i / N_i ).

With h = -log chi and psi(s) = 2 e^{-s}/(1 - e^{-s}) (decreasing, with integral 2 log(1 - e^{-s})), y_i = (eps/h) h psi(ih),
and comparing the sum with the integral,

    sum_{i=j+1}^{L-1} y_i = 2 log( (1 - chi^L)/(1 - chi^{j+1}) ) + O(1/N_j).

Together with (4): for l_2 <= j < L,

    P_{j,L} := prod_{i=j+1}^{L-1} A_i = chi^{L-1-j} ( (1 - chi^{j+1})/(1 - chi^L) )^2 (1 + p_j),  |p_j| <= C E_j.      (6)

Step 4: summation. From (5), D_L = P_{l_2 - 1, L} D_{l_2} + sum_{j=l_2}^{L-1} P_{j,L} G_j. By (5) and (6),

    sum_{j=l_2}^{L-1} P_{j,L} G_j = ( 2 q* chi^L / (1 - chi^L)^2 ) sum_{j=l_2}^{L-1} (1 - chi^{j+1})^2 (1 + O(E_j)).

Since eps N_j / 4 <= 1 - chi^j <= eps N_j, S_L >= c eps^2 N_L^2 L, while
sum_{j<=L} (1 - chi^j)^2 E_j <= C eps^2 (1/eta + Lambda_L) N_L L. So the O(E_j) terms change the sum by a relative
O(E_L). The omitted terms j < l_2 are at most eps^2 l_2^3, a relative O(l_2/N_L). Finally 0 <= D_{l_2} <= 2 T_{l_2}
<= 2 q* l_2 (the 2x2 kernel is positive semidefinite) and P_{l_2-1,L} <= C chi^L (eps l_2)^2/(1 - chi^L)^2, again a
relative O(l_2/N_L). For L < l_2 the claim holds by enlarging C. This proves the theorem.

The limits of F_L follow from the closed form of S_L: with L = t/eps, eps S_L -> t - 2(1 - e^{-t}) + (1 - e^{-2t})/2.

## Remarks

1. Dependence on eta. The proof gives C(eta) through l_2. Lemma A shows where it enters: the term
a^{l-l_1} v_{l_1} is a relative eps/(beta delta_1)-size correction at depth 1/eps. The limit is therefore not uniform
over pairs with delta_1 of order eps/beta or smaller.
2. Where the logarithm comes from: rho_l = (beta^2/(4 chi^3) - f'''(1)/(6 chi^2)) delta_l + o(delta_l) under (H)
(the remainder is O(delta_l^2) if phi has a fourth derivative with a bounded Gaussian moment). The coefficient
vanishes exactly when beta^2/4 = chi f'''(1)/6. When it does not vanish in the limit eps -> 0 the sum of rho_l over
depth is of order log N_L; that the logarithm survives in D_L/F_L itself is not proved here.
3. The posted ordered-phase law (fixed eps, L -> infinity) has the form kappa k(delta_1) L chi^L. The theorem says
kappa k(delta_1) = 2 q* (1 + O(eps log(1/eps))) for fixed delta_1, which is the second derivation in T249_CROSSOVER.md.
4. Other conventions for the first layer change T_l and D_1 by bounded amounts and do not affect the statement.

## Numerical check (tanh, sb2 = 0.05)

`uniform_check.py` iterates (1) exactly (Gauss-Hermite, 100 nodes) and prints D_L/F_L - 1 for c_1 in {-0.5, 0, 0.5, 0.9}.
See `uniform_tanh.out`. At depth 1/eps (t = 1):

    eps      c1=-0.5   c1=0     c1=0.5    c1=0.9
    0.01     +0.078    +0.040   -0.040    -0.374
    0.0025   +0.031    +0.021   -0.001    -0.121

and the error is flat in L from t = 3 to t = 20 (for example +0.0196, +0.0219, +0.0235 at c1 = 0, eps = 0.0025),
as the theorem states. The c1 = 0.9 column shows the 1/delta_1 term of Remark 1.

Third value, `uniform_tanh_b.out` (eps = 0.000625), at t = 1: +0.0107, +0.0082, +0.0027, -0.0302.
The form a eps log(1/eps) + b eps fitted to the first two values of the c1 = 0 column (a = 3.11, b = -10.35)
predicts +0.0079 at eps = 0.000625; measured +0.0082. This is consistent with the logarithm of Remark 2 (a two-parameter fit to two points and one prediction, not a proof).
The c1 = 0.9 column falls 0.374, 0.121, 0.030, a factor of 3.1 then 4.0 per factor 4 in eps.

One row is excluded: eps = 0.000625, L = 32000 (t = 20), where all four columns shift by the same +0.013.
There delta_L is about 2e-12 while the rounding residual of the computed map at c = 1, about 1e-15, has a fixed point
of size 1e-15/eps = 1.6e-12 under delta -> chi delta + residual. A shift that is the same for every c1 is what an
additive floor in delta would produce; this explanation has not been tested with higher precision.

Open before this is claimed: an independent audit of Steps 1-4; a second activation (erf, sin); a higher-precision
rerun of the excluded row; reading Roberts-Yaida-Hanin 2106.10165 and Terjek 2501.13225 for the same formula.

Second and third activation (`uniform_sin.out`, `uniform_erf.out`, same sb2 = 0.05, eps = 0.01 and 0.0025), D_L/F_L - 1 at t = 1:

    act   eps      c1=-0.5   c1=0     c1=0.5    c1=0.9
    sin   0.01     +0.063    +0.026   -0.055    -0.406
    sin   0.0025   +0.021    +0.011   -0.010    -0.140
    erf   0.01     +0.070    +0.035   -0.038    -0.355
    erf   0.0025   +0.027    +0.018   -0.002    -0.113

Same pattern as tanh, and again flat in L from t = 3 to t = 20. (The "second activation" item above is done.)
