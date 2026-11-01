SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T09:35:31Z.
attacking: the designated partner's diffuse row/column-star survivor — resolve overlap/misalignment by a dimension-free disjoint-innovation selection, then split transverse wedge mass from an aligned common-bank survivor.

# Early substantive checkpoint

Full QFORM remains open. This checkpoint records the first new calculation before the final argument.

## Fresh designated partner now available

I use the completed designated partner fleet04/B07 result

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

In its unpaid N3 rank-four survivor there is an actual physical row-star vector `r` and an actual physical column-star vector `c` satisfying

`R:=||r||_2>h`, `C:=||c||_2>h`,

while every physical coefficient in either star satisfies

`||r||_infinity, ||c||_infinity <= h/8`,

where

`h=(2 sqrt(2)-1)/1572864 = 1.1624826588606455e-6`.

The partner's stated remaining issue is that the two bank systems can overlap or be misaligned. I attack exactly that issue below, without pretending that the resulting linear-bank certificate already controls arbitrary quadratic curvature.

## Lemma 1: disjoint innovation selection from two diffuse stars

Let `r,c` be real vectors on one finite physical-coordinate ground set (pad either vector by zeros where necessary). Put `R=||r||_2`, `C=||c||_2`, and assume

`||r||_infinity,||c||_infinity <= delta <= min(R,C)/8`.

Then there is a partition of the coordinates into disjoint sets `S union T` such that

`||r_S||_2^2 ||c_T||_2^2 >= (63/256) R^2 C^2`.

In particular,

`||r_S||_2 >= sqrt(63) R/16`,
`||c_T||_2 >= sqrt(63) C/16`.

Proof. Independently color each coordinate into `S` with probability `1/2`, and let

`U=sum_j 1_{j in S} r_j^2`, `V=sum_k 1_{k in T} c_k^2`.

The diagonal terms never occur in `UV`, whereas every ordered pair with different coordinates occurs with probability `1/4`. Hence

`E[UV]=(1/4)(R^2 C^2-sum_j r_j^2 c_j^2)`.

Moreover

`sum_j r_j^2 c_j^2 <= ||r||_infinity^2 C^2 <= delta^2 C^2 <= R^2 C^2/64`.

Therefore `E[UV]>=63 R^2 C^2/256`, so one partition realizes this lower bound. Since `U<=R^2` and `V<=C^2`, the two individual norm lower bounds follow as well. QED.

Applying the designated partner with `delta=h/8` gives disjoint ORIGINAL-coordinate banks `S,T` with

`||r_S||_2,||c_T||_2 > (sqrt(63)/16)h
 = 5.766825035194508e-7`.

This removes the partner's overlap/misalignment obstruction at the level of two genuine independent linear innovations. It does NOT remove arbitrary within-bank quadratic curvature.

## Lemma 2: transverse mixed-minor bank or aligned common mode

Define the two-star wedge currency

`W^2 := sum_{j<k}(r_j c_k-r_k c_j)^2
      = R^2 C^2-(r dot c)^2`.

Exactly one of the following two useful alternatives is available.

### Transverse branch

If `W>=RC/9`, then `W^2>=R^2C^2/81`. Randomly bipartition the physical coordinates. Each unordered pair `{j,k}` is cut with probability `1/2`, so some disjoint `S,T` satisfy

`sum_{j in S,k in T}(r_j c_k-r_k c_j)^2
 >= W^2/2
 >= R^2 C^2/162`.

For the partner survivor this gives a cancellation-free aggregate bank of actual mixed `2x2` coordinate minors exceeding

`h^4/162 = 1.1272777052964666e-26`.

No single minor is selected or reciprocated.

### Aligned branch

If `W<RC/9`, choose `sigma in {+1,-1}` so that `sigma(r dot c)>=0`, and normalize `u=r/R`, `v=c/C`. Then

`|u dot v|>sqrt(80)/9`,

so

`||u-sigma v||_2 < sqrt(2-2sqrt(80)/9)
 =0.11128351180739575 <1/8`.

Also `||u||_infinity<=1/8`. Apply the designated partner's elementary four-bank greedy argument to `u`: there are four disjoint banks `B1,...,B4` with `||u_Bq||_2>=1/4`. For each bank,

`||v_Bq||_2 >= ||u_Bq||_2-||u-sigma v||_2
 >1/4-1/8=1/8`.

Therefore every one of four disjoint ORIGINAL-coordinate banks simultaneously carries both stars:

`||r_Bq||_2>=R/4>h/4`,
`||c_Bq||_2>C/8>h/8`.

This is a common-mode/grouped-bank alternative. It is intentionally not converted into a small-operator-norm perturbation: the source correction forbids treating a small coefficient matrix as a uniformly small random quadratic perturbation for arbitrary unbounded inputs.

## Current mathematical consequence

The designated partner's diffuse row/column-star survivor is therefore sharpened to an exhaustive dimension-free ORIGINAL-coordinate alternative:

1. two disjoint innovation banks with norms `>sqrt(63) h/16` always exist;
2. more structurally, either a disjoint-bank aggregate mixed-minor mass is `>h^4/162`, or four disjoint common banks each carry row-star norm `>h/4` and column-star norm `>h/8`.

The next step is to splice one of those two certificates into a curved receiver that retains all same-bank quadratic terms and the true ambient Schur remainder. That implication is not asserted here.
