# WWW14 covariance payment for the audited GMP family

All entropies are in bits. This is a source-audit application, not a novelty or best-constant claim. Let a=7/8, r=a^k, epsilon=8^-k. Let f_k be OR of k disjoint AND3 blocks, with sign outputs. Let y be the minimal positive input with only the last block true; g_k agrees with f_k except g_k(y)=-1. Let F_k have selector children f_k,g_k.

## Source interface and its limits

Wan--Wright--Wu arXiv:1312.3003v1, Lemma 1.5, Lemmas 1.7/2.5 and Section 2.3 give an almost-prefix-free ternary protocol on a COMPLETE computing decision tree T. Its expected character count L is bounded by 4 I(f)+2 Cov(T). Consequently H(f)<=2 I(f)+log2(3)[4 I(f)+2 Cov(T)]. Cov(T) is the reach-weighted SIGNED covariance of physical sibling functions on their common remaining input cube. It is not conditional spectral entropy, an absolute covariance, or a nonnegative reserve. The theorem is a bound, not an assertion that every code has this length.

The read count is the total number of nodes bearing a variable across the tree, not the number of appearances on a path. WWW Theorem 1.1 gives 9k and Theorem 1.2 gives 12d only with I>=1. Shalev arXiv:1806.03646v2 Theorem 31 gives Cov(T)<=2 sqrt(k) I; Theorem 9 states its FEI consequence. Neither gives a universal constant for unbounded read count. The campaign C017 already records this overlap. No latest-best or priority conclusion follows from these two sources.

## A whole tree that pays the GMP forced selector

An independent reconstruction of the source payment uses A(T)=sum_v reach(v) Var(f_v). The source random protocol visits node v with nonempty spectral mass reach(v) Var(f_v), since the nonempty child spectral mass is exactly one half of that child's squared spectrum. Thus its expected character count is 2A(T). At each actual split, with child means a,b and child product expectation c, direct expansion gives Var(f_v)=2 Inf_query(f_v)+Cov(children)-(a-b)^2/4. On a complete computing tree, the influence telescope is sum reach Inf_query=I(f), while the martingale mean-square telescope is sum reach (a-b)^2/4=Var(f). Hence A(T)=2I(f)+Cov(T)-Var(f), independently recovering the source's upper bound and preserving its sign. The exact node identity and complete-tree aggregate are checked on the direct GMP fixtures. On a stopped tree these identities instead retain I(f)-E I(leaf) and Var(f)-E Var(leaf); they do not remove terminal spectral entropy.

Use the natural short-circuit tree T_k: inspect a block's three bits until the first false bit, then continue to the next block; stop positively at the first all-true block. Every leaf is constant. Write C_k=Cov(T_k), V_k=Var(f_k)=4a^k(1-a^k), C_0=0.

For a residual Boolean core h on disjoint variables, a partially tested fresh AND block with s remaining literals has plus child OR(AND_(s-1),h) and minus child h. Their covariance is (1-2^(-(s-1))) Var(h), because the fresh AND event is independent of h. If C is the covariance of the complete tree for h, the remaining-one-literal covariance is C/2; the remaining-two-literal covariance is Var(h)/2+3C/4; the remaining-three-literal covariance is Var(h)+7C/8. Therefore

    C_k = V_(k-1)+a C_(k-1)
        = 4 a^(k-1) [ k-8(1-a^k) ].

Since I(f_k)=(3k/4)a^(k-1), C_k/I(f_k)=16/3-[128/(3k)](1-a^k)<=16/3. This is a signed full-tree account; no local entropy-decrement rate is assumed.

To compute g_k use the same tree, refining its unique positive leaf containing y by a short-circuit test isolating y in that leaf. The refinement computes a constant minus one point, hence is a read-once OR/AND-of-literals tree with covariance zero. At an old ancestor of y of reach w, only one physical child changes. Its conditional edit probability is delta=2 epsilon/w. For sign functions u,u',v differing on a delta-fraction, |Cov(u,v)-Cov(u',v)|<=|E[(u-u')v]|+|E[u-u']E[v]|<=4 delta. Multiplication by w bounds the change by 8 epsilon per ancestor. There are at most 3k ancestors, so

    Cov(T_g)<=C_k+24k epsilon.

The exact root sibling covariance is Cov(f_k,g_k)=4r(1-r-epsilon)<=4r. The complete selector-first tree T_F therefore satisfies

    Cov(T_F)<=C_k+12k epsilon+4r.

For k>=2, divide this upper bound by I(f_k). The excess over 16/3 is at most

    -[128(1-a^k)-14]/(3k)+2/7^(k-1).

Here 1-a^k>=15/64, so the bracket is >=16. Also 3k<=8*7^(k-1) for k>=1: it holds at k=1 and multiplication by 7 dominates k->k+1. Thus 2/7^(k-1)<=16/(3k), and the excess is nonpositive. Finally I(F_k)=I(f_k)+epsilon(3k-5)>=I(f_k) for k>=2. Hence Cov(T_F)<= (16/3) I(F_k). The source protocol gives

    H(F_k)<= [2+(44/3)log2(3)] I(F_k) <26 I(F_k), k>=2.

The strict numerical bound uses the integer certificate 3^11<2^18, so log2(3)<18/11. For k=1, the actual four-bit F_1 has I=1/2 and H<=4, giving H<=8I. The displayed 26-rate payment is weaker than the earlier pending 23-rate source repair; its purpose is to expose a different, primary whole-tree funding mechanism. It does not improve that constant.

## Adversarial scope controls

For AND_n the short-circuit expected depth is d=2(1-2^-n), while I=n2^(1-n), so d/I=(2^n-1)/n diverges; replacing an expected-query-depth bill by an influence bill requires proof. Its tree covariance is zero. For parity_n the full natural tree has Cov=-(n-1), so tree covariance is not a nonnegative amount one may repeatedly spend. Adding m irrelevant queries above both copies of a fixed core adds m Var(core) to tree covariance without changing H or I: a universal bound for EVERY computing tree is false even for the AND2 core. This agrees with WWW's explicitly stated extraneous-path warning.

Stopping at a nonconstant leaf does not satisfy the computing-tree hypothesis: the leaf's spectral set can contain unqueried coordinates. For a stopped physical tree, the exact entropy telescope retains E H(leaf), and the influence telescope retains E I(leaf). The first unsupported universal line would be to invoke the complete-tree code at such a stopped tree, or to infer a dimension-independent covariance bound for some complete computing tree for every Boolean function. Neither is established here.

Universal bridge: C019 gains an explicit complete-tree covariance account for the very GMP family whose prescribed local decrement rate diverges. All terminal functions in this construction are computed, so no terminal bill is dropped. A universal selected-query/reference-reset invariant or a universally paid complete tree is still missing. The next shortest route is to compare this signed covariance bill with the campaign's same-reference residual at one inherited mixed query, keeping both child terminal debts and all earlier bookings.
