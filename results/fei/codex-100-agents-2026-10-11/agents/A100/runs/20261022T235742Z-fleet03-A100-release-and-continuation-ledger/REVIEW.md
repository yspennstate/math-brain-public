# A100: independent reconstruction of one prescribed narrow reset

Review target: A094-NARROW-QUERY-PRESCRIBED-RESET-SAME-RATE4@1, original statement and hypotheses unchanged. The complete all-parameter reconstruction below uses the actual source spectrum, complete normalized reference, root physical influence, full child posterior normalizers and signed reset substitution. The exact finite checker is independently implemented and imports no A094/A095 helper. The final verdict and executed scope are saved with the original claim in CLAIMS.json after validation.

For h_l=1−2·1_zero, take g=h_w h_2 on w+2 active bits, with m dummies, w≥4. A fair selector chooses g or its all-zero point flip. Write n=w+2+m, δ=2^−n, q=2^(1−w), b=1−q. At an old source mask the true coefficient is a_T−δ; every new coefficient has magnitude δ. The source is full on its 2^(w+2) active masks. Put W=2δ−2^(w+2)δ². The prescribed reference has old mass (1−W)a_T² and new mass δ² on every other Fourier mask. It has total mass one, including all selector and padding masks, and is positive on true support.

Independently summing the tensor coefficients gives source entropy c=2−2b² log2 b+(2q−q²)(2w−2), signed profile A=2+2b log2 b+(2−q)(2w−2), and unweighted profile B=−8 log2 b+2^(w+3)w−8w+8. The complete root cost is exactly

    CE = c−2δA+δ²B−(1−W)log2(1−W)+2nW.

The old actual probability is 1−W because sum_T a_T=g(0)=1. Thus the normalizing term has that exact coefficient; it is not a conditional law with missing reference mass. The signed A term cannot be replaced by an unsigned profile.

The positive atanh series gives ln2>2/3. Integration gives −ln(1−x)≤x/(1−x), and −(1−x)ln(1−x)≤x. Consequently c<2+(4w−1)q−(2w−2)q², A≥4w−2−(2w+1)q and B/2^(w+2)≤2w. The last inequality uses −log2 b<(3/2)q/b≤3/14<w−1. Substitution yields

    CE < c + δ[4m−2w+15+(4w+2)q].

Independent physical directional edge counting gives I_root=1+wq+δ(m−w−1). Keeping the dimension terms before subtracting gives

    4I_root−CE > 2+q+(2w−2)q²−δ[2w+19+(4w+2)q] > 395/256.

For the last strict bound the two nonnegative subtractions decrease with w and m. At w=4,m=0 they sum to 27/64+9/256=117/256. Their successive w ratios are (2w+21)/(4w+38)<1 and (4w+6)/(16w+8)<1. The positive q and q² terms may be discarded. This is a reserve in the original 4I_root account, not a separate influence quota for a descendant. It differs from A095's 3/256 surviving-terminal margin.

For a physical query, write p for the mean of its actual signed child laws and r for the current reference marginal. Use posterior pi_b=P_b/(2p) on occupied fibers, 1/2 on zero true fibers, raw Q_b=2r pi_b and actual normalizers Z_b>0, with Z_0+Z_1=2. Membership-KL disintegration and concavity of log show complete CE release Δ+L−mean log2 Z_b≥0; Δ includes both erasure and the phase/channel increment. Multiplying each finite node identity by its actual reach telescopes exactly. Hence all old complete query releases plus ALL inherited terminal costs equal the original CE. No infinite-tree or limit exchange is used. Both actual child normalizers and reference-only zero true fibers remain present.

Every wide-only adaptive tree has a unique all-zero edited path. At its stopped edited leaf let d be its depth and t=w−d. Query one width-two coordinate. Its zero child is exactly the same selector edit of h_t h_1 with the original padding and selector; its original reach is λ=2^(−d−1). The complementary child and all other leaves keep their inherited references. This geometric identification holds for every wide order; off-path queries alter only the telescoping releases and their retained terminal bills. When d<w both actual queried children are nonconstant. At d=w, h_0=−1 is an explicit boundary source and no division by its influence is made.

Build the fresh canonical complete reference from the TRUE residual source support S_t: old masses (1−W')P_t, new masses ε², where ε=2^(−t−1−m) and W'=2ε−|S_t|ε². This support is sparse for t=0,1; replacing |S_t| by 2^(t+1) would give a wrong reference. For t≥2 put u=2^(1−t), a=1−u. The source profiles are

    c_t=−2a²log2 a+(2u−u²)(2t−2),
    A_t=2a log2 a+(2−u)(2t−2),
    B_t=−2log2 a+(2^t−1)(2t−2).

Here |S_t|=2^t, A_t≥4t−4−(2t+1)u and B_t/2^t≤2t−2. The last uses −log2 a≤t−1, including equality at t=2. Because ε2^t≤1/2, the full fresh canonical cost obeys

    CE_can < c_t+ε[4m−3t+14+(4t+2)u].

For t≥4, c_t<57/32 and the bracket is at most 4m+17/4. The integer induction 16m+17≤17·2^m therefore bounds the correction by 17/128 and gives CE_can<245/128<2. For t=2 the same formula gives CE_can≤29/8<4. For t=3 it gives CE_can<97/32<4. The linear-times-dyadic corrections have their maxima at m=0, as comparison of successive terms shows. At t=0,1 the source spectrum is a single character. The canonical reference equals the actual selector-edit spectrum, and CE_can≤ε(4(t+1+m)+3)≤7/2<4, decreasing after total residual source width one. All boundary denominators are positive.

For the prescribed mixture Q_fresh=(1−eta)Q_can+eta U on EVERY child mask, eta∈[0,1/4], the occupied-atom bound Q_fresh≥(3/4)Q_can gives CE_fresh<CE_can+1/2. This uses log2(4/3)<1/2, equivalent to 16<18 after squaring positive quantities. At d=0, t=w≥4 and λ=1/2, so λCE_fresh<5/4. At d≥1, λ≤1/4 and CE_can<4, so λCE_fresh<9/8. For eta=0, λCE_can<1 at every boundary.

The exact change to the original release-plus-terminal ledger is λ(CE_fresh−CE_old_zero). Its positive part is at most λCE_fresh because the inherited normalized-reference cost is nonnegative. All old releases, the complementary child and every other terminal remain. The same original quota therefore leaves reserve greater than 395/256−5/4=75/256, or greater than 395/256−1=139/256 at eta=0. Subsequent finite no-reset transport merely disintegrates that existing bill. This proves the original claim's prescribed one-reset scope, rather than a new influence price for each child.

An independent untouched terminal with its full normalized finite-cost reference remains a product under product-compatible posterior choices, including zero true fibers. Its entire CE and KL add with coefficient one and never finance the core reset. If its own influence price is supplied, the combined rate is the maximum of that price and four; arbitrary terminals do not receive a universal price by this argument.

Checks that could fail were targeted explicitly: the sign of the old A term; the ORIGINAL physical I; d=0 where the reached fresh charge is largest; t=0,1 where support shrinks; both normalizers and zero-true reference mass; positive as well as negative signed reset excess; and the unchanged complementary/off-path bills. The finite domain is frozen before computation. Direct integer character sums and independent edge counting reconstruct actual functions; reference transport is implemented from its definition. Integer fixed-point logarithm intervals round every product and sum outward and use the positive atanh tail 9/[4·49·3^49]. Numerical interval overlap is only a crosscheck of identities already derived algebraically here.

No arbitrary-core theorem follows. A second prescribed reset must subtract this reset's actual signed excess from the same remaining reserve; it cannot restart with 395/256. The precise universal gap remains an influence-priced useful source/reference profile, or a selected continuation/reset whose complete positive bills fit one original account. A072/A074 saturation reinforces that a donor already fully booked cannot supply this capacity. Full FEI and the two independent integrated A099 audits remain open.
