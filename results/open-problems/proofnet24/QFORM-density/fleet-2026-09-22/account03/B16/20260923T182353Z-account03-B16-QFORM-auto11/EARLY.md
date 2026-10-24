SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T18:23:53Z.
attacking: projection-product interaction: close or sharply reduce the superdiffuse 80-bank same-side curvature branch while retaining original-coordinate dependence.

# Early calculation — exact discriminant cancellation at the true near-coloop

Status: supporting calculation; full QFORM remains open. Execution: WITHOUT_VERIFIED_BRAIN.

Start from account03/B16 r29's exact-rank-three surviving collar. Thus A=R Lambda R^T, R^T R=I_3, sigma_min(Lambda)>=1; the selected original-coordinate row is r_0=sqrt(c)e with c>63/64; every physical diagonal has |A_jj|<1/64; and the hub-star energy R_*^2=sum_{j!=0}A_0j^2 exceeds 4031/4096.

Choose the transverse spectral basis so

Lambda = [[alpha,beta,0],[beta,u,v],[0,v,w]].

Write every leaf row as (s_j,p_j,q_j), and define the three leaf projections
S=sum s_j X_j, U=sum p_j X_j, V=sum q_j X_j.
Parseval gives ||s||_2^2=1-c, ||p||_2=||q||_2=1 and s,p,q pairwise orthogonal. With x=X_0,

Q = alpha(sqrt(c)x+S)^2 + 2 beta(sqrt(c)x+S)U + u U^2 + 2vUV + wV^2.

Treat Q as a quadratic polynomial in the genuine independent physical scalar x. For a target t, its root discriminant divided by 4 is

D_t = c[(alpha S+beta U)^2-alpha(alpha S^2+2 beta S U+uU^2+2vUV+wV^2-t)]
    = c[(beta^2-alpha u)U^2-2alpha v UV-alpha wV^2+alpha t].

The longitudinal projection S cancels exactly before any absolute value or conditional projection-height bound is taken.

Put Delta=beta^2-alpha u and
H_D=[[Delta,-alpha v],[-alpha v,-alpha w]].
Then the exact determinant identity is

det H_D = alpha det Lambda.

If alpha det Lambda>0, H_D is definite. The joint law of (U,V), an orthonormal two-dimensional projection of the original product law, has density at most 2. For any probability density rho<=M on R^2 and any definite nonsingular symmetric H,

sup_t E |Z^T H Z-t|^{-1/2} <= 2 sqrt(2 pi M) |det H|^{-1/4}.

Indeed after y=|H|^{1/2}z the transformed density is at most L=M/sqrt(|det H|), while for every t and epsilon>0 the annulus {| |y|^2-t |<epsilon} has area at most 2 pi epsilon. Hence P(|Z^T HZ-t|<epsilon)<=min(1,2 pi L epsilon); integrating the layer-cake identity for W^{-1/2} gives 2 sqrt(2 pi L).

The one-dimensional quadratic root formula gives, conditional on the leaves,

p_{Q|leaves}(t) <= c^{-1/2} [((Delta U^2-2alpha vUV-alpha wV^2+alpha t)_+)]^{-1/2},

so on the sign-compatible branch alpha det Lambda>0,

||p_Q||_infinity <= 4 sqrt(pi) c^{-1/2} |alpha det Lambda|^{-1/4}.

In particular, if |alpha det Lambda|>=1/4096 then c>63/64 gives

||p_Q||_infinity < 4 sqrt(pi) sqrt(64/63)*8 = 57.166898 <58.

Two additional exact ledgers sharpen the remaining source-overlap issue. Put a=1-c and d^2=alpha^2 a+beta^2=R_*^2/c. Since |A_00|=c|alpha|<1/64 and c>63/64, |alpha|<1/63, hence

beta^2 > 4031/4096 - 1/(63^2*64) = 15998975/16257024 >31/32.

For a>0 define Z=S/sqrt(a), and the normalized physical leaf-star aggregate
L=(alpha sqrt(a) Z+beta U)/d.
In the orthonormal coordinates (x,L,V), the 2x2 x-L block B_xL satisfies

det B_xL = -k Delta,

while the 3x3 compression satisfies

det B_xLV = k det Lambda,

where k=beta^2 c/d^2. Quantitatively

k > (63/64)*(1 - [1/(63^2*64)]/[4031/4096])
  =15998975/16252992
  =0.9843710622... >31/32.

Moreover if alpha det Lambda>0, the identity det Lambda=-(Delta w+alpha v^2) implies |Delta w|=|det Lambda|+|alpha|v^2>=1. Consequently

|w det B_xL|=k |Delta w|>31/32.

Thus the sign-compatible true-near-coloop branch has a uniformly nondegenerate algebraic two-hub-plus-square determinant ledger. The still-unpaid point is exactly source overlap: L and V are orthogonal product projections of the same leaf coordinates, not independent source banks. A valid next step must pay this overlap jointly rather than replace the bounded joint projection density by independence.
