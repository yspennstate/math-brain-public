# Distinct dependent controllers still require the marked singleton owner

Author proof with exact checks; independent-person review pending. All logarithms are base two. Put
U(f)=sum_S P_f(S) log2(pi_f(S)/P_f(S)), V(f)=U(f)-phi((Ef)^2),
phi(u)=-u log2 u, pi_f(S)=sum_(T containing S)P_f(T), and
G_V(f)=sum_i[V(f)-(V(f|i=0)+V(f|i=1))/2].
Zero summands are zero. The functional V is not variance.

## 1. Actual Boolean family and exact comparison

Let g on three bits be negative only at000. Set b=g tensor g on six bits,
delta=1/64, v=0, u=e0; then b(v)=1 and b(u)=-1. For any odd n=2m+1,
m>=1, let a=Maj_n(z) and take a fresh fair bit w in sign notation.
Define F=b*a on x=v, F=b*a*w on x=u, and F=b elsewhere.
The two raw controllers a and a*w are distinct and depend on the same z.
Their normalized shared mux is h(y,z,w)=a(z) when y=0, -a(z)w when y=1.
DATA means the six original x coordinates. The source controllers use z,w.
The seven fixed carrier variables (x,w) are an algebraic grouping only;
w is not allocated a second DATA payment.
The comparison under test is

  G_V(F) <= 2delta G_V(h) + K I_DATA(F).                 (N*)

This is an unproved extension of A021's unmarked-owner rule, not a claim
made proved by A022. We show that no fixed K>=0 works in (N*).
The root marked singleton J_y(h) is zero, so adding K' J_y(h) cannot help.

## 2. Fixed carrier decomposition and the logarithmic term

Write F=B(x)+a(z) C(x,w), where
B=b-1[x=v]+1[x=u], C=1[x=v]-w 1[x=u].
The physical supports of B,C are disjoint, B^2+C^2=1, and
||C||_2^2=2delta. With S an x Fourier set and W indicating w,
Bhat(S,0)=bhat(S)-delta+delta(-1)^(0 in S), Bhat(S,1)=0,
Chat(S,0)=delta, Chat(S,1)=-delta(-1)^(0 in S).
Thus Chat^2 is uniform on all 128 fixed-carrier sets, each mass delta^2.
Its upper-set functional is U_C=7delta. The part with w present has
mass delta and U_C,w=3delta.

For an arbitrary Boolean a of mean s, empty-z amplitudes are A=Bhat+s Chat
and complete fixed-carrier marginal M=Bhat^2+2s Bhat Chat+Chat^2. Let Z be its
upward tails. Nonempty-z rows factor exactly, giving

  V(F)=2delta V(a)+delta phi(s^2)+T(s),                 (1)
  T(s)=E0(s)+7delta-4delta s^2,
  E0(s)=sum_(S nonempty x sets) A(S,0)^2 log2(Z(S,0)/A(S,0)^2).

Indeed the w-present empty-z rows contribute
delta phi(s^2)+3delta s^2. Both global empty coefficients are removed
in (1). No independent-copy approximation is used.

For |s|<=1/2, the unchanged Bhat magnitudes are at least4delta and
the changed ones at least2delta; |Chat|=delta, hence p=A^2>=delta^2
in E0. The DATA norm of A is <=1, Z<=1, and Z>=p. Also
|Z'/Z|<=2: each affine M satisfies |M'|/M<=2 by 2|BC|<=B^2+C^2.
Summing over E0's rows, sum p''<=1/16 and sum p'^2/p<=1/8.
For c=log2(e)<3/2 (the positive atanh series gives ln2>2/3), exact differentiation yields

 E0''=sum p'' log2(Z/p)-c sum p''
       -c sum[p'/sqrt(p)-sqrt(p)Z'/Z]^2.

Since log2(Z/p)<=12, these estimates give E0''>=-399/32 and
E0''<=3/4. Subtracting8delta=1/8 proves |T''|<14.
All denominators are strictly positive on the entire stated interval.

## 3. The all-dimensional residual

For majority let d_m=binom(2m,m)/4^m. Its mean is zero; all singleton
coefficients have magnitude d_m, and every z child has mean +/-d_m.
The recurrence d_(m+1)=d_m(2m+1)/(2m+2) proves
1/(4m)<=d_m^2<=1/(2m+1), hence nd_m^2<=1 and
n phi(d_m^2)>=(1/2)log2(m+1). These are the same elementary bounds
as A021 Section2, with positive denominators m>=1.

Write h=a*l on disjoint cubes, with l(y,w)=1 at y=0 and -w at y=1.
Its spectrum is uniform on four atoms. Thus U(l)=1, G_U(l)=2,
(El)^2=1/4. Tensor tails multiply, so U(a*l)=U(a)+U(l).
At the balanced root, summing all physical h coordinates gives

 G_V(h)=G_U(a)+2+n phi(d_m^2/4),
 G_V(a)=G_U(a)+n phi(d_m^2).

From (1), the total z drift of F is
2delta G_V(a)-delta n phi(d_m^2)+S_m,
S_m=n[T(0)-(T(d_m)+T(-d_m))/2], |S_m|<=7.
For each fixed-carrier restriction at the balanced root, the coefficient of V(a)
is the child's ||C||^2; its two-outcome mean is the parent's ||C||^2.
That term cancels. The rest depends only on the fixed B,C spectra.
Consequently total (x,w) drift Dstar is independent of n and is obtained
with the representative a=z. Root dimension8 and child dimension7 give
-49<=Dstar<=56 from 0<=V<=H<=dimension.

Using phi(t/4)=phi(t)/4+t/2 now gives the exact identity

 G_V(F)-2delta G_V(h)
  =(delta/2)n phi(d_m^2)-delta n d_m^2+S_m+Dstar-4delta. (2)

Therefore the residual is at least

 (1/256)log2(m+1)-57.                                (3)

Since I_DATA(F)<=6, every fixed K>=0 fails. Explicitly for real K take
M=ceil(256(6K+58)), m=2^M and n=2m+1; (3) is >6K.
This specifies an actual finite Boolean function for every K, without
claiming to enumerate its astronomical truth table. Root J_y(h)=0
because Ea=0, although its descendants have nonzero singleton debt.

## 4. The marked owner repairs this distinct-controller family

Keep the mark on y until it is physically queried. Before that query use
W_y=V-J_y; after it retain the full V of BOTH actual controller children.
Call the resulting root signed sum G_mark(h). At our balanced root J_y=0.
Each z child has J_y=(d_m^2/4)log2(2/d_m^2); both w children have J_y=0.
The y query keeps both full controller terminals. Consequently

 G_mark(h)=G_V(h)+(n/4)phi(d_m^2)+n d_m^2/4.

Subtracting this correction from (2) cancels its entire logarithmic term:

 G_V(F)-2delta G_mark(h)
   =-(3delta/2)n d_m^2+S_m+Dstar-4delta <=63.           (4)

Since I_DATA(F)>=21/16, equation(4) proves
G_V(F)<=2delta G_mark(h)+256 I_DATA(F) for EVERY odd n>=3.
This uses the SAME marked source and both terminals, with no renewed
source allowance. It settles only this distinct dependent-controller
family, not all arbitrary dependent pairs or all adaptive descendants.
In particular G_mark is a marked transition functional, not the unmarked
G_V of a single Boolean function; replacing the two is exactly the error.

## 5. Scope and a bounded entropy ratio

At a balanced root the Fourier rows split into the disjoint z-empty B
sector of mass1-2delta and nonempty-z C tensor a sector of mass2delta.
The normalized B spectrum uses at most64 atoms; the C spectrum is uniform
on128 atoms. Hence exactly
H(F)=h2(2delta)+(1-2delta)H(P_B/(1-2delta))
      +2delta[7+H(a)] <=7+2delta H(a).
The last estimate uses h2(1/32)<=7/32 (proved by the binomial integer
inequality 32^32<=2^7*31^31), so the constant part is <=7.
I(F)=I_DATA(F)+delta[2I(a)+1], where the extra delta is the actual w
influence, charged once as controller influence. Also Pr(F!=b)=delta, so the six old DATA
influences sum to >=I(b)-12delta=21/16. The threshold paper's
Theorem A gives H(a)<9 I(a). Thus H(F)/I(F)<9+16/3<15.
The finite checks need not assume this threshold bound to verify (2).

Only (N*) and any addition priced solely by root J_y are refuted. No FEI
constant, essential-coordinate rule, signed marked-owner rule, or universal
upper-set route is refuted. Replacing G_V(h) by an actual marked-sector
owner can retain the missing cocycle. Its eligibility and payment from ONE
original unused source, for arbitrary dependent controllers and all children,
remain unpaid. Independent-person review is pending.
