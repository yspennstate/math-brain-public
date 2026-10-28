# Exact dyadic boundary transport for a prime selector completion

All logarithms are natural. Functions are actual finite Boolean signs under
an interior independent product law. The selector is a distinct physical
coordinate. No spectral-conditioning or repeated-wire interpretation is used.
Full FEI remains OPEN.

## 1. Independent reconstruction of A043's completion

For an essential n-variable core f, n>=3, let q be an input reflection of
the sign threshold T_2^n. Exclude q=f,-f and f with one input reflected.
The 2^n reflections are distinct: every essential coordinate of T_2^n
has a fixed positive monotonicity orientation, reversed by its reflection.
There are at most n+2 forbidden functions and 2^n>n+2, so a q exists.

Set G(x,z)=f(x) at z=0 and q(x) at z=1. A proper Boolean wire block
permits at most two distinct cofactor rows. T_2^n has three rows through
every proper block with at least two coordinates: inside counts0,1,2
against outside counts0,1 give --,-+,++. For a proposed block of G,
restricting z=1 excludes every block with at least two x coordinates
and at least one outside x coordinate. The remaining blocks are all x,
or {z,x_i}. For all x, two row pairs (f(x),q(x)) would force q=+/-f.
For {z,x_i}, essentiality gives two distinct rows on each face; their
union has size<=2 only when the two ordered face pairs agree or reverse,
forcing f=q or its i-reflection. Each was excluded. This independently
reconstructs primeness, essentiality, and the exact n>=3 hypothesis.

For fixed core biases put a_S=c_S(f), b_S=c_S(q), v_S=product v_i.
The exact physical coefficients are

 c_S(G)=(1-e)a_S+e b_S,
 c_{S+z}(G)=(b_S-a_S)/2,       v_z=4e(1-e).             (1)

These follow by expanding G=f+z(q-f), z=e+(Z-EZ)/2, including S=empty.
Their actual masses and influence/entropy have the source's fixed-n
continuous limits. Finite sums and t^2 ln(1/t^2)->0 at t=0 justify the
limits; no uniform-in-n continuity rate is inferred. The same argument
uses the undivided corrected inequality when Delta=0. Verdict on
A043-PRIME-SELECTOR-COMPLETION@1: HOLDS at its original scope.
No arbitrary-core payment is accepted by this review.

## 2. Exact directional rounded-scale limit

Use upper rounding 1/2<2^{j(c)}|c|<=1. For occupied HIGH core sets
(|S|>=2), let D be those with |a_S|=2^{-k}, integer k>=1, and
a_S(b_S-a_S)>0. Define the actual outward dyadic mass

    d=sum_{S in D}v_S a_S^2;   M=sum_high v_S a_S^2.

Then the limit exists and equals, exactly,

    lim_{e downarrow0} J_hi(G)=J_hi(f)-ln4 d.             (2)

At a nondyadic nonzero atom j is locally constant. At a dyadic atom an
outward approach has j=k-1 for every sufficiently small positive e;
an inward or constant approach keeps j=k. At |a|=1 no outward approach
is possible because |b|<=1. At a=0, c^2 j(c)->0. New selector-containing
high atoms have O(e) mass and fixed normalized coefficients. These facts,
applied to the finite physical label partition, prove (2) with no liminf
gap. In particular 0<=d<=M<=Delta; the coarse source bound is recovered.

## 3. The same complete reference transports its lost scale

Preserve actual masses on empty and singleton labels. On high labels put
W(S)=v_S4^{-j_S}, Z=sum_high W, Q(S)=M W(S)/Z. If M=0 set Q=P.
Let L_hi=sum_high P ln(1/(2^j|c|)^2), n=M ln(Z/M),
K=KL(P||Q)=n-L_hi. This is an ordinary full probability reference.

At the endpoint, every atom in D has W_f(S)=P_f(S). Under the outward
approach its W limit is4P_f(S), while every other occupied old W limit
is unchanged. At zero and new selector atoms W<=4P, so their W vanishes.
For M>0 it follows that

 Z_G -> Z_f+3d,
 L_hi(G) -> L_hi(f)+ln4 d,
 n_G -> n_f+M ln(1+3d/Z_f),
 K_G -> K_f+M ln(1+3d/Z_f)-ln4 d.                     (3)

The final KL DIFFERENCE is signed; it is not new available credit. Both
full endpoint laws are specified: Q_f has high weights W_f, whereas
Q_limit has high weights W_f+3P_f 1_D, with total high mass M and the
same old low masses. Selector-containing Q masses vanish. At M=0 all
these charges vanish, since 0<=n,K,L_hi<=M ln4; no division by M is used.

Substitution in J_hi+n-K shows exact cancellation of the lost scale:

 lim(J_hi(G)+n_G-K_G)=J_hi(f)+n_f-K_f.                 (4)

The SAME corrected high entropy is retained; there is no refund to spend
twice. The actual singleton and empty sectors converge separately to
their full f sectors. Old singleton imports and low/high carries, if
present in a larger formula, remain booked to their original owners.
Equation(4) does not bound its value by influence or pay the core.

## 4. When reflection can remove the jump: an exact character test

Specialize to FAIR core inputs. Write b^0_S=hat T_2^n(S). For reflection
sigma in {0,1}^n, b^sigma_S=(-1)^{sigma dot S} b^0_S. A high set is
dangerous only when a_S is nonzero dyadic and |b^0_S|>|a_S|. At a dangerous
set, zero outward jump requires

    (-1)^{sigma dot S}=-sign(a_S b^0_S).              (5)

Thus zero jump is exactly feasibility of these parity equations, followed
by excluding the at most n+2 forbidden completion faces. Linear algebra
over F_2 tests feasibility; if consistent with rank r, there are2^{n-r}
solutions before exclusions. This is a characterization, not an assumed
independence of constraints. In particular any XOR dependency among the
sets must have the same XOR dependency among their prescribed bits.

For every essential fair core on n=3 or4, an admissible zero-jump q exists.
Indeed every nonzero core coefficient has magnitude at least2^{1-n}.
Directly summing the n+1 negative vertices of T_2^n gives, for |S|=k>=1,

    b^0_S=(-1)^{k+1}(n+1-2k)/2^{n-1}.               (6)

For n=3 the only possible dangerous high atom is the triple, where
|b^0|=1/2; danger requires |a|=1/4. A reflection reversing that sign
removes the jump. Such an f cannot be +/- a reflected T_2^3 (their top
magnitudes are1/2), so ALL reflection faces are eligible. Without a
dangerous atom use the source completion selection.
For n=4, degrees2 and3 have |b^0|=1/8 and cannot be dangerous. Only the
full set, |b^0|=3/8, can be dangerous, with |a|=1/8 or1/4. Again half
the reflections reverse its sign and all are eligible since f has a
different top magnitude from every +/- reflected threshold face.
This proves the all-core claims analytically; exhaustive checks are separate.

## 5. Five core bits force a jump for EVERY admissible reflection

Let n=5 and f=+1 only at x=00000, and -1 elsewhere, on fair inputs.
It is essential. Every nonempty coefficient has magnitude1/16 and j=4.
Every q_sigma=T_2^5(x xor sigma) is eligible: q has26 positive vertices,
-q has6, and every reflected f has1. No forbidden equality is possible.

At degrees2,4,5, the threshold magnitudes are respectively1/8,1/8,1/4;
degree3 is zero. All these nonzero high levels are dangerous. For a
reflection of Hamming weight r, the number N_r of outward atoms is

 N_r=r(5-r) + (5-r if r even, r if r odd) + 1_{r even}.

The three terms count pairs of odd reflection parity, four-sets of even
reflection parity, and the full-set even parity, respectively. For
r=0,1,2,3,4,5 the exact counts are6,5,10,9,6,5. Thus

    min_sigma d_sigma=5/256>0.                       (7)

There is no zero-jump allowed reflected threshold, even chosen after f.
Equivalently, two disjoint pair constraints in(5) force even parity on
their four-set while that four-set constraint demands odd parity.
This is the first possible core arity among n>=3: section4 covers n=3,4.

For this seed M=26/256, Z_f=M, K_f=L_hi(f)=n_f=0, and
J_hi(f)/ln4=104/256. The BEST reflected completion still has limit
J_hi(G)/ln4=99/256. Its limiting full-reference KL is positive and equals

    [26 ln(41/26)-5 ln4]/256.                        (8)

For every reflection, replace5 with its actual N_r in(8). Positivity
also follows directly from strict KL nonnegativity: both jumped and
unjumped high atoms exist and Q_limit differs from P_f. The rational
log-interval checker verifies all four occurring N values independently.
The jump is rounding/reference transport, not lost entropy or a FEI
counterexample. Other prime-completion classes are not excluded.

## 6. Exact unpaid line

The source prime completion localizes an arbitrary retained core inside
one rare selector. Equations(2)-(4) now transport its exact rounded scale,
normalizer, ordinary KL and BOTH full endpoint laws. Selecting a clever
reflection cannot generally make the scale jump disappear, as (7) proves.
The still unsupported line is paying the retained arbitrary-core high
entropy from SAME unused original influence after prior singleton/import/
carry commitments. Continuity and exact reference conversion supply no
such initial price. The next useful mechanism must fund that source,
rather than discard the forced dyadic transfer or repeat an endpoint limit.
