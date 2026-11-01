SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T17:28:33Z.
attacking: conditional C0 transfer and whether the owner's stronger continuous-density conclusion follows from the central universal L-infinity bound without any class-wide continuity modulus.

# Early substantive checkpoint

## Claim being proved

Let W be arbitrary and let Y be real. Assume that for almost every w the regular conditional law of Y given W=w has a density p_w in C_0(R), and that

    ||p_w||_infinity <= M

with the same finite M for almost every w. Then the unconditional law of Y has a density p in C_0(R) with ||p||_infinity <= M.

This has a target-level consequence. Assume only the central QFORM height conjecture with constant C: every independent cap-one product input and every real symmetric matrix B with s_3(B)>=1 has an output density with essential supremum at most C. Then every target Q=X^T A X actually has a C_0 representative, and that representative has ordinary pointwise supremum at most C. Thus the owner's stronger continuity conclusion does not require a second universal continuity modulus once the central height bound is established.

## Proof skeleton

For the conditional transfer, use a jointly measurable density version obtained from conditional Gaussian smoothing:

    p_w(y)=lim_{m->infinity} (mu_w * gamma_{1/m})(y)

on the full-measure set where the conditional law has a C_0 density. For every bounded Borel test h, Tonelli gives that p(y)=E p_W(y) is an unconditional density. If y_n->y, then p_W(y_n)->p_W(y) a.s. and |p_W(y_n)|<=M, so dominated convergence gives p(y_n)->p(y). If |y_n|->infinity, p_W(y_n)->0 a.s. and dominated convergence gives p(y_n)->0. Height <=M is immediate.

For QFORM, let r=rank(A)>=3. Factor A=V Lambda V^T with V having r orthonormal columns and Lambda invertible. Choose r original-coordinate rows I for which V_I is invertible. Then the physical principal block

    B=A_{I,I}=V_I Lambda V_I^T

is nonsingular. Set s=s_3(B)>0. Condition on W=X_{I^c}. The conditional polynomial in Z=X_I is

    Z^T B Z + 2 Z^T c(W) + d(W).

Completing the square gives

    (Z+B^{-1}c(W))^T B (Z+B^{-1}c(W)) + d'(W).

For each fixed w the shifted original coordinates remain independent and cap one. The already-completed fixed-instance rank>=3 regularity theorem gives p_{Q|W=w} in C_0. Applying the assumed central QFORM bound to B/s and scaling back gives the uniform conditional height

    ||p_{Q|W=w}||_infinity <= C/s.

The conditional C_0 transfer therefore yields p_Q in C_0. Independently, the central theorem applied to the original target A gives ess sup p_Q<=C. Since the C_0 representative is continuous, it cannot exceed C at even one point without exceeding C on a positive-measure neighborhood. Hence its ordinary supremum is <=C.

## Partner equation

The completed fleet04/B15 pivoted-convolution theorem gives, after conditioning on arbitrary outside coordinates, for the physical block

    [[a,b,0],[b,0,0],[0,0,gamma]],

    p_{Q|W=w} in C_0,
    ||p_{Q|W=w}||_infinity <= 6 |b|^(-2/3) |gamma|^(-1/3)

uniformly in w and in the induced affine terms. The conditional transfer immediately gives the actual unconditional inequality

    p_Q in C_0,
    ||p_Q||_infinity <= 6 |b|^(-2/3) |gamma|^(-1/3).

No common continuity modulus in w is required.

Status: proof skeleton complete; polishing measurability and the exact logical separation between unconditional fixed-instance regularity and the open universal height remains for the final report. Full QFORM remains OPEN.
