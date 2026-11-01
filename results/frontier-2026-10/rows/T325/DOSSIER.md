# T325 Do trained transformers learn in-context regression by gradient descent?

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv abstracts below (read 16 Oct 10:3x).
The row is not audited yet. Statements about a paper's content beyond its abstract are marked as unread.

## STATEMENT
As listed: prompts (x_1, y_1, ..., x_N, y_N, x_query), x_i ~ N(0, I_d), y_i = <w, x_i>, w ~ N(0, I_d). Zhang-Frei-Bartlett: gradient
flow on one linear self-attention layer from a suitable initialization reaches a predictor implementing one step of preconditioned
GD. Prove that gradient training of a multi-layer softmax transformer, or of a linear transformer with L >= 2 layers from random
initialization, converges to a predictor whose in-context risk approaches the Bayes-optimal (ridge) risk as N -> infinity, and say
which algorithm it implements.
Comment: as written the target is too weak in one place. With noiseless labels and d fixed, every consistent predictor has risk
-> 0 as N -> infinity (for N >= d least squares is exact), so "approaches Bayes as N -> infinity" is met by one GD step with step
size -> 1 already. The content is in the proportional limit N/d -> 1/q with label noise sigma^2 > 0, where the Bayes predictor is
ridge with lambda = sigma^2 (in the per-sample normalisation) and L steps of GD have a strictly larger risk for every finite L. A
sharper statement: (i) for L >= 2 untied linear layers from random initialization, gradient flow on the population loss converges
to a global minimizer, and that minimizer is L steps of preconditioned GD; (ii) the risk of that minimizer converges to the ridge
risk as L -> infinity at the proportional limit, at a rate to be identified. The softmax half is separate.

## FRONTIER
- Zhang, Frei, Bartlett arXiv:2306.09927: one linear self-attention layer, gradient flow from a suitable random initialization
  reaches a global minimum; error competitive with the best linear predictor; robustness to several distribution shifts.
- Ahn, Cheng, Daneshmand, Sra arXiv:2306.00297: one layer, the global minimum is one step of preconditioned GD; for L layers,
  certain critical points implement L steps of preconditioned GD (landscape, not convergence).
- Mahankali, Hashimoto, Ma arXiv:2307.03576: one layer with isotropic Gaussian covariates: the pretraining minimizer is one GD step;
  non-isotropic covariates and weights give preconditioned GD.
- Gatmiry, Saunshi, Reddi, Jegelka, Kumar arXiv:2410.08292: looped linear transformer (multi-layer, weights shared across layers):
  the global minimizer of the population loss is multi-step preconditioned GD, and gradient flow converges fast through a gradient
  dominance condition - described as the first such analysis for a multi-layer transformer in this setting. Initialization: not
  read beyond the abstract.
- Zhang, Wu, Bartlett arXiv:2402.14951: linear attention plus a linear MLP block reaches nearly Bayes-optimal risk with a non-zero
  prior mean (attention alone cannot); the optimal block is one GD step with learnable initialization, found by gradient flow.
- Zhang, Singh, Latham, Saxe arXiv:2501.16265: multi-head linear attention; merged key-query weights give two fixed points and one
  abrupt loss drop; separate key and query matrices give exponentially many fixed points and saddle-to-saddle dynamics, during which
  the model implements principal component regression with a growing number of components.
- Chen, Sheen, Wang, Yang arXiv:2402.19442 and He, Pan, Chen, Yang arXiv:2503.12734: one layer of multi-head softmax attention;
  global convergence of gradient flow under suitable initialization, optimal within the class up to a constant; from random
  initialization the heads learn a debiased GD predictor that is Bayes-optimal up to a proportional factor.
- Boursier, Boyer arXiv:2512.11784: in the large-prompt regime one softmax layer behaves like linear attention along the whole
  training trajectory (non-asymptotic concentration), so linear-attention optimization analyses transfer to one softmax layer.
- Open as far as these abstracts show: untied L >= 2 linear layers from random initialization (convergence to a global minimizer),
  and every multi-layer softmax case.

## ARCHITECTURE
Rotational invariance of the isotropic Gaussian model reduces the population loss to a function of a few matrices per layer. In the
known proofs one of two structures carries the argument: a one-layer loss that is a low-degree polynomial with balanced dynamics
(2306.09927), or weight sharing that makes the L-layer map a polynomial in one preconditioner, where a gradient dominance
inequality holds (2410.08292). Inside the invariant class where each layer's preconditioner is a multiple g_l of the identity, L
layers compute L GD steps with step sizes g_1..g_L, and the risk on noiseless data is int prod_l (1 - g_l s)^2 dMP_q(s), with MP_q
the Marchenko-Pastur law of the sample covariance.

## FAILURE POINT
Untied layers. The population loss is a polynomial of high degree in L independent matrices, with no weight sharing to collapse it
to one variable. Ahn et al. find the L-step-GD critical points inside a restricted sparsity pattern only, and from random
initialization the parameters start outside that pattern; Zhang-Singh-Latham-Saxe show that even one layer with separate key and
query matrices has exponentially many fixed points. No gradient dominance inequality is known for untied layers.

## SHAPE
Weeks for the scalar-step reduction (gradient flow on (g_1..g_L) against MP_q, global landscape, risk gap to ridge as L grows).
Months for untied matrices from random initialization (attraction to the invariant class plus the landscape inside it). Softmax
with L >= 2: no route visible yet beyond the large-prompt linearization of 2512.11784, which is proved for one layer.

## OBSTRUCTION
Two pieces: (1) the invariant class (block structure, scalar preconditioners in the isotropic case) must attract gradient flow from
random initialization; (2) inside it, the step-size landscape must have no spurious minima. Piece (2) is a one-dimensional
polynomial problem: on noiseless data the best residual polynomial of degree L with P(0) = 1 minimizes a convex quadratic, and its roots are real
and lie in the support (it is proportional to the Christoffel kernel at 0, i.e. an orthogonal polynomial for s dMP_q(s) - standard
orthogonal-polynomial facts, recalled), so the global minimum is reached by real steps g_l = 1/root_l; with label noise the extra term changes the quadratic and this
argument is not claimed. The open question for
piece (2) is whether the map from steps to coefficients creates spurious local minima where two steps coincide.

## TARGETS
1. Scalar-step landscape: prove that gradient flow on (g_1, ..., g_L) for R(g) = int [P(s)^2 + sigma^2 q (1 - P(s))^2 / s] dMP_q(s),
   P(s) = prod (1 - g_l s), reaches the global minimum from almost every start; give the risk gap to ridge as a function of L.
   (A numerical check of this is running for q = 0.25, 0.5, sigma^2 = 0, 0.25, L = 1..6; results are added below when done.)
2. Untied linear layers, isotropic data: show that the off-pattern parameters decay under gradient flow from small random
   initialization, which with Target 1 gives convergence to L-step GD.
3. Two softmax layers: extend 2512.11784's large-prompt linearization to the second layer, whose input is no longer Gaussian.

## MEASUREMENT 2026-10-16 (agent A): the scalar-step landscape of Target 1
Setup (gd_steps_landscape.py, gd_steps2.py; outputs gd_steps_out.txt, gd_steps2_out.txt): R(g) = int [P(s)^2 + sigma^2 q (1 - P(s))^2 / s]
dMP_q(s), P(s) = prod_l (1 - g_l s), by quadrature on MP_q; L-BFGS-B from 200 uniform random starts on [0, 6/b], b the upper MP edge;
q = 0.25, 0.5; sigma^2 = 0, 0.25; L = 1, 2, 3, 4, 6. The "floor" is the minimum over all real-coefficient P of degree L with P(0) = 1
(a quadratic in the coefficients), so it may need complex roots.
- Noiseless: 200/200 starts reach the floor for every q and L. The floors agree to 7 digits with R*_L = 1 / sum_{k=0}^{L} q^(-k)
  (q = 0.25: 0.2, 0.047619, 0.0117647, 0.0029326, 1.831e-4; q = 0.5: 1/3, 1/7, 1/15, 1/31, 1/127), i.e. R*_L ~ (1 - q) q^L, the
  Chebyshev-type rate q per layer. The formula is read off the numbers, not proved here; a proof via the Christoffel function of
  s dMP_q at 0 is the obvious route. The optimal roots are real and inside the support, as the OBSTRUCTION section expected.
- With noise, L <= 3: 200/200 reach the floor (its roots are real).
- With noise, L = 4 and 6: the floor polynomial has complex-conjugate roots (q = 0.25, L = 4: 1.976, 1.749, 0.669 +- 0.236i), so no
  real step sizes reach it. GD on real steps ends at coincident pairs of steps, the boundary of the real-root region. At L = 4 all
  200 starts end at one value (q = 0.25: 0.0777449 against the floor 0.076704; q = 0.5: 0.1853658 against 0.18270). At L = 6 the
  ends split: q = 0.25 four values 0.0776525 (51% of starts), 0.0778655, 0.0779109, 0.0795123; q = 0.5 three values 0.1845717 (33%),
  0.1846001, 0.1847158. Whether these are strict local minima or slow points of L-BFGS-B was not checked (no Hessian).
- Ridge floors: 0.0751838 (q = 0.25), 0.1753905 (q = 0.5). Gap of the best real-step value to ridge at L = 6: 3.3% and 5.2%.
Reading: Target 1 as written is false with label noise: for L >= 4 here the global minimum over polynomials is not reachable by real
step sizes, and at L = 6 GD on real steps has several end values. Two repairs: (i) the trained linear transformer is not restricted to
real scalar steps - two layers with 2 x 2-block preconditioners, or any parametrization that realises a real quadratic factor
(1 - a s + b s^2) with complex roots, reach the floor; whether the invariant class of Target 2 contains such pairs is the question to
settle; (ii) restricted to real steps, the statement to prove is uniqueness of the constrained minimum (supported at L = 4, contradicted
at L = 6 unless the extra end values are stalls). Noiseless Target 1 is supported: 200/200 at every L tried, with the exact floor above.

## RATE 2026-10-16 (agent A): the gap to ridge as a function of L, over polynomials
Here the minimum is over all degree-L residual polynomials with P(0) = 1, complex roots allowed (what a parametrization realising
real quadratic factors reaches; for real steps see the MEASUREMENT above).
- Noiseless, proof. R*_L = min int P^2 dMP_q = 1 / sum_{k<=L} p_k(0)^2, with p_k the orthonormal polynomials of MP_q (Christoffel
  function at 0). MP_q (mean 1, variance q, q < 1) has Jacobi parameters alpha_0 = 1, alpha_n = 1 + q (n >= 1), beta_n = q (recalled,
  the free Poisson law; the first two match the quadrature's mean and variance). The three-term recurrence at s = 0,
  sqrt(q) p_{k+1}(0) = -alpha_k p_k(0) - sqrt(q) p_{k-1}(0), gives p_k(0) = (-1)^k q^(-k/2) by induction, since
  (1 + q) q^(-k/2) - sqrt(q) q^(-(k-1)/2) = q^(-k/2). Hence R*_L = 1 / sum_{k=0}^{L} q^(-k) = (1 - q) q^L / (1 - q^(L+1)), the formula
  the MEASUREMENT read off the numbers. The optimal P is K_L(s, 0) / K_L(0, 0), whose roots are real and in the support (zeros of a
  Christoffel kernel interlace; recalled), so real steps reach it - matching 200/200.
- With noise, measured (gap_rate.py, gap_rate_out.txt; Chebyshev basis, L = 1..16, ridge risk int lam/(s + lam) dMP_q on the same
  nodes, lam = sigma^2 q): the gap R*_L - R_ridge decays geometrically with ratio rho^(-2), where rho = |x0| + sqrt(x0^2 - 1) and
  x0 = (-2 lam - a - b)/(b - a) is the ridge pole s = -lam mapped onto [-1, 1], [a, b] = [(1 - sqrt q)^2, (1 + sqrt q)^2]. Successive
  ratios at L = 12..16 against rho^(-2): q = 0.25, sigma^2 = 0.25: 0.21382 / 0.21382; sigma^2 = 1: 0.1459 / 0.14590; q = 0.5,
  sigma^2 = 0.25: 0.33999 / 0.33999; sigma^2 = 1: 0.17157 / 0.17157. At sigma^2 = 0 the pole sits at 0 and rho^(-2) = q, the noiseless
  rate above. This is the Bernstein-ellipse rate of polynomial approximation to the ridge filter lam/(s + lam) (recalled standard
  approximation theory); the prefactor was not fitted.
So Target 1's second half has an answer: risk(L) - risk(ridge) = Theta(rho(q, sigma^2)^(-2L)), proved for sigma^2 = 0, measured
to five digits otherwise. More noise means a pole further from the support and a FASTER rate. What stays open is the first half
(reachability) - with noise and real steps, see above.

## SPURIOUS MINIMA 2026-10-16 (agent A): the L = 6 end values with noise are strict local minima
gd_steps3.py, gd_steps3_out.txt: sigma^2 = 0.25, L = 6, 200 fresh starts per q; each distinct end value polished with BFGS, then the
gradient norm and a central-difference Hessian (h = 1e-6) at the polished point.
- q = 0.25: 0.077652515 (119 starts; steps 0.344 x4, 1.3029 x2), 0.077865513 (50; 0.6881 x6), 0.077910937 (31; 0.3349 x2, 0.852 x4).
- q = 0.5: 0.184571738 (64; 0.6004 x6), 0.184600118 (77; 0.2859 x4, 1.2223 x2), 0.184715804 (59; 0.2965 x2, 0.7652 x4).
- At every one |grad| <= 1.2e-9 and the Hessian is positive definite (smallest eigenvalue 1.4e-4 to 5.2e-3). These are strict local
  minima of the real-step risk, not stalls. Every minimum has its steps in groups of even size: a complex-conjugate pair that the
  polynomial optimum wants is collapsed to a double real root, and the grouping chooses the basin.
- The global real-step minimum attracts 60% of starts at q = 0.25 and 32% at q = 0.5. At q = 0.5 the global minimum is one step size
  repeated six times, (1 - 0.6004 s)^6. The gaps between minima are small (at most 0.3% of the risk).
Reading: with label noise, Target 1 in its "almost every start" form is false at L = 6 for real scalar steps. The two statements that
survive: (i) noiseless, every start reached the global minimum (now with the closed form); (ii) with noise, any parametrization that can
realise a complex-conjugate pair of steps (2 x 2 blocks, or a learnable quadratic factor per pair of layers) has no reason to keep these
minima - not tested. For the transformer question this sends the weight to Target 2: whether trained untied layers stay in the
scalar-step class (and inherit these minima) or leave it.

## QUADRATIC FACTORS 2026-10-16 (agent A): pairing the layers does not remove the minima
Repair (ii) above, tested (quad_factors.py, quad_factors2.py; outputs *_out.txt): P(s) = prod_{i<=L/2} (1 - a_i s + b_i s^2), each
factor free to have a complex root pair, sigma^2 = 0.25, 200 starts from random real-step pairs, then gradient norm and Hessian at
each distinct end.
- Reaching the polynomial floor: q = 0.25, L = 4: 85/200; L = 6: 56/200; q = 0.5, L = 4: 77/200; L = 6: 135/200.
- The other ends are strict local minima again (|grad| <= 4e-9, Hessian positive definite, smallest eigenvalue 1.6e-5 to 1.2e-2). The
  commonest is the symmetric point where two factors coincide: q = 0.25, L = 4 ends 115/200 at two identical factors
  (a, b) = (1.8768, 0.7036) with real roots, risk 0.0777449 - exactly the real-step minimum. At L = 6, q = 0.25 has five end values
  (0.0752533 global, 0.0755624, 0.0776432, 0.0794197, 0.0795123), q = 0.5 two (0.1762316 global, 0.1768083 with two equal factors).
Reading: the spurious minima come from the product structure (permutation symmetry of the factors), not from the real-root
constraint alone. The risk is convex in the COEFFICIENTS of P; it is not convex in any factorisation tried. For the transformer this
makes the question sharp: an untied L-layer linear transformer composes L maps, so its predictor is a product, and gradient flow on it
can be expected to meet these minima unless the matrix structure gives a way around them (extra directions in the full matrix space
that are not in the scalar class could turn these minima into saddles - not tested; that is the next measurement, on small d with
full matrices).

## FULL MATRICES 2026-10-16 (agent A): at d = 4, L = 4 untied full preconditioners keep the real-step minimum
full_matrix2.py, full_matrix2_d4L4.txt (full_matrix.py and full_matrix_d4L4.txt are the first try, superseded - see below). Residual
P(S) = (I - G_4 S)...(I - G_1 S) with free 4 x 4 matrices G_l (64 parameters), S = X^T X / N, N = 16 (q = 0.25), sigma^2 = 0.25; risk
mean_S [tr(P P^T)/d + sigma^2 q tr((I - P) S^{-1} (I - P)^T)/d] over 30 sampled S, each conjugated by all 384 signed permutations so
that the scalar points G_l = g_l I are exact critical points (the commutant of that group is the scalars). Two seeds.
- The real-step minimum (two coincident steps, e.g. 0.427, 0.541, 1.38, 1.38, risk 0.084704 against the polynomial floor 0.0845375 on
  the same spectrum) is a strict local minimum in the full 64-dimensional space: |grad| 1.1e-9, Hessian smallest eigenvalue +1.06e-3,
  none negative. Seed 2 the same (+1.04e-3).
- Gradient descent on full matrices from five small random initialisations (entries 0.05 N(0,1)) ends at that same value in 5/5 runs
  per seed (0.0847042, 0.0880496), and a 1e-3 kick off the scalar minimum returns to it. None reaches the floor.
- The first try, without the group average, gave a non-zero gradient at the scalar point (1.3e-2) and descents below the floor: full
  matrices fitted the 200 particular samples of S. That run is kept only as the reason for the symmetrisation.
Reading, for d = 4, q = 0.25, L = 4 only: with label noise, untied linear layers trained from small random initialisation converge to
L-step GD with real step sizes, and that predictor misses the best degree-L polynomial (here by 0.2 percent of the risk). The extra
matrix directions do not open a way to the complex-pair optimum. Not tested: larger d, L = 6 (where the real-step landscape has several
minima), other q. If it holds, Target 1 and 2 combine to: trained linear transformers implement real-step GD, which is optimal without
noise and strictly sub-optimal against polynomial filtering with noise from L = 4.

## L = 6, 2026-10-17 (agent A): the full-matrix end values below the scalar minima are a fit to the sample
Files: full_matrix3.py, full_matrix3_d4L6.txt (d = 4, q = 0.25, sigma^2 = 0.25, L = 6, 30 sampled S averaged over the
signed-permutation group, M = 11520).
On the training spectrum: polynomial floor 0.0808308, best scalar minimum 0.083401 (steps 0.383 x 4, 1.481 x 2; two more scalar
minima at 0.083407 and 0.083707). Full-matrix L-BFGS from three small random initialisations ends at 0.0833879, 0.0827501 and
0.0827501, below the best scalar minimum, with 6-37 percent of each layer's norm outside the scalar line.
Scored on 4000 fresh S (not symmetrised; polynomial floor there 0.0816349): the scalar minima give 0.0840169, 0.0840402 and
0.0855324; the three full-matrix end points give 0.0928951, 0.0955964 and 0.0954886.
Reading. The training gain of the full matrices (0.0006 below the scalar minimum) turns into a loss of 0.011-0.012 on fresh S, so
the end points below the scalar minima at L = 6 are fits to the 30 sampled spectra, not lower critical values of the risk. The
scalar minima generalise to within 0.0006 of their training value. With 30 sampled S the L = 6 question of Target 2 (does the
full-matrix landscape leave the scalar minima at L = 6) is therefore not answered by this run; it needs enough sampled S that the
fresh and training risks of the full-matrix end points agree, which at L = 4 took the group average over 200 samples.

## L = 6 with 90 sampled S, 2026-10-17 (agent A)
Files: fm3_m90.py (full_matrix3.py with M = 90 base samples, M = 34560 after the group average), full_matrix3_d4L6_m90.txt.
Training spectrum: polynomial floor 0.0802762; scalar minima 0.082753, 0.082756, 0.083206 (best steps 0.294 x 2, 0.470 x 2,
1.553 x 2; at 30 samples the best was 0.383 x 4, 1.481 x 2, so the scalar landscape itself moves with the sample). Full-matrix
L-BFGS from three small random initialisations ends at 0.0821430, 0.0821158, 0.0821158, again about 0.0006 below the best scalar
minimum, with 13-32 percent of each layer's norm off the scalar line. Every layer of every end point has all four singular values
equal: the off-scalar part is a rotation, each layer is a multiple of an orthogonal matrix.
On the same 4000 fresh S (floor 0.0816349): scalar minima 0.0840166, 0.0840104, 0.0858268; full-matrix end points 0.0851136,
0.0865685, 0.0867711.
Reading. Tripling the sample cut the full-matrix fresh-minus-training gap from 0.0095-0.0128 to 0.0030-0.0047, roughly in
proportion, while the scalar minima moved from 0.0006 to 0.0013 above their training value. The full-matrix end points still
lose to the best scalar minimum on fresh S (by 0.0011-0.0028). With 90 samples the run still fits the sample, so it does not
decide whether the full-matrix landscape at L = 6 has a critical value below the scalar minima. Two cheaper routes than more
samples: (i) restrict each layer to multiples of orthogonal matrices, which the end points select by themselves, and integrate
over S exactly in that family; (ii) compute the population risk of the end points by exact expectation over S rather than by
sampling, since the risk is a polynomial in the layer matrices.
