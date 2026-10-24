# Matching with reference-only rows and one paid conditional bill

All laws are finite. KL and entropy are in bits. Physical Fourier laws are actual Boolean signs on independent uniform cubes. The graph argument itself applies to arbitrary normalized finite laws and normalized channels; no Boolean quotient is presumed.

## 1. Exact support-complete matching criterion

Let p_e(t,z) be an erased source law and q_e(t,z) a normalized reference dominating it. Apply the same normalized branch channel K_b(t,z) to both, including an explicitly fixed fallback when p_e=0. On the full q_e support put L(t,z)=p_e(t,z)/q_e(t,z), which may equal zero. Write Qjoint(b,t,z)=q_e(t,z)K_b(t,z). Actual physical children are p_b=2p_e K_b, and inherited reference children are QBayes_b=Qjoint_b/Q_B(b). Consequently their likelihood ratio is 2Q_B(b)L(t,z), also at reference-positive/source-zero atoms. For a nonfair abstract channel replace 2Q_B(b) by Q_B(b)/P_B(b) on occupied branches; the matching criterion is unchanged.

For every fixed t, form a graph on ALL z with q_e(t,z)>0. A branch joins every pair of its vertices on which K_b>0. Then actual and inherited child spectator laws agree given t on all source-occupied child rows if and only if L is constant on every graph component.

Proof: On an occupied child row, conditional matching is exactly constancy of the likelihood over the entire reference branch support; the constant is positive, so extra reference-only atoms forbid it. On an unoccupied source child row every such likelihood is zero, already constant. Thus every branch clique is constant if and only if matching holds. Constancy on these cliques is equivalent to constancy on their connected components. A component consisting entirely of reference-only atoms has constant zero and is harmless until connected to actual support. A reference-only vertex with positive fallback in both branches can connect two formerly disjoint actual branch cliques. This extends A047's common-erased-support criterion rather than refuting it.

The reference-only mass G=sum_(p_e=0) q_e is transported to the children: sum_(b,p_e=0) q_e K_b=G. Its distribution between branches depends on the fallback, but it cannot disappear. ReferenceOnlyRows.lean checks g*k0+g*k1=g when k0+k1=1, the implication that two zero transported masses force g=0, and u/(u+g)=1 iff g=0 when u+g!=0. This is the formal scope; the graph and entropy statements are analytic, independently checked in finite domains.

## 2. The exact owned conditional account

Let C_e=E_(p_e(T)) D(p_e(Z|T)||q_e(Z|T)). KL chain rule for the two conditional joint laws on (B,Z) gives

    C_e = E_T D(P(B|T)||Q(B|T))
          + sum_(b,t) P(b,t) D(P(Z|b,t)||Q(Z|b,t)).

This identity includes every reference-only row under the same normalized fallback. Its last term is the physical mean inherited-child conditional KL, C_child. Thus C_child<=C_e, but C_e is an existing liability, not a newly influence-funded credit. The full identity retains queried-label erasure, actual reference outcome prediction and full inherited child KL:

    D(p||q)=E_erasure+D(fair||Q_B)+mean_b D(p_b||QBayes_b).

Neither identity introduces free child credit. A different fallback may move debt between outcome and inherited-child accounts while preserving the complete identity.

## 3. Small actual Boolean illustration

Take f(x0,x1,x2)=(1-2x0x1)(-1)^x2, query x0, retain both residual frequencies as spectator, and use the positive uniform reference on all eight parent masks. All three physical coordinates are essential. Root H=2, I=2; query influence=1/2. Its two terminal cores are characters, with expected influence 3/2 and spectral entropy zero.

The erased source law has two real atoms of mass 1/2, at the two masks containing x2. The reference is uniform on four residual masks; its two reference-only atoms have total mass G=1/2. The actual supported channel is deterministic between the two real atoms. A fair fallback on the reference-only atoms connects both cliques and gives outcome KL zero, mean inherited-child KL exactly one bit. Sending both reference-only atoms to branch zero instead gives outcome KL=1-(1/2)log2(3) and mean child KL=(1/2)log2(3). Total source KL is one bit in either case; queried-label erasure KL is zero. This verifies that dropping the reference-only contribution, or treating a changed fallback as a free invariance of each separate bill, would lose actual reference debt. It is not an FEI counterexample or a universal price obstruction.

## 4. Actual exposed priority query and canonical reference

Use independent bits x,a,b,y and the actual reached A038/A092 gate

    F=(-1)^a if x=0; else (2y-1) if b=1; else +1.

This gate follows the essential shared-data exposure described by A038. Query the actual private b bit (index 2), take spectator frequency Z=S_y and retained T=(S_x,S_a). The query is essential with influence 1/4. Root H=3 and I=3/2. Both retained terminals have H=2; their influences are 1 and 3/2. Hence their certified mean rate-four surplus is mean S4=mean(4I-H)=3 bits. No arbitrary-core FEI assumption supplies it.

Parent spectral masses are 1/4 at {a},{x,a}, and 1/16 at the eight masks using only {x,b,y}. The nonempty source mass is v=15/16 and its conditional marginal vector is r=(8/15,8/15,4/15,4/15). The complete canonical reference matches the empty atom, Q(empty)=1/16, and sets Q(S)=v product_j Bernoulli(c r_j)(S_j)/c on nonempty S. Its positive normalizer satisfies

    1-c=(1-8c/15)^2(1-4c/15)^2.

There is a unique positive solution. Indeed F0(c)=ln(1-c)-sum_j ln(1-r_j c) has F0(0)=0, F0'(0)=sum r_j-1=3/5>0 and F0''(c)<0 for c in [0,1), since sum r_j^2=32/45<1 and r_j/(1-r_j c)<=r_j/(1-c). It tends to minus infinity at one. The intermediate value theorem and strict concavity yield a unique positive root. Direct rational signs put it in (3/4,13/16); a 48-step exact polynomial bracket provides the independent interval certificate. This reference is normalized, and Q_nonempty has conditional marginals r because c=1-product(1-cr). Its log density is affine in S, proving the standard maximum-entropy projection by KL/Pythagorean comparison with all other laws having those marginals. Thus this is the canonical nonempty occupancy reference, not a product surrogate or equal-leaf mixture.

After erasing b, at T with S_a=1 the actual Y frequency is deterministically zero; the row S_y=1 is reference-only. Both actual real rows have branch kernel 1/2. With the fixed fair fallback, the ghost rows also have kernel 1/2. In the reference, conditioning on a present and either x-frequency removes the empty-atom exception; summing b leaves the Bernoulli Y parameter tau=4c/15. Every actual inherited child conditional KL on these rows is -log2(1-tau). Their physical total weight is 1/2.

At S_a=0, the source channel routes Y=0 wholly to b=0 and Y=1 wholly to b=1, so both actual and inherited conditional laws are deterministic and equal. Therefore the COMPLETE mean inherited-child conditional KL is exactly

    C_child=-(1/2)log2(1-4c/15).

No other conditional bill is omitted. Since 3/4<c<13/16,

    (1/2)log2(5/4) < C_child < (1/2)log2(60/47).

The integer inequalities 5^4>2*4^4 and 60^8<8*47^8 prove

    1/8 < C_child < 3/16 = mean S4/16.

The generic interval reconstruction independently bounds C_child and C_e, with C_e<3/8. The conditional splitting identity explains why the larger erased conditional account also contains conditional outcome debt.

## 5. One explicit owner, with the remaining debt stated

Prespecify the actual mean child S4 account as unused before this transaction, and withdraw C_child exactly once. It costs less than one sixteenth of that account and leaves more than fifteen sixteenths. All actual terminal entropy remains: mean H_child+C_child <4 mean I_child-(15/16)mean S4. This is a mean-child allocation, not a claim that each child individually loses at most one sixteenth of its own surplus. No source conditional KL is simultaneously treated as another paid bank, and the old product-reset rho is not charged again.

Complete inherited child reference cross-entropy also includes its retained-quotient KL. That debt, the source occupancy erasure/outcome balance, any conversion to fresh products and subsequent data-query liabilities are NOT paid by the above conditional allocation. FIRST UNSUPPORTED universal line: the remaining signed quotient/reference costs and complete terminal continuation can be funded by genuinely unused source/child surplus under an eligible universal policy, without renewing this spent conditional account. The support criterion and this actual partial payment do not prove FEI or an arbitrary non-flat-core transfer.
