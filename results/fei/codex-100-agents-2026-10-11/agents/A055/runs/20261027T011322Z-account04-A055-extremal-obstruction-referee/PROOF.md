# Untouched arbitrary cores obstruct short eligible continuations

Uniform Boolean signs, entropy in bits. Let a(f) be the minimum influence
over invertible affine input maps and output characters, and D_K(f)=H(f)-K a(f).
All physical leaves retain their original uniform reaches. K>=0 throughout.

## 1. Full affine minimum is exactly tensor additive

For a direction v set m_f(v)=min(Pr[f(x+v)!=f(x)],Pr[f(x+v)=f(x)]).
For any input-direction basis, an output character can prescribe its derivative
sign independently on every basis vector. Consequently a(f) is the minimum
basis sum of m_f. This includes constants, characters, zero costs and redundant
directions. Translation of the input changes none of these quantities.

For disjoint factors f_j and F=product_j f_j, independence gives

  1-2m_F(v_1,...,v_t)=product_j(1-2m_fj(v_j)).

Every factor on the right lies in [0,1], so m_F(v)>=max_j m_fj(v_j).
Let r_f(s) be the dimension of the span of directions with m_f(v)<=s.
The preceding inequality yields r_F(s)<=sum_j r_fj(s). The minimum basis
weight formula is

  a(f)=integral_0^(1/2) [n-r_f(s)] ds.

For completeness, the greedy minimum-weight basis contains r_f(s) vectors
of weight <=s at every threshold between the finitely many weights: any
smaller number could be augmented from their span, replacing a heavier
vector. Integrating the count of basis vectors heavier than s proves the
formula. Endpoints have measure zero. Thus a(F)>=sum_j a(f_j). Conversely,
the union of factor-optimal bases has exactly that cost, proving equality.
Squared Fourier spectra are products, so H(F)=sum_j H(f_j). Therefore

  D_K(product_j f_j)=sum_j D_K(f_j).                         (1)

This proof requires no FEI inequality or affine minimality hypothesis.

## 2. A pathwise full-terminal lower bound

Fix an n-bit seed h with d=D_K(h)>0, and t disjoint copies. Consider ANY
finite adaptive physical data-query tree on their product, with no intermediate
mixing of coordinates between seed blocks or nonlinear phase multiplication.
Queries may depend on every previous answer; stopping may be arbitrary.
Along a leaf let T be the number of seed blocks touched and Q the number of
distinct data coordinates queried. Repeated queries may be deleted; Q counts
distinct coordinates in the leaf cylinder. Untouched seeds remain exactly h.
A touched block with q_j queried coordinates has n-q_j remaining coordinates.
For every Boolean u on b coordinates, H(u)>=0 and a(u)<=b/2, since each
centered directional cost is <=1/2. Hence D_K(u)>=-Kb/2. Applying (1) gives

  D_K(leaf)>=td-(d+Kn/2)T+(K/2)Q.                          (2)

All factors remain present, including constants. Discarding a constant factor
is harmless because its affine deficit is exactly zero. The inequality holds
for every cylinder independently; adaptivity does not alter conditional
uniformity on the coordinates not queried.

Average (2) with the ORIGINAL reaches. If the complete optimized child
reserve S=-E D_K(leaf) is nonnegative, then

  (d+Kn/2) E T >= td+(K/2) E Q,
  E T >= td/(d+Kn/2).                                      (3)

The denominator is positive because d>0. If every individual leaf is a
K-nonviolator, each path obeys the analogous pointwise lower bound. Conversely,
if E T<td/(d+Kn/2), then the same full reserve is strictly NEGATIVE, and
E[(D_K(leaf))_+] >= td-(d+Kn/2)E T >0. This is an actual terminal obstruction,
not a claim that a local upper bound must be saturated.

## 3. Rare activation and the explicit previous witness

Let F=1+A_k(Q_gadget product_j h_j-1), where A_k is a k-bit point event,
p=2^-k, and Q_gadget is ANY fixed Boolean sign on independent gadget bits.
First resolve all controls and gadget coordinates; on inactive branches F=1,
and on active branches it is a constant sign times the seed product. Then
allow ANY adaptive data-only stopping tree, possibly depending on the resolved
gadget assignment. At original reaches, with conditional expectations over
the active branch (and all gadget assignments),

  -S >= p[td-(d+Kn/2) E(T|active)+(K/2) E(Q|active)].         (4)

No p is cancelled when it is zero; here k is finite and p>0. Thus rarity
cannot make the exact eligibility condition easier: (3) holds conditionally
on activation with precisely the same coefficient. Absolute reserves can
still be arbitrarily small. No root reserve or query payment is recredited.

For the prior depth-five NAND32 certificate at K=17/4, d>1/8, n=32.
The function x/(x+68) is strictly increasing for x>0, so (3) forces

  E(T|active)>t/545.                                       (5)

For the earlier t=100000000 source, integer-valued E T need not be an
integer, so no ceiling is applied to the expectation. A pointwise eligible
leaf must touch more than t/545 blocks (there an integer ceiling is valid).
The explicit NAND application is CONDITIONAL on that previous seed certificate;
the general theorem and the new AND2 example need no such dependency. AND2
has H=2,a=1 and d=1 at K=1, giving E T>=t/2 exactly.

## 4. Independent review of A052 near-optimum rank rigidity

A052 stage11 starts with the already independently reconstructed bound
D_K^aff(fP)<=D_K^aff(f)-r*m, m=K(2^(1-d_phase)-4delta)-1>0.
For an actual joint competitor g, I(g)>=a(g), so D_K(g)<=D_K^aff(g).
If D_K(g)>=D_K^aff(f)-epsilon, epsilon>=0, combining yields r*m<=epsilon.
Division by m>0 gives r<=epsilon/m. Since r is a nonnegative integer,
epsilon<m forces r=0. A real Boolean phase with singleton Fourier support
is a signed character by Parseval. At epsilon=m, r=1 is not excluded by
these inequalities. Comparing against the actual root deficit requires
I(f)=a(f); comparing against D_K^aff(f) does not. This reconstructs the
corollary without repair; it adds no acceptance of the giant witness.

## 5. Boundary, hypothesis and scope audit

The tensor identity is checked with all constants and characters; no division
by an influence occurs. Equation (2) also holds when d<=0, but the positive
occupation conclusion explicitly requires d>0. K>=0 is used when multiplying
the upper bound a<=b/2. A full query has constant factors and Q=nT, correctly
leaving only untouched positive d. At t=0 there is no positive occupation
conclusion; the theorem assumes t>=1. Expected eligibility and pointwise
eligibility are distinguished. The fixed-K seed d, not a root-ratio seed,
appears in (2)--(5). The theorem concerns complete optimized descendants,
so raw physical nonviolation alone is not asserted to imply (3).

Arbitrary affine changes or phase multiplication DURING the data tree can
destroy the physical tensor factorization. Equation (2) is not claimed for
those policies. A genuine least-dimensional violating root still excludes
these embedded cores already; nothing here turns an embedded root into one.

## 6. First unpaid universal line

Derive an ORIGINAL proper-pair selection/payment theorem on a genuine
high-K critical source, retaining phase price, mixed rows, unused quotient
rank and exact nonnegative complete-child reserves. The present result
rules out replacing that condition by a bounded-touch physical cleanup
of the already phase-extremal rare cores. It does not prohibit a paid
growing-depth continuation, nor fund one. Universal FEI remains OPEN.
