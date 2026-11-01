# Root lead — a frame-pair form of the scalar rank-three Fisher gap

Status update: the pair identity below is exact, but X032 has derived a rigorous near-parallel-frame counterexample to the unrestricted FIRST proposed Fisher inequality. Consult agents/X032.md for its current proof status and adaptive joint compensation. The first inequality must not be assumed or assigned as a universal target. X028 proves it under the row bound R≤2. Root derivation, not an additional sub-agent.

For a rank-three Parseval frame write its nonzero rows as sqrt(t_i)n_i*, with unit n_i and sum_i t_i n_i n_i*=I_3. Put x_i=n_i* A n_i, a_ij=n_i* A n_j, lambda_ij=|n_i*n_j|^2 and c_ij=-log(1-lambda_ij) for independent pairs. If W is X004/X008's entropy-weighted second-exterior operator, then

    tr(W adj A)=sum_{i<j} t_i t_j c_ij [x_i x_j-|a_ij|^2].

Proof: the corresponding pair effect is the Hodge dual of the two frame rows. Its pairing with adj A is det(V_{ij} A V_{ij}*), equal to the displayed bracket times t_i t_j. The coefficient is the pair log Gram ratio. Dependent pairs have zero determinant identically and are omitted; their limiting c times squared volume is zero in the original W definition.

Thus X016's first stronger scalar sufficient conjecture is the explicit inequality

    sum_i t_i x_i^2 >= sum_{i<j} t_i t_j [-log(1-lambda_ij)]
                                      [x_i x_j-|a_ij|^2]

for every Hermitian A. The overlaps form a reversible Markov matrix P_ij=t_j lambda_ij, since sum_j t_j lambda_ij=1; its stationary measure is t_i/3. This gives a possible entropy/Markov interpretation, but a generic spectral-gap or scalar Jensen inequality has not been shown to prove the displayed quadratic form. Signed terms and complex interference must remain.

Together with the distinct second-exterior inequality

    F_w(A)>=tr((W+tau I)adj A),

this would settle every scalar active base, with -H''>=(1-2s(1-s))FI>=FI/2, because

    tr((W+s tau I)adj A)
      <=(1-s)F_v(A)+sF_w(A)=s(1-s)FI.

The second inequality is not automatically the first applied to the pair frame: its entropy operator and its triple law need an actual identification. This was the original proposed route. The first universal inequality is now contradicted by X032's example; a JOINT compensation using both measurement layers is the appropriate replacement target. The second inequality remains unproved in general.
