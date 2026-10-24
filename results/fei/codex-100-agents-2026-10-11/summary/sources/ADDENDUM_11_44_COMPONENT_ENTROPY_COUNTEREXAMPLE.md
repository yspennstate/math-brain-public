# 11.44 Connected-component raw entropy subadditivity fails

1 October 2026, 04:59 UTC. Unrestricted FEI remains unproved and unrefuted. This is a precise auxiliary-route obstruction, not a novelty claim or a solution.

## Exact source and result

The independently checked [nine-bit witness](https://github.com/yspennstate/math-open-problems/blob/1517573ec0b37bd7aeb6a285562a6763059c5a20/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/separated-entropy-counterexamples/report-connected.md) is on private open draft PR12 at commit `1517573ec0b37bd7aeb6a285562a6763059c5a20`, report blob `5254f18a649fcdb9fb3b3dcbcf5e34fcc1b8595c`, SHA256 `d3a5f3503cf776f87c282f60b67b9a7968e859a5abe33c92e409855fe3f25a4e`.

On the uniform binary9cube, write coordinates as five data bits y and four control bits x. Set A={wt(y)<=1} times the full4cube and B={(11111,0000)}. A and B are the two connected components of their union, have sizes96 and1, and minimum cross-distance4. For indicator raw Fourier entropy with natural logarithms, including the empty coefficient and zero terms interpreted as0,

    Hraw(1_(A union B)) - Hraw(1_A) - Hraw(1_B) > 1/5000.

The exact prime-log numerator divided by262144 is

    540672ln2 - 82728ln3 - 8450ln5 - 39690ln7
    - 21780ln11 - 8450ln13 - 9610ln31 - 18818ln97.

Its certified interval is (0.000224462410050, 0.000224462410068). The checker independently enumerates Walsh coefficients and edges, checks connectivity and uses rational atanh-series logarithm enclosures. Root read the derivation and both witness checkers and replayed their outputs byte-for-byte. This is independent mathematical/code checking plus exact finite arithmetic, not proof-assistant formalization.

## What survives

With D_i=(Id-flip_i)/2 and E=sum_i E(D_i g)^2, energies are5/16,9/1024,329/1024 for A,B,union. Their entropy/energy ratios satisfy

    R(A) < R(A union B) < R(B)=4ln2.

Thus this witness defeats raw entropy subadditivity even over actual connected components. It does NOT defeat the weaker maximum-component-ratio inequality, prove or refute strict physical-criticality implies connected support, or change the finite n<=4 certificate in11.43. Components are not generally physical restrictions. No universal FEI constant follows.

A smaller7bit graph-separated pair is archived in the same package but its first support has five components; the9bit example establishes the stronger actual-two-component failure. The old small-n floating diagnostic is preserved with a correction link; its absence of small-n violations was never a universal certificate.

## Safe continuation

Do not revive disjoint physical support as disjoint Fourier support, or use an incoherent mixture for the squared sum of amplitudes. Actual single-coordinate separation has an elementary packet-entropy proof, but arbitrary complementary subsets do not inherit it. A weaker ratio-max or controlled-excess argument still needs a complete proof and nonreusing global accounting. Existing signed/source-sensitive and Boolean-middle lifetime gaps remain open.

[Exact checker](https://github.com/yspennstate/math-open-problems/blob/1517573ec0b37bd7aeb6a285562a6763059c5a20/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/separated-entropy-counterexamples/check_connected.py) has blob `762313d59d3b5ebbc9b5d01bce4b487e9624e748`, SHA256 `af13bc0e45c2f927aae5ca7348ac5a20c6257f87592e4b6f1b38120aaed3e527`. All nine publication readbacks, including the historical diagnostic correction, matched complete expected bytes. Code remains on the unmerged draft branch; this index neither deploys it nor grants source admission, scheduler control or external permissions.
