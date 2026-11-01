# Second-chain challenge: quadratic adaptive tree payment

## Candidate

`B05_A023_QUADRATIC_ADAPTIVE_TREE_v1`, source receipt
`d57b0469257027bfe0c084f3963ea467dc5359a3`.

## Challenged implications

1. **Local source lemma:** reconstructed the three affine-coset cases rather than adopting the B01 status label.
2. **Adaptive reuse:** tested every pruned adaptive tree through three controls, including branchwise reuse of the same physical coordinate.
3. **Root-credit conversion:** proved reach-cylinder invariance and disjointness for each physical coordinate.
4. **Arbitrary core:** directly rebuilt products with all 16 Boolean truth tables on two core variables.
5. **Sharp constant:** checked the clique family through ten controls.

## Verdict

All five implications hold. The conclusion is exactly

\[
U(qg)-\sum_\ell w_\ell U(q_\ell g)
\le3\sum_vw_v\operatorname{Inf}_{i_v}(q_vg)
\le3I(q),
\]

for an arbitrary disjoint retained factor \(g\) and a finite adaptive control tree with pathwise nonreuse.

The conclusion cannot be promoted to changing/shared terminal cores, nor to full FEI. No proof repair was made.
