# Second-chain challenge

## Chain separated

1. **Finite truth-table claim:** accepted independently.
2. **Inference `a+b>2.974`:** accepted because this witness has `U=I=5`.
3. **General bent-fiber pattern:** accepted only after adding
   `s=rank(M)=m-2`; original broader wording is refuted.
4. **“Near sharpness” of 3:** not a theorem because `G<=3I` remains open.
5. **Full FEI:** no implication; remains open.

## Hard regimes selected

* Direct character sums replaced the author's FWHT implementation.
* Every physical coordinate was edge-counted independently.
* All twenty restrictions were reconstructed without using the archived
  support data.
* The witness's algebraic degree was computed to exclude accidental coverage
  by the quadratic theorem.
* Extra dependent nonzero shield rows were tested as the minimal embedding
  most likely to break the extracted general statement.

## Exact scope falsifier

Take `m=3`, `s=2`, and duplicate binary rows `111,111`. Let

\[
 P(x_1,x_2,y)=(-1)^{(x_1+x_2)(y_1+y_2+y_3)+y_1y_2}.
\]

The matrix has rank `1=m-2`; every row and column is nonzero; and on each
kernel coset the core is a two-bit bent phase. Nevertheless its Walsh support
has 16 of 32 points with magnitude 8, so it is not bent. Exact reconstruction
gives `H=4`, `U=2`, and `I=5/2`, contradicting `U=I=m-1=2`.

