# A positive non-point reset paid by the original balanced-wrapper source

All cubes are finite and uniform; all entropy, cross entropy (CE) and KL are in bits. This is a supplied-source transaction for an explicit family, not full FEI. No canonical source is replaced for free.

## 1. Actual source and the old conditional bill

Let g on three bits be negative exactly at Hamming weight one. Its truth table is (1,-1,-1,1,-1,1,1,1). Its squared spectrum has empty mass 1/16, full mass 9/16, and six other masses 1/16. Its three coordinate influences are 3/4, hence I(g)=9/4. Write H_g=H(g).

Let q_g(0)=p_g(0) and q_g(T)=(5/6)p_g(T)+(1/6)(15/16)1[T=full] on nonempty T. This is a normalized complete reference with the same support. In particular q_g(full)=5/8 and the six proper nonempty masses are 5/96. Define CE_g=H_g+D(p_g||q_g).

For every integer m>=1 on disjoint blocks set h=chi_z product_{j=1}^m g_j. Thus h is balanced, I(h)=1+9m/4, H(h)=m H_g. Its supplied reference q_h is the tensor of the q_g with a forced z frequency. Define F on the additional controls x,b,y by F=h if x=0, F=+1 if x=1,b=0, and F=2y-1 if x=b=1. It has dimension 3m+4.

The initial balanced lift L has mass 1/16 on each of the eight control-only masks; for every nonempty core mask T it has q_h(T)/4 at T and T+x, with b=y frequencies zero. Declare the actual INITIAL reference

    Q(S)=(4/5)L(S)+(1/5)L(S symmetric-difference {y}).

Q is normalized and dominates the entire source. The y-frequency perturbation leaves all eight control-only masses unchanged. On the nonempty core sector it puts fractions 4/5 and 1/5 on y absent/present. This is a declared correlated supplier, not a reset of an inherited occupancy product. Put C=(1/2)log2(5/4). Direct source weighting gives

    H0=3+m H_g/2, I0=3/2+9m/8,
    A0=D(P_F||Q)=m D(p_g||q_g)/2+C,
    CE0=3+m CE_g/2+C,
    M0=4I0-CE0=3+9m/2-m CE_g/2-C.                 (1)

Query b; then query y in BOTH b branches, including the physically dummy y in b=0; then query x at every resulting leaf. Transport the actual current reference by the coherent kernel, fair on source-zero erased rows, with its OWN outcome normalizers. Both outcomes always remain. At the b frontier the complete conditional y-reference bill is exactly C. The reached y erasures release exactly C. All reference outcome laws in this prefix are fair, and its b and x releases are zero. The x=0 subfrontier has total reach 1/2, actual core h and EXACT inherited q_h; the x=1 subfrontier contains constants and has total reach 1/2. Thus the old C is charged in (1) and appears in the release ledger once. It is not silently removed or spent a second time. An additional eligible old booking 0<=omega<=1/4 may already belong to this same account; it remains explicitly subtracted below.

The prefix statements follow atomwise: nonempty core rows before y erasure have the fixed 4:1 y split; all control-only rows retain their source masses. The coherent b and y kernels are fair on this sector, including the reference-only y rows. After the y erasure only the original q_h multiplier remains. The x query separates core from constants. No quotient or unsupported zero-row normalization is used.

## 2. Independently reconstructed positive inherited conversion

For the pure g query of its first coordinate a, the a=0 child is parity on the other two bits; the a=1 child is the width-two point sign negative at (0,0). With alpha=1/6, the actual inherited parity reference is exact. In empty/singleton/singleton/full order the inherited point reference is

    (1/4,5/22,5/22,13/44),

whereas the prescribed FULL fresh reference is

    (1/4,5/24,5/24,1/3).

The reference outcome probabilities are 13/24 and 11/24. Both source children have physical probability 1/2. The averaged new-minus-inherited complete KL is

    sigma_g=(1/8)log2(1404/1331)>0.                 (2)

Thus the reset actually strengthens a conditional 1/11 profile to 1/6. Matching support does not make it nonpositive. For general 0<alpha<1 the same reconstruction gives sigma_g=(1/8)log2[4(2+alpha)/((2-alpha)^3(1+2alpha))]. The numerator minus denominator is alpha^2(18-11alpha+2alpha^2)>0, since the bracket exceeds 7. This independently verifies the pure-core all-alpha part of A047's incoming obstruction. It does not claim an independent audit of every other clause of that composite claim.

In each reached h core, query a_j in every block j, after every query resetting ONLY the queried factor on BOTH outcomes to its full same-alpha law (exact for parity). Keep all other current factors, the forced z frequency and every constant terminal. A source/ref product cancels the spectator factors in the coherent kernel; therefore the local reference outcome probabilities and (2) remain literal. This also permits any physical-history-dependent order that queries each block exactly once on each core path. The total ACTUAL signed reset cost, with the core reach included, is

    sigma_total=m sigma_g/2=(m/16)log2(1404/1331)>0.       (3)

Neither a new source nor a fresh variance bank is introduced at a reset.

## 3. Every terminal, all KL releases and the signed refund

Each restricted g block is parity (H=0,I=2) or point2 (H=2,I=1), with equal physical probabilities. Tensor additivity, including the forced z character, gives whole-frontier quantities

    Hf=m/2, If=1/2+3m/4, S=4If-Hf=2+5m/2.       (4)

The constant half contributes zero, but is retained. All reached references remain normalized and complete. Atomwise likelihood telescoping for the CURRENT references, with every reset included, gives

    A0+sigma_total = sum reached(erasure KL+outcome KL)
                    + sum reached(complete terminal KL).           (5)

In particular the prefix release C is present in (5). Define the signed physical edge

    e=H0-Hf-4(I0-If)=-1-2m+m H_g/2.

Then exactly

    S-[A0+e+sigma_total]_+-omega
      =min(S,M0-sigma_total)-omega.                 (6)

The e term is retained with its sign; edge costs are not individually clipped.

For an elementary dimension-free sign certificate, H_g<=3 by the eight-atom entropy bound. Since q_g(T)>=(5/6)p_g(T) at every nonempty atom,

    D(p_g||q_g)<(15/16)log2(6/5)<5/16,
    CE_g<53/16.

The integer inequalities 6^3<2*5^3 and 5^3<2*4^3 prove log2(6/5)<1/3 and C<1/6. Also 1<1404/1331<2, so 0<sigma_total<m/16. Consequently

    A0+e+sigma_total
      =C-1+m(CE_g/2-2+sigma_g/2)
      <C-1-9m/32<0.                               (7)

Equations (4),(6),(7) prove the exact final paid account

    S-[A0+e+sigma_total]_+-omega
      =2+5m/2-omega >=7/4+5m/2.                   (8)

For m=1, the lower bound is 17/4. This pays a genuinely positive prescribed inherited non-point-profile conversion after mixed control queries, with a nonzero old conditional bill, an additional old quarter booking and all physical terminals retained. Its relatively generous surplus comes from this explicit non-point family; no arbitrary-core payment theorem follows.

## 4. Exact certificates and first unpaid line

code/pay_reset.py reconstructs the complete m=1 history using exact Walsh squares, physical pivots, current coherent kernels and prime-log KL vectors. It retains 12 physical terminal leaves, independently compares every reached terminal spectrum to a direct Walsh sum, checks the explicit inherited point profile, the entire likelihood telescope (5), the old C release and the signed account. The 64 tensor-formula instances are finite consistency checks; the tensor proof above, not that list, proves all m.

code/audit.py uses a separate standalone Walsh/edge/likelihood implementation for the critical core conversion and an integer polynomial identity for the all-alpha sign. No Lean compilation is asserted or needed: the concrete risk is incorrect inherited normalization or missing physical terms, which the exact probability certificates test directly. Prior held formal checks are not counted as passes.

FIRST UNSUPPORTED UNIVERSAL LINE: supply an influence-priced complete initial reference for an arbitrary Boolean core AND bound its necessary hereditary positive profile conversions by the SAME unused original margin after all old debits. In particular nothing here funds A097's isospectral zero-energy conversion in an arbitrary inherited source. This stage consumes and pays the actual A047 non-point obstruction in a finite-to-infinite tensor family; it does not solve the arbitrary-source interface or full FEI.
