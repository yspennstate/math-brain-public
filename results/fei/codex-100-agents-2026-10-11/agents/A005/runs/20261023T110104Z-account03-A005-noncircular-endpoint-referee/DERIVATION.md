# Arbitrary affine frontiers retain rare-core deficit

Finite uniform cubes, actual Boolean signs, normalized Walsh coefficients, entropy H in bits, D_K=H-KI with K>=0. All adaptive branches carry their original conditional probability. No infinite optimizer is used.

## 1. A character-error potential survives every affine chart

Define e(g)=min_(sigma=+-1,S) P[g(X)!=sigma chi_S(X)]=(1-max_S |ghat(S)|)/2. It lies in[0,1/2]. Every invertible affine input change and output-character multiplication permutes absolute Fourier coefficients, so preserves BOTH e and H.

Query any current physical coordinate i and let g_b be both actual children. Restrict one minimizing signed character of g to the two fibres. It is still a signed character on each fibre. Its two conditional errors average exactly to e(g), while each child may select a better signed character. Therefore

E_b e(g_b)<=e(g).

For any translation direction v, compare g to its best signed character on the two endpoints of that translation. The corresponding disagreement indicators can differ only if at least one endpoint is an error, of total probability<=2e(g). The character itself has directional disagreement either0 or1. Hence the smaller directional probability m_g(v)=min(w_g(v),1-w_g(v)) satisfies

m_g(v)<=min(2e(g),1/2).

These are physical Boolean statements, not a relaxation of the squared spectrum.

## 2. One-query entropy price and a uniform adaptive bound

The established universal single-coordinate inequality is

L_i(g)=H(g)-E H(g_b)<=h2(p_i)+(2/ln2)p_i.

Multiply g by chi_i when p_i>1/2. This preserves root H and both complete child entropies and complements p_i. Thus the sharper symmetric form is

L_i(g)<=phi(m_i), phi(x)=h2(x)+(2/ln2)x, m_i=min(p_i,1-p_i).

Phi is concave and increasing on[0,1/2]. Let any adaptive tree have maximum SINGLE-COORDINATE query depth r, allowing arbitrary branch-dependent affine/character resets between queries. They may mix every remaining data/control direction and change the next query partition. Resets preserve e,H. Pad stopped leaves with idle levels (zero L, zero m) solely for accounting, without querying them.

The preceding supermartingale gives E e at each padded level<=e(root). With a=min(2e(root),1/2), the active-node minority influences have average<=a. Jensen and monotonicity give, at every level,

sum_active reach*L_i <=phi(a).

Every complete reset terminal remains. Entropy telescopes, so

H(root)-E H(leaves)<=r phi(a).                            (1)

No sign or absolute-value bound on each L_i is asserted. Resets need NOT decrease I for (1). For deficit payment, assume each chosen reset does not increase the actual child influence. The physical influence split then gives E I(leaves)<=I(root), hence

E D_K(leaves)>=D_K(root)-r phi(a).                        (2)

This keeps signed complete terminal debt; it does not replace it by a coherent/incoherent mixture or drop a negative branch.

## 3. Arbitrary-seed admission through arbitrary affine frontiers

Take any finite positive-entropy seed f, choose its finite affine-minimal compressed representative g, H0=H(g)=H(f), q=I(g)<=I(f), mu=Eg, |mu|<1. For any integers t>=1,k>=2, p=2^-k, let G=g^tensor(t), and F=1+1[all k controls=0](G-1).

The source activation ledger gives

I(F)=p[tq+k(1-mu^t)],
H(F)=pt H0+R_k(mu^t), |R_k(u)|<=p(10k+15).

Tensor and activation preserve full affine span and influence minimality. A constant-character predictor has error p(1-mu^t)/2<=p, so a<=2p<=1/2. The entropy bound h2(x)<=x log2(e/x) and monotonicity imply

phi(a)<=phi(2p)<=2p[k+3/ln2].

Equations(1)--(2) therefore hold UNIFORMLY over EVERY permitted adaptive affine policy, including control queries and intervening changes of query partition:

E D_K(leaves)>=p[t(H0-Kq)-(10+2K)k-15-2r(k+3/ln2)].       (3)

If every complete terminal is K-nonviolating, and the numerator is positive, this forces the explicit necessary MAXIMUM-depth bound

r >= [t(H0-Kq)-(10+2K)k-15]/[2(k+3/ln2)].

This is a bound on maximum path depth, not expected depth; rare long paths must not be replaced by their average.

This extends A002's original-data/no-intervening-reset admission to arbitrary affine frontiers. The conclusion here is about the COMPLETE EXPECTED terminal deficit, not every leaf separately.

For the A051 bounded-I escape choose t=2^k. If r=r(k) satisfies rk/2^k->0, every policy retains expected deficit >=D_K(g)-o(1), while H(F)->H0, I(F)->q, F->1 in L2. This covers every fixed r and depths growing almost as fast as 2^k/k in the little-o sense.

For arbitrarily weak total influence choose t=2^l,k=2l. If r(l)l/2^l->0, then I(F)->0, H(F)/I(F)->H0/q, and

E D_K(leaves)/(pt)>=D_K(g)-o(1).

Consequently ANY positive seed deficit remains positive in at least one complete leaf of every such frontier, even after full affine optimization. There is no arbitrary-core embedding into genuine smaller-child NONVIOLATION. For all K the implication is conditional on an actual seed with positive D_K; no unknown universal-K counterexample is assumed.

## 4. Concrete certificate and the necessary scope boundary

Use the eight-bit point defect g, whose full spectrum has empty coefficient127/128 and255 other coefficients of magnitude1/128. It is full-span affine-minimal, q=1/16, and rational logarithm enclosures certify D_(15/4)(g)>1/256.

Choose k20,t2^20,r64,K15/4. Since ln2>2/3, the bracket deductions in(3) are

(10+2K)k+15=365,
2r(k+3/ln2)<2r(k+9/2)=3136.

Therefore EVERY permitted depth<=64 frontier has

E D_(15/4)(leaves)>595/1048576>0.

This is a fixed, explicitly defined finite Boolean root, certified by its formula and scalar inequalities; its multi-million-bit truth table is not constructed. It is a counterguard to frontier eligibility at this candidate constant, not an unbounded H/I family.

ALL-leaf positivity would be false with control queries: fixing any activation control to1 yields a constant child. This does not harm(2)--(3), which retain that zero-deficit branch at its full reach. Resets that increase I are excluded from(2); a constant can be multiplied by a fresh nontrivial character to increase I without changing H. Entropy statement(1) still holds for that reset.

## 5. Source-bound independent reconstructions

A002-BOUNDED-DATA-FRONTIER-ESCAPE@1, REVIEW_A051 Section4: scoped HOLDS without repair. At most r original-data queries touch at most r source copies. Entropy additivity bounds the changed contribution by r(d+H0). Full affine minimum is additive across tensor factors after minimizing each finite factor; untouched factors contribute at least(t-r)q. Activation's exact linear minimum then traps every original leaf influence within p[r(d+q)+2k] of q. The complete scalar entropy profile traps every leaf entropy within p[r(d+H0)+10k+15] of H0. These prove the source E and all-leaf conclusion under its precise narrower hypotheses. This is not a source census replay.

A052-ORIGINAL-PARTITION-COMPENSATED-RESET-INVARIANCE@1, PRECONDITIONING_PROOF Sections1--2: scoped HOLDS without repair. Its triangular affine map sends each original fibre bijectively to one original fibre. Complete child H and minimum I are unchanged. Thus both query-plus-release totals equal their own root I minus the SAME optimized leaf I; subtraction gives the stated compensated Delta. The minority directional costs transform by an invertible pullback, so every transported old parity booking has the same quotient rank. This accepts those identities, not source finite census or all-k guard. The present frontier theorem is not an invariance claim about changed partitions; it uses a separate character-error supermartingale.

## 6. First unsupported universal line

Use genuine finite least-essential-dimensional positive fixed-K criticality to force one paid ORIGINAL proper pair, with independent quotient-rank funding from the SAME unused NONNEGATIVE smaller-affine-child reserve, mixed interaction and every full terminal. Equations(1)--(3) do not select or fund that pair. Instead they show that short arbitrary affine frontiers cannot manufacture the missing terminal eligibility from rare arbitrary cores. No universal FEI constant improves. Analytic proof and exact finite certificates are author work pending independent-agent review.
