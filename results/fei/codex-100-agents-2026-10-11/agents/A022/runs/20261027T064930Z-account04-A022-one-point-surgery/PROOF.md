# The original adjacent mark covers unbalanced dependent controllers

Rung: author proof with exact validation; independent review pending. All logarithms are base two. Full FEI remains open.

Let g be -1 only at 000, b=g tensor g on six DATA bits, delta=1/64. For arbitrary Boolean a,c on the SAME independent finite uniform control cube, put F(0,z)=a(z), F(1,z)=-c(z), and F=b elsewhere. No balance, independence between a and c, or distinctness is assumed. Let h(y,z) select a and -c. With p_f(S)=fhat(S)^2, pi_f(S)=sum_{R containing S}p_f(R), define

 V(f)=sum_{S nonempty}p_f(S)log2(pi_f(S)/p_f(S)),
 W(h)=V(h)-p_h({y})log2(pi_h({y})/p_h({y})),
 Gmark(h)=sum_j[W(h)-E W(h|z_j)]+W(h)-(V(a)+V(c))/2.

Both physical outcomes are retained. A zero mass contributes zero. The marked coordinate is the SAME original coordinate in every control child. We prove

 GV(F)-2delta Gmark(h) <101 <256 I_DATA(F),                 (1)
 V(F)>=2delta W(h).                                      (2)

These hold for all finite controller dimensions, including zero and constant controllers. They extend the A021 balanced-root theorem to arbitrary controller means, at the same original rate and coefficient. They do not pay for an arbitrary initial marked source.

## 1. Exact remainder and its global size

Write s=Ea,t=Ec,r=E(ac), epsilon_S=(-1)^{1_{0 in S}}, H_S=bhat(S), B_S=H_S-delta(1-epsilon_S). Then

 A_S=B_S+delta(s-epsilon_S t),
 M_S=B_S^2+2delta B_S(s-epsilon_S t)+delta^2(2-2epsilon_S r),
 p_S=A_S^2, Z_S=sum_{R containing S}M_R.

M is the complete DATA marginal, not just the empty-control row. It equals the expectation of [B_S+delta(a-epsilon_S c)]^2 under the actual four-outcome joint sign law q of (a,c). Thus 0<=p_S<=M_S<=Z_S, sum M=1, and Z<=1. The exact nonempty-control row factorization gives

 V(F)=2delta W(h)+T(q),
 T(q)=sum_{S nonempty}p_S log2(Z_S/p_S)+(5delta/2)(2-s^2-t^2). (3)

This is A021's correlation-aware identity, rechecked on unbalanced physical children here. The five other DATA frequencies are uniform in each nonempty-control row, with mean missing count 5/2; removal of the vacuum and marked singleton leaves exactly W. No cross term is omitted.

Every term of T is nonnegative. Also, for the at most 63 nonempty DATA rows with sum p<=1, sum p log2(1/p)<=log2(63)<6. To see the subprobability bound, fix mass m: its entropy is at most m log2(63/m), an increasing function on 0<=m<=1 since ln(63)>1. Therefore

 0<=T(q)<6+5/64=389/64                                 (4)

on the entire realizable sign-law simplex, without a positive Fourier floor.

## 2. Fisher cost of the four-outcome law

Take any affine path q(lambda) in the simplex, with means s,t affine and derivatives u,v. Let J=sum_alpha q'_alpha^2/q_alpha in the relative interior. Each deterministic sign pair alpha gives nonnegative M_S(alpha), hence K_S(alpha)=sum_{R containing S}M_R(alpha), and Z_S=sum_alpha q_alpha K_S(alpha). Weighted Cauchy-Schwarz gives

 (Z'_S)^2/Z_S <=sum_alpha K_S(alpha) q'_alpha^2/q_alpha.

The following uniform weighted spectrum bound applies to each of the four deterministic edited seeds:

 sum_{S nonempty}K_S(alpha)
 =sum_R(2^|R|-1)M_R(alpha) <16.                          (5)

Indeed the weighted Fourier norm squared sum_R 2^|R| bhat(R)^2 is (35/16)^2: on one three-bit point seed its value is (9+26)/16. A single value flip changes each Fourier coefficient by magnitude 2delta, whose weighted norm is 2delta sqrt(3^6)=27/32. There are at most two flips, so the triangle inequality gives total weighted norm at most 35/16+2(27/32)=31/8 and square 961/64<16. Subtracting the unweighted mass only improves the bound. Consequently

 sum_{S nonempty}(Z'_S)^2/Z_S <=16 J.                    (6)

Let c0=1/ln2<3/2. Away from zeros of A, E=sum p log2(Z/p) satisfies the exact differentiation identity

 E''=sum p''log2(Z/p)-c0 sum p''
       -c0 sum[p'/sqrt(p)-sqrt(p)Z'/Z]^2.

The first term is nonnegative. Summing over all 64 rows gives sum p''=(u^2+v^2)/32 and sum p'^2/p=(u^2+v^2)/16; omitting the empty row can only decrease these nonnegative sums. Use (x-y)^2<=2x^2+2y^2 and p<=Z, then (6). Including the bonus in T yields

 T'' >=-[(5c0/32)+(5/64)](u^2+v^2)-32c0 J.              (7)

The entropy of the joint sign law satisfies H(q)''=-c0 J. Since [(5c0/32)+(5/64)]/2<5/32, midpoint integration of (7) gives, for q=(q_++q_-)/2 and s_+-s=+-u, t_+-t=+-v,

 T(q)-(T(q_+)+T(q_-))/2
 <=32[H(q)-(H(q_+)+H(q_-))/2]+(5/32)(u^2+v^2).           (8)

All side conditions matter. First prove this along paths with positive q, on intervals excluding the finitely many zeros of the affine A_S. The function A^2 log(A^2) has a continuous first derivative at zero; the lower second-derivative bound integrates across those zeros, so they produce no negative jump. Identically zero A rows contribute zero. Z is positive on the positive-q simplex: the four deterministic coefficients at each row cannot all vanish (delta>0). Approximate boundary laws by mixing both endpoints with the same positive uniform law. Continuity extends (8) to boundary laws. For Z tending to zero, 0<=p log2(Z/p)<=Z/(e ln2) tends to zero, so no division by a vanishing endpoint is made. No infinite-dimensional limit or exchange of an infinite sum is used.

## 3. Sum over every physical controller coordinate

For the actual jth query, q_+,q_- are the conditional sign laws, u=ahat({j}),v=chat({j}), and the entropy difference in (8) is I(z_j;(a,c)). Independence of the input bits gives

 sum_j I(z_j;(a,c))<=H(a,c)<=2.

For completeness, conditional subadditivity gives H(z|(a,c))<=sum_j H(z_j|(a,c)); subtract from H(z)=sum_j H(z_j). Since (a,c) is a deterministic function of z, the resulting total mutual information is H(a,c). Parseval gives sum_j(u_j^2+v_j^2)<=Var(a)+Var(c)<=2. Thus (3),(8) imply

 G_z V(F)-2delta G_z W(h)<=64+5/16.                     (9)

This pays all physical control queries and both children, without balance or coefficient floors. The entropy H(a,c) here is at most TWO BITS of joint physical output, not the potentially large Fourier entropy of either controller. It supplies the curvature debit only; it does not replace the original marked owner.

## 4. The DATA query retains the same signed mark

Put R=W(h)-(V(a)+V(c))/2. For each of the five DATA bits other than bit 0, both edits survive together in one child at density 2delta; its nonempty-control contribution is at least 4delta W(h), while the other child's V is nonnegative. Hence its decrement is at most T(q).

At bit 0, the two children each have one edit at density 2delta. Their nonempty-control contributions average to at least delta[V(a)+V(c)]; the DATA bonuses and empty-control terms are nonnegative for arbitrary child seeds. Thus this decrement is at most 2delta R+T(q). Both outcomes are used. Summing gives

 G_DATA V(F)-2delta R<=6T(q)<1167/32.                   (10)

Combining (9),(10), with Gmark=G_zW+R, yields residual <3225/32<101. The sign of R cancels exactly and is never replaced by an absolute debit. T>=0 proves (2).

The physical edit set has probability at most 2delta. Each DATA influence changes by at most twice that probability. Since I(b)=3/2,

 I_DATA(F)>=3/2-24delta=9/8,
 101<288=256*(9/8).

This proves (1) at all allowed means, including opposite constant controllers and the corner with 28 cancelled Fourier rows.

## 5. Scope, ancestry and the first unpaid line

Every CONTROL restriction retains the same six-bit DATA seed and original mark, so the pointwise theorem applies to all such unbalanced descendants. This is not permission to renew a bank at those descendants. For an adaptive tree querying only controls, the exact T differences telescope to T(root)-E T(leaf)<=T(root)<389/64; the same mark remains in every full terminal. No repeated credit is created.

DATA restrictions change the seed; (10) is a single complete root DATA sum with the original children, not an all-history DATA eligibility theorem. Initial source eligibility for arbitrary cores, arbitrary DATA histories, and an influence-priced original marked source remain unproved. In particular neither balanced nor unbalanced fixed-carrier transfer settles universal GU or FEI. The next mathematical step is a compatible ORIGINAL marked source admitting arbitrary cores and required DATA descendants, with old debits and both full terminal/KL bills retained.
