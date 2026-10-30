# An unchanged seed terminal through every controller stopping cut

All entropy is in bits. All influences refer to the original independent
uniform physical bits. Write L=log2(3). Let u have four bits, with the bit
of weight one varying fastest, and define the actual ternary truth row

    a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1], b=1-a^2.

For EVERY Boolean seed h on arbitrarily many fresh bits x, put
F_h(z,u,x)=a(u)+z*b(u)*h(x). Pointwise exactly one of a and b is occupied,
so this is an actual Boolean truth function. No phase or seed FEI hypothesis
is imposed. A079's raw Walsh arrays and identities are independently
reconstructed in REVIEW_A079.md and in the saved truth-table certificates.

## Universal seed cancellation, including each complete terminal

For any partial physical assignment s of u, let a_s,b_s be the restricted
rows, beta_s=E b_s, and G_s=a_s+z*b_s (the same gate with constant seed).
Let h_s=H(G_s) and i_s=I(G_s). The complete spectrum of the actual
restriction F_{h,s} is

    p(0,U,T)=ahat_s(U)^2 * 1{T=empty},
    p(1,U,T)=bhat_s(U)^2 * hhat(T)^2.

The two z-frequency labels are disjoint even for a biased or constant
seed. Tensor entropy and cardinality therefore give EXACTLY

    H(F_{h,s})=h_s+beta_s H(h),
    I(F_{h,s})=i_s+beta_s I(h),
    4I(F_{h,s})-H(F_{h,s})
      = S_s+beta_s[4I(h)-H(h)],  S_s=4i_s-h_s.

These formulas include all controller and z energy and the full seed
terminal. They do not assume 4I(h)-H(h)>=0. If query i of u leads to
s0,s1, beta_s=(beta_s0+beta_s1)/2. Thus both its entropy drop Delta_i
and influence Inf_i are independent of h. Both individual child formulas
above, rather than a replacement flat terminal, are retained.

At the root,

    h_root=5-(9/16)L, i_root=17/8, beta_root=3/8,
    S_root=7/2+(9/16)L.

This explicit positive structural component is the source of the reserved
1/8 below. The symbolic seed deficit is a separate retained obligation;
we make no claim that the complete root deficit is nonnegative.

## First physical query of the bit of weight eight

The two children have equal complete entropy

    H(F_{h,v=0})=H(F_{h,v=1})=6-(27/16)L+(3/8)H(h).

Their INDIVIDUAL influences are unequal:

    I(F_{h,v=0})=7/4+(3/8)I(h),
    I(F_{h,v=1})=3/2+(3/8)I(h).

Their mean is 13/8+(3/8)I(h). An initial validation assertion incorrectly
substituted that mean for each child; direct edge checking rejected it,
and the implemented assertions and these formulas were corrected.

Consequently Inf_v=1/2, Delta_v=(9/8)L-1, and

    2 Inf_v-Delta_v=2-(9/8)L > 1/5.

Indeed 3^5=243<256=2^8 implies L<8/5. This is a payment of this actual
query, not a claim about every subsequent controller query.

## Exact all-history controller certificate

For any finite adaptive tree T querying unassigned u bits and stopping
at any chosen nodes, with q_s=2^(-depth(s)), define

    C4(T)=sum_internal q_s[Delta_i(s)-4 Inf_i(s)].

All internal vertices query original physical coordinates; there are no
queries of z or of seed x in this theorem. Telescoping the preceding full
identities gives

    C4(T)=H(F_h)-E_leaf H(F_{h,s})
           -4[I(F_h)-E_leaf I(F_{h,s})].

The seed terms cancel because E_leaf beta_s=3/8. The terminal spectra
are still the actual spectra displayed above, with both child normalizers.

There are 3^4=81 partial states and 108 available state/query transitions.
Backward induction with stop value 0 and action value

    c_i(s)+(V(s0)+V(s1))/2,
    c_i(s)=h_s-(h_s0+h_s1)/2-4[i_s-(i_s0+i_s1)/2],

certifies the EXACT maximum

    max_T C4(T)=delta=1-(9/16)L,  1/10<delta<1/8.

All Bellman values and a maximizing policy are saved in
out/controller_stopping.json. check.py obtains h_s from independent direct
integer character sums, checks physical edges separately, and certifies
comparisons by rational log intervals. A second implementation replay.py
uses a fast integer transform, obtains entropy directly by prime valuations,
and aggregates ALL 238145 deterministic adaptive trees with multiplicities.
Its 28 distinct root costs are in out/replay.json; integer powers certify
that none exceeds delta, and 1690 trees attain delta. The tree querying
the bit of weight one and immediately stopping already attains it.
Thus no reliance on floating point or on a guessed optimal policy occurs.

For the bracket, 3^5<2^8 gives delta>1/10, and 2^14<3^9 gives delta<1/8.
The exact sign comparison used in the replay is: for rational A,B, clear
positive denominator D, then compare 2^(DA)3^(DB) with 1 by putting negative
exponents in the denominator. This proves the sign of A+B log2(3).
The first checker's log bounds independently use the positive atanh series
with its explicit geometric remainder.

Reserve U=1/8 ONCE from S_root; it pays the positive net cost of every
controller history and stopping cut, with leftover at least U-delta>0.
Individual local costs do NOT all have this sign: 10 transitions exceed
rate4 and 47 exceed rate2. Replacing this conserved bank by renewed local
reserves would change the statement. The construction still retains full
FEI in its seed; this certificate supplies no universal FEI conclusion.

## First unsupported line and next action

The theorem does not include querying the seed or deleting z, nor resetting
an arbitrary incoming nonflat reference. A query x_i produces the two
complete seed restrictions h_+,h_-, so the remaining seed ledger contains
their full Shannon entropy, signed conversion and normalizers. Paying that
query/reset from the SAME surviving original bank is the first unpaid step.
The 1/8 controller reserve is consumed only through its actual cumulative
cost; it cannot be reissued at the next query. Half-integral height-two
rows are not covered by the ternary mass-rigidity shortcut. This stage
changes to physical-history accounting because A079 proves a one-product
sibling admission condition still contains arbitrary seeds.
