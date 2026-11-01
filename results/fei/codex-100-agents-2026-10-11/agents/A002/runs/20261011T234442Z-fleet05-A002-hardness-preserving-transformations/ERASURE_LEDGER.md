# Exact aggregate-erasure transport

For a probability law P on subsets of [n], write H(P) for entropy in bits, B_i(P)=H(S_i|S_-i), B=sum B_i, and D=H-B (dual total correlation). Let phi(x)=-x log2 x and E(x,y)=phi(x)+phi(y)-phi(x+y). Then B_i is the sum of E(P(T),P(T+i)) over T not containing i. E is nonnegative and homogeneous of degree one, including zero arguments. All transformations below are actual Boolean signs on independent uniform physical cubes.

**Tensor, balancing, coding and parity lift.** Disjoint tensor products add H,I,B,D and multiply means; dimension adds. A fresh balancing literal z changes H,I,mean to H,I+1,0 and leaves B unchanged because its spectral membership is deterministic. Dummy padding and character multiplication preserve B. For systematic code S -> (S,AS), every new auxiliary B_j is zero and old B_i is B_i(seed) if column A_i=0 and zero otherwise. Thus B(code)=sum_(A_i=0) B_i(seed). This follows by testing spectral adjacency: an original-coordinate edge survives exactly when its column is zero; an auxiliary-coordinate edge is impossible for an injective graph. H and mean are unchanged and I increases by E|AS|. In particular the one-auxiliary parity lift with every column equal to 1 has B=0, H=H(seed), I=I(seed)+Pr(|S| odd). Pair parity lifts also have B=0, H unchanged and I doubled. Any support separation >1 has B=0, including stage 1's smoothed coded examples.

**General point activation.** Let h have mean a on n data bits, d=1-a, p=2^-s, s>=1; F=1+A_s(h-1) has n+s bits and mean 1-pd. Put c=(1-pd)^2 and q_i=hat h({i})^2. The exact formulas are

    B_i(F)=p[B_i(h)-E(a^2,q_i)] + p(1-p)E(d^2,q_i) + E(c,p^2 q_i)  (data i),
    B_j(F)=p(1-a^2)+(p-2p^2)d^2+E(c,p^2d^2)                  (each control j).

Proof: when the remaining data index T is nonempty, every control label contributes p^2 times the original edge entropy, summing to p times that edge entropy. For T empty, nonempty control labels give p^2(d^2,q_i), in number 1/p-1, and the empty control label gives (c,p^2q_i). Subtract the original empty-data edge before inserting these replacements. A control edge at nonempty data has equal masses, with total p(1-a^2); at empty data with nonempty remaining controls it contributes (p-2p^2)d^2; the last edge is (c,p^2d^2). This accounts for every spectral edge exactly once. H and I are the stage-1 three-group ledger, including I=p[I(h)+sd].

For a balanced core h=b^tensor m with m>=2, no singleton coefficient is nonzero (every tensor block must have nonempty support). Therefore

    B(F)=pm B(b)+s[2p-2p^2+E((1-p)^2,p^2)],
    H(F)=pm H(b)+2sp(2-p)+phi((1-p)^2), I(F)=p[mI(b)+s].

If H(b)>0, s=ceil(2log2 m), then B(F)/H(F)->B(b)/H(b) and H(F)/I(F)->H(b)/I(b). The control contribution divided by sp tends to 2, while its entropy contribution divided by sp tends to 4. Indeed E((1-p)^2,p^2)=O(p^2 log(1/p)) and phi((1-p)^2)=O(p). More generally when s/m->ell<infinity and s->infinity, the limits are (B(b)+2ell)/(H(b)+4ell) and (H(b)+4ell)/(I(b)+ell). Thus rarity does not supply a near-one erasure fraction for a seed below one; if controls dominate, B/H tends to 1/2. This is an erasure ledger, not a fresh proof of activation H/I.

**Balanced two-cell selector.** For balanced g on n bits, M_g=((1+g)/2)y1+((1-g)/2)y2 has n+2 bits, mean zero, H=2+H(g)/2 and I=1+I(g)/2. Its two leaf-label coordinates have B=0 because exactly one belongs to a sampled spectral set. Conditioning on the label leaves the same data law (delta_empty+P_g)/2 in either branch. Consequently

    B(M_g)=B(g)/2 + (1/2)sum_i E(1,hat g({i})^2).

Only the empty-data edges change; balance removes their original contribution. With g=z f^tensor m for a nonconstant arbitrary seed f of mean a, the only possible singleton is {z}, of mass a^(2m). Thus

    B(M_g)=mB(f)/2 + E(1,a^(2m))/2,
    H(M_g)=2+mH(f)/2, I(M_g)=3/2+mI(f)/2.

For H(f)>0 both normalized ratios tend to their seed ratios. With a balanced core b^tensor m, m>=2, even the extra singleton term vanishes. Tensoring, balancing, selector formation and economical activation therefore do not solve the lead's B/H->1 admission problem. Coding sets B to zero.

# Paid erasure inflation and its obstruction

Let b_r be any bent sign on 2r fresh bits, for example a product of r disjoint two-bit signs (-1)^(uv). It has H=B=2r and I=r. For F=f^tensor m times b_r,

    H=mH(f)+2r, B=mB(f)+2r, I=mI(f)+r, D=mD(f).

For H(f)>0 and D(f)>0 put R=H(f)/I(f), eta=D(f)/H(f), epsilon_F=D(F)/H(F). Eliminating r gives the exact Pareto relation

    H(F)/I(F) = 2/[1+(2/R-1)epsilon_F/eta].

If B(F)/H(F)->1 then epsilon_F->0 and the ratio tends to 2. It cannot preserve any fixed seed ratio R>2. More generally, adjoining any auxiliary tensor whose H/I is at most a fixed C cannot preserve a seed ratio R>C while forcing B/H->1: D(total)>=mD(seed) forces auxiliary entropy to dominate, so limsup H/I<=C. This is a proved obstruction to the specified tensor dilution mechanism, not an obstruction to all Boolean transformations.

For R in (0,2], admission is possible while retaining a physical seed tensor: choose r=m^2 and append a parity on ell_m=floor(r(2/R-1)) fresh coordinates (or no parity when ell_m=0). The parity has H=B=0 and I=ell_m. Then B/H->1 and H/I->R. For R=0 take ell_m=r^2 instead. The entropy overhead dominates the seed, so this is a paid low-ratio admission, not a compression of arbitrary seed entropy. A seed with R>2 is the first unresolved case. Seeds with D=0 already have a product spectral law and R<=2, as proved below.

# Exact endpoint and failed quantitative shortcut

For any law, B=H iff the coordinate membership bits are mutually independent. To prove it, fix any coordinate order and write D as the sum of nonnegative terms I(S_i; S_(i+1..n) | S_(1..i-1)). If D=0, the first bit is independent of all later bits; applying the remaining zero terms inductively yields a product law. The converse follows by conditioning independent bits.

For an actual uniform Boolean sign, one independent nontrivial spectral bit must have influence 1/2. Write the two Walsh magnitude ratios as coprime positive integers c/b. Independence gives |W_(T+i)|=c k_T and |W_T|=b k_T, and Parseval implies b^2+c^2 divides 2^(2n). Opposite parity gives an odd number >1; both odd gives 2 modulo 8; hence b=c=1. Deterministic bits have influences 0 or 1. Thus B=H forces a coordinate-face uniform spectrum, with an even number r of free bits since all nonzero amplitudes 2^(-r/2) are rational. Factoring deterministic memberships gives a character times a bent function on those r coordinates, and H=r<=2I. This reconstructs ERASURE_RIGIDITY section 1; it does not give stability for B near H.

Near-one B/H does not even imply closeness to the coordinate-product law. Let u and v be parities of two disjoint t-bit blocks, t>=2; let c_t=(-1)^(uv). Tensor this with bent b_r on 2r fresh bits. The actual Boolean function has dimension 2t+2r, mean 2^(-(r+1)),

    H=2+2r, B=2r, D=2, I=t+r,
    TC=sum_i H(S_i)-H=2t-2,
    TV(P, product_i P_i)=1-2^(2-2t).

Each t-block spectral membership is a duplicated fair flag; there are four possible cluster patterns. For t>=2 every bit inside a cluster is determined by its mates, so its B_i=0. Each fresh bent bit has B_i=1 and influence 1/2. Choosing t=r^2 gives B/H->1, TV->1 and TC/H->infinity, with H/I->0. Thus a dimension-independent near-product conclusion in total variation or total correlation is false even for actual Boolean spectra. The example has ample influence; it does not refute a near-erasure-fraction H/I bound.

# The precise universal residual

Fix epsilon in (0,1). Suppose every Boolean sign with B>=(1-epsilon)H obeys H<=C_epsilon I. For the other signs, B<(1-epsilon)H. On the near-one class B<=H<=(1-epsilon)H+epsilon C_epsilon I. Hence every sign obeys

    B <= (1-epsilon)H + epsilon C_epsilon I.

The lead's erasure-fraction bridge then gives full FEI with constant C_epsilon+2/(epsilon ln2). There is a sharper consequence retaining the piecewise hypothesis: FEI holds with constant max(C_epsilon,2/(epsilon ln2)). Here is an independent minimal-violator proof. Set c_JS=2/ln2 and C=max(C_epsilon,c_JS/epsilon). If a violator exists, take one with the fewest relevant coordinates n; n>=2 because one-variable signs have H=0. Every one-coordinate child obeys H<=CI. Write delta=H-CI>0. The influence and entropy restriction identities give, for every relevant i,

    Delta_i H >= C I_i + delta,
    B_i >= (C-c_JS)I_i + delta.

Sum these n inequalities to obtain D=H-B <= c_JS I-(n-1)delta < c_JS I. Since H/I>C>=c_JS/epsilon, D/H<epsilon, so the violator lies in the near-one class. Its assumed H<=C_epsilon I<=CI is a contradiction. This sharpens the additive transfer constant to a maximum, without proving the class premise. Conversely full FEI(C) bounds every near-one class by C. Thus bounded H/I for one fixed near-one erasure class is FEI-equivalent in finiteness, not an isolated product-spectrum stability result. The coefficient 2/(epsilon ln2) is a restriction JS payment, not a claim of equality of optimum constants.

The exact first unsupported line is a quantitative Boolean-specific statement for fixed epsilon>0 that bounds H/I on B>=(1-epsilon)H, or a genuinely different Boolean embedding that inflates the erasure fraction without diluting a seed ratio >2. Neither the exact product characterization nor any tested conventional transformation establishes it.
