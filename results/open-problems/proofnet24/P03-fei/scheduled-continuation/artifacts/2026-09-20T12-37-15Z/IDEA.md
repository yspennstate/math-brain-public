# PROB10-01 idea before checker: hybrid allocation plus adaptive endpoint rebate

Full Friedgut--Kalai FEI remains OPEN. This note fixes the mathematical target before the substantive checker source is persisted.

Let `f:F_2^n->{-1,1}` and let `S` have squared Fourier law. For a nonempty physical block `A subsetneq [n]`, write

`B_A(f)=H(S_A | S_{A^c})`.

Use the already proved dimension-adaptive endpoint potential

`Phi_n(f)=n(sum_T |fhat(T)|^(2-1/n)-1)`, with `Phi_0=0`,

and define the block endpoint charge

`A_A(f)=Phi_n(f)-2^(-|A|) sum_a Phi_(n-|A|)(f_{A=a})`.

The new quantity to test is

`C_A(f)=B_A(f)+A_A(f)`.

The reason for adding, rather than separately paying, these terms is exact. The current arbitrary-block Walsh theorem gives `H(f)<=2 R_blk(T)` for every full adaptive physical block tree, where `R_blk=sum_v w_v B_{A_v}(f_v)`. The endpoint charges telescope on the same tree to `Phi_n(f)`. Physical block influences also telescope exactly:

`I(f)=sum_v w_v I_{A_v}(f_v)`, `I_A=sum_{i in A} Inf_i`,

because conditioning the other queried coordinates preserves each remaining edge boundary on average.

Therefore a universal hereditary selector

`for every nonconstant state f of dimension >=2, there exists a nonempty proper physical block A with B_A(f)+A_A(f) <= K I_A(f)`

would give

`R_blk(T)+Phi_n(f)<=K I(f)`.

Since the proved endpoint proxy has `Phi_n(f)>=(ln 2/2) H(f)` and block recombination gives `H(f)<=2R_blk(T)`, this would imply

`(1+ln 2) H(f) <= 2 K I(f)`,

hence full FEI with coefficient `2K/(1+ln 2)`.

This does not use a pointwise erasure converse, does not replace dependent children by independent samples, and does not revive any retired resolvent/drift/overlap target. The all-coordinate form is already impossible: the current padded bent-background endpoint theorem has a relevant coordinate with `A_i/j_i -> infinity`, and `B_i>=0`. Only the existential selector is live.

Three attacks for this bounded continuation:

1. **Hybrid singleton selector.** Test `B_i+A_i` instead of either `B_i` or `A_i` alone. The endpoint rebate can be negative on majority/addressing-type splits while `B_i` is the true hereditary allocation.
2. **Proper-block selector.** Use the new arbitrary-block Walsh recombination theorem and exact block influence budget; multi-coordinate blocks may lower the local hybrid ratio when no singleton is attractive.
3. **Aggregate / obstruction stress.** Test whether the padded bent-marker obstruction that kills every-coordinate endpoint payment also kills existence after adding true allocation, and compare one-point, addressing, bent/quadratic, tensor, majority-substitution and fresh-control families. The archived coded `F_8` has 2,040 inputs, so its new hybrid selector cannot be truth-table enumerated in a bounded run; no compressed hybrid certificate is assumed.

Precise remaining gap after any finite test: prove the universal existential proper-block inequality above, or produce an all-dimensional Boolean family on which every nonempty proper block has `(B_A+A_A)/I_A -> infinity`. Finite checks cannot settle that quantifier.
