# Corrected GMP class-dependency chain

All entropy is in bits. For a Boolean split with child coefficients a,b, let V=sum|a^2-b^2| and D=sum(a-b)^2=4I_i. Use the complete decrement Delta=E+R from the previous run, with q=(a^2+b^2)/2, E=sum q h((a-b)^2/[2(a^2+b^2)]), R=sum q[1-h(a^2/(a^2+b^2))]. Zero fibers contribute zero.

The corrected entropy upper bound is h(t)<=2sqrt(t(1-t)). A proof avoiding a citation dependency: put z=2sqrt(t(1-t)) and x=sqrt(1-z^2). The function G(z)=h((1-x)/2) has G(0)=0, G(1)=1 and G''(z)=[atanh(x)-x]/[(ln2)x^3]>=0 for 0<z<1. Convexity gives G(z)<=z, extending by continuity to the endpoints. Consequently each q h term is <=|a^2-b^2|/2. Thus E<=V/2. The positive binary-entropy series gives 0<=R<=D (the proof is reproduced in the previous REPORT); hence

Delta_i <= V_i/2 + 4I_i.

For completeness, the refund estimate is independent of the earlier claim's review: with t=(1+e)/2, the nonnegative series 1-h(t)=(1/ln2) sum_{j>=1} e^{2j}/[2j(2j-1)] is <=e^2, because the coefficients sum to ln2 at e=1. Then q[1-h(a^2/(a^2+b^2))]<=(a^2-b^2)^2/[2(a^2+b^2)]<=(a-b)^2. The last step uses (a+b)^2<=2(a^2+b^2). Summing proves R<=D including endpoint and zero cases.

This replaces GMP's printed use of h<=sqrt and the dropping of R. In particular V_i<=K I_i implies Delta_i<=(K/2+4)I_i. No zero-influence exception is needed: D=0 forces a=b and both sides vanish. The constants below are conservative source repairs, not claims of sharpness or novelty.

For every finite physical stopping tree, weight a reached node v by w_v=2^{-depth(v)}; variables are never re-queried along a path. Retain the exact terminal term:

H(f)=sum_internal w_v Delta_v + sum_terminal w_l H(f_l),
I(f)=sum_internal w_v I_query(f_v) + sum_terminal w_l I(f_l).

If all terminal functions share a dimension-independent constant C0 and every internal V_v<=K I_query(f_v), it follows that H(f)<=max(C0,K/2+4) I(f). Merely saying each finite leaf has some constant does not supply a uniform class theorem. This is a use of the established stopping-tree telescope, not a new universal reduction.

GMP Proposition 6.1 survives its own algebra: for g+=pq, g-=pr with separated {-1,0,1}-valued functions, the q-exclusive and r-exclusive Fourier sectors each contribute at most D; the common p sector contributes at most 2D. In detail D=E p^2 [E q^2+E r^2-2(E q)(E r)]. Since q^2=|q| and r^2=|r|, the bracket is at least |E q|+|E r|-2|E q||E r|. Also |a^2-b^2|<=2(a+b-2ab) for a,b in [0,1]: assume a>=b, use a+b<=2 and a+b-2ab>=a-b. The common sector equals E p^2 |(E q)^2-(E r)^2|, proving its 2D bound. Hence V_g<=4D_g. If g+ and g- are Boolean children this gives V_f<=16I_i. Thus Theorem 6.3's semi-separation class has corrected node rate 12 and global rate max(C0,12). Common p spectra cancel by tensor factorization; no independent data entropy is discarded at the leaves.

For Theorem 6.8, tribe separation gives Boolean children f-=h, f+=max(h,k) with h,k on disjoint coordinates. Set beta(h)=(1-h)/2. Then g-=beta(h), g+=beta(h)beta(k), a semi-separated {-1,0,1} pair with the third factor equal to 1. Its D_g=(1/4)D_f=I_i(f). Proposition 6.1 gives V_g<=4I_i. For nonempty Fourier sets the f coefficients are -2 times the g coefficients, so their V contribution is <=16I_i. For the empty set, |(E f+)^2-(E f-)^2|<=2|E f+-E f-|=4I_i, using monotonicity. Therefore V_f<=20I_i, corrected node rate 14 and global rate max(C0,14). Source equation (30) also changes the normalization of K; the explicit calculation here keeps the factor four.

For Theorem 5.3, let H be disjoint tribes on m>=1 bits of widths w_j>=1, let G be OR of those m bits and one extra bit, and let u>=1 be the shared-block width. A positive-prefix node is H+(G-H) AND_u. Split a shared bit: f-=H and f+=H+(G-H) AND_{u-1}. Put h0=E H and alpha=2^{1-u}. A fiber involving a remaining shared bit or the extra OR bit has b=0, so total V in these fibers is <=D=4I_i. The empty fiber contributes <=4I_i by monotonicity. Other fibers have nonempty T on the m data bits, a_T=b_T+alpha(Ghat(T)-Hhat(T)). For I_i=2^{-u}(1-2^{-m}-h0), disjoint tribes imply 2*2^{-m}<=1-h0 and therefore I_i>=2^{-(u+1)}(1-h0). To verify the first inequality, 1-h0=2 product_j(1-2^{-w_j})>=2 product_j 2^{-w_j}=2*2^{-m}.

Write W=1-h0. Sum over nonempty data T. The elementary bound |a^2-b^2|<=|a-b|^2+2|a-b||b| gives a first term <=4I_i. Parseval gives sum Hhat(T)^2=1-h0^2<=2W. Since |Ghat(T)|=2^{-m}, Cauchy via 2|Ghat Hhat|<=Ghat^2+Hhat^2 gives sum 2|Ghat Hhat|<=2^{-m}+2W<=5W/2. The two cross terms are thus at most (5+8)2^{-u}W<=26I_i. Data-only fibers contribute <=30I_i. Combining the three sectors gives V_i<=38I_i and corrected node rate 23. The same derivation applies at every positive shared-block prefix. When m=0, the function is AND of u shared bits and the extra bit: V_i=8*2^{-u}(1-2^{-u})<=8I_i, so the degenerate case also satisfies the rate.

After the shared block is queried, leaves are H and G. Both are disjoint tribes (constants permitted). Every restriction of a disjoint-tribes function remains disjoint tribes or a constant, and every relevant split is tribe separated. The preceding 14-rate reconstruction therefore proves H<=14I for disjoint tribes by a full tree with constant leaves. This supplies a uniform terminal certificate without importing an unchecked numerical constant. The delta-tribes theorem is restored with H<=23I. CKLS corrected Theorem 5.11 and Remark 5.1 also state the stronger read-once bound H<=10I, but that additional source bound is not needed here.

The first unsupported universal step remains existence of a physical tree with V_v<=K I_query(f_v) for every arbitrary Boolean root, or a signed replacement whose excess is paid once by an owned child/terminal reserve. GMP Proposition 5.1 already shows that arbitrary fixed splitting choices do not suffice. Restoring its class proofs does not prove that universal step.
