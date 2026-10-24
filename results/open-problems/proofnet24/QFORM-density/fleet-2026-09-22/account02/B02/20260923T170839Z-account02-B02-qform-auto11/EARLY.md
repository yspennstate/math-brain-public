SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T17:08:39Z.
attacking: the singular-second-anchor concentrated-E2 / fixed-scale-strip survivor by compiling scalar Schur E2 mass back into a physical one-hub third-volume packet before applying an integrated-Fourier receiver.

# Early checkpoint — scalar Schur E2 is dominated by a physical one-hub 3-volume

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Target-wide universal unweighted `int |phi_Q|` remains OPEN / not refuted.

Fresh source actually used: the grouped projected-crossing theorem `GC` at `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`; latest completed designated partner `account03/B02` r34 is `a31a7a4773212dfdd2fd1098fbc6efddc3190b64`. I also independently checked the row-promotion algebra in the fresh account01/B03 one-hub compiler `4b7608c198ea570378ae30b5a22d63ba7d387534` before using its stated constant below.

## 1. Deterministic lift

Let an ORIGINAL-coordinate physical cross block, after row/column reordering, be

`B = [[p, r^T],
      [c, N]]`,

where the scalar physical edge `p!=0`, the first row is a genuine original coordinate `h`, the first column is a genuine original coordinate `j`, and the remaining row and column banks are disjoint original-coordinate banks `I,J`. Define the algebraic scalar cross-Schur residual

`S = N - c r^T/p`

and the scalar-Schur second-volume packet

`H = p^2 E2(S)`.

No random-variable shear is made: S is used only as a coefficient identity.

Let the full physical hub row on the column bank `{j} union J` be

`m=(p,r^T)`,

and for every residual physical row i let

`a_i=(c_i,N_i)`.

Define the physical one-hub aggregate third-volume

`V3 = sum_(i<k in I) |m wedge a_i wedge a_k|^2`.

For each i perform only the algebraic row operation

`a_i' = a_i - (c_i/p)m = (0,S_i)`.

Since wedging with m is invariant under adding multiples of m,

`m wedge a_i wedge a_k = m wedge a_i' wedge a_k'`.

By Cauchy-Binet, for every pair i<k the squared three-volume is the sum of squared 3x3 coordinate minors. Keeping only the triples that contain the pivot column j gives

`|m wedge a_i wedge a_k|^2
 >= sum_(T subset J, |T|=2)
      det([m;a_i';a_k']_[{j} union T])^2
 = p^2 sum_(|T|=2) det(S[{i,k},T])^2`.

Summing over i<k yields the exact monotonicity

`boxed: V3 >= p^2 E2(S) = H.`

This is source-coordinate exterior algebra. It does not infer independence after Schur completion and it does not select a reciprocal small minor.

## 2. Fourier consequence from the physical one-hub compiler

The fresh row-marginal-free one-hub two-volume theorem (account01/B03 r29, itself built from the reviewed projected-crossing source plus literal-row promotion) states that every physical packet `V3>0` of the form above gives a continuous C0 density with

`||p_Q||_infinity <= C_hub V3^(-1/6)`,

`C_hub = 3*2^(7/6)*exp(1/3) = 9.39913188784886...`,

for arbitrary same-bank quadratic terms, arbitrary outside couplings after conditioning, and arbitrary affine terms. Its proof supplies an actual integrable characteristic-function envelope, not a law-uniform scalar pointwise decay assertion.

Therefore the deterministic lift gives the new scalar-Schur receiver

`boxed:
 H=p^2 E2(S)>0
 => ||p_Q||_infinity <= C_hub H^(-1/6),
    phi_Q in L1(R).`

This removes every row/column E2-marginal gate and every stable-rank gate from the nonzero scalar-anchor branch.

## 3. Immediate application to the live rank-one second-anchor branch

The preceding B02 / account03-B02 double-anchor algebra established that if a physical 2x2 second anchor has rank one and its incident third-volume packet is `G3`, then choosing any genuinely nonzero scalar entry p of that anchor produces an actual scalar-Schur packet with

`H=p^2 E2(S) >= G3`.

Hence

`boxed: ||p_Q||_infinity <= C_hub G3^(-1/6).`

In particular, on the designated partner's r33/r34 packet `G3>Z/864`,

`boxed: ||p_Q||_infinity < 29.007260 Z^(-1/6),`

with `phi_Q in L1`, so the density is continuous and vanishes at infinity.

This pays the previously surviving **singular/rank-one second-anchor concentrated-E2 collar**. The literal strip alternatives U,V from account03/B02 r33 remain separate because their individual factors can cancel inside the corresponding 3x3 determinant; no false implication `U or V => G3` is made.
