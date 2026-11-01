# B11 / A052 — payment of the complete singleton nonroot KL layer

**Status:** PROVED at the stated all-dimensional scope; independent review pending. Universal GU and full FEI remain OPEN.

## Frozen target

- Primary packet: **A052**.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim: `B11-A052-SINGLETON-KL-LAYER-v1`.
- Frozen pair: \((a,b)=(4,3/4)\).
- Prior endpoint: on positive-residual tensor-prime Boolean functions it remained to pay all nonempty KL rows together with \(\sum_i(B_i-\Gamma_i)\).

## New theorem

Let \(W_2=\sum_{|S|=2}p(S)\). For ordered \(i\ne j\), set
\[
m_{ij}=p(\{j\})+p(\{i,j\}),\qquad P_j=\pi(\{j\}),
\]
and
\[
V_1=\sum_{i\ne j}m_{ij}\log_2(P_j/m_{ij}).
\]
Then the entire singleton nonroot KL layer satisfies
\[
\boxed{K^{(1)}\le\frac12V_1+\frac{2}{\ln2}W_2.}
\]

The proof keeps the signed upper correlation inside the exact posterior. For the two genuine Boolean children \(f_{i,+},f_{i,-}\), singleton granularity gives
\[
|\widehat {f_{i,\pm}}(\{j\})|\le\operatorname{Inf}_j(f_{i,\pm}),
\]
which yields the rowwise KL estimate. No arbitrary spectral-law relaxation or unsigned-correlation replacement is used.

Combining this with the sharp root theorem gives
\[
\boxed{G\le D_{\ge2}+\frac12V_1+\frac{2}{\ln2}I,}
\]
where
\[
D_{\ge2}=\sum_i(B_i-\Gamma_i)+\sum_i\sum_{|A|\ge2}K_{i,A}.
\]
Thus every \(|A|=0\) and \(|A|=1\) KL row has been removed from the unpaid KL aggregate.

## Minimal-positive-residual consequence

If the frozen GU pair fails, a dimension-minimal positive-residual counterexample exists and has a tensor-prime positive-residual factor. Every proper child has nonpositive residual, hence
\[
\Delta_iG-\frac34\Delta_iU
\ge4\operatorname{Inf}_i(f)+R(f)
\]
at every relevant coordinate. This excludes the quadratic-phase curvature obstruction because that family has \(R<0\).

It is now sufficient, only on tensor-prime Boolean functions with \(R>0\), to prove
\[
\boxed{
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U.}
\]
This would imply \(G\le4I+3U/4\), then \(U\le16I\) and \(H\le34I\).

The remaining KL obligation begins at derivative order two. The explicit \(V_1/2\) term remains unpaid; no dimension-free bound for it is asserted.

## Verification

The checker reconstructs every signed KL row from Walsh coefficients and upper-set masses. It exhausts all Boolean signs modulo global output sign through dimension four and adds seeded dimension-five and dimension-six controls. It verifies the row theorem, the sharp root payment, and the complete displayed reduction.

## Next action

Use the minimal-child residual inequalities to test whether the signed term \(\sum(B_i-\Gamma_i)\) absorbs \(V_1/2\) on positive-residual sources. Only after that should the \(|A|=2\) KL layer be expanded.
