# PROB10-01 idea before code: entropy-debiased endpoint banks and monotone scale switching

Full Friedgut--Kalai FEI remains OPEN. This note fixes the new mathematics and the precise gap before any checker is persisted.

Let `H_n(f)` be Shannon Fourier entropy in bits and

`Phi_{n,lambda}(f)=(n/lambda)(sum_S |fhat(S)|^(2-lambda/n)-1)`, `0<lambda<=1`,

with the already proved uniform endpoint inequality

`(ln 2/2) H_n(f) <= Phi_{n,lambda}(f) <= H_n(f)/2`.

Write `c=ln(2)/2` and define the nonnegative endpoint defect

`G_{n,lambda}(f)=Phi_{n,lambda}(f)-c H_n(f) >= 0`,

with `G_{0,lambda}=0`; every one-bit Boolean function also has `G_{1,lambda}=0`.

For a nonempty proper physical block `A`, let

`B_A(f)=H(S_A | S_{A^c})`,

`Delta_A G_lambda = G_{n,lambda}(f)-2^(-|A|) sum_a G_{n-|A|,lambda}(f_{A=a})`,

and

`Q_{A,lambda}(f)=B_A(f)+Delta_A G_lambda`.

The first target is an exact compiler: if every state has a proper block with `Q_{A,lambda}<=K I_A` for one fixed lambda, then full FEI follows with coefficient `2K`. This is strictly easier locally than the preceding hybrid `B_A+Delta_A Phi`, because

`Q_{A,lambda}=B_A+Delta_A Phi_lambda-c Delta_A H`.

The second target removes the fixed-lambda rigidity. The scalar map `lambda -> G_{n,lambda}(f)` is increasing. Therefore on an adaptive restriction tree, if the chosen endpoint scales are nondecreasing down every root-to-leaf path, the variable-scale defect drops have a nonnegative total after summation by parts. Hence a local paid selector may increase its endpoint scale as information is revealed without losing the global budget. This is a genuinely adaptive dependent-branch compiler; no sibling independence or fresh control is introduced.

The third target is the tangent bank. Expanding at `lambda=0`, with `p_S=fhat(S)^2` and `X_S=-ln p_S`, gives

`G_{n,lambda}(f)=lambda V_n(f)+O(lambda^2)`,

`V_n(f)=(1/(8n)) sum_S p_S X_S^2 >=0`.

Thus `V_n` itself is a nonnegative all-dimensional bank, and more generally the full endpoint defect is a positive series of normalized log-spectrum moments. These banks can be used with monotone nonnegative multipliers by the same tree summation-by-parts argument.

Three materially different attacks in this run:

1. prove the entropy-debiased fixed-scale compiler and sharpen the existing character-child payment;
2. prove monotone adaptive-scale switching by an exact tree integration-by-parts identity;
3. derive the log-spectrum moment bank and test whether adaptive scale choice improves the local selector on exhaustive small cubes and the archived stress families.

Precise remaining gap: prove one universal finite `K` and a hereditary rule assigning, at every nontrivial Boolean state, a nonempty proper physical block `A` and a scale `lambda` that never decreases along descendants, such that `Q_{A,lambda}<=K I_A`; or produce an all-dimensional Boolean obstruction to every such monotone-scale policy. Finite checking cannot settle that quantifier.

The archived coded `F_8` has 2,040 physical inputs; no truth-table enumeration or compressed new bank certificate is assumed for it.
