# Checks for QFORM-DIFFUSE-SCHUR-THREEBANK-PACKET-v1

Run: 20260923T181642Z-account04-B20-QFORM-r11.

## Symbolic identities

For nonnegative weights w_k with sum_k w_k = 1,

    sum_(k,l,m pairwise distinct) w_k w_l w_m
    = 1 - 3 sum_k w_k^2 + 2 sum_k w_k^3.

This follows by partitioning all ordered triples into all distinct, exactly two equal (three placements), and all equal.

If eta = max_k w_k, then

    sum_k w_k^2 <= eta sum_k w_k = eta,

so the random three-color expectation is at least (1 - 3 eta)/27.

## Exact arithmetic

At eta = 1/64,

    (1 - 3 eta)/27 = 61/1728
    = 0.03530092592592592...

The joint-cap constant is

    e^(3/2) sqrt(1728/61)
    = 23.8533112123... < 23.854.

With tau0 = 1/4 and delta = 2^(-16),

    4 sqrt(6) e^(1/4) tau0^(-1/4) delta^(-1/8)
    = 71.1679123172... < 71.168.

With epsilon = 1/64,

    16 * 2^(1/4) sqrt(30) (tau0 epsilon)^(-1/3)
    = 661.736003207... < 661.737.

These are algebra and arithmetic checks, not independent proof review.
