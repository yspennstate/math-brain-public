# Source-bound FEI handoff — account02/B18 — 2026-09-22T05:11:05Z

**Status:** full unrestricted FEI remains OPEN / NOT PROVED.

**Control read:** OWNER CONTROL revision `2026-09-22.2`; later all-gate target supersedes the older half-band Campaign-C compiler assignment.

**Scientific source:** `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T051105Z-random-depth-barycenter/REPORT.md`, creation commit `3f228a8a91559bbc354d207baf74d6c88a68996f`.

## Exact correction

The previous B18 criterion `exists 1<=r<n: B_r^RO+a_*Q_r>=0` does not qualify as a smaller implication: at `r=n-1`, all restriction children are constants/literals, hence `F_{n-1}^RO=P_{n-1}=0` and

\[
B_{n-1}^{RO}+a_*Q_{n-1}=D_{\Gamma_*}(G).
\]

So the terminal scale is the full target itself.  Preserve the random-block identities, but do not present that existential range as reduction.

## New exact signed net

For the random physical reveal chain define

\[
L_r^{RO}=F_r^{RO}-F_{r+1}^{RO},\qquad
\Delta_r=P_r-P_{r+1}>0\quad(0\le r\le n-2),
\]

and

\[
\lambda_r=-L_r^{RO}/\Delta_r,\qquad w_r=\Delta_r/P_0.
\]

Then

\[
-\frac{D_{\Gamma_{RO}}(G)}{P_0}=\sum_{r=0}^{n-2}w_r\lambda_r,
\qquad
D_{\Gamma_*}(G)=\sum_{r=0}^{n-2}\Delta_r(a_*-\lambda_r),
\]

with

\[
w_r=\frac{\sum_{k\ge2}kW_k[1-(r)_{k-1}/(n-1)_{k-1}]}
{n\sum_{k\ge2}(k-1)W_k}.
\]

Applying account03/B14's exact singleton restriction cocycle gives the authentic signed step

\[
\ell_{RO}(H,j)=E_Z\Gamma_{RO}(p_{out}(H_Z))-\Gamma_{RO}(p_{out}(H))
+\frac{It_j}{V_{p_j}}[\Gamma_{RO}(p_j)+h_2(V_{p_j})]
-I(Z;S)-H(K|S),
\]

and `L_r^RO=E ell_RO`.  Both negative information terms, the physical leaf normalization, multiplicity and terminal cancellation are retained.

## Applied peer result

Account03/B13 `20260922T043158Z-balanced-six-two-generation` proves `D_{Gamma_*}>0.020451553271865` on the balanced six-bit zero-singleton nonliteral-child slice.  Since `P_0<=(6-1)/4=5/4`, the new barycenter there obeys

\[
\sum_r w_r\lambda_r<0.251843557382508<a_*=0.2682048.
\]

## Remaining obligation

A pointwise bound on every `lambda_r` is not viable; the completed bent-swap work already gives unbounded local requests.  The next universal step must be an amortized two-generation/adaptive-depth compensation theorem that uses actual child defect to pay above-`a_*` local requests.  Do not drop child slack, `I(Z;S)`, or `H(K|S)`, and do not reintroduce the terminal-tautological existential criterion.
