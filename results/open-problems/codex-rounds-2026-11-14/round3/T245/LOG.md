# T245 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Receipt: 15 November 2026, 03:34 Asia/Tbilisi (23:34 UTC on 14 November).

## Orientation and scope

Read the earlier REPORT.md, PROOF.md, LOG.md, verify.py and literature file in `~/codex_op_1114/briefs/T245`; that directory is read-only for this task. Read the startup memory index, recall results, compute state, and mesh protocol. The current task's explicit folder-only rule overrides shared checklist, mesh, memory and git mutations. No subagents, git, outside-folder edits, or external messages. One initial brain recall was attempted as instructed by the global startup ritual; it completed, but no further brain commands will be run because recall can have logging side effects. A guessed startup.md path did not exist; the actual MEMORY.md index was read.

Compute state: status warn, mode owner_away_open, CPU saturated, memory 64% free. Only small standard-library calculations will be run, one thread, OMP_NUM_THREADS=1, nice -n 15, below 1 GB and 20 minutes. The inherited priority is expected to be 20; the previous worker documented the macOS nice warning at that priority. The scripts will check priority and resource use directly.

## Bounded literature check — 03:34–03:38 Asia/Tbilisi

Used the web search tool for joint depth/width NTK training limits, 2025–2026 work, and deep-linear dynamics. Opened the following primary pages:

- Boris Hanin, Mihai Nica, *Finite Depth and Width Corrections to the Neural Tangent Kernel*, https://arxiv.org/abs/1909.05989.
- Jiaoyang Huang, Horng-Tzer Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, https://arxiv.org/abs/1909.08156.
- Zhengmian Hu, Heng Huang, *On the Random Conjugate Kernel and Neural Tangent Kernel*, https://proceedings.mlr.press/v139/hu21b.html.
- Qiyang Han, Masaaki Imaizumi, *Precise gradient descent training dynamics for finite-width multi-layer neural networks*, https://arxiv.org/abs/2505.04898. Its proportional regime keeps width and depth bounded, so it does not answer this question.
- Zihan Yao, Ruoyu Wu, Tianxiang Gao, *Feature Learning Dynamics in Infinite-Depth Neural Networks*, https://arxiv.org/abs/2512.21075 (v3, May 2026). Residual architecture and depth scaling, as already distinguished in the earlier report.
- Andrea Combette, Nelly Pustelnik, Antoine Venaille, *Correlation flow governs learning at criticality*, https://arxiv.org/abs/2608.08350. The earlier report distinguished its sequential limit; no new joint training theorem was located.

No whole-problem solution found in the bounded check. This is not a proof of absence. No SOLVED_ELSEWHERE.md is created, since the stop condition was not met. No literature novelty claim will be made for deep-linear factorization dynamics.

## Earlier main claim re-derived, before extension

Starting from the Euclidean derivative in Theta coordinates, each layer contributes
`(1/n) ||W_{l+1:L}^T e1||^2 <W_{1:l-1}x,W_{1:l-1}x'>`.
On the earlier diagonal orbit this gives exactly
`A_n=P^2 sum(a_l^-2)/n`,
`B_n=sum(prod_{j>l}a_j^2 prod_{j<l}s_j^2)/n`.
The update is `a_l^+=a_l-eta r P/(n a_l)` and `b^+=b-eta r`.
Writing `a_l=s_l+(c+o(1))/n`, uniformly in l, gives
`log(P/S) -> t c` and the suffix log ratio `c(t-l/n)`.
Consequently `A -> t P^2` and `B -> S^2 integral_0^t exp(2cu)du`.
This independently reproduces the earlier main law, including the contribution of off-diagonal parameter derivatives. The normal log-product law is exact at every n. No error found in that claim. Numerical verification independent of the earlier script will also be included in this folder.

## Chosen extension, recorded before calculation

Prove a closed depth-profile recursion for a fixed-dimensional invariant block, in particular a 2 by 2 block, trained on several noncollinear examples. Keep the earlier fully trainable linear network, scalar-identity random initialization, fixed readout and output bias. This tests the next step named in the earlier report: noncommuting matrix dynamics within a two-dimensional block. It avoids claiming stability for arbitrary perturbations or iid Gaussian matrices.

Normalize depth to z in [0,1], and write the active block as `A_l=s_l(I+C_l/n)`. Scalar gain products cancel from each layer gradient, leaving only the total product S in the limit. Anticipated closure: a continuous matrix function C_k(z), forward product U_k solving `U'=t C_k U`, suffix V_k=U_k(1)U_k(z)^-1, and a pointwise training update. This is a closed function-valued description, not a finite-dimensional matrix recursion. The full NTK, including test inputs outside the block, will be derived. A first-time derivative will check whether an off-diagonal kernel change is visible even if the diagonal changes vanish to first order.

## Proof saved — after 03:39 Asia/Tbilisi

Created PROOF.md. Exact finite-array identities give `C_l^+=C_l-eta S_n s_l^-2 R_l^T e g_n^T Q_{l-1}^T`. A uniform ordered-product lemma and induction over fixed training steps yield the profile recursion and full kernel. The earlier scalar result is recovered by d=1. The initial matrix-kernel rate was derived both from the limiting exponential formula and from finite-size ordered-pair sums `J_n=sum_{j<l}s_j^-2 s_l^-2`, with `J_n/n^2 -> t^2/2`.

The explicit diagnostic is t=S=1, inputs e1,e2, targets 1,1, equal loss weights, readout e1. Its first active kernel matrix is
`[[1+eta^2/12, eta/4+eta^3/96], [eta/4+eta^3/96, 1+eta^2/6+eta^4/480]]`,
and the perpendicular coefficient is `1+eta^2/12`.
The full kernel also includes the constant bias contribution. Its diagonal rates vanish, while the off-diagonal rate is 1/4. At step two the (2,2) profile entry is `eta^2(1-eta)(1-z)/4`, which proves the common-matrix-per-layer ansatz fails for 0<eta<1. Thus the result is explicitly a depth-profile closure; no claim of a finite-dimensional replacement is being made. Next: independent dense parameter differentiation, profile quadrature, finite-size convergence, scalar reduction, and degenerate-case checks.

## Independent computation — 03:43 Asia/Tbilisi

Created verify.py without importing or copying functions from the earlier script. It uses 2 by 2 block products, a separate depth RK4 integrator and Simpson quadrature, and direct numerical differentiation of every parameter in a small dense network. It also checks the earlier scalar orbit by products with a layer explicitly omitted rather than division by the total product.

Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit code 0. The `nice: setpriority: Operation not permitted` warning occurred because priority was already 20; the script checked this directly. Complete output is saved as verification_output.txt, with detailed JSON in verification_data.json. Output that matters:

```text
All checks passed.
Earlier exact scalar orbit/kernel error: 2.220446049250313e-16.
Earlier normal moments, product versus normal law: 1.3322676295501878e-15.
Earlier limiting scalar recursion versus matrix profile: 1.822542117224657e-12.
Dense full-parameter kernel error: 8.518963312553751e-12 (432 numerical partials).
Dense numerical GD update versus block identity: 6.827871601444713e-14.
Finite-size initial-rate error: 2.3180769803676782e-10.
Pair sum calculated two ways: 15.767360802925927 in both cases.
Explicit first-step polynomial error: 4.951594689828198e-14.
At eta=0.2: M1 = [1.0033333333333334, 0.05008333333333326,
                    0.05008333333333326, 1.0066700000000495].
B1 = 1.0033333333333334.
C2_22 profile formula error: 1.9949319973733282e-17.
C2_22 endpoints: 0.007999999999999985 and 0.0.
Initial M rate by symmetric differences: [0.0, 0.25000000000104167,
                                         0.25000000000104167, 0.0].

t      n       max full-state error, over states 0,...,4
0.5      32   0.005257971049
0.5     128   0.002242808586
0.5     512   0.0003583684793
0.5    2048   0.0001325679896
0.5    8192   3.534222484e-05
1.0      32   0.01588113158
1.0     128   0.003343502255
1.0     512   0.0009280438499
1.0    2048   0.0002138960677
1.0    8192   5.609617701e-05
2.0      32   0.03011930654
2.0     128   0.01200030759
2.0     512   0.003243333723
2.0    2048   0.000749772108
2.0    8192   0.0001883916879

Profile grids 1024 versus 2048: errors 3.674e-12, 2.762e-11, 2.984e-10
at t=0.5,1,2 respectively.
Gain reversal differences: 6.515e-9 (n=128), 4.882e-11 (n=512),
                         3.873e-11 (n=2048).
One-layer constant kernel, zero-residual stationary state, and zero-input
bias-only training: all passed.
Resources: 1.729050667 seconds, 43646976 bytes peak RSS, priority 20.
```

The finite-size convergence arrays have Gaussian log-gain bridges conditioned on S=1.3, sigma=0.6; they test the deterministic theorem, not an iid universality claim. The full-state error is the maximum absolute entry error in M, B, S*Q, and b; it includes initial and later states. The profile reference is numerical, with independent grid refinement reported above. This is not a rigorous finite-size error bound. The exact normal law is established algebraically, rather than by estimating lognormal tail moments from a small Monte Carlo sample.

## Attempt to break the result

Checked layer multiplication order against direct numerical differentiation, including parameters outside the trained block. Verified that the perpendicular kernel contribution remains present although those parameters do not move on the training examples. Differentiated the finite-size kernel before taking the limit and recovered the same t^2 coefficient. The nilpotent two-example case tests a leading off-diagonal effect invisible to diagonal first derivatives. Reversing the gain order is not an exact finite-size invariance; the small nonzero discrepancies are reported rather than discarded. The example also has a nonzero commutator between C2 at opposite depths, supporting the need for ordered products. Zero residuals, zero training inputs, and L=1 each test a distinct exceptional case.

## Final extension audit and report

Derived the endpoint commutator symbolically: `(C2(0)C2(1)-C2(1)C2(0))_21=eta^6/32`. This gives a direct proof of noncommutativity in the same two-example case, rather than relying on the computed commutator alone. Added this identity to PROOF.md and its independent numerical check to verify.py.

Reran the exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit code 0, all checks passed. The mathematical outputs are identical to the preceding run. The added commutator-entry formula error is `2.0752307207730358e-20`. Final run resources: `1.7911947909742594` seconds, `43991040` bytes peak RSS, priority `20`. The complete final output is verification_output.txt and its data are verification_data.json.

Saved REPORT.md with verdict PARTIAL. Rechecked the normalization of the loss (weights sum to one), the Theta-to-W factor 1/n in the GD update, the order of forward and suffix products, the constant bias term in the full kernel, and the distinction between fixed finite training steps and unbounded training time. The S=1 example is expressly deterministic, not a positive-probability conditioning claim. The random convergence proof uses a single coupled normal total gain plus a summable maximum-gain bound. No result is asserted for Gaussian matrix initialization or nonaligned perturbations. No outside-folder mutation, git command, or subagent was used after the initial startup recall noted above.

The next checkable step is a finite-variable reduction of the two-example depth profile, or a stronger obstruction to such a reduction; the exact C2 profile and commutator provide tests. Balancedness identities of gradient flow cannot be imported into discrete GD without bounding their defects. That direction is left to the next session rather than adding a second extension here.

Final read-only artifact checks: `rg -n 'VERDICT:|Task:|commutator|Scope|Gaussian' REPORT.md PROOF.md LOG.md` confirmed the verdict on REPORT.md line 1 and the scope qualifications. `ls -lh REPORT.md PROOF.md LOG.md verify.py verification_data.json verification_output.txt` confirmed all six artifacts exist. `tail -25 ~/codex_op_1114/briefs/T245/LOG.md` confirmed that the earlier log ends with its finite-horizon and non-universality qualifications; no additional result changes the present extension.
