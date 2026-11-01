SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-23T21:56:03Z.
attacking: dependence-safe two-sided Plancherel for conjugate quadratic pairs, replacing exact matched-opposition by an invertible cross-difference condition without treating residual curvature as a small random error.

# Early substantive calculation

Let X=(X1,X2), Y=(Y1,Y2) be independent product vectors with scalar densities <=1. Let F,G be arbitrary measurable real functions and C an invertible 2x2 real matrix. Put

S = F(X)+G(Y)+X^T C Y.

For t!=0 define a_t(x)=f_X(x)e^{itF(x)} and b_t(y)=f_Y(y)e^{itG(y)}. Then

phi_S(t)=int a_t(x) \hat b_t(t C^T x) dx,

with Fourier convention \hat b(xi)=int e^{i xi.y} b(y)dy. Since f_X,f_Y are product probability densities bounded by one,

||a_t||_2^2 <=1,  ||b_t||_2^2<=1.

Cauchy-Schwarz, the change xi=t C^T x, and Plancherel give

|phi_S(t)| <= 2 pi |det C|^{-1/2}|t|^{-1}.

Hence

|phi_S(t)| <= min(1, 2 pi |det C|^{-1/2}|t|^{-1}).

Writing A=2 pi |det C|^{-1/2}, direct integration gives

int_R |t|^{-1/2}|phi_S(t)| dt <= 8 sqrt(A) = 8 sqrt(2 pi)|det C|^{-1/4},

and

int_R |t|^{-1/2}|phi_S(t)|^2 dt <= (16/3) sqrt(A) = (16/3)sqrt(2 pi)|det C|^{-1/4}.

Using |x|^{-1/2}=(2 pi)^(-1/2) int_R e^{-itx}|t|^{-1/2}dt in the positive-regularized sense, the first estimate implies

sup_s E|S-s|^{-1/2} <= 8 |det C|^{-1/4},

while the independent-copy identity |phi_S(t)|^2=E exp(it(S-S')) gives

E|S-S'|^{-1/2} <= (16/3)|det C|^{-1/4}.

For conjugate variables U=X-X', V=X+X' and quadratic pairs
R_-(U)=U^T P_-U+ell_-^TU+d_-,
R_+(V)=V^T P_+V+ell_+^TV+d_+,
expansion in the genuine independent originals X,X' yields

R_-(U)+R_+(V)=F(X)+G(X')+2 X^T(P_+-P_-)X'

for explicit one-bank quadratics F,G. Therefore if K=P_+-P_- is invertible,

sup_s E|R_-+R_+-s|^{-1/2} <= 4 sqrt(2)|det K|^{-1/4},

and

int_R |t|^{-1/2}|phi_{R_-+R_+}(t)|^2dt <= (16/3)sqrt(pi)|det K|^{-1/4}.

This is nonperturbative in P_-+P_+: same-bank residual curvature is retained exactly inside F,G, so no moment/support assumption is introduced. One further independent physical square d(Z+h)^2 then gives an output density bounded by 4 sqrt(2)|d|^{-1/2}|det K|^{-1/4}, hence linear small-ball scaling.

Status: calculation to be checked and integrated with the designated fleet04/B03 dependent sum/difference theorem before final publication. Full QFORM remains open; continuity is not asserted for the square-convolution branch.
