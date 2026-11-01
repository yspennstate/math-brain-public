# Stage19 working reconstruction

Target A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@2, original finite source reference and C0 retained throughout. Independent review in progress; no acceptance yet. Full FEI OPEN.

Source inheritance identity: with marginal r, average true child law m and raw child 2r*pi, source mass s, Z0+Z1=2s. On true atoms child likelihood ratio is (m/r)(Z/s). Parent conditional divergence yields Dparent-average Dchild = conditional KL - average log2(Z/s). This is nonnegative by arithmetic-geometric mean. Zero true fibers keep normalized posterior and reference mass. This verifies the load-bearing contraction directly, including subprobability penalty -log2(s).

## General envelope dependency, reconstructed

Let rho=pt. The actual data marginal is q=A^2-4rho*b*A+4pt^2. Young gives q<=2A^2+6pt^2. For beta=6rho, the complete prescribed data model (R+beta U)/(1+beta) has mass (s+beta)/(1+beta), covers every true atom, and has nonnegative log loss. Its cost is at most 2c+beta(2n+r-log2(6)+7). This uses log2(1+beta)<=2beta and beta<=3/2, without renormalizing the source.

To reconstruct the stated selector bound independently, the nonempty selector mass is e=4p(1-p)t, spread uniformly over 2^r-1 labels. Hence B<=H(selector)=h2(e)+e log2(2^r-1). In h2(e)<=e[log2(1/e)+log2(euler)], the two logarithms involving 1-p cancel exactly: log2(1/e)+log2(2^r-1)=n+2r-2. Since log2(euler)<2, B<=e(n+2r)<=4pt*n+8rpt. Adding the data cost gives 2c+pt[16n+14r+42-6log2(6)]<=2c+30pt(n+r). This closes the selector-entropy dependency without quoting an omitted coefficient lemma. It is a reconstruction of the existing bound, not a substantive repair.

For the old padding-prefix dependency, direct two-amplitude JS bounds give entropy release <=h2(d_j)+4d_j/ln2<=d_j[log2(1/d_j)+9], with d_j=2rho*2^j. Thus the full original padding-prefix bill is <=(1+2^-ell)c+2rho*T, T=15(s0-ell)+ell(s0+8)-ell(ell-1)/2, s0=a+b+r. For q=b+r>=2, T/a<=q^2+15q+7 and this divided by2^q decreases to its maximum41/4. The sign-sensitive division uses the positive remaining numerator H=(15+ell)q-7ell-ell(ell-1)/2; do not divide its negative terms separately. Therefore L_ell<=3c/2+41Ig/4. With E<=Ig/4 and K=4C0+15, residual >=(3C0/2+1)Ig. The minimum nonzero cube boundary >=a follows by slicing into two sections; neither full coordinate dependence nor FEI is used.

## Source-prefix v2: full ledger and original bank

At source depth k let w=2^-b, lambda=w*2^-k. The unedited source stopping tree includes EVERY nonmatching sibling. Complete divergence contraction above gives sum alpha_v D_v<=D; entropy contraction gives 2^-k H_h<=H. Replacing only the active source terminal by its prescribed first-edit floor adds at most D_h+2H_h+15B_h to its divergence, B_h=2p*2^-(a-k)*(a-k+r). Therefore average final divergence <=(1+w)D+2wH+15lambda B_h. No conditional distribution or normalizer is omitted.

For any prescribed models, signed node increment lambda_v=average Dchild-Dparent telescopes algebraically to L=H(F)+average final D. Combining the root SCALAR entropy bound H(F)<=2H+15Broot gives L_k<=2(1+w)c+30pt(2a+b+2r-k). For a>=2,k>=1, minimum boundary Ig>=2a*2^-a gives [Broot+lambda B_h]/Ig<=2^-(b+r)[2+(b+2r-k)/a]<=3/4. Also w<=1/2. Thus L_k<=3c+45Ig/4. Since I(F)>=3Ig/4+C+J, the SAME K leaves at least K(C+J).

At k=a, all source leaves have one reference atom of mass s. Their divergence is -log2(s), not zero. The final scalar floor (s+6p)/(1+6p)>=s implies edited-terminal divergence <=-log2(s)<=D. Thus L_a<=H(F)+D<=2c+15Broot and residual >=C0 Ig+K(C+J), also when a=1. There is no dimension-zero use of the positive-dimensional envelope. Positive Z factors follow from actual positive child support; all true-zero fibers keep their reference mass.

Root residual >=(C0+15/2)Ig+4C0(C+J); old padding residual >=(3C0/2+1)Ig; source residual >=K(C+J). Therefore U_star=min{(C0+1)Ig,K(C+J)} is simultaneously admissible at every old frontier. This is sufficient, not necessary. Physical reaches are the original fair-cube reaches. No repeated witness/leaf is transmitted or counted twice. Optional unqueried terminal reference tensors remain complete products, including zero-true terminal fibers, by core-only/product-compatible inheritance.

## Two-edit v3: independent reconstruction of the new bottleneck

For the second floor use Young with coefficient1/2: q<=3P/2+8rho U. The actual prescribed model (Qold+8rho U)/(1+8rho) has its full mass. With beta=8rho<=2, the data CE is <=3c_old/2+beta(2m+r+4). The true selector mass lies between2rho and4rho, hence B<=4rho(m+2r+2). Summing yields CEnew<=3c_old/2+40rho(m+r), including constant source functions with finite positive-cost references. No descendant source certificate is introduced.

Write F2=g+delta1+delta2 on the final cube. Weighted Cauchy-Schwarz, 2/3+1/6+1/6=1, yields P_F2<=3P_g/2+6 delta1hat^2+6 delta2hat^2. Each delta_i is a point cylinder and delta_i_hat^2=4rho_i U_Di. This remains true when the two edit points overlap: the second sign is the ACTUAL F1 value. A mixture with beta_i=24rho_i and B=sum beta_i<=9/64 has scalar CE<=3H/2+sum beta_i(2Di+4)<=3H/2+60sum rho_i Di. This is ONLY a scalar entropy bound; no actual reference is replaced by the auxiliary mixture.

For each old nonempty frontier, v<=1/2 is the first active reach before source restriction (v=2^-ell during padding,2^-b thereafter). The original stopping-tree source divergence total is <=D; active weighted source entropy <=vH and active weighted source cost <=v c.

If the second point is in the first active leaf, retain every off-leaf D and bound the new active D by 3CE1_active/2 minus its actual nonnegative entropy. The old active cost is <=2c_h+30rho1_local(D1-depth). Then L2<=3c+105rho1D1+100rho2D2. This uses the paired CE=H+D cancellation; counting H and D separately again would inflate the price.

If the second point is in a distinct off-leaf j, baseline source divergence is <=D. Relative to it, the first active leaf adds weighted(D_h+2H_h)+30rho1(D1-depth), and the second leaf adds weighted(D_j/2+3H_j/2)+40rho2(D2-depth_j). Because these are DISTINCT leaves, their extra weighted D terms together are <=D, not2D. Active weighted H<=vH and second off-leaf weighted H<=H/2. Adding the scalar entropy bill gives L2<=2D+13H/4+90rho1D1+100rho2D2<=13c/4+105rho1D1+100rho2D2. At the root, the direct floor bound is <=3c+45rho1D1+40rho2D2. All cases use the ORIGINAL source R and c.

For a>=1,b>=6,r1,r2>=1, q=b+r1>=7 and monotonicity of (q+1)/2^q give rho1D1/Ig<=1/32, rho2D2/Ig<=9/512, E1/Ig<=1/128, E2/Ig<=1/32, G1/Ig<=1/16. Literal physical edge counts give I2=Ig+G1+G2-E1-E2>=(123/128)Ig+G1+G2. Therefore L2<=13c/4+645Ig/128 and KI2-L2>=[19C0/32+75/8]Ig+K(G1+G2). Subtract FULL old U<=U_star<=KIg/16 to retain [11C0/32+135/16]Ig+K(G1+G2)>0. These rational coefficients were independently expanded, not read as numerical approximations.

All signed conversions are counted via L2=H(F2)+sum leaf reach*D. An earlier complete L1 stays charged: B2=(KI1-L1-U)+K(I2-I1)-(L2-L1). This identity changes the constructed target function and is NOT a KL-only reset on a fixed target. K and C0 are not renewed. Optional tensor-terminal costs stay additive and cannot fund the source bank. The v3 statement does NOT price arbitrary positive-part accumulation separately from its signed operation ledger.

## A095 rare-allowance obstruction and A094 third-reset sign

For h4*h2 padded by m>=8, delta=2^(-m-6), source amplitudes have magnitude7/16 on4 masks and1/16 on60. Root true old masses (a-delta)^2, reference (1-W)a^2, W=2delta-64delta^2; every complementary actual/reference atom equals delta^2. All atoms and normalization remain. Triangle inequality gives sqrt((1-W)chi2)<=W+16delta+128delta^2<=20delta, hence Droot<(19200/31)delta^2<delta. This is complete root divergence, not a fresh law.

After the narrow query, true source support S has16 masks, true mass1-Wchild with Wchild<=4delta. Fresh quarter-uniform reference gives Qfresh(S)<=3/4+4delta<4/5. Log-sum on {S,complement} yields Dfresh>4041/16384, using log2(5/4)>1/4 and h2(Wchild)<27/8192. Inheritance contracts average D, so the actual reached signed excess e1=(Dfresh-Dold0)/2>4039/32768>1/10. At the SAME A011 source parameters C0=4,K31,Ig=3/2,C+J=(m+1)delta, its displayed sufficient U_star<=279/16384<1/10. The ratio e1/(C+J) is unbounded. This invalidates automatic admission through that particular sufficient cap, not A011 v2/v3: root models and policies differ and no handoff is identified.

For A094's separate third-reset witness, the three actual child probability classes are49/64,1/64 repeated7,1/64 repeated8. Inherited reference classes18375/33856,1695/33856 repeated7,113/8464 repeated8 normalize; fresh classes63/128,7/128 repeated7,1/64 repeated8 normalize. Their likelihood ratios are12250/11109,3390/3703,452/529. Therefore e3=log2(N/D)/512, N=12250^49*3390^7*452^8,D=11109^49*3703^7*529^8. Exact N>16D,N^2<512D^2 proves1/128<e3<9/1024. Only the shortcut 'canonical means free' is refuted.

## Exact unpaid universal continuation

No gap was found in the named source-prefix v2 or two-edit v3 bounds. Their supplied influence-priced initial source reference remains a hypothesis. Arbitrarily many interacting edits at FIXED padding and rate are unproved: additional exceptional leaves can accumulate source entropy and conversion liabilities. An arbitrary non-point-source nonempty-profile conversion at one retained original reserve is also not paid by the rare-edit sufficient cap. These are universal gaps, not consequences of the finite checks.
