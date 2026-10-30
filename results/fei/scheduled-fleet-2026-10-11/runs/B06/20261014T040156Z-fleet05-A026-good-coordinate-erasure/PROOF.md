# Exclusive data-edge reserve for an interleaved Boolean shadow

All entropy is in bits, all functions are Boolean signs on finite independent uniform physical cubes. Let f(z,r)=A(r)+zD(r), with actual branches g_+=A+D,g_-=A-D, and let F(x,r)=A(r)+h(x)D(r) for any disjoint Boolean encoder h. Write delta=I_z(f), mu=E h, q=(1+mu)/2, v=Var(h)=4q(1-q), and p=g_+g_- on the actual data cube. Define

 W(f,h)=v I(p).

This potential is nonnegative. It is a replacement for the signed B_z potential, not a statement that data queries decrease B_z.

## 1. Universal support-entropy bound, with no FEI assumption

Let E(r)=1{g_+(r)!=g_-(r)}. Its probability is delta, and p=1-2E. Concavity of homogeneous binary entropy gives B_z(f)<=h2(delta). We next prove

 h2(delta)=H(E)<=sum_j H(E|r_without_j)=I(p).                 (1)

Indeed, since E is a deterministic function of independent physical signs, chain rule gives H(E)=sum_j I(E;r_j|r_before_j). Adding the independent future signs cannot decrease this mutual information:

 I(E;r_j|past)<=I(E,future;r_j|past)=I(E;r_j|all other signs).

The last quantity equals H(E|all other signs), because E is fixed by the full cube. At fixed other coordinates, E is either constant or a fair binary bit. Its conditional entropy is therefore exactly the pivotal probability of p in direction j. This proves (1). No unnormalized derivative spectrum is assumed Boolean. In particular

 **B_z(f)<=h2(delta)<=I(g_+g_-)<=I(g_+)+I(g_-).**             (2)

The last inequality is pointwise: the product flips exactly when precisely one branch flips. All constants in (1)-(2) are attained by an AND2 shadow at its distinguished coordinate (one branch constant, the other a dictator).

## 2. Physical ownership and sharp bias-dependent price

For each actual data edge j, let a_j be the probability that g_+ flips and g_- does not, and b_j the converse. Put A_ex=sum a_j, B_ex=sum b_j. These are exclusive pivotal probabilities, not separate independent coordinate influences. Then

 I(p)=A_ex+B_ex,
 X(f,h)=q A_ex+(1-q)B_ex <=sum_j I_j(F)=I_data(F).            (3)

The quantity X is the physical influence carried by edges pivotal in exactly one of the two branches. Product support and actual encoder output give the weights q and 1-q. For every q in [0,1],

 W=4q(1-q)(A_ex+B_ex)<=c(q) X,
 c(q)=4max(q,1-q)=2(1+|mu|)<=4.                             (4)

The endpoints have W=0. For every interior dyadic q the coefficient c(q) is sharp: choose an AND2 shadow oriented so its only nonconstant branch is the less likely encoder output. Then I(p)=B_z(f)=1 and X=min(q,1-q). Resolve the encoder completely before any data query; the total shadow bank equals W. Balanced encoders have the sharp coefficient 2; the supremum over all Boolean encoder biases is 4. Thus W is owned by actual exclusive data influence, not by auxiliary uniform shadow influence or already-spent encoder influence.

## 3. A conserved nonnegative reserve under arbitrary interleaving

Use one fixed encoder/data partition, allowing any adaptive physical query order, stopping time, and actual history. At every node restrict f and h to their actual remaining physical inputs. Reach weights are the true fair physical weights. An encoder query i has singleton gamma=hat h({i}); the actual influence is delta I_i(h). The outer p is unchanged and variance drops in expectation by gamma^2. Therefore its W decrement is gamma^2 I(p). The desired shadow charge is gamma^2 B_z(f), no larger by (2).

A data query j leaves h unchanged. Its two product functions are exactly p restricted to r_j=+/-1. The established physical influence telescope gives I(p)-avg I(p_child)=I_j(p), hence the W decrement is v I_j(p)>=0. This is why W survives the signed unlocking that defeated v B_z(f).

Define, over encoder nodes,

 Q=sum w gamma^2 B_z(f),
 G=sum w gamma^2[I(p)-B_z(f)]>=0,

and, over data nodes, L=sum w v I_j(p)>=0. Then the exact reserve identity is

 **Q+G+L+E W_leaf=W_root.**                                 (5)

Every term is nonnegative. Consequently Q<=W_root-E W_leaf-L<=W_root. Root capacity is charged once; data exposure cannot refill it for free. The terminal reserve W_leaf remains explicit.

The physical exclusive account also has an exact conservation law. At an encoder query, q is a martingale and A_ex,B_ex stay fixed, so X has zero expected drop. At a data query j, A_ex and B_ex obey labelled-edge influence conservation, with drops a_j,b_j respectively. Thus, with e_j=q a_j+(1-q)b_j,

 **sum_data w e_j+E X_leaf=X_root.**                        (6)

Since e_j<=I_j(F), (4)-(6) price the complete shadow bank from one subset of the actual data budget, including any unspent terminal portion. This does not permit spending the same portion again to pay data erasure or terminal entropy.

## 4. Insertion into the actual entropy ledger

Consume A026's stage4 signed-row transfer with C0=log2(32/27)+2/(e ln2), and put a=2/ln2. Let E_inner=sum_encoder w delta B_i(h), E_data=sum_data w B_j(F), and S_enc,S_data the actual spent influences. The exact entropy decrement B+JS and JS price give

 H(F_root)<=E H(F_leaf)+E_inner+E_data+Q+(C0+a)S_enc+a S_data.

Using (5) yields the new terminal-inclusive bound

 **H(root)<=E H(leaf)+E_inner+E_data+W_root-E W_leaf-G-L
                              +(C0+a)S_enc+a S_data.**      (7)

All credits and all terminal entropy are retained. Q is now paid by an explicit source-owned nonnegative reserve even when A003's signed data transfer R is negative. This is not a complete FEI proof: E_inner,E_data and the physical terminal entropy must share the remaining budget with W.

For example, if a particular tree has separately proved E_inner<=K_h S_enc, E_data<=K_d S_data, and H(leaf)<=K_t I(leaf) at every actual leaf, then (4),(6),e_j<=I_j(F),X_leaf<=I(leaf) give the conditional constant

 H(root)<=max{K_h+C0+a, K_d+a+c(q_root), K_t+c(q_root)} I(root). (8)

The c(q_root) is assigned once to the exclusive data account. It is additional headroom, not an inference from merely nonnegative child surplus. The hypotheses in (8) are not assumed universally or restriction closed. Repeatedly allocating this same reserve in changing encoder representations has no proved global bound.

## 5. Exact boundary controls and relation to the previous obstruction

For AND2 outer f, oriented with the active branch probability t=min(q,1-q), I(p)=B_z=1, X=t, W=4t(1-t). A complete encoder-only tree has Q=W. Thus Q/X=4(1-t), proving sharpness of (4) for every realizable interior dyadic bias, including 2 at balance and a limit of 4 as t->0. Actual terminal core entropy is zero (constant/dictator spectra), but its influence X is not zero.

For A003's unlocking family f(z,u,y)=g(zu,y), with quadratic bent g branches differing at y=0, delta=2^-k, the initial B_z(f)=0 but p=g(+u,y)g(-u,y)=1-2 1{y=0}. Thus I(p)=2k delta and W_root=2k delta for balanced Maj3. Querying u unlocks B_z but I_u(p)=0, so L at that query is zero and the initial positive capacity is unchanged. Resolving the encoder then spends Q=B_z(g), with the nonnegative gap 2k delta-B_z(g) retained. This precisely identifies the outer-data capacity absent from the old encoder-only and unlocking-plus-encoder no-gos. Their mathematical statements remain true; no FEI counterexample is produced or repaired.

## 6. Exact first unsupported line and NEXT

The missing universal step is selecting data queries and inherited/terminal certificates so the exclusive account used for W is not also spent in E_data or H(leaf), across a complete policy and any changes of encoder representation. In (8), merely certifying the leaves at K does not provide the extra c(q_root) headroom. Root rate 2 (balanced) or <=4 (arbitrary bias) for the isolated shadow bank is proved; a dimension-independent rate for the entire erasure/terminal ledger is not. NEXT is to subtract the owned exclusive portion from actual certified data-child surplus at the first nontrivial outer-data query, or give a source-bound obstruction to that same-price subtraction. Further encoder slices or root-family bounds do not address this remaining common-budget problem.
