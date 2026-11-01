# Independent audit: bounded-overlap theorem

Date: 11 October 2026. Scope: the recovered threshold manuscript, Section 5 (Read-k unions of structured gates), and its antichain and signed-piece dependencies in Sections 3–4.

Reviewed source: `recovered/threshold/fourier-entropy-threshold-functions/paper/main.tex`, SHA-256 `3a395e98153f826fa9160c348e45779f204d3ea77376f40cd71ee57440ba8193`.

Verdict: no substantive gap found in the stated bounded-overlap ordinary and strengthened entropy theorems. This was an independent analytic reading of the complete argument, not external peer review or a formal proof. No fresh computational counts are claimed. The manuscript's existing numerical and exact-check receipts belong to their original authors and runs.

## Path probability and global root normalization

For gate l, resampling every relevant coordinate makes the final value of h_l independent of the complete initial input. Hence the event that f begins false and h_l finishes true has probability exactly p_0 p_l. Every intermediate input is uniform. A single coordinate resampling crosses from false to true with probability Inf_j(f)/4: on a pivotal edge the initial endpoint is false with probability one half, and the independent new bit takes the true endpoint with probability one half. The union bound and each coordinate's membership in at most k gate supports give p_0 sum_l p_l <= k I(f)/4. Monotonicity of outer gates is unnecessary for this step.

The queue law is a valid subprobability law: it assigns probability to all finite successful runs; infinite queues and invalid subset sizes may lose mass. Gibbs' inequality only requires total mass at most one. The factor Lambda = sum_l log_2(1+pi_l/k) is counted once per complete run, not at every node.

## Forest roots and support disjointness

The ownership map tau partitions A among the visited gates. The directed edge l -> l' means that an owned coordinate in A_l also belongs to R_l'. Choosing one root in each source strongly connected component reaches every active gate. A directed spanning forest yields a run visiting each active gate once and outputs exactly A, with roots + children = number of active gates <= |A|.

If j belongs to A intersect R_r and A intersect R_s for two roots, its owner tau(j) has an edge to each root except when it equals that root. Because neither root component has an incoming edge from another component, tau(j) must lie in both source components. This is impossible for distinct roots. Thus the root-intersection sets are disjoint, and dense-root costs satisfy sum b_r <= beta sum |A intersect R_r| <= beta |A|. Each nondense root is paid from a variable it owns. No independence of root supports in the physical cube is assumed.

The remaining subset cost follows from sum_l |A_l| log_2(kappa_l/|A_l|) <= |A| log_2 k. Root and child gate names together contribute at most |A| log_2 k. Multisets permit repeated routing through one parent variable; the prescribed child labels and deterministic occurrence order still specify a valid finite queue run.

## Rare pivotal pieces and signed Fourier interference

For a signed piece supported on a rare gate's pivotal set, condition only on coordinates outside the gate support R. Every remaining fiber has support density alpha_z <= Inf_j(h) <= 2 p. Hypercontractivity at correlation 1/4 gives stability <= alpha_z^(8/5). Averaging and then dividing by E alpha_z yields a relative factor at most (2p)^(3/5). This order of operations preserves the rare-fiber cost; no claim is made that conditioning preserves the original density of an arbitrary event.

The exponent is 3/5 - 2/beta = 5/12 for beta = 120/11. Dense/nondense status is evaluated on A=T union {j}; therefore |A intersect R|=|T intersect R|+1 agrees with the rare-tail lemma.

Disjoint physical pieces do not have disjoint Fourier supports. The manuscript correctly uses the pointwise weighted Cauchy–Schwarz inequality nu_j(T) <= sum_l nu_j,l(T), rather than identifying the coherent squared Fourier sum with a mixture. Splitting each outer piece among at most M pivotal regular inners introduces the stated factor M. The subsequent tail union bound contributes kM, with the logarithm paid by integration of the exponential tail.

## Strengthened bound and small nonsingleton mass

The singleton entropy estimate uses |fhat({i})| <= Inf_i(f) and Var(d_i f) >= |fhat({i})|-fhat({i})^2, giving the claimed 2 log_2(e) J payment.

The proof of W log_2(1/W) <= 8 J handles the delicate near-dictator regime. Small J with variance >3/4 forces a coordinate of influence >1-2 delta. After orienting that coordinate, f=A+x_i B and D=1-B have support E of density eta <=1-E B. The manuscript correctly bounds W <=4 eta and J by the Dirichlet energy of D. Every edge leaving E contributes at least one quarter to the squared derivative, so cube isoperimetry gives J >= (eta/2) log_2(1/eta). This pays the missing mass logarithm. The constants and inequalities in the other two regimes are consistent.

For the queue vacuum term, W I <= Var(f) J gives W Lambda <= log_2(e) J through the path lemma. It does not reuse the ordinary bound v Lambda <= log_2(e) I as a strengthened conclusion.

For the conditional G moment, when nu_j(T nonempty) >=1/2, the ordinary moment immediately suffices after multiplying its bound by two. In the opposite case, nu_j(empty)>1/2 implies Inf_j(f)>1/2, since fhat({j})^2 <= Inf_j(f)^2. Some outer gate then has pivotality >1/(2k), and one regular inner has pivotality >1/(2kM). The unate Chow identity and the desirability order imply rank <4k^2M^2. This gives the stated pointwise G bound; conditioning creates no unaccounted entropy charge.

The sum of these separate payments is the displayed coefficient 8+3 log_2(e)+K_0+2 E_0, rounded to 66. The chain-partition extension changes only the subset normalizer by a factor w per selected coordinate; the rank and conditional arguments remain valid within one chain.

## Scope preserved

The theorem requires a finite bound k on actual relevant-support overlap. It does not remove this parameter for arbitrary Boolean functions. It also does not supply an automatic dimension-independent estimate for the joint witness functional. The latter is a separate variational refinement and remains a research obligation in the general case.
