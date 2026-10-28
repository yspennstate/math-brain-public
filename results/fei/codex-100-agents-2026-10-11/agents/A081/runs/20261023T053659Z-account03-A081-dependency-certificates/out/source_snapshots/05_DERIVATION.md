# A positive booked reset cannot be hidden in a vanishing rare-edit allowance

All costs use bits and normalized complete references. Put h_L=1-2 indicator(all L bits zero). For every integer m>=8, fix the actual Boolean source g=h_4 h_2 on six disjoint source bits, append m dummy data bits and use one fair selector to flip the all-zero full point on its selector-one branch. This is exactly the A095/A094 source family, with no new representation or approximate Boolean law. Let delta=2^(-m-6), and use A095's original support-completed reference Q with source P_g. Query one narrow coordinate immediately, with no preceding wide queries. Retain the complementary child and every complete terminal/release. Reset only child0, physical reach1/2, to

    Qfresh=(3/4)Qcan(h_4 h_1)+(1/4)U,

where U is full uniform on all m+6 remaining Fourier coordinates and Qcan is the prescribed canonical support-completed reference of the ACTUAL residual source. Let e1=(CEfresh-CEinherited,0)/2 and p1=max(e1,0). No bank is renewed, no sibling discarded, and no independent terminal funds this charge.

**Theorem (analytic author proof; independent review pending).** For every m>=8,

    e1>1/10,
    U_star=min{(C0+1)I(g),(4C0+15)(C+J)}<1/10

when the A011 v2 allowance is instantiated at the SAME Boolean source with R=P_g,C0=4,r=1,b=m. More precisely I(g)=3/2,C=m delta,J=delta,K=31 and U_star<=31(m+1)delta<=279/16384. Thus the already incurred conservative booking p1 exceeds that theorem's stated extra-booking admission for EVERY m>=8. Also p1/(C+J) is unbounded. This refutes automatic admission of this booked conversion into that rare-edit allowance; it does NOT refute A011's conditional theorem or claim the actual remaining bank equals U_star.

## 1. Complete root KL is small, with all reference atoms retained

The64 source coefficients a have magnitudes7/16 or1/16; their signed sum is g(0)=1 and sum a^2=1. On old source masks actual root probabilities are(a-delta)^2 and Q=(1-W)a^2, W=2delta-64delta^2. On EVERY other root mask both true probability and Q equal delta^2. Both entire laws normalize. For delta<=1/64, W<=1/32 and

    chi2(P_root,Q)=sum_old [(W a-2delta+delta^2/a)^2]/(1-W).

Indeed divide P-Q by sqrt Q on the old support; every new-support contribution is zero. The Euclidean triangle inequality and min|a|=1/16 give

    sqrt[(1-W)chi2] <= W+2delta sqrt64+delta^2 sqrt(sum1/a^2)
                           <=2delta+16delta+128delta^2<=20delta.

Hence chi2<=12800delta^2/31. From ln x<=x-1, D_2(P||Q)<=log2(e)chi2<(19200/31)delta^2. Since m>=8 implies delta<=1/16384<31/19200,

    Droot<delta.                                      (1)

No source probability or reference-only atom is removed. In particular this is a bound on the actual inherited root model, not a free fresh reference substitution.

## 2. The quarter-uniform child incurs a fixed divergence

Let S be the16-mask true support of the unedited h_4 h_1 source inside the remaining Fourier cube, which has2^(m+6)=1/delta masks. Its actual edited child has edit mass epsilon=2delta and

    P_child(S)=1-Wchild, Wchild=2epsilon-16epsilon^2<=4delta.

All complementary actual probabilities are epsilon^2. The canonical Qcan has the SAME total old-support mass1-Wchild. Uniform mass on S is16delta. Consequently

    Qfresh(S)=(3/4)(1-Wchild)+4delta<=3/4+4delta<4/5.

The full reference and true probabilities outside S are retained. By the two-cell KL log-sum inequality,

    Dfresh >= d_2(1-Wchild || Qfresh(S))
            >= (1-Wchild)log2[1/Qfresh(S)]-h2(Wchild).

The omitted complementary cross-entropy contribution is nonnegative. Since log2(5/4)>1/4 (625>512), the first term is at least(1-Wchild)/4. Moreover Wchild<=4delta<=1/4096. The elementary bound h2(x)<=x log2(e/x), and monotonicity of this upper bound on(0,1), give

    h2(Wchild)<(12+3/2)/4096=27/8192.

Thus

    Dfresh>4095/16384-54/16384=4041/16384.            (2)

The bound h2(x)<=x log2(e/x) follows from -(1-x)ln(1-x)<=x. Its monotonicity follows by differentiating x ln(e/x), whose derivative is-ln x>0 on(0,1). All logarithms here have positive arguments; the argument includes the complete complement of S.

## 3. Retain the actual inherited child and exact signed reset

Transport Q through the actual physical narrow query using normalized posterior kernels, including all zero true fibers. Conditional KL disintegration gives

    Droot-(Dold,0+Dold,1)/2
       =L_cond-[log2 Z0+log2 Z1]/2>=0,

with Z0,Z1>0,Z0+Z1=2. Both child divergences are nonnegative, so Dold,0/2<=Droot. The reset changes neither physical function nor entropy. Therefore the reached SIGNED excess is exactly

    e1=(Dfresh-Dold,0)/2
       >=Dfresh/2-Droot
       >4041/32768-1/16384=4039/32768>1/10.          (3)

This is the entire actual old-reference subtraction. It does not claim the reset is free, reassign a fresh terminal budget, or spend the untouched sibling. The complete ledger becomes CEroot+e1, retaining its earlier release and both terminal costs. An independent untouched product terminal cancels from the signed difference and remains wholly additive.

## 4. Exact scope of the A011 allowance comparison

A011's a=6,b=m,r=1,p=1/2,t=delta data obey every source-parameter condition; sign-translation of the selector makes its edited point agree. The source has I(g)=1+4/8=3/2 and H(g)<=log2(64)=6=4I(g), so R=P_g and C0=4 are valid without any FEI premise. At the all-zero source point all six original source edges are pivotal, d=6. Hence

    C=2pt(a+b-d)=m delta,
    J=2rpt=delta,
    K=4C0+15=31,
    U_star=min{15/2,31(m+1)delta}.

The sequence(m+1)2^(-m) decreases for integers m>=0. For m>=8,

    U_star<=31*9/2^14=279/16384<1/10<p1.             (4)

For m>=1 its next-to-current ratio is(m+2)/(2m+2)<=3/4, so C+J tends to zero geometrically and p1/(C+J) tends to infinity. No finite universal multiplier of C+J can cover this prescribed quarter-uniform positive booking. This is an actual Boolean/reference family, not an arbitrary non-Boolean spectral measure.

The root reference in A011 is its different general envelope, and its source-prefix policy exposes padding FIRST. This construction does not silently identify those references or policies. It shows that any proposed handoff carrying this already executed booking as an EXTERNAL U cannot invoke that theorem's stated U<=U_star admission. Reference conversion and policy compatibility would require separate proofs as well. U_star is only a sufficient proven allowance, not a necessary bound on the actual unused original quota; the original A095 rate-four payment remains valid.

## 5. Independent challenge of A094's third-reset sign

For the separate w4,m0 fixture after both narrow resets, take the actual -h4 point-selector with its canonical model, query a wide bit and reset child0 to canonical -h3 at original reach1/8. Reconstruct actual child P and both references from definitions. They have three classes: P=(49/64,1/64 repeated7,1/64 repeated8); inherited Q=(18375/33856,1695/33856 repeated7,113/8464 repeated8); fresh Q=(63/128,7/128 repeated7,1/64 repeated8). Their three old/fresh likelihood ratios are12250/11109,3390/3703,452/529.

With N=12250^49*3390^7*452^8 and D=11109^49*3703^7*529^8, independent integer comparisons N>16D and N^2<512D^2 prove1/128<e3=log2(N/D)/512<9/1024. This scoped A094 obstruction HOLDS; no full arbitrary-source floor theorem is independently accepted here.

## First unsupported universal line

To consume arbitrary-source floors after these histories, prove a SAME-owner allowance for a genuinely inherited, nonvanishing profile-conversion booking, preserving original C0 and both full terminals; the rare-edit-only U_star cannot provide it. Enlarging U_star to an actual unused source surplus may work, but requires a proof at every preceding frontier rather than resetting a descendant bank. Source-prefix transport alone and a finite successful third reset do not establish that step. Full FEI remains OPEN.
