# A paid original pair still admits arbitrary Boolean cores

Finite uniform F_2 cubes, Boolean signs, normalized real Walsh coefficients; H uses bits. Put h(x)=-x^2 log2(x^2), h(0)=0. All terminals and original reaches are retained.

## 1. Consumed interfaces and scope of reconstruction

A052 RANK_PAIR_PROOF Section1: for parity minority costs m(v), greedy independent growth saturates their rank r(s) at every cost threshold s. Any basis has at most r(s) vectors below that threshold. Integrating the number above it gives the exact minimum a=integral_0^(1/2)(d-r(s))ds. Coordinate centering costs sum c_j, so release is character refund plus integral(r(s)-number of cheap coordinates)ds. This independently reconstructs the ownership formula, without changing its statement. Proposed dependent swaps cannot be added.

A002 RESET_LEDGER Sections1--2: for k>=2, p=2^-k, activation A_k(g)=1+1[z=0](g-1) has directional costs p w_g(u) on data and p(1-mu) on every direction involving controls. Physical disagreement gives w_g(u)<=1-mu. Threshold ranks therefore give a(A_k(g))=ell(A_k(g))=p[ell(g)+k(1-mu)]. This proves the mixed-basis step without assuming a split optimizer. Apply it separately to every actual child to get rho_A(A_k(g))=p rho_A(g)-p E(ell(child)-a(child)). The exact full entropy profile gives the signed mean-profile correction; it need not have a sign. This is a scoped independent reconstruction, not acceptance of the source census or other claims.

## 2. Construction; exact executable refund

Let f be any seed with H(f)>0. Select a finite full-affine minimum g, then remove all zero-influence coordinates. H(g)=H(f), q=I(g)<=I(f), and the squared spectrum of g has full affine span. A cheapest centered parity basis exists in the finite orbit; zero-cost vectors span the affine annihilator, so removing their constant labels leaves full span. Write h0=H(g)>0, mu=E g, |mu|<1.

Let Q(a,b,c,z)=(-1)^(ab+ac+bc+za). It is bent: H(Q)=4, I(Q)=2, E Q=1/4. For integer t>=1, let G_t=Q product_(j=1)^t g(x_j), and activate the WHOLE product on k>=2 new controls. Call the result F_(t,k), p=2^-k, v=mu^t. Query the ORIGINAL pair A=(a,b).

The four unactivated branches, ordered a+2b=0,1,2,3, are core, chi_c chi_z core, chi_c core, -chi_z core. Branch1 has character weight2; branches2,3 have weight1. Replace (c,z) in branch1 by the invertible physical substitution old_c=new_c+new_z, old_z=new_z. This changes chi_c chi_z to chi_c, leaves the core and controls intact, preserves the COMPLETE squared coefficient multiset, and releases exactly p influence. At original reach1/4 this gives executable release r_A=p/4. It need not be the complete affine optimum; no extra core release is booked.

Thus I_A(F)=p and I_A+r_A=5p/4. Every character-only child release is zero when k>=2: every marginal in an activated child is at most 2p<=1/2. Every terminal contains all t copies of g. None is pruned, including the branch with no Q character.

## 3. Exact profile, uniform control, and payment

Define R_k(u) by the exact activation identity H(A_k(w))=p H(w)+R_k(Ew):

R_k(u)=h(1-p(1-u))-p h(u)+p(1-p)h(1-u)
       +2kp[(1-u^2)+(1-p)(1-u)^2].

Root and all four reset terminal profiles are therefore

H(F)=p(t h0+4)+R_k(v/4),
I(F)=p[tq+2+k(1-v/4)],
H_0=p t h0+R_k(v), I_0=p[tq+k(1-v)],
H_b=p t h0+R_k(0), I_b=p[tq+1+k] for b=1,2,3.

All branches have reach1/4. Hence EXACTLY

L_A=4p+R_k(v/4)-[R_k(v)+3R_k(0)]/4,
D_K(F)+S_A^reset=L_A-(5K/4)p,
S_A^reset=E_b[K I_b-H_b].

The mean-profile term is retained, not dropped as a mixed refund. For -1<=u<=1, |h'(u)|<6; on 0<=u<=2, |h'(u)|<14 (endpoint limits included). These follow from |u ln|u||<=1/e on |u|<=1, ln2>2/3 and e>2. For x>=1, |h'(x)| increases up to its value 8+4/ln2<14 at x2. Since 1-p(1-u) is in[1/2,1], differentiating R gives

|R_k'(u)| <=p(26+12k).

The quadratic bracket derivative has absolute value at most6. The mean value theorem, also at u0 where h' extends continuously, implies the explicit uniform estimate

|L_A/p-4| <=(13+6k)|mu|^t.

For EVERY fixed K>16/5, set eta=5K/4-4>0. Whenever (13+6k)|mu|^t<eta, the displayed original pair plus this explicit reset is strictly paid at K. This includes K=15/4. This is an eventual all-dimensional theorem, not an extrapolation from finite checks.

## 4. Affine minimality, weakness and SAME-K hardness

Tensor products of affine minima remain affine minimal in their product chart: each parity bias factors, so its minority cost is at least the minority cost of each nonempty factor, hence at least each used coordinate cost. The minimum-basis criterion applies. Full affine spans add. Q and g are affine minima, so G_t is too; the directional argument of Section1 then makes F_(t,k) a full-span affine minimum as well.

Choose k=max(2,ceil(sqrt(t))). Then k=o(t), and (13+6k)|mu|^t tends to0. The elementary activation profile bound |R_k(u)|<=p(10k+20), uniform in |u|<=1, gives

H(F)/I(F) -> h0/q >= H(f)/I(f),
I(F) ->0, max_i Inf_i(F) ->0.

The error bound follows directly from |h(u)|<=1 on[-1,1], |h(1-u)|<=8 on[0,2], h(1-p(1-u))<=8p, and the quadratic bracket between0 and5. Exponential p dominates tq+2+2k. Both denominators are positive since h0,q>0.

Consequently, for each FIXED K>16/5 and each epsilon>0, FEI(K) restricted to full-affine-span affine-minimal roots with I<epsilon and one ORIGINAL proper pair paid by a genuine non-character refund implies full FEI(K) at the SAME K. The converse is immediate. The refund may be the explicit one above or the full affine optimum, since the latter can only increase available release. Seeds with H=0 satisfy FEI(K) directly. This endpoint is therefore no easier even after an actual local pair is paid.

## 5. Exact eligibility obstruction, not a critical embedding

If a canonical seed has d=h0-Kq>0, each of the FOUR explicit reset terminals obeys

H_b-K I_b >= p[t d-K(1+2k)-10k-20] >0

for all sufficiently large t. The same holds for the affine-optimized terminals, whose entropy is unchanged and influence no larger. Thus S_A^reset<0 and S_A^star<0. More precisely, when the root violates K and the pair is paid, the exact identity gives S_A^reset<-D_K(F)<0. A positive root deficit and genuine proper-child nonviolation cannot both hold here.

FIRST UNSUPPORTED UNIVERSAL LINE: at a least-essential-dimensional positive fixed-K witness, use NONNEGATIVE reserves of all smaller Boolean affine images to FORCE a paid original proper pair from the SAME unused bank, with complete terminal entropies and mixed interaction retained. Our embedding proves hardness of the paid-pair class; it does not embed arbitrary seeds into this critical eligibility hypothesis. A proof must exploit that hypothesis in the lower-funding direction, not just root minimality, weak influence or existence of one locally paid pair.

Analytic result and exact checks are author work pending independent-agent review. No full FEI bound, disproof or universal constant gain is claimed.

## 6. Concrete finite negative-bank certificate

Take g to be the eight-bit point defect (negative at one vertex only). Its mean is127/128, every nonzero directional influence is1/128, q=1/16, and its squared spectrum has full support. It is affine minimal by the all-direction minimum-basis criterion. Its exact entropy is h(127/128)+255h(1/128). Rational atanh logarithm bounds certify H(g)-(15/4)q>1/256.

Fix t=100000000, k=10000, K=15/4. This is a scalar certificate for an explicitly defined finite Boolean function, not a truth-table computation at that dimension. Bernoulli gives (127/128)^t<=128/(128+t). Therefore the signed pair is paid with margin

[K(I_A+r_A)-L_A]/p > 7633553/12500016 >0.

Every complete reset terminal has deficit at least

(H_b-K I_b)/p > 862405/4 >0.

The root also violates K by the corresponding root profile bound. Every further full affine optimization only increases a positive terminal deficit. No huge power or huge truth table was evaluated. This certificate supplies an actual positive-deficit, weak, affine-minimal paid-pair example excluded by smaller-child nonviolation; it is not an unbounded H/I family or a disproof of full FEI.
