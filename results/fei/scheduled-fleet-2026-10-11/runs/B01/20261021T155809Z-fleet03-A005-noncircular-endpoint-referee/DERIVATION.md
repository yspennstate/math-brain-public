# Whole-sign curvature audit (author derivation; review pending)

All cubes are finite and uniform. Walsh coefficients a_S are real, H=-sum a_S^2 log2(a_S^2), I=sum |S|a_S^2, mu=a_empty. Put k(t)=-t^2 log2(t^2)+3t^2/ln2, with zero terms continuous. The curvature/Bregman construction is used only on [-1,1], where k is convex. Let R_c be sum_S [k(c 1_{S=empty})-k(a_S)-kprime(a_S)(c 1_{S=empty}-a_S)], c in {-1,1}. These are exactly the refunds for flipping the full positive or full negative sign set, respectively. An empty sign set is allowed.

## 1. Exact calculation
kprime(t)=-2t log2(t^2)+4t/ln2, continuously zero at t=0. Parseval gives sum kprime(a_S)a_S=2H+4/ln2. Both the original and the target coefficient vectors have squared norm one, and both constant targets have entropy zero. Therefore

R_c=H+4/ln2+c[2mu log2(mu^2)-4mu/ln2].

Consequently R_+ + R_-=2H+8/ln2, and

R_min := min(R_+,R_-)=H+a(|mu|),
a(u)=(4/ln2)(1-u+u ln u), a(0)=4/ln2.

These identities do not assume criticality, a flow, or FEI. They include constants, dictator and parity. In particular, bounding the sum after subtracting its constant floor by 2KI is EXACTLY FEI(K). No flow normalization turns that whole-sign remainder into an independent payment.

## 2. Uniform error at small influence
For 0<=u<=1, 0<=1-u+u ln u<= (1-u)^2: nonnegativity follows by integrating -ln u; the upper bound follows from ln u<=u-1, multiplied by u>=0 (the u=0 endpoint follows continuously). Parseval/Poincare gives 1-u<=1-u^2=Var(f)<=I(f). Thus for every nonconstant f,

0<=R_min/I-H/I<=4I/ln2.

The zero-influence case is constant and R_min=H=0; no division by zero is made. This bound requires no spectral positivity beyond an actual Boolean spectrum and Poincare. Small dimension does not replace the influence condition.

## 3. Arbitrary-seed admission into the smaller-refund endpoint
Fix any nonconstant Boolean seed f, write h=H(f), j=I(f)>0. For integer t>=1 take g_t=z product_{b=1}^t f(x_b) on disjoint copies with a fresh literal z. Then g_t is balanced, H(g_t)=th, I(g_t)=1+tj. Set k=ceil(sqrt(t)), p=2^-k and F_t=1 off the all-positive k-control vertex, F_t=g_t on it. These are actual Boolean functions. Direct Fourier expansion gives

mu(F_t)=1-p,
I(F_t)=p(1+tj+k),
H(F_t)=pth+(4p-2p^2)k-(1-p)^2 log2((1-p)^2).

The control-only nonempty coefficients equal -p; each nonzero data coefficient of g_t occurs at all 2^k control sets with amplitude p times its old amplitude. This proves the entropy formula including the empty coefficient and all auxiliary costs. The entropy last term is O(p), since -ln(1-p)<=p/(1-p), p<=1/2. Thus I(F_t)->0 and H(F_t)/I(F_t)->h/j; all individual influences also go to zero. No exchange of infinite sums occurs: each formula is finite; polynomial(t)2^-ceil(sqrt(t))->0 and k/t->0. Section2 implies R_min(F_t)/I(F_t)->h/j as well.

Write C_star=sup_all_nonconstant H/I in the extended reals. For eps>0 let M(eps)=sup_{0<I<=eps} R_min/I. This domain is nonempty by the construction. Then C_star<=M(eps)<=C_star+4eps/ln2, where the left inequality follows by admitting each fixed seed and taking the limit inside the fixed eps domain (not by interchanging a supremum with a limit). Hence lim_{eps down to0} M(eps)=C_star, including C_star=infinity. More quantitatively, a uniform endpoint R_min<=K I for all sufficiently small-I Boolean functions implies FEI at the SAME K. The converse from FEI(K) supplies K+4eps/ln2 on I<=eps; it does not assert exact K at positive eps. This distinguishes same-constant hardness from a falsely asserted fixed-eps equivalence.

## 4. Scope and first unpaid line
The full A052 finite-maximality conditions imply all-edit refund-dominating cut inequalities. This audit neither embeds arbitrary seeds into genuine finite maximizers nor refutes those conditions. It isolates the whole-sign refund resource: an O(I) bound on its smaller value in the rare regime already contains full FEI at the same constant. The large, empty-sign refund at constants must not be charged; only R_min removes this known constant obstruction, and even that corrected endpoint is FEI-hard. The next unpaid step is a proper physical edit/pair comparison derived from finite maximality that pays the selected interaction and all retained child debt from the SAME unused reserve, without assuming the whole-sign refund bound being sought.
