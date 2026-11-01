# A095 independent reconstruction

Target: A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1. The only queries are previously unqueried wide-block coordinates. Information uses bits. The prescribed source is P_(h_w h_2); no source replacement, reset, or terminal renewal is admitted.

The signed tensor calculation can be reconstructed directly. For h_w, the signed coefficient sum is -1 and the signed log-profile is -2b log2 b -(2-q)(2w-2), where q=2^(1-w), b=1-q. The width-two factor has signed sum -1 and constant log-profile 2. Multiplication gives A=2+2b log2 b+(2-q)(2w-2). Summing unsigned log-profiles gives B=-8log2 b+2^(w+3)w-8w+8. At the edited vertex g(0)=1, so all old coefficients shift by -delta and new coefficients have magnitude delta; this keeps every signed cross term.

Every queried wide edge on the edited path was pivotal in g. At that node, the selector-one edit destroys that edge and reduces its conditional influence by delta_node. Physical reach times delta_node equals the original delta. Thus the total debit changes by exactly t delta, where t is the number of wide queries on that one path. This proves the stated influence identity independently of spectral calculations.

The no-reset reference transport is reconstructed from conditional cross entropy: CE_parent=CE(p,r)+B+L, while mean CE_child=CE(p,r)-JS+mean log2 Z. Therefore release=B+JS+L-mean log2 Z>=0. Here L is a true conditional KL, Z0+Z1=2, Zb>0 follows from Q positive on true parent support and P_b having total mass one. No reference mass on p=0 is discarded; the prescribed fallback is retained.

## Normalization and finite success

Let k=w+2, n=k+m, N=2^k, delta=2^-n. There are N old atoms and 2^(n+1)-N new atoms. The new reference mass is exactly delta^2(2^(n+1)-N)=W=2delta-Ndelta^2, so the old part (1-W)P_g makes Q a probability law. Since w>=4, all old source coefficients are nonzero and 0<W<1. Thus Q covers the actual spectrum, every relevant logarithm is finite, and no witness/atom is counted twice. The construction is a supplied probability reference rather than an unproved sampler or uniquely decodable code. Each atom is indexed by its literal physical Fourier mask. Finite history depth is at most w; no limit or optional-stopping assertion is needed.

## All-width root estimate

Put q=2^(1-w), b=1-q. The source entropy is c=2-b^2 log2(b^2)+(2q-q^2)(2w-2). The old true mass totals 1-W (Parseval, or summing (a_T-delta)^2 using sum a_T=g(0)=1). Therefore the complete root cost is exactly

    c-2delta A+delta^2 B -(1-W)log2(1-W)+2nW.

The positive atanh series gives ln2>2/3; integration gives -ln(1-x)<=x/(1-x). These imply

    c < 2+(4w-1)q-(2w-2)q^2 <=121/32,
    A >=4w-2-(2w+1)q,       B/N<=2w.

For the first bound, w=4 evaluates to121/32, while for w>=5 the decreasing term (4w-1)2^(1-w) is at most19/16. The B bound follows from B/N=2w+8(1-w-log2 b)/N and -log2 b<(3/2)q/b<=3/14<w-1. Thus all signs used in multiplying by delta are legitimate. Applying W<=2delta and -(1-W)log2(1-W)<3W/2 gives

    CE_root < c+delta[4m-2w+15+(4w+2)q]
            <=c+delta(4m+37/4).

Here (4w+2)q<=9/4, since its ratio at the next width is (4w+6)/(8w+4)<=1. The integer inequality16m+37<=37*2^m follows by induction: its successor step follows from16<=16m+37. Hence delta(4m+37/4)<=37/256 and CE_root<1005/256. This is an all-parameter argument; finite cases are not its proof.

## Every adaptive policy and the final expectation

Write Pi_g for the reached sum of original wide-coordinate query influences. On the edited all-zero path, let t be the number of queries. The untouched narrow block contributes exactly1 to original remaining influence. The earlier literal edited-edge count gives

    E I(M_leaf)=1+wq-Pi_g+delta(m-w-1+t).

The all-zero-path leaf has reach2^-t. Every one of its w-t unqueried wide coordinates has conditional original influence2^t q. All other leaves have nonnegative influence. Consequently wq-Pi_g >=(w-t)q, and

    E I(M_leaf)>=1+delta[m-1+(w-t)(q/delta-1)]
                  >=1-delta>=63/64.

The division is safe because delta>0, and q/delta=2^(m+3)>1. Adaptivity changes the order and t, but does not duplicate the all-zero path or change its physical reach. Summing the nonnegative complete CE releases over the finite tree yields E CE_leaf<=CE_root. Therefore

    4 E I_leaf-E CE_leaf>4*(63/64)-1005/256=3/256.

Every terminal is retained as H(P_leaf)+D(P_leaf||Q_leaf). Only the actual reached mean is bounded; no bound for every individual leaf is asserted. There is one original bank, no renewed ancestor budget, and every erased edge remains in the physical identity.

## Untouched terminals and the zero-fiber boundary

For an independent terminal h and its reference R_h, use the core posterior pi_b(T) on the entire terminal fiber, including labels with P_h=0. Then raw child references factor as(2r_core pi_b)R_h, both Z_b equal their core values, and normalized references remain Q_core,b times R_h. Complete CE and KL add. The terminal's entire prescribed cost is outside the core payment. If its reference fails to cover true support, use the extended-value additive identity; do not cancel infinities or infer a finite terminal budget.

The product-compatible extension is essential. Take a constant terminal with P_h=(1,0), R_h=(1/3,2/3). At a core fiber with pi_0!=1/2, globally applying the fair fallback on the zero terminal label changes the terminal/core likelihood ratio and destroys the product. This does not refute A095, whose product-compatible condition is explicit. The verifier records literal rational witnesses.

## Independent checks and disposition

The final independent helper imports no author checker. It uses direct character sums, literal cube edges, rational normalized posterior transport and 18-term atanh log enclosures, rounded outward to96 fractional binary bits. All2,373 checks PASS on(w,m)=(4,0),(4,1),(5,0), including all405 labelled partial wide assignments, every possible next physical wide query, dynamic minima over ALL adaptive stopping trees, and three complete reference policies per root. The final run takes1.240 seconds internally. The original552-check pilot precedes the final verifier changes and is not added to this total. An intervening output-serialization failure is preserved as a noncertificate.

Verdict: HOLDS at the full named A095@1 scope, without substantive repair. Rung: independently reconstructed analytic proof with exact finite checks; any separately checked Lean arithmetic lemma does not certify the entropy theorem. The first unsupported universal line is influence-priced construction of an arbitrary incoming complete reference, or payment for a specified fresh descendant reset from the SAME unused ancestor capacity with its complementary full terminal. Querying the untouched width-two block is also outside this theorem. Full FEI remains OPEN.
