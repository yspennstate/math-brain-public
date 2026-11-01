TASK: B14 ACCOUNT: fleet02 RUN: 2026-09-21T19:01:43.679479Z — affine pair-parity restriction with an exact centered global budget

**Status:** PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated `math_brain` or cognitive-memory retrieval/context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. Configured reasoning level, provider reasoning-token usage, and provider thinking time: UNKNOWN / not exposed.

**FULL-PROBLEM CHANGE:** **NO FULL-BOUND MOVEMENT.** No finite dimension-independent FEI constant is proved here.

**MECHANISM CHANGE:** **YES.** The previous B14 runs stayed inside physical-coordinate erasure/refunded selectors and then all-block lower criticality. This run executes the required method change: it enlarges the admissible restriction tree to a specific affine operation, a two-coordinate parity split, and proves an exact nonnegative *centered influence drop* for that operation. Those drops telescope exactly along an arbitrary adaptive hybrid physical/affine tree, so there is now a genuinely global summable budget rather than another scalar threshold for the same selector.

FLEET_RULES moves used:
- **#1 CHANGE THE CATEGORY:** from physical subcubes only to codimension-one affine parity cosets;
- **#12 FIND WHAT IS CONSERVED:** use character-invariant folded influence `J` as the tree potential;
- **#19 MAKE IT AN ALGORITHM:** define a hybrid restriction tree whose local budget telescopes to the root `J`.

No novelty or publication-priority claim is made.

## 0. Fresh frontier and the required three-run comparison

Fresh scientific master was recovered during the run. The last three substantive B14 mechanisms before this run were:

1. **fixed-seed recursive selector convergence:** repeated self-composition of one fixed balanced non-dictator cannot make the local selector obstruction diverge;
2. **centered refunded selector:** character-centering removed deterministic parity padding and localized a hard physical restriction-critical descendant to small centered first-shell fraction;
3. **block-JS / fractional-Han criticality:** the coherent restriction surcharge tensorizes over physical blocks, yielding all-block erasure floors and a fractional-Han hierarchy.

The same universal implication remained unpaid: construct a restriction strategy whose entropy decrement is globally chargeable to a nonreused `O(I)` budget. Therefore this run does not further optimize the centered singleton threshold or the block-Han constants.

The current interactive continuation handoff supplies the exact physical centered budget
`D_A = J(f)-E J(f_A=z)` and its tree telescope. It also warns that every-prescribed-coordinate payment is false and that weak ratio-critical functions can be tensor-replicated without lowering their ratio. Those warnings are preserved.

The newest completed neighboring result inspected during this run was B17's self-XOR/Hellinger bridge; it shows that destroying joint XOR dependence is fatal even after retaining all shiftwise Hellinger credits. A concurrent B18 affine-subspace artifact had begun appearing, but no completed B18 report was present at the observed master, so no claim is made about its final scope.

## 1. Normalization

Work on `F_2^n` with Boolean `f:F_2^n -> {-1,+1}`. Let

`a_S = fhat(S)`,  `mu(S)=a_S^2`,  `X~mu`.

Write

`H(f)=H(X)`,
`p_i=Pr(i in X)=Inf_i(f)`,
`I(f)=sum_i p_i`.

The folded/centered influence is

`q_i=min(p_i,1-p_i)`,
`J(f)=sum_i q_i`.

Multiplication by a Fourier character translates `X`, hence preserves `H` and `J`. Median-character center once so every current coordinate has `p_i<=1/2`; then `J(f)=I(f)`. Recenter descendants after every restriction. This changes neither descendant entropy nor descendant `J`.

For a pair `i!=j`, write

`p_ij = Pr(i in X and j in X)`.

## 2. The new affine operation: fix one pair parity

Fix distinct coordinates `i,j`. Split the physical cube by

`x_i xor x_j = sigma`,  `sigma in {0,1}`.

Parameterize each parity coset by eliminating `x_i`: keep `x_j` and all other coordinates, and put `x_i=sigma xor x_j`. Let the resulting `(n-1)`-variable Boolean children be `g_0,g_1`.

Define the affine entropy decrement

`Delta^xor_ij H := H(f) - (H(g_0)+H(g_1))/2`.

This is a genuine restriction to two affine hyperplanes, not a mock change of variables.

### Theorem 2.1 -- exact ordinary-influence drop

For every Boolean `f`,

`I(f) - ( I(g_0)+I(g_1) )/2 = 2 p_ij`.          (2.1)

In particular the drop is always nonnegative.

### Proof

For any surviving coordinate `k` outside `{i,j}`, flipping the corresponding child coordinate flips only original `x_k`. Averaging the two parity cosets recovers the original `k`-edge disagreement probability, so its averaged child influence is `p_k`.

Flipping the surviving child coordinate `x_j` flips both original coordinates `i` and `j`. Let

`delta_ij = Pr_x[ f(x) != f(x xor e_i xor e_j) ]`.

Therefore

`(I(g_0)+I(g_1))/2
 = sum_{k notin {i,j}} p_k + delta_ij`.          (2.2)

Fourier expansion of a translation disagreement gives

`delta_ij
 = sum_S mu(S) 1{ |S intersect {i,j}| is odd }
 = p_i+p_j-2p_ij`.                               (2.3)

Subtract (2.2) from `I(f)` and use (2.3), proving (2.1). QED.

This identity is the reason the affine step is safe for FEI induction. No transformed-coordinate cost is silently dropped: the child total influence is computed in the actual quotient-cube coordinates, and its difference from the parent influence is exactly the nonnegative quantity `2p_ij`.

## 3. PROVED: exact centered pair refund

Assume now that the parent is median-character centered, so `J(f)=I(f)`. For each raw parity child let its quotient-coordinate influences be `r_{sigma,k}`. Define

`D^xor_ij(f)
 := J(f) - (J(g_0)+J(g_1))/2`.                   (3.1)

### Theorem 3.1 -- pair-affine centered budget identity

`D^xor_ij
 = 2 p_ij
   + (1/2) sum_{sigma in {0,1}} sum_k (2 r_{sigma,k}-1)_+`.     (3.2)

Hence

`D^xor_ij >= 2 p_ij >= 0`.                       (3.3)

### Proof

For every Boolean child,

`I(g_sigma)-J(g_sigma)
 = sum_k [r_{sigma,k}-min(r_{sigma,k},1-r_{sigma,k})]
 = sum_k (2r_{sigma,k}-1)_+`.                    (3.4)

Average (3.4), insert Theorem 2.1, and use `J(f)=I(f)`:

`D^xor_ij
 = I(f) - E_sigma I(g_sigma)
   + E_sigma[I(g_sigma)-J(g_sigma)]
 = 2p_ij + E_sigma sum_k(2r_{sigma,k}-1)_+`.

This is (3.2). QED.

The second term is a genuine recentering refund: parity restriction can polarize a surviving child influence past `1/2`, after which character-centering recovers the excess. Nothing negative is discarded.

## 4. PROVED: entropy decomposition and a pair cap

The affine split is also an ordinary one-coordinate split after an invertible linear change of physical variables. Put

`y_0 = x_i xor x_j`,
`y_j = x_j`,
`y_k = x_k` for `k notin {i,j}`.

Holding `y_j` fixed, flipping `y_0` flips only original `x_i`, so the splitter influence in this representation is `p_i`. The dual linear map only permutes Fourier coefficients, hence preserves spectral entropy. The two children at `y_0=0,1` are exactly `g_0,g_1`.

Let

`jmath(s) = 1-h_2(1/2+sqrt(s(1-s)))`,
`Psi(s) = h_2(s)+jmath(s)`,  for `0<=s<=1/2`.

The inherited sharp singleton recombination estimate is `JS<=jmath(s)` at centered influence `s`. The erasure term is at most the entropy of the splitter spectral bit, `h_2(s)`. Therefore

`Delta^xor_ij H <= Psi(p_i)`.                    (4.1)

Using the symmetric parameterization that eliminates `x_j` instead gives

`Delta^xor_ij H <= Psi(p_j)`.                    (4.2)

Thus

`Delta^xor_ij H <= min{Psi(p_i),Psi(p_j)}`.       (4.3)

Equivalently, in the original spectral coordinates the erasure part is the conditional binary entropy on the pair fibres `{S,S xor {i,j}}`; the two quotient parameterizations give the same child spectral-mass multisets.

Equation (4.3) is only an upper envelope. It does **not** imply that every pair has a bounded payment ratio, and no such every-pair claim is made.

## 5. PROVED: a globally summable hybrid physical/affine budget

At every node of a restriction tree:

1. median-character center the current Boolean function;
2. choose either
   - a physical coordinate split, with exact centered drop
     `D_i = J(parent)-E J(children) >=0`, or
   - a pair-parity affine split, with exact centered drop `D^xor_ij>=0`;
3. recenter each child and continue.

Both operations reduce the dimension by one. Continue until centered leaves are constants/characters, for which `H=J=0`.

Let `pi_v` be the probability of reaching node `v` under the uniform branch labels. Let `Delta_v` be its entropy decrement and `D_v` the corresponding centered budget drop.

### Theorem 5.1 -- exact hybrid tree telescope

For every such complete adaptive hybrid tree,

`sum_v pi_v D_v = J(root)`,                       (5.1)

`sum_v pi_v Delta_v = H(root)`.                   (5.2)

Consequently, if the strategy chooses at every internal node a physical or pair-affine split satisfying

`Delta_v <= C D_v`,                               (5.3)

then

`H(f) <= C J(f) <= C I(f)`.                       (5.4)

### Proof

At each node, (by definition of `D_v`)

`J(parent)=D_v+E[J(child)]`.

Multiply by the probability of reaching the node and telescope over the finite tree. Leaves have `J=0`, proving (5.1). The identical entropy recursion gives (5.2). Summing (5.3) and using the two identities gives (5.4). QED.

This is the requested global budget. Pair coordinates may be reused after later affine changes of basis, but there is no hidden multiplicity: every intermediate `J(child)` appears once with a plus sign and once with a minus sign and cancels. The only surviving budget is the original root `J`, which is at most the original physical `I`.

A randomized choice of admissible split is equally valid if its conditional expected entropy decrement is at most `C` times its conditional expected `D`; averaging simply adds another expectation to the same telescope.

## 6. NEW implication from the previous centered-shell localization

For a centered node let `K=|X|`. Its centered first-shell mass is

`W_1 = Pr(K=1)`

and, when `J>0`,

`r_c = W_1/J`,  because `J=I=E K`.

The *sum of the base pair drops available at that node* is

`sum_{i<j} 2p_ij
 = E[K(K-1)]`.                                      (6.1)

Since `K(K-1)>=K` for every integer `K>=2`,

`E[K(K-1)] >= E[K 1{K>=2}]
             = J-W_1
             = (1-r_c)J`.                           (6.2)

The earlier B14 physical selector localized any counterexample above the current certified lower-bound scale to a physical restriction-critical descendant with

`r_c < 0.3156061323581677`.

For that descendant, (6.2) forces

`sum_{i<j} 2p_ij
 > 0.6843938676418323 J`.                           (6.3)

This is a genuine before/after change in the obstruction. Previously, shell-poor critical cores were simply the regime where the singleton centered selector lost leverage. Now the same shell-poor condition implies a quantitatively large supply of **pair-affine nonnegative influence drops**.

Important quantifier: the left side of (6.3) is an availability statistic over all possible first affine splits. It is **not** a spendable sum; one tree node may choose only one split. Treating all pairs as simultaneously payable would reuse coordinates and is not authorized by (5.1). The remaining theorem must turn this large pair supply into an existential or randomized paid split.

A sufficient scalar condition for a pair is, by (3.3) and (4.3),

`min{Psi(p_i),Psi(p_j)} <= 2 C p_ij`,              (6.4)

but (6.4) is not proved to hold for some pair in every shell-poor Boolean core. Diffuse sign-free probability laws can fail such scalar overlap tests; the current handoff already shows that joint Boolean realizability cannot be replaced by a scalar profile relaxation.

## 7. A stronger critical-core reduction for this enlarged strategy

Consider all descendants reachable from a centered Boolean function by the hybrid operations above, with recentering after every branch. This is a finite family up to the finite choices of current coordinates. Choose a nonconstant descendant maximizing `H/J`, and among maximizers choose minimum dimension. Put `R=H/J`.

For every allowed physical or pair-affine first split, each nonconstant child has ratio strictly below `R`. Therefore

`Delta_v >= R D_v`,                                (7.1)

with strict inequality whenever positive child `J` survives.

For a pair this combines with (3.3)--(4.3) to give the new all-pair necessary condition

`2 R p_ij
 <= R D^xor_ij
 <= Delta^xor_ij
 <= min{Psi(p_i),Psi(p_j)}`                        (7.2)

for every pair in the hybrid-minimal critical core.

Thus a hypothetical unbounded-ratio sequence must simultaneously satisfy:
- the earlier physical centered restrictions are all lower-critical;
- every pair-parity affine split is also lower-critical;
- all pair co-occurrences obey (7.2);
- in the shell-poor regime their total base mass still obeys (6.2).

This is stronger than the previous physical-only critical core. It still does not bound `R`; the missing step is a Boolean joint-realizability theorem converting (6.2) and (7.2), plus signs/phase constraints, into a contradiction for sufficiently large `R`.

## 8. Preserved failure: pair parity is not automatically better

The new operation enlarges the strategy; it is not claimed to dominate physical restriction pointwise.

For the one-point defect on `n` variables,

`f_n(x)=1-2 1{x=0}`,  `N=2^n`,

one has

`p_i=2/N`,  `p_ij=1/N`.

For every physical coordinate split and every pair-parity split, one branch is constant and the other is the `(n-1)`-variable one-point defect. Hence

`Delta_i H
 = Delta^xor_ij H
 = H(f_n) - H(f_{n-1})/2`,                          (8.1)

and both local base influence drops are `2/N`. Their local ratios are identical and tend to `4` as `n->infinity`.

So pair parity does not magically repair a bad physical coordinate. Its value is the additional exact globally summable option (and the large pair supply forced by shell-poor spectra), not a false every-pair dominance statement.

All inherited counterexamples to payment at every prescribed physical coordinate remain valid and untouched.

## 9. Exhaustive sanity check, scope, and preserved checker failure

A checker was executed exhaustively on all `65,812` Boolean truth tables through dimension four.

Exact rational checks:
- `394,000` pair-affine identities
  `I(parent)-E I(raw child)=2p_ij`;
- `394,000` centered identities
  `D^xor_ij=2p_ij+recentring refund`;
- both natural quotient parameterizations had identical child spectral-mass multisets.

Floating diagnostics (not theorem certificates):
- the `Psi` cap had maximum observed violation `0`;
- after character centering, the worst best hybrid local ratio through dimensions three and four was `4.867668746754797`, equal to the worst best physical ratio there;
- in dimension two the hybrid option reduced the diagnostic worst best ratio from `4` to `2`.

The first checker draft failed immediately with the harmless harness error `Generator expression must be parenthesized`. The final source changes only that parenthesization and then passed. The failed draft is not used as evidence.

Finite checks do not prove a dimension-independent bound.

## 10. Literature/status check

Current primary-source checking still has the universal FEI conjecture open. González--MacManus--Pereyra (arXiv:2606.00246, submitted 29 May 2026) explicitly use coordinate restriction decrements and stopping binary trees: if the local decrement inequality held at the required branch nodes, induction would prove FEI. The present theorem is compatible with that architecture but adds a specifically affine pair-parity branch with an exact centered influence drop.

Chakraborty--Kulkarni--Lokam--Saurabh (TCS 2016) bound Fourier entropy using parity-decision-tree complexity, so parity restrictions themselves are not a novelty claim here. The point of this run is the FEI-facing exact drop `2p_ij` plus the centered refund and telescoping `J` budget.

Potapov (arXiv:2609.21563, 18 September 2026) proves FEI for plateaued functions (sharp class constant `4`) and partially bent functions (sharp class constant `2`), not the full conjecture.

No search miss is treated as evidence of novelty.

## 11. Exact residual for the next B14 step

**Full FEI remains OPEN.**

The next unpaid implication is no longer “find another scalar threshold for the centered singleton selector.” It is:

> On a hybrid-minimal centered Boolean critical core with small first-shell fraction, use the actual signed/Boolean joint constraints to choose a physical or pair-affine split (or a paid random mixture) satisfying `Delta <= C D` with a dimension-independent `C`.

The hard regime already has more than a constant fraction of `J` present as aggregate pair base drops by (6.2), while every pair must obey the critical inequality (7.2). The missing step is a contention/joint-realizability argument that converts that aggregate availability into one **legal** local payment without summing mutually competing pairs.

This scope is complementary to B17's joint self-XOR/Hellinger work and to B18's affine-subspace/plaquette line: B14's deliverable here is the exact restriction-tree budget and selector compiler, not a sign-free global profile optimization.
