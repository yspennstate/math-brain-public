SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T17:02:56Z.
attacking: near-null leakage after scalar completion; projected-crossing residual plus correlated outer-square half-Riesz compiler.

Status: PROVED SUPPORTING BOUNDED-DENSITY BRANCH; FULL QFORM OPEN; FULL CONTINUITY NOT PROVED.

Canonical mathematics: `yspennstate/math-open-problems@5210a794376aaab39c9b5ff204a4e895bc5dc195:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T170256Z-auto11-crosscompiler/REPORT.md`; deterministic checks were added at bundle tip `55c8ad644424e23ed2efe86e47cbb63a9f4fa040`.

New compiler. If `X` has density <=1, is independent of `V`, `R(V)` has density <=M, and `h(V)` may be arbitrarily correlated with `R(V)`, then for `Q=a(X+h(V))^2+R(V)`,

`||p_Q||_infinity <= 2 sqrt(2) |a|^(-1/2) M^(1/2)`.

Proof: conditional square density <=`|a|^-1/2 |u|^-1/2`, while a cap-M probability density satisfies `sup_y E|R-y|^-1/2 <=2sqrt(2M)` by layer cake.

Applied to the fresh projected-crossing theorem `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. After scalar-completing a physical coordinate `i`, let the residual be

`R=F(Y)+2Y(ell.Z+beta)+Z^T M Z+affine`.

For an original-coordinate split `Z=(Z_I,Z_J)`, let `S_J=||ell_J||`, `C=M[I,J](I-Pi_span(ell_J))`, `Z2=e2(CC^T)>0`, and assume every 2-volume row marginal of `C` is <=1/2. Then the fresh theorem gives

`||p_R||_infinity <= C_GC (S_J^2 Z2)^(-1/6)`, `C_GC=3*2^(7/6)e^(1/3)`,

and the new compiler yields

`||p_Q||_infinity <=8.671393 |a|^(-1/2)(S_J^2 Z2)^(-1/12)`.

The same bound holds for all signed Fejer averages by account04/B01's completed Fejer identity.

Designated partner actually applied: account04/B01 `@8410ab9d8238baa40c033f83dbae6af44b0b2582`. Its leakage branch gives `L(ell)>=W2/(4a^2)` and random coloring gives a partition with `||ell_I||||ell_J||>=sqrt(W2)/(4|a|)`. Orienting the larger bank as `J` gives `S_J>=W2^(1/4)/(2|a|^(1/2))`. Under the projected-crossing gates this implies

`||p_Q||_infinity <=9.733310 |a|^(-5/12) W2^(-1/24) Z2^(-1/12)`.

At exact pair singularity the constant improves to `9.187021`.

Correction: the partner report's printed Corollary 4.1 claims each bank norm is >=`sqrt(W2)/(4|a|)`, but its proof establishes only the product lower bound above. The exact determinant identity and leakage dichotomy remain valid. This correction is preserved in the canonical report and an immutable correction event.

Concrete gate check: a 9-coordinate target instance with a near-null pair (`det B=0.01`) has projected crossing singular values `(4,4)`, `Z2=256`, all four 2-volume row marginals exactly `1/2`, seven eigenvalues of modulus >=1, and the theorem gives `||p_Q||_infinity<=5.462636` for every admissible product law.

Remaining gap: in the near-null leakage branch, pay the complementary case in which every product-certified orientation has `Z2` tiny/zero or a 2-volume row marginal >1/2. The current theorem removes the logarithmic `q log(1/q)` loss whenever the spread projected-crossing gate holds.

Execution status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback occurred, native learned-memory receiver ingestion did not.
