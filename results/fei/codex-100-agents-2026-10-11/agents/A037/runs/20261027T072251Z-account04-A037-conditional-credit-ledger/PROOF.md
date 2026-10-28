# A free calibration need not pay the next physical query

All laws are finite and all information is in bits. Full FEI remains OPEN. This stage independently reconstructs A050's supplied-source calibration theorem and gives a Boolean counterexample to a stronger, invalid way of spending its released credit. The new result is an author proof with exact certificates; external independent review is pending.

## 1. Independent reconstruction of the actual physical ledger

Let p be a Boolean squared Fourier law. Let q=b p+sum_j c_j delta_Wj, with b>0, c_j>=0 and b+sum c_j=1. Labels can be ghosts and can collide. Delete the queried frequency bit to obtain R=Mp and Z=Mq. For physical child laws p_t, Fourier restriction gives (p_0+p_1)/2=R. On occupied rows set k_t(U)=p_t(U)/(2R(U)); complete source-zero rows by ANY common stochastic pair. Then r_t=sum_U Z(U)k_t(U)>=b/2>0 and q_t=Z k_t/r_t. The true physical outcome weights remain 1/2. Ghost reference mass stays in r_t and q_t.

Apply finite log-sum separately to each erased fiber and the exact joint KL chain to R(U)k_t(U), Z(U)k_t(U). With A=D(p||q), E=A-D(R||Z)>=0, O=D((1/2,1/2)||r)>=0, the result is

    A=E+O+average_t D(p_t||q_t).                         (1)

This uses the same channel on both joint laws, not a phase-blind parent-to-child kernel. Every positive target row has positive reference mass, and both outcome normalizers are positive. No stochastic source-zero completion is discarded.

At a node with t=p(empty), z=q(empty), match vacuum by setting q*(empty)=t and q*(s)=(1-t)q(s)/(1-z) for nonempty s when t<1. If t=1, set q*=p. Finite KL makes all required denominators positive. Direct expansion gives

    D(p||q)-D(p||q*)=d=D(Ber(t)||Ber(z))>=0.             (2)

Endpoints t=0,1 follow directly with 0 log 0=0. The nonempty conditional distribution is preserved. For t<1 put k=(1-t)/(1-z), b*=kb. Since q>=bp implies 1-z>=b(1-t), 0<b*<=1. Scale nonempty witness weights by k and replace all empty weights by t(1-b*). These coefficients are nonnegative and normalized. Thus no new nonempty witness is needed; all empty weights occupy one slot. This independently accepts A050's exact repeated calibration statement without a substantive repair.

If calibration is made before each query and at terminal nodes, (1)-(2) give, with raw incoming A_v,

    A_v=d_v+E_v+O_v+average_t A_vt.                     (3)

For every finite adaptive stopping tree, summing by the ORIGINAL physical reaches gives

    A_root=sum_all_reached w_v d_v
           +sum_internal w_v(E_v+O_v)
           +sum_terminal w_v D(p_v||q*_v).             (4)

The same identity holds conditionally at each reached node with its ACTUAL incoming A_v, and includes both complete terminal laws. Every term on the right is nonnegative. Hence the total released calibration credit is at most A_root; it cannot also remain available as its former KL at a descendant. In cross-entropy units, if B_v=H(p_v)-H(Mp_v) and J_v=H(Mp_v)-average H(p_vt), then B_v+average CE_child=CE_raw_parent-d_v-J_v-E_v-O_v. This is precisely the full ledger, including query KL, not just an endpoint functional.

## 2. A strictly stronger local payment rule is false on AND2

Consider the genuine two-bit Boolean table f=(1,1,1,-1), with bit0 changing fastest. Its squared Fourier law on (empty,{0},{1},{0,1}) is p=(1/4,1/4,1/4,1/4). Use the complete positive reference

    q=(63,1,32,32)/128.

This is a legal supplied moving-witness mixture: choose b=1/32 and residual masses (31/64,0,31/128,31/128) on (empty,{0},{1},{0,1}); their sum is 31/32. In particular q>=bp and no ghost or support singularity is involved.

Query bit0. The child at 0 is constant and the child at 1 is a dictator. The coherent outcome kernel is deterministic on the two erased frequency rows. Before calibration, the empty erased row has mass (63+1)/128=1/2, so r=(1/2,1/2) and O_old=0.

Vacuum calibration produces

    q*=(1/4,3/260,24/65,24/65).

Its released credit is

    d=(1/4)log2(32/63)+(3/4)log2(96/65)>0.

Its query outcome law is r*=(17/65,48/65), whence

    O_new=(1/2)log2(4225/3264)>d.                        (5)

To certify the strict sign without numerical logarithms, multiply O_new-d by four. Its base-two exponential is the rational number

    R=(4225/3264)^2 / [(32/63)(96/65)^3]>1.

Clearing its positive integer denominator verifies the sign. The exact value and comparison are recorded in out/CHECK.json. Thus even the inequality O_new-O_old<=d is FALSE. Free calibration can create more next-query KL debt than the credit it releases. Matching the vacuum does not permit omitting O, nor does the released credit alone fund a required subsequent query.

## 3. The witness is stable and does not contradict conservation

For 0<epsilon<1/2, take q_epsilon=(1/2-epsilon,epsilon,1/4,1/4) on the same actual Boolean p. All four reference probabilities are positive; choosing b<=4 min q_epsilon represents it as an allowed finite mixture. The uncalibrated query remains fair. If z=1/2-epsilon, calibration gives the first outcome probability

    r*_0=(1+t-2z)/(2(1-z)),  t=1/4,

which tends to 1/4 as epsilon decreases to zero. Hence O_new tends to 1-(1/2)log2(3), whereas d tends to (3/4)log2(3)-1. Their difference tends to 2-(5/4)log2(3)>0, certified by 2^8=256>243=3^5. Continuity on positive probabilities gives an interval of genuine full-support references with the same strict failure. The singular endpoint itself is not used as a counterexample. The explicit epsilon=1/128 above supplies an exact member.

Before and after calibration, the actual normalized reference children for this query are the exact constant/dictator child spectra. Their terminal KL and their child vacuum releases vanish. Therefore (1)-(2) reduce to

    A_old=E_old,
    A_old=d+E_new+O_new.

Consequently E_old-E_new=d+O_new>2d. The missing next-query payment is supplied by reduced erasure KL, not renewed original capacity. This explains precisely why the full original account survives and a release-only subaccount fails. Terminal entropy, source cross-entropy and any old bill remain separate obligations.

## 4. Scope, checks and unpaid universal step

Potential failing checks are: genuine Boolean realization; correct bit and child ordering; reference normalization and b>0; use of actual coherent outcomes; ghosts on source-zero rows; fair physical rather than reference branch weights; constant and zero-vacuum endpoints; full conditional tree telescope; and strict logarithmic comparison. The independent checker uses literal Walsh sums, rational probabilities and prime-log vectors, importing no peer implementation. All signs used in the explicit counterexample are rational-power integer comparisons. The finite census supports the all-tree derivation; it does not replace it. A core Lean check is requested for the cleared strict integer sign only; its pass, if obtained, does not certify the entropy theorem.

The accepted source scope is A050 20261027T005654Z PROOF sections1-4. Its theorem already retains O and is not refuted. A039's moving-anchor budget also retains O; its full source is not independently accepted here. A094's original query-KL objection supplies motivation only; no unverified peer claim is used to derive (1)-(5).

FIRST UNSUPPORTED UNIVERSAL LINE: supply a noncircular influence-priced ORIGINAL complete reference for arbitrary Boolean cores, or pay a genuinely necessary compatible query/stopping rule from the SAME unused original resource, with erasure KL, query KL, all previous bills and both full terminals retained. Neither free vacuum calibration nor charging only its releases proves that line. Full FEI remains OPEN.
