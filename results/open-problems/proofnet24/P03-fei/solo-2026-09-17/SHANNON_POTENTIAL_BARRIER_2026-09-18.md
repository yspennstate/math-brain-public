# The unequal-NAND potential has an unbounded Shannon-restriction defect

Status: proved below and self-checked; novelty UNVERIFIED. This is an obstruction to extending `UNEQUAL_NAND_CONTRACTION_2026-09-18.md` from disjoint products to general coordinate restrictions. It is not a counterexample to FEI.

All logarithms are base two unless `ln` is written. For an indicator A, retain

    V(A)=U(A)+(2/ln2)Q_A,

where

    U(A)=sum_edges not touching empty
           min(c_S^2,c_T^2)|log(c_S^2/c_T^2)|
         +sum_i[-c_i^2 log(c_i^2)],
    Q_A=sum_i c_i^2.                                    (1)

## 1. Statement

For every fixed real c and every positive even m, define the singleton-corrected potential

    W_c(A)=U(A)+cQ_A.                                    (2)

There is an indicator A on m+1 bits, with restrictions A_0,A_1 at its last bit, such that the selector influence is 2^(-m) and

    [W_c(A)-(W_c(A_0)+W_c(A_1))/2]/2^(-m)
      =[1/4+1/(2ln2)+o(1)]m.                            (3)

Consequently there is no universal C for which

    W_c(A)<=[W_c(A_0)+W_c(A_1)]/2
             +C Inf_selector(1-2A)                      (4)

holds for every indicator and every restriction coordinate.

The unequal-NAND potential is the special case c=2/ln2. Thus merely retuning its singleton coefficient cannot repair the restriction recursion.

This does not contradict the unequal-NAND contraction. Product children occupy disjoint variable blocks and have factorized Fourier coefficients. Shannon restrictions share all remaining variables and mix signed coefficient vectors before squaring.

## 2. Bent marker construction

Put N=2^m, epsilon=N^(-1/2), and delta=N^(-1)=epsilon^2. On {0,1}^m define

    g(x)=(-1)^(x_1x_2+...+x_(m-1)x_m).                  (5)

Its Fourier coefficients are s_S epsilon, where s_S is +1 or -1. Tensoring the two-bit Walsh transform `(1,1,1,-1)/2` proves this directly. Moreover

    s_empty=s_{i}=+1,
    n_+=(N+sqrt(N))/2,   n_-=(N-sqrt(N))/2,             (6)

and in each coordinate direction exactly N/4 unordered Fourier edges change sign. The last assertion follows because toggling one member of a quadratic pair changes the dual quadratic sign exactly when its partner bit equals one.

Let g' equal g except at zero, where its value is flipped. Then

    ghat'_S=s_S epsilon-2delta.                          (7)

Let F have restrictions g and g' at a selector bit, and set A=(1-F)/2, A_0=(1-g)/2, A_1=(1-g')/2. The selector influence is exactly delta.

## 3. Exact formulas for the two restrictions

For A_0 every nonempty squared Fourier coefficient is

    q=epsilon^2/4.

All internal adjacent masses agree, and all singleton signs in (5) are positive. Formula (1) gives

    W_c(A_0)=m h(q)+c m q,                               (8)

where h(x)=-x log x.

For A_1 define

    x_+=epsilon^2(1-2epsilon)^2/4,
    x_-=epsilon^2(1+2epsilon)^2/4.                       (9)

There are mN/4 internal sign-changing edges, every singleton has mass x_+, and all other internal edges have equal endpoint masses. Hence

    W_c(A_1)=(mN/4)x_+ log(x_-/x_+)
             +m h(x_+)+c m x_+.                        (10)

At m=2, x_+=0 and the edge term is zero by continuity.

## 4. Exact formula for the selector function

The selector Fourier pairs of F are

    u_S=s_S epsilon-delta,    v_S=delta.                (11)

For nonempty coefficients of A put

    z_+=epsilon^2(1-epsilon)^2/4,
    z_-=epsilon^2(1+epsilon)^2/4,
    y=epsilon^4/4.                                      (12)

The nonselector spectral layer has masses z_+ or z_-; the selector layer has constant mass y. Its data-direction sign-changing edges contribute

    K_data=(mN/4)z_+ log(z_-/z_+).                      (13)

The selector-direction edge at S=empty touches the global empty coefficient and is represented by the singleton entropy h(y) in (1). All other selector edges are internal, giving

    K_sel=y[(n_+-1)log(z_+/y)+n_-log(z_-/y)].           (14)

Finally, the singleton masses are z_+ in each of the m data directions and y in the selector direction. Therefore

    W_c(A)=K_data+K_sel+m h(z_+)+h(y)+c(m z_++y).       (15)

Equations (8), (10), and (15) are exact for every positive even m.

## 5. Asymptotic defect

Write

    L(t)=log[((1+t)/(1-t))^2]
        =[4/ln2](t+t^3/3+O(t^5)).                       (16)

The difference between the data-edge term (13) and half of the edge term in (10) is

    (m/16)(1-epsilon)^2L(epsilon)
      -(m/32)(1-2epsilon)^2L(2epsilon)
      =[m epsilon^2/(2ln2)]+O(m epsilon^3).             (17)

For (14), use `log(z_+/y)=m+2log(1-epsilon)` and the analogous plus formula. Equation (6) then gives

    K_sel=m epsilon^2/4+O(m epsilon^4+epsilon^4).        (18)

It remains to check that the singleton entropy and Q differences are lower order. Put q=epsilon^2/4. The three data-singleton masses are q, q(1-2epsilon)^2 and q(1-epsilon)^2. Taylor's theorem for h around q, using

    h'(q)=O(m),    h''(x)=-1/[x ln2],

on the interval between these three masses, shows

    m{h(q(1-epsilon)^2)-[h(q)+h(q(1-2epsilon)^2)]/2}
       =O(m^2 epsilon^4).                               (19)

The Q difference is in fact exact:

    (m z_++y)-[m q+m x_+]/2=(1-m)epsilon^4/4.           (20)

Thus every fixed c contributes only O(m epsilon^4). Also h(y)=O(m epsilon^4). Since m epsilon and m epsilon^2 tend to zero, (17)--(20) imply

    W_c(A)-[W_c(A_0)+W_c(A_1)]/2
      =[1/4+1/(2ln2)+o(1)]m epsilon^2.                  (21)

Because epsilon^2=delta is the selector influence, (3) follows.

For completeness, the Taylor bound in (19) is uniform for all sufficiently large even m because the three arguments lie between q/4 and q; the finitely many earlier m do not affect the asymptotic statement.

## 6. Consequence for the live route

The complement-invariant potential is genuinely stable under arbitrary unequal disjoint NAND but not under Boolean-preserving Shannon restriction with a constant local influence charge. No fixed coefficient multiplying Q repairs it. Thus a full proof cannot alternate the NAND contraction with unrestricted coordinate induction while charging only the split coordinate.

The obstruction is local, not aggregate. It does not show that V(A)/I_A is unbounded, and it does not refute a choice of a favorable coordinate, a block selection theorem, or a global multiscale payment. The full universal K/I problem remains unchanged.

`check_shannon_potential_barrier.py` verifies (5)--(15) for the actual unequal-NAND potential c=2/ln2 against full exact Walsh transforms for even m through 12, using rational arithmetic and outward rational logarithm intervals. The all-m statement for every fixed c is proved above, not inferred from finite computation. The check is not an independent audit.
