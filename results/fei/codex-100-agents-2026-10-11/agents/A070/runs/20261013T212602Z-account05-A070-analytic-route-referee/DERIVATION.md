# Stage 2 independent analytic referee

All cubes have uniform probability measure, all entropies/code lengths use bits. Physical influence is defined only for Boolean signs. For a normalized real vector use E_spec=sum |S| fhat(S)^2 instead; substituting it for Boolean pivotal probability requires proof.

## 1. Original lead neutralization: exact scope and boundary correction

The incoming statement is B14-LEAD-POINT-DEFECT-NEUTRALIZATION v1, source CLAIMS.json in 20261011T224500Z-claude-B14-granularity-neutralization. Its one-point formula, influence comparison, spectral L1 bound, fixed-seed asymptotics and FEI equivalence are correct. The stated global boundary scope needs repair. A067 stage 2 already identified the n=1,N=2 entropy-domain issue; we independently confirm it and do not claim it as new.

1. At n=1,N=2 the declared eps=2*2^-2*(sqrt(2)+1)=(sqrt(2)+1)/2>1, so h2(eps) in clause (c) is undefined. A bound involving this expression cannot be accepted for every N>n.
2. If zero-dimensional Boolean functions are included, take f=1 on n=0 and N=1. Edit the all-plus point: g=-x_1. Anchor A={1} gives g chi_A=-1, whose coefficient at [N] is zero. Thus clause (a)'s EVERY-anchor assertion is false at this allowed boundary, although the unanchored top coefficient remains nonzero. The exact two-sign witnesses are in out/CONTROL_CHECK.json. This additional obstruction was not in the inspected A067 caveat.

Repair the theorem by requiring N>n and N>=2, and replace its entropy expression by the following all-parameter bound. Put delta=2^-N, eps_raw=2delta(2^(n/2)+1), and eta=min(eps_raw,1-2^-N). Then

    |H(g_N)-H(f)| <= h2(eta)+eta log2(2^N-1).       (N1)

Here g_N(x)=f(x_1,...,x_n)(1-2*1{x=x0}). The coefficient update is

    ghat_N(S)=fhat(S)*1{S subset [n]}-2delta f(x0) chi_S(x0). (N2)

For n>=1, each nonzero fhat is an even integer Walsh numerator divided by 2^n, hence has magnitude >=2^(1-n). The edit magnitude 2^(1-N) is strictly smaller. Old nonzero coefficients remain nonzero and all zeros become nonzero. For n=0 and N>=2 the old empty coefficient has magnitude one, while the edit magnitude is <=1/2, so the same conclusion holds. Every coefficient is nonzero. Multiplication by any character permutes coefficients, so every anchor has a nonzero top coefficient and d=N for every set. Therefore U(g_N)=N Var(g_N)-I(g_N).

The pivot indicator in coordinate i changes only at x0 and its neighbor, proving |Inf_i(g_N)-Inf_i(f)|<=2delta. Expanding squared coefficient differences and summing gives

    ||p(g_N)-p(f)||_1 <=4delta(sum_S |fhat(S)|+1)
                         <=4delta(2^(n/2)+1).       (N3)

For eta in (N1), if eps_raw<=1-1/M, M=2^N, the entropy-continuity function h2(t)+t log2(M-1) is increasing for 0<=t<=1-1/M and actual TV<=eps_raw. If eps_raw exceeds that threshold, the right side is exactly log2 M=N, which is the unconditional bound on the difference of two entropies on M atoms. The cap is justified by these two cases; we do NOT assume actual TV<=eta in the second case.

For fixed n, delta N->0 and eta->0. Thus H(g_N)->H(f), I(g_N)->I(f). For nonconstant f, Var(f)>0 and I(f)>0, so U/I grows linearly with N. For nonnegative psi with max_s psi(s,N)=o(2^N), the difference between the edited support functional and its seed d=N specialization is at most max psi times (N3), hence tends to zero. FEI on the corrected padded-edited class implies FEI on all nonconstant seeds with exactly the same constant by taking limits; constants satisfy FEI separately. This supplies a source-bound corrected v2, not an independent acceptance of our own repair. A070 is a contributor to v2 and recuses from its independent review.

Normalized real diagnostic: psi_n=n^-1/2 sum x_i has H=log2 n, E_spec=1, fourth moment 3-2/n and support antichain U=0. It violates a Boolean arithmetic payment if the sign assumption is removed. The neutralization formulas alone do not add a Boolean entropy payment: they identify exact-support fragility, not a universal influence estimate. The repair does not rescue the refuted one-shot U route.

## 2. Independent A068 cyclic full-support reference reconstruction

The author stage-2 REPORT.md states a theorem for odd q>=5, cyclic quadratic controlled majority F_q(x,z)=MAJ_q(x_i(-1)^(u_i u_(i+1))), N>=2q after padding, and any single input edit G. Its source folder lacks CLAIMS/PROGRESS/PACKET_DELTA and a full validation output at this stage's read cutoff. The report itself contains a complete candidate derivation; our acceptance is source-bound to that theorem, not to its asserted packaging/full-census completion.

Explicit private data labels give Fhat(S,T)=MAJhat(S) ahat_S(T), where a_S is a Boolean quadratic control phase. A088 independently accepted the underlying stage-1 reference using the pinned regular-core C001 rank theorem; this dependency remains explicit. Our new code reconstructs quadratic spectral flats by direct q-block character sums, verifies packet amplitudes against an independently recursive full-cube transform, and computes actual edges. It does not import author code or trust author polar-rank outputs.

Let c_q=binom(q-1,(q-1)/2)/2^(q-1), J=q c_q. Every data influence is c_q. Reversing control u_j toggles zero, one, or two votes with probabilities 1/4,1/2,1/4. A one-vote and a two-vote toggle each change odd majority with probability c_q, hence I_z=3J/4. The recurrence c_(q+2)/c_q=q/(q+1) gives J>=15/8 for all odd q>=5. Exact replay: q=5 has (I_x,I_z)=(15/8,45/32); q=7 has (35/16,105/64).

The base reference is

    R0(S,T)=w_|S| [prod_(i in S) i^-2 / Z_|S|] 2^-r_S 1{T in L_S},
    Z_k=sum_|S|=k prod_(i in S) i^-2.

Each affine fiber and rank level is normalized, sum R0=1. Majority is balanced, so its spectral level K>=1. The geometric reference 2^-k on k>=1 proves H(K)<=E K=J. In the accepted Euler-rank proof this replaces the generic level coefficient C_lev=log2(4+e) by one. Consequently

    Gamma0(F_q)<=B=(C_bal+3/2)J,
    C_bal=1+2log2(e*pi),
    B/J<9,
    C_reg J+2I_z(F_q)-B>(3/2)J.                   (Q1)

The last two estimates use the accepted C_reg<9 and elementary C_lev>5/2. All base geometry/reference costs remain charged.

Repair R0 by a uniform complete branch with delta=2^-N:

    R_delta=(1-delta)R0+delta U_N, U_N(A)=2^-N.

This is normalized and R_delta>=delta^2 everywhere, so L_delta<=2N. On the base, expected cost <=B+log2(1/(1-delta))<=B+3delta. For e=G-F_q each Fourier coefficient has square 4delta^2, giving weighted edit energy <=8Ndelta. Weighted triangle, before squaring, yields

    Gamma_delta(G)<=(sqrt(B+3delta)+sqrt(8Ndelta))^2. (Q2)

No incoherent entropy mixture or dropped cross term occurs. For N>=2q>=10 and J>=15/8, a=3delta/J<=1/640 and b=8Ndelta/J<=1/24. Thus the surcharge above B divided by J is <=1/640+1/24+5/4, using the rational square comparison

    4*(1/24)*(9+1/640)=5761/3840<25/16.

Physical edit influence loss in the weighted block target is at most 2q delta(C_reg+2)<11Ndelta, so divided by J it is <=11/192. Subtracting these paid costs from (Q1) gives

    H(G)<=Gamma_delta(G)
         <=C_reg I_x(G)+2I_z(G)-(287/1920)J,       (Q3)
    3/2-1/640-1/24-5/4-11/192=287/1920.

For fixed q under padding, the base branch penalty, weighted edit energy and their coherent cross surcharge vanish; Gamma_delta(G)->Gamma0(F_q). This repaired functional passes the pad-and-flip test even though edited antichains and the exact private quadratic representation need not survive. The old reference had zero probabilities on empty-data/padding atoms and could not be reused as-is.

Independent certificates cover 16 selected edits: q=5,7; N=2q,2q+2; four declared edit locations. Every complete mixture expected cost is enclosed by rational log intervals and lies below the stronger target 8I_x+2I_z, also retaining at least (287/1920)J margin. C_reg>8 follows from (4+e)e^2*pi^2>6*7*9>256. Direct physical edges agree with spectral influence in every coordinate. Finite certificates are implementation checks; (Q1)-(Q3) prove all q, all padding, and all edit locations with the stated baseline dependency.

Normalized real diagnostic specific to this route: replace MAJ_q by q^-1/2 sum_i x_i, keeping the same cyclic quadratic controls. There are 4q atoms of mass 1/(4q); H=log2 q+2, E_x=1 and E_z=1. Its fourth moment is 3-2/q, since conditioning on controls only reorients independent data signs. Hence the proposed block influence payment fails as q grows in this real-valued relaxation. The regular Boolean base's ternary pivotal antichain/rank estimate is indispensable; packet normalization or quadratic control alone does not pay the data entropy. No Boolean theorem is rejected by this outside-domain diagnostic.

Verdict: the report's all-parameter repaired cyclic theorem HOLDS at its exact scope with the source-bound accepted C001/rank dependency. A070 supplied no mathematical repair to A068's theorem. Author package completion remains unverified/incomplete at the read cutoff; B20 must assign/map its upstream claim ID.

## 3. Independent A069 stage-2 interface and addressing payment

Review A069-ALIGNED-EDIT-ENERGY-ADDRESSING v1 from the source claim file and DERIVATION (A1)-(A4),(S1)-(S5). The all-subset code is L_T(S)=1+sum_v b_v 1{S meets C_v}; for binary trees Lmax=2N-1. A070 already accepted the v1 Kraft/weighted-triangle parent in stage 1, so it is not re-opened.

For a-bit addressing, spectral samples choose one uniform data label and an independent uniform selector subset. The balanced selector tree has expected internal occupancy R(a), with R(1)=0 and R(k)=1-2^-k+R(floor(k/2))+R(ceil(k/2)). The selected data leaf occupies exactly a internal vertices. Joining selector/data subtrees, and optionally a padding tree, gives

    Gamma_T(A_a)=3+2a+2R(a)+2*1{padding}
                <=4a+3=8I(A_a)-5.

For any edit fraction rho, weighted triangle and physical edge stability prove

    Gamma_T(f)<=2Gamma_T(A_a)+8rho(2N-1)
               <=16I(f)-10+48N rho-8rho.          (A1)

This is <=16I for N rho<=1/8. For one point N>=3, N2^-N<=3/8; hence Gamma<=16I+8. Balanced addressing and a one-point flip give Var(f)>=15/16 and I>=Var, so Gamma<=(368/15)I<25I. One-point edits satisfy the 16 bound for N>=6. Root, masks, every label, padding and new tail atoms are included. Fixed a padding stability follows from Lmax=O(N). The old influence-only reference costs log2(a)+2+o(1) per unit influence; this new complete reference closes the concrete addressing gap in A070's prior NEXT.

For a proper split Z,Y with r=|Z|, join fixed binary trees at the root. Set W_Z,W_Y to their internal-mask costs. Flip g on z=z*, put h=g(z*,.), rho=2^-r, e=-2*1{z=z*}h. Its exact coefficient factorization is

    ehat(U,V)=-2rho chi_U(z*) hhat(V).

The normalized difference-spectrum law is uniform on control subsets times h's full spectrum, including its empty coefficient. Its energy is therefore

    E_e=4rho[1+2(1-rho(Eh)^2)+U_Z+E_(S_h) W_Y],
    U_Z=sum_v 2(1-2^-|C_v|).                      (A2)

The root/empty probability accounts for the correction rho(Eh)^2. Restriction Parseval gives E_(S_g)W_Y=E_z E_(S_(g_z))W_Y, so rho E_(S_h)W_Y<=E_(S_g)W_Y. Since U_Z<=2(r-1),

    E_e<=4E_(S_g)W_Y+4rho(2r+1),
    Gamma_T(f)<=2Gamma_T(g)+8E_(S_g)W_Y+8rho(2r+1). (A3)

On a free-coordinate edge either both endpoints are edited or neither is; its pivotal probability is unchanged. On a control crossing edge exactly one of g,f is pivotal; total directed crossing probability is 2rho per control coordinate, so I_Z(f)+I_Z(g)>=2r rho. The retained core is not assumed cheap, and cancellation can make f constant. Thus (A3) is an interface, not a universal Gamma<=KI payment.

Independent code uses direct character sums, literal edges, and all 4,608 three-bit subcube edit fixtures, plus 360 addressing point edits. No author implementation is imported. Verdict: A069-ALIGNED-EDIT-ENERGY-ADDRESSING v1 HOLDS/ACCEPT_AT_STATED_SCOPE, without repair. Its actual sign alphabet is used in e=-2g on edit support and in pivotal comparisons; the weighted triangle and generic code remain valid for normalized real laws, on which their expectation need not be O(E_spec).

## 4. First two-edit term: signed cell projections, not physical intersection alone

This is a new audit of the interface missing from single-edit (A2), not a universal stopping payment. Let u,v be arbitrary real functions and define

    <u,v>_L=sum_S uhat(S) vhat(S) L_T(S),
    P_C u=E[u | coordinates outside C].

Fourier orthogonality shows P_C retains exactly frequencies disjoint from C. Therefore

    <u,v>_L=(1+sum_v b_v)E[uv]
                -sum_v b_v E[(P_(C_v)u)(P_(C_v)v)]. (X1)

This identity is valid for arbitrary real functions and does not itself use Booleanity. Even disjoint physical supports only make E[uv]=0; their projected products need not vanish and can have either sign. The projection costs are exactly the additional signed information required for transport.

For two distinct single input edits x!=y of a Boolean seed g, let e_x=-2g(x)1{X=x}, e_y=-2g(y)1{X=y}. The character sum gives

    <e_x,e_y>_L=-4g(x)g(y)2^-2N
          *sum_v b_v 2^(N-|C_v|)1{x and y agree outside C_v}. (X2)

Proof: sum_S chi_S(x)chi_S(y)=0 for distinct points; the sum over frequencies disjoint from C is 2^(N-|C|) precisely when the points agree outside C. Their difference coordinate set, not physical intersection of edit events, determines which projections interact.

Actual Boolean witness on N=2: g(x)=x_1, edit x=(+,+) and y=(-,+). Root has two children, so L(empty)=1 and L(S)=3 for nonempty S. Each one-point difference has energy 5/2, and (X2) gives cross=1/2. The combined difference energy is

    E_(e_x+e_y)=5/2+5/2+2*(1/2)=6,

although the physical edit sets have intersection probability zero. The edited sign is -x_1 x_2. Thus no finite K can give <e_1,e_2>_L<=K P(D1 intersect D2) for all Boolean seeds and edits, nor bound its absolute value that way. This refutes only the precisely specified physical-overlap-only cross payment; A069 never asserted it and its theorem remains valid. Independent exact checks exhaust every distinct point pair for all two- and three-bit seeds (7,264 cases).

The failure also occurs inside A069's proper-subcube/nonempty-core domain. Let Z={x_1,x_2}, let Y be any nonempty core cube, and let h be ANY Boolean sign on Y, with mean m. Take g=x_1 h(Y), D1={x_1=+,x_2=+}, D2={x_1=-,x_2=+}; both leave the whole Y core free and have density 1/4, but their intersection is empty. Join a binary Z subtree and any binary Y tree under a binary root. The Y-only projections preserve disjoint Z supports and contribute zero to (X1); the Z projection gives 1/2 and the root projection gives m^2/2. Thus

    <e1,e2>_L=(1+m^2)/2 >=1/2.                  (X3)

For balanced h=y on one bit, each retained core is y or -y, each single edit energy is 9/2, and the combined difference energy is 10. This independent exact witness is saved in out/PROPER_SUBCUBE_WITNESS.json. It does not rely on empty retained cores.

The same family also checks the complete signed cancellation. Put E_Y=E_(S_h)W_Y, retaining that full core bill. The final edited function is f=-x_1 x_2 h, so

    Gamma(g)=Gamma(f)=5+E_Y,
    H(g)=H(f)=H(h), I(f)=I(g)+1=2+I(h).

Single edit energies are 9/2-m^2/2+E_Y. Their sum plus twice (X3) is 10+2E_Y=2Gamma(g). Moreover <g,e1+e2>_L=-Gamma(g). The exact source/edit cross rebate cancels the entire difference-energy bill in Gamma(f); it must not be lost by a triangle estimate and then charged again from retained influence. This is a terminal-core-preserving transport identity, not a bound on H(h) or E_Y for arbitrary h. A previously paid source reference transports across these particular edits without an extra code cost, whereas an arbitrary source remains unpaid.

For sequential flips on possibly overlapping events, the actual final difference is e_1+e_2-2e_12, with e_j=-2g1_(D_j) and e_12=-2g1_(D1 intersect D2). An intersection term is required even before squaring. For union-once editing the coefficient is instead e_1+e_2-e_12. The ordered operation must be specified. Expanding energy includes all pairings in (X1), and no remaining core entropy or projection bill may be discarded.

## 5. Honest universal line and shortest next action

A068 repairs a support-only reference by a paid complete branch; A069 supplies a complete edited-addressing endpoint and one-subcube energy interface; the lead's corrected neutralization identifies why support arithmetic is only a leaf certificate. These scoped facts do not imply full FEI. The first unsupported universal line is a nonreusing influence payment for the sum of signed projected-core cross terms in (X1), including the intersection correction and both retained terminal cores, for a chosen complete source reference. A physical overlap density is insufficient by (X2).

NEXT: combine (X1) with a first-exposure assignment of cells containing the difference coordinates of two overlapping-control subcube edits, and prove or refute one owned projected-core charge while retaining both terminal costs. This targets the exact new debt rather than repeating one-point addressing or demanding an impossible physical-overlap-only bound. Reviewers A088/A094; A069/A067 and B14/B20 are mathematical consumers. The stage-1 missing cyclic-law Addendum is not replayed or used as a proof premise here.
