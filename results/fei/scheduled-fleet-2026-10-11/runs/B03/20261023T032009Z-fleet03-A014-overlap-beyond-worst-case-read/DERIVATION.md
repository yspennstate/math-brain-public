# One inherited reference on Fourier pairs

The singleton debt and one conditional phase cost replace the amplification
of arbitrary inherited row KL. The same reference reaches both children.
This is a transport identity; its repeated phase costs are not yet paid.
All logarithms are base two. Constants have zero nonempty cost throughout.

Let f be any +/-1 function on a finite uniform cube, and choose coordinate i.
Let p(A)=fhat(A)^2, v=1-p(empty), m=p({i}), and w=v-m. Let f_0,f_1 be
the two restrictions, with spectra p_b and nonempty masses v_b. For every
nonempty T disjoint from i, define

 g(T)=p(T)+p(T+i)=[p_0(T)+p_1(T)]/2,    w=(v_0+v_1)/2.          (1)

This follows from the two Walsh identities fhat(T)=(fhat_0(T)+fhat_1(T))/2,
fhat(T+i)=(fhat_0(T)-fhat_1(T))/2. No disjointness or nesting is needed.

Fix a probability q on the nonempty Fourier sets, positive on EVERY such
set. We retain this one original reference throughout the comparison. Put
q_i=q({i}), and for nonempty T disjoint from i set

 qbar(T)=[q(T)+q(T+i)]/(1-q_i).                               (2)

For n>=2 the denominator is positive. This probability law depends only on
the inherited reference and i, and is used UNCHANGED for both children.
The case n=1 has w=0 and is handled without defining qbar.

Define qsym({i})=q_i and qsym(T)=qsym(T+i)=[q(T)+q(T+i)]/2.
Let Q(empty)=1-v, Q(A)=v q(A), and similarly Qsym. With
alpha=m/v when v>0 and w>0,

 E_sym := CE(p,Qsym)-H(f)
 = v D(Ber(alpha)||Ber(q_i))
   + w D(g/w||qbar) + Phi_i,                                (3)

 Phi_i=sum_{T!=empty} g(T)[1-h2(p(T+i)/g(T))],    0<=Phi_i<=w. (4)

Zero g terms are omitted. This is the KL chain rule for the partition into
the singleton {i} and the pairs {T,T+i}; the phase term is the conditional
KL from the true pair probabilities to the uniform phase law. The same
formula extends to w=0 with the proper-pair terms omitted. If v=0 all costs
are zero. These boundary conventions avoid every zero denominator.

Let Q_b(empty)=1-v_b and Q_b(T)=v_b qbar(T), b=0,1, with constants using
the empty point mass, and E_b=CE(p_b,Q_b)-H(f_b). Define the branch label
J by probabilities lambda_b=v_b/(2w), omitting zero v_b, and let
P_b=p_b(.|nonempty). Then g/w=sum lambda_b P_b, so

 w D(g/w||qbar)=(E_0+E_1)/2 - w JS_lambda(P_0,P_1).            (5)

In particular the coefficient-one transport is exact:

 E_sym = v D(Ber(alpha)||Ber(q_i)) + Phi_i
         +(E_0+E_1)/2 - w JS_lambda(P_0,P_1).                 (6)

All child terminal KL costs remain; the nonnegative JS term is a genuine
credit, not a new influence bank. Equation (6) repairs last stage's
arbitrary-reference amplification obstruction only by explicit pair
symmetrization, and with the singleton debt and phase term retained.

The change from the original reference has the exact signed cost

 CE(p,Qsym)-CE(p,Q)
 = sum_{T!=empty} [p(T)log(2q(T)/(q(T)+q(T+i)))
                  +p(T+i)log(2q(T+i)/(q(T)+q(T+i)))] <= w.     (7)

Each logarithm is <=1. This is a single fixed reference change; applying it
repeatedly requires payment of the accumulated costs, with old debits kept.

For a complete occupation mass M>0 on nonempty sets, Z=sum M, q=M/Z.
Equation (2) becomes [M(T)+M(T+i)]/[Z-M({i})]. Thus the original Z and
the full pair-sector normalizer are retained. The reference is neither
retuned by a sampled Fourier set nor replaced by a different prime table.
The two Q_b share qbar; only their actual empty/nonempty masses differ.

Optionally calibrate qsym's singleton mass to alpha and scale its pair
sector to 1-alpha, keeping qbar. The resulting Qcal has actual p(empty)
and p({i}), so

 E_cal = Phi_i+(E_0+E_1)/2-w JS_lambda(P_0,P_1),
 CE(p,Qcal)=CE(p,Qsym)-v D(Ber(alpha)||Ber(q_i)).                (8)

Calibration lowers expected cost, but (8) is not claimed for the original
unmodified reference. Any decoder/model-selection charge needed to implement
successive calibrations is still a separate obligation. Formula (6) keeps
the singleton debt for applications that must retain the original reference.

## Exact obstruction to a local influence payment

The phase term cannot be paid by a universal multiple of the queried
coordinate's influence, even with every coordinate relevant. Take odd
majority f on n=2k+1 bits. It is balanced and supported on odd Fourier
degrees. Every pair {T,T+i} therefore has at most one nonzero coefficient,
so its conditional phase entropy is zero and Phi_i=w=1-p({i}). The singleton
coefficient and queried influence are both

 a_k=binom(2k,k)/4^k;       p({i})=a_k^2,      Inf_i=a_k.

Consequently Phi_i/Inf_i=1/a_k-a_k is unbounded. An elementary bound is
a_k<=1/sqrt(k+1): the squared ratio a_(k+1)^2/a_k^2=(2k+1)^2/[4(k+1)^2]
is at most (k+1)/(k+2), since the difference after clearing denominators
is 3k+2>=0. Starting at a_0=1 proves the bound by induction. Thus the ratio
is at least sqrt(k+1)-1 and diverges. At k=1 the ratio is 3/2.
This does not refute full FEI or a stopping-tree payment from a global
unused bank. It refutes treating the new phase cost as a free local query
charge. Dummy queries give the same warning but are not needed here.

## Full original-reference transport without renewal

The full cross-entropy is better behaved than its excess over entropy. Put
G=CE(p,Qsym)-CE(p,Q), and C_b=CE(p_b,Q_b). The original, UNMODIFIED
reference has the exact identity

 CE(p,Q)=h2(v)+v CE(Ber(alpha),Ber(q_i))
          +w CE(g/w,qbar)+w-G.                                (9)

Here w-G is the nonnegative original conditional phase cross-entropy,
sum_{pairs,A} p(A)log((q(A)+q(A+i))/q(A)). Also
(C_0+C_1)/2=[h2(v_0)+h2(v_1)]/2+w CE(g/w,qbar).
The categorical root cross-entropy in (9) is at least the entropy of
(p(empty),m,w), which is at least h2(w). Concavity gives
h2(w)>=[h2(v_0)+h2(v_1)]/2. Therefore

 delta_i=CE(p,Q)-(C_0+C_1)/2 >=0.                              (10)

This retains the singleton debt, both full child terminals, and the original
phase reference. There is NO symmetrization reset in (9)-(10).
Each child's actual empty/nonempty mass is calibrated, so its FULL reference
is not simply the literal pushforward of the parent's FULL Q. That calibration
is explicitly paid: the categorical root term minus the average child binary
entropy is nonnegative. Only the nonempty reference q is projected unchanged;
no fresh reference table or influence allowance is supplied at a child.
After a queried set U, the nonempty child reference is exactly the original
q pushed forward by S -> S\U and conditioned on a nonempty image. This
depends on U, not on the observed bit values. Repeating (2) produces this
same law; no fresh prime table or posterior spectral reference is introduced.

For every finite adaptive restriction tree, including every stopping cut,

 sum_internal reach(h) delta_h
       + sum_leaves reach(h) CE(p_h,Q_h) = CE(p_root,Q_root).   (11)

All terms are nonnegative, so (11) is a single original account with old
debits preserved. It does not say that delta_h equals the true entropy
decrement. It does not bound an arbitrary root cross-entropy by influence.

## Complete original edge-occupation cost on unbounded-read cliques

Let C_n be the independent-set indicator of K_n, n>=3, f_n=1-2C_n,
lambda=1/(n-1), D=(1+lambda/4)^(n(n-1)/2)-1. Use the SAME complete
edge-occupation mass M from A014 stage5; no root/prime table is changed.
For every nonempty A of size k, put F_k=D M(A). The exact closed forms are

 F_(2r)=(2r)!/[2^r r!] * (lambda/48)^r,
 F_(2r+1)=(2r+1)!/[2^r r!] * (lambda/48)^r
                         *lambda(3n-2r-3)/96.                 (12)

In K_n[A], a maximal matching is perfect when k is even; when k is odd it
leaves exactly one vertex unmatched. Every untouched matched pair contributes
J(0,0)=1/2. An attachment to one endpoint replaces that by J(1,0)=1/12,
a factor 1/6. The unmatched vertex has n-k external choices of weight
lambda/32 and k-1 internal choices of weight lambda/8 times 1/6. This gives
lambda[(n-k)/32+(k-1)/48]=lambda(3n-k-2)/96, proving (12).

Let Z_F=sum_{k=1}^n binom(n,k)F_k, so the actual normalized reference is
q(A)=F_|A|/Z_F=M(A)/sum M. The complete normalizer is retained; D cancels
EXACTLY rather than being omitted as a free code constant.

For all k, log2(1/F_k)<=27n/4. Indeed, for even k=2r>=2,
(2r-1)!!>=r!>=(r/e)^r (integrate log x from 1 to r). Thus
log2(1/F_k)<=r log2(48e)+r log2((n-1)/r).
Using log2(e)<3/2, log2(48e)<15/2 and ln u<=u-1 bounds this by
6r+3(n-1)/2<=9n/2<=19n/4. For odd k>=3, (12) is the previous even term
times a factor at least 1/48, hence its logarithm is at most
19n/4+log2(48)<=27n/4. The case k=1 has F_1=1/32. Here log2(e)<3/2
follows from ln 2>2/3 by the positive atanh expansion, and e<3 implies
48e<144<2^(15/2). No asymptotic factorial estimate is used as an exact bound.

The full normalizer is bounded directly, without assuming a queue theorem.
The sum of the even terms, including k=0, is the matching polynomial of
K_n at weight lambda/48, at most (1+lambda/48)^(n(n-1)/2)<=exp(n/96).
For the odd terms, select the unmatched vertex first. Its factor in (12)
is <=1/32, and the remaining matching polynomial is <=exp(n/96).
Consequently

 Z_F <= (1+n/32)exp(n/96)-1 <=exp(n/24),
 log2 Z_F <=n/12,     log2(1/q(A))<=41n/6.                     (13)

The last inequality uses 27/4+1/12=41/6 and ln 2>1/2.

For this actual Boolean family,
s=(n+1)/2^n<=1/2, v=4s(1-s), I=n(n-1)/2^(n-1), and v/I<=4/n.
Since v>=2s>=2^(1-n), h2(v)<=v log2(e/v)<v(n+1/2)<=7nv/6.
Combining this with the ENTIRE nonempty reference expectation in (13),

 CE(f_n,Q_n)=h2(v)+sum_nonempty p_n(A)log2(1/q(A))
            <=8nv<=32 I(f_n).                                (14)

All entropy, root, matching, attachment and normalizer costs are included.
The k=|A| spectral coefficient is Chat(A)=(n+1-2k)/2^n, obtained by summing
the empty input and the n singleton inputs. This independently checks the
formula for s and the pivotal influence. The reference-cost conclusion is
stronger than a mere FEI conclusion for this already known threshold class;
no novelty claim is made for FEI on f_n itself.

Every variable belongs to n-1 positive edge terms, and all those size-two
minterms are necessary, so maximum read is unbounded in this representation
and in every positive DNF. Combining (11) and (14), ALL adaptive histories
and stopping cuts on this family retain their full original-reference
terminal costs and all booked delta debits inside the SAME 32I(f_n) account.
No bank is renewed at a child. This pays a complete original-reference
cost for one unbounded-overlap linear-hypergraph family.

## First unsupported line and exact scope

Pay the cumulative signed quantity consisting of the retained singleton
debt, phase cost, and reference-change cost, minus the actual JS credits,
from one UNUSED original influence account along a useful restriction
history on arbitrary overlapping graphs, while retaining both full terminal
reference costs. This is now paid for the clique family's original reference
by (11)-(14). The equations do not justify renewing a w allowance or resetting
a child reference to its own spectrum. For general linear hypergraphs the
first unsupported line is the dimension-independent bound on the ORIGINAL
normalized complete occupation expectation. Clique matching multiplicities
give (13); arbitrary induced subgraphs do not have that multiplicity bound.
The finite graph checks verify transport, not an all-graph occupation theorem.
