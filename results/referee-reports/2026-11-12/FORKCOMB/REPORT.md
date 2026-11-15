# Fork comb, K(2N+4) >= N+2: independent check of section 5 of the K5 run

Verdict: SOUND. The section can go into lumping-mixing-time as written (it gives K(n) >= floor(n/2) for n >= 4).

Source: K5 run REPORT.md, section 5 ("A stronger general lower bound: a comb with two end leaves"), lines 270-394,
together with equations (1)-(2) of its section 1.

Checked by hand, line by line:
1. Row weights S_k (a-side of z_k z_{k+1}), S_N (everything except c) and W: internal edges twice, the boundary
   edge once, loops once. The tooth y_k contributes (t+1) alpha r^{k+1}, b contributes (t+1) alpha r^{N+1}. Correct.
2. Bridge crossing H(x,y) = S/w_xy: summing the hitting-time equations over the x-side cancels internal and loop
   terms and leaves w_xy H(x,y) = S. Correct. Hence H(a,z_0) = t, H(z_k,z_{k+1}) = S_k/r^{k+1}, M = H(a,c), and
   every other start skips nonnegative terms of M (each leaf costs exactly t to leave), so M = max_x H(x,c).
3. Quotient: tooth y_k attaches to z_{k+1}, so the edge between fibres k and k+1 has conductance (1+alpha) r^{k+1};
   the a-side row weight gains y_k's loop and boundary edge, Q_k = S_k + t alpha r^{k+1}. A = H(a, c-hat) and
   H(b, c-hat) = t. Correct, including N = 0 (A = t).
4. mu = E_pi H(., c) = W^{-1} sum_e S_e^2 / c_e on a tree; the t^2 terms collect to t^2 (1 + alpha G_{N+1}).
   mu-hat likewise. Correct.
5. Equation (10). Pairs with the root give a_i - mu, maximal at a. For i, j != c the common path contains the root
   edge, so K_ij >= r^{-(N+2)} and F_ij <= 2M - mu - W/r^{N+2} <= M - mu once W/r^{N+2} >= M. In the quotient the
   arms of a and b meet only at the root, so F_ab = A + t - mu-hat; cross pairs with b and pairs with the root are
   smaller; left-arm pairs share the last edge (conductance (1+alpha) r^N) and are bounded once
   W/((1+alpha) r^N) >= A - t. Diagonal entries are <= 0. Correct.
6. Limits: S_k/r^{k+1} = 1 + O(1/t), S_N/r^{N+2} = 1 + O(1/t), so M = t + N + 1 + O(1/t);
   Q_k/((1+alpha) r^{k+1}) = (1 + t^2 + O(1/t))/(1+t), so A/t -> N+1; mu <= (S_N/W) M and S_N/W ~ 1/((N+2) r^2),
   so mu, mu-hat = o(1). Ratio -> N+2. Both sufficient inequalities hold because W >= L = (N+2) r^{N+4}.

Exact check (closed_forms.py, output closed_forms_output.txt): for N = 0..3 and t = 2, 3, 10, 100 the closed forms
M - mu and A + t - mu-hat equal the mixing times computed by the independent killed-hitting solver
(check_fork_comb.py), and both sufficient inequalities hold at every point, already at t = 2. All 16 cases exact.

Minor wording: "Q_k" is the a-side row weight in the QUOTIENT at the k-th quotient edge (it includes y_k); the report
says "the prefix weight at the k-th edge is Q_k", which is right but worth one more word in a paper.
Together with the quotient bound K(n) <= max_q min(2^{n-q}, q-1) and the one-merge doubling theorem (K5P), this
gives K(5) = 2, K(6) = 3, K(8) = 4 exactly; K(7) is 3 or 4.
