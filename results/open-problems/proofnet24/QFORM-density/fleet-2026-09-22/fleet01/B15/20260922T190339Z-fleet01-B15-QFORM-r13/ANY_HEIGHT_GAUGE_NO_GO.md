# Strong no-go: every unbounded monotone scalar-conditioned projection-height gauge fails

This strengthens `ALL_POSITIVE_MOMENTS_NO_GO.md` and the assigned partner fleet02/B15 r6. The same fixed target and fragmented cap-one product inputs make the scalar-conditioned three-dimensional projection-density height itself uniformly large on **every** scalar level carrying probability. Thus the obstruction is not specific to power moments.

## Setup

Use the fleet02/B15 r6 construction with normalized Hadamard `H`, fixed target

`A=H diag(1,2,-3,1/2) H^T`,

and independent inputs

`f_1=1_(E_M)`, `E_M=union_{j=1}^M [10j,10j+1/M]`,

`f_2=f_3=f_4=1_[0,1]`.

Let `Y=H^T X`, `Q'=Y_4^2/2`, and let `p_4` be the density of `Y_4`. The partner calculation gives disjoint scalar packets

`p_4(s)=(1/M) sum_{j=1}^M g_M(s-a_j)`

with `||g_M||_infinity<=2`. Therefore, on the support of `p_4`,

`p_4(s)<=2/M`.

Orthogonality preserves the unit indicator density of the source. For almost every supported scalar level, the conditional density of `(Y_1,Y_2,Y_3)` is the normalized indicator of the corresponding section, hence

`H_M(s):=||rho_(123|Y4=s)||_infinity = 1/p_4(s) >= M/2`.

The construction has `Y_4>0`, so conditioning on `Q'=Y_4^2/2` is equivalent to conditioning on `Y_4`. Consequently

`||rho_(123|Q')||_infinity >= M/2`

almost surely.

## Corollary — no unbounded monotone gauge can be universally paid

Let `Phi:[0,infinity)->[0,infinity)` be any nondecreasing function. Then

`E Phi(||rho_(123|Q')||_infinity) >= Phi(M/2)`.

In particular, if `Phi(r)->infinity`, the left side diverges along this one fixed target matrix as `M->infinity`.

This contains the power-moment statement

`E||rho_(123|Q')||_infinity^beta >= (M/2)^beta`

for every `beta>0`, but is strictly more general.

## Proof-search consequence

The full QFORM output for this fixed matrix remains bounded (and, by the completed fleet02/B15 r3 theorem, continuous) for every `M`. Hence no universal proof can first collapse each scalar residual level to **any unbounded monotone function of the conditional projection-density height alone** and then average that scalar penalty. The missing information is genuinely geometric: the translated location/overlap of the conditional output profiles.

The source-valid object retained by r13 is therefore the pre-normalized joint profile / graph trace

`p_Q(t)=int G(y,t-y^T Lambda y)dy`,

or an equivalent translation-aware quantity. Conditional normalization followed by a height-only penalty is ruled out in an essentially maximal way by this construction.

This is an intermediate-mechanism elimination, not a counterexample to the quadratic-form bounded-density conjecture.
