# C7 v1: deterministic entry from the spherical start at q0 = 1

Author: agent H (lead), written beside worker U's T240 proofs (LEAD_C7_entry/) because worker U is out of Codex quota and holds proofs/.
Computer-assisted, exact outward interval arithmetic (iv_exact.py, 160-bit fixed point, floats refused
in every checked inequality). Kind: special. Target 1. Needs an independent reviewer.

## Statement

Let E = [4999999999/10^10, 5000000001/10^10] (the eta interval of C6) and consider the fully symmetric
slice (q, c, r) = (Q11 = Q22, Q12, R11 = R12 = R21 = R22) of the K = M = 2 erf overlap ODE, including the
eta^2 C_ij drift, exactly as evaluated by iv_scm.full_driver. For every eta in E, the solution from
(q, c, r)(0) = (1, 0, 0) exists for all t >= 0 and converges exponentially to the C6 plateau x*(eta).
Since the slice is invariant under the full seven-dimensional ODE, the spherical-start trajectory
(Q(0) = I, R(0) = 0) converges to the symmetric saddle along its stable manifold. With C4 (accepted, conditional on
this entry), C5 and C6, this discharges the deterministic-entry hypothesis of C4 for eta in E and q0 = 1.

Not included: a nondegenerate eta interval (E is 2e-10 wide); other q0; post-exit recovery.

## Method

1. Reference. A float trajectory (DOP853, rtol 1e-13) of the closed slice drift from (1, 0, 0) to T = 1600 gives
   K = 1069 rational nodes t_k, xhat_k and slopes m_k. The step is h_k = min(max(0.004/|v(t_k)|, 0.002), 2). On each
   segment xhat(t) is the cubic Hermite interpolant (exact rational coefficients). The node at t = 0 is exactly (1, 0, 0).
2. Local frame. P_k is the real eigenvector matrix of the float Jacobian at xhat_k (real block form when complex),
   rounded to dyadic rationals; P_k^{-1} is exact. With z = P_k^{-1}(x - xhat) on segment k,
       d|z|/dt <= mu_k |z| + d_k,
   where mu_k bounds lambda_max(sym(P_k^{-1} M P_k)) over every M in the interval Jacobian of an a-priori box E_k
   (Gershgorin on the interval matrix), and d_k bounds |P_k^{-1}(xhat' - f(xhat))|.
3. Defect. Each segment is cut into 6 sub-intervals. On each, delta(t) lies in delta(t_c) + [xhat'' - Df(X) xhat'] (t - t_c),
   with delta(t_c) evaluated at the exact point and Df over the sub-box X enclosed by the centred form
   Df(c) + D2f(X)(X - c). The second derivatives come from a second-order forward jet (scripts/iv_h2.py, same vector
   field code; checked against finite differences of the first-order jet to 1e-10).
4. A priori box. E_k = X_k + P_k [-R, R]^3, with X_k the range of xhat on the segment. Accept when
   (r_k + d_k h) e^{max(mu_k,0) h} < R (first-exit argument: the solution cannot leave E_k). Then
   r_{k+1} <= e^{mu_k h} r_k + d_k h e^{max(mu_k,0) h}, using the rational bounds e^x <= 1 + x + x^2/2 (x <= 0) and
   e^x <= 1/(1 - x) (0 < x < 1/2).
5. Frame switch. r <- ||P_{k+1}^{-1} P_k||_2 r, the norm bounded by s with s^2 I - M^T M proved positive definite by exact
   Sylvester minors.
6. Trap ball. With P* the eigenframe at the C6 centre xhat*, on the ball |P*^{-1}(x - xhat*)| <= rho (rho = 2e-4),
   covered by its circumscribed z-cube, the same centred Jacobian gives log norm <= mu* < 0, and
   |P*^{-1} f(xhat*)| < -mu* rho. Then the ball is forward invariant, f is a contraction on it in the z-norm, so it holds
   exactly one equilibrium (the C6 root, whose 1e-7 box lies inside) and every solution in it converges at rate |mu*|.
   The final node satisfies |P*^{-1}(xhat_K - xhat*)| + ||P*^{-1} P_K||_2 r_K < rho.

The time range is split into pieces run separately. Piece j assumes |z| <= r_in(j) at its first node and proves a
bound r_out(j) at its last; the chain is valid when r_out(j) <= r_in(j+1) at every junction (the frame at a junction
node is the same deterministic matrix in both pieces).

## Numbers (filled from run2 logs)

Run 2 (16 Oct 2026, q0 = 1, T = 1600, W = 0.004, K = 1069 segments, nsub = 6). Every number below is an exact
rational in the logs; the floats are for reading.

| piece | nodes | t range | r_in | r_out | max d_k | mu_k range | max switch norm |
|---|---|---|---|---|---|---|---|
| p1  | 0-89     | 0-2.045        | 0         | 5.126e-6 | 3.99e-6 | [0.0019, 0.0791]   | 1.5681 |
| p2  | 89-178   | 2.045-10.476   | 1e-4      | 1.0614e-4 | 2.86e-6 | [-0.0308, 0.0017] | 1.0018 |
| p3b | 178-267  | 10.476-40.053  | 1.07e-4   | 6.409e-5 | 1.00e-6 | [-0.0306, -0.0265] | 1.0019 |
| p4  | 267-356  | 40.053-175.537 | 1e-4      | 4.030e-5 | 1.09e-6 | [-0.0259, -0.0110] | 1.0027 |
| p5  | 356-700  | 175.537-863.537 | 1e-4     | 3.082e-6 | 1.21e-7 | [-0.0097, -0.0041] | 1.0007 |
| p6  | 700-1069 | 863.537-1600   | 1e-4      | 1.0574e-5 | 5.4e-10 | [-0.0036, -0.0021] | 1.00001 |

Junctions (exact): 5.126e-6 <= 1e-4, 1.0614e-4 <= 1.07e-4, 6.409e-5 <= 1e-4, 4.030e-5 <= 1e-4, 3.082e-6 <= 1e-4.
(p3 was first run with r_in 1e-4, below p2's r_out; it was rerun as p3b with r_in 107/10^6. The first p3 log is not part
of the chain.)

Trap (r_end = 1e-4 >= p6's r_out): |P*^{-1}(xhat_K - xhat*)| <= 8.862e-5, required radius 1.886e-4, rho = 2e-4 on one
cube (nsplit 1): mu* <= -1.8006e-3 (exact rational in trap.jsonl), |P*^{-1} f(xhat*, E)| <= 3.43e-12 < -mu* rho = 3.6e-7.
C6's root box (half width at most 1.1e-7 about xhat*) maps into z-radius 3.17e-7 < rho, so the unique equilibrium of the
ball is the C6 root.

logs/chain_check.txt is the exact chain check (CHAIN CLOSED). logs/audit_float.txt is an independent float sanity check:
a Radau solution (rtol 1e-12) sits at |z| <= 2.7e-6 of the certified r at every one of the 1069 nodes, and the float
midpoint defect is at most 0.0994 of the certified d_k. These floats are not part of the proof; they would expose a
sign or frame bug.

Engine note: scripts/iv_scm.py differs from worker U's scripts/iv_scm.py in one line (line 52 accepts a jet-valued eta, for a
later eta-jet experiment). entry.py always passes an interval eta, which takes the unchanged branch. iv_exact.py,
certify_plateau.py and check_symmetric_closed.py are byte-identical to worker U's. SHA256SUMS lists every file.

Review status: lead-authored, NOT independently reviewed. worker U and every Codex reviewer are out of quota until 20 Oct.
A reviewer should rerun chain_check.py on the logs, rerun at least one piece and the trap from the scripts, and read
segment() and trap() against the method above.

## Reproduce

scripts: entry.py, iv_h2.py, plus worker U's iv_exact.py, iv_scm.py, certify_plateau.py (invert_rational),
check_symmetric_closed.py (float reference only), resource_limits.py.
    cd scripts; python entry.py piece 1 1600 0.004 OUT.jsonl K0 K1 R_IN
    python entry.py trap 1 1600 0.004 OUT.jsonl R_END
    python chain_check.py <dir> p1 p2 p3b p4 p5 p6   (expects <dir>/trap.jsonl)
Runtime on this laptop: about 1.7 CPU-hours for the six pieces, 10 minutes for the trap.
