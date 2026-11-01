# QFORM fleet01/B01 early checkpoint

Run `20260923T050738Z-fleet01-B01-qform-auto11`.

Target remains the full three-large-eigenvalue quadratic-form density conjecture; full target OPEN.

Substantive direction: split the exact exterior-three energy by overlap size. For a fixed physical coordinate `s` with `a=A_ss != 0`, let `B=A_{K,K}-a^{-1}A_{K,s}A_{s,K}` be the exact Schur complement, `K=[n]\{s}`, and define the overlap-one star

`W1(s)=sum det(A[{s} union P,{s} union T])^2`,

where the sum runs over ordered disjoint two-sets `P,T subset K`. Exact block elimination gives

`W1(s)=a^2 * D0(B)`,

`D0(B)=sum_{P cap T=empty, |P|=|T|=2} det(B[P,T])^2`.

For a uniformly random bipartition `K=I disjoint_union J`,

`E e2(B[I,J]^T B[I,J]) = D0(B)/16`,

so some partition has pair-volume at least `D0(B)/16`. Applying the previously proved unconditional pair-volume half-Riesz theorem to the Schur residual and the source-valid square peel yields the scoped bound

`||p_Q||_infinity <= sqrt(2) C_E2 |a|^(-1/4) W1(s)^(-1/8)`

with `C_E2 <= 12*2^(5/6)*exp(5/24)`, hence coefficient `<37.242`.

This pays an entire overlap-one exterior-energy star before selecting a physical 2x2 minor. It does not pay the zero/near-zero pivot endpoint, which is the remaining structural obstruction for this overlap class.

Second calculation in progress: extend fleet03/B01's rank-two-cross/transverse-curvature receiver to the exact zero-transverse-curvature case when the cross-kernel direction couples linearly to the orthogonal two-plane. A vector-valued Hausdorff-Young calculation suggests an `L^q_t` bound for the transverse amplitude with scaling `||c||^{-1/q}`, leading at q=4 to a continuous-density estimate of order `7.852 Delta^{-2/5}||c||^{-1/5}`. This is not yet declared final until all mixed-norm and projection constants are checked.
