# Relative orientation/refund defect under the actual reductions

Let f be a finite uniform-cube Boolean sign. Use the A052 signed face refunds M_i,M_j, with zero denominators assigned zero. Define

    T(f)=sum_i O_i(f)+sum_(i<j) R_ij(f),
    R_ij=sum_retained_rows (M_i+M_j),
    O_i=sum_(s avoiding i)(hat f(s+i)^2-hat f(s)^2)_+,
    Theta(f)=T(f)/I(f) for nonconstant f.

Constants have T=I=0; no normalized value is required there. T is nonnegative and dimensionless, and is a structural diagnostic, not an entropy payment. Entropy is in bits. This stage does not assume an optimizer or admit wrappers as critical witnesses.

## 1. Exact disjoint tensor ledger

If f,g use disjoint coordinate cubes, then

    T(fg)=T(f)+T(g),  I(fg)=I(f)+I(g).

Proof: an orientation difference for a coordinate of f is its old difference multiplied by the squared spectator coefficient of g. The positive part scales by that nonnegative factor, and Parseval sums it to one. Each same-factor face refund is homogeneous of degree two in its four amplitudes; its spectator square again sums to one. On a face across the two factors the four amplitudes form a rank-one matrix, so both merging variances vanish, including zero-weight cases. Sum the contributions. In particular

    Theta(f^tensor m)=Theta(f),
    Theta(fg)=[I(f)Theta(f)+I(g)Theta(g)]/[I(f)+I(g)].

An additional balancing character z contributes exactly T(z)=I(z)=1 and H(z)=0. Therefore, for h_m=h^tensor m and g_m=z h_m,

    T(g_m)=mT(h)+1, I(g_m)=mI(h)+1.

These exact facts distinguish a reduction-stable normalized diagnostic from its unnormalized absolute neighborhood.

## 2. Balanced activation: the core diagnostic is retained exactly

Fix a nonconstant seed h on k named coordinates, mean mu=E h (|mu|<1). For m>=1 set h_m=h^tensor m, mu_m=mu^m, and g_m=z h_m. Let r>=1, p=2^-r. On r new controls activate g_m at the all-zero assignment, and output +1 elsewhere; call the resulting Boolean sign F. Querying all controls and z leaves +/-h_m with total probability p.

Arrange core variables first, then z, then controls. The Fourier coefficients have three forms:

    empty coefficient: 1-p;
    nonempty controls-only coefficient: -p;
    coefficient containing z and core set U, at any control label: epsilon*p*hat(h_m)(U), epsilon in {-1,1} fixed by the balancing-character convention.

All remaining coefficients are zero. The code uses balance sign 2*bit-1, giving epsilon=-1 for Walsh characters (-1)^bit. Choosing the opposite balancing character changes epsilon but not the diagnostic. A different prescribed control assignment only changes characters, with no effect on the squared quantities used here.

Core orientations and all core-core refunds therefore contribute EXACTLY

    T_core(F)=p*T(h_m)=p*m*T(h).                    (1)

Indeed their nonzero retained rows contain z, and summing the 2^r identical scaled control-labelled rows multiplies p^2 by 2^r=p^-1. Tensor faces between different core copies have zero refunds. Every core-control face is rank one, so it contributes no refund. All control orientations are zero because their paired magnitudes agree except at the dominant empty coefficient.

The balance-coordinate influence is p. Its minority mass is p*mu_m^2, giving

    O_z(F)=p(1-mu_m^2).

Consequently the remaining diagnostic E=T(F)-pmT(h) is nonnegative and consists exactly of O_z, the balance-core refunds, the balance-control refunds, and the control-control refunds.

## 3. Explicit wrapper bound from one influence ledger

For a balance-core face the only possibly nonzero refund rows have empty retained core set. Their amplitudes, in the appropriate order, are (a,b,0,d), with b^2=p^2*mu_m^2. The sum of refunds is at most the sum of the two singleton collision quantities, each at most 4b^2. There are 2^r control labels per core coordinate, so

    sum_balance-core R <=8 p mk mu_m^2.

For a control-control face, all refund rows vanish except the one containing the empty coefficient. Its quartet is (1-p,-p,-p,-p). The exact total refund is

    4p^2 / [((1-p)^2+3p^2)((1-p)^2+p^2)] <=64p^2,

because p<=1/2. For a balance-control face only the exceptional quartet (1-p,-p,epsilon*p*mu_m,epsilon*p*mu_m) can have a refund. Its two separately conditioned collision sums are at most 4p^2+2p^2 mu_m^2 and 8p^2 mu_m^2, hence its refund is at most 14p^2.

Combining these nonnegative contributions yields the finite, explicit certificate

    0<=E<=p+8pmk mu^(2m)+[64 binom(r,2)+14r]p^2.  (2)

No amplitude absolute value is substituted for a signed merging square. This bound is deliberately conservative and not claimed sharp.

## 4. Relative limit and a finite error bound

Set r=r_m to the least integer with 2^r>=(m+1)^4, so p_m<= (m+1)^-4 and r_m=O(log m). The actual influence is

    I(F_m)=p_m[m I(h)+1+r_m].

From (1),(2), T(F_m)->0, but its influence-normalized value satisfies

    lim_m Theta(F_m)=Theta(h),                     (3)
    |Theta(F_m)-Theta(h)|
      <=[1+8mk mu^(2m)+(64 binom(r_m,2)+14r_m)p_m
          +(1+r_m)Theta(h)]/[m I(h)+1+r_m].         (4)

For each fixed seed the error is O(log m/m). This proves that the same absolute-neighborhood admission used by A055 retains, rather than erases, the normalized core defect. It does NOT prove that every other admission mechanism has this property, or that a small-Theta class has a FEI bound.

The corresponding entropy identity is

    H(F_m)=p_m*mH(h)+4r_m p_m+A(p_m),
    A(p)=-(1-p)^2 log2((1-p)^2)+p^2 log2(p^2)=O(p).

It follows directly by separating the empty, controls-only, and balanced-core Fourier coefficients listed above. Thus R(F_m)->R(h). If D_K(h)>0 for a fixed K>=0, then

    D_K(F_m)/(p_m m)->D_K(h),
    T(F_m)/D_K(F_m)->T(h)/D_K(h).                  (5)

Even the normalization by the positive root deficit preserves the seed's relative diagnostic in this construction.

## 5. Finite high-threshold deficit normalization and child eligibility

The proper physical block B of all controls and z has

    S_B=-E D_K(child)=-p_m m D_K(h),
    D_K(F_m)+S_B=p_m[(4-K)r_m-K]+A(p_m).           (6)

For x in [0,1], -x ln(x)<=1-x, by convexity of x ln(x)-x+1. Thus A(p)<2p/ln2<3p; the last strict inequality follows from the positive atanh series ln2>2/3. For EVERY m>=1,r>=1 and K>=4, not merely in a limit,

    D_K(F)+S_B < p[(4-K)r-K+3] <=-p,             (7)
    D_K(F)<pmD_K(h).

In particular a positive activated K-deficit forces D_K(h)>0 and S_B<0. Combining the exact retained-core diagnostic with the strict deficit inequality gives

    T(F)/D_K(F) >= T(h)/D_K(h)                  (8)

whenever D_K(F)>0 and K>=4. Balanced tensor activation cannot make the diagnostic small relative to the positive high-threshold deficit, even at a finite parameter. Its ratio normalized by influence can change at finite m, but the simultaneous hardness-preserving limit retains Theta as in (3).

A positive root deficit cannot replace the critical bank D+S: (7) proves that bank is already negative on this proper physical cut. The wrapper is inadmissible for essential-dimension minimality. These are transport and eligibility theorems, not a critical-source payment theorem. No virtual-child or optimizer assumption enters.

## 6. Consume the different systematic-code endpoint without conflating it

A005's stage4 uses a different actual reduction: an injective spectral code of minimum Hamming distance at least three, then one physical edit. Before that edit every singleton row has at most one occupied coefficient, so beta_i=0 and O_i=Inf_i. Every two-coordinate face has at most one occupied coefficient, so both refunds vanish. Therefore EXACTLY

    T(coded f)=I(coded f), Theta(coded f)=1.        (9)

Thus Theta is tensor-stable but is not invariant under all campaign reductions: coding can replace a seed's Theta by 1. It does not erase the total orientation budget when it erases pair collision/refunds. This is why neither a qualitative code endpoint nor the activation transport may be silently granted criticality.

For a one-point edit on N bits, p=2^-N, squared-spectrum TV<=2sqrt(p). The function O_i is at most2 times TV-Lipschitz: the positive parts of the upward paired differences change by at most the sum of absolute probability changes. Consequently

    |sum_i O_i(edited)-I(coded)|<=4N sqrt(p).

The old empty singleton partners receive amplitudes of magnitude2p; their total minority mass is at most2p and C_i<=8p. Every total face refund is at most C_i+C_j, so

    sum_refunds(edited)<=16 binom(N,2)p,
    |T(edited)-I(coded)|<=4N sqrt(p)+16 binom(N,2)p.

Physical influence changes by at most2Np. On A005's logarithmic-redundancy code applied to tensor powers, I(coded)>=m I(h), N=O(m), and these errors are exponentially small. Therefore Theta(edited)->1 while R(edited)->R(h), and all singleton/pair physical child reserves remain negative for a hard seed as proved in A005's source. A small total refund or pair collision is compatible with an influence-sized orientation budget. This consumes the existing code admission and adds its exact relative diagnostic; it claims neither a new coding mechanism nor a bound on genuine critical sources.

out/CODE_GUARD.json checks the exact value1 on coded PD2/PD3 and the finite squared surgery estimates after two dummy bits and one flip. Both resulting truth tables have odd negative count and full Fourier support. They are guard fixtures, not minimal witnesses.

## 7. Honest remaining line

The absolute T-neighborhood contains arbitrary-core hardness; tensor/balancing/activation preserves the seed's Theta in its hardness-preserving limit, whereas the code endpoint has Theta tending to1. Both lose actual child eligibility. The first unsupported line is a reserve-relative selected pair/larger-block inequality on an actual least-dimensional K-violator. Neither a zero-rigidity argument, an absolute diagnostic floor, nor either construction supplies it. NEXT is to compare the signed parity cost minus exact merging refunds with D+S_pair and the retained phase margin, using the exact relative ledgers as admissibility tests; do not normalize by an arbitrary positive root deficit, discard orientation when refunds vanish, or discard the core terminal.
