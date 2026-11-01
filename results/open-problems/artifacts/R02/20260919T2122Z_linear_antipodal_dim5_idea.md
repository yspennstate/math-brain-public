# R02 idea before archive checker — linear antipodal codes collapse to a 16-point Walsh signing problem

The current explicit sign-matrix lower bound is supplied by the nonlinear order-17 witness with discrepancy 7. A natural structurally different route to a new witness is a complement-closed **linear** covering code: if a binary linear code `C <= F_2^n` contains the all-one word, has `|C| <= 2n`, and covering radius `R`, then choosing one representative from each antipodal pair in `C` and duplicating rows if necessary gives an `n x n` sign matrix with discrepancy `n-2R`.

For `17 <= n <= 31`, any such linear code has dimension at most five, because `|C| <= 2n < 64`. Choose a basis whose first generator is the all-one word. The other at most four generator coordinates identify every coordinate position `j` with a point `x_j in F_2^4`. Thus every codeword is an affine character on the multiset `(x_j)`.

Let `m_x` be the multiplicity of `x in F_2^4`. For a target sign word, let `q_x` be the signed sum inside the coordinates of type `x`. We can force

- `q_x = 0` whenever `m_x` is even;
- `q_x in {+1,-1}` whenever `m_x` is odd.

Hence only the parity support `O={x:m_x odd}` remains. Its cardinality has the same parity as `n`. For an affine character indexed by `a in F_2^4`, the correlation with the target is the Walsh coefficient

`sum_{x in O} q_x (-1)^{a.x}`.

So the linear-code route is killed if the following finite 16-point lemma is true:

- every even support `O subset F_2^4` admits signs with every Walsh coefficient at most 6 in absolute value;
- every odd support admits signs with every Walsh coefficient at most 5 in absolute value.

If certified exactly, this gives a target word at distance at least `(n-6)/2` for even `n` and `(n-5)/2` for odd `n`. Therefore every complement-closed binary linear code of dimension at most five has covering radius at least those values, and its associated sign-matrix discrepancy is at most 6 for even `n` and at most 5 for odd `n`.

In particular, no linear antipodal code can match the existing discrepancy-7 witness at any odd order `17..31`, and no linear antipodal code can improve the normalized R02 bound at any order `17..31`.

The next step is an exact exhaustive checker of all `2^16=65536` supports. For each support it may quotient global sign, Gray-enumerate signings, and stop as soon as it finds the relevant threshold certificate. This is a finite-core check, not a source closure claim or a novelty certificate.
