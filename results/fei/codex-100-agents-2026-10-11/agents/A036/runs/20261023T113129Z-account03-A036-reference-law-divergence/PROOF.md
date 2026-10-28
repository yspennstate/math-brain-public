# A supported prescribed reference reset can dwarf a vanishing influence

Full FEI is OPEN. Entropy and KL are bits. This stage tests the precise arbitrary-factor repair left unpaid by A039: sigma_j<=K Inf_j for the SAME-profile full-spike reference. The point theorem remains valid. All-dimensional conclusions below are analytic, not extrapolated from finite checks. Independent review pending.

## 1. Actual Boolean family and explicit complete law
For k>=5 use z in{0,1}^k, j in{0,1}, delta=2^-k. Let chi(z)=(-1)^z1, B=e2, C=e1+e2, A=0. Let g(z)=chi(z) except reverse its sign at B,C. Let v(j,z)=g(z) except reverse its sign at(j=1,z=A). All three z points are distinct. Query the physical j bit. The two target children are g and g'=g reversed at A. Hence Inf_j(v)=delta exactly. This is an actual Boolean family, not an abstract spectral measure.

Write Fourier masks in little-endian order j then z1,...,zk. Direct character sums give

    E g=0, E g'=-2delta, E v=-delta, vhat({j})=delta;
    vhat(z_FULL)=3delta, vhat({j}+z_FULL)=delta;
    ghat(z_FULL)=4delta, g'hat(z_FULL)=2delta;
    vhat({z1})=1-5delta.

For any Boolean target f here, alpha in(0,1), beta=1-alpha, define

    q_f(0)=p_f(0),
    q_f(S)=beta p_f(S)+alpha Var(f)1[S=FULL], S!=0.     (1)

For our calculation alpha=1/6, beta5/6. Every FULL atom just listed is source-positive. Therefore q has EXACTLY source support at the root and BOTH children. A zero empty mass remains zero. Normalization follows by summing(1). No reference-only source-zero row is suppressed; in this family none is introduced by the prescribed reset.

For either epsilon sign, G_epsilon(x,j,z)=epsilon atx0,v(j,z) atx1. Its reference R copies actual zero-data masses(epsilon+/-Ev)^2/4 and puts q_v(S)/4 on each of the two x copies for nonempty S. This complete law is normalized, matches source support, and has KL D(P_G||R)=D(p_v||q_v)/2. Queryj with actual coherent kernel P_y/(2Pbar), fair on erased source-zero rows; normalize the reference child using its OWN actual outcome r_y. ACTUALLY reset BOTH children to their same-alpha outer lifts. Sigma is the physical mean of fresh KL minus inherited KL.

## 2. Exact normalized transaction formula
Put e=delta^2. The two zero-data erased source masses are

    A_c=(1-2c epsilon delta+2e)/4, c=+1,-1.

Their erased reference/source ratios are1-alpha e/(4A_c). At remaining-full z frequency the aggregate erased source mass is5e and its reference/source ratio is beta+alpha(1-e)/(10e). All other nonzero rows have ratio beta. The two fresh children have means0,-2delta and full squared coefficients16e,4e. Their nonfull terms cancel EXACTLY in

    sigma=(1/2)mean_y D(p_vy||q_vy)-D(Pbar||Rbar)+D(fair||r). (2)

For constant spectator, B=R, so this is the A039 compensated identity with no spectator quotient. In natural units the surviving expression is

    (ln2)sigma = V + e ln R(e) -(1/2)ln(1-eta^2),          (3)
    V=sum_c A_c ln(1-alpha e/(4A_c)),
    R(e)=(8192/3125)*(1+49e)^5/[(1+80e)^4(1+16e)],
    eta=2r_0-1=(1/6)[3/10-4e/5-e(1+2e)/(2(1+4e^2))].

All denominators are positive. Epsilon only swaps the two vacuum rows, so the formula and outcome law agree for both signs. The ACTUAL r0=(1+eta)/2,r1=(1-eta)/2. To derive eta, split the reference as beta P+alpha M, where M is the alpha1 spike law's outer lift. At remaining full the physical kernel sends to child0 with probability4/5. At each vacuum row its child0 probability is1/[2(1-2c epsilon delta+2e)]. Summing M through these rows gives the expression above. This explicitly retains the effect missed by a phase-blind or unnormalized reference.

## 3. Uniform positive lower bound: local influence tax is false
For k>=5, delta<=1/32,e<=1/1024. Since A_c>=(1-2delta)/4, the quantity z_c=alpha e/(4A_c) lies in[0,1/2]. Thus ln(1-z)>=-z/(1-z)>=-2z gives

    V>=-alpha e=-e/6.                                  (4)

Also1+80e<=9/8,1+16e<=33/32; the numerator factor(1+49e)^5>=1. The rational inequality

    (8192/3125)>(9/8)^4*(33/32)

therefore gives R(e)>1. The subtractions in the eta bracket are bounded by(4/5)e+e(1+2e)/2<=2e for e<=1/1024. Consequently the bracket>=3/10-1/512>1/4, and eta>=1/24. The elementary inequality -ln(1-t)>=t yields

    -(1/2)ln(1-eta^2)>=eta^2/2>=1/1152.

Combining(3)-(4),

    (ln2)sigma >=1/1152-1/6144=13/18432>1/2048;
    sigma>1/(2048 ln2),
    sigma/Inf_j(v)>2^k/(2048 ln2) -> infinity.            (5)

All comparisons are rational or elementary monotone logarithm bounds. In fact delta->0 gives sigma->-(1/2)log2(399/400)>0; this limit is supplementary to the finite uniform lower bound(5). This REFUTES a dimension-independent bound sigma<=K Inf_j for this fixed prescribed same-profile rule, even with SAME old/new alpha, exact matching empty masses, exact SAME support, and both physical terminals. It is NOT a counterexample to FEI. This refutes an ALL-coordinate local refresh price, not an existential suitable-coordinate rule. Keeping the inherited law or choosing another coordinate is not excluded; the prescribed reset is not asserted necessary for every FEI strategy. The earlier high-influence parity-point price is not contradicted: these queried influences vanish.

## 4. Independent source eligibility and recovery, without a new bank
The obstruction is local. A genuine unspent original source can still pay this one positive conversion. For k>=10 let h=v_k and use F_h=chi_a atx0,h atx=b=1,+1 otherwise. Fix the ORIGINAL correlated lift Q0 using alpha0=1/8 factor law(1): copy all six zero-data/control masses and use q_h(S)/16 at four nonempty-data control copies. No earlier canonical conversion is included.

We first PROVE the source price rather than assume FEI. For a Boolean f on n bits with Fourier coefficient1-2s at a character, put a=1-(1-2s)^2. Partitioning the squared law into that atom and its complement gives H(f)<=h2(a)+a log2(2^n-1). For v, its named character coefficient is1-5delta, so delta<=a<=10delta. Since log2(1/a)<=k and log2(euler)<2,

    H(v)<=10delta(2k+3), I(v)>=(1-5delta)^2>=1-10delta.

For k>=10, delta(2k+3) decreases with k. Initial D(p_v||q_v^0)<=log2(8/7)<1/5. Therefore

    4I(v)-CE(p_v,q_v^0)
      >=4(1-10/1024)-230/1024-1/5
       =9053/2560>7/2.                                (6)

For g,g', the main character coefficients are1-4delta and1-6delta. Their complementary masses lie between delta and12delta, and dimension is k, so H<=12delta(2k+2), I>=1-12delta. The same rational endpoint bound gives4I-H>7/2 for BOTH physical target children. These estimates use only explicit Fourier coefficients and entropy partitioning; no conjectural arbitrary-core FEI premise.

Queryb; retain b0. In b1 querya; retain BOTH signs. ACTUALLY reset both activation references from inherited Q0 to their alpha1/6 lifts. Let sigma1 be the complete weighted first reset. Then queryj in BOTH already-reset a descendants; retain all four new children, ACTUALLY reset to their alpha1/6 lifts, and call the global second increment sigma2. All complementary b0 terminal remains. No prefix or further profile generation is included in this recovery theorem.

The standard source sectors, reconstructed here, give A0=D(P_F||Q0)=D(p_v||q_v^0)/4, H(F)<=3+H(v)/4, I(F)=1+t/2+I(v)/4. With M0=4I(F)-H(F)-A0,

    M0>1+2t+7/8, 2t=1+delta.

The complete fresh bill of EITHER reset generation is <=(1/4)log2(6/5)*Var(v) or its mean child variance, hence<11/160. For the second generation use mean Var(v_y)<=Var(v). These are bounds on gross fresh KL; actual signed new-minus-inherited sigmas are retained. In particular sigma2=(1/2)sigma>1/(4096 ln2), while

    M0-sigma1-sigma2>1+2t+7/8-11/80>15/8.             (7)

The b/a control queries have zero erasure and outcome KL: the likelihood ratio depends only on the unchanged data mask, while matching empty mass preserves each fair physical outcome. Hence their inherited activation references are EXACTLY the alpha0 lifts. The first actual reset is sigma1=[D(p_v||q_v^(1/6))-D(p_v||q_v^(1/8))]/4>0: KL along this nontrivial affine reference segment is strictly convex with its minimum at the parameter value alpha=0. This is an exercised positive debit, not a hypothetical fresh bill.

No variance reserve is renewed: both gross bills are charged against(6)'s SAME original source slack. The exact full terminal surplus also has a proved lower bound. For J_epsilon(f), 4I-H>=-2epsilon Ef+(4I(f)-H(f))/2. Both target children obey4I-H>7/2, and the two fair a signs cancel their means. The complete activation pair afterj therefore has surplus>7/4; b1 reach is1/2, and retained b0 contributes1, so S=4If-Hf>15/8.

Let e_hist=H0-Hf-4(I0-If). Keeping the ORIGINAL A0, BOTH actual sigmas, all erasure/outcome and terminal KL, signed recovery is algebraically

    S-[A0+e_hist+sigma1+sigma2]_+
      =min(S,M0-sigma1-sigma2)>15/8.

Subtract the SAME eligible prior debit0<=omega<=1/4 ONCE: remaining owner>13/8. This separate recovery implication proves that failure of an influence-priced LOCAL reset does not imply insolvency of the original account or disprove FEI.

## 5. First unsupported universal line
An arbitrary-factor full-spike supplier cannot be closed by charging each actual reset only to the queried influence: equation(5) rules that rule out on an actual same-support Boolean family. The remaining bridge is to charge necessary cumulative conversions to ACTUAL unused ORIGINAL source surplus (possibly phase/occupancy information), without renewing it, and to supply an influence-priced initial reference for arbitrary Boolean cores. The explicit character-near source slack(6) pays this single transaction, not unlimited fixed-size resets. No universal FEI constant improves. Collision T=L/Z=H(v/Z)-log2Z remains tensor-additive and unchanged; the already-refuted fixed raw-L payment is not revived.
