# Interleaved shadow ownership and a locally unpayable unlocking debit

Bits; normalized Fourier transform on actual uniform physical cubes. B_z(f)=H(S_z|S_without_z). The shadow variable z is auxiliary and is never mistaken for a queried physical encoder bit.

## 1. Exact interleaved variance account

Start with any Boolean shadow f(z,r)=A(r)+zD(r) and any Boolean encoder h(x) on disjoint support. Query any adaptive actual physical prefix, using only its remaining encoder or data coordinates. At a reached node v, f_v and h_v are their actual restrictions; mu_v=E h_v, V_v=Var(h_v)B_z(f_v). Reach weights are fair physical weights w_v.

At an encoder query i, the two means are mu_v +/- gamma_v, gamma_v=hat h_v({i}), so the average variance decreases by gamma_v^2. The shadow is unchanged. At a data query j the encoder is unchanged, while the shadow has its two actual uniform j slices. Define

 Q=sum_(encoder nodes) w_v gamma_v^2 B_z(f_v),
 R=sum_(data nodes) w_v Var(h_v)[B_z(f_v)-(B_z(f_(v,+))+B_z(f_(v,-)))/2].

Then EXACTLY

    Q+R=V_root-E V_leaf.                         (1)

This is the extension of A026's encoder-only identity. R is signed; it cannot be silently omitted or declared nonnegative. If the encoder is resolved, its variance is zero. If all data inputs are resolved, the shadow is a sign on at most z, so its spectrum is a point mass and B_z=0. Otherwise V_leaf remains explicit. Querying irrelevant coordinates also obeys the identity with zero physical influence; no relevance convention changes its algebra.

Actual query influences are

 alpha_encoder=delta_v Inf_i(h_v), delta_v=Inf_z(f_v),
 alpha_data=q_v Inf_j(f_v|z=+1)+(1-q_v)Inf_j(f_v|z=-1), q_v=(1+mu_v)/2. (2)

The latter is generally not the uniform-shadow influence. The proof is direct physical pivotal conditioning on the actual output of h_v. Thus the account does not substitute auxiliary uniform reach weights for physical ones.

## 2. Terminal-inclusive insertion into A026's transfer

Consume A026-SIGNED-ROW-UNIFORM-SHADOW-TRANSFER v1, independently reconstructed at scalar/interface scope in REVIEW.md: at encoder nodes,

 B_query<=delta_v B_i(h_v)+gamma_v^2 B_z(f_v)+C0 alpha_query,
 C0=log2(32/27)+2/(e ln2).

Let E_inner=sum_encoder w delta_v B_i(h_v), E_data=sum_data w B_j(F_v), and S_encoder,S_data denote physical spent influences. Set a=2/ln2. Physical entropy and influence telescopes, with no leaves dropped, give

 H(F_root)<=E H(F_leaf)+E_inner+E_data+V_root-E V_leaf-R
                   +(C0+a)S_encoder+a S_data.      (3)

This is a conditional interface, not a universal bound. It identifies the exact new bill -R when data queries unlock a shadow collision. All data erasure and actual terminal entropy remain. For once-sliced majority nodes E_inner is paid by the previously independently accepted B_i(h)<=2Inf_i(h), but that does not pay -R or E_data.

## 3. Actual Boolean unlocking witness (consume A096's family)

For even k>=4, b(y)=(-1)^(y1*y2+...+y_(k-1)*y_k), with y coordinates in {0,1}, b(0)=1. Define g(s,y)=b(y)-1_(y=0)+s 1_(y=0), and delta=2^-k. Then Inf_s(g)=delta. Its s-pair Fourier coefficients are (epsilon sqrt(delta)-delta,delta), epsilon in {-1,1}. The explicit bent spectrum follows by tensoring the two-input quadratic sign.

Write B*=B_s(g). Every packet satisfies Phi((epsilon sqrt(delta)-delta)^2,delta^2)>=delta^2 log2((sqrt(delta)-delta)^2/delta^2)>=delta^2(k-1). Thus B*>=delta(k-1). This is the same source family as A096 stage4; its new use below is a shadow-account translation, not a claim that the witness is newly invented.

Set f(z,u,y)=g(zu,y), and encode z by fresh Maj3 h, so F(x,u,y)=g(h(x)u,y). The parity character embedding makes B_z(f)=0: nonzero coefficients have either neither or both z,u. Its uniform shadow erasure is zero, but querying physical u reveals shadows g(+z,y) and g(-z,y), each with B_z=B*. Hence the first data query has

 V_root=0, Var(h)=1, R=-B*, alpha_u=delta.

Now resolve only the three encoder inputs in any complete adaptive encoder policy, leaving the y core untouched. Every branch has the same B_z=B*. Formula (1) gives Q=B*, E V_leaf=0. The exact spent encoder influence is delta I(Maj3)=3delta/2; the unlocking data bit spent delta. Therefore for EVERY such complete encoder policy

    Q/(S_encoder+S_unlock)=B*/((5/2)delta)>=2(k-1)/5 ->infinity. (4)

Also -R/alpha_u>=k-1. No dimension-independent price pays the signed unlocking debit at each data node from that node's physical influence; even adding the entire downstream encoder account remains insufficient. This strictly adds the unlocking bit to A026's excluded encoder-only budget. The omitted y core budget is essential, and is not asserted inadequate.

The actual terminals are g(+1,y)=b(y) and g(-1,y)=b(y)-2 1_0, each reached with probability 1/2 because h*u is balanced. Hence exact retained terminal entropy is [k+H(b-2 1_0)]/2, not zero. Root H is H(g)+delta H(Maj3)=H(g)+2delta by balanced composition; direct edge counting gives I(g)=k/2+(k+1)delta and total influence I(F)=I(g)+(3/2)delta=k/2+(k+5/2)delta. Each data influence is 1/2+delta: flipping the origin adds exactly one disagreement edge in each data direction to the bent child, whose influence is 1/2+2delta; average it with the unmodified child. A096 DERIVATION section 4 separately gives I(G)=k/2+(k+2)delta for the parity-duplicated function G; that is our auxiliary shadow f, rather than g or the majority-encoded physical F. Its formula is consistent with these direct counts. Since H(g)<=k+1, H(F)<=k+1+2delta and H(F)/I(F)<3 for k>=4. This is a reserve/ownership no-go on a bounded-ratio Boolean family, not an FEI disproof. Our k=2 finite control is not used in the k>=4 lower bound.

## 4. One exclusive terminal reserve pays the witness bank

The unlocking physical query itself has B_u(F)=0: its inactive coefficients lie on the empty encoder support and its active coefficients on nonempty supports, so no adjacent occupied spectral pair exists. After it, cumulative inherited encoder erasure is E_inner=delta for every Maj3 query order: the first majority query has erasure zero, its two two-input slices each have erasure one on the next query, and the final constant/dictator slices have erasure zero. The terminal laws from section 3 have averaged influence k/2+k delta. Define their ACTUAL K=2 terminal surplus

 S2=E[2I(F_leaf)-H(F_leaf)]
    =k+2k delta-[k+H(b-2 1_0)]/2 >=2k delta,

since the defect child is a law on 2^k atoms and hence H<=k. The exact shadow bill Q=B*<=h2(delta)<=delta[k+log2(e)]. For even k>=4, log2(e)<2 gives

    Q+E_inner<=delta[k+log2(e)+1]<2k delta<=S2.     (5)

Thus this unbounded local bill IS paid by one explicit terminal-core surplus, assigned once, leaving S2-Q-E_inner nonnegative. Substituting (5) in (3) gives H(F)<=2E I(F_leaf)+(C0+a)S_encoder+a S_unlock; the coefficient max(2,C0+a) is a safe conditional-transfer bound on this witness. The elementary H/I<3 bound was already stronger; the advance here is exclusive terminal ownership, not a new sharp class FEI result.

This does not prove terminal children on an arbitrary seed have a comparable positive surplus; child-certification alone gives nonnegativity, not the amount in (5). This is exactly the next universal requirement.

## 5. Consequence for the minimal target

A shadow reserve that assumes R>=0, or funds max(0,-R) locally from the unlocking bit plus its encoder, is false. Summing only favorable data drops changes the account. The smallest still-live common-budget lemma is a bound, under an actually selected physical policy, on E_inner+E_data-R+E[H(F_leaf)-V_leaf], with the initial V_root charged ONCE to a source-owned core reserve. No arbitrary seed theorem supplying that reserve is proved. This is an identified unpaid obligation rather than an equivalent target advertised as a solution.

The next mathematical action is to derive a conditional remainder owned by actual certified core-child slack at the first unlocking data query, retaining its complete terminal law and the signed R. This interfaces directly with A096's full conditional KL requirement. Uniform variance or the queried/erased pair alone cannot own the original core bill.
