# Retained reserve and selector endpoints

All logarithms are natural. Let v_i=4p_i(1-p_i), v_S=product v_i, P(S)=v_S c_S^2, D=sum_{S nonempty}(|S|-1)P(S), R=sum_{|S|>=3}(|S|-2)P(S), and E=sum_{S nonempty}P(S)ln(v_S/P(S)). Define h(t)=t^2 ln(1/t^2), with h(0)=0. Thus E=(ln2)Hplus.

## Exact signed singleton slack

For any Boolean sign gate at an interior product law, put D_i=(f|Yi=1-f|Yi=0)/2, t_i=|E D_i|=|c_i|, and d_i=E D_i^2. The physical random variable D_i takes values -1,0,1. Parseval gives

    sum_i v_i Var(D_i)=sum_{|S|>=2}|S|P(S)=2D-R.

Consequently the unused singleton reserve is exactly

    S := 4D-2R-E_single
       = sum_i v_i [2(d_i-t_i)+2t_i(1-t_i)-h(t_i)].       (1)

Both summands inside each bracket are nonnegative: d_i>=t_i and ln(1/t)<=1/t-1. Moreover d_i-t_i=2 min(P(D_i=1),P(D_i=-1)). This separates cancellation of signed derivatives from scalar logarithm slack, with no monotonicity assumption. It is an exact identity, not an additional spectral budget. In particular

    (4+ln4)D-E = S-[E_ge2-ln4 D-2R].                    (2)

The still-unproved universal step is to bound the bracketed higher-degree excess by the actual S. Equation (2) is equivalent to the corrected inequality and is not presented as a solution of it.

## Scoped independent reconstruction of A043

Source: A043-TERNARY-PRIME-CLOSURE-AND-RESERVE-OBSTRUCTION@1, statement SHA256 020b97a3820a338acb78f02d9b22287302d18dfc754cb34eabc90fcc455b0e86, CORE_PROOF.md and REPORT.md. This review accepts its signed reserve, three new representative orbit upper bounds and sharp paths, and explicit quaternary obstruction. It does not independently accept the catalogue, mux dependency, majority bundle, or whole read-once closure claim. No repair to the reviewed portions was needed.

For all-equal on three inputs, use sign variables with means m_i. The sign polynomial is (X1X2+X1X3+X2X3-1)/2. Thus c_i=(m_j+m_k)/2, c_ij=1/2, c_123=0. With c=|(a+b)/2|, reflect both means so a+b>=0. Direct subtraction gives

    [(1-a^2)+(1-b^2)]/2-2c(1-c)=(1-a)(1-b)>=0.

Hence E_single<=sum_i v_i(v_j+v_k)/2=4D and E_ge2=ln4 D. At p_i=q tending to zero, D=12q^2+O(q^3), E_single=48q^2+O(q^3), proving the sharp ratio (4+ln4)/ln2. The checker uses output negation, mask126, which leaves squared spectra invariant.

For exactly-one (mask22), c_ij=(3m_k-1)/4, c_123=3/4. Set u=2c_ij. Then the pair excess over ln4 P(ij) is -(v_i v_j/4)u^2 ln u^2, while the triple mass T=(v_i v_j/4)(1-u)(u+2). For |u|>=1 the excess is nonpositive. Otherwise -u^2 ln u^2<=1-u^2 and (1+u)/(2+u)<=2/3. Summing all pairs gives E_ge2<=ln4 B+[2+ln(16/9)]T. Adding E_single<=4D-2T, with D=B+2T, yields E<=(4+ln4)D-ln9 T. At (1-q^3,q,q), D=4q^2+O(q^3), E_single=16q^2+O(q^3), and E_ge2=8ln2 q^2+o(q^2). Other coefficients have higher-order contributions even after logarithmic factors. This proves the same sharp supremum.

For mask25, direct mixed differences give c_12=1-p3/2, c_13=-p2/2, c_23=-p1/2, c_123=-1/4. In the first pair set u=2-p3 in (1,2). Since u^2 ln u^2>=2u(u-1)>=2(u-1)(2-u), its excess over ln4 P(12) is at most -2T. The other two pair excesses are respectively 2T A(p2), 2T A(p1), where A(x)=x ln(1/x)/(1-x)<=1. Triple entropy is ln16 T. Therefore E_ge2<=ln4 D+2T, which is paid by the signed singleton reserve. Along (q,q,1-q^3) the same D and E leading terms as for mask22 apply. The distinguished negative pair credit is essential to this proof. Strict interior upper inequalities follow from strict scalar logarithm inequalities and positive variances. These are continuum proofs; the finite checker merely verifies their spectra and numerical inequality signs with rational intervals.

For mask33152, positive exactly at assignments 7,8,15, the checker independently establishes all four essential coordinates and all ten proper block row counts, each equal to three. A one-bit block factorization would have at most two distinct rows, so the gate is prime. At (1/2,1/2,1/2,1/1024), the independently computed D=5257209/16777216, R=262911/4194304, companion excess >13/100 and full margin >9/20 agree with the source. This accepts an obstruction to the proposed companion, not a counterexample to FEI.

## Full selector-line certificate for the obstruction gate

Fix the first three probabilities at 1/2 and let z=p4 range over [0,1]. The z=0 slice is AND3, and the z=1 slice is the all-equal gate. Orthogonality on the first three fair bits gives, for nonempty S contained in {1,2,3},

    c_S=(1+z)/4 if |S|=2, and (1-z)/4 otherwise.

Every c_{T union {4}}, including T empty, has absolute value 1/8. Writing v=4z(1-z), the exact formulas are

    D(z)=(5+14z-7z^2)/16,
    E(z)=4h((1-z)/4)+3h((1+z)/4)+(v/8)ln64.           (3)

These formulas extend continuously to z=0,1; selector-containing masses vanish there. To prove a continuum margin, split ln16 from the first seven logarithms. The four (1-z) terms have excess

    (1-z)^2/2 ln(1/(1-z)) <= z(1-z)/2,

using A(1-z)<=1. The three (1+z) terms have nonpositive excess, which may be discarded. Thus

    E(z) <= (ln2)(7+10z-5z^2)/4+z(1-z)/2.

Subtracting this upper bound from (4+ln4)D yields

    [20-18ln2 +(48-12ln2)z+(-20+6ln2)z^2]/16.

Since ln2<1, the z-dependent part is nonnegative on [0,1]. Therefore

    (4+ln4)D(z)-E(z) >= (10-9ln2)/8 > 0.47.           (4)

Equality in the first inequality holds at z=0, so this uniform lower margin is exact on the closed selector segment. The strict rational bound uses ln2<52/75, certified by the same log interval; no decimal computation is a premise. This proves that the entire line containing the higher-degree counterexample has a positive full-entropy reserve. It does not prove the all-bias result for this prime.

## Symbolic endpoint expansions

At z tending to zero, ordinary Taylor expansion in (3) gives

    D=5/16+(7/8)z-(7/16)z^2,
    E=(7/4)ln2+[(5/2)ln2+1/8]z+O(z^2).

In particular Hplus/D tends to 28/5 at this composite-slice endpoint. At s=1-z tending to zero,

    D=3/4-(7/16)s^2,
    E=(3/2)ln2+[(3/4)+(3/2)ln2]s
      +(1/2)s^2 ln(1/s)+O(s^2).

Thus Hplus/D tends to 2 at the all-equal slice. The logarithmic term comes from the four normalized coefficients that vanish at z=1, not from the vanishing selector variance. Both remainders follow from Taylor's theorem for h near 1/4 or 1/2; h(s/4) is written exactly. Here both endpoint deficits are positive, so no zero-deficit quotient is assigned. Zero-deficit and unit-atom endpoint rules remain those already established in A042 stage1.
