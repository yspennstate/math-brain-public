# Stage19 working derivation: two-private reserve conversion

Units bits, uniform probability Fourier normalization. Full FEI OPEN. All new results pending independent reconstruction.

Let G(S,U),H(S,V) be Boolean, with S,U,V disjoint physical blocks and z fresh. Set u(s)=E_U G,v(s)=E_V H, a=Fourier(u),b=Fourier(v), rhoG=1-Eu^2,rhoH=1-Ev^2. No independence across shared rows is assumed. The private coordinate blocks U,V ARE disjoint. Shared parent amplitudes are (a+b)/2,(a-b)/2; private G and H frequencies split equally into selector sectors. Thus exactly

 B=1-(||a||^2+||b||^2)/2+sum_T Phi(((a+b)/2)^2,((a-b)/2)^2),
 d=Pr[G!=H]=(1-<u,v>)/2,
 I(F)=(I(G)+I(H))/2+d.

For L(a,b)=Phi(((a+b)/2)^2,((a-b)/2)^2)-(a^2+b^2)/2, one has B=1+sum L. At differentiability points,

 L_aa=[ln(2(a^2+b^2)/|a^2-b^2|)+2a^2/(a^2+b^2)-2]/ln2-1 >= -2/ln2.

The last bound follows from the logarithm being at least ln2; all other terms are nonnegative. The same holds for L_bb. At a=+/-b the first derivative is continuous, since x^2 ln(x^2) has derivative tending to zero at x=0, while its negative has second derivative tending positively to infinity. For fixed b=0, L(a,0)=0 identically including the origin. Therefore L(a,b)+a^2/ln2 is globally convex in a for each fixed b, and likewise in b. This proves global semiconvexity across the diagonal singularities and axes, without assuming twice differentiability there.

If u(s)=chi_R(s)u0(Ls),v(s)=chi_R(s)v0(Ls) for a common independent parity map of rank r<=3, B and d reduce exactly to this quotient. Let M=2^r. For a single row variable u0(y), sum_T (da_T/du0(y))^2=1/M, so B+(sum_y u0(y)^2+v0(y)^2)/(M ln2) is convex separately in each of its 2M variables. Rounding each row independently to +/-1 with the stated mean therefore gives

 B(u0,v0) <= E B(sigma,tau)+(rhoG+rhoH)/ln2
             <=4d+(rhoG+rhoH)/ln2.

The last step is A012 v6 applied to the two rounded Boolean phases on at most three bits; average rounded disagreement is exactly d. Complementing H permits d*=min(d,1-d) in the 4d term without changing rho or B. C005 then gives Delta<=K d*+(rhoG+rhoH)/ln2, K=4+2/ln2.

For calibrated complete child references (every shared-only singleton at its true child mass; whole private conditional reference retained including off-target mass), take Q=P_F on shared-only parent atoms, and R_Gcal/4 or R_Hcal/4 on each corresponding nonempty-private atom in each selector sector. Disjoint U,V make those sectors disjoint. Exactly sum Q=1, D_F=(D_Gcal+D_Hcal)/2, CE_F=average child CE+Delta. No joint private entropy is dropped.

Define inherited old debits bG,bH>=0 and available child reserves SG=K I(G)-CE_Gcal-bG, SH=K I(H)-CE_Hcal-bH. If SG+SH >=2(rhoG+rhoH)/ln2, the same rate K admits the parent and preserves average old debit; no reset or renewed bank is used. More strongly, for any chosen nonnegative booked debits satisfying CE_j+b_j+(2/ln2)rho_j<=K I(j), that inequality suffices. This is an explicit private-variance reserve condition; it is not an assumed parent entropy bound.

The finite child lemma and the new admission are now proved in the sections below; the earlier pilot is only discovery evidence. Arbitrary-length compositions still require the strengthened reserve to survive the next node; that is not yet proved.

## Exact child certificate and complete reference allowance

Every nonconstant Boolean function on at most four PHYSICAL coordinates satisfies H<=4I-1/4; constants have H=I=0. child_exact.py author enumerates all65536 truth tables using integer FWHT and lower logarithms floor(log2(k^64))/64, certified by integer powers. Its minimum exact lower gap is579/2048. The independent replay enumerates in Gray order, updates character sums by the unique truth flip, checks physical-edge influence and uses independently coarser logs floor(log2(k^32))/32. Its minimum lower gap is265/1024. Both exceed1/4. The frozen target was only1/8; these exact minimum outputs prove the stronger1/4 without a new search or parameter change. Padding dummy variables covers fewer than four essential variables. The replay uses no author spectrum routine. Matching spectral histograms are checked. No Boolean PAIRS are exhaustively enumerated.

Calibrate every shared-only child singleton to its true mass. On the entire nonempty-private category, of true mass rho>0, supply ANY normalized prior pi and take R=15P/16+rho*pi/16. The reference dominates15P/16 pointwise, so D(P||R)<=rho log2(16/15)<1/8, since (16/15)^8<2. Full joint private true entropy and off-target prior mass are retained; no independent-row prior is assumed. Thus CE<=4I-1/8 for every nonconstant at-most-four-bit child. If rho=0 omit the category, and constants use the vacuum. A supplied historical reference satisfying this dominance is retained; arbitrary historical replacement is NOT free.

## Same original bank and genuine both-private admission

For each such child book b_j=(2/ln2)I_shared(j) BEFORE the query. The ORIGINAL child stock KI_j-CE_j-b_j contains (2/ln2)I_private(j), plus at least1/8 when nonconstant. Conditional Poincare gives rho_j<=I_private(j). Average the two child stocks, charge (rhoG+rhoH)/ln2 ONCE for the new variance correction, and retain both old bookings. The normalized parent reference from above satisfies

 CE_F+(I_shared(G)+I_shared(H))/ln2 <= K I(F).

If both children are nonconstant, there is in addition at least1/8 of UNUSED original source after that conversion and after preserving the displayed old booking. Indeed each child's conservative surplus above4I is at least1/8; the averaged surplus remains1/8. For single private bits I_private=rho, so the private-variance stock is consumed exactly by its upper debit; the retained1/8 is NOT that consumed stock. For multiple private bits the further remainder (I_private(G)+I_private(H)-rhoG-rhoH)/ln2 is nonnegative and can be separately recorded. K(d-d*) is also nonnegative and not needed here.

This holds whenever EACH child depends on at most four physical coordinates and their actual intersection has at most three coordinates, using the supplied complete reference class. It includes all65536^2=4294967296 ordered pairs on three shared bits and one independent private bit per branch. Of these,65280^2 use BOTH private bits genuinely. The all-pair result follows analytically from the common-rank3 variance lemma plus the65536-child exact certificate; finite parent fixtures do not prove the pair quantifier. Any smaller nonnegative old child debits can also be retained. No stock is renewed or counted twice.

The finite-node rule can be added to the v6 syntax. Physical restrictions keep each branch at most four-bit and their intersection at most three-bit, or select an already certified child. The same finite lemma constructs certificates for those RESTRICTED FUNCTIONS. Signs, disjoint products, fresh balancing and activation remain closed. Restricting a rare activated balanced tensor still recovers its original seed, preserving hidden-core membership reflection. The five-bit at-least-two sign has no new root, because its two cofactors share all four remaining essential variables; the old affine-rank and product-minor exclusions still apply. No opaque child leaf is added. This is structural function-class heredity, NOT a claim that reconstructing a restricted reference transports a prescribed ancestral Q at no cost.

## Exact frontier and physical profile transport

The generic variance-transfer lemma applies in arbitrary physical shared dimension and arbitrary disjoint private dimensions when the ACTUAL two conditional means occupy a common affine Fourier coset of dimension<=3 and the displayed child variance reserves have already been proved. It is sufficient, for example, that CE_j<=4I_j with old bookings at most(2/ln2)I_shared(j); disjoint products of source-complete4I certificates also supply such stock. This does not extend a4I source through arbitrary activations automatically.

For private-history stability of the common quotient, require the full factorization G=chi_R g(L(S),U), H=chi_R h(L(S),V), or recompute and verify the actual means after each physical query. A013 stage18's exact conditional-moment block law supplies that update. Its stale-profile counterexample forbids carrying only old marginal probabilities. The finite physical node above has the required factorization trivially.

FIRST UNIVERSAL unsupported line: fund another colliding node/query from the SAME DIMINISHED source after the private-variance conversion, retaining the old shared booking, both full references and all earlier costs. The parent's K-bound alone does not regenerate(2/ln2)rho. The finite result leaves at least1/8 of unused original stock for genuine both-private pairs, but no universal next-query bound fitting that stock is proved. NEXT is one actual shared-coordinate query after this paid node, with its inherited Q and original remaining stock, using the exact conditional-moment update and no reference reset. Universal common-rank3 existence, rank4 same-constant payment, original L/S/R contraction and full FEI remain open. New v7 awaits independent-agent review.
