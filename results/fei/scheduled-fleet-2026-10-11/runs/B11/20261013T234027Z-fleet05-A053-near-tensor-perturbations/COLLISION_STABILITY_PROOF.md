# Point surgery preserves signed collision with a dimension-free error

Uniform finite cubes, Boolean signs, and entropy in bits throughout. A is a nonempty proper physical block, a=|A|, d=2^a, m=n-a. Use A051's row notation w_t(x)=hat(f_x)(t), q_t=E_x w_t(x)^2, B_A=H(S_A|S_C), Gamma_A=sum_t q_t log2(E w_t^4/q_t^2), and V_A=B_A+Gamma_A. Zero rows contribute zero. This proof reconstructs the needed row facts; no unproved universal FEI bound is a premise.

## 1. A joint-law Lipschitz bound with no retained-alphabet dependence

Put P(x,t)=w_t(x)^2/d. This is a probability law. For an arbitrary probability law P with d possible x values define

    G(P)=sum_t q_t log2(d sum_x P(x,t)^2/q_t^2), q_t=sum_x P(x,t).

Thus G(P_f)=Gamma_A(f). For a positive row, write r_x=P(x,t)/q_t and s=sum r_x^2. Differentiating its homogeneous summand gives

    partial G/partial P(x,t)=log2(d s)+(2 r_x/s-2)/ln 2.

We have 1/d<=s<=1 and r_x/s<=(sqrt(d)+1)/2. To prove the latter, set u=r_x and use s>=u^2+(1-u)^2/(d-1); maximizing the resulting ratio gives u=1/sqrt(d). Hence every partial derivative lies in the same interval

    [-2/ln 2, a+(sqrt(d)-1)/ln 2].

If two probability laws differ by total variation delta, integration along their line segment, using the zero total mass of the derivative direction, proves

    |G(P)-G(Q)| <= [a+(sqrt(d)+1)/ln 2] delta.                 (1)

Zero entries in a positive row pose no problem for the displayed derivative. An entirely zero row can be handled by adding the same positive full-support law to both endpoints with weight epsilon, proving (1), and letting epsilon decrease to zero. Each row summand is between 0 and a q_t, so continuity at a zero row is explicit. The bound is independent of the number of retained rows. It does not replace signed row convolutions by absolute convolutions.

## 2. One-point surgery: Gamma has a uniform O(2^(-n/2)) modulus

Let g=f-2 f(v)1_v and p=2^-n. Only physical assignment v_A changes. The edited m-bit child's normalized amplitude vectors have inner product 1-2*2^-m. For unit amplitude vectors u,v, Cauchy--Schwarz applied to (u-v)(u+v) gives TV(u^2,v^2)<=sqrt(1-<u,v>^2). Therefore

    delta_Q=TV(P_f,P_g)<=2^-a * 2 sqrt(2^-m(1-2^-m)).

Combining with (1),

    |Gamma_A(g)-Gamma_A(f)| <= rho_(n,a)
      :=[a+(2^(a/2)+1)/ln 2]2^(1-a) sqrt(2^-m(1-2^-m))
      <10 sqrt(p),                                                (2)

for EVERY proper block, uniformly in its size. For the last constant, divide by sqrt(p): the expression is at most 2a*2^(-a/2)+(2+2*2^(-a/2))/ln 2. The elementary induction a<=2*2^(a/2), 2^(-a/2)<=1/sqrt(2), ln2>2/3, sqrt2<3/2 bounds it by 4+21/4<10. For a=1,2,3 the induction's bases hold; the step a->a+2 uses a+2<=2a for a>=2, and a=1->3 is checked directly. The inequality ln2>2/3 follows from ln2=2 atanh(1/3)>2/3.

This controls Gamma rather than the unlogged averaged fourth-moment C_A. Small row masses cause no denominator hypothesis in (1) or (2).

For n>=4 let u_n=2^(1-floor(n/2))<=1/2. Parent spectral TV is at most 2 sqrt(p(1-p))<=u_n. The conditional-entropy common-mixture argument proves

    |B_A(g)-B_A(f)|<=a u_n+h2(u_n).

Indeed decompose the two joint spectral laws into their common mass and residual laws; conditional entropy is between the weighted conditional entropies and that quantity plus the binary mixing entropy. The conditional entropy of the queried alphabet ranges between 0 and a. No bound on the retained alphabet is used. Consequently

    |V_A(g)-V_A(f)| <= Omega_(n,a):=a u_n+h2(u_n)+rho_(n,a).       (3)

Each queried influence changes by at most 2p. A fixed-price slack K I_A(f)-V_A(f)>Omega_(n,a)+2K a p, K>=0, implies V_A(g)<K I_A(g). If I_A(f)>2ap, the normalized cost is at most [V_A(f)+Omega]/[I_A(f)-2ap]. Equality without slack is not claimed; A053's parity boundary remains valid.

## 3. Direct product-phase approximation avoids large fourth-moment error

More generally let F=h(x_A)k(x_C) be a Boolean product and G any Boolean function with disagreement probability epsilon. Put r_t=hat k(t), and choose the Boolean row phase b_t=sign(r_t)h when r_t!=0, arbitrary Boolean b_t otherwise. The unnormalized rows satisfy W_t=sqrt(q_t) b_t. For rows W'_t of G, set q'_t=E(W'_t)^2. The reverse triangle inequality gives

    ||W'_t-sqrt(q'_t)b_t||_2 <=2||W'_t-W_t||_2.

For zero old rows the same inequality holds for any b_t. Parseval in the retained coordinates therefore gives

    sum_t q'_t ||W'_t/sqrt(q'_t)-b_t||_2^2 <=4||G-F||_2^2=16 epsilon.   (4)

Positive new rows only are summed. Thus the mean capped norm error eta=sum_t q'_t min(1,||W'_t/sqrt(q'_t)-b_t||_2) is at most min(1,4 sqrt(epsilon)). Normalized row squared spectra and Boolean-phase squared spectra have TV at most the capped norm error by Cauchy--Schwarz and Walsh orthogonality.

Assume FEI(K) for all Boolean functions of fewer than n essential coordinates, K>=0. Every b_t is an actual Boolean function on a<n coordinates. With psi_a(s)=h2(s)+s log2(2^a-1) up to 1-2^-a, capped by a thereafter, concavity and the standard maximal-coupling entropy bound yield

    B_A(G)<=K I_A(G)+psi_a(eta)+K a eta.                         (5)

The influence expectation differs between the two squared row laws by at most a times their TV. This is an independent reconstruction of A052's phase mechanism with externally chosen product phases; it never declares these phases physical descendants.

If G is a least-essential-dimension K-violator, all physical children have nonpositive D_K=H-KI. The exact restriction identity retains them:

    D_K(G)=B_A(G)+J_A(G)-K I_A(G)+E_x D_K(G_x).

J_A<=Gamma_A follows from Jensen under the row's squared-density tilt. For one-point surgery of F, Gamma_A(F)=0 and (2),(5) imply the new deficit restriction

    0<D_K(G)<=10 sqrt(p)+psi_a(s)+K a s,
    s=min(1,4 sqrt(p)).                                         (6)

For arbitrary epsilon the same phase bound (5) holds, but the dimension-free collision estimate (2) is specific to one-point surgery. Do not extend it to arbitrary Hamming perturbations without a separate argument. In (6), n is the essential dimension of the purported violating G, with F written on that same named cube. If G loses coordinates, remove them and re-establish the product-cut hypotheses before invoking minimality.

## 4. A prime near-tensor separates joint cuts from singleton prices

Let h be the pinned NAND6 case0006 and K=12/5. The direct character-sum certificate verifies H(h)>3+1/200, I(h)=5/4, V_{48}(h)<47/20, and V_i(h)/Inf_i(h)>319/100 for all six singletons. All coordinates are essential, so each Inf_i>=1/32 by counting physical edges on a six-bit cube.

For t>=4 take F_t=h^(tensor t), n=6t, and flip any one physical vertex to obtain G_t. Tensor additivity gives D_K(F_t)>t/200, V_{48}(F_t)<47/20 and I_{48}=1 on any selected copy's mask48; each singleton remains above319/100. Point surgery makes G_t tensor-prime over every coordinate partition, all-essential and full Fourier support: the product has even negative count, the edit makes it odd, and every integer Walsh sum is then2 modulo4.

At n=24 let u=1/2048. The binary entropy bound h2(u)<=u log2(1/u)+2u gives

    |delta H|<=37/2048<19/1000,
    K|delta I|<= (24/5)*24*2^-24<1/1000.

Thus D_K(G_t)>0 at t=4 and thereafter: these errors decrease when n increases by6 whereas t/200 increases. For either a=1 or2, Omega<=15/2048+10/4096<1/100, and 2K a p<1/1000, uniformly for n>=24. Hence

    V_{48}(G_t)<K I_{48}(G_t),
    V_i(G_t)>K Inf_i(G_t) for every singleton i.                (7)

The joint block has seed slack >1/20; each singleton's opposite slack exceeds(319/100-12/5)/32=79/3200>11/1000. The same rational errors therefore prove both signs. The monotonic error claims are elementary: at n->n+6, u divides by8, sqrt(p) divides by8, and each linear prefactor grows by at most8; strict decrease follows from the actual n>=24 prefactors. No large truth table is enumerated.

This is an actual all-dimensional prime Boolean family exhibiting a useful joint block while every singleton collision price fails at the fixed threshold. It is not a FEI disproof: H/I tends to the finite seed ratio. It is not a critical-witness obstruction: fix all but one copy and choose a fixed vertex in another copy away from the edit; the resulting proper child is +/-h with D_K(h)>1/200. The affordable joint cut itself forces positive mean child deficit via the exact telescope. Tensor-primitivity plus failure of all singleton collision tests therefore does not certify dimension-criticality or control hidden tensors.

## 5. What has and has not been closed

(1)--(6) are analytic all-dimensional bounds. They quantify hidden-product separation at a specified deficit and fixed threshold, without assuming lower bounds on individual influences. The fixed-price transfer in (3) still requires strict slack. The phase deficit estimate can be much larger than the actual deficit; point defects with exponentially small deficits are not excluded by its scale. The NAND control is not dimension-critical because a higher-ratio child survives. No universal constant is proved.

FIRST UNSUPPORTED LINE: a dimension-independent K and a rule choosing a proper block on every least-dimensional K-violation with Gamma plus Boolean-phase error strictly below its positive deficit, or equivalently an affordable V block with all terminal deficits retained. The dimension-free surgery modulus removes a continuity obstruction, not this selection/payment gap.
