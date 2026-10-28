# Independent reconstruction: singleton transfer and source-only obstruction

Uniform finite cubes and bit entropy throughout. Exterior and internal coordinates are disjoint; K and C can depend on exactly the SAME exterior coordinates. C is an indicator, K vanishes on C and is a sign off C. F=K+Cg is Boolean for any Boolean internal g. No claim below closes full FEI.

## 1. Arbitrary-bias transfer, including zero endpoints

At internal coordinate i write g=A+x_i B, mu=Eg, beta=E B=ghat(i), t=Inf_i(g). For each nonempty remaining internal frequency T, the physical pair of Fourier amplitudes of F is Chat(s)(Ahat(T),Bhat(T)). At T empty it is (Khat(s)+mu Chat(s),beta Chat(s)). The homogeneous packet Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b) therefore gives exactly

 B_i(F)=c B_i(g)-c Phi(mu^2,beta^2)+S,
 S=sum_s Phi((Khat(s)+mu Chat(s))^2,beta^2 Chat(s)^2).             (1)

No latent independent copies or selector law appear. Actual influence is ct, by physical edges. When c=0 there is no internal dependence. When beta=0, S is zero, including zero Chat rows; avoid every logarithm at zero. At c=1 K=0 and (1) reduces to B_i(g).

For beta nonzero and positive Chat rows, P_s=Chat(s)^2/c is a probability law by indicator Parseval. The elementary inequality Phi(a,b)<=b[1+ln(1+a/b)]/ln2 follows by writing Phi=b ln(1+a/b)+a ln(1+b/a) and ln(1+u)<=u. Jensen in P and Parseval, using KC=0 pointwise, imply

 S<=c beta^2[1+ln(1+(1-c+c mu^2)/(c beta^2))]/ln2
  <=c beta^2 log2(1/c)+c[(1+ln2)beta^2+2beta^2 ln(1/|beta|)]/ln2. (2)

Omitting Chat=0 rows only decreases the squared numerator norm. No exterior independence is needed. Since B is in {0,+1,-1}, |beta|<=E|B|=t. Thus beta^2<=t and beta^2 ln(1/|beta|)<=t/exp(1), including the limiting beta=0 case.

The actual entropy decrement is D_i=B_i+J_i. For real amplitudes a,b, put v=a^2+b^2 and r=2ab/v. In natural units the JS contribution is v[(1+r)ln(1+r)+(1-r)ln(1-r)]/2. Its bracket is nonnegative and at most 1-sqrt(1-r^2): differentiate to compare atanh(r) with r/sqrt(1-r^2), whose difference has nonnegative derivative for r>=0, and use symmetry. Hence J_i<=2 sum b^2/ln2=2ct/ln2. Dropping the subtracted nonnegative packet in (1) yields

 D_i(F)<=c B_i(g)+c beta^2 log2(1/c)+A ct,
 A=1+(3+2/exp(1))/ln2<7.                                    (3)

The strict constant follows from exp(1)>2, ln2>2/3. The latter follows from the positive atanh expansion with argument1/3. This reconstructs A059's general local transfer, without changing its statement. Private-list constants and all-history DATA/controller imports are NOT proved by (3).

## 2. Once-only variance payment and source allocation

Under the two fair restrictions child means are mu+beta and mu-beta. Consequently Var(g)-E Var(g_child)=beta^2. On EVERY finite adaptive physical stopping tree, the exact weighted sum of these nonnegative drops is Var(g_root)-E Var(g_leaf). This is a telescoping equality; stopping need not be complete, and actual child variances are retained. For fixed exterior C, the reserve c log2(1/c)Var(g) pays all descendant singleton-density bills, with its literal terminal residual. Parity3 has zero initial singleton coefficients but variance1, proving that frozen initial singletons cannot replace the updated reserve.

For even m>=4 take paired-quadratic bent b, C=1_(z=0), c=2^-m, s=sqrt(c), K=b-C. Its Fourier amplitudes are s times signs (the two-bit identity tensorizes), Eb=s, b(0)=1. Use actual source W_0=g, W_1=K+Cg on fresh X. Direct disagreement gives

 d_X=[1-c-mu(s-c)]/2>=(1-s)/2>=3/8.

Every physical entropy decrement lies in [0,2] bits: erasure is a binary conditional entropy<=1; JS is nonnegative and<=1 by the same scalar bracket's maximum ln2 and Parseval. The root-weighted new ticket is cm Var(g)/2<=1/8: m2^-m decreases for integer m>=4, and equals1/4 at m4. Thus

 D_X+E ticket<=17/8<=(17/3)d_X,
 6d_X-D_X-E ticket>=d_X/3.                                  (4)

This pays the actual old source debit and the newly allocated density reserve ONCE. At an inherited internal history g means that actual restricted function. It neither renews the old internal ticket nor pays exterior queries. We accept only this elementary source budget in the larger A059 claim; its assembled stopping theorem remains conditional on its stated fine-controller/DATA imports.

## 3. Sharp coefficient and full reserve necessity

Fix any finite Boolean g as m grows. For beta nonzero, each row of (1)'s S has a=[s epsilon+(mu-1)c]^2>=c(1-2s)^2>=c/4 and b=beta^2 c^2. Phi(a,b)>=b log2(a/b). Summing the 1/c rows gives

 S>=c beta^2[m-2-log2(beta^2)]>=c beta^2(m-2).

Equation (2) gives S<=c beta^2 m+O_g(c). In (1) all other terms are O_g(c), and 0<=J_i<=2ct/ln2. For beta=0 the same conclusion is exact up to O_g(c). Hence

 lim_even_m [D_i(F_m)-c B_i(g)]/(cm)=beta^2.                  (5)

For a fixed finite complete internal query tree, apply (5) to its finitely many actual restrictions and telescope FULL physical entropies. The sum of weighted beta^2 is Var(g), not root singleton energy. The terminal is b when the revealed g is+1, and b-2C when it is-1. Thus

 lim_even_m {H(F_m)-[(1+mu)H(b)+(1-mu)H(b-2C)]/2}/(cm)=Var(g). (6)

For incomplete trees the limit is Var(g)-E Var(g_leaf), retaining actual wrapped leaf entropies. No interchange of infinite query trees and limits is used; g and its finite tree are fixed. Any coefficient below1 plus a fixed A cI(g) fails by (5) or (6) at sufficiently large even m. This is a sharpness statement for the stated density payment, not a Boolean unbounded H/I family.

## 4. Independent source6 exterior obstruction, all even m

Set g=+1, so W_0=1,W_1=b; internal influence, fine U/R and variance reserves vanish. Reveal X. Only on the X=1 branch reveal exterior bit0. Both exterior children are a literal times bent(m-2), so each has entropy m-2, while H(b)=m; the actual root-weighted second debit is1. The X=0 terminal is retained with entropy0.

Direct Fourier transformation of W gives empty-exterior squared amplitudes (1+s)^2/4,(1-s)^2/4 and 2(1/c-1) other squared amplitudes c/4. Therefore, with

 G(s)=(1+s)^2 ln(1+s)+(1-s)^2 ln(1-s),
 D_X=2-cm/2-G(s)/(2ln2),
 Delta_m=D_X+1-6d_X=3s-cm/2-G(s)/(2ln2).                     (7)

G(0)=G'(0)=0 and G''(s)=6+2ln(1-s^2)<=6, so G(s)<=3s^2. For even m>=4, ms<=1 (the ratio from m to m+2 is (m+2)/(2m)<=1), s<=1/4 and ln2>2/3. Hence

 Delta_m>=s[3-ms/2-3s/(2ln2)]>(31/16)s>0.                  (8)

This preserves the actual old source debit and all full terminals; it supplies no internal reserve to raid. At m4 the actual spectrum is {25/64,9/64,thirty1/64} and the terminal average after both queries is1, so

 Delta_4=11/4-[25log2(25)+9log2(9)]/64>49/100,

as certified by outward rational logarithm intervals. Since d_X=3/8, the enlarged policy's source-only rate must exceed73/10. An originally funded exterior-influence account could cover the added debit (for this constant fallback, rate4 times its root influence1/4 pays exactly1: a bent coordinate has influence1/2 and the rare branch has weight1/2); no such account is created by this obstruction. A larger original source rate is also not excluded. In an explicitly additive factor ledger, fixed-m tensorization multiplies the positive deficit, so a fixed global additive entropy allowance cannot repair source6. Influence-proportional or per-factor funding survives tensorization.

## 5. Honest first unsupported line

An exterior query changes the conditional wrapper C,K and c. Concavity of c log2(1/c) proves nonnegative expected density-reserve release but gives no sufficient lower bound for the physical entropy/profile cost after earlier debits. Source6 alone is REFUTED for that extension, even at zero old internal debit. The remaining target is to use genuinely unspent ORIGINAL exterior capacity through one exterior query after a nonzero internal debit, retaining the original bank, actual U/R/variance remainders and BOTH full terminals. Generic inherited core and terminal entropy remain unpaid. Full FEI is OPEN.
