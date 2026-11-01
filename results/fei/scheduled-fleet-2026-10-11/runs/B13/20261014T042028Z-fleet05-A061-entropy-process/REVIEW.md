# Independent audit of A064's repeated physical fallback

Source A064-REPEATED-FALLBACK-PRIORITY-GLOBAL-DEBT@1, run 20261014T030103Z. This stage reviews that new local controller clause and its assembly into the ordered-priority potential. The data lift and shared-X clauses retain their exact previously reviewed dependency scopes. No source repair or new broad candidate is intended.

Write phi(z)=z log2(1/z), Phi(x,y)=phi(x)+phi(y)-phi(x+y). At the actual point-control query, let p be live point probability, u the override core, G the identical physical fallback on both children, y=Eu, x=EG, g its data-averaged controller profile, W the selected fallback-core variance sum, and Vg=Var(g). Independence of u from G gives d=p(1-xy). It does not imply independence between G's two occurrences.

## Reconstruction by physical sectors

For u-data rows the erasure equals p Var(u), exactly the released u rarity reserve. For fallback nonempty-data rows the multiplier (1-A) has erasure c(p)=p-2p^2+Phi((1-p)^2,p^2). Their rarity release has multiplier k(p)=phi(1-p)-phi(1-2p)/2>=0. The remaining controller-profile rows have erasure

    Bprofile=(p-2p^2)E(g-y)^2
       +sum_T Phi((ghat(T)-p*(ghat(T)-y*1[T=empty]))^2,
                   p^2*(ghat(T)-y*1[T=empty])^2).

Thus B-kappa=Bprofile+(c-k)W. This derivation uses Parseval for each actual fallback selector, not copies of fallback children. Constants have zero core variance. All zero cases follow by continuity.

Phi(a^2,b^2)<=2|ab| follows from homogeneity and monotonicity of the binary ratio at amplitude ratio z in [0,1]: the derivative numerator (z^2-1)ln(1+z^2)-z^2 ln(z^2)>=0. Also c<=2p from b(p)=2p(1-p)+Phi((1-p)^2,p^2)<=3p. For p<=1/4, its divided upper envelope 2(1-p)+p(2log2(1/p)+1/ln2) is increasing, with endpoint 5/2+1/(4ln2)<3; for 1/4<=p<=1/2, use the amplitude inequality. These cover every live point width.

Discard k only for an upper bound. Triangle inequality on the profile sum gives

    B-kappa <= p[3Vg+2W+(x-y)^2+2|x(x-y)|]
             <= p[3(1-x^2)+(x-y)^2+2|x(x-y)|].

After simultaneous sign reversal take x>=0. For y<=x the bracket is 3+y^2-4xy<=4(1-xy). For y>=x it is 3-4x^2+y^2<=4(1-x^2)<=8(1-xy). The zero-influence endpoint vanishes identically. Therefore B-kappa<=8d; physical JS<=2d/ln2 yields D-kappa<=(8+2/ln2)d<11d. The strict guard is ln2>2/3 from its positive atanh series. No lower bound on D-kappa is claimed.

## Interleaved global assembly and boundaries

Let Q=sum q_j r_j+sum phi(q_j)Var(u_j), where each nonnegative r_j has the declared C-priced own-history drift. At a controller query the inherited first sum has zero expected drift: q_j is a physical martingale and no core history changes. The reviewed local bound therefore pays the control query at 11. At a data query the additional A064-v2 lift gives rate C+11/2, with the same Q. Initial rarity ownership gives Q0<=sum q_j r_j(root)+2I_ctrl. These two imported facts are conditioned on their published disjoint-core and own-history hypotheses, not replaced by a universal assumption.

Finite Bellman induction with actual full-completion leaf reserve zero yields least reserve<=Q, because Q is nonnegative at every reached node. At a finite stop retain H_leaf-Q_leaf. At controller resolution it is H(selected core)-r_selected; at complete data it is the actual controller entropy; only full data-and-control completion has H=Q=0. The stopped bound and optional root certificate reproduce source rate max(C+11/2+K,13); the 2I_ctrl root funding and rate11 control debit add. No paid root capacity is replenished after a query. Expected Q_terminal<=Q0+C Pi_data follows separately from core entropy decrements>=0 and variance-rarity decrease.

Shared-X extension is conditional on the reviewed A087 one-sided/disjoint-child geometries, after which the priority local clause applies. This does not assert an all-controller or shared-data representation.

## Verification scope and unpaid line

The independent checker builds actual truth tables from control labels, derives every physical child spectrum and influence, and compares the erasure formula, rarity release and residual. Separate complete trees expose one core bit between the two private A bits and keep every physical branch, with C=0 (nonzero inherited H reserves) and C=4 (zero reserves for these named cores). Nonconstant stopped boundaries remain explicit. The all-dimensional local proof above supplies quantifiers; finite checks alone do not.

First unsupported universal line: pay arbitrary inherited core reserves and one overlapping non-point controller residual from unused physical influence while retaining both child and terminal functions. Verdict is scoped independent acceptance of the new local controller derivation and global assembly conditional on the exact additional-v2 data lift and shared-X dependency. Older bundled v1 claims are not reaccepted. A universal FEI bound remains open.
