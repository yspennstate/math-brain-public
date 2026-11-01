# Derived checkpoint 07: parallel slabs, exceptional-layer geometry, and method boundaries

Date: 2026-10-02 UTC / 2026-10-03 Jerusalem. Parent master0803e2077b56636cc151b4c6534d6fb5fbd35574. All results below are new extensions of the already archived LTF and monotone-band results. Full Boolean FEI remains open in this campaign. Internal proof audits are separate from outside peer review and historical priority.

The complete bundle is in `proofnet24/P03-fei/continuations/2026-10-02-parallel-slabs/`. Read the actual proofs, audits and scripts, not just this summary.

## 1. Every parallel slab

`stripe_extension_parallel_slabs_proof.md` proves a universal bound H(f)<=C_slab I(f) for every Boolean interval indicator or complement of one weighted linear form, with arbitrary real weights, bias, endpoints, and either endpoint convention. The proof supplies the stronger largest-weight local split bound and restriction induction. Narrow intervals use a general disjoint-exceptional-support entropy lemma. Wide intervals use signed pivotal slabs, atom-safe relative concentration, primary halfspace noise/influence estimates, weighted Jensen, and a signed empty-atom dyadic KL calculation.

The same proof establishes at most m actual sign crossings under STRICT separation greater than twice the largest input weight, with a constant C_m depending only on m. It does not claim arbitrary-weight, arbitrary-spacing finite-crossing FEI. The final statement makes the crossing and endpoint scope explicit.

Independent K and heat/entropy audits and the full root audit pass. The original candidate is preserved. Root read the complete final proof, both audits and the checker, and reran3,846slab cases through dimension12, including2,184narrow and1,662wide cases. The script checks signed stability, pair tails, low-degree mass and KL identities. Numerical checks supplement the analytic proof and do not establish its dimension-independent conclusion.

## 2. Finite unions with additive boundaries

`stripe_extension_union_proof.md` proves for arbitrary disjoint cube subsets E_j, with g_j=1-2 1_(E_j) and f=1-2 1_(union E_j),

H(f)<=r sum_j H(g_j)+log2(e)(1+1/e) sum_j Var(g_j).

If no cube edge joins distinct components, I(f)=sum_j I(g_j). More generally the exact difference is twice the physical probability of joining edges. Hence component FEI with constant C yields union FEI with constant rC+log2(e)(1+1/e). Applying the slab theorem permits arbitrarily narrow parallel intervals when their separating gaps are strictly wider than2w_max. Boundary cancellation prevents dropping that condition.

The independent K, author-coordinator, root and separate union/chain audits pass. Both author and independently written verifiers are preserved; the latter uses exact integer boundary identities.

## 3. Nonmonotone exceptional Hamming layers

`stripe_extension_almost_symmetric_proof.md` removes both monotonicity and contiguity. For any Boolean f constant on all layers outside an exceptional set, let ell be the longest consecutive run of exceptional layers, and P_sym coordinate-permutation averaging. It proves

H(f)<=24.08 I(f)+32(ell+1)^2[I(f)-I(P_sym f)].

The constant depends on ell, not on the total number of exceptional layers. When exceptional layers are pairwise nonconsecutive, the sharper bound is H(f)<=24.08 I(f)+32[I(f)-I(P_sym f)]<=56.08 I(f)<57I(f) for nonconstant f. For k exceptional layers this implies [25+32(k+1)^2]I(f). With no exceptional layer, use the established symmetric constant12.04 directly.

The proof averages symmetric Boolean comparators along uniform maximal chains. Exact uniform edge sampling gives E I(g)=I(f); orthogonal symmetrization gives E I(f-g)=2[I(f)-I(P_sym f)]. A layer adjacency bound and an averaged variance argument handle both dimension regimes. This is distinct from the slab/KL route and does not assume monotone layer labels or nested comparators.

The finite-crossing consequence permits any fixed number m of exceptional score points and total L1 normalized weight deviation A=sum_i |w_i/c-1| bounded independently of dimension: at most m(floor(A)+1) layers can be nonsymmetric. No bias or crossing-spacing hypothesis is needed in this restricted weight regime. Arbitrary labels at exceptional score points are included by the closed-interval count.

Root, heat, author-coordinator and separate independent union/chain full analytic audits pass; the maximum-run/deficit statement has its own heat audit. Root read and reran the independently written checker: all65,812Boolean functions through dimension4,4,000additional functions in dimensions5/6,75,808component assignments,16,368layer-subset adjacency checks and3,000weighted attained-endpoint examples. Integer identities and numerical entropy/eigenvalue checks are clearly distinguished.

## 4. Preserved exact failures of stronger local claims

At equality crossing distance2w, weights(1,1/2,1/2) and the open interval(-1,1) have actual pivot influence1/2 while each crossing halfspace has influence3/4. The four-row exact certificate and the audits preserve this cancellation. Endpoint perturbation preserving the Boolean function shrinks the interval, so it cannot rescue the non-strict general separation claim. The arbitrary two-crossing theorem survives through its narrow branch.

`three_crossing_largest_weight_obstruction.md` supplies an exact three-crossing family with unique largest weightN+1, pivot influencealpha=2^-N, and

Delta H/alpha >= (N+3)/2-log2[N(N+1)/2] -> infinity

for oddN>=15. Majority's central-layer coefficient formula, an elementary uniform coefficient lower bound, and the exact entropy split prove this analytically. It obstructs a universal largest-weight LOCAL split criterion; it is not an FEI counterexample and does not rule out another adaptive coordinate choice. Root and an adversarial independent audit pass. Both exact-rational/Decimal checkers are preserved; root reran the independent check through250odd coefficient-bound dimensions<=513 and400-digit entropy displays throughN511.

## Sources, completeness and remaining targets

Read `stripe_extensions_source_check.md` and `stripe_extensions_checks_readme.md`. Primary Keller--Klein2019, KOS2004, O'Donnell--Wright--Zhou2011 and standard hypercontractivity inputs are credited. Recent primary papers arXiv2606.00246v2 and2609.21563v1 still present general FEI as conjectural and prove distinct subclasses. The latter's actual abstract history is September18,2026v1, inspectedOctober2UTC. Bounded searches located no earlier complete proof of these precise new statements; they do not certify priority.

The unrestricted Boolean conjecture, arbitrary-weight finite crossings, all-fugacity forest correlation, full Sidorenko Mobius-ladder case, and Kaplansky/direct finiteness are not solved by this checkpoint. Subsequent work must build beyond the internally completed subclass results and preserve failed routes rather than presenting finite evidence as a proof.
