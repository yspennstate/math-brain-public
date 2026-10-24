# MOC4 account02/B08 — repeated-spectrum lift and common-block boundary

Run: `B08-20260922T000415Z-f12b18`

Outcome: **ESSENTIAL_STEP_APPLIED** (strict special-boundary theorem; the full MOC4 target remains open).

Candidate version: **MOC4-DOUBLE-EIGENVALUE-LIFT-v1**.

## Exact target and scope

For complex normal 4-by-4 matrices `A,B` with eigenvalues `a_1,...,a_4` and `b_1,...,b_4`, the MOC4 target is

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`.

This report proves the target when either spectrum has a repeated eigenvalue, and records the separate common-reducing-block reduction. It does **not** claim the unrestricted 4-by-4 conjecture.

Primary source context is the campaign TARGETS record, which points to Bebiano–da Providencia (2025), Drury (2004), and Mulero-Martinez (2026). No novelty claim is made for the special case proved here.

## Other-account result consumed

Consumed exact peer result `account03/B09`, candidate `MOC4-C2-COMPLEMENT-BOUND-v1`, coordination commit `a31796705864a71e1bb495ceac7d85b8c8ba1b18`, scientific commit `157071bb996f723151a14e79bf38764fb341c783`.

That result separates the middle (`k=2`) Cauchy–Binet layer into complementary-pair transport plus an orientation/parity component, and identifies the unresolved general task as coupling the one-minor transport to this middle layer with one common `S_4` optimizer. The repeated-eigenvalue symmetry below removes exactly the need to match the full orientation data: one designated 2-set marginal plus the one-point marginals suffice, and these marginals admit an exact permutation lift.

## Determinant expansion

Diagonalize `A`, and write

`A = diag(a_1,a_2,a_3,a_4)`, `B = U diag(b_1,b_2,b_3,b_4) U*`, with `U` unitary.

For row and column subsets `I,J` of the same size set

`Q_{I,J} = |det U[I,J]|^2`.

Principal-minor expansion followed by Cauchy–Binet gives the exact polynomial identity

`det(A+B) = sum_{I subset [4]} a_{I^c} sum_{|J|=|I|} Q_{I,J} b_J`,       (1)

where `a_K=prod_{i in K} a_i` and `b_J=prod_{j in J} b_j` (empty products are one).

For any permutation `sigma`,

`prod_i (a_i+b_{sigma(i)}) = sum_{I subset [4]} a_{I^c} b_{sigma(I)}`.       (2)

Thus it is enough to build a probability law `mu` on `S_4` whose subset-image statistics reproduce the combinations of `Q` that survive after equal eigenvalues of `A` are identified.

## Lemma 1 — a one-pair compound marginal always lifts to permutations

Let `P_{ij}=|u_{ij}|^2` and

`q_{jk}=Q_{12,{j,k}}=|det U[{1,2},{j,k}]|^2` for `j<k`.

There exists a probability measure `mu` on `S_4` such that

1. `Pr_mu[sigma(i)=j]=P_{ij}` for every `i,j`; and
2. `Pr_mu[sigma({1,2})={j,k}]=q_{jk}` for every unordered pair `{j,k}`.

### Proof

By Cauchy–Binet, `q` is a probability distribution on the six 2-subsets. Its weighted degree at column `j` is

`d_j := sum_{k != j} q_{jk} = P_{1j}+P_{2j}`.       (3)

We first orient fractionally the weighted complete graph on columns. We seek nonnegative masses `x_{j->k}` satisfying

`x_{j->k}+x_{k->j}=q_{jk}`,  and  `sum_{k != j} x_{j->k}=P_{1j}`.       (4)

The standard fractional-orientation/max-flow criterion says (4) is feasible iff for every vertex set `S`,

`q(E(S)) <= sum_{j in S} P_{1j}`.       (5)

For completeness, (5) is exactly the min-cut condition in the network having a source-to-edge node of capacity `q_e`, each edge node connected to its two endpoints, and vertex `j` sent to the sink with capacity `P_{1j}`; total source and sink capacity are both one.

For four vertices, (5) follows directly from unitarity:

- `|S|=0,1,4` is immediate.
- If `S={j,k}`, Hadamard/Cauchy–Schwarz on the 2-by-2 minor gives
  `q_{jk} <= (P_{1j}+P_{1k})(P_{2j}+P_{2k}) <= P_{1j}+P_{1k}`.
- If `S=[4]\{l}`, then by (3),
  `q(E(S)) = 1-d_l <= 1-P_{1l} = sum_{j in S}P_{1j}`.

Hence (4) has a solution. Choose `{j,k}` with probability `q_{jk}` and, conditional on that pair, assign rows 1 and 2 to `j,k` with the two orientation masses in (4). This produces row-1 marginal `P_{1j}` and row-2 marginal `d_j-P_{1j}=P_{2j}`.

For rows 3 and 4, Jacobi's complementary-minor identity for a 4-by-4 unitary matrix yields

`Q_{34,K}=Q_{12,K^c}`.       (6)

Apply the same fractional-orientation argument to the complementary-pair law `r_K=q_{K^c}`, targeting row-3 marginals `P_{3j}`; row 4 is then automatic. Conditional on the chosen top pair, couple the top and bottom orientations independently (or by any coupling with the prescribed two Bernoulli marginals). The resulting four assignments form a permutation. This defines `mu` and proves both claims. ∎

## Lemma 2 — double eigenvalue collapses every remaining k=2 requirement

Assume `a_1=a_2=alpha`; write `a_3=gamma`, `a_4=delta`. Let `mu` be the law from Lemma 1.

The `k=0,4` terms in (1) and the `mu`-average of (2) agree trivially. The `k=1` terms agree from the one-point marginals `P`. The `k=3` terms also agree because for `I=[4]\{i}`, `J=[4]\{j}`,

`Q_{I,J}=P_{ij}`

by complementary minors, while `sigma(I)=J` iff `sigma(i)=j`.

For `k=2`, the pairs `12` and `34` agree by Lemma 1 and complementarity. The only potentially unmatched pairs occur in the equal-coefficient groups

`a_{13^c}=a_{23^c}=alpha*delta`,
`a_{14^c}=a_{24^c}=alpha*gamma`.       (7)

For each target 2-set `J`, every permutation satisfies

`1_{sigma(13)=J}+1_{sigma(23)=J}
 = 1_{sigma(3) in J} - 1_{sigma(34)=J}`.       (8)

Taking `mu`-expectations gives

`Pr[sigma(13)=J]+Pr[sigma(23)=J]
 = sum_{j in J}P_{3j} - Q_{34,J}`.       (9)

On the compound-minor side, Cauchy–Binet applied to the two-column isometry `U[:,J]` gives the inclusion identity

`Q_{13,J}+Q_{23,J}+Q_{34,J}=sum_{j in J}P_{3j}`.       (10)

Therefore the right side of (9) is exactly `Q_{13,J}+Q_{23,J}`. The identical argument with row 4 gives

`Pr[sigma(14)=J]+Pr[sigma(24)=J]=Q_{14,J}+Q_{24,J}`.       (11)

Because (7) makes only these sums enter (1), every `k=2` contribution agrees. ∎

## Theorem — MOC4 holds whenever either matrix has a repeated eigenvalue

Under `a_1=a_2`, Lemmas 1–2 and (1)–(2) give the exact identity

`det(A+B) = E_mu [ prod_i (a_i+b_{sigma(i)}) ]`.       (12)

Thus `det(A+B)` is a convex combination of the 24 Marcus–de Oliveira permutation products. No invertibility was used, so zero eigenvalues and singular sums are included directly.

Any repeated eigenvalue of `A` can be moved to positions 1,2 by relabeling. If instead `B` has a repeated eigenvalue, swap `A` and `B`; the determinant is symmetric and the set of permutation products is unchanged after replacing `sigma` by `sigma^{-1}`. Hence the conclusion holds whenever either normal 4-by-4 matrix has a repeated eigenvalue. ∎

## Common reducing block boundary

Suppose `A` and `B` have a common nontrivial reducing subspace, so after one unitary change of basis

`A=A_1 direct_sum A_2`, `B=B_1 direct_sum B_2`,

with block sizes `r` and `4-r`. Then

`det(A+B)=det(A_1+B_1) det(A_2+B_2)`.

For each block, the lower-dimensional Marcus–de Oliveira conclusion (`n<=3`, a known input in the MOC4 source history) writes the block determinant as a convex combination of its local permutation products. Multiplying the two convex combinations gives a convex combination of the global 4-dimensional permutation products corresponding to permutations preserving the two blocks. Those are vertices in the full `S_4` hull. Therefore every common-reducing-block pair satisfies MOC4.

This block argument is recorded as a boundary reduction, not as a new proof of the known lower-dimensional theorem.

## Relation to the peer complementary-pair decomposition

`MOC4-C2-COMPLEMENT-BOUND-v1` shows that the general middle layer remembers an orientation/parity defect beyond complementary-pair transport. When `a_1=a_2`, the coefficient equalities (7) quotient out exactly the row-1/row-2 orientation distinctions that create that obstruction. Lemma 1 then couples the surviving pair law to the same one-minor matrix `P` by an actual probability measure on `S_4`. In this boundary regime the peer's unresolved joint-coupling step is therefore paid exactly, rather than bounded by an auxiliary parity slack.

## Status and remaining obligation

**ESSENTIAL_STEP_APPLIED:** the repeated-spectrum boundary and the common-reducing-block boundary are closed rigorously.

The unrestricted simple-spectrum, irreducible MOC4 case remains open. A next useful recipient should attempt to deform from the double-eigenvalue face while controlling the orientation/parity term, or show how the one-minor `P` layer absorbs the peer parity defect without relying on spectral equality.

No benchmark artifacts, held-out answers, private data, credentials, or unrelated material were used. Work proceeded `WITHOUT_VERIFIED_BRAIN`.
