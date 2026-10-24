# An actual Boolean boundary to unrestricted overlap

There is no absolute selector-only constant L such that H(z-select(G,H)) <= (H(G)+H(H))/2+L Inf_z for arbitrary overlapping Boolean cores. This refutes only that transfer inequality, not FEI.

For every even k>=4 let b(x)=(-1)^(x_1 x_2+...+x_(k-1)x_k), b'=b-2*1_zero. Both are actual Boolean signs because b(0)=1. Put delta=2^-k, e=2^-k/2. The quadratic sign has Fourier coefficients sigma_T e; the flip changes each coefficient to sigma_T e-2delta. These identities follow by tensoring the two-bit quadratic Fourier transform and the singleton's transform. They are the previously certified A097/A023 B05 seed, used here as a new obstruction to unrestricted selector admission rather than a new FEI family.

Let h select b,b' by a fresh physical fair selector. The selector influences exactly delta, since the two outputs differ only at zero. At each residual data fiber its two parent spectral masses are A_T=(sigma_T e-delta)^2 and B_T=delta^2. Hence

    B_z(h)=sum_T phi(A_T,delta^2),
    Delta=H(h)-(H(b)+H(b'))/2=B_z(h)+J_z(h)>=B_z(h).

For positive A,B, phi(A,B)=B log2(A/B)+(A+B)log2(1+B/A)>=B log2(A/B). Since e>=4delta,

    A_T>=(e-delta)^2>=(9/16)delta,
    B_z(h)>=2^k delta^2 log2((9/16)/delta)
             =delta[k-log2(16/9)].

Thus Delta/Inf_z>=k-log2(16/9) tends to infinity. The complete seed entropy bill was explicitly retained and the selector is used exactly once. The counterexample does not depend on a dictionary mismatch or omitted history cost: exact leaf references already give it. The missing l1 admission cannot be removed without changing the budget; here the b collision vector has l1 norm 2^(k/2). A proof extending the one-shared-bit result to arbitrary overlap must borrow a quantitatively stated seed/core reserve, not merely reuse a purported absolute selector tax. Total core influence remains of order k, so this result gives no unbounded H/I family.
