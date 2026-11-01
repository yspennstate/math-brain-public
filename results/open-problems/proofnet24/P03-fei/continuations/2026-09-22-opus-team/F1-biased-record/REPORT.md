# F1: biased inputs into Numaro's 18-input gate

No lower bound above 6.521845710923046575 is established here and nothing is certified as a new record.
PROVED (exact finite computations; standalone checker `code/check_local.py`): Numaro's gate g has 72 coordinate
automorphisms, transitive on the nine core and on the nine auxiliary coordinates, and 72 coordinate permutations
pi with g(pi x) = -g(-x). Consequently the composition slack with one biased input is an even function of the bias,
every first derivative of the slack vanishes at the unbiased point, and along every exactly balanced bias direction
the slack rises like eps^2 log2(1/eps^2) Lambda(v) with Lambda positive definite on the balanced subspace; g is a
strict local minimiser of the balanced composition slack under input biasing. NUMERICAL: at C = C_rec =
6.521845710923046575 the value iteration over AND, OR, NOT and g with one or two biased inputs, nested to any depth,
converges with V(1/2) = C; exactly balanced auxiliary-only biasing never goes below C; capping V at C changes nothing.
Biased g lowers the slack function away from 1/2 (by up to 0.094 at p = 0.4917) but not at 1/2. A family with all
nine core inputs at a common bias makes the grid iteration diverge at C_rec, C_rec + 1e-7 and C_rec + 1e-6 but not
at C_rec + 1e-5; on a grid four times finer near 1/2 it converges at C_rec + 1e-6, and a second-order computation of
the individual moves shows no expand/contract cycle that lowers V(1/2); the divergence is chord-interpolation error,
not a gain. FAILED: no explicit composition with H > C_rec (I - 1) was found.

## 1. Setting and validation

g is `inputs/numaro18_pm1_table.npy` (SHA-256 f8a7bb2c...9c7839; bit i of the index is coordinate i, bit value 1
means x_i = -1 = true). Input i receives a function of truth probability p_i on fresh variables; mu_i = 1 - 2p_i,
V_i = 4p_i(1 - p_i). Per coordinate, values a (x_i = +1) and b (x_i = -1) transform to c0 = (1 - p) a + p b,
c1 = sqrt(p(1 - p)) (a - b); applied on every axis this is the biased spectrum Ghat_mu(T). Htilde = sum_T
Ghat^2 log2(1/Ghat^2), It_i = sum_{T ni i} Ghat^2, Pr[F true] = (1 - Ghat_mu(empty))/2, and

    s_C(F) = sum_i (It_i/V_i)(V(p_i) + h(V_i)) - Htilde_g(p),

V(p) the least known slack C I - H at truth probability p. A balanced F with s_C(F) < C gives C_FEI > C.
Validation (`code/gate.py`, `logs/gate_validation.out`): I(g) = 261/128, H/(I - 1) = 6.521845710923047, singletons
57/256 and 1/256; at p_0 = 3/8: p_out = 967/2048, It_0 = 855/4096, sum_{i>=1} It_i = 465/256,
Htilde = 6.7442547370563144. The class-compressed evaluator (`code/compressed.py`) and the numba evaluator
(`code/fast_gate.py`) agree with the full transform to 1e-14.

## 2. Symmetry and local bias-stability of g (PROVED)

Theorem 2.1. Among coordinate permutations, g has exactly 72 automorphisms (g(sigma x) = g(x)) and exactly 72 dual
isomorphisms (g(pi x) = -g(-x)); the automorphisms act transitively on {0..8} and on {9..17}.
Every such permutation preserves influences, maps the signed graph of the pair coefficients ghat({i,j}) on the core
to itself (automorphisms) or to its negative (dual isomorphisms) and preserves the core-auxiliary matching
ghat({i,j}) = 0; the search runs over all core permutations compatible with these invariants and compares whole
truth tables (`code/symmetry.py`, `code/check_local.py`).

Corollary 2.2. If x has independent coordinates with means mu and pi is a dual isomorphism, the biased spectrum of g
at mu has the same magnitudes as at nu, nu_j = -mu_{pi^-1(j)}, and E_mu g = -E_nu g. For mu = m e_i, nu = -m e_{pi^-1(i)},
and an automorphism returns pi^-1(i) to i. Hence Htilde_g(m e_i) = Htilde_g(-m e_i), sum_{j != i} It_j is even in m,
and Pr[F] - 1/2 is odd in m; for any symmetric price V the one-input slack is even in m, so every first derivative of
s_flat(mu) = sum_i (It_i/V_i)(C + h(V_i)) - Htilde_g(mu) vanishes at mu = 0. (Measured |s(d) - s(-d)| < 5e-14.)

Proposition 2.3. Let Z = {T : ghat(T) = 0} (it contains the empty set) and a_T(v) = sum_{i not in T} v_i ghat(T u {i}).
Uniformly for |v| = 1, as eps -> 0,

    s_flat(eps v) - s_flat(0) = eps^2 log2(1/eps^2) Lambda(v) + O(eps^2),
    Lambda(v) = sum_i Inf_i v_i^2 - sum_{T in Z} a_T(v)^2.

Proof. C sum_i It_i/V_i is analytic with zero gradient at 0. sum_i (It_i/V_i) h(V_i) = eps^2 log2(1/eps^2) sum_i
Inf_i v_i^2 + O(eps^2), since h(1 - u) = u log2(1/u) + O(u). Coefficients with ghat(T) != 0 stay at distance >= 1/512
from 0 and contribute analytically. For T in Z, dGhat(T)/dmu_j = Ghat(T u j)/sigma_j (j not in T), so
Ghat_{eps v}(T) = eps a_T(v) + O(eps^2), and x^2 log2(1/x^2) at x = eps(a + O(eps)) equals eps^2 a^2 log2(1/eps^2)
+ O(eps^2) because a^2 log(1/a^2) is bounded.
Exact data: diag Lambda = 5613/32768 (core), 117/32768 (auxiliary); eigenvalues -0.228651 (the direction of the output
mean, T = empty), 0.00337, 0.003616 (x8), 0.221268 (x8). On the balanced subspace {sum_i ghat({i}) v_i = 0} Lambda is
positive definite: exact LDL^T in a rational basis has 17 positive pivots, the smallest 3.5845e-3. Lambda + c c^T
(c_i = ghat({i}); the T = empty term removed, which is repaid by h(V_out) when the output is used as an input) is
positive definite on R^18, smallest pivot 3.5817e-3 (`logs/lambda_exact.out`, `logs/check_local.out`).

Corollary 2.4. If the input price satisfies V >= C near 1/2, there is eps_0 > 0 such that every exactly balanced bias
vector mu != 0 with |mu| < eps_0 has s(mu) > s(0) = C I(g) - H(g). (A balanced mu is eps v with c.v = O(eps), so
Lambda(v) >= lambda_0 |v|^2 - O(eps); and s - s_flat = sum_i (It_i/V_i)(V(p_i) - C) >= 0.)

## 3. Read-once slack at the record constant (NUMERICAL)

`code/ro_gamma_nb.py` (the certificate grid: step 2^-11 on [1/32, 1/2], 24 nodes per octave to 2^-40) converges in 40
sweeps at C_rec. Gamma_RO(1/2) = C with slope about 31 on each side, a maximum 6.616 near p = 0.49, Gamma_RO(0.45) =
6.470, Gamma_RO(1/4) = C - 2 (`logs/ro_gamma_Crec.out`).

## 4. Value iteration with g at C = C_rec (NUMERICAL)

`code/vi_g.py`: AND/OR/NOT moves plus g-families in which the inputs in a set K are biased, the others single
variables; one input's bias is solved so that Pr[F] lands exactly on a grid node. Families: one core, one auxiliary,
and the seven pair classes (core-core +/-, core-auxiliary 0/+/-, auxiliary-auxiliary two classes).
- Convergence with V(1/2) = C (`logs/vig_all10_Crec.out`). Sanity: at C_rec - 9e-10 the same code diverges.
- Every balanced configuration costs more than C; the cheapest is g itself. At the smallest grid bias (1/256):
  core pairs +1.71e-3, core-auxiliary +2.7e-3, auxiliary with solved core +2.9e-5, auxiliary pairs +3.05e-5; best
  AND split at 1/2 +9.4e-3 (`logs/inspect_center_all10_Crec.out`, `logs/balanced_curves_Crec.out`).
- Auxiliary-only (E F = sum_j mu_j/256 exactly): k auxiliaries at +m and k at -m cost +5.1e-4 (k = 1, m = 0.1) up to
  +6.7e-2 (k = 4, m = 0.99), about k times one pair, the limit being restrictions of g; all random L-BFGS starts
  converge to the unbiased point (`logs/opt_aux_Crec.out`).
- With V capped at C at every sweep (no cusp at 1/2) V(1/2) still equals C (`logs/vi_optimistic_Crec.out`).
- g lowers V off 1/2: max(V_RO - V) = 0.0937 at p = 0.4917; V - C = +4.4e-4 at 0.4995 (slope 0.89), +2.3e-3 at 0.49,
  -9e-4 at 0.485, -8.3e-2 at 0.45; AND/OR carry the lowering to all of (0,1) (`logs/g_lowering_Crec.out`).
- All 18 biases free, one layer, inputs priced by this fixed point (`code/bell_fast.py`, exact gradient checked to
  3e-9): the defect s - V(p_out) is negative near 1/2 along "all core inputs biased the same way" (-1.62e-4 at
  p_out = 0.5039); all other local minima found are positive.

## 5. All core inputs at a common bias: a grid artifact

`code/vi_full.py` adds g with the nine core inputs at a common bias (solved per node in [0.3, 0.7]).
Standard grid: diverges at C_rec (sweep 70, V(1/2) - C = -7.4e-7), C_rec + 1e-7 and C_rec + 1e-6; converges at
C_rec + 1e-5 and + 1e-4. Grid four times finer on [0.44, 0.56] (`code/vi_full_fine.py`): converges at C_rec + 1e-6
(max change 3.2e-7 at sweep 20, where the standard grid diverges); at C_rec the cascade is 20 to 56 times slower than
on the standard grid; at C_rec + 3e-7 a slow creep (2.9e-5 per sweep at sweep 30, V(1/2) = C when stopped). The
threshold falls with the node spacing like an O(h^2) chord-interpolation error in the concave part of V near 1/2,
accumulated by slope-neutral expand/contract cycles at zero margin.
Local second-order computation (`code/delta_moves.py`, `logs/delta_moves.out`). With W = V + h(V), each move satisfies
W_out - C = sum_i (It_i/V_i)(W_i - C) + Delta(eps). Measured: all core inputs at eps: Delta = -(0.0446 log2(1/eps^2)
+ 3.76) eps^2; one core input +0.95 eps^2; one auxiliary +0.02 eps^2; exactly balanced core pair +2.30 eps^2;
auxiliary pair (F, NOT F) +0.045 eps^2. The uniform-core move multiplies the distance from 1/2 by 2.004 and lowers
(W - C)/t by about 9t per step; the one-core move contracts by 57/256 and raises it by about 17t; a cycle returning to
its scale (A A B) raises it by about 41 t. The best idealised balanced step after a long uniform-core chain from a flat
seed still costs +5.2 t^2 (core pair) and +0.11 t^2 (auxiliary pair).

## 6. Exact balance patterns

Auxiliary inputs only: E F = (sum_j mu_j)/256 exactly (every ghat on two or more auxiliaries vanishes), so
(F on auxiliary j, NOT F on auxiliary k) is balanced for every F. Core 0 with auxiliary 9: ghat({0,9}) = 0 and
E F = (57 mu_0 + mu_9)/256 exactly. For a dual isomorphism pi, every bias vector with mu_{pi(k)} = -mu_k for all k
is exactly balanced (E_mu g = -E_mu g).

## 7. Files

code/: gate.py, fast_gate.py, compressed.py (evaluators); ro_gamma.py, ro_gamma_nb.py (read-once slack); vi_g.py,
vi_full.py, vi_full_fine.py, grid_fine.py, vi_optimistic.py, vi_full_pess.py (value iterations); opt18.py,
bell_fast.py, bell_multi.py, opt_aux.py (18-input searches); first_order.py, symmetry.py, lambda_form.py,
lambda_exact.py, check_local.py (local theory, exact checker); delta_moves.py, chord_gap.py, trace_policy.py,
chain_core.py, explicit.py, explicit_dp.py, scan1.py, inspect_center.py (diagnostics).
logs/: SUMMARY.json and the outputs named above.

A lesson about the method, worth keeping for any value iteration at zero margin: slope-neutral expand/contract cycles
can make a grid iteration diverge from interpolation error that scales like h^2; rerun on a finer grid before
believing a divergence.
