# A two-bank receiver for a one-hub square with nonlinear bank phases

23 September 2026. Scope: a proved bounded-density theorem for three independent coordinate banks, and an explicit exact-rank-three family. This does not prove the unrestricted quadratic-density conjecture.

## 1. Two-bank theorem

Let \(H\) be independent of two independent random vectors \(X_+,X_-\). Assume \(H\) has density at most \(K_H\). On each bank put
\[
L_\pm=\ell_\pm\cdot X_\pm,\qquad V_\pm=v_\pm\cdot X_\pm,
\]
and assume the joint density of \((L_\pm,V_\pm)\) is at most \(M_\pm\). Let \(F(H)\) and \(G_\pm(X_\pm)\) be arbitrary real measurable functions, and let \(\kappa\lambda\ne0\). Then
\[
Q=F(H)+G_+(X_+)+G_-(X_-)
   +2\kappa H(L_++L_-)
   +\lambda(V_++V_-)^2
\]
has a bounded continuous density with
\[
\boxed{\quad
\|p_Q\|_\infty\le
3\left(\frac{K_H^2 M_+M_-}{\kappa^2|\lambda|}\right)^{1/3}.
\quad} \tag{1}
\]
All bank self terms, including arbitrary original-coordinate affine terms and the chirps \(\pm2\varepsilon L_\pm^2\), are allowed. A constant offset in the hub partner \(L_++L_-\) can be absorbed into \(F\).

### Proof

For fixed \(t\), push \(e^{itG_\pm(X_\pm)}d\mathbb P_\pm\) onto \((L_\pm,V_\pm)\), obtaining complex densities \(a_{\pm,t}\). Their moduli are bounded by the ordinary joint densities, hence
\[
\|a_{\pm,t}\|_2^2\le M_\pm.
\]
Writing \(\Phi_{\pm,t}\) for their two-dimensional Fourier transforms, Plancherel and Cauchy–Schwarz give
\[
\int_{\mathbb R^2}|\Phi_{+,t}(x,y)\Phi_{-,t}(x,y)|\,dx\,dy
 \le (2\pi)^2\sqrt{M_+M_-}. \tag{2}
\]
The Fresnel identity for \(e^{it\lambda(V_++V_-)^2}\), followed by integration in \(H\), gives for \(t\ne0\)
\[
|\phi_Q(t)|
\le {K_H\over 2|\kappa t|\sqrt{4\pi|\lambda t|}}
\int_{\mathbb R^2}|\Phi_{+,t}(x,y)\Phi_{-,t}(x,y)|\,dx\,dy
\le {\pi^{3/2}K_H\sqrt{M_+M_-}\over
|\kappa|\sqrt{|\lambda|}\,|t|^{3/2}}. \tag{3}
\]
Here the change of variables is \(x=2\kappa th\); the factor \(e^{itF(h)}\) has modulus one. One may first regularize the Fresnel integral by a Gaussian, use the integrable majorant (2), and then remove the regularization. The same bound holds for the actual characteristic function.

If \(|\phi_Q(t)|\le\min(1,A|t|^{-3/2})\), Fourier inversion gives
\[
\|p_Q\|_\infty\le {1\over2\pi}
  \int_{\mathbb R}\min(1,A|t|^{-3/2})\,dt
={3\over\pi}A^{2/3}.
\]
Substitution of \(A\) from (3) proves (1). Integrability of \(\phi_Q\) gives continuity.

For product coordinates with densities at most one, the two-dimensional projection theorem gives
\[
M_\pm\le {2\over\sqrt{\det G_\pm}},\qquad
G_\pm=
\begin{pmatrix}
|\ell_\pm|^2&\ell_\pm\cdot v_\pm\\
\ell_\pm\cdot v_\pm&|v_\pm|^2
\end{pmatrix}. \tag{4}
\]
This statement only uses the actual two-bank product source to certify the joint density caps; the Fourier step itself permits arbitrary laws within each bank.

## 2. An exact-rank-three family outside three simple structural receivers

Let \(m\) be a positive multiple of four, index the light coordinates by \(j=1,\ldots,m\), and add one physical hub coordinate \(h\). Define light vectors
\[
w_j=m^{-1/2},\qquad
v_j=\sqrt{12\over m(m^2-1)}
       \left(j-{m+1\over2}\right),\qquad
p_j=s_jm^{-1/2},
\]
where \(s_j\) repeats \((+1,-1,-1,+1)\). Then \(w,v,p\) are orthonormal. For \(\varepsilon=m^{-3}\), let
\[
A_\varepsilon=e_hw^\mathsf T+we_h^\mathsf T
                 +vv^\mathsf T
                 +\varepsilon(wp^\mathsf T+pw^\mathsf T).
\]
The light vectors are extended by zero at \(h\). Its quadratic form is
\[
X^\mathsf TA_\varepsilon X
=2HL+V^2+2\varepsilon LP,\qquad
L=w\cdot X',\quad V=v\cdot X',\quad P=p\cdot X'.
\]
In the orthonormal frame \((e_h,w,v,p)\), \(A_\varepsilon\) has nonzero eigenvalues
\[
\sqrt{1+\varepsilon^2},\quad
-\sqrt{1+\varepsilon^2},\quad 1,
\]
so \(s_3(A_\varepsilon)=1\) exactly.

This family defeats the following *particular* proposed structural trichotomy as \(m\to\infty\).

* For every principal coordinate set \(K\) of size at most \(N\),
\[
s_3((A_\varepsilon)_{KK})
 \le \|v_K\|^2
      +\varepsilon\|w_Kp_K^\mathsf T+p_Kw_K^\mathsf T\|
 \le (3+2\varepsilon)N/m.
\]
The omitted hub–partner part has rank at most two on \(K\).

* For every physical cut \(S|T\), the crossing block of \(A_0\) has rank at most two. The perturbation has operator norm \(\varepsilon\). Thus
\[
s_3((A_\varepsilon)_{ST})\le\varepsilon.
\]
Since \(A_\varepsilon\) has rank three,
\[
Z_3((A_\varepsilon)_{ST})
=\prod_{j=1}^3s_j((A_\varepsilon)_{ST})^2
\le(1+\varepsilon^2)^2\varepsilon^2.
\]

* No principal bank \(S\) carries an exact rank-one square of coefficient bounded below. A hub–light principal pair has determinant \(-1/m\). For distinct light \(i,j\), writing \(\Delta(a,b)=a_ib_j-a_jb_i\), the principal-pair determinant is
\[
2\varepsilon\Delta(v,w)\Delta(v,p)
   -\varepsilon^2\Delta(w,p)^2.
\]
If \(s_i=s_j\), this is
\(2\varepsilon s_i(v_i-v_j)^2/m\ne0\).
If \(s_i=-s_j\), it is
\[
{2\varepsilon s_j\over m}(v_i^2-v_j^2)
       -{4\varepsilon^2\over m^2}.
\]
A nonzero root in \(\varepsilon\) has magnitude
\(m|v_i^2-v_j^2|/2\ge6/(m^2-1)>m^{-3}\);
when \(v_i^2=v_j^2\), the second term is nonzero. Hence every principal pair minor is nonzero for the chosen \(\varepsilon\), and every principal bank of at least two coordinates has rank at least two. A singleton light-bank square has coefficient at most \(3/m+2/m^4\), and the hub diagonal is zero.

These statements refute only the indicated structural trichotomy. They do not supply a high-density example.

## 3. The same family has a uniform receiver

Partition light coordinates into \(I_+=\{j:s_j=1\}\) and \(I_-=\{j:s_j=-1\}\). Put \(L_\pm=w_{I_\pm}\cdot X_{I_\pm}\) and \(V_\pm=v_{I_\pm}\cdot X_{I_\pm}\). Then
\[
L=L_++L_-,\qquad V=V_++V_-,\qquad
P=L_+-L_-,
\]
and therefore the leakage factors *within* the independent banks:
\[
LP=L_+^2-L_-^2. \tag{5}
\]
The pattern is invariant under reflection \(j\mapsto m+1-j\), whereas \(v\) changes sign, so \(w_{I_\pm}\cdot v_{I_\pm}=0\). Directly summing squares over each four-index block gives
\[
G_\pm=\operatorname{diag}\left({1\over2},{1\pm d_m\over2}\right),
\qquad d_m={12\over m^2-1}\le{4\over5}. \tag{6}
\]
Equation (4) yields
\[
M_\pm\le {4\over\sqrt{1\pm d_m}},\qquad
M_+M_-\le {16\over\sqrt{1-d_m^2}}\le {80\over3}.
\]
Take \(G_\pm(X_{I_\pm})=\pm2\varepsilon L_\pm^2\), plus arbitrary original-coordinate affine terms on each bank, in Theorem (1), with \(\kappa=\lambda=K_H=1\). For every \(m\) and every real \(\varepsilon\), the form
\[
aH^2+b_hH+2H L+V^2+2\varepsilon LP
       +b_{\rm light}\cdot X'+c
\]
has density satisfying
\[
\boxed{\quad\|p_Q\|_\infty
\le3(80/3)^{1/3}<9.\quad}
\]
The statement permits arbitrary real \(a,b_h,b_{\rm light},c\), and arbitrary independent cap-one input densities. The structural obstruction and the uniform density bound are therefore compatible.

## 4. Boundary of this mechanism

The factorization (5) uses \(p_j=w_j\) on one bank and \(p_j=-w_j\) on the other. If instead \(p_j=\alpha w_j\) on one bank and \(p_j=\beta w_j\) on the other, then
\[
LP=\alpha L_+^2+\beta L_-^2+(\alpha+\beta)L_+L_-.
\]
The mixed term vanishes only when \(\alpha+\beta=0\). A general diffuse orthonormal pair \(w,p\) has no such exact two-bank partition. Controlling the mixed term uniformly as its coefficient tends to zero requires a further product-source estimate; the theorem here does not supply it.
