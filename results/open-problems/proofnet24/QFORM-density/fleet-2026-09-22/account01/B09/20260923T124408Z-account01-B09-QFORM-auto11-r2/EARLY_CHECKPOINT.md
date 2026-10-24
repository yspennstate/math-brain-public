# Early substantive checkpoint — aggregate singleton volume to one disjoint physical cut

Run `20260923T124408Z-account01-B09-QFORM-auto11-r2`.

Work in an exact two-physical-hub packet. Let `H={h1,h2}`, let `L` be the leaf coordinates, write `C=A[L,H]`, `D=A[L,L]`. For each leaf `k`, form the singleton-augmented cross matrix

`M^(k)=[ C_(L\{k}), D_(L\{k},k) ]`,

whose three columns are the two original hub columns plus the promoted physical leaf `k`. Put

`Gamma_k^2 = det((M^(k))^T M^(k))`

(with value zero when the rank is below three), and `S=sum_k Gamma_k^2`.

For a physical bipartition `L=I disjoint_union K`, the actual original-coordinate cross cut `I | (H union K)` has matrix

`B_(I,K)=[C_I, D_(I,K)]`.

Restrict its 3x3 minors to column triples `{h1,h2,k}`, `k in K`, and row triples `T subset I`. Define

`Z_(I,K)=sum_(k in K) sum_(T subset I, |T|=3) det B[T,{h1,h2,k}]^2`.

If each leaf is independently put in `I` or `K` with probability `1/2`, then every singleton-augmentation minor contributing to `Gamma_k^2` survives exactly when `k in K` and its three row leaves lie in `I`, an event of probability `2^-4=1/16`. Therefore the exact identity is

`E Z_(I,K) = S/16`.

Hence a deterministic physical partition exists with

`Z_(I,K) >= S/16`.

This is the first essential bridge from account03/B09's aggregate singleton defect `sum Gamma_k^2` to one fixed disjoint original-coordinate bilinear cut. It does not rotate any random coordinates and does not discard the same-bank curvature.

The first remaining analytic gate is the row-marginal condition in the fractional three-volume Fourier theorem. For the determinant law restricted to the minors above, either all row inclusion marginals are at most `2/3`, in which case the q=4/3 fractional-volume estimate will pay the cut directly, or one literal row carries more than two thirds of this restricted determinant mass. The latter is a localized physical high-volume-row branch, not a failure of the identity above.
