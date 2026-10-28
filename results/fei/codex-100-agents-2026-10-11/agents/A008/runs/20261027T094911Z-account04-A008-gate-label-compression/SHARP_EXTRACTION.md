# A sharp cost criterion and a cheap source whose conditioned core is expensive

All logarithms are base two. References are fixed before the spectral sample. These statements concern reference extraction, not an obstruction to optimized whole-set coding or to FEI.

Let Omega be a finite alphabet, E a subset with at least two atoms, p a nonnegative weight on E of positive total mass v, and u a nonnegative weight on Omega. For every strictly positive subprobability R on Omega put Z=sum_E R and r=R/Z on E. Define C_p(r)=sum_E p log(1/r) and C_u(R)=sum_Omega u log(1/R). For any beta>0,

    C_p(r) <= beta C_u(R) for EVERY such R

holds if and only if p(e)<=beta u(e) for every e in E. Necessity remains true if any fixed finite additive allowance is put on the right.

For sufficiency, log(1/R)>=0 and log Z<=0 give C_p(r)=sum_E p log(1/R)+v log Z<=beta C_u(R). This retains the exact surplus identity with a=1/beta:

    C_p(r)=(D-B)/a+v log Z,
    D=sum_E u log(1/R), B=sum_E(u-ap)log(1/R)>=0.

For necessity, fix an atom j and positive masses at every other atom with total at most 1/2; let R(j)=t tend to zero. Another E atom has a fixed positive mass, so Z stays bounded above and away from zero. The coefficients of log(1/t) on the two sides are p(j) and beta u(j). All other terms stay bounded. Thus p(j)>beta u(j) contradicts the proposed inequality, even with a fixed additive allowance. In particular u(j)=0<p(j) is fatal. The two-atom condition matters: on a singleton sector r=1 and its cost is always zero. Positivity of R can be relaxed to spectral coverage by approximation, but is sufficient for the sharp necessity test.

If R=Q/theta is a conditioned raw output reference with fixed theta>0, replacing R(j) by t only adds bounded log theta terms. The exact identity is C_p(r)=(D_Q-B_Q)/a+v log Q_E. Neither root nor sector conditioning changes the divergent coefficient in the preceding test. This does not permit changing the original generator for an actual coding application.

## A positive prime-clause family

Use 0/1 inputs for the description and sign outputs for Fourier analysis. For s,L>=1 set

    g_s=2[z OR AND_(i=1..s) x_i]-1,
    F_s,L=2 AND_(i=1..s,l=1..L)(z OR x_i OR y_i,l)-1.

Every displayed clause is a prime implicate and is irredundant: falsify its z,x_i,y_i,l, make the other private bits in group i true, and make all other x variables true. Removing z, x_i, or its private literal is witnessed by changing that literal to true in this assignment. A private bit is relevant by the same assignment. The positive core CNF is AND_i(z OR x_i). Its false density is (1-2^-s)/2<=1/2, so the orientation used in A007 has already been imposed.

Write epsilon=2^-L, a=(1+epsilon)/2 and b=(1-epsilon)/2. Averaging the private bits gives success probability one when z=1 and product_i[epsilon+(1-epsilon)x_i] when z=0. In the character convention chi_S=(-1)^sum_(i in S) bit_i, the empty core coefficient is a^s and the z-only coefficient is -(1-a^s). If S contains k>=1 x variables and optionally z, its core coefficient is (-1)^k a^(s-k)b^k. Indeed the conditional sign polynomial is -chi_z+(1+chi_z)product_i(a-b chi_i). The corresponding core coefficient of g_s has magnitude 2^-s.

Therefore the squared amplitude ratio at these S is

    (1+epsilon)^(2(s-k))(1-epsilon)^(2k),

whose minimum is (1-epsilon)^(2s), attained at all s x variables (with either choice of z). The z-only ratio is no smaller: 1-a^s=(1-a)sum_(k=0..s-1)a^k >=(1-epsilon)(1-2^-s)>=(1-epsilon)^s(1-2^-s). Consequently the EXACT best coefficient in arbitrary-reference extraction is

    beta_s,L=(1-2^-L)^(-2s).

This is a minimax statement over supplied references, not a lower bound against the best chosen reference. Exact physical edges give

    I(g_s)=1+(s-1)2^-s,
    I(F_s,L)=1-a^s+(s/2)[1+(L-1)epsilon]a^(s-1).

For fixed L both influences tend to one. Even a transfer normalized by physical influence has optimal factor beta_s,L I(F_s,L)/I(g_s), unbounded with s.

For 0<delta<=1, beta_s,L<=1+delta requires epsilon<=delta/(2s): (1-epsilon)^(-2s)>=(1+epsilon)^(2s)>=1+2s epsilon. Conversely epsilon<=delta/(4s) suffices, since Bernoulli gives (1-epsilon)^(2s)>=1-2s epsilon>=1-delta/2>=1/(1+delta). Thus the necessary and sufficient multiplicity scales for this family differ by at most one bit:

    L >= ceil(log2(2s/delta)) is necessary,
    L >= ceil(log2(4s/delta)) is sufficient.

This does not establish a logarithmic upper bound for arbitrary positive cores. A007's O(s+log(1/delta)) choice remains a valid general sufficient bound.

## The obstruction persists even for a uniformly cheap supplied source

Fix L=1, so F_s,1=z OR AND_i(x_i OR y_i) in sign form, a=3/4 and physical dimension 2s+1. Let u be its actual squared Fourier law on ALL nonempty output sets. Let j be the set of all x_i, excluding z and private variables. Then p(j)=4^-s, u(j)=16^-s. Set M=16^s and define the complete fixed output subprobability

    R(j)=u(j)2^(-M)/2,
    R(A)=u(A)/2 for every other nonempty set with u(A)>0.

Zero spectral atoms may have reference mass zero; coverage holds for every positive target. All choices use the explicitly given family and j, before any sample. This is a reference on complete spectral outputs: names, masks and output ambiguity are already resolved by the output atom. It does not assert realization by a PI-J gate queue.

With v_F=sum_nonempty u, its complete nonempty ideal cost is EXACTLY

    C_F(R)=H_nonempty(F_s,1)+v_F+u(j)M
          =H_nonempty(F_s,1)+v_F+1 <=H(F_s,1)+2.

The z-only mass is (1-a^s)^2. Splitting that atom from all others gives H(F_s,1)<=1+2a^s(2s+1). Since s a^(s-1)<=sum_(k=0..s-1)a^k<=4, this is <=29/2. Also I(F_s,1)>=3/4: for s=1 it equals 3/4, and for s>=2 its displayed formula is >=1. Thus C_F(R)<=33/2<=22 I(F_s,1), uniformly in s. This bound uses full entropy only for this explicit easy family and supplies its own elementary dimension-independent estimate; it assumes no FEI theorem.

The core sector E contains all nonempty subsets of z,x. Its reference mass Z is at least R({z})=(1-a^s)^2/2>=1/32. All reference costs are nonnegative. Therefore

    C_g(r)=sum_E p log(1/R)+Var(g)log Z
          >=p(j)M-5 >=4^s-5.

The SAME fixed supplied source is uniformly cheap, but its conditionally normalized core reference costs unboundedly more than I(g_s)<=5/4. If a normalized nonempty source is desired, divide R by its total T<=1/2; the source cost decreases by v_F log T<=0 and r is unchanged. A fixed raw root factor theta gives exactly the same r and does not remove the lower bound. Integral prefix rounding can be handled with one global bit here since I(F)>=3/4; the statements above use ideal bit costs.

The full empty/nonempty wrapper is also paid. With R'=R/T, set Q(empty)=1-v_F and Q(A)=v_F R'(A) at nonempty sets. Then the COMPLETE full-output cost is h2(v_F)+C_F(R')<=35/2<24 I(F). Conditioning Q to the core sector gives the identical r. There is no latent gate/attachment choice to reveal: each atom names the entire physical spectral subset, including the empty set. Set ell(A)=ceil(-log Q(A)); Kraft's inequality holds. Sort atoms by (ell(A), public lexicographic rank of A), give the first atom the all-zero word of its length, and obtain each next word by incrementing the previous integer and shifting left by the length increase. Kraft's inequality prevents overflow; the resulting canonical words are prefix-free. A decoder using the fixed public trie returns exactly the entire subset. The expected length is less than the full ideal cost plus one, at most 37/2<=25 I(F). These are explicit output references and codes, not a claim that the original prime-implicant queue realizes Q. Gate names, attachments and masks have been replaced by the complete output atom in this new reference; no original queue bill is deleted.

This counterexample refutes fixed-L extraction from EVERY cheap supplied positive-lift reference. It does not refute existence of a good core reference (this core is easy), a supplied structured reference with coefficient domination, A007's dimension-dependent finite extraction, or any universal FEI bound. The reference deliberately underweights one rare core atom, with its small lifted mass paying only one extra source bit. The first unpaid universal step is still an ORIGINAL complete source for arbitrary interacting cores; a conditioning argument must state how its coefficient losses are paid.
