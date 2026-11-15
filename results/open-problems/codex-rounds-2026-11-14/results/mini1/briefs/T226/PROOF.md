# A small-step obstruction for a two-layer linear network

Fix positive integers m,d and a vector b in R^d. All entries of a in R^m and W in R^{m by d} are trainable. The network and loss are

\[
 f_{a,W}(x)=a^TWx,\qquad
 L(a,W)=\frac12\|W^Ta-b\|^2.
\]

This is the full-batch empirical loss on the d examples x_j=sqrt(d)e_j, y_j=sqrt(d)b_j, with the convention L=(1/(2d)) sum_j(f(x_j)-y_j)^2. It is also exactly the population square loss (1/2) E[(f(x)-b^Tx)^2] for x distributed as N(0,I_d). The finite-batch interpretation requires no population approximation. In particular m=16,d=8 is a fixed network with 144 trainable parameters.

Use the Euclidean parameter norm

\[
 S=\|a\|^2+\|W\|_F^2,
\]

and let sharpness mean lambda_max of the Hessian in these coordinates. Gradient descent updates both layers simultaneously with the same positive step eta.

## Deterministic theorem

Write beta=||b|| and R=S_0+2 beta. If R>0 and eta R <= 1/32, then, for every integer t>=0,

\[
 S_t\leq 6R,\qquad
 \|\nabla^2L(a_t,W_t)\|_{\mathrm{op}}\leq 10R,
 \tag{1}
\]

and

\[
 L_{t+1}\leq L_t-\frac\eta2\|\nabla L(a_t,W_t)\|^2.
 \tag{2}
\]

Consequently sharpness never reaches 1/eta; in fact eta lambda_max <=5/16. Any parameter limit of the iterates also satisfies (1). If R=0, the parameters and target are zero and every iterate is zero.

### Derivative estimates

Put v=W^Ta and r=v-b. Direct differentiation gives

\[
 g_a=Wr,\qquad g_W=ar^T.
 \tag{3}
\]

For a perturbation h=(u,V), the output differential is J h=W^Tu+V^Ta. Cauchy--Schwarz gives

\[
 \|Jh\|\leq\|W\|_F\|u\|+\|a\|\|V\|_F
 \leq \sqrt S\sqrt{\|u\|^2+\|V\|_F^2}.
\]

Thus ||J||_op <= sqrt(S), ||g|| <= sqrt(S)||r||, and

\[
 \nabla^2L[h,h]=\|Jh\|^2+2u^TVr.
\]

Because 2|u^TVr| <= ||r||(||u||^2+||V||_F^2), the Hessian, which is symmetric, satisfies

\[
 \|\nabla^2L\|_{\mathrm{op}}\leq S+\|r\|
 \leq\tfrac32 S+\beta.
 \tag{4}
\]

Here ||v|| <= ||a||||W||_F <= S/2 was used in the last inequality. The absolute value of every Hessian quadratic form is bounded by the displayed constant, so (4) bounds negative as well as positive eigenvalues.

### The discrete balance estimate

Define the symmetric m by m matrix B=WW^T-aa^T. From (3) and the simultaneous updates,

\[
 B_{t+1}-B_t=\eta^2(g_{W,t}g_{W,t}^T-g_{a,t}g_{a,t}^T).
 \tag{5}
\]

Indeed the terms linear in eta are -eta(ar^TW^T+Wra^T) in both WW^T and aa^T and cancel. Let ||.||_* denote the nuclear norm. Since ||ZZ^T||_*=||Z||_F^2,

\[
 \|B_{t+1}-B_t\|_*\leq\eta^2\|g_t\|^2,
 \qquad \|B_0\|_*\leq S_0.
 \tag{6}
\]

Suppose (2) has already been proved for steps 0,...,t-1. Telescoping, using L_t>=0, yields

\[
 \sum_{k<t}\eta\|g_k\|^2\leq 2L_0,
 \quad L_t\leq L_0,
 \quad D_t:=\|B_t\|_*\leq S_0+2\eta L_0.
 \tag{7}
\]

These statements hold also at t=0, with an empty sum. At initialization,

\[
 \|r_0\|\leq S_0/2+\beta=R/2,
 \qquad L_0\leq R^2/8.
 \tag{8}
\]

It follows that

\[
 \|r_t\|\leq R/2,\qquad
 \|v_t\|\leq\beta+R/2\leq R,\qquad
 D_t\leq R+\eta R^2/4.
 \tag{9}
\]

The matrix bound also controls both factors. Set q=||a_t||^2. Since WW^T=aa^T+B,

\[
 \|v_t\|^2=q^2+a_t^TB_ta_t\geq q^2-D_tq.
\]

This implies q<=D_t+||v_t||: if q>D_t+||v_t||, then q(q-D_t)>||v_t||^2, a contradiction. Moreover

\[
 \|W_t\|_F^2=q+\operatorname{tr}B_t\leq q+D_t.
\]

Combining these inequalities and (9) gives

\[
 S_t\leq 3D_t+2\|v_t\|
 \leq 5R+\tfrac34\eta R^2
 \leq\left(5+\tfrac3{128}\right)R<6R.
 \tag{10}
\]

### Closing the induction

By (3), (9), and (10),

\[
 \|g_t\|\leq\sqrt{6R}\,R/2.
\]

Every point theta_t-s eta g_t on the proposed step segment, 0<=s<=1, therefore has parameter norm at most

\[
 \sqrt{6R}(1+\eta R/2)\leq\sqrt{6R}\,\frac{65}{64}.
\]

Its squared norm is less than 8R, since 6(65/64)^2=12675/2048<8. By (4) and beta<=R/2, the Hessian operator norm on the entire segment is at most

\[
 \tfrac32(8R)+\beta\leq\tfrac{25}{2}R<13R.
\]

Taylor's integral formula on this segment gives

\[
 \begin{aligned}
 L(\theta_t-\eta g_t)
 &\leq L_t-\eta\|g_t\|^2+\tfrac{13R}{2}\eta^2\|g_t\|^2\\
 &\leq L_t-\tfrac\eta2\|g_t\|^2,
 \end{aligned}
\]

because 13 eta R<=13/32<1. This proves (2) at step t from the earlier steps and closes the induction. Finally, (4) at the iterates and S_t<=6R give

\[
 \|\nabla^2 L_t\|_{\mathrm{op}}\leq 9R+\beta\leq\tfrac{19}{2}R<10R.
\]

Multiplication by eta gives eta lambda_max<=10/32=5/16. Continuity of the Hessian proves the assertion about parameter limits. This proves the theorem.

## Gaussian initialization and the endpoint event

Fix sigma>0, m,d, and b independently of eta. Initialize the p=m(d+1) parameter entries independently as N(0,sigma^2). For beta>0 assume 0<eta<=1/(128 beta); for beta=0 impose no additional restriction. Then

\[
 \mathbb P\!\left\{\exists t\geq0:\lambda_{\max}(\nabla^2 L_t)\geq1/\eta\right\}
 \leq \min\left\{1,\;2^{p/2}\exp\!\left(-\frac1{256\sigma^2\eta}\right)\right\}.
 \tag{11}
\]

To prove this, the deterministic theorem shows that the event in (11) is contained in {S_0+2 beta>1/(32 eta)}. Under the stated restriction,

\[
 \frac1{32\eta}-2\beta\geq\frac1{64\eta}.
\]

For a scalar Z distributed as N(0,sigma^2), completing the square in the Gaussian integral gives E exp(Z^2/(4 sigma^2))=sqrt(2). Independence and Markov's inequality now give

\[
 \mathbb P\{S_0>1/(64\eta)\}
 \leq\exp\!\left(-\frac1{256\sigma^2\eta}\right)
       \mathbb E\exp(S_0/(4\sigma^2))
 =2^{p/2}\exp\!\left(-\frac1{256\sigma^2\eta}\right).
\]

This proves (11).

The same estimate applies separately at every eta if the Gaussian variance is sigma_eta^2. For fixed m,d,b, the edge-entry probability still tends to zero whenever eta sigma_eta^2 tends to zero. Thus initialization variances growing strictly slower than 1/eta are excluded as well.

For a precise version of the endpoint event, let epsilon(eta)>=0 be any deterministic function with epsilon(eta)->0. Consider convergence in parameter space to a global minimizer theta_infinity satisfying

\[
 |\lambda_{\max}(\nabla^2L(\theta_\infty))-2/\eta|
 \leq\epsilon(\eta).
 \tag{12}
\]

For all sufficiently small eta, 2/eta-epsilon(eta)>1/eta. On {eta R<=1/32}, every parameter limit has sharpness at most 5/(16 eta), so (12) is impossible. Its probability therefore has the same upper bound (11), whether or not entry into an edge regime is required as an additional condition. The conclusion also holds for any endpoint window with lower edge greater than 5/(16 eta), for example |eta lambda_max-2|<=1/2.

## Scope

This proves a small-probability alternative for a fixed network and a fixed initialization law. It does not prove convergence for all initializations, nor does it establish any positive-probability edge regime. The high-probability trajectories are shown to satisfy a descent condition; this is an obstruction to edge entry, not an explanation of convergence beyond the descent condition. The constants are conservative and are not asserted optimal. The bound is for fixed dimension and fixed sigma, and need not vanish if either grows as eta tends to zero. In particular it does not address initialization with variance of order 1/eta.

The loss nevertheless has arbitrarily sharp global minima. For c>0 take a=c e_1, W_{1,:}=b^T/c, and all other rows of W zero. Then W^Ta=b. At any zero-residual point the Hessian is J^TJ, whose nonzero eigenvalues are those of JJ^T=W^TW+||a||^2 I_d. For this particular family the top eigenvalue is c^2+beta^2/c^2. It tends to infinity with c. Thus the result is not a consequence of the absence of sharp global minima or of global smoothness of the loss.
