# Conditional entropy is not conditional reference-reset credit

Uniform physical bits, Boolean signs, base-two entropy/KL, actual fresh queries and actual leaf spectra throughout.

## 1. Independent reconstruction of A050 v1

Assume a controller-only tree has actual spectral laws p_v(c,u,z)=pbar_v(c,u)k(z|u), with the same normalized k at every reached node, and references q_v=qbar_v k. Normalization follows by summing k. KL chain rule immediately gives D(p_v||q_v)=D(pbar_v||qbar_v), while CE(p_v,q_v)=CE(pbar_v,qbar_v)+L_v, L_v=E H(k(.|U)). This latter term is retained, not free.

At a controller query the erased spectral row is p_e(T,z)=pbar_e(T)k(z|u), and the actual coherent branch kernel is p_child_b(T,z)/(2p_e(T,z)). The k factor cancels on positive rows, so the kernel depends only on T. Source-zero rows require a normalized fallback independent of z, including reference-only rows; that hypothesis is necessary to justify the normalization argument there. Applying the same kernel to q_e gives the same branch predictions as quotient transport and Bayes children with the same k. Every source, child, conditional-erasure, outcome and signed reference-reset KL then agrees with its quotient counterpart. No fresh projection is called an inherited reference.

For source/reference laws p,q, erasure gives E=D(p||q)-D(p_e||q_e). Embed the same kernel as (T,b), retaining T. This preserves erased KL exactly. Splitting by physical b gives D(p_e||q_e)=O+average D(p_b||q_Bayes_b), because physical b is fair and reference predictions are those actually produced by transport. Hence, for chosen normalized references q'_b, with rho=average[D(p_b||q'_b)-D(p_b||q_Bayes_b)],

    D(p||q)=E+O+average D(p_b||q'_b)-rho.

It telescopes without losing the sign of rho. The controller marginal restriction identity makes L a physical martingale, giving L_root=E L_leaf, and controller M,J and physical influence equal their quotient quantities. The quotient need not be a Boolean spectrum: a separate quotient certificate is required for any price transfer. Common independent Boolean factors satisfy the scope only if every arm AND fallback contain that same factor. A certified factor terminal bill is charged once.

At any query outside spectator Z, set T to the remaining quotient labels. Direct entropy decomposition gives

    DeltaL = H(S_Z|S_i,T)-average_b H(S_Z|T,b)
           = I(b;S_Z|T)-I(S_i;S_Z|T).

The first term is the coherent physical branch information conditional on T; the second is root-spectral frequency information. Both are nonnegative. Thus [DeltaL]_+<=J_full<=2 Inf_i/ln2 by the scalar fair-channel inequality and Parseval. This statement concerns entropy, not arbitrary reference KL.

If p/q=r(T)>0 over the whole reference support, erase i and apply the same K: p_e=r q_e, and p_b/q_Bayes_b=2q_b r(T). This ratio is independent of Z. Hence actual and inherited child references have the same conditional spectator law, and there is no extra conditional KL. The likelihood condition is sufficient, not necessary in every channel. Any chosen child reference matching its actual conditional law has the same full and quotient reset. The actual h2(C)*h3(U,Z) examples in out/MATCHED_* verify this nontrivially for physical U queries with flat and nonflat positive controller references. The additional out/CONTROLLER_* examples use conditional-kernel lifts of chosen quotient references; their entropy drift and extra conditional reset both vanish exactly.

This reconstructs all clauses of A050-COMMON-CONDITIONAL-KERNEL-REPAIR@1 without a substantive repair. ACCEPT unchanged at scope. The arbitrary nonmatching reference/core bill remains open, exactly as the source says.

## 2. Specify the nonmatching quantity before testing it

For one physical query i, let Q be the product of actual parent spectral marginals. Erase i in P and Q, apply the SAME actual branch kernel to both, and normalize its reference children Q_B,b. On source-zero residual rows the frozen fallback is fair. Let P_b be the actual child spectra. Let Q'_b be the product of actual child spectral marginals. Fix spectator labels Z and retained quotient T, with i erased.

Define C_Z(P,Q)=D(P||Q)-D(P_T||Q_T), the conditional KL discarded by quotienting. The extra signed conditional reference reset is

    rho_cond = average_b [C_Z(P_b,Q'_b)-C_Z(P_b,Q_B,b)].

It is exactly full signed reset minus the quotient signed reset using the MARGINALS OF THE SAME transported full references. In a nonmatching case those marginals must not be silently substituted with a separately transported quotient kernel. The inherited laws, fresh laws and their quotient marginals are all independently normalized in the checker. This is a definite conditional bill, rather than an informal KL label.

The exploratory false extension tested by this run is

    [rho_cond]_+ <= K [DeltaL]_+

for any universal finite K on every actual Boolean query with the above product-reference convention. It is not asserted by A050 or any named accepted claim. It would wrongly use the already paid positive spectator entropy drift as sole credit for a nonmatching conditional reset.

## 3. Original four-bit Boolean certificate

Take independent fair bits x,a,b,y. Let v(y)=2y-1 and

    F(x,a,b,y)=(-1)^a when x=0;
              v(y) when x=1,b=1;
              +1 when x=1,b=0.

This is the actual A038 opposite-priority gate after an essential u-data exposure: choose u=(-1,-1,-1,+1), expose its first data bit at 0, so u becomes -1. Its other bit is a genuine irrelevant remaining coordinate; suppressing that dummy removes only a deterministic zero Fourier frequency. The ancestor exposure influence is 1/8. Our original effective truth table, indexed by x+2a+4b+8y, is

    (1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,1).

Query a and take Z={y}; retained quotient frequencies are x,b. Every nonzero residual spectral row is positive, so the certificate does not depend on a zero-row fallback. The query is essential with influence 1/2. Direct physical edges give I(F)=3/2 and average terminal influence 1. The two children remain actual nonconstant functions.

Direct character summation gives parent masses 1/4 at masks {a} and {x,a}, and 1/16 at masks empty,{x},{b},{x,b},{y},{x,y},{b,y},{x,b,y}. Every other parent mass is zero. Thus H(F)=3 exactly and H/I=2. Each child has one heavy mass 9/16 and seven other masses 1/16 on all frequencies of {x,b,y}; the heavy mass is empty for a=0 and {x} for a=1. Their entropy is 4-(9/8)log2(3). Parent product-reference marginals are (1/2,1/2,1/4,1/4) on (x,a,b,y); its induced reference branch predictions are exactly fair.

The retained conditional spectator entropy is

    L_root=1/2,
    average L_child=1-(9/8)log2(3)+(5/8)log2(5),
    DeltaL=-1/2+(9/8)log2(3)-(5/8)log2(5)<0.

The exact inherited and freshly projected conditional KL bills are

    average C_Z(P_b,Q_B,b)=3-(3/4)log2(3)-(3/4)log2(5),
    average C_Z(P_b,Q'_b)=1+(3/8)log2(3)-(5/8)log2(5).

Consequently

    rho_cond=-2+(9/8)log2(3)+(1/8)log2(5)>0.

Multiplying the entropy drift by eight proves its negative sign from 3^9<2^4*5^5. Multiplying the conditional reset by eight proves its positive sign from 3^9*5>2^16. These are exact integer inequalities, with no floating-point sign or limiting argument. The positive reset is approximately 0.0733 bits, but its rational interval is the actual computational certificate. Because [DeltaL]_+=0, every finite K in the tested extension fails. There is no claim that rho_cond/I is unbounded: this is a false zero-credit substitution with queried influence 1/2.

The sufficient likelihood ratio p/q=r(T) explicitly fails. For example source p at {a} is 1/4 while its product reference mass is 9/64, and source p at empty is 1/16 with the same reference mass 9/64. Both project to retained T=empty but their likelihood ratios are 16/9 and 4/9. Some reference-positive root rows also have source mass zero. Thus the example does not refute A050's scoped matching theorem.

## 4. Exact minimality within the frozen reference scheme

For all 256 Boolean truth tables on three bits, query coordinate 0 and use one spectator coordinate, with product parent/fresh references and the same physical Bayes transport. None has essential query, DeltaL<=0 and rho_cond>0. A second exact run checks all 256 tables with both remaining coordinates in the spectator block; again none. Renaming cube coordinates covers every query and every nonempty spectator block on n=3. An empty spectator block has no conditional reset. Every n<=2 case embeds with a dummy coordinate and unchanged product reference/transport on its support. Therefore effective dimension four is minimal for this particular false extension under its fixed reference/fallback convention. This is not a minimum across arbitrary references or all possible FEI counterexample targets.

The census establishes this finite minimality; it does not prove a universal nonmatching payment bound. Four actual reached priority point-core fixtures v_n, n=1,...,4, retain the nonmatching histories and terminal profiles. No larger dimension was chosen automatically.

## 5. Bridge and first unsupported line

The matched-kernel theorem controls exact common conditional transport; its influence-priced entropy drift is a different quantity from the signed conditional KL reset. The concrete gate retains both true child spectra and influence, and refutes buying the latter from the positive part of the former alone. A039's occupancy release deficits and A083's physical versus equal-leaf posterior mismatch are consistent with this distinction; neither supplies unused credit here.

There is a precise normalized PRODUCT-reference repair when the entire signed conditional account is carried. Write C_v=D(P_v||Qprod_v)-D(P_{v,T}||Qprod_{v,T})=sum_{j in Z}h2(d_j(v))-H(S_Z|T). For any fresh query outside fixed Z, let Gamma_Z=sum_{j in Z}[h2(d_j)-average_b h2(d_j(b))]. Spectral restriction preserves expected spectator influence, so concavity gives Gamma_Z>=0. Algebra gives

    average C_child-C_root=DeltaL-Gamma_Z,
    [average C_child-C_root]_+<=2 Inf_i/ln2.

For a tree never querying fixed Z this telescopes to E C_leaf<=C_root+2 I_removed/ln2. C_root is an existing conditional reference debt, not a newly supplied influence reserve. The quotient bank and full terminal spectrum still need payment. This corollary applies to endpoint product projections, including nonmatching histories, not arbitrary occupancy or chosen references. It is a narrow application of the independently reviewed entropy-drift lemma, not a new broad FEI candidate.

In the four-bit certificate Gamma_Z=0 and the original parent conditional bank is C_root=3/2-(3/4)log2(3). The erased conditional bank is C_e=1-(3/2)log2(3)+(5/8)log2(5). Actual inherited conditional branch release is O_cond=C_e-C_Bayes=-2-(3/4)log2(3)+(11/8)log2(5). Thus

    C_root-C_fresh=-DeltaL>0,
    rho_cond-O_cond=(5/8)log2(27/25)>0,
    C_root-C_fresh=(C_root-C_e)+O_cond-rho_cond.

The erased conditional source bank alone is slightly larger than rho_cond (certified by 2^24*5^4>3^21), but it already includes the inherited child conditional debt. Spending it all on rho_cond would reuse that child bank. The exact conditional erasure C_root-C_e restores the positive balance; omitting it produces the strict deficit above. This identifies both a failed release-only payment and a valid once-only joint conditional payment at the source's actual query. No total-influence price is assigned to C_root itself.

FIRST UNSUPPORTED universal line: supply the initial conditional source bank and retained quotient reference together with complete terminal/core bills from one exclusive physical influence budget, or transfer this product-reference signed payment to the actual canonical occupancy reference with its complete likelihood correction. The shortest next action is to carry the exact conditional erasure/likelihood statistic distinguishing {a} from empty into that prescribed occupancy reference, explicitly retaining reference-only rows and both child debts. Reopening a separate history-bank bound or assuming a matched-kernel hypothesis on this gate would repeat a settled obstruction.
