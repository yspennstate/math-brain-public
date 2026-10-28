# Sharpness and scoped reconstruction of A059's singleton-density transfer

Entropy is in bits. All functions below are actual Boolean signs on disjoint uniform cubes. This independently reconstructs A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1, Sections 1 and 2's variance identity, and Section 3's elementary source budget. It does not independently accept the imported controller/DATA estimates or the assembled stopping theorem. Full FEI remains open.

## 1. Reconstruction of the exact packet and its upper bound

Put F(z,y)=K(z)+C(z)g(y), with C an indicator of mean c>0 and K=0 on C, a sign elsewhere. Fix internal coordinate i. Let mu=Eg, beta=ghat(i), t=Inf_i(g), and let B_i denote spectral erasure. For each remaining internal frequency u, pair amplitudes indexed by u and u+i. If u is nonempty, both amplitudes are Chat(z) times the corresponding amplitudes of g. Homogeneity Phi(ra,rb)=r Phi(a,b) and sum Chat^2=c give c times the corresponding g packet. At u empty the original c Phi(mu^2,beta^2) is replaced by

S=sum_z Phi((Khat(z)+mu Chat(z))^2,beta^2 Chat(z)^2).

Consequently B_i(F)=c B_i(g)-c Phi(mu^2,beta^2)+S, exactly. This derivation uses physical Fourier pairs, not a latent selector law.

For beta nonzero, use Phi(a,b)<=b[1+ln(1+a/b)]/ln2. On Chat nonzero rows, normalize weights Chat^2/c. Jensen's inequality gives

S <= c beta^2 [1+ln(1+(1-c+c mu^2)/(c beta^2))]/ln2.

Indeed the weighted numerator norm is at most sum_z(Khat+mu Chat)^2=1-c+c mu^2, since KC=0. Omitting zero-Chat rows only decreases that norm. This is valid for dependent exterior K,C. The further bound

S <= c beta^2 log2(1/c)+c[(1+ln2)beta^2+2 beta^2 ln(1/|beta|)]/ln2

follows from 1-c+c mu^2<=1 and |beta|<=1. The Boolean derivative takes values 0,+1,-1; its mean is beta and its second moment is t. Thus |beta|<=t, beta^2<=t and beta^2 ln(1/|beta|)<=t/e. The physical Jensen-Shannon remainder satisfies 0<=J_i(F)<=2ct/ln2: pairwise, in natural units, J(a,b)<=2 min(a^2,b^2)<=2b^2. Therefore

D_iH(F)<=c B_i(g)+c beta^2 log2(1/c)+[1+(3+2/e)/ln2]ct.

This reconstructs the source transfer without changing it. At beta=0, S=0 literally; at c=0 the query is irrelevant. The coefficient bound <7 follows from ln2>2/3 and 2/e<1. The physical-JS bound can also be checked by writing v=a^2+b^2 and q=2ab/v: the scalar bracket [(1+q)ln(1+q)+(1-q)ln(1-q)]/2 is at most 1-sqrt(1-q^2). Its derivative comparison is q/sqrt(1-q^2)>=atanh(q), whose derivative difference is nonnegative on [0,1).

## 2. Coefficient one in the singleton-density term is necessary

Fix any finite Boolean g and coordinate i with beta nonzero. For every even m>=4 let c=2^-m and b(z)=(-1)^(sum_j z_(2j)z_(2j+1)), on m bits. It has b(0)=1 and bhat(s)=sqrt(c)b(s). Set C=1_(z=0), K=b-C and F_m=K+Cg. These are actual signs; the internal influence is ct.

Every exterior packet in S has a_s=[sqrt(c)b(s)+(mu-1)c]^2 and b_s=beta^2 c^2. Since |mu-1|<=2 and sqrt(c)<=1/4,

a_s>=c(1-2sqrt(c))^2>=c/4.

For a,b>0, Phi(a,b)>=b log2(a/b): subtracting the right side leaves (a+b)log2(1+b/a)>=0. Summing 1/c rows gives

S>=c beta^2[m-2-log2(beta^2)]>=c beta^2(m-2).

The upper bound in Section 1 is c beta^2 m+O_g(c). The exact erasure identity and 0<=J<=2ct/ln2 therefore prove

lim_(m even -> infinity) [D_iH(F_m)-c B_i(g)]/[c log2(1/c)] = beta^2.       (A)

In particular no coefficient lambda<1 can replace one in the source density term with any fixed dimension-independent additive rate A ct, even for a fixed nonflat g such as AND3 (mu=3/4, beta=-1/4 at every coordinate). This is sharper than a fair-literal-only necessity example. It does not prove the source's base constant optimal.

## 3. The entire variance reserve is asymptotically necessary

At any actual restriction of g, child means are mu+beta and mu-beta. The average child squared mean is mu^2+beta^2, so the original mean-variance reserve releases exactly beta^2. On every finite stopping tree,

sum_v w_v beta_i(g_v)^2=Var(g)-E Var(g_leaf).

No influence surrogate or independence of child spectra is used. For a fixed COMPLETE internal query tree, apply (A) at every node (finitely many, all independent of m). The terms c B_i(g_v) and the bounded O_g_v(c) errors sum to O_g(c). The full physical entropy decrement telescopes with both actual exterior terminals retained. If p_+=(1+mu)/2 and p_-=(1-mu)/2, this proves

lim_(m even -> infinity) {H(F_m)-p_+ H(b)-p_- H(b-2C)}/[c log2(1/c)] = Var(g).       (B)

Thus no uniform multiplicative discount of the whole variance ticket can fund these density bills, even if a fixed A c I(g) base allowance is retained: g is fixed while m grows. For incomplete finite trees the same argument yields Var(g)-E Var(g_leaf), retaining every actual exterior-wrapped terminal.

The history update is essential. For g=parity3 all INITIAL singleton coefficients are zero, yet Var(g)=1. A complete physical query tree first restricts parity until the last remaining literal has squared singleton coefficient one. Hence freezing the root singleton coefficients would assign zero density capacity while (B) tends to one. This refutes that frozen-root substitute, not the actual source theorem, which updates the reserve at every restriction.

## 4. Source-budget scope and tensorization

For A059's stated source W_0=g, W_1=b-C+Cg, the actual fresh-X influence is [1-c-mu(sqrt(c)-c)]/2>=(1-sqrt(c))/2>=3/8. The full D_X lies between zero and two bits. The root-weighted descendant variance ticket is (cm/2)Var(g)<=1/8 for even m>=4. Therefore D_X+E ticket<=17/8<=(17/3)d_X and the SAME original source6 account retains at least d_X/3 after the actual old D_X. This independently verifies the elementary source budget, including arbitrary bias. It does not verify the imported private-list/controller/DATA maintenance before and after X.

For products of independent Boolean factors, squared Fourier distributions are products and H and I add exactly. A FIXED global additive entropy constant disappears on taking k factors and dividing by k. A local change A ct is proportional to an influence bill and scales by k, so does NOT disappear in that way. Nor does the leading density coefficient: (A),(B) already force it to be one. Product examples transfer only to ledgers explicitly closed under additive factor accounts; no canonical single-wrapper tensor closure is asserted.

## 5. Exact obstruction to a rate6 source-only exterior extension

Take the SAME actual source with g identically +1. All internal influence, fine U/R, and mean-variance tickets vanish. The actual children are W_0=1 and W_1=b. Query X, retain the X=0 terminal, and on X=1 query exterior bit0 once. Both actual children of that exterior query have entropy m-2, so D_0H(b)=2 and its original-root-weighted cost is one bit. The original source account is 6d_X=3(1-s), where s=sqrt(c)=2^(-m/2).

The full spectrum of W has two empty-exterior amplitudes (1+s)/2,(1-s)/2 and 2(2^m-1) other amplitudes of magnitude s/2. Put G(s)=(1+s)^2 ln(1+s)+(1-s)^2 ln(1-s). Direct entropy evaluation gives

D_X=2-cm/2-G(s)/(2ln2).

Hence the actual two-query entropy decrement minus the WHOLE original source6 account is

Delta_m=D_X+1-6d_X=3s-cm/2-G(s)/(2ln2).

Now G(0)=G'(0)=0 and G''(s)=6+2ln(1-s^2)<=6, proving G(s)<=3s^2. For even m>=4, m*2^(-m/2)<=1 (the ratio from m to m+2 is (m+2)/(2m)<=1), s<=1/4 and ln2>2/3. Therefore

Delta_m >= s[3-ms/2-3s/(2ln2)] > (31/16)s >0.             (C)

This is an ALL-even-m actual Boolean obstruction. It spends the actual old D_X first and retains every full terminal. No internal ticket exists to transfer; the variance reserve is zero; reusing the incoming source6 alone cannot pay this exterior step. It does not refute the existing theorem, which explicitly excludes exterior queries. It does not rule out an originally funded exterior-influence account or a larger source price.

For the smallest case m=4, the squared root spectrum is exactly {25/64,9/64, thirty copies of1/64}. The literal terminal average after the two-query tree is one bit. Thus

Delta_4=11/4-[25log2(25)+9log2(9)]/64 >49/100.

Since d_X=3/8, a source-only rate for this enlarged policy must exceed73/10 (certificate below), rather than6. Direct character-sum reproduction verifies the same bound independently of the FWHT. The broader 24-case boundary probe also records nonflat AND3 fallbacks, but (C)'s zero-internal-ticket family is the clean obstruction; no claim is made that an enlarged original joint internal account cannot pay the AND3 cases.

Tensorizing the fixed m=4 two-query witness in an explicitly additive factor ledger multiplies Delta_4 by the number of factors. A FIXED global entropy allowance cannot repair source6. The fact that Delta_m tends to zero as m grows does not make it disappear under tensorization at fixed m. A per-factor or influence-proportional surcharge would survive.

## 6. First unsupported line

After an exterior bent-data query, c and K,C change. Concavity alone shows the old density ticket has NONNEGATIVE expected release: c log2(1/c)>=E[c_child log2(1/c_child)]. This does not bound the actual exterior query's entropy/profile debit after earlier internal debits. A rate6 source-only payment is now refuted by (C), including the zero-old-internal-debit boundary. A payment using genuinely unused originally funded EXTERIOR capacity, with both full child terminals and old debits, remains unproved. No universal FEI assertion follows from (A),(B),(C), or the scoped source audit.
