# Checks for QFORM-PHYSICALPAIR-BANK-OVERLAP-v1

Run: 20260923T192012Z-account04-B16-QFORM-r2.

## Symbolic exponent check

The account01/B16 overlap receiver gives

    C_* (MN)^(2/5) (s_1 s_2)^(-2/5) |lambda|^(-1/5).

For the literal physical pair and one residual bank,

    N=1,
    M=2^(3/2) (det G_b)^(-1/2),
    s_1 s_2=D.

Therefore

    (MN)^(2/5)=2^(3/5)(det G_b)^(-1/5),

and

    D^(-2/5)|lambda|^(-1/5)
    =(D^2|lambda|)^(-1/5)
    =[D |det Lambda| tau]^(-1/5),

using D|lambda|=|det Lambda|tau. This reproduces equation (2.2).

## Live-gate arithmetic

With

    C_*=5(675/256)^(1/5),
    C_pair=2^(3/5)C_*,

one obtains

    C_*    = 6.069917185377548...,
    C_pair = 9.200274035222916....

At W_b>61/1728 and the gate

    det G_b >= W_b s^2/(64D tau),

the denominator in (2.2) is at least W_b s^5/64, so

    C_pair (64*1728/61)^(1/5)
    =41.25527996573107... <41.256.

These are exact algebra and numerical arithmetic checks, not an independent proof review.

## Hypothesis audit

- The two-dimensional receiver variable is the literal pair O^T(X_i,X_j); its joint density cap is one because |det O|=1.
- Independence is asserted only between disjoint original-coordinate sets I and J_b.
- No independence of the two rotated pair coordinates is used.
- No independence among (Z_1,Z_2,T) is used.
- The three-dimensional projection theorem is used only to establish its genuine joint cap.
- Conditioned variables enter only through affine shifts; the receiver is uniform in those shifts.
