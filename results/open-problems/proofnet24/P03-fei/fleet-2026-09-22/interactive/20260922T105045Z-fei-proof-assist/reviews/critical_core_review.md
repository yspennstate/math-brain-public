# Independent review of robust trigger clusters and critical child slack

Date: 22 September 2026, 11:12 UTC.

Reviewed complete report: `fei_proof_20260922/path_c/REPORT.md`, SHA-256 `1c61bd06ffacc0dd25ce74a3b11842056a0b2ec56f5e20b3e48310abff8ba286`.

Reviewed/replayed checker: `fei_proof_20260922/path_c/CHECKER.py`, SHA-256 `49564d274482faaf565e90354318509cbb65f46900b2fb23a546126b47997039`.

## Verdict

**PASS for the stated conditional structural, physical-fiber, child-slack, and single-state fractional transport results. No mathematical blocker found. Full FEI remains OPEN.**

The new capacitated Hall argument in section 8 is valid. It removes reuse of a trigger-coordinate capacity within one fixed trigger-independent row family at one fixed Boolean state. It does not remove the cost of selecting or covering enough rows, the loss from choosing only one representative of a clique, the cost of complement queries, or reuse across successive states. The report preserves these limitations.

The report inherits `K>2` from its source terminal-core theorem. This matters for the child-slack proof because `rho>K>2>r_m` makes the good-fiber contribution positive. State `K>2` explicitly near the report's initial setup and theorem 8.1 to make that hypothesis visible without opening the source. This is an exposition improvement, not an unresolved mathematical assumption.

This review checks logical correctness and scope, not publication priority. The supplied finite checker is supporting evidence, not the proof of arbitrary-dimensional assertions or of the Hall theorem.

## 1. Exact source definitions checked

I read both complete reports used for the terminality and crossing premises at the exact cited commits:

- [All-block terminal critical core](https://github.com/yspennstate/math-open-problems/blob/85ffa60db26997421d980b1f86c03d82259504ca/proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md), blob `68e838a493671ed5c27a29468dfcce7bb621d860`.
- [Terminal trigger surplus](https://github.com/yspennstate/math-open-problems/blob/fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113/proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md), blob `d283c7b495316959312155f8ba68fb83569d9633`.

The precise source charge is

`U_A = sum_{k in A} h2(q_k) - W_A`,

with `D_A = sum_{k in A} q_k + sum_{j notin A} c_j(A)` and `W_A = sum_{j notin A} j'(q_j)c_j(A)`. All-block terminality means `U_A >= K D_A` for every nonempty physical block, with `K>2`.

For an unqueried coordinate, in the centered parent gauge,

`c_i(A) = E[(2 Pr(E_i=1 | x_A)-1)_+]`.

This equals the absolute-value formula in the source. It is nonnegative and monotone when more physical coordinates are revealed. Child `J` and `F` use folded influences, equivalently character-centered children. No uniformity of a projected nonphysical measure is assumed.

The broader curvature-refunded source inequality is used as the report's stated imported premise; this review verifies the new deductions from it rather than claiming to re-audit every older dependency in the repository.

## 2. Robust derivative rigidity and the factor-16 DAG

The Boolean identity `Delta_j E_i = Delta_i E_j` holds pointwise because `E_i = Delta_i b` and Boolean differences commute. Replacing `E_i` by `Q_i` changes its derivative only at an erroneous endpoint, giving disagreement at most `2 epsilon_i`. All probabilities refer to one physical cube, with derivative indicators constant in their own coordinate.

The distinct-subcube separation lemma is correct. Unequal dyadic masses differ by at least a factor two; equal-mass distinct coordinate subcubes intersect in at most half of that mass. Therefore two unequal stripped subcubes have symmetric difference at least `2(s_i+s_j)/3`, whereas the approximation bound is at most `2 eta(s_i+s_j)/(1-eta)`. The contradiction uses exactly `eta<1/4`.

Thus reciprocal adjacency forces equality of closed core sets and agreement of the stripped literals. Equality propagates along reciprocal paths, and every pair of vertices in such a connected component is then reciprocal. The components are cliques. For cliques of size at least two, the literal assignments combine as stated, including the two-vertex case.

For a one-way arrow, the triggering row gives `p_ij >= 2(1-2 eta)q_i`, while the nontriggering row gives `p_ij <= 2 eta q_j`. Hence `q_j >= ((1-2 eta)/eta)q_i`. At `eta=1/16`, the quotient of clique subcube masses is at least `210/17`. Because that quotient is a power of two, it is at least 16. Cycles are impossible, and the claimed four-unit drop in trigger codimension follows.

The geometric single-path coefficient is correctly calculated as `272/225`. It is explicitly a charge for one representative per clique along one path. Summing it over merging paths would reuse the sink; the report correctly does not do that.

Two small explanatory details could be added without changing the result:

- A singleton reciprocal component has no row supplying the literal at its own coordinate; that literal can be chosen arbitrarily because its derivative subcube does not depend on it. The physical-fiber theorem only uses cliques of size at least two.
- An inactive coordinate cannot be a trigger of a positive robust row, even at positive `eta<1/2`: its mixed derivative is zero, while the triggering lower bound is positive. This justifies the sentence that a sink has no external trigger when every active row is robust.

The exact `eta=0` classification is sound. No one-way trigger or inactive trigger is possible; disjoint closed clique monomials reproduce every Boolean derivative. Their quotient with `f` is constant. The report appropriately makes no claim of a new FEI theorem for this familiar product class.

## 3. Physical point-defect fibers

Multiplying by the monomial sign XORs derivative supports, so `Inf_i(f M_N)=epsilon_i` exactly for `i` in the clique. Averaging ordinary child influences under uniform physical restriction gives the sum of these errors.

The minimum nonzero total ordinary influence on an `m`-cube is `m 2^(1-m)`. The proof through the cube's minimum nontrivial edge cut is correct, including the induction cases. It concerns ordinary influence of the error function, not folded influence; that is the appropriate quantity here.

Subtracting all nonconstant error fibers from the activation event gives

`P(good active fiber) >= 2^(-t) - epsilon_C/J_m`.

The conversion to `(1-2 eta)/(1-eta) * 2^(-t)` uses `m s = 2^(-t)J_m` and `epsilon_C <= eta m s/(1-eta)`. Both are exact. No independence between the activation and error events is required. These are physical branch probabilities, not spectral selector probabilities.

## 4. Linear child slack and extremality

For `m>=2`, the one-point defect has centered influence `q=2^(1-m)` in every coordinate, Fourier empty mass `(1-q)^2`, and each other Fourier mass `q^2`. The entropy formula and the analytic bound `H_m<4m q` are correct. Concavity of `j` and its endpoint chord give `j(q)>=2q`, hence `r_m<2`.

Full ratio extremality ensures every other physical child has nonnegative `rho J-F` slack after character centering. On each good fiber its slack is exactly `(rho-r_m)J_m`. Since the source setup has `rho>K>2`, multiplying the good-fiber lower bound by this positive quantity is legitimate.

The coefficient follows without a hidden factor:

`m s - epsilon_C >= J_C - 2 epsilon_C >= (1-2 eta)J_C`.

Thus theorem 7.1's linear lower bound is valid. The exact restriction identity `Delta_A F = rho D_A + E L_z`, combined with the imported `Delta_A F <= B_A-W_A`, gives theorem 7.3 in the correct direction.

The full-clique exception is also sound. There is only one outside fiber, and its nonconstant probability is bounded strictly below one; it therefore vanishes. The resulting point defect has ratio below two and cannot be the intended critical core.

Terminality alone would not guarantee nonnegative slack of all children. The report correctly distinguishes full ratio extremality from terminality and does not substitute one for the other.

## 5. Detailed check of the new capacitated Hall theorem

Let `R` satisfy `F_i intersect R = empty` for each selected row. For any subset `S` of rows, set `A = union_{i in S} F_i`. Then `A` is disjoint from all of `R`, in particular from `S`. Hence every requested row still exists after revealing `A`; none of its demand is silently attached to a queried-away coordinate.

For `i in S`, the sigma-field generated by `x_A` refines the one generated by `x_{F_i}`. Conditional Jensen applied to the convex function `(2u-1)_+` proves

`c_i(A) >= c_i(F_i) >= q_i-epsilon_i`.

Terminality rearranges exactly to

`sum_{k in A}(h2(q_k)-Kq_k) >= sum_{j notin A}(K+j'(q_j))c_j(A)`.

All omitted terms are nonnegative because `K>2`, `j'>=0`, and `c_j>=0`. Retaining `S` proves the needed subset inequality

`sum_{k in union_{i in S}F_i} sigma_k >= sum_{i in S}d_i`.

These are the complete capacitated Hall conditions, not merely the singleton-row conditions. In the finite row/trigger network, source-to-row capacity is `d_i` and trigger-to-sink capacity is `sigma_k`. Unrestricted row-to-trigger arcs can be replaced by a finite capacity exceeding the total demand plus total trigger capacity. Max-flow/min-cut therefore supplies a flow saturating all source-to-row edges.

Capacities and flows may be arbitrary nonnegative real numbers. No integrality theorem, rational approximation, discretized codeword allocation, or computability claim is needed for existence. Each trigger coordinate appears once on the sink side, so its capacity cannot be reused among rows within this one flow.

The converse is correct as stated. With all capacities nonnegative, infeasibility yields a subset `S` whose union-trigger capacity is smaller than its demand. Monotonicity then gives `U_A<KD_A` for that actual physical block. If some `sigma_k<0`, then `U_{k}-KD_{k} = sigma_k - sum_{j!=k}(K+j'(q_j))c_j({k})<0`, so the singleton is affordable directly.

A deterministic choice of the first failed cut depends only on the known current Boolean function and decoded physical history. It introduces no extra hidden spectral-address random variable. This is an information statement, not an efficient algorithm claim: finding the exact cut or exact capacities can be expensive, and the physical query's entropy cost is still present in `U_A`.

One representative per clique in a DAG antichain is trigger-independent. The theorem does not justify selecting all clique vertices, paying one capacity repeatedly across different antichains, or transporting the same numerical bank between different physical states. The report explicitly leaves these global issues open.

## 6. Verification performed and remaining scope

I independently replayed `CHECKER.py`; it returned `PASS` with 276 exhaustive gates through dimension three, 592 robust rows, 280 reciprocal components, and the described eleven-variable hierarchy. Its physical-fiber probabilities are `127/128` and `1/2`, and its tested child-slack inequalities pass at `rho=10`. The largest displayed point-defect ratio through dimension 128 was approximately `1.1059020282359633`.

This checker does not exercise the new Hall theorem. My acceptance of theorem 8.1 is based on the complete analytic argument above. A numerical Hall test is unnecessary to justify the finite capacitated Hall implication and would not prove its hypotheses for all Boolean functions.

The results are suitable to publish as a scoped research checkpoint. They do not yet give a global nonreused entropy budget, a full robust-row cover, or control of nonrobust/small-influence rows. They therefore do not establish a dimension-independent FEI constant.
