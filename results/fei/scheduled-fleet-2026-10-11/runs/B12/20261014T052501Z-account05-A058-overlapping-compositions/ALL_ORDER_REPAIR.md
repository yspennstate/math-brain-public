# The first private reveal is also paid: arbitrary interleaving

Keep exactly the family and units of SHARED_FIRST_PROOF.md. Any restriction before selector revelation leaves each branch either constant +1 or a point activation of a restricted quadratic, with remaining activation probability p,q in {0,1,2^-l:l>=1}. Thus p,q may now exceed the shared-first limit 1/2. No renewed root-profile or selector mark is assigned.

## Shared queries

The earlier Cauchy-Schwarz calculation still gives P<=(2/ sqrt(1/2))(pd+qe), N<=(1/sqrt(1/2))(pd+qe), since p+q<=2. Therefore |D_shared|<=4sqrt(2)Inf(F)<6Inf(F). The two inherited activated-core erasures cost at most8Inf(F), giving B_shared<14Inf(F). This also covers p=1, where the branch is simply its restricted quadratic, and p=0, where it is constant. After selector revelation the selected branch has the smaller activated-core rate8.

## Private activation-control queries

Suppose a remaining X control is queried. Then p<=1/2 and its true branch influence is j=p(1-m), m=Eu. Only the shared-only common rows collide with the other branch. Their derivative coefficients are a_C=p(uhat(C)-1_{C=empty}); hence their EXACT derivative mass is

    J=sum_C a_C^2=2p^2(1-m)=2pj.

Both conditional-private-mean coefficient vectors have squared norm at most one. The symmetric-shift lower/upper comparisons, homogeneous concavity and monotonicity in the first argument give

    |D_control|<=Phi(1,J)/2.

A restricted quadratic other than constant+1 has Pr[u=-1]>=1/4; a nonzero degree<=2 polynomial has weight at least1/4. Consequently j>=p/2 whenever j>0, while j<=2p. Thus p^2<=J<=4p^2<=1. Using Phi(1,J)<=J log2(e(1+J)/J) yields

    |D_control|/Inf_control(F) <=2p log2(2e/p^2)<5.

Indeed 2p log2(2e)<5/2, and 4p log2(1/p)<=4/(e ln2)<9/4. The latter exact bounds use e>8/3 and ln2>2/3. Zero-influence cases have zero derivative rows. The identical calculation applies to Y.

The activated-core control erasure is exactly Phi((1-j)^2,j^2)+2j(1-j)<=4j by the scalar envelope. Half the inherited core bill is therefore <=4Inf_control(F), and

    B_control(F)<9Inf_control(F).

This avoids the loose selector-only private admission by paying the actual p-suppressed common derivative mass. It uses the unactivated quadratic minority gap; it is not a universal real-derivative entropy theorem. After selector revelation the selected core has the smaller rate4 at controls.

## Selector query

Let delta=Inf_z(F). Put a_G=p Pr[u=-1], a_H=q Pr[v=-1]. If each genuinely active branch has remaining probability <=1/2, then delta=a_G+a_H-2pq Pr[u=v=-1]>=max(a_G,a_H)>=(a_G+a_H)/2. The quadratic minority gap gives delta>=(p+q)/8 after dropping constant+1 branches and zero probabilities. The common mean vectors g,h satisfy ||g-h||_2<=2(p+q). Their selector erasure is bounded by

    B_common<=sum_C |g_C^2-h_C^2|/2
               <=||g-h||_2 ||g+h||_2/2<=16delta,

since ||g||_2,||h||_2<=1. Exclusive private frequencies contribute exactly

    B_out=p(1-p)(1-Eu)+q(1-q)(1-Ev)<=4delta.

For completeness delta>=p(1-p)Pr[u=-1] and the corresponding q bound hold pointwise after conditioning on S: on u=-1 the mismatch is p or p+q-2pq, each at least p(1-p). This proves the displayed B_out bound even outside the rare case. Thus B_z<=20delta in the rare case.

If one active probability is1 and the other <=1/2, mismatch on the resolved phase's negative set and the other inactive controls gives delta>=1/8, so B_z<=1<=8delta. A resolved constant+1 branch is dropped; a constant-1 branch has at least the same bound. If both probabilities are1, the output phases are quadratics on S. Either they are identical, giving B_z=delta=0, or their product has a nonzero degree<=2 polynomial and delta>=1/4, giving B_z<=4delta. Constant/failed branches and zero endpoints follow by the same reductions. Hence B_z<=20Inf_z at every reached pre-selector state.

## One physical ledger for every adaptive tree

Every finite adaptive fresh-coordinate tree, including arbitrary controller/shared interleaving and selector timing, now obeys

    B_tree <=14 P_shared+9 P_controls+20 P_selector,
    H(root)<=E H(actual leaf)
          +(14+2/ln2)P_shared+(9+2/ln2)P_controls
                            +(20+2/ln2)P_selector.

Coordinate-wise influence conservation assigns these resources once. Before selector revelation the exact leaf entropy is the half-sum of both actual core entropies plus their coherent R. After revelation it is the actual selected-core entropy. It is never deleted or replaced by a fresh root allowance. Complete constant-leaf trees give B_tree<=20I and H<23I. The shared-first class entropy estimate H<16I remains stronger; the new gain is arbitrary interleaving with all stopped terminals.

All quadratic gap claims above follow by the elementary weight induction: a nonzero degree-d polynomial has weight>=2^-d, since a nonzero relevant derivative has degree<=d-1 and exactly one endpoint is one whenever that derivative is one. No independence between shared phases is used.

The new first unsupported line is replacing the unactivated quadratic minority/derivative gaps by an unused certified terminal-child surplus for arbitrary phases. Common derivative mass J=2pj remains exact for arbitrary activation cores, but J>=p^2 need not hold: an arbitrarily rare negative phase can destroy this price. A selector-only renewed mark is not assumed to pay that logarithmic excess. This is the next universal ownership gap; the first private reveal for independently activated quadratics is now closed.
