# Third-query boundary with the original two-query bank retained

All bits are binary, signs Boolean, Fourier transform normalized, entropy in bits. This is an obstruction to an ALL-POLICIES stopping rule, not to FEI or an existential block rule.

## Family and complete signed spectra
For integer r>=1 set m=2r, d=2^-m, t=2^-r. Put g(x)=(-1)^(sum_j x_(2j)x_(2j+1)), and g'=g-2*1_{x=0}. Both are Boolean. Define h(x,0)=g(x), h(x,1)=g'(x). Every Walsh coefficient of g is sigma_s*t, sigma_s in {+1,-1}; there are c_+=(2^m+2^r)/2 plus signs and c_-=(2^m-2^r)/2 minus signs. This follows by tensoring the two-bit AND sign with coefficients (1,1,1,-1)/2. At each data label s, h has coefficients sigma_s*t-d without the selector and d with the selector.

Replace EVERY logical bit of h by parity of its own disjoint triple of physical bits. This gives F on n=3(m+1)=6r+3 bits with Fourier support a triple repetition code, minimum distance at least 3. Its support has exactly 2^(m+1) labels. Set p=2^-n and G=F-2*1_{physical 0}. Since F(0)=1 this is a Boolean one-point edit. Its coefficients are: sigma_s*t-d-2p on selector-free code labels, d-2p on selector-containing code labels, and -2p off the code. All are nonzero. In particular every variable is essential.

F has even negative count: every h input has 2^(2(m+1)) physical preimages. G has odd negative count. Hence G cannot factor as a product of Boolean functions on two nonempty disjoint sets: such a product has negative count a(2^v-b)+(2^u-a)b, which is even when u,v>=1. Thus this family also has exact tensor primitivity despite its coded ancestry.

Query the three ORIGINAL physical bits encoding the selector, in a fixed order. Retain their actual four prefix children, eight terminal children, and their original probabilities. All seed data neighbors of 0 equal +1 and all seed selector neighbors equal -1. The exact influence edit formula is 2p F(0)F(e_i). Therefore

 Q_2=2d-4p, Q_3=3d-6p,
 I(G)=3m/2+3(m+1)d+6(m-1)p.

Q_j is the total influence of queried coordinates at the root; it equals the expected accumulated query debit by restriction averaging. H(G)<=n and I(G)>=3m/2 give H(G)/I(G)<=2(m+1)/m<=3. This family is already FEI(3), and cannot be a positive K>=9 witness.

## Actual prefix and terminal bank, including all old credit
Write H_h=H(h), H_g'=H(g'), and let E(N) denote the entropy of a zero-vertex edit of h coded on N physical bits, with triple data blocks and a selector block of the remaining size. It has the three coefficient groups above with p replaced by 2^-N. At the two-query prefix N=n-2: three branches have entropy H_h, and the single edited branch has entropy E(n-2), each at reach 1/4. Therefore

 L_2=E(n)-[E(n-2)+3 H_h]/4.

At depth three, four branches are g', three are g, and one is the physical zero-vertex edit of triple-coded g, on 3m bits. Write its entropy H_e; its coefficients are sigma_s*t-2q on data code labels and -2q off code, q=2^-3m=8p. Thus exactly

 L_3=E(n)-[H_e+3m+4 H_g']/8.

For K>=9 retain B_2=L_2-K Q_2 and B_3=L_3-K Q_3. The third incremental bill is B_3-B_2=(L_3-L_2)-K(d-2p); no credit is reset. The prior stage theorem applies to this very family and policy, so B_2<-p/2. The check recomputes the actual negative B_2 directly, independently of that theorem.

## Divergent third-query price: analytic all-dimensional certificate
Before the final physical point edit, the three-bit block entropy decrement of F equals the one-selector decrement of h. In each signed row (a_s,b_s)=(sigma_s*t-d,d), put w_s=a_s^2+b_s^2. The spectral conditional entropy contributes at least b_s^2 log2(w_s/b_s^2). The full physical decrement equals that conditional entropy plus a nonnegative Jensen-Shannon term (the entropy of the average of the two squared restricted spectra minus their average entropy). Since t<=1/2, |a_s|>=t/2, w_s>=d/4. Summing the 2^m rows yields

 L_3(F)>=2^m*d^2*(m-2)=(m-2)d.

For completeness the point-edit transfer uses finite probability coupling, not an unproved continuity heuristic. Two normalized real amplitude vectors u,v give TV(u^2,v^2)<=||u-v||_2 ||u+v||_2/2. A Boolean point edit of measure delta has inner product 1-2delta, hence TV<=2sqrt(delta(1-delta)). Coupling distributions on at most 2^N labels gives |H(P)-H(Q)|<=h2(epsilon)+epsilon*N for epsilon=TV, by introducing the disagreement event and conditioning. If epsilon<=U<=1/2 then this is <=h2(U)+U*N. Finally h2(U)<=U[log2(1/U)+1/ln(2)]<U[log2(1/U)+3/2], since ln(2)>2/3 by its positive atanh series.

At the root choose U=2^-3r, which exceeds 2sqrt(p). The root error is less than U(9r+9/2). The single changed terminal has dimension 6r, edit measure q=8p, and admissible bound 2U; its weighted error is less than (2U/8)(9r+1/2). Thus

 |L_3(G)-L_3(F)| < 2^-3r*(90r+37)/8.

For every r>=7 this is less than d. Indeed 90*7+37=667<8*2^7=1024; the induction follows from 90(r+1)+37<2(90r+37) for r>=1. Consequently

 L_3(G)>(2r-3)d,   Q_3<3d,   L_3(G)/Q_3>(2r-3)/3 -> infinity.

For every fixed K>=9 choose r>=7 with 2r-3>3K. Then B_3>0 despite the entire paid two-query prefix. In particular r=16,K=9 gives B_3>2d. Hence the all-policy two-query theorem has a sharp obstruction at the first permitted support collision. Selection, or a criticality-dependent release mechanism, is essential; tensor primitivity alone does not pay this third query.

## First unsupported line
On a least-dimensional positive fixed-K witness, choose an original proper block and rank-certified unused affine release whose SAME ancestor deficit plus complete transformed-terminal reserve is nonpositive. The explicit G above cannot refute that line because it already satisfies FEI(3). No universal critical selector is proved here.
