# Rare majority-cut defects: growing Fourier norm paid without an l1 charge

All logarithms are bits, inputs uniform. Let b=2m+1>=3, c=b+3, d=2b+3. On d shared bits let h be central majority, +1 at weight<d/2. Let A be the event that all c address bits are0 and the b free bits have weight<=m. Thus p=Pr(A)=2^(-b-4). Replace h on A by an arbitrary Boolean profile V on an independent private cube, obtaining F=h+1_A(V-1). Write mu=EV. The private profile can be biased and have arbitrary dimension.

## 1. Genuine growing-norm positive event and physical ownership

A is not a subcube for b>=3. Its vertices and their immediate neighbors are in h=+1 (their weights are at most m+1<=b+1). No carrier pivotal edge is removed. With D=1-2*1_A, I_b=b*binom(b-1,m)/2^(b-1), direct edge counting gives

 I(D)=2^-c(c+I_b),
 I_shared(F)=I0+((1-mu)/2)I(D)>=I0,
 I_private(F)=p I(V), I0=I(Maj_d).                 (1)

The last equality holds coordinatewise; no private bill is issued again. Address boundary and free-majority boundary are disjoint, and all event-boundary edges were positive at both endpoints before editing.

For the b-bit majority, its coefficient at an individual odd level2l+1 is

 a_(2l+1)=(-1)^l alpha_b binom(m,l)/binom(2m,2l),
 alpha_b=binom(2m,m)/4^m.

This follows by taking a coordinate derivative (the central tie slice) and expanding its elementary character sum; equivalently its odd coefficients start at alpha_b and obey a_(k+2)=-k*a_k/(b-1-k). Consequently

 ||Maj_b_hat||_1=alpha_b*b*sum_(l=0..m) binom(m,l)/(2l+1)
                 >=alpha_b*2^m>=2^m/b.

The face indicator has l1 norm1 and is on disjoint address coordinates, so

 L_A=||1_A_hat||_1=(1+||Maj_b_hat||_1)/2>=2^(m-1)/b. (2)

Here alpha_b>=1/b because the central binomial coefficient is the maximum among2m+1 coefficients summing to4^m. Also I_shared(F)<=d+1. Thus the previous global derivative allowance12L_A divided by actual shared influence is unbounded. This refutes only that proposed allowance as a uniformly influence-priced source, not FEI or the actual entropy increment.

## 2. Complete private-frequency split

Let a_S=1_A_hat(S), C_A=sum_S g(a_S), g(t)=-t^2 log2(t^2), g(0)=0. Since sum a_S^2=p, normalized spectral entropy is at most d, giving

 0<=C_A<=p[d+log2(1/p)]=p(3b+7)<=1/8.             (3)

The last quantity is1/8 at b3 and strictly decreases when b increases by2. The complete empty-private row is mhat(S), where m(s)=E_private F=h+(mu-1)1_A. Put E=sum_S g(mhat(S)). Exact factorization of EVERY nonempty-private coefficient a_S*Vhat(T) yields

 H(F)=p H(V)+(1-mu^2)C_A+E-p g(mu).              (4)

No private dimension enters the shared spectral support and no zero/mean row is discarded. In particular negative correction -p g(mu) can be dropped for an upper bound, not converted into a new positive bank.

## 3. A normalized shared-sector continuity payment

Parseval gives ||mhat-hhat||_2<=2sqrt(p) and M=sum mhat^2=1-p(1-mu^2)<=1. Form probability distributions P=(hhat(S)^2,0) and Q=(mhat(S)^2,1-M) on2^d+1 symbols. Their total variation obeys

 delta<=0.5||mhat-hhat||_2(||mhat||_2+1)+(1-M)/2
       <=2sqrt(p)+p/2<=3sqrt(p).

For any two distributions on N+1 symbols, maximal coupling with mismatch probability delta gives |H(P)-H(Q)|<=h2(delta)+delta log2 N: condition on mismatch and at most N choices remain. Taking N=2^d and using H(Q)=E+phi(1-M)>=E gives

 E<=H(h)+1+3d sqrt(p)<H(h)+4.                    (5)

Indeed d^2 p<1 at b3 (81/128<1), and the step b->b+2 multiplies d^2 p by (d+4)^2/(4d^2)<1. This bound uses only the shared dimension. Applying continuity to the full private/shared cube instead would introduce an unjustified private-dimension cost. The extra mass1-M is indispensable for normalization.

## 4. Relative FEI and arbitrary finite towers

Universal quantitative lemma: the complete private-frequency split and normalized shared-sector continuity argument do NOT require a majority carrier, or even positivity of A. For ANY Boolean h and ANY event A on d shared inputs, set F=V on A and h elsewhere, with independent private inputs. For0<p<=1, exactly the same nonempty-private factorization and norm/mass estimates give

 H(F)<=p H(V)+H(h)+1+3d sqrt(p)+p[d+log2(1/p)].     (6a)

For a general A, use m=h+1_A(mu-h) rather than h+(mu-1)1_A. Positivity was used only for the majority family's physical source ownership(1). Equation(6a) is unconditional and retains the entire input entropy bill; it is not an influence-priced universal FEI theorem. The p0 case is exactly F=h.

Combining(3)-(5) gives, with NO threshold theorem yet,

                  H(F)<=p H(V)+H(h)+33/8.         (6)

The supplied threshold paper, Theorem A equation(6), pages1-2, gives H(h)<9I0. This is an EXPLICIT EXTERNAL PREMISE; its proof is not independently rechecked here. Majority influence is nondecreasing in odd dimension, so I0>=I(Maj9)=315/128 and33/8<=2I0. Hence

 H(F)<=p H(V)+11I_shared(F),
 I(F)=p I(V)+I_shared(F).                         (7)

If V has FEI constant C0, F has constant max(C0,11). Induction proves H<=11I for EVERY finite tower of these fresh-shared-coordinate majority-cut wrappers over constants/characters, uniformly in depth, rarity, and exponentially growing event Fourier norm. Over a certified base class use max(C0,11). Each original shared scale pays its own actual shared edges; the inherited private bill is multiplied by its actual activation p. There is no per-vertex/profile l1 allowance, child donor renewal, or sum of11 over depths. Arbitrary private dimension and bias are allowed.

This new static source payment does not transplant the earlier two-profile point-prefix prices, reset Q96I0, spend its old FIRST/D0 collision debits again, or assert consumed-influence stopping payment. Those earlier source claims retain their original scopes. Here one profile has an exact conditional spectral factorization and no collision source is required. The proof closes a genuinely new unbounded-l1 tower family, conditional solely on the supplied carrier threshold premise.

## 5. Exact remaining universal line

The dimension/rarity condition d^2 p<1 pays the shared-sector continuity bill. Arbitrary Boolean event geometry need not have a useful effective dimension satisfying this condition; many independently correlated profiles also lose the rank-one nonempty-private factorization(4). An influence-priced replacement for this effective-dimension/rare-mass term, with all full input/terminal rows retained, is not proved. Full FEI remains OPEN. NEXT: identify a complete shared spectral support or whole-set witness cost replacing d in(5), and price it from ORIGINAL unused boundary influence when d^2 p is unbounded. This moves C020/C024's actual source-admission obstruction rather than another depth test.
