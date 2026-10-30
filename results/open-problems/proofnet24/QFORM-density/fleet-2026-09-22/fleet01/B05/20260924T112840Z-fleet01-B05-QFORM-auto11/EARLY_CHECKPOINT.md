SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-24T11:28:40Z.
attacking: QFORM-PAIR-L3-SHARED-CARRIER-GLUE-v1 — derive a product-preserving coarea estimate for a fully coupled physical triple, so the third carrier may share original-coordinate sources after Schur completion.

# Early calculation — direct physical-triple near/far coarea

Let `B` be any invertible real symmetric `3x3` matrix and `q(x)=x^T Bx` in three ORIGINAL independent coordinates with cap-one probability densities. Put `Delta=|det B|`.

A direct small-ball split appears to give a determinant-scale theorem with a much smaller constant than the existing physical-triple receiver and without any independent-square hypothesis.

For an interval `I` of length `eps`, split at `R>0` by the Euclidean gradient `|grad q|`.

**Near-gradient part.** Since the joint product density is <=1, discard it. With `y=grad q=2Bx`, `dx=dy/(8 Delta)` and `q=(1/4)y^T B^{-1}y`. For any invertible symmetric `C` and Euclidean ball `B_R`, the pushforward of Lebesgue measure on `B_R` by `y^T C y` has density bounded by

`16 R |det C|^(-1/3)`.

Proof: rotate `C` to `diag(lambda_1,lambda_2,lambda_3)` (the ball is rotation invariant), dominate the ball by `[-R,R]^3`, and use the three one-dimensional signed-square pushforwards. Each has `L^(3/2)` norm exactly `2^(4/3) R^(1/3)|lambda_j|^(-1/3)`, so three-fold Young gives `16R|det C|^(-1/3)`.

For `C=(1/4)B^{-1}`, this gives

`P(q in I, |grad q|<=R) <= 8 eps R Delta^(-2/3)`.

**Far-gradient part.** If `|grad q|>R`, some physical derivative satisfies `|partial_k q|>R/sqrt(3)`. Conditioning the other two ORIGINAL variables, the restriction of `q` to `x_k` is a one-variable quadratic. On the subset where `|q'|>L`, the preimage of an interval of length `eps` has Lebesgue measure at most `2eps/L` (at most two monotone branches). Since the conditioned density is <=1,

`P(q in I, |grad q|>R) <= 6 sqrt(3) eps / R`.

Hence

`P(q in I) <= eps [8 R Delta^(-2/3)+6sqrt(3)/R]`.

Optimizing at `R=sqrt(3sqrt(3)/4) Delta^(1/3)` gives

`P(q in I) <= C0 eps Delta^(-1/3)`,
`C0=2 sqrt(48 sqrt(3))=18.2360564556...`.

This already closes the shared-carrier issue for any literal nonsingular physical triple: arbitrary pair/carrier cross terms are allowed, no Schur-completed independence is needed. Affine terms are removed by translating the three original variables. The remaining work this run is to audit every step, extend to arbitrary density caps, prove the continuous-density conclusion by smooth approximation, compare against the pre-existing `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`, and isolate the aggregate-before-inversion obstruction that remains when all physical triple determinants are tiny.
