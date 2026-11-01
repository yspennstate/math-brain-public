SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T17:10:49Z.
attacking: eliminate the localized two-hub high-column-leverage survivor by converting the fixed-pair anchored third volume into a k=2, ell=1 projected-crossing packet before any reciprocal pair-core or column-minor inversion.

# Early checkpoint — anchored third volume is exactly a two-hub projected-crossing currency

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

In the localized-pair branch of fleet03/B09 r35/r36, fix the literal physical hub pair `a,b`, the moved-leaf bank `S`, and the opposite bank `T`. Put

`B=A[{a,b},T]`, `Delta=det(B B^T)>0`, `R=A[S,T]`,

and let `Pi` be the orthogonal projection in `R^T` onto `row(B)`. Define

`C=R(I-Pi)`.

The fixed-pair anchored third volume from r35 is

`V_ab(S)=sum_{k in S} sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`.

A direct Cauchy--Binet/Gram decomposition gives the exact identities

`V_ab(S)=Delta ||C||_F^2`,

and leaf-by-leaf

`V_k:=sum_{J,|J|=3} det A[{a,b,k},J]^2 = Delta ||C_k||_2^2`.

Hence the one-volume row marginals of the projected crossing are

`alpha_k=||C_k||_2^2/||C||_F^2 = V_k/V_ab(S)`.

In the r32 diffuse-singleton compiler branch, `V_k/V_ab(S)=w_k(S)/W(S) <= Gamma_k^2/W(S) < 1/2`. Therefore the fresh reviewed grouped projected-crossing theorem (`NEW_PROJECTED_CROSSING.md`, k=2, ell=1) applies with the two *physical* hub coordinates themselves as the grouped hub. Since their joint density cap is at most one,

`||p_Q||_infinity <= 3*2^(5/6) Delta^(-1/6) ||C||_F^(-1/3)`.

Using `V_ab=Delta ||C||_F^2`, all `Delta` factors cancel:

`boxed: ||p_Q||_infinity <= 3*2^(5/6) V_ab(S)^(-1/6)`.

Thus no column-range leverage hypothesis is needed. In the r34 localized pair branch `V_ab(S)>=27 G_*/400`, giving

`||p_Q||_infinity <= 3*2^(5/6)*(400/27)^(1/6) G_*^(-1/6) < 8.378 G_*^(-1/6)`.

The source theorem supplies an L1 characteristic-function envelope, so this branch has a continuous density and the same coefficient times interval length. Arbitrary pair-core curvature, arbitrary leaf curvature, outside couplings and conditioning-generated affine terms remain inside the allowed functions/phases.

This directly targets the r36 survivor where the column range projection can have leverage one.
