# Positive threshold regions: entropy domination replaces Fourier l1

Uniform independent physical inputs; entropy in bits. This is a supplied-threshold-theorem result, not full FEI. New scope is ONE live private profile on a genuine nonsubcube event. An inherited collision account can be retained only once already frozen; this does not transplant the two-active-profile collision identity to general masks.

## 1. Dimension-free domination of the mean spectrum

Write phi(t)=-t log2 t for t>=0, phi(0)=0, and g(a)=phi(a^2). For 0<=P<=1 and 0<=w<=4P, put x=w/P when P>0. Since phi(P)>=0 and phi(x)<=1/(Euler ln2)<1,

 phi(w)=x phi(P)+P phi(x)<=4 phi(P)+P.             (1)

If P0=0 then w0=0. Thus for a probability distribution P and nonnegative weights w dominated coordinatewise by4P, their UNNORMALIZED entropy is at most4H(P)+1. No number of coordinates and no Fourier l1 norm appear.

Let h and a=2*1_A-1 be Boolean functions on the same shared cube, with h=+1 on A. Replace h on A by any Boolean private profile V, independent of the shared inputs. Let mu=EV and q=(1-mu)/2 in[0,1]. The mean function m=E_private F=h-q(1+a). At every NONEMPTY shared frequency,

 mhat(S)=hhat(S)-q ahat(S).

P(S)=[hhat(S)^2+ahat(S)^2]/2 is a probability distribution. Cauchy-Schwarz gives mhat(S)^2<=2[hhat(S)^2+ahat(S)^2]=4P(S). Applying(1) on nonempty frequencies, then the standard entropy-of-a-mixture inequality and the bound g(mhat(empty))<=1, yields

 E:=sum_S g(mhat(S))<=2H(h)+2H(a)+6.              (2)

The mixture inequality H((P1+P2)/2)<=[H(P1)+H(P2)]/2+1 follows by introducing a fair label and dropping its nonnegative conditional entropy. All bounds hold for arbitrary Boolean h,a and arbitrary profile mean; no threshold theorem was used here.

## 2. Exact spectrum for an arbitrary positive event

Put p=Pr(A), J(A)=sum_S g(widehat(1_A)(S)), and

 U=p H(V), R=(Var(V)/2) J(A),
 Z=E+R-p g(mu)+1.                                (3)

For nonempty private frequency T, the COMPLETE Fourier coefficient is widehat(1_A)(S)*Vhat(T). The product identity g(ab)=b^2 g(a)+a^2 g(b), Parseval sum_S widehat(1_A)(S)^2=p, and sum_(T nonempty) Vhat(T)^2=Var(V) imply EXACTLY

 H(F)=E+p[H(V)-g(mu)]+Var(V)J(A)
     =U+R+Z-1.                                   (4)

Z>=0, since E,R>=0 and p g(mu)<=1. In particular the offset1 persists on every actual branch, including dead events, constant carriers and complete leaves. A codimension-c subcube has J(A)=2c p, so R recovers the previous c p Var(V) reserve exactly; replacing J(A) by codimension for a nonsubcube would be wrong.

Writing gamma=Ea=2p-1, the indicator entropy is

 J(A)=g(p)+[H(a)-g(gamma)]/4+2p(1-p)
     <=H(a)/4+3/2.                               (5)

At EVERY physical shared/private restriction use the actual cofactors h,A,V in(3). The structure is preserved. Equation(4) gives

 DeltaH=DeltaU+DeltaR+DeltaZ.                      (6)

For shared queries DeltaR may be signed; do not discard increases or claim a nonnegative consumed-influence payment. For private queries DeltaR=(J(A)/2)*Vhat({i})^2>=0. Every finite adaptive stopping tree telescopes(6), keeping the full U and terminal H. No suffix price or descendant FEI certificate is created.

## 3. Growing positive threshold regions and actual source ownership

Let d=2m+1>=5, h=+1 at shared Hamming weights<=m, and

 A={shared weight<=k}, 0<=k<=m-1.                 (7)

For k>=1 this event is not a subcube and its support size grows with d. At EVERY shared restriction both h_v and a_v are symmetric thresholds on r<=d bits. The supplied threshold_paper_38pp.txt pages1-2 Theorem A equation(6) gives H(threshold)<9 I(threshold). This is an external proof dependency, not proved by finite checks here. The maximum influence M_r=r max_j binom(r-1,j)/2^(r-1) is nondecreasing, since M_(2l)=M_(2l-1), M_(2l+1)=(2l+1)M_(2l)/(2l). Hence, with ORIGINAL I0=I(h)>=15/8>=1,

 H(h_v),H(a_v)<=9I0,
 E_v<=36I0+6,
 J(A_v)<=9I0/4+3/2,
 0<=Z_v<=(297/8)I0+31/4<=45I0.                  (8)

The boundary of A is weight k to k+1 and lies strictly inside h=+1. The original h boundary, weight m to m+1, is untouched. Physical edges therefore give exactly

 I_shared(F)=I0+q I(a)>=I0,
 I_private(F)=p I(V).                            (9)

No shared influence is issued again to a child. Thus the SAME numerical original carrier quota Q=96I0 from the previous stage is owned by ACTUAL ORIGINAL shared influence. For any independently valid inherited prefix with actual old shared booking0<=L<=58, define ONCE at its frontier

 Lambda=Q-L-Z.

Because I0>=15/8, L<=(464/15)I0; (8) gives

 Lambda>=(301/15)I0>=20I0,
 L+Z+Lambda=Q EXACTLY.                            (10)

Freeze Lambda thereafter. If an old collision account K has ALREADY been frozen, retain its same value in all descendants, together with FIRST and oldD0 as originally booked; no new K or donor certificate is issued. Equations(6),(10) pay every finite subsequent mixed tree, including event death, constant/nonconstant siblings and arbitrary stopping. The source inequality after combining an INDEPENDENTLY PAID prefix is

 H_root-EH_leaf+E(R+Z+Lambda+K)_leaf
 <=U_root-EU_leaf+R_root+Q+K_root+C P_private,prefix, (11)

where C P_private,prefix denotes the actual permitted old private payment (e.g.12 times consumed private influence ONLY if that prefix theorem applies). The precise prefix premise is a paid inequality using the SAME U and R of(3), the same inherited K, its full frontier H, and actual shared bill L; a payment with a different reserve is not sufficient without a separately checked conversion. L appears once as prefix payment and once as debit from Q; it is not erased. Without any prefix, use L0 and start directly from(6). This does NOT prove that the old two-profile5/15/38 prefix applies to this new mask, nor that an ACTIVE collision account transports through it. The inherited-prefix hypothesis is explicit and is not needed for original-root admission.

## 4. Fixed constant for all finite nonsubcube-event towers

Equations(2),(4),(5),(8), without any collision or prefix premise, imply

 H(F)<=pH(V)+(153/4)I0+15/2
      <=pH(V)+46 I_shared(F).                    (12)

The last step uses I0>=1 and (9). If H(V)<=C0 I(V), the EXACT physical partition(9) gives

 H(F)<=max(C0,46) I(F).                          (13)

Induction proves the SAME constant46 for EVERY finite acyclic tower of wrappers(7), starting with constants/characters, with fresh independent shared variables at each wrapper. No dependence on depth, event size, rarity or hereditary Fourier l1 norm occurs. This closes the nonpoint/nonsubcube tower class CONDITIONAL ON the supplied threshold theorem. It does not settle general FEI.

## 5. The Fourier l1 obstruction is genuinely removed

For A={weight<=m-1} on d=2m+1, fixing two shared inputs to0 makes its indicator the positive central-majority indicator on2m-1 inputs. Fourier l1 cannot increase under restriction (each child coefficient is a sum of two signed parent coefficients). For central majority on n=2l+1, its coefficient at degree2j+1 is

 (-1)^j alpha_n binom(l,j)/binom(2l,2j),
 alpha_n=binom(2l,l)/2^(2l).                     (14)

One proof takes a physical derivative: it is the middle-layer indicator on2l inputs; its degree2j coefficient is the middle-layer Krawtchouk coefficient. Double-counting subsets gives the coefficient in(14), since [z^(2j)](1-z)^l(1+z)^l=(-1)^j binom(l,j); odd terms vanish. Thus

 ||Maj_(2l+1)||_A
  =alpha_n sum_j [(2l+1)/(2j+1)]binom(l,j)
  >=alpha_n 2^l>=2^l/(2l+1).

The indicator norm is(1+||Maj||_A)/2. Consequently

 ||widehat(1_A)||_1>=2^(m-2)/(2m-1),              (15)

which divided even by d tends to infinity. Since I0<=d, no dimension-independent inequality ||widehat(1_A)||_1<=K I0 can fund these events. Our new Z bound does so by entropy domination, not by assuming this false l1 budget.

## 6. Honest first unsupported line

The entropy domination(1)-(2) and arbitrary-event spectrum(3)-(6) are universal one-profile facts. Admission(8) uses hereditary entropy certificates for BOTH the original carrier and event sign. For arbitrary A this is precisely an unpaid spectral-entropy certificate, not a consequence of influence alone proved here. For TWO active nonsubcube profiles, nonempty private Fourier rows mix two different mask spectra; their entropy no longer factors as(4), and the old point/parallel-face Xi/K identity is not available. The companion DISJOINT_MASK_PROOF.md now resolves that interference by a DIFFERENT universal conditional-spectrum bank and an explicit source conversion, enlarging the ORIGINAL quota from96I0 to240I0 and freezing the actual old balances unchanged. It does not prove active old-Xi transport or the same96I0 two-profile bound. The remaining universal gap is hereditary mask-entropy source admission and growing profile count. Full FEI remains OPEN; all new statements await independent review.
