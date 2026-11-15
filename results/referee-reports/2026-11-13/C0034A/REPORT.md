PARTIAL

# C0034: orthogonal union couplings of projection determinantal measures

No full proof or counterexample was obtained. The literature search found the requested rank-one case already proved by Lyons in 2003, and found no published resolution of the general question. This run supplies an explicit construction and proof for that case, the complement and coordinate-block consequences, an exact obstruction to the proposed induction, and 288 verified rational coupling certificates. Numerical searches remain numerical evidence.

Task: “Open problem C0034”, received 13 November 2026, approximately 10:07 Asia/Tbilisi (06:07 UTC).

## Statement and notation

Given orthogonal closed subspaces H_1,H_2 of ell^2(E), put H=H_1 direct-sum H_2. The question asks for random subsets X_1,X_2 with laws P_{H_1},P_{H_2} whose union has law P_H. For finite E, their fixed cardinalities force disjointness. Disjointness also follows on countable E from the one-point intensities: for each e, the required union intensity equals the sum of the two marginal intensities, forcing P(e in X_1 intersect X_2)=0.

For finite E, if V is a matrix with orthonormal columns spanning a rank-r space L, then

    P_L(B) = |det V_B|^2,    |B|=r.

Cauchy–Binet normalizes these masses to one. We use zero-based coordinate labels in all code and data.

## 1. Literature result

The original arXiv:1406.2707 was downloaded and converted to [text](sources/lyons2014.txt), without saving PDFs or rendering page images. Section 2, pp. 2–8, was read. Question 2.8 is on p. 6, immediately after stochastic domination, Theorem 2.7. Complement duality is Corollary 2.3. Spectral mixtures in Theorem 2.11 do not give the required joint splitting.

The following primary sources were checked. Matching text files and URL/hash provenance are in `sources/`; [SEARCH.md](sources/SEARCH.md) records the searches, including searches for citations to Question 2.8 and its earlier numbering, Question 10.1.

| Reference | Relevant result and its scope |
|---|---|
| R. Lyons, **Determinantal probability measures**, Publ. Math. IHÉS **98** (2003), 167–212, [DOI 10.1007/s10240-003-0016-0](https://numdam.org/item/10.1007/s10240-003-0016-0.pdf) | Theorem 6.2 proves stochastic domination for nested finite-ground-set subspaces. Section 10 states the present question as Question 10.1. **Lemma 10.4, pp. 203–204, already proves the rank-one difference law. Proposition 10.3 extends suitable fixed-difference couplings to countable E.** The paragraph after Lemma 10.4 explicitly notes the positive answer for every ground set of size at most five. |
| R. Lyons, **Determinantal probability: basic properties and conjectures**, Proc. ICM 2014, IV, 137–161, [arXiv:1406.2707](https://arxiv.org/abs/1406.2707) | Question 2.8 asks the full question; Theorems 2.7 and 2.9 concern domination. The author's [errata dated 30 December 2025](https://rdlyons.pages.iu.edu/errata/icm.pdf) report other resolutions but do not report one for Question 2.8. That omission alone does not establish openness. |
| J. Borcea, P. Brändén, T. M. Liggett, **Negative dependence and the geometry of polynomials**, J. Amer. Math. Soc. **22** (2009), 521–567, [arXiv:0707.2340](https://arxiv.org/abs/0707.2340) | Proposition 3.5 gives the strongly Rayleigh property for positive-contraction DPPs; Theorem 4.13 gives domination for ordered kernels. These results do not prescribe the law of the difference of a higher-rank monotone coupling. |
| R. Pemantle, Y. Peres, **Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures**, Combin. Probab. Comput. **23** (2014), 140–160, [arXiv:1108.0687](https://arxiv.org/abs/1108.0687) | Proposition 2.2 gives stochastic covering from the projected homogeneous Rayleigh property. This controls differences under conditional couplings, not the three marginals in the present question. |
| R. Lyons, A. Thom, **Invariant coupling of determinantal measures on sofic groups**, Ergodic Theory Dynam. Systems **36** (2016), 574–607, [arXiv:1402.0969](https://arxiv.org/abs/1402.0969) | Constructs invariant monotone couplings for ordered equivariant kernels. It does not assert that the removed process has the kernel difference. |
| N. Anari, S. Oveis Gharan, A. Rezaei, **Monte Carlo Markov Chain Algorithms for Sampling Strongly Rayleigh Distributions and Determinantal Point Processes** (2016), [arXiv:1602.05242](https://arxiv.org/abs/1602.05242); N. Anari, S. Oveis Gharan, C. Vinzant, **Log-Concave Polynomials I** (2018), [arXiv:1807.00929](https://arxiv.org/abs/1807.00929) | The former's Theorem 1.1 concerns mixing; the latter's Theorems 1.1 and 1.3 concern counting. Neither is a union-coupling theorem. Later log-concave sampling work was also searched. |
| A. I. Bufetov, Y. Qiu, A. Shamov, **Kernels of conditional determinantal measures and the Lyons–Peres completeness conjecture**, J. Eur. Math. Soc. **23** (2021), 1477–1519, [DOI 10.4171/JEMS/1038](https://ems.press/journals/jems/articles/17429) | **Published Theorem 1.4** proves completeness of sampled reproducing kernels; Theorem 1.6 proves tail triviality. This is a different Lyons–Peres conjecture. The arXiv version uses different theorem numbering. |
| J. Møller, E. O'Reilly, **Couplings for determinantal point processes and their reduced Palm distributions with a view to quantifying repulsiveness**, J. Appl. Probab. **58** (2021), 469–483, [arXiv:1806.07347](https://arxiv.org/abs/1806.07347) | Lemma 1 explicitly gives the singleton-difference law for finite-rank projection kernels. Theorem 1 treats reduced Palm measures; it does not settle arbitrary orthogonal splits. |
| A. Kassel, T. Lévy, **Determinantal probability measures on Grassmannians**, Ann. Inst. Henri Poincaré D **9** (2022), 659–732, [DOI 10.4171/AIHPD/152](https://ems.press/journals/aihpd/articles/7883115) | Proposition 5.15 proves monotone coupling for determinantal linear processes by reduction to DPPs. No general prescribed union marginal follows. |
| L. Decreusefond, G. Moroz, **Optimal transport between determinantal point processes and application to fast simulation**, VMSTA **8** (2021), 209–237, [article](https://www.vmsta.org/journal/VMSTA/article/211/read) | Studies transportation distances and simulation, not this three-marginal splitting. |
| A. Poinas, **On determinantal point processes with nonsymmetric kernels**, Electron. J. Probab. **31** (2026), paper 94, [arXiv:2406.03360v4](https://arxiv.org/abs/2406.03360v4) | Section 4 constructs marked/attractive couplings. Proposition 4.1 and Corollary 4.2 include pointwise splitting, with different kernel hypotheses and marginals; they do not answer Question 2.8. |

The author's current publications page was also checked and saved. No full resolution was located in this bounded search through 13 November 2026. This is not a complete citation-graph audit or a proof that no such publication exists. The special-case existence results below are already consequences of the 2003 paper.

## 2. Rank one: explicit construction from the minors

Suppose H_1=span(u), ||u||=1, and W=H_2 has dimension k. Choose an orthonormal basis v_1,...,v_k of W and write

    w = v_1 wedge ... wedge v_k,       z = u wedge w.
    a(B)=|w_B|^2  (|B|=k),           b(C)=|z_C|^2  (|C|=k+1).

Thus a=P_W and b=P_H. The coordinates w_B,z_C are the corresponding signed minors.

Construct a finite network with edges s -> B of capacity a(B), B -> C of capacity 1 whenever B is contained in C, and C -> t of capacity b(C). Fix lexicographic orders and run Edmonds–Karp. We prove that the maximum flow is one.

For a family F of k-subsets, let N(F) consist of the (k+1)-subsets containing some B in F. Let Pi_F and Pi_N be exterior-coordinate projections. The interior product i_u, adjoint to exterior multiplication by u, satisfies ||i_u||<=1 and i_u z=w because u is unit and orthogonal to W. Moreover its B-coordinate depends only on z_C with C containing B. Consequently

    Pi_F w = Pi_F i_u Pi_N z,
    sum_{B in F} a(B) <= sum_{C in N(F)} b(C).                 (1)

This is a norm form of the adjoint Laplace/Plücker expansion. It works over both R and C, with conjugates in the adjoint.

Equation (1) is weighted Hall. Explicitly, a cut with a crossing B -> C edge has capacity at least one. A cut without such an edge, whose source side contains the B-nodes F, must also contain N(F), so its capacity is at least

    1 - a(F) + b(N(F)) >= 1.

The source cut has capacity one. Max-flow/min-cut therefore gives a flow gamma(B,C) with B-marginal a and C-marginal b.

Sample (B,C) from gamma and set X_2=B, X_1=C\B. The union is C~P_H. The difference is exactly one point, and for every e

    P(X_1={e}) = P(e in C)-P(e in B)
               = (P_H)_{ee}-(P_W)_{ee} = |u_e|^2.            (2)

Thus X_1 has the required rank-one law. Equivalently, first choose e with probabilities |u_e|^2 and then choose B avoiding e with conditional law

    q_e(B) = gamma(B,B union {e}) / |u_e|^2,                 (3)

whenever |u_e|>0. Equation (2) normalizes each q_e; zero-probability e need no conditional law. The B-marginal is a, and summing (3) over e in a fixed C gives exactly b(C). This proves the union law. In general q_e is not ordinary conditioning of P_W to avoid e.

[rank_one_flow.py](code/rank_one_flow.py) implements this construction using Fraction capacities and no LP solver. Its [worked rational example](data/rank_one_flow.json) saves the q_e laws. The flow has value one, 19 augmentations, and 19 positive masses; the separate kernel-minor verifier checks its three marginals.

For countable E and finite-rank W, Lyons' domination theorem gives containment and the fixed sizes give the same singleton argument. For infinite-rank W, take finite-rank W_m increasing densely to W and orthogonal to the same u. Take a weak limit of the rank-one couplings in the compact product of configuration spaces. Containment and “difference has at most one point” are closed. Each coordinate difference still has probability |u_e|^2; these probabilities sum to one, so the limit difference has exactly one point. This is the rank-one part of Lyons' Proposition 10.3.

## 3. Codimension one and coordinate pieces

For finite E, complement duality gives

    P_{L perp}(E\B)=P_L(B).

Put H_3=H perp. A union coupling is equivalent to a random partition (X_1,X_2,X_3) of E with X_i~P_{H_i}: take X_3=E\(X_1 union X_2). This formulation is symmetric in the three subspaces.

If any of their dimensions is zero, complementary sampling settles the question. If any dimension is one, apply the rank-one result to that space plus either other space and complement their union to obtain the third color. In particular, when dim H=|E|-1, apply rank one to

    H_3 direct-sum H_2 = H_1 perp

and set X_1=E\(X_2 union X_3). The union of X_1 and X_2 is E\X_3~P_H. Complement duality and this codimension-one argument also hold for closed subspaces on countable E.

Thus every finite instance with

    min(dim H_1, dim H_2, |E|-dim H) <= 1

is settled. This includes every |E|<=5. The first rank triple not covered is (2,2,2) at |E|=6; at |E|=7 it is a permutation of (2,2,3). No general codimension-two theorem is proved here.

For coordinate pieces, partition E into blocks E_j and assume H_i is the orthogonal sum of H_{ij} contained in ell^2(E_j). Given a coupling in each block, take the block couplings independently and unite each color. The projection kernels are block diagonal, so the determinants factor; this proves all three required laws. In particular, independent sampling works if H_1 and H_2 have disjoint coordinate supports. More generally it works whenever each finite block satisfies the displayed rank condition, using the proved block couplings. Countably many finite blocks follow by product measures and finite inclusion events.

## 4. The proposed induction does not automatically preserve the marginal

Composing a split of H_1' direct-sum H_2 with a rank-one addition of u preserves the H_2 law and the total union law. It does not force the law of the first component after adding the singleton.

Here is an exact example. Let the columns a,u,b,c of the following orthogonal matrix be

    Q = (1/2) [ 1  1  1  1 ]
              [ 1  1 -1 -1 ]
              [ 1 -1  1 -1 ]
              [ 1 -1 -1  1 ].

Take H_1'=span(a), H_2=span(b), and add u. Choose each row below with probability 1/4. Both stages are deterministic conditional on S.

| A | B | S=A union B | Added e | T=S union {e} | A union {e} |
|---|---|---|---|---|---|
| {0} | {1} | {0,1} | 2 | {0,1,2} | {0,2} |
| {3} | {0} | {0,3} | 1 | {0,1,3} | {1,3} |
| {1} | {2} | {1,2} | 3 | {1,2,3} | {1,3} |
| {2} | {3} | {2,3} | 0 | {0,2,3} | {0,2} |

The first-stage laws are P_span(a), P_span(b), and P_span(a,b). The second stage is a valid rank-one monotone coupling of P_span(a,b) and P_span(a,u,b), and e has law P_span(u).

But A union {e} assigns mass 1/2 to each of {0,2},{1,3}; P_span(a,u) assigns mass 1/4 to each of {0,2},{0,3},{1,2},{1,3}. The composed marginal is wrong. [induction_example.py](code/induction_example.py) checks every stage with exact fractions; [the saved record](data/induction_failure.json) contains the full example. This refutes an inference about arbitrary composition, not the existence of a compatible choice of couplings and not C0034.

## 5. Exact rational certificates

The transportation variables are x(A,B)>=0 for disjoint A,B of sizes p,q. The equations are

    sum_B x(A,B) = P_{H_1}(A),
    sum_A x(A,B) = P_{H_2}(B),
    sum_{A union B=C} x(A,B) = P_H(C).                        (4)

[exact_transport.py](code/exact_transport.py) generated rational orthogonal matrices in two ways: Cayley transforms (I-S)(I+S)^(-1) for rational skew-symmetric S, and products of rational Givens rotations with entries 3/5,4/5 or 5/13,12/13. Orthogonality is checked exactly. The two Cayley seeds and one Givens seed per n give 18 distinct matrices.

All probabilities are computed exactly from integer determinants after clearing denominators. HiGHS dual simplex proposes a support. A fraction-free exact integer solve then reconstructs its masses. Every reconstructed mass must be nonnegative and every equation in (4) must hold exactly. An unsuccessful reconstruction would be rejected, not counted as feasibility or infeasibility. All saved certificates passed on the first proposed support.

| Ground-set size n | All nonzero rank splits, three matrices | Additional column allocations | Saved certificates |
|---:|---:|---:|---:|
| 2 | 3 | 0 | 3 |
| 3 | 9 | 0 | 9 |
| 4 | 18 | 0 | 18 |
| 5 | 30 | 0 | 30 |
| 6 | 45 | 15 | 60 |
| 7 | 63 | 105 | 168 |
| Total | 168 | 120 | 288 |

“All nonzero rank splits” means every p,q>=1 with p+q<=n, taking the first p and next q columns of each sampled matrix. The additional suite covers every column allocation of ranks (2,2,2) at n=6 and (2,2,3) at n=7 for one Cayley matrix, modulo permutation of the three colors. There are 15 and 105 allocations, respectively. The two suites overlap once at each of those sizes: **288 files, 286 distinct (Q,I,J) instances**. These are finite samples, not all rational kernels or all subspaces of those sizes.

Each [certificate file](data/certificates/n6_cayley0_p2_q2.json) saves the entire rational Q, both column sets, and every positive rational x(A,B). [exact_summary.json](data/exact_summary.json) indexes the suite.

The independent [verify_certificates.py](code/verify_certificates.py) does not import the producer, NumPy, SciPy, or SymPy. It reconstructs projection kernels using Fraction and evaluates their principal minors by rational Gaussian elimination, an independent route from the producer's squared integer basis minors. It checks nonnegativity, disjointness, normalization, and every row of (4), including zero target masses. It verified **288 certificates and 14,772 marginal equalities**. [verification.json](data/verification.json) records the results and SHA256 hashes. The separate rank-one flow is additionally verified and is not included in that count.

## 6. Adversarial search and Farkas control

[adversarial_search.py](code/adversarial_search.py) targets the remaining rank triples at n=6,7. It performs eight trials for each size over each of the real and complex fields: **32 optimization runs, 23,742 objective evaluations**.

For the fixed transportation incidence matrix M, it chooses rational vectors y satisfying M^T y>=0 exactly. Every feasible coupling therefore satisfies b(Q)^T y>=0. It minimizes this signed Farkas functional over left Cayley rotations in O(n) or U(n), using L-BFGS-B and up to 60 iterations. Thus it searches for a violation of a valid coupling inequality over orthogonal decompositions. This is a local search over finitely many dual directions, not global optimization or exhaustive separation.

At each endpoint it also solves the full phase-I transportation problem, minimizing ||Mx-b||_1 for x>=0, and its bounded dual. All 32 local optimizations reported convergence. No counterexample candidate exceeded the 1e-7 investigation threshold. The smallest fixed-dual value was about -2.08e-16. Maximum actual primal L1 residual was 2.46e-9; maximum absolute raw dual phase-I value was 1.50e-9. Values of this scale are numerical error, not exact certificates. [adversarial_results.json](data/adversarial_results.json) saves the duals, floating matrices, diagnostics, and all runs.

The detector has an exact positive control: at n=3, require X_1={0}, X_2={1}, but prescribe union {0,2}. This deliberately violates the subspace-sum specification. In row order A={0},{1},{2}; B={0},{1},{2}; C={0,1},{0,2},{1,2}, take

    y = (-1,0,0; 0,-1,0; 2,1,1).

All six allowed disjoint-pair column sums are nonnegative, while b^T y=-1. This is an exact Farkas certificate of that artificial system's infeasibility; the numerical minimum L1 residual is 2. **It is not a counterexample to C0034.** The [saved certificate](data/positive_control_farkas.json) lists all pairings.

[verify_search.py](code/verify_search.py) independently checks the control, all **4,800 exact dual inequalities** in the search records, and the rank-one flow. It recomputes the floating objective values using scalar complex Gaussian determinants, agreeing within 3.76e-16; it also checks unitarity. Results are in [search_verification.json](data/search_verification.json).

## 7. Reproduction, resources, and remaining gap

From this directory, with Python 3, NumPy, SciPy, SymPy and pdftotext installed, and process niceness at least 10:

```sh
python3 code/induction_example.py
python3 code/rank_one_flow.py
python3 code/exact_transport.py
python3 code/verify_certificates.py
python3 code/adversarial_search.py
python3 code/verify_search.py
```

The numerical modules set BLAS/OpenMP/Accelerate and HiGHS to one thread. The inherited niceness was 15. Recorded peak resident memory was about 111 MiB for certificate production, under 20 MiB for the independent certificate verifier, and under 110 MiB for adversarial search. The sandbox refused OS address-space/data-limit changes; matrices remained small and code checks peak RSS below 3 GiB. No subagents, publication, or pushes were used. All artifacts are in this directory.

The general question remains unanswered by this work. In particular, there is no proof for arbitrary rank-(2,2,2) decompositions in dimension six. The exact four-coordinate example explains why rank-one addition alone does not supply the missing induction: it controls the added point's law, but not its joint dependence with the earlier first component.
