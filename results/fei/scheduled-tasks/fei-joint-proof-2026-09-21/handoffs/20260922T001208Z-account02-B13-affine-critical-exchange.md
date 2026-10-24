# FEI handoff — account02/B13 — simultaneous affine-minimum critical core

Status: PARTIAL; full FEI remains OPEN.

Source-bound scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T001208Z-affine-critical-exchange/REPORT.md`, creation commit `049beb8f160331de23e5062c2b627fd0d31c9a08`. Exact checker/output commits: `7c2749ea724e536d08ff33d9bbb5267ce3293f20`, `bec933c65a9bcb160889a11cadb9ac9332cb0363`.

Named other-account dependency actually consumed: account04/B13 `20260921T2325Z-asymmetric-exception-compiler/REPORT.md`, blob `52039a8b5b499dc23c073e194e3183a6d9cc0205`.

## New proved interface

Fix finite `C`. If FEI at `C` fails, a minimum-dimensional folded-`J` violator can be moved by one `GL(n,2)` map plus one character multiplier into a single Boolean function `g` satisfying simultaneously

`J(g)=I(g)=I_aff(g)`, tensor primitivity, and for every nonempty proper physical block `A`,

`Delta_A H(g) > C D_A^J(g) >= C I_A(g)`.

Thus affine-basis minimization is compatible with the same physical restriction-critical primitive core; no separate gauge/tensor loss is needed.

In this gauge, if `X` is the spectral sample and `p_i=Pr(i in X)`, then every nonempty parity `T` satisfies the joint basis-exchange envelope

`min(Pr(xor_{i in T} X_i=1), Pr(xor_{i in T} X_i=0)) >= max_{i in T} p_i`.

For pair atoms `p_ik=Pr(i,k in X)`, with `a=max(p_i,p_k)`, `b=min(p_i,p_k)`,

`max(0, a+b/2-1/2) <= p_ik <= b/2`.

Hence for a maximum-influence row `x`, `m=p_x`,

`d_x <= (I_aff-m)/2`, so its derivative-depth defect obeys

`0 <= delta_x <= 1/2 [I_aff/m - 1 - log2(1/m)]`.

## C=12 consequence using account04/B13

A hypothetical minimum-dimensional 12-counterexample in this affine-minimum gauge cannot have zero or account04-capturable low derivative depth. With `eta0<=1/32`, `c0=log2(32/31)`, and

`delta_asy(r)=W(2 ln(2)(8r+9))/(4 ln(2)(8r+9))`, define

`tau(m)=min(eta0, delta_asy(log2(1/m)+c0))`.

Then the maximum row necessarily satisfies

`delta_x > tau(m)`

and therefore the strict anti-one-point surplus

`I_aff(g)/m > 1 + log2(1/m) + 2 tau(m)`.

The exact one-point family sits at equality without the surplus and is excluded from a 12-critical core; bent families stress the opposite high-depth endpoint.

Finite self-check: 1,936,992 exact rational/integer checks over all Boolean functions modulo global sign through n=4, PASS. This is a self-check, not FEI closure.

Next shared target: use the all-parity envelope, not pairwise witness summation, to pay the high-depth/asymmetrically exceptional cluster without witness reuse.
