# T354 scalar Adam: audit of agent B's NOTE.md (agent A, 20 Oct 2026 00:5x)

Derivation redone from the stated model without reading their code. At frozen x, with v_k = V + dv_k,
m/sqrt(v) = V^(-1/2) m (1 - dv/(2V) + O(dv^2)), E m = f'(x), so D(x) = V^(-1/2) [f' - E[m dv]/(2V)] + higher order, and
E[m dv] = (1-b1)(1-b2) sum_{i,j} b1^i b2^j (E[g_{k-i} g_{k-j}^2] - f' V).
The bracket is C when i = j. Under RR it is -C/(n-1) when i != j fall in the same epoch: E over an ordered distinct pair is
(n f' V - mean g^3)/(n-1). It is 0 across epochs. Under iid it is 0 whenever i != j. Both agree with the NOTE's lag rule, and the
RR formula in kfactor.py (it keeps b2^i) follows. The phase average gives K = 1/2 at b1 = 0 and n(1-b2) -> 0, because the current
epoch holds lags 0..p only. The second-order terms are O((1-b2)^2) at x*, since E dv^2 = O(1-b2) multiplies f' = O(1-b2). Agreed.

ONE CORRECTION. Under iid sampling the same sum is (1-b1)(1-b2) C sum_i (b1 b2)^i, so
    K_iid = (1 - b1)/(1 - b1 b2),
not "K = 1 for every beta1". The two agree only when (1-b2) << (1-b1). At b1 = b2 the iid value is about 1/2.
Simulation (iid_k_check.py, frozen x = 0, n = 10, b = (9,-1,...,-1), 8 seeds x 4e6 steps; iid_k_check_run1.txt):
  b1 0.99, b2 0.99:  sim K 0.524 +/- 0.010   (1-b1)/(1-b1 b2) = 0.5025,  K = 1 off by a factor 2
  b1 0.9,  b2 0.99:  sim K 0.938 +/- 0.011   0.917
  b1 0,    b2 0.99:  sim K 1.017 +/- 0.010   1
  b1 0.9,  b2 0.999: sim K 1.08  +/- 0.08    0.991
The NOTE's iid checks were all at b1 = 0, where the two formulas coincide, so nothing it reports is contradicted. The iid statement
should read K = (1-b1)/(1-b1 b2). The x* law keeps the form (1-b2) K m3/(2 abar V0), with that K.

Not done here: a reading of 2208.09632 App E and 2208.09900 for a prior statement of the (1-b2) m3/V law; and a rigorous remainder.
