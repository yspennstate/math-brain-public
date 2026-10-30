# A shared selector can move a logarithmic bill into a singleton

Author proof with exact checks passed; external mathematical review pending. Bits throughout.
Full FEI remains OPEN. No H/I counterfamily is claimed.

## 1. Exact target and the proposed extension being tested

For a Boolean function let P(S)=fhat(S)^2,
pi(S)=sum_(T containing S)P(T),
V(f)=sum_(S nonempty) P(S)log2(pi(S)/P(S)), and
G_V(f)=sum_physical_i[V(f)-average_b V(f|i=b)].
Zero terms are omitted. These are EXACTLY A022@9's nonempty upper-set
quantities, not Fourier entropy substituted for V.

A022@9 GU_PROOF Section7 represents two adjacent controlled edits with
an actual shared selector h(y,z)=a(z) or epsilon c(z). It explicitly leaves
the singleton J_y(h) and its signed changes unpaid. We test the NATURAL
but UNPROVED extension

       G_V(F)<=2delta G_V(h)+K I_DATA(F),                 (N)

with ONE combined-selector owner and a dimension-independent K. We prove
(N) FALSE for every fixed K>=0. This refutes no assertion A022@9 claims
proved. In particular the one-point stable256 transfer remains untouched.

Set t=2,k=6,delta=1/64, b(x)=g(x_0,x_1,x_2)g(x_3,x_4,x_5),
g=-1 at000 and +1 elsewhere. Then b(0)=+1 and b(e_0)=-1.
For ANY odd n=2m+1,m>=1, let a_n be balanced majority on n controls,
and form the ACTUAL Boolean function

 F_n(x,z)=b(x)a_n(z) when x is0 or e_0, and b(x) elsewhere.

Both adjacent edits use the SAME controller. Their epsilon is -1, so the
actual shared selector is h_n(y,z)=(-1)^y a_n(z). DATA and controls are
independent uniform cubes. Bit notation0/1 is equivalent to the specified
uniform sign cube by the usual Walsh characters.

## 2. Exact vacuum-migration identity for the original owner

For ANY controller a, multiplication by a fresh character shifts every
spectral set to one containing y. Therefore U(y*a)=U(a), V(y*a)=U(a).
If a is balanced, the physical y increment of V is zero and
G_V(y*a)=G_U(a). Write phi(u)=-u log2 u. Each original controller child
has mean +/-ahat({j}), whereas the parent has mean zero. Consequently

 G_V(a)-G_V(y*a)=sum_j phi(ahat({j})^2).                  (1)

At the root V(a)=V(y*a) and J_y(y*a)=phi((Ea)^2)=0. Both root values
therefore conceal the positive child singleton debt in(1).

For majority, every singleton magnitude is exactly
d_m=binom(2m,m)/4^m and every child mean is +/-d_m. Thus the missing
owner cocycle is n phi(d_m^2), not a function bounded by root J_y.
The recurrence d_(m+1)=d_m(2m+1)/(2m+2) proves, by squaring,

 1/(4m)<=d_m^2<=1/(2m+1),  m>=1.                        (2)

For the lower bound start d_1^2=1/4 and compare squared ratios to m/(m+1).
For the upper start d_0=1 and use
(2m+1)(2m+3)<4(m+1)^2. Hence n d_m^2 lies in[1/2,1], d_m<=1/2,
and

            n phi(d_m^2)>= (1/2)log2(m+1).               (3)

These are all-m inequalities, not a finite-width extrapolation.

## 3. Exact output split and a uniformly bounded smooth remainder

Let H_S=bhat(S). For a controller of mean s the empty-controller
amplitudes and COMPLETE DATA marginal are

 A_S(s)=H_S+2delta(s-1)1[0 in S],
 M_S(s)=A_S(s)^2+4delta^2(1-s^2)1[0 in S].

Every nonempty controller row has amplitude2delta ahat(T) on DATA
frequencies containing0 and zero on the other half. Summing its upper-set
term over the other five fair DATA frequencies gives EXACTLY
2delta V(a)+5delta(1-s^2). Let Z_S=sum_(R containing S)M_R and

 T(s)=sum_(S nonempty) A_S(s)^2 log2(Z_S/A_S(s)^2)
                                      +5delta(1-s^2).

Then, with the global empty frequency removed,

                  V(F)=2delta V(a)+T(s).                (4)

No cross row was replaced by independent controller copies. The special
DATA bit is forced to be present, as in A022's destructive-cancellation
interface. Since b(0)+b(e_0)=0, the global mean stays9/16.

The COMPLETE M_S, hence every Z_S, is affine in s. On |s|<=1/2,
all p_S=A_S^2>=delta^2=1/4096. Indeed H_S for0 in S is either
4delta or -12delta, and unchanged amplitudes have magnitude>=4delta.
For the two changed row types M_S/delta^2 is respectively8(1+s)
or200-56s. Thus |M'_S|/M_S<=2; averaging gives |Z'_S|/Z_S<=2.
Also Z>=p, Z<=1, sum p<=1, sum p''=1/16 and
sum p'^2/p=1/8. Direct differentiation of E=sum_(S nonempty)p log(Z/p)
gives

 E''=sum p''log2(Z/p)-c sum p''
                -c sum[p'/sqrt(p)-sqrt(p)Z'/Z]^2,
 c=1/ln2<3/2.

Since log2(Z/p)<=12, square<=2sum p'^2/p+2sum p(Z'/Z)^2,
subtracting the second derivative10delta of5delta(1-s^2) proves

                -13<T''(s)<1, |s|<=1/2.                (5)

In detail the lower bound is -101/8>-13 and the upper is19/32<1.
No endpoint singularity is discarded; all actual majority child means
lie in this compact interval of nonzero amplitudes.

Therefore the TOTAL CONTROL remainder
S_m=n[T(0)-(T(d_m)+T(-d_m))/2] lies in[-1/2,13/2], by(2).

For each DATA query, the coefficient2delta V(a) in(4) cancels in
expectation. Querying bit0 separates two one-point children, each of
density2delta; querying another bit keeps the pair only in one child,
with density2delta and half the reach. All remaining terms depend only
on s. Thus TOTAL DATA drift at s=0 is a fixed number Dstar, independent
of the width/profile of a. Compute it on the representative dictator a=z.
Its root has7 bits and children have6, while0<=V<=H<=dimension. Hence

                       -36<=Dstar<=42.                  (6)

Together(1),(4)--(6) give the exact residual

 G_V(F_n)-2delta G_V(h_n)
        =2delta n phi(d_m^2)+S_m+Dstar
        >=delta log2(m+1)-37.                           (7)

The DATA influence is at most6. Thus (7) defeats EVERY fixed K in(N).
An explicit256 witness is m=2^100736,n=2^100737+1: the residual is at
least1537, while256 I_DATA<=1536. This is an exactly defined actual
Boolean function, not a floating spectral distribution or a searched
large truth table. Its existence is proved by(1)--(7).

Adding any fixed multiple of root J_y(h_n) to(N) cannot repair it: that
term is identically zero. This is a potential/owner counterfamily, NOT
a proof that H(F_n)/I(F_n) diverges and NOT a disproof of FEI.

## 4. A retained singleton repairs this SAME family at the SAME256 rate

The correct marked-sector owner is W_y(h)=V(h)-J_y(h), which equals
V(a) for h=y*a. Its signed control drift is G_V(a), not G_V(h).
After querying the marked bit y, descend to V of the remaining controller; before that query retain the mark in both control children. Thus the marked y increment is zero. For the family above, (4)--(6) imply

             -37<=G_V(F_n)-2delta G_V(a_n)<=49.          (8)

The probability F differs from b is delta, since majority is balanced.
For each DATA bit |Inf_i(F)-Inf_i(b)|<=2Pr(F!=b); hence
I_DATA(F)>=3/2-12delta=21/16. Consequently

             G_V(F_n)<=2delta G_V(a_n)+256 I_DATA(F_n).  (9)

Thus the omitted singleton cocycle is exactly the growing bill; this
same family remains within the256 transfer with the original marked
controller owner. It obstructs dropping a signed vacuum-sector debt,
not every adjacent-edit extension or a universal upper-set approach.

## 5. Checks and first unsupported universal line

Frozen finite checks cover n3,5,7 (total bits9,11,13), exact Walsh spectra,
EVERY physical coordinate of F and h, exact upward tails and rational-log
identities in(1),(4),(7),(8),(9). A separate direct-character implementation
reconstructs n3 and checks the same residual with no production import.
The FWHT checker passed 37 assertions on n3,5,7 (12.6894 seconds). The
separate direct-character checker passed 790 assertions, including m1..256
exact central-binomial recurrence and squared bounds (1.4606 seconds); the induction above proves ALL m.
They verify identities and repair at small widths; they do NOT enumerate
the astronomical256 witness or infer divergence from finite data.

First unsupported universal line: for TWO arbitrary dependent controllers,
pay the full signed marked singleton/sector cocycle and its changes after
both physical outcomes from ONE original compatible owner at a stable
rate. A root-only J credit, or replacement of that owner by an unmarked
V(h), is insufficient by(7). Arbitrary original owner eligibility and the
universal G_V criterion remain unproved. Retain both child sectors and
their terminal debts; no fresh controller entropy or source influence
is allocated by this counterfamily argument.
