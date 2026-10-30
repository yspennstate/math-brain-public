# A growing ownership entropy need not be an unpaid output bill

Bits, gamma=6/5. This is a narrow diagnostic of attempting to transplant A007's now-proved full-support tail to arbitrary prime supports. It refutes that transplantation, not the reviewed full-support theorem, not joint root/factorial payment, and not FEI.

## Actual Boolean prime-table obstruction

Let g_n=2 OR(x_1=1,...,x_n=1)-1. Its exact prime table is the n singleton clauses h_i=(x_i=1), pi_i=1/2. Every positive implicant forces a positive literal, and removing the sole literal from any listed prime permits the all-negative input. All coordinates are relevant. Put z=2^-n. The constant Fourier coefficient is 1-2z, and every nonempty coefficient has magnitude 2z; direct expansion of the negative full cell proves this. Thus

    P_g(T)=4z^2 for every nonempty T,
    Var(g)=4z(1-z), I(g)=2nz.

For every selected nonempty T, s=|T|, ownership is FORCED: coordinate i can only go to its own prime gate. All s used gates own one coordinate, kappa_i=1, and the original ownership graph has no edges. There is one actual base partition event, with every used gate a root and zero children. Its conditional ownership entropy is exactly log s; posterior erasure cannot make a different old assignment available.

Consequently no dimension-independent bound on E_eta_T H(owned sizes/s) holds for arbitrary-support prime tables. The conditional expectation over the normalized nonempty Boolean spectrum is also unbounded:

    E[H(ownership) | T nonempty]=E[log |T| | T nonempty]
                        >=(1/2)log ceil(n/2) ->infinity.

Indeed a Bin(n,1/2) variable has at least half its mass at or above ceil(n/2), by pairing subsets with their complements; conditioning on nonempty only increases that probability. This is an all-dimensional proof, not an extrapolation of small truth tables.

The pointwise attempt to apply Pr_eta(H>=h)<=min(1,6^(s-1)2^(-sh/5)) is explicitly false: take n=s=8192, T=[n], h=log s. The true probability is one, while 6^5<s implies the proposed right side <1/6. T has positive Boolean Fourier mass 4*4^-n. This symbolic large-n witness is checked through integer inequalities and the proved Fourier formula; no 8192-dimensional truth table is claimed to have been generated.

These are coding-scope obstructions. They are not an unbounded H(g)/I(g) family: the elementary vacuum estimate eta(1-v)<=v log e gives H(g_n)<4I(g_n), using log e<2. The unconditioned spectral ownership bill is tiny compared with n and should not be confused with its normalized conditional divergence.

## A007's general intersection cost is nearly sharp here

For selected control size u=1, its exact K term on this forced assignment is

    K_s(1)=s log s-(s+1)log((s+1)/2).

The complete occupation sum is

    Z_s(1)=s*2^(-gamma(s-1)),

because there are s choices of the control owner; the owner has owned size/intersection two, and each of the other s-1 gates has size one and intersection two. Compare the reviewed envelope log Z>=-(u/5)H-gamma K:

    log Z_s(1)-[-(1/5)log s-gamma K_s(1)]
       =gamma[2-(s+1)log(1+1/s)].

The function (s+1)ln(1+1/s) decreases from 2ln2 to 1, since its derivative is ln(1+1/s)-1/s<0. Therefore this gap lies in [0,gamma(2-log e)) and approaches the upper endpoint. The K term is not an avoidable unbounded error of the general envelope on this witness; the ownership and K losses need their joint credits.

## Exact root/factorial refund under the same activated prime reference

Fresh one-control activation F=2 A_1 OR_n-1 has exactly the n width-two primes (control=1,x_i=1). Start from lambda_i=1 in the base table, and choose globally beta=1/n. New weights are 1/n, feasible at the common control. All orders are control first. The data-core reference is fixed before the Fourier set, and its inherited base cost is retained.

For U={control} and selected T of size s, c=s old roots have rarity 1/2. The root-removal credit is 2^(s-1). The one-control owner must be the surviving root and its component tree is a star. There are s owner choices and (s-1)! chronological child-label sequences, hence s! DISTINCT actual events. The exact rank-stripped multiplier is

    J_1(T)=n^(-s) (s-1)! 2^(s-1) Z_s(1)
          =(s!/n^s)*2^(-(s-1)/5).

Thus all selected data labels cost s log n, but the actual factorial refund is log(s!). For the full set s=n,

    -log J_1([n])<=n log e+(n-1)/5,

because sum_(j=1)^n ln j>=integral_1^n ln x dx>=n ln n-n. The n log n bill has become linear, despite ownership entropy log n diverging and K being nearly sharp. This is a pointwise selected-sector certificate, not a complete spectral payment. For empty selected control, L_0=n^-s remains and must still enter the original signed Psi expectation; it is not discarded by this calculation.

## Actual queue probability, separately from surrogate mass

Let alpha=2^(-6/5) and D'=(1+1/(4n))^n-1. All inactive-root probabilities and conditioning are retained. For a fixed T of size s, the same finite star event family has EXACT original conditioned probability

    Q_star(T union {control})
      =s!/[24 D' n^s s^2(s+1)]
                      *[alpha/(4(1+alpha))]^(s-1).

Proof: its root odds contribute 1/(4nD'); root selected size two costs 1/6 and selects the full width-two support; child count s-1 costs 1/[s(s+1)]; the all-control attachment multiset costs 1/s. Each child label costs 1/n. A leaf selects its data singleton with probability alpha/[2(1+alpha)] and zero children with probability 1/2. Multiply these factors for each distinct star, then sum exactly s! stars. For s=1 the formula gives 1/(48nD'), agreeing with a one-root size-two zero-child event. Surrogate J and Q_star are not identified.

The total root odds sum is 1/4, so product expansion gives D'<=1/3. Also alpha>1/4 gives alpha/[4(1+alpha)]>1/20. Hence

    Q_star(T union {control})
      >=s!/[8n^s s^2(s+1)20^(s-1)].

For s=n this costs at most n log e+(n-1)log20+3+2log n+log(n+1), again O(n) with every original queue factor retained. It is not the full output mass, and its spectral expectation, empty-core sector, core-only sector, signed normalizer and inherited base residual are not set to zero or inferred paid by this pointwise result.

## What remains

A007's full-support conditional tail is valid and its controller correction is now proved. The general tail transplant above is false even for disjoint singleton primes. A universal continuation therefore needs the expected JOINT label/K/ownership budget minus actual root/factorial credits under the same posterior, not a uniform ownership entropy bound on all prime tables. The next shortest target is a non-disjoint incidence fixture where this exact joint cancellation survives or fails, keeping all spectral sectors, feasible weights and inherited nonconstant core cost.
