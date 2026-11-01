# Deterministic checks — QFORM-GROWING-DIRECTION-UNIFORM-CONVOLUTION-BARRIER-v1

Status: `PASS_QFORM_GROWING_DIRECTION_UNIFORM_CONVOLUTION_BARRIER`

1. Tetrahedral frame:

`sum_{a=1}^4 t_a t_a^T = (4/3) I_3` exactly. Therefore rows `r_{k,a}=sqrt(3/(4K)) R_k t_a` satisfy `T_K^T T_K=I_3` and every leverage is `3/(4K)`.

2. Exact spectrum:

For `A_K=T_K B_K T_K^T` with `T_K^T T_K=I_3`, the three nonzero eigenvalues of `A_K` equal those of `B_K`. For `B=I-2nn^T`, `n=(1,2,3)/sqrt(14)`, one has exactly

`B=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`, `B^2=I`, `det B=-1`, `spec(B)={1,1,-1}`.

3. Carrier covariance:

`W=sqrt(3/4) sum_a t_a U_a`, `Var(U_a)=1/12`, so

`Cov(W)=(3/4)(1/12)(4/3) I_3=I_3/12`.

4. Tetrahedral high-frequency projection lemma:

For unit `u`, `sum_a (t_a dot u)^2=4/3`. If at most one absolute projection were at least `1/3`, the sum of squares would be strictly less than `1+3(1/9)=4/3`. Hence at least two satisfy `|t_a dot u|>=1/3`. Since the sinc arguments are `(sqrt(3)/4)(t_a dot eta)`, two factors each obey `|sinc|<=4 sqrt(3)/|eta|`, giving

`|phi_W(eta)|<=48/|eta|^2`.

5. High-frequency integral:

For `|xi|>=R sqrt(K)`,

`|hat g_K(xi)| <= (48K/|xi|^2)^K`.

In dimension three its radial integral is exactly bounded by

`4 pi (48K)^K (R sqrt(K))^(3-2K)/(2K-3)`
`= [4 pi K^(3/2)/(2K-3)] 48^K R^(3-2K)`,

which tends to zero for every fixed `R>sqrt(48)`.

6. Source cap:

For arbitrary probability law `nu_i`, `X_i=U_i+J_i` has density

`f_i(x)=nu_i([x-1/2,x+1/2])`,

hence `0<=f_i(x)<=1` pointwise and `integral f_i=1`.

7. Pinned Theorem-F hypotheses:

With `B_K=O diag(lambda) O^T`, the physical eigenframe is `V_K=T_K O`; `V_K^T V_K=I_3`, `G_I=I_3`, every row leverage is `3/(4K)<=1/2` for `K>=2`, and residual quadratic part is zero. Conditioning on `J` adds only a linear term, explicitly allowed in the pinned theorem. Therefore

`|Phi_{K,z}(t)| <= (4 pi)^(3/2) |t|^(-3/2) |lambda_1 lambda_2 lambda_3|^(-1/2)`
`<= (4 pi)^(3/2) |t|^(-3/2)`.

The capped majorant `min(1,(4 pi)^(3/2)|t|^(-3/2))` switches at `|t|=4 pi` and has exact integral `24 pi`.

8. Gaussian comparison envelope:

At variance `v=1/12`, each noncentral Gaussian-square characteristic factor has modulus at most `(1+4v^2 lambda^2 t^2)^(-1/4)`. With `|lambda|>=1`, the three-factor modulus is at most

`(1+t^2/36)^(-3/4) <= 6^(3/2)|t|^(-3/2)`.

9. Quantitative Fourier bridge:

Let `epsilon=||g_K-gamma||_1` and `C_*=(4 pi)^(3/2)+6^(3/2)`. Then

`|Phi_{K,z}-Phi^G_{K,z}| <= min(epsilon,C_* |t|^(-3/2))`.

The crossover is `t_0=(C_*/epsilon)^(2/3)` and

`integral_R min(epsilon,C_* |t|^(-3/2)) dt = 6 C_*^(2/3) epsilon^(1/3)`.

Hence Fourier inversion gives

`sup_z ||h_{K,z}-h^G_{K,z}||_infinity <= (3/pi) C_*^(2/3) epsilon^(1/3)`.

Numerically `C_*=59.24356243135273...` and `(3/pi) C_*^(2/3)=14.51216338024275...`.

10. Growing-direction stress:

With per-coordinate rare-jump probability `lambda/(4K)` and `D_K=c sqrt(4K/3)`, one rare jump gives active displacement exactly `±c R_k t_a`. Summing the leading squared active jump over `4K` coordinates gives

`4K * [lambda/(4K)] * c^2 = lambda c^2`,

so the active Lindeberg tail stays nonzero.
