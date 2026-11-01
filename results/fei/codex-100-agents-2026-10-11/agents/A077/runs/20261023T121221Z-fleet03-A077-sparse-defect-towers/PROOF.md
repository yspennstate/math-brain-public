# Positive subcube defects: arbitrary support size, one original account

Bits and independent uniform physical inputs. This extends A076's supplied-source depth-uniform account; it is not full FEI. Its numeric carrier admission explicitly depends on the supplied hereditary threshold entropy certificate. The private profile/terminal bills remain present.

## 1. Family and physical coordinates

Let h be central majority on odd d>=5 shared bits, positive at weight<d/2. Choose b>=1 free shared bits and c=d-b address bits with1<=b<=(d-3)/2, so c>=4. The separator is address bit1. Let A and B be the parallel b-dimensional subcubes whose address strings are0 and e1. Both lie entirely in h=+1: their maximum weights are b and b+1. Replace h by arbitrary correlated Boolean private profiles V,W on A,B respectively; elsewhere retain h. The private cube is independent of the shared cube. Each edited face has mass p0=2^-c and2^b vertices, which is UNBOUNDED in this family. The edits are not points padded by irrelevant variables: free shared coordinates still affect the actual outside majority and can be queried there.

At every mixed descendant, surviving events are zero, one or two parallel subcubes on the remaining shared cube. In the two-face phase their residual address strings remain adjacent. Let p be the common event mass and c_v its residual codimension; free shared coordinates do not enter c_v. After separation there is one face with its actual mass and codimension. The carrier h_v is always its ACTUAL threshold cofactor. It is+1 on every surviving edited face. All actual siblings, including event-dead nonconstant carrier cofactors, are retained.

## 2. Complete spectrum and exact mean-sector account

For a live face a let P_a be its private Boolean profile, mu_a its mean. Put

 U=p sum_live H(P_a), R=c_v p sum_live Var(P_a),
 m(s)=E_private F(s,private), E=sum_S g(mhat(S)),
 g(t)=-t^2 log2(t^2), g(0)=0.

Use Xi=p sum_(T nonempty)k(Vhat(T),What(T)) in the two-face phase, with k=[g(a+b)+g(a-b)]/2-g(a)-g(b); Xi=0 otherwise. A codimension-c_v face indicator has Fourier coefficients of magnitude p supported exactly on subsets of its FIXED address coordinates, zero at every frequency involving a free coordinate. Therefore the COMPLETE same-spectrum expansion is

 H(F)=U+Xi+2R+E-p sum_live g(mu_a).                 (1)

This is A076's point formula with the RESIDUAL ADDRESS CODIMENSION replacing total shared dimension. Replacing c_v by the number of remaining shared inputs would be wrong. It double-counts free-coordinate entropy and fails the saved exact checks.

Define Z=E+R-p sum_live g(mu_a)+1. Then exactly

 H(F)=U+Xi+R+Z-1, Z>=0.                           (2)

Indeed E>=0 since all mean-row Fourier coefficients are in[-1,1], g(mu)<1, and total edited mass p*number_live<=1. The constant1 remains on EVERY actual branch, including no-edit and constant terminals. Also R<=1: two faces have c_v>=1 and2c_v2^-c_v<=1; one face has c_v2^-c_v<=1/2 or codimension0 with R0.

The Fourier l1 norm of EACH face indicator is EXACTLY2^c_v*p=1 at every restriction. Thus

 ||mhat-hhat_v||_1<=sum_live(1-mu_a)<=4.

Since g is C1, including0, and |g'|<=6 on[-1,1],

 |E-H(h_v)|<=24, 0<=Z<=H(h_v)+26.                 (3)

The support cardinality2^b and its growth never appear in this bound. It is not a sum of independent point allowances.

## 3. SAME collision source and every physical query

After all old bookings supply one ORIGINAL B>=4p0, with Xi_o at the continuation root. While both faces survive use K=p(B-Xi_o)/p0+Xi. If an address gate kills both events, set K0 while retaining its actual carrier entropy. At separation freeze K_parent in BOTH actual children and every later descendant, including event death and constants. Under PRIVATE queries DeltaXi=DeltaK. Under a common ADDRESS gate both p and Xi double on its surviving answer, so DeltaXi=DeltaK=0. Under a FREE shared query p and Xi are unchanged on both answers, so again both decrements are0. At a separator Xi_parent<=0 disappears, while K is frozen; hence DeltaXi<=DeltaK. Therefore EVERY physical node satisfies

 DeltaH<=DeltaU+release_R+DeltaK+DeltaZ.            (4)

No local suffix price is newly issued. R releases0 under a free query, releases the usual codimension event mass at an address gate/separator, and releases c_v p sum(singleton profile coefficients)^2 at a private query. The actual event mass p is a martingale before separation, including free queries; freeze its bookkeeping value at separation. Thus for every finite adaptive mixed stopping tree,

 H(F_o)-E H(F_leaf)+E(R_leaf+K_leaf+Z_leaf)
 <=U_o-E U_leaf+R_o+B+Z_o,
 E K_leaf>=B-4p0.                                 (5)

Both inherited profile entropy bills and every complete actual terminal remain. This algebraic statement holds for ANY Boolean carrier positive on the faces; it does not supply a general carrier entropy certificate.

## 4. Original carrier quota: hereditary premise and physical ownership

The supplied threshold paper Theorem A equation(6), pages1-2, gives H(h_v)<9 I(h_v) for the threshold cofactors. This is an external theorem dependency, not independently proved by this stage. The maximal total influence M_r of a symmetric threshold is nondecreasing in r (the even step has equality, the next odd step increases by (2l+1)/(2l)). Consequently I(h_v)<=I0=I(h), and I0>=I(Maj5)=15/8>=1. From(3),

                       Z_v<=35I0.                (6)

Unlike point edits at0,e1, the present positive faces MAY REMOVE some original carrier pivots. Free-coordinate edges inside a face had h=+1 at both endpoints and still have identical profile values at both endpoints; these cause no loss. Separator edges between the two faces also originally had both values+1, so cannot remove pivots. For each other address coordinate, affected directed edges have measure at most4p0. Hence rigorously at the ORIGINAL root

 I_shared(F)>=I0-4(c-1)p0>=I0-3/4>=(3/5)I0,       (7)

because c>=4, (c-1)2^-c decreases thereafter, and I0>=15/8. This argument allows arbitrary profile means and correlation. It is not an assumed retention of every carrier edge. Therefore one ORIGINAL quota

 Q=96 I0 <=160 I_shared(F)                        (8)

has an actual physical source, independently of support size2^b. Its numerical value is the SAME96I0 allowance in A076;160 is the new conversion to actual edited shared influence after possible pivot loss, not a changed quota or a claimed160I0 source. The private bent donor uses disjoint physical PRIVATE edges, so it is not spent again to fund Q.

## 5. Old bookings and handoff; no prefix theorem silently transplanted

At an inherited prefix frontier keep its actual old shared bill L, admitted here with0<=L<=58 (for example an ALREADY CHECKED three-query5/15/38 prefix). Then from the SAME original quota define once

 Lambda=Q-L-Z>=3I0,
 L+Z+Lambda=Q EXACTLY.                            (9)

Freeze Lambda on every descendant of that frontier node. Combining an already-paid prefix with(4) pays EVERY finite subsequent mixed continuation, including arbitrary free/address queries, separation, early guard, private/bent/padding queries and stopping. The old collision FIRST4p0 and oldD0 remain in B=S-D0-4p0, with original S=p0(3k/2+5), even k>=4. Admission D0<=S-8p0 leaves E K>=S-D0-8p0. No descendant bent certificate or original quota is renewed. With an already-paid prefix whose shared charges L and private price12 have been checked, the complete source inequality is

 H(F_o)-E H(F_leaf)+E(R+K+Z+Lambda)_leaf
 <=U_o-E U_leaf+R_o+B+Q+12P_private,old-prefix.    (10)

The old E L cancels in the combined displayed inequality because it is explicitly DEBITED from Q in(9), not erased. All rows and old bookings remain in the saved ledger. Alternatively start(5) at the original root and admit Z_o from Q with L0; no prior local-price theorem is needed.

Important scope: the point-family5/15/38 prefix theorem is NOT automatically a theorem for EVERY block family here. General prefix use of(10) is conditional on that prefix's valid payment and bound L<=58. The actual non-point fixture verifies its complete declared prefix exactly; the algebraic all-depth extension(4)-(5) and original root admission do not require that prefix. This prevents a source/hypothesis reset disguised as padding.

Executed fixture: d5,b1,c4, four edited vertices in two genuine faces; k4,m2, BOTH initial x1 answers, FIRST4p0 and oldD0=p0. Here p0=1/16,S11/16,B6/16, expected K remainder>=2/16=1/8. Original I0=15/8,Q180. This differs from the previous POINT d5 fixture's1/16 because p0 doubled from1/32 to1/16; both retain exactly the same normalized guarantee2p0. The additional carrier quota is explicit, not paid by the small collision balance. Policies query the free shared coordinate and the separator after the three actual old address bookings, retaining both nonconstant carrier siblings and full core/terminal spectra.

## 6. Uniform-depth tower closure, with no repeated influence budget

The same expansion gives a static relative inequality, independently of any collision donor admission. At the original root Xi<=0, g(mu)>=0, R<=1 and E<=H(h)+24. Under the explicitly supplied threshold theorem,

 H(F)<=p0[H(V)+H(W)]+9I0+26
      <=p0[H(V)+H(W)]+(343/15)I0
      <=p0[H(V)+H(W)]+(343/9)I_shared(F).         (11)

The middle step uses I0>=15/8, so26<=(208/15)I0. The last uses the ORIGINAL physical edge-loss estimate(7). For every private physical coordinate i, the two disjoint activation faces give exactly

 Inf_i(F)=p0[Inf_i(V)+Inf_i(W)],
 I(F)=I_shared(F)+p0[I(V)+I(W)].                  (12)

No independence between V and W is assumed. These equalities follow directly from physical edges on each face, not an influence budget issued to a child. Therefore whenever BOTH profiles satisfy H(P)<=C0 I(P),

                   H(F)<=max(C0,343/9) I(F).       (13)

This closes EVERY finite acyclic tower of the stated positive-face majority wrappers, with fresh independent shared coordinates at each wrapper, starting from constants/characters (or any already-certified base class of constant C0). Unequal child variable sets can be embedded in a common private cube using irrelevant inputs. Children may share any private inputs and be correlated. An induction in the finite construction order gives the SAME constant max(C0,343/9), without dependence on depth, shared dimension, rarity, or face support cardinality. With constants/characters as base, H<=343 I/9 throughout. The only non-elementary premise is still the supplied threshold theorem.

Equations(11)-(13) do not allocate another Q, reuse a collision donor, or claim a consumed-influence stopping theorem. Outer shared influences and private influences partition the physical influence exactly in(12); recursive private bills are discharged by the inductive child certificate with their actual activation weights. This is precisely why the constant does not add at successive scales. It is separate from the inherited-prefix history statement(10), whose valid-prefix and original-source hypotheses remain unchanged. In this tower class, an unbounded H/I counterfamily is excluded CONDITIONAL ON that supplied threshold theorem; no universal FEI claim follows.

## 7. Universal frontier

This closes a genuine non-point edit with UNBOUNDED support size and an influence-owned original carrier quota. It does not give influence-controlled admission for arbitrary edit geometry or an unbounded number of independent profiles. A general positive event can have large hereditary Fourier l1 norm; arbitrary carriers lack the supplied hereditary H(h_v)<=9I0 certificate. Unrestricted original-source eligibility, profile/terminal FEI and reference conversion remain open. Full FEI is OPEN. NEXT is a positive NONSUBCUBE event with a growing boundary/indicator Fourier norm, keeping the same old source and both terminal/core bills: identify whether its mean-sector disturbance can be paid from genuinely unused original boundary influence instead of one allowance per vertex or profile. Further point or parallel-face depth cases would repeat this completed mechanism.
