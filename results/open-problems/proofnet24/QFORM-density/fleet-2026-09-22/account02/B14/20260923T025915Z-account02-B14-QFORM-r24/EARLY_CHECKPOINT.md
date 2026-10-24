# account02/B14 r24 early substantive checkpoint

Status: supporting calculation; full QFORM remains open.

## Conditioning-order obstruction for Claude's D5 theorem

Use the completed D5 theorem from `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`:

For a physical cross block `M` with `Z_5=e_5(M^T M)>0`, arbitrary self blocks and affine terms,

`||p_Q||_infty <= 5 sqrt(2e) Z_5^(-1/10)`.

Let `E_N=union_{j=1}^N [4^j,4^j+1/N]` and let `X,X'` be iid uniform on `E_N`. Put `U=X-X'`, `V=X+X'`, and `m_N(u)=|E_N intersect (E_N-u)|`. Then `U` has density `m_N`, and conditional on `U=u`, `V` has density cap `M(u)=1/(2m_N(u))`. Account03/B14 r24 proves, for `gamma>-1`,

`int m_N(u)^gamma du = 2/(gamma+1) [(1-1/N) N^(1-gamma)+1/N]`.

Take ten independent copies `(U_i,V_i)` and the target-valid form

`Q(V)=2 sum_{i=1}^5 V_i V_{5+i}`.

Unconditionally the ten `V_i` are independent and each has density cap at most one. The cross block is `I_5`, so direct D5 gives

`||p_Q||_infty <= 5 sqrt(2e)`.

If instead one first conditions on all differences `U_i=u_i`, normalizes each sum fiber, and rescales `Y_i=M(u_i)V_i` to cap one, then the conditional cross block is diagonal with entries

`(M_i M_{5+i})^(-1)=4 m_i m_{5+i}`.

Hence

`Z_5(u)=4^10 prod_{i=1}^{10} m_i^2`,

and the conditional D5 certificate becomes

`5 sqrt(2e)/4 * prod_i m_i^(-1/5)`.

Averaging this certificate against the difference density `prod_i m_i du_i` costs exactly

`5 sqrt(2e)/4 * [int m_N^(4/5)]^10`

`= 5 sqrt(2e)/4 * {10/9[(1-1/N)N^(1/5)+1/N]}^10`,

which grows like a positive constant times `N^2`.

Thus D5 itself is uniform on this target-valid family, while the proof order "condition on conjugate differences -> normalize thin sum fibers -> rescale -> apply D5 -> average" loses quadratically in the fragmentation parameter. The correct order is aggregate/decouple before any normalized-fiber reciprocal payment.
