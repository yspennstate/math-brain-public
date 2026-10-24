SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T05:31:36Z.
attacking: the account03/B16 r26 near-coloop collar by testing whether an absolute spectral Fresnel integral can stay uniform as the residual line mass tends to zero.

# Early substantive checkpoint

Fresh partner input: account03/B16 r26 (`QFORM-R23-ONE-COLOOP-REDUCTION-v1`) leaves, inside its exact-rank-three residual chamber, only the leverage collar `c>63/64`; the bound must be uniform as `a=1-c -> 0`.

Take `Lambda=diag(1,1,-1)` and the orthonormal coefficient basis

`e=(1,0,1)/sqrt(2)`, `p=(1,0,-1)/sqrt(2)`, `q=(0,1,0)`.

In this basis the quadratic matrix is

`B=[[0,1,0],[1,0,0],[0,0,1]]`.

For `c=1-a`, use physical rows

`r_0=sqrt(c)e`, `r_1=sqrt(a)e`,

and a many-direction Parseval plane frame `w_k in e^perp`, `sum_k w_k w_k^T=I_2`, with `max ||w_k||^2<1/64`. Thus the spectral coordinates are

`T=sqrt(c)X_0+sqrt(a)X_1`, `(C,D)=sum_k w_k X_k`,

and

`Q=2TC+D^2`.

The line bank `{X_0,X_1}` is independent of the whole generally dependent projected pair `(C,D)`. The two-dimensional product-projection theorem gives `||p_(C,D)||_infinity<=2`, while convolution gives `||p_T||_infinity<=c^(-1/2)`. Rescaling the already completed null-scalar/dependent-pair theorem therefore yields

`||p_Q||_infinity <= 3*2^(4/3)*c^(-1/3) < 7.60` whenever `c>63/64`.

However the exact three-dimensional Fresnel formula underlying Claude's completed Theorem F produces, after absolute value in the Fresnel dual variable, a coefficient containing

`I(a,c)=int_R |psi(sqrt(c)xi) psi(sqrt(a)xi)| dxi`,

for `psi(t)=sin(t/2)/(t/2)` when `X_0,X_1` are unit-interval uniforms. Writing `r=sqrt(a/c)` and `x=sqrt(c)xi/2`,

`I(a,c)=(2/sqrt(c)) int_R |sinc(x) sinc(r x)| dx`.

For `|rx|<=1`, `sinc(rx)>=sin(1)`. Summing the intervals `[k pi,(k+1)pi]` gives

`I(a,c) >= (8 sin(1)/(pi sqrt(c))) (H_(N+1)-1)`,

where `N=floor(1/(pi r))-1`. Hence `I(a,c) -> infinity` logarithmically as `a->0`.

So the near-coloop collar is a genuine phase-sensitive endpoint: an absolute-value spectral Fresnel coefficient cannot be uniformly bounded even on a source-valid target family whose true output density stays below `7.60`. The final report will make the many-direction plane frame, strict-N3 inequalities, and the lower bound fully explicit.
