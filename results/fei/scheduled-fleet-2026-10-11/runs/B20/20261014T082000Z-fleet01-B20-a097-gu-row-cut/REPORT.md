# B20 / A097 — source-bound GU row cut and failed cross-route transfers

**Status:** the all-dimensional reduction below is proved from source-complete inputs and independently rechecked here. Universal GU and full FEI remain **OPEN**. Independent end-to-end review remains pending.

## Frozen target

- Primary packet: **A097 (cross-route transfer)**.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim: `B20-A097-GU-ROW-CUT-v1`.
- Frozen pair: \((a,b)=(4,3/4)\).
- Required universal conclusion: \(G(f)\le4I(f)+3U(f)/4\) for every genuine Boolean function on every finite uniform cube.

## Mathematical assembly

The new B11 singleton theorem was reconstructed from its complete proof. Its genuinely Boolean step is valid: for each restricted child \(g=f_{i,\pm}\),
\[
|\widehat g(\{j\})|\le \operatorname{Inf}_j(g),
\]
and this is applied before discarding the signed upper-set posterior. Together with the previously sharp root theorem it yields
\[
\boxed{G\le D_{\ge2}+\frac12V_1+\frac{2}{\ln2}I,}
\]
where
\[
D_{\ge2}=\sum_i(B_i-\Gamma_i)+\sum_i\sum_{|A|\ge2}K_{i,A},
\]
\[
V_1=\sum_{i\ne j}\bigl(p_j+p_{ij}\bigr)
\log_2\frac{\pi_j}{p_j+p_{ij}}.
\]
Hence the exact smaller unpaid GU leaf is
\[
\boxed{
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U}
\tag{GU-cut}
\]
only on tensor-prime positive-residual sources. This implies universal \(G\le4I+3U/4\), then \(U\le16I\), and the audited reduction gives \(H\le34I\).

Every root and singleton KL row is now removed from the unpaid KL aggregate. The remaining KL rows start at \(|A|=2\); \(V_1/2\) remains explicit.

## Minimal-counterexample condition

For a dimension-minimal positive-residual counterexample, every relevant coordinate satisfies
\[
\Delta_iG-\frac34\Delta_iU
\ge4\operatorname{Inf}_i(f)+R_{4,3/4}(f).
\]
This is a valid structural input to (GU-cut), not a proof of it.

## Invalidated transfers

1. **Direct \(U\)-payment is false.** Exhaustive four-bit computation finds a genuine Boolean witness with \(U=1/4\), \(V_1=7/4\). Thus even \(V_1/2\le U\) fails. The witness has negative frozen residual, so the restricted positive-residual leaf remains viable.
2. **Adaptive single-use does not yet pay the static singleton layer.** B07's theorem controls root rows along one read-once physical tree. The sum defining \(K^{(1)}\) contains all incompatible ordered first-query pairs at one parent. No proved transport converts that static sum into one nonreused tree while retaining terminal terms.
3. **A099 remains a separate FEI route.** Its amplified-extension functional has no proved algebraic identification with \(V_1\) or \(D_{\ge2}\), and its critical-profile conclusion does not itself imply universal GU.

These are dependency invalidations, not disproofs of GU or FEI.

## Verification

`verify_gu_row_cut.py` exhausts all 32,906 Boolean signs modulo global output sign through dimension four. It reconstructs all signed KL rows, verifies the root and singleton inequalities and the complete displayed reduction, and isolates the exact four-bit failed-transfer witness.

## Next action

Use the minimal-child residual inequalities coordinate-by-coordinate to test whether the signed term \(\sum_i(B_i-\Gamma_i)\) absorbs the reuse functional \(V_1/2\) on positive-residual sources. Do not expand the \(|A|=2\) KL layer until that signed absorption is resolved.

## Status distinctions

This run is researched and locally saved. Canonical and mirror persistence/readback receipts are recorded separately after the immutable writes. It is not independently reviewed, natively ingested, or publicly released.
