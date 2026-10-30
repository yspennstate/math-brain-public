# Early guard exposure keeps the original source

Rung: analytic restricted-history proof; exact validation and independent review are recorded separately. Full FEI remains OPEN. Version1's arbitrary-carrier PRIVATE history theorem is retained. The new clause removes the late-guard restriction for the complete restricted Maj3 carrier state space.

Let h(s)=+1 at the shared three-bit vertices of weight at most1 and -1 elsewhere. Replace its values at vertices0 and1 by arbitrary correlated Boolean private profiles V,W. The remaining shared and private physical coordinates are uniform and independent. Every adaptive tree may query ANY remaining physical coordinate, including a common guard before any or all shared coordinates, and may stop anywhere. Each physical coordinate is queried at most once on a path. There is no hypothesis on either edited mean.

At a descendant let r be the number of shared bits, p=2^-r, and L the labeled surviving edited vertices. Put

    U=p sum_live H(profile),
    R=r p sum_live [1-(E profile)^2].

With two live adjacent edited vertices retain Xi=p sum_(T nonempty) k(Vhat(T),What(T)), where k(a,b)=[g(a+b)+g(a-b)]/2-g(a)-g(b), g(t)=-t^2 log2(t^2), g(0)=0. Set Xi=0 in single-profile and no-profile phases. All terminal entropies are the COMPLETE actual Boolean spectra, not spectra with the empty row omitted.

## 1. The private price does not require a hidden guard

Expanding actual Walsh coefficients at every private row gives

    H(F)=U+Xi+2R+Emean-p sum_live g(E profile).        (1)

Emean is the complete empty-private sector, including its interference with the current nonconstant carrier. Along a private query let a,b be the singleton profile coefficients, with dead profiles omitted, and t=p sum_live a^2. The translated mean-row derivative law has entropy at least r-1 in the two-profile phase, and exactly r in the one-profile phase. Its total row mass is 1-p sum_live Var(profile)<=1. Thus the finite curvature calculation gives

    (Emean+R)'' >= -(2+6/ln2)t.

For completeness, write the affine empty-sector coefficients c_j(u), derivatives d_j, sum d_j^2=t and M=sum c_j(u)^2<=1. For t>0, the probability law d_j^2/t has entropy at least r-1 (or r for one profile). Nonnegativity of its relative entropy against c_j^2/M implies -sum d_j^2 log2(c_j^2)>=t(r-1); a zero c_j with nonzero derivative gives the correct positive infinite limit. Since g''(c)=-2log2(c^2)-6/ln2 and R''=-2rt, summing gives the displayed bound. The midpoint loss for a second-derivative lower bound -A t is at most A t/2. The remaining mean-g terms have midpoint loss at most6p sum|a|. These yield the residual stated below, with no dimension-dependent constant.

The binary entropy decomposition proving the r-1 bound is the same two-row Hadamard law used to prove -4p<=Xi<=0; for one profile its shared row magnitudes are all equal. The zero-direction case is exact. A varying zero coefficient causes only an integrable logarithmic singularity: g is C1, so corrected derivatives glue across finitely many affine row zeros. All means stay in [-1,1], where |g'|<=6.

The midpoint estimate and |profilehat(i)|<=Inf_i(profile)<=1 give

    Delta_private H(F)
      <= Delta_private U + release_R + 12 Inf_private(F)+Delta_private Xi. (2)

Indeed the residual is at most p[(1+3/ln2)sum a^2+6 sum|a|]<=12p sum Inf_i(profile). The actual query influence is EXACTLY p sum_live Inf_i(profile), by disjoint physical edited events. Also release_R=r p sum_live a^2. This reconstructs the A077/A076 mean-sector proof for nonzero means and for single-profile states. When r=0 the actual function is a profile or a carrier constant, and Delta H=Delta U exactly. No core FEI premise is used.

## 2. A character cofactor costs at most ten actual query influences

Suppose one actual child at a physical query is a signed character L on the OTHER inputs; the other is any Boolean G. Multiply the parent and both children by L. This permutes Fourier labels and preserves all three entropies; because L does not use the queried bit, its physical query influence is unchanged. The children become +1 and G L.

Write j=Pr(G!=L), m=E(GL)=1-2j. Direct complete Fourier expansion yields EXACTLY

    Delta H=4j(1-j)+g(1-j)+g(j)-g(1-2j)/2.          (3)

For 0<=x<=1, -x ln x<=1-x gives g(x)<=[2/ln2]x(1-x). This includes x=0,1 by continuity. The first term of the positive atanh series gives ln2>=2/3. Since g(1-2j)>=0,

    Delta H <=10j(1-j)<=10j.                        (4)

This is a universal character-cofactor lemma, not a majority-specific entropy certificate. It retains the other child's complete entropy. At j=0 both children coincide and Delta H=0; at j=1 they are opposite characters and again Delta H=0. No division by j or Fourier amplitude is used.

## 3. The remaining Maj3 shared queries have a paid alternative

There are exactly27 partial shared assignments and27 remaining-coordinate queries among them. Their structural classification is finite and exhaustive; private dimension and private spectra are unrestricted.

* If a child has no surviving edited vertex and its restricted carrier is a character, apply(4). This includes the shared query immediately following an EARLY guard on the active common-prefix branch: the inactive sibling is a literal, regardless of both nonzero edited means.
* If there is no such clean character child, except for the final two-profile separator below, at least one fixed disagreeing UNEDITED carrier edge gives physical Inf>=1/4. Every one-bit physical selector satisfies Delta H<=2: its data marginal is the half-mixture of the two normalized child spectra, with mixture entropy at most1+average child entropy, and conditional selector entropy at most1. Thus Delta H<=8Inf at these states. This explicitly uses an actual carrier edge, not a guessed mean or a mask with edited vertices set to0.
* If r=1 and both vertices are edited, this is an ordinary one-bit selector of V,W. Its nonempty-private erasure is at most p(Var(V)+Var(W))=release_R. Its empty-private coefficients are a=(mu+nu)/2,b=(mu-nu)/2. The elementary ln(1+x)<=sqrt(x), obtained by differentiating sqrt(x)-ln(1+x), gives Phi(a^2,b^2)<=[2/ln2]|ab|<=3|ab|<=3 Inf, since |mu-nu|<=2Pr(V!=W) and |mu+nu|<=2. The physical JS bound is JS<=2 Inf/ln2<=3Inf. Hence Delta H<=release_R+6Inf. The JS inequality is the campaign's C005 scalar two-child bound, independently reconstructed in A076 v8 section1.

For all27 cases, therefore,

    Delta_shared H(F)<=release_R+10 Inf_shared(F).  (5)

At a shared query, U is harmonic and release_R=p sum_live Var(profile)>=0, including event death and separation. In particular the proof NEVER applies A077's zero-mask bound after guard exposure. CARRIER_CLASSIFICATION.json records every labeled case; the proof of each case is either the character lemma, an explicit fixed-edge floor, or the r=1 separator calculation. No finite-dimensional profile census is used to justify arbitrary private profiles.

## 4. The SAME diminished original collision account

Use exactly A076/A077's accepted freezing convention. At original continuation state o with two live profiles let e_o be its vertex mass, Xi_o its signed collision, and B the UNUSED original budget AFTER all old debits. Assume B>=4e_o, and set C=(B-Xi_o)/e_o. Until separation define

    K_v=p_v C+Xi_v.

Then K_o=B and K_v>=p_v(C-4)>=0. Under private queries Delta Xi+E K_child=K_parent. At a nonseparating shared query both event masses and Xi double on the surviving branch and vanish on the other; K is harmonic. At the separating query FREEZE K_parent in BOTH actual children, and retain it on all later descendants, even if their edited event dies. It is a transported ancestor earmark, not a descendant certificate. Thus K is harmonic at EVERY shared query. The source density p, doubled on a surviving common event and zero on its killed sibling, is frozen as a bookkeeping mass at separation. It is a martingale under the original physical reach probabilities. Every finite stopping frontier consequently satisfies

    E K_leaf>=B-4e_o.                               (6)

Combining(2),(5) with this same account and finite telescoping gives, for EVERY adaptive mixed tree, including arbitrary early guard exposures,

 H(F_o)-E H(F_leaf)+E[R_leaf+K_leaf]
   <= U_o-E U_leaf+R_o+B+12 P_private+10 P_shared.   (7)

P is the sum of actual queried influence times ORIGINAL physical reach. Both full wrapper terminals, both inherited profile entropy allocations, and all original debits remain. The maximum continuation transaction price stays12. This is not a universal FEI rate: arbitrary root input and terminal entropy are not supplied free.

## 5. Actual padding donor and the early-guard handoff

At the ORIGINAL source choose even k>=4, m>=2, V=y*bent_k(z), W=y[1-2*1{z=0,x1=...=xm=0}]. Then H(V)=k and I(V)=k/2+1, INCLUDING the guard. Its original C5 allocation splits ONCE as

    5e_o I(V)=e_o H(V)+S, S=e_o(3k/2+5).

Preserve the FIRST booked4e_o and any old D0>=0. After the first x1 answer retain BOTH actual answers and set B=S-D0-4e_o conditionally on each. Their original physical average is B. Admission D0<=S-8e_o gives B>=4e_o and the same expected remainder S-D0-8e_o. No descendant certificate is renewed, even when y or bent coordinates are queried early. The original e_o H(V) bill accounts for all inherited V entropy decrements plus its expected complete terminal entropy; S is its disjoint surplus, not a second copy of the original influence budget.

The executed fixture has k4,m2,e_o1/8,S11/8, the first debit4/8, ANOTHER old D0=1/8 and B6/8. It retains expected K>=2/8 after every tested complete history. Four mixed policies on BOTH original x1 answers expose y while shared bits remain, include both choices of the next shared query, then stop with private inputs still live. All complete terminal spectra and both full profile spectra are saved. All physical shared, private, bent, guard and padding influences are counted from actual truth tables.

## First unsupported universal line

For a general carrier, a shared query may have neither a character cofactor nor a fixed physical influence floor. The extra nonzero-mean carrier-row erasure then remains unpaid. Universal admission of an unused original donor and arbitrary inherited core/terminal FEI also remain open. The new theorem removes the guard-order restriction for the Maj3 carrier, and the character lemma supplies a reusable universal local clause. NEXT is the first nonconstant, noncharacter carrier-cofactor query with SMALL physical influence, retaining the same diminished source and both complete terminals; repeating guard-order or Maj3 checks would no longer address an open gap.
