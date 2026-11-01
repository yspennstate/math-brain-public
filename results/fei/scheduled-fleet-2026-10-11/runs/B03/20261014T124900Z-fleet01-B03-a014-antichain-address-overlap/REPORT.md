# B03 / A014 — arbitrary-depth antichain addressing with unbounded physical reuse

**Status:** proved restricted GU theorem, pending independent review. **Universal GU and full FEI remain open.**

## Frozen candidate

- Packet: **A014**.
- Attempt: `A014-ANTICHAIN-ADDRESS-OVERLAP-1`.
- Stable gap: `GU-COHERENT-UPPER-SET-OVERLAP`.
- Claim: `B03-A014-ANTICHAIN-ADDRESS-OVERLAP-v1`.
- Pair: `(a,b)=(1,0)` on the stated class.

Prior work gave the exact binary nonparallel-character collision and the sharper class constant `1/5`, but did not cover multiway collision or unbounded selector depth. The frozen candidate was that arbitrary-depth addressing among parity branches with antichain supports admits a complete signed cost independent of overlap congestion.

## Result

For a genuine Boolean selector

\[
F(Y,x)=\chi_C(x)\chi_{A_Y}(x),\qquad Y\in\{-1,1\}^k,
\]

where the `2^k` branch supports `A_z` form an arbitrary antichain and may reuse physical coordinates without any congestion bound, define

\[
d_i(z)=\#\{w:A_z\setminus\{i\}\subseteq A_w\setminus\{i\}\}.
\]

Exact Boolean upper-set accounting gives

\[
U=\frac k2,
\quad I=|C|+\frac k2+2^{-k}\sum_z|A_z|,
\quad
\boxed{G=\frac k2-2^{-k}\sum_{i,z}\log_2d_i(z)}.
\]

Every selector contributes exactly `1/2`; common coordinates contribute zero; every restriction-induced coherent containment contributes the negative refund `-2^{-k} sum_z log2 d_i(z)`. Therefore

\[
\boxed{G\le k/2\le I}.
\]

This supplies the uniform restricted GU pair `(1,0)` with no arity, depth, dimension, overlap, or reuse loss. It includes four-way and higher addressing collisions, not only orthogonal or disjoint branch supports.

## Verification

`verify_antichain_address.py` reconstructs the genuine Boolean truth tables, Walsh spectra, every physical restriction, `U`, `I`, and `G`. It checked 429 antichain families for selector depths `k=1,2,3`, including heavily reused middle-layer supports, with 4,797 assertions. Maximum errors at 90-digit Decimal precision were `4e-90` for `U` and `1.3e-88` for `G`. Seed: `20261014`.

The computation validates the formulas; the proof is analytic for all finite `k` and all finite antichains.

## Exact implication and remaining gap

The theorem is a direct all-parameter restricted instance of `G<=aI+bU`. It removes coherent upper-set overlap caused solely by restrictions of arbitrarily reused parity branches: that overlap is favorable in the signed aggregate.

It does **not** establish universal GU. Comparable initial branch rows and noncharacter branch spectra can merge Fourier amplitudes after restriction; then containment multiplicities alone no longer determine the posterior. The next action is to analyze the smallest genuine two-frequency branch row where one reused coordinate causes an actual signed coefficient merger, retaining its terminal and normalization terms.

Model/effort metadata: `UNKNOWN`.
