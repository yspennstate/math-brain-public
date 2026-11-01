# C8: deterministic entry over an eta cell, eta in [0.4998, 0.5002], q0 = 1

Author: agent H (lead). Computer-assisted, exact outward interval arithmetic (worker U's iv_exact.py, 160-bit
fixed point; floats only build the reference and the frames, never decide an inequality). Kind: special. Target 1.
Extends C7 (eta interval of width 2e-10) to a cell of width 4e-4. Needs an independent reviewer.

## Statement

Let E8 = [2499/5000, 2501/5000]. For every eta in E8, the solution of the symmetric slice (q, c, r) of the K = M = 2
erf overlap ODE (with the eta^2 C_ij drift, as evaluated by iv_scm.full_driver) from (1, 0, 0) exists for all t >= 0
and converges exponentially to an equilibrium x*(eta). For each eta, x*(eta) is the unique zero of the slice drift in a
certified box that passes every C6 plateau test (Krawczyk existence and uniqueness, contraction, physical
(q - c > 0, q + c - 4r^2 > 0), Hurwitz in the slice, the antisymmetric two-dimensional block stable, the teacher-odd
pair with common < 0 and lambda > 0). So for every eta in E8 the spherical start enters the symmetric saddle along its
stable manifold, and C4's deterministic-entry hypothesis holds on E8 at q0 = 1.

Not included: other q0; eta outside E8; post-exit recovery.

## What changes from C7

1. Reference affine in eta. xhat(t) + (eta - eta0) yhat(t), eta0 = 1/2, where yhat approximates d x / d eta: central
   differences (eps = 1e-5) of two DOP853 runs at eta0 +- eps, sampled at C7's 1069 nodes, with slopes
   f_x yhat + f_eta (float). Both xhat and yhat are cubic Hermite with exact rational data; yhat(0) = 0 exactly, so the
   error starts at 0 for every eta in the cell.
2. Defect over (t, eta). delta(t, eta) = d/dt[xhat + (eta - eta0) yhat] - f(xhat + (eta - eta0) yhat, eta). On each of
   six sub-intervals of a segment, by the mean value theorem in both variables,
       delta in delta(t_c, eta0) + d_t delta(B) [-w h, w h] + d_eta delta(B) [-WE, WE],
   and d_eta delta = g = yhat' - f_x yhat - f_eta is enclosed the same way about (t_c, eta0), with
       d_t g = yhat'' - f_xx(x_t, yhat) - f_x yhat' - f_x,eta x_t,   d_eta g = -f_xx(yhat, yhat) - 2 f_x,eta yhat - f_eta,eta,
   all second derivatives from second-order jets in the four variables (q, c, r, eta) over the box (iv_h2.py).
3. Jacobians range over the whole cell. The log-norm bound mu_k is taken over the a priori box and over eta in E8.
4. Trap ball about a moving centre. c(eta) = xs0 + (eta - eta0) ys, xs0 the float plateau at eta0 and ys = -J^{-1} f_eta.
   With P* the eigenframe at xs0 and z = P*^{-1}(x - c(eta)), d|z|/dt <= mu*|z| + res on the ball, where
   res >= |P*^{-1} f(c(eta), eta)| for all eta in E8 (mean value along the line c), and mu* < 0 bounds the log norm over
   the ball and the cell. res < -mu* rho makes the ball invariant, the field a contraction on it, so it holds exactly one
   equilibrium per eta and every solution in it converges at rate |mu*|.
5. Linking to the plateau. Sixty-four eta cells of width 1/160000 tile E8; on each, the certified plateau box lies inside
   the trap ball for every eta of that cell. The trap's unique equilibrium is therefore the certified plateau root.

The chain, the trap and the frame switches are otherwise exactly C7's (pieces with r_out(j) <= r_in(j+1); rational
exponential bounds; Sylvester-minor operator norms).

## Numbers

Chain (K = 1069 nodes, t in [0, 1600], step 2 late; pieces run in parallel, each certified on its own):

| piece | nodes | r_in | r_out | max mu |
|---|---|---|---|---|
| q1 | 0-89 | 0 | 1.118e-5 | 0.0795 |
| q2 | 89-178 | 1e-4 | 1.114e-4 | 0.0026 |
| q3 | 178-267 | 2e-4 | 1.238e-4 | -0.0242 |
| q4 | 267-356 | 2e-4 | 8.575e-5 | -0.0083 |
| q5 | 356-700 | 2e-4 | 5.401e-5 | -0.0012 |
| q6b | 700-1020 | 6e-5 | 2.868e-5 (partial) | -0.0011 |
| q6c | 1020-1045 | 2.868e-5 | 2.677e-5 | -0.0014 |
| q6d | 1045-1069 | 3e-5 | 2.818e-5 | -0.0014 |

Every junction satisfies r_out(j) <= r_in(j+1) exactly (rationals). q6b was cut by a machine restart after its segment
1019; its completed rows are each certified, so it ends at node 1020. The rows keep r as a correctly rounded float, so
r_exact <= float(r)(1 + 2^-52); the check uses a factor 1 + 1e-12 against q6c's r_in 717/25000000 (relative gap 1e-4).

Trap: r_end = 1e-4 >= last r_out 2.818e-5. Ball rho = 2e-4 in the plateau eigenframe about c(eta), two-way split,
mu* <= -7.534e-4, residual about 8e-8, so res < -mu* rho with need_rho 1.89e-4 < 2e-4.

Plateau: 64 cells of width 1/160000 tile [2499/5000, 2501/5000] contiguously. In every cell the C6 tests pass:
lambda lower bound >= 0.0315, physical margin >= 0.0059, root box half-width <= 5.78e-5. Largest z-radius of a certified
box about c(eta): 1.670e-4 < rho = 2e-4, so the trap's unique equilibrium is the certified plateau root on every cell.

chain_check_eta.py prints CHAIN CLOSED (logs/chain_check.txt).

Float sanity (not part of the proof; Radau, rtol 1e-12, in the certified frames): the worst |z_true| / r_certified is
2.15e-2 at eta = 0.4998 and 0.5002 (node 1) and 2.2e-7 at eta = 1/2 (logs/audit_float.txt). The certified bound is loose
by about a factor of 50 at the cell's ends and never exceeded.

## Reproduce

scripts (in scripts/): entry_eta.py, entry.py, iv_h2.py, iv_exact.py, iv_scm.py (jet-eta variant, as in C7),
certify_plateau.py, check_symmetric_closed.py, widen_eta.py, chain_check_eta.py, audit_float_eta.py, resource_limits.py,
unthrottle.py.
    python entry_eta.py piece 1/2 1/5000 1600 0.004 OUT.jsonl K0 K1 R_IN
    python entry_eta.py trap 1/2 1/5000 1600 0.004 OUT.jsonl R_END
    python -c "import widen_eta; widen_eta.run('2499/5000', '2501/5000', '1/160000', 'cells.jsonl')"
    python chain_check_eta.py logs logs/trap.jsonl logs/plateau_cells.jsonl q1 q2 q3 q4 q5 q6b q6c q6d
    python audit_float_eta.py logs q1 q2 q3 q4 q5 q6b q6c q6d
