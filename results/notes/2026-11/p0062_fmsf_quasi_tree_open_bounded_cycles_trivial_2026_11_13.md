---
name: p0062_fmsf_quasi_tree_open_bounded_cycles_trivial_2026_11_13
description: "[PROVISIONAL] P0062 (Lyons-Peres Q11.37): FMSF connected on graphs roughly isometric to a tree? Open (Pete-Timar 2020 cite it open, no later paper found); bounded-simple-cycle case is deterministic and trivial; first real test case is tree x K2"
metadata:
  type: project
status: provisional
---
P0062, rank 4 on the 200 list. Question (Probability on Trees and Networks, 19 Aug 2026 ed., Question 11.37, p.410): if a connected locally finite graph is roughly isometric to a tree, is its free minimal spanning forest connected a.s.?

Literature, checked 13 Nov 2026 (two web searches):
- Pete-Timar, arXiv 2006.06387 (2020), cite it as open; their counterexample is for the UNIFORM forest (the free USF tree count is not a quasi-isometry invariant) and does not transfer.
- Lyons-Peres-Schramm, Minimal spanning forests, Ann. Probab. 2006 (math/0412263): the FMSF together with Bernoulli(eps) percolation is connected on any graph. That is near-connectivity, not an answer.
- Newman-Tassion-Wu, arXiv 1512.09107: one tree on quasi-planar slabs Z^2 x {0..k}^(d-2). A different geometry.
- No paper found that answers it.

Observation (mine, short, checked once): if the simple cycles of G have length at most lambda, then for x, y with d_G(x,y) = d, EVERY spanning tree of a ball containing a geodesic from x to y joins them by a path of length at most about lambda*d. The tree path and the geodesic split into simple cycles of length at most lambda, and there are at most d of them. The event "x and y joined within L steps" depends only on finitely many edges, so it survives the weak limit, and the FMSF is connected for every labelling. Such graphs (bounded blocks arranged in a tree) are roughly isometric to trees, so this case is trivial. The same argument gives the bounded-cycle FSF theorem of Shi-Sidoravicius-Song-Wang-Xiang 2018 (see [[p0050_fsf_wsf_singularity_open_bounded_cycles_partial_2026_11_13]]).
So the question only has content on quasi-trees with unbounded cycles. The simplest test case is T x K2 (a regular tree times an edge, the "tree ladder"), then T x P_k. It is untested here; a finite-ball simulation of the MST there is a cheap next step.

How to apply: start from the tree-ladder case, not from the bounded-cycle case.

Update 13 Nov, about 14:10: tree ladder numerics and a sketch (unverified).
- Simulation (scratchpad p0062/ladder_mst.py, scipy MST): binary tree of depth n times K2, iid uniform labels, 200 trials per n. Tree path in the free MST between (root,0) and (root,1): mean 2.1-2.5 steps, 90th percentile 5, deepest level reached 90th percentile 2. Flat from n=4 to n=14, and the path never reached depth n-1 for n >= 8. This points to the FMSF being connected on T x K2.
- Sketch of why. In the MST the path between x and y is the minimax path. A path (v,0) -> (v,1) uses one rung r_w and both copies of the tree path [v,w], so its value is max(U(r_w), max over tree edges e on [v,w] of max(U(e0),U(e1))), with a tree-edge weight distributed like t^2 (critical level 2^(-1/2) on the binary tree). The minimax path crosses the invasion bottleneck edges in order. Between bottlenecks it sits in a finite pond where every weight is below the current bottleneck. The recursion stops as soon as a pond contains a rung below the next bottleneck, which has probability at least about 0.7 per pond vertex. So the recursion ends a.s. and the path is finite. Not written carefully: the independence between ponds and the tie-breaking at a bottleneck need checking before it counts.
- If it holds, the same argument should cover T x H for any finite connected H and bounded-degree T. A general quasi-tree (not a product) needs a different decomposition (blocks of bounded diameter along the tree), and that case is the actual question.
- More shapes, 13 Nov 14:2x (p0062_tree_ladder/prod_mst.py): 3-ary tree x K2 to depth 9, path mean 2.5-2.8, flat; binary tree x P3 to depth 13, path mean 4.8-5.4, deepest level q99 at most 7, never reaches depth n-1 for n >= 9. The same tightness in all three products.
- Reduction (standard, valid on any graph): FMSF restricted to a FINITE cluster C of {labels < t} is the MST of C, because a cycle whose largest label is below t lies inside C. So x and y are FMSF-connected whenever they share a finite cluster at some level t. A disconnection therefore needs m(x,y) = inf over finite paths of the largest label to be at least p_c(G), and the cluster of x in {labels <= m} to be infinite: a bottleneck edge f with label m and one side infinite below it. The proof for T x K2 has to handle the descending chain of such bottlenecks. The pond argument in the sketch above is meant to do exactly that.
