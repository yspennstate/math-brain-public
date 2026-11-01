# Later private query before the shared selector

All entropy uses bits. This is a restricted local payment, not full FEI.

Let Y be an independent fair {0,1} bit. Let A be any indicator on a private cube, and let B=P(1+x)/2, where P is any indicator on a second private cube and x is a fresh sign bit. These cubes are disjoint from Y and from three pairwise disjoint Boolean core cubes supporting u,v,G. Point events are the intended application. Put

F=(1-Y)G+Y[A u+(1-A)(B v+(1-B)G)].

The same physical G occurs twice. At any node obtained by compatible actual restrictions of these cubes, suppose Y and x remain unresolved. Put a=E A, p=E P and q=p/2. Orientations do not affect the argument. Then the full spectral erasure of this query satisfies B_x(F)<=(8+8a) Inf_x(F)<=16 Inf_x(F). If a<=1/2 the price is12; if a=1 both sides vanish. Thus every residual private-point A case has price12. Neither an independent replacement for G nor a new reserve is introduced. Core dimensions, residual private widths, biases and remaining core spectra are arbitrary. The initial point-guard bound14 was improved to12 by pairing the empty-controller rows before using triangle inequality. Checking which hypotheses the proof uses then removes the point-event assumption at the parameter-dependent price8+8a.

## 1. Scalar packet bound

Write Phi(s,t)=(s+t)h2(s/(s+t)), with Phi(0,0)=0. The standard scalar inequality is Phi(c^2,d^2)<=2|cd|. Here is a calculus verification: for z>=0 put g(z)=2z ln2-(1+z^2)ln(1+z^2)+z^2 ln(z^2), with g(0)=0. On (0,1), g'(z)=2 ln2-2z ln(1+1/z^2). The function k(z)=z ln(1+1/z^2) has derivative ln(1+1/z^2)-2/(1+z^2) and second derivative 2(z^2-1)/(z(1+z^2)^2)<0. Thus k is strictly concave on (0,1), starts at 0, ends at ln2 and has derivative ln2-1<0 at 1. It crosses the level ln2 exactly once in (0,1) and again at 1. Consequently g increases and then decreases to g(1)=0. Hence g>=0 on [0,1]; g(z)=z^2 g(1/z) handles z>1. The endpoints d=0 or c=0 give zero exactly. This keeps the full packet; it does not replace an alpha^2 log(1/alpha^2) asymptotic by O(alpha^2).

## 2. Keep the repeated fallback in one Fourier row

On the cube excluding B's coordinates set K=G+YA(u-G) and D=Y(1-A)(v-G). The queried Walsh pair is (Lhat,bhat), where b=PD/2 and L=K+b. Thus, by triangle inequality and disjointness of P and (K,D),

sum |Lhat bhat| <= q S + d,
S=sum |Khat Dhat|,   d=||b||_2^2=Inf_x(F).

The identity for d uses Boolean F: the half-difference b is in {0,+1,-1}. More explicitly, with m=E G, n=E v, T=1-mn,

d=q(1-a)T/2.

In the K,D overlap, nonempty u-only and v-only data rows are disjoint, and rows containing more than one core support vanish. The only remaining data rows are G-nonempty rows and the all-empty row. With V=1-m^2, and ell=E u, their contributions give

S <= [(1-a)(1+a)/2] V
     + |n-m| [(1-a)max(|m|,|M|)/2+a(1-a)|ell-m|/2],    (1)

where M=(1-a)m+a ell. Indeed, in the all-empty data row, the empty-A pair of Y coefficients of K is ((m+M)/2,(M-m)/2), and those of D have modulus (1-a)|n-m|/2. Their product sum is (1-a)|n-m|max(|m|,|M|)/2. Nonempty A rows contribute exactly a(1-a)|n-m||ell-m|/2. Keeping the Y pair together is what improves14 to12.

For completeness, the controller Fourier overlaps used here are exact:

sum |(1-YA)hat [Y(1-A)]hat|=(1-a)(1+a)/2,
sum |1hat [Y(1-A)]hat|=(1-a)/2,
sum |(YA)hat [Y(1-A)]hat|=a(1-a).

For ANY indicator A, Ahat(empty)=a, (1-A)hat(S)=-Ahat(S) for S nonempty, and Parseval gives sum_nonempty Ahat(S)^2=a(1-a). Hence sum |Ahat(1-A)hat|=2a(1-a). Tensor with Y (sum Yhat^2=1/2) proves the third identity. Separating empty and nonempty A rows proves the first; the second has just the empty controller row. For a=0 and a=1 the identities follow directly. No flatness of the A or P spectra is used.

## 3. Price by actual current influence

For m,n in [-1,1], |n-m|<=T, because T>=0 and T^2-(n-m)^2=(1-m^2)(1-n^2)>=0. Also V<=2T: T>=1-|m|, and V=(1-|m|)(1+|m|)<=2(1-|m|). Finally |ell-m|<=2 and max(|m|,|M|)<=1 since M is a convex combination. Substitution into (1) yields

S <=(1-a)(3/2+2a)T,                                  (2)

for every a in [0,1]. The right side is at most (5/2)(1-a)T when a<=1/2. Therefore

B_x(F)=sum Phi(Lhat^2,bhat^2)
 <=2sum |Lhat bhat| <=2q S+2d <=(8+8a)d.

If a=1 then D=b=0 and both sides vanish. If q=0, T=0, or any core is constant, the formulas still hold without division. This proves the all-dimensional stated local result by ordinary analysis; independent review remains required. The exact finite replay supplements the argument and does not prove its infinite quantifiers.

## 4. Ledger consequence and exact unpaid line

The actual restriction entropy decrement is B_x+JS_x, with JS_x<=2d/ln2, hence Delta_x H<=(8+8a+2/ln2)d. For residual point A this is at most (12+2/ln2)d. For any stopping prefix consisting only of queries covered by this theorem with a<=1/2 or a=1, sum w Delta_x H<=(12+2/ln2)sum w d, retaining E H(F_leaf) exactly. This assertion does not extend to unrestricted data or shared-selector queries by omission.

Keep the original merged controller probabilities pi_G=1/2+(1-a)(1-b)/2, pi_u=a/2, pi_v=(1-a)b/2, where b=Pr[B]. The fine reserve R=sum_j pi_j log2(1/pi_j) Var(core_j), and the complete actual leaf entropy/profile, are carried from the same physical partition. The present bound spends only current query influence and does not debit or replenish R. If a previously proved nonnegative reserve release is subtracted, the inequality remains valid, but that release is not counted as additional funding here.

The first unsupported universal line is payment of the inherited arbitrary-core profile and unresolved overlapping-controller queries with the same previous debits. In particular, the cores above may encode arbitrary Boolean functions; their terminal entropy has not been bounded. Ordinary data-query remainders have an imported signed payment, but this does not pay inherited core entropy. A per-node private-query theorem is not an FEI proof.

## 5. Source-dependent two-prefix stopped extension

Take A and B to be private point events again and keep the same single arbitrary Boolean G core. The first-private query is paid by A057 stage6 Section3, the later-private query by the proof above, Y by the imported A091 shared-activation repeated-fallback result, and queries after Y by the previously accepted two-private-test result (A057 stage5). Thus both private tests may now be queried in arbitrary order before Y. Actual core-data queries may be interleaved under the stage4 exact signed data identity. Every such source dependency is explicit; this corollary is not an independent review of those earlier theorems.

Let E_ne(h)=H(h)-phi((E h)^2), U=sum pi_j E_ne(h_j), R=sum phi(pi_j)Var(h_j), with the SAME merged probabilities in Section4 recomputed only by actual restrictions. U is harmonic at controller queries and R has nonnegative controller release. The new query satisfies Delta H <= drop(U+R)+(12+2/ln2)d without spending R, while all imported controller prices are <17. On data queries, the stage4 signed identity and M+N<=(3/ln2)pi_j beta^2+phi(pi_j)beta^2+pi_j phi(beta^2) give Delta H<=drop(U+R)+(3/ln2)Inf_query. Therefore, on every finite compatible stopped tree,

H_root <= U_root+R_root+(3/ln2)Pi_data+17 Pi_ctrl
          +E[H_leaf-U_leaf-R_leaf].

Both actual child terminal profiles are retained even when a test stops unresolved. No child receives a fresh root reserve. The root R funding (if used) is the prior once-only R_root<=2 I_ctrl(root); it is separate from the rate17. The inherited U_root remains arbitrary core entropy and is not declared paid. Queries inside G while Y and a prefix remain unresolved, or nonpoint guard queries within A, are outside the controller payment in a refined fine-core representation. Treating G as one coarse arbitrary core merely transports those queries through its still-unpaid E_ne(G); it does not pay the fine controller bill. The ordinary core-data identity is paid locally, but its inherited U and full terminal profile remain the universal obstruction.
