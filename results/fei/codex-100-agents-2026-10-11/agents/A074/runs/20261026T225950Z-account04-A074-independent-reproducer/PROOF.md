# Independent reconstruction of A075's whole-row cancellation

Verdict: HOLDS unchanged for A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1,
statement digest ff1866ccd4bbad05ef7a28b12298c145b88c08656bdfa06c6bf6eaeb74af4698.
This is an analytic proof review with exact finite checks, not a Lean certificate.
Full FEI remains OPEN.

1. Fix any finite sign-valued outer h and disjoint finite uniform physical
cores g_j, with the original partition retained under restrictions. Constants,
zero-dimensional cores and dummy bits are allowed. Use entropy in bits and
eta(v)=-v log2(v), with eta(0)=0. Set

    L(x,y)=eta(x^2)+eta(y^2)-[eta((x+y)^2)+eta((x-y)^2)]/2.

The paired squared masses have equal total, so L(lambda x,lambda y)=lambda^2
L(x,y), including lambda=0. Pairing Fourier coefficients across one coordinate
gives H(g)-mean_b H(g_b)=sum_S L(ghat(S),ghat(S+i)). This holds for signed
coefficients and makes no assumption that individual rows are probability laws.

2. Write s=x^2+y^2. Then L=Phi(x^2,y^2)+J, where
Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), and
J=eta(s)-mean eta((x+/-y)^2). Both are nonnegative; concavity of eta applies on
all nonnegative masses, including masses larger than one. For xy nonzero,
ln(1+t^2)<=t for t>=0 follows by differentiating t-ln(1+t^2): its derivative
is (t-1)^2/(1+t^2). Apply it to |y/x| and |x/y| separately to obtain
Phi<=2|xy|/ln2. Cases x=0 or y=0 follow directly, without division.

For s>0, put z=2xy/s, so |z|<=1 and
J=s G(z)/ln2, G(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2.
On [0,1), the derivative comparison
atanh(z)<=z/sqrt(1-z^2) follows by differentiating again and comparing
(1-z^2)^(-1) to (1-z^2)^(-3/2); both original functions vanish at zero.
Integrating proves G(z)<=1-sqrt(1-z^2). Evenness and continuous endpoint
limits cover [-1,1]. The s=0 case is direct. Thus

    0<=L(x,y)<= (2/ln2)min(|x|,|y|)(|x|+|y|).

For Boolean g, mu=E g and t=ghat({i}) satisfy |mu|+|t|<=1, because mu+/-t
are actual conditional means. The derivative (g_+-g_-)/2 belongs to {0,+1,-1},
so |t|<=E |(g_+-g_-)/2|=d=Inf_i(g). Consequently L(mu,t)<=2d/ln2.
No variance is divided out; all deterministic output biases are included.

3. Write h=A+z_j D. After substituting all other cores, let a_W and d_W
be the uniform Fourier coefficients of A and D on those physical bits.
D takes values 0,+1,-1, so sum_W d_W^2=q_j, the actual outer pivotal
probability. A nonempty remaining frequency S of g_j yields a full coefficient
pair d_W(ghat(S),ghat(S+i)); its entire entropy decrement therefore sums to
q_j L(ghat(S),ghat(S+i)). The exceptional empty S instead yields
(a_W+mu d_W,t d_W). The nonempty rows cancel exactly between H(F) and
q_j H(g_j).

For k!=j, q_k is affine in the sign distribution of g_j, even at deterministic
biases. Its average under the two actual physical restrictions equals its
parent value. q_j itself is unchanged. Thus for C=H(F)-sum_k q_k H(g_k),

    mean C_child-C_parent
      =q_j L(mu,t)-sum_W L(a_W+mu d_W,t d_W)
      <=(2/ln2)q_j d=(2/ln2)Inf_i(F).

The last physical influence equality follows by counting the independent event
that the inner bit flips its output and the other outer outputs make j pivotal.
This includes q_j=0 and d=0. In particular zero physical influence has
nonpositive drift, even if other inner restrictions differ. The positive
atanh series at 1/3 gives ln2>2/3 and hence 2/ln2<3.

4. For every real K>=0 let rho_j be the finite stopping hull of
(H(g_j)-K I(g_j))_+. This is the least nonnegative majorant closed under every
conditional query average, defined by finite backward induction. Put

    U=C+kappa I(F)+sum_j q_j rho_j, kappa=2/ln2 or 3.

Influence satisfies I(F)-mean I(F_b)=Inf_i(F), so C+kappa I(F) is
superharmonic. It vanishes after full revelation; backward induction proves
it is nonnegative without assuming an entropy bound. Weighted hulls are
superharmonic: the queried q_j stays fixed; each other rho_k stays fixed
and mean q_k is conserved. Since I(F)=sum q_j I(g_j), U>=H(F)-K I(F),
and nonnegativity upgrades this to U>=(H(F)-K I(F))_+.

If actual incoming credit a>=U_parent is supplied, let
s=a-mean U_child>=0 and a_b=U_b+s. Then a_b>=0, mean a_b=a and each full
child is funded. A nonnegative owner label can be multiplied by a_b/a when
a>0; when a=0 both child totals vanish. For debit d_b=K I(F_b)-H(F_b)+a_b,
both d_b>=0. Old signed debit labels together with the new query label have
total T=mean d_b. If T>0 multiplying every label by d_b/T preserves the
conditional mean of each label and makes the child sum d_b. If T=0, both
d_b=0; the identity kernel preserves all cancelling signed labels. This
proves conditional conservation, not existence of initial capital. Admissions
that reveal nothing and keep the same decomposition leave U unchanged.
Changing the decomposition needs a separate theorem.

At the same state, partition, K and hulls, U_6-U_3=3 I(F) exactly. Its query
mean decrease is 3 Inf_i(F). Keeping actual arriving credit while switching
future allocation is allowed; refunding a previously spent donor is not.

5. The four-bit primitive is +1 except at assignments 8,9,10 (least significant
bit convention). For the fourth bit, mu=5/8 and t=d=3/8. Exactly

    L(mu,t)-2d=37/16-(9/32)log2(3)-(25/32)log2(5)>0,

because 2^74>3^9*5^25. Thus the stronger exceptional-row estimate fails for
an actual Boolean function; it does not refute a 2Inf bound for FULL drift.
The AND-of-OR(3,2,2) witness has positive full drift; its seven complete
query rows, including full constant/dummy children, satisfy the 3Inf reserve.

6. Implementation independence. reproduce.py obtains a binary multilinear
polynomial by finite differences, then expands b_i=(1-z_i)/2. If c_T are its
coefficients, ghat(S)=(-1)^|S| sum_{T superset S} c_T/2^|T|. This differs from
the producer's FWHT and row derivation. Inverse characters, Parseval, physical
edges, exact entropy differences, outer pivotal averages and stopping hulls
cross-check this conversion. No producer executable is imported or executed.
Equalities are rational prime-log profiles, not numerical tolerances.

For logarithms, z=(y-1)/(y+1) after dyadic reduction satisfies 0<=z<=1/3.
The first N=48 positive terms of 2 sum z^(2k+1)/(2k+1) form a lower bound;
the tail is at most 2z^(2N+1)/((2N+1)(1-z^2)). Ratio intervals with the
positive enclosure of ln2 bound log2 exactly. Strict signs stop at this fixed
precision; any unresolved sign aborts. All finite cases pass, but the universal
quantifiers are justified by steps 1-4, not by the finite domain.

7. First unsupported universal line: an absolute influence price for INITIAL
C+sum q_j rho_j on arbitrary indecomposable cores. Singleton physical-bit
cores have H=0 and rho=0, so U=H(F)+kappa I(F). Bounding this initial bank
by an absolute multiple of I would already prove FEI. Nothing above pays it.
