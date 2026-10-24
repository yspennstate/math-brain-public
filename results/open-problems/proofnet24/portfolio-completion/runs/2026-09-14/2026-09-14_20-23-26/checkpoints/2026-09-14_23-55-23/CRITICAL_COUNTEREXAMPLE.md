# A critical infinite-variance offspring law with non-Gaussian degree counts

This note gives a complete counterexample to the critical infinite-variance Gaussian extension in Janson Problem 20.2 and Thévenin's closing conjecture. It integrates the construction in [agent028](agents/028.md), the complete independent audit and computable selector in [agent033](agents/033.md), the parent proof review, and the full integration audit [062](agents/062.md). Historical novelty is not certified.

The offspring law is fixed before the size of the conditioned tree varies. Its definition uses a terminating finite-stage selector. No critical-stage integers were computed; the theorem is an analytic existence and computability result, not a numerical experiment.

## 1. The precise theorem

There is a probability distribution \(\pi\) on the nonnegative integers such that

\[
\pi_1=\frac14,\quad \pi_2=\frac18,\quad \pi_0>\frac12,
\quad \mathbb E\xi=1,
\quad \mathbb E\xi^\alpha=\infty\quad\hbox{for every }\alpha>1,
\tag{2}
\]

where \(\xi\sim\pi\). In particular its variance is infinite, and it has no positive exponential moment. Its support has span one. Let \(T_n\) be its Galton–Watson tree conditioned to have \(n\) vertices. This conditioning is defined for every \(n\ge1\). For a deterministic sequence \(n_r\to\infty\),

\[
\frac{N_1(T_{n_r})-n_r/4}{\sqrt{n_r}}
\Longrightarrow
\frac12\mathcal N(-1,3/16)+\frac12\mathcal N(1,3/16).
\tag{3}
\]

In particular, unrestricted convergence to \(\mathcal N(0,3/16)\) is false for this law. The two components have positive variance. Their mixture is not any Gaussian distribution.

## 2. A fixed finite-law conditional local CLT

This is the constant-row special case of agent 001's proved lemma. A proof is included to make the analytical dependency explicit.

Let \(Q\) be a finitely supported distribution on \(\mathbb Z_{\ge0}\), with positive masses at 0, 1, and 2. Put

\[
q=Q(1),\quad \mu=\mathbb E_Q X,\quad V=\operatorname{Var}_QX>0,
\quad \gamma=q(1-\mu),\quad b=q(1-q),
\quad v=b-\gamma^2/V>0.
\tag{4}
\]

For independent \(Q\)-distributed variables, let \(S_N=\sum X_i\) and \(B_N=\sum\mathbf1_{\{X_i=1\}}\). If integer \(k_N\) satisfy

\[
\frac{k_N-N\mu}{\sqrt N}\longrightarrow a\in\mathbb R,
\]

then

\[
\sqrt N\,\mathbb P_Q(S_N=k_N)
\longrightarrow
\frac{1}{\sqrt{2\pi V}}e^{-a^2/(2V)},
\tag{5}
\]

and

\[
\mathcal L_Q\!\left(\frac{B_N-Nq}{\sqrt N}\,\middle|\,S_N=k_N\right)
\Longrightarrow\mathcal N\!\left(\frac{\gamma a}{V},v\right).
\tag{6}
\]

Convergence in (6) is also in Kolmogorov distance, because its limiting distribution function is continuous.

To prove the lemma, set \(Y=\mathbf1_{\{X=1\}}\). The covariance is exactly

\[
\operatorname{Cov}(Y,X)=q-q\mu=\gamma.
\tag{7}
\]

For fixed real \(s\), Fourier inversion yields

\[
\begin{split}
&\mathbb E_Q\left[e^{is(B_N-Nq)/\sqrt N};S_N=k_N\right]\\
&\qquad=\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{-it(k_N-N\mu)}
 \left(\mathbb E_Q e^{it(X-\mu)+is(Y-q)/\sqrt N}\right)^N\,dt.
\end{split}
\tag{8}
\]

After substituting \(t=u/\sqrt N\), the integrand converges pointwise to

\[
e^{-iau}\exp\{-\tfrac12(Vu^2+2\gamma us+bs^2)\}.
\tag{9}
\]

This is the ordinary quadratic characteristic-function expansion for a fixed bounded random vector. For domination, if \(\phi_N(t,s)=\mathbb E_Qe^{itX+isY/\sqrt N}\), the independent-copy identity, keeping just the atom pairs 0 and 1, gives

\[
1-|\phi_N(t,s)|^2
\ge 2Q(0)q\,[1-\cos(t+s/\sqrt N)].
\tag{10}
\]

For \(|t|\) in a fixed small neighborhood of zero this bounds \(|\phi_N|^N\) by \(e^{-cN(t+s/\sqrt N)^2}\); after substitution the bound is the integrable function \(e^{-c(u+s)^2}\). Outside that neighborhood the integrand is exponentially small uniformly in \(N\), for fixed \(s\). Dominated convergence therefore gives the Gaussian integral of (9) after multiplication of (8) by \(\sqrt N\). At \(s=0\) this is (5). Dividing the general integral by its value at zero gives

\[
\exp\left\{i\frac{\gamma a}{V}s
 -\frac12\left(b-\frac{\gamma^2}{V}\right)s^2\right\},
\]

which proves (6). Strict positivity of \(v\) follows from strict Cauchy–Schwarz: \(Y-q\) cannot be an affine multiple of \(X-\mu\), because its values agree at 0 and 2 but differ at 1.

Uniform convergence of the distribution functions follows directly from weak convergence and continuity of the Gaussian distribution function. One proof is to choose finitely many partition points making all Gaussian increments and both tails small, then use convergence at those points and monotonicity between them.

**The order of limits matters.** This lemma will be applied with the entire finite law held fixed while choosing a size at one stage. It is not asserted uniformly for all the eventual stages. The quantitative diagonal tests below provide exactly the uniformity needed along the selected sequence.

## 3. The recursive stage data and all selection tests

Start with the finite probability law

\[
Q^{(0)}(0)=\frac58,\qquad Q^{(0)}(1)=q=\frac14,
\qquad Q^{(0)}(2)=\frac18.
\tag{11}
\]

Its mean is \(1/2\), variance is \(1/2\), and the conditional variance in (4) is \(5/32\). Put \(n_0=1\). At stage \(r\ge1\), the law \(Q^{(r-1)}\) is already fixed and has mean

\[
\mu_r=1-\Delta_r,\qquad \Delta_r=2^{-r}.
\tag{12}
\]

Define from this finite law

\[
\begin{split}
M_r&=\max\operatorname{supp}Q^{(r-1)},\\
V_r&=\operatorname{Var}_{Q^{(r-1)}}X,\\
v_r&=q(1-q)-\frac{q^2\Delta_r^2}{V_r}>0,\\
\varepsilon_r&=\frac1{r+10},\\
c_r&=\frac1{\sqrt{2\pi V_r}}
       \exp\left(-\frac{V_r}{2q^2\Delta_r^2}\right)>0.
\end{split}
\tag{13}
\]

For each candidate \(n=2^\ell\), let \(N=n-1\) and define

\[
D_r(n)=\frac{V_r\sqrt N}{q\Delta_r},\qquad
L_r^\pm(n)=\left\lfloor N\Delta_r\pm D_r(n)\right\rfloor,
\qquad k_r^\pm(n)=N-L_r^\pm(n).
\tag{14}
\]

Here all support points are integers; irrationality of \(D_r(n)\) creates no mean-adjustment problem.

Choose \(n_r\) by the deterministic certificate enumeration in Section 10, accepting a power of two only when all the following tests hold. Every law in the tests is the already fixed law \(Q^{(r-1)}\). The selection does not require deciding whether a computable real number is exactly zero.

**G1: growth and support separation.**

\[
n\ge2^{8r},\qquad n\ge2n_{r-1},\qquad
M_r\le\varepsilon_r n\Delta_r,
\qquad D_r(n)+\Delta_r+1\le\varepsilon_r n\Delta_r,
\qquad L_r^-(n)<L_r^+(n).
\tag{15}
\]

**G2: both local probabilities have a prescribed relative error.** For each sign,

\[
\left|\frac{\sqrt N\,\mathbb P_{Q^{(r-1)}}(S_N=k_r^\pm(n))}{c_r}-1\right|
<\varepsilon_r.
\tag{16}
\]

**G3: both conditional count laws have a prescribed error.** Writing \(d_K\) for Kolmogorov distance,

\[
d_K\left(
\mathcal L_{Q^{(r-1)}}\left(\frac{B_N-Nq}{\sqrt N}\,\middle|\,S_N=k_r^\pm(n)\right),
\mathcal N(\mp1,v_r)
\right)<\varepsilon_r.
\tag{17}
\]

**G4: the no-current-pair route is negligible.**

\[
\exp\left\{-\frac{(n\Delta_r-1)^2}
 {2(nV_r+M_r(n\Delta_r-1)/3)}\right\}
<\varepsilon_r\,\frac{c_r n^{-3}}{\sqrt N}.
\tag{18}
\]

**G5: all routes with at least two current-pair atoms are negligible.**

\[
2n^{-6}<\varepsilon_r\,\frac{c_r n^{-3}}{\sqrt N}.
\tag{19}
\]

Together with the selector in Section 10, these gates specify the stage. Tests G2 and G3 are finite probability calculations. More explicitly, if

\[
F_r(z,u)=Q^{(r-1)}(0)+qzu+
 \sum_{j\ge2}Q^{(r-1)}(j)z^j,
\tag{20}
\]

then

\[
\mathbb P_{Q^{(r-1)}}(S_N=k,B_N=b)
=[z^ku^b]F_r(z,u)^N.
\tag{21}
\]

All its coefficients are rational. For (17), the conditional distribution has finitely many jumps, at \((b-Nq)/\sqrt N\); the supremum is the maximum of the differences from the Gaussian CDF at the left and right sides of those jumps. Therefore (17) also uses a finite list of explicitly defined numbers.

Section 10 fixes an enumeration of candidate and precision pairs and selects the first candidate whose strict gates have positive rational lower bounds. Every proof below uses only G1–G5. Existence of a passing candidate, proved next, also proves termination of that selector. No stage integer has been computed in this run, and no numerical efficiency is asserted.

### Every stage's selection set is nonempty

Hold \(r\) and \(Q^{(r-1)}\) fixed and let candidate powers of two tend to infinity. All terms \(M_r,V_r,\Delta_r,c_r,v_r,\varepsilon_r\) are fixed finite constants, with the needed ones positive. G1 eventually holds, because \(D_r(n)=O(\sqrt n)\), \(n\Delta_r\) is linear, and the earlier support is fixed. Also

\[
\frac{k_r^\pm(n)-N\mu_r}{\sqrt N}
=\mp\frac{V_r}{q\Delta_r}+O(N^{-1/2}).
\tag{22}
\]

The finite-law lemma gives (16), since (5)'s Gaussian factor is exactly \(c_r\). Equation (6) gives the target mean

\[
\frac{q\Delta_r}{V_r}
\left(\mp\frac{V_r}{q\Delta_r}\right)=\mp1,
\tag{23}
\]

and the variance is exactly \(v_r\), so (17) eventually holds. The exponent on the left of (18) grows linearly in \(n\), while its right side is a positive fixed constant times \(n^{-7/2}(1+o(1))\). Thus (18) eventually holds. Finally, the ratio of the left of (19) to its right side is

\[
\frac{2\sqrt{n-1}}{\varepsilon_r c_r n^3}=O_r(n^{-5/2})\longrightarrow0.
\tag{24}
\]

Hence (19) eventually holds as well. There are finitely many tests, so sufficiently large powers of two pass all of them. This proves nonemptiness and completes the diagonal-existence argument.

## 4. The exact probability and mean update

At the selected size write \(L_r^\pm=L_r^\pm(n_r)\), and set

\[
p_r=n_r^{-4},\qquad H_r=n_r^4,
\qquad a_r=\frac{\Delta_r/2-p_r(L_r^-+L_r^+)}{H_r}.
\tag{25}
\]

Add mass \(p_r\) at each of \(L_r^-\) and \(L_r^+\), add mass \(a_r\) at the integer \(H_r\), and subtract total mass

\[
h_r=2p_r+a_r
\tag{26}
\]

from zero. Call the resulting finite law \(Q^{(r)}\). All its probabilities are rational. No already assigned positive support mass changes at later stages.

From G1, since \(\varepsilon_r<1/10\) and \(\Delta_r\le1/2\),

\[
M_r<L_r^-<L_r^+<n_r<H_r,
\qquad
(1-\varepsilon_r)n_r\Delta_r
\le L_r^-\le L_r^+\le(1+\varepsilon_r)n_r\Delta_r.
\tag{27}
\]

For the first strict inequality, use \(M_r\le\varepsilon_r n_r\Delta_r\) and \(1-\varepsilon_r>\varepsilon_r\). The upper bound follows from \(L_r^+\le(n_r-1)\Delta_r+D_r\). Thus every stage has three fresh, disjoint support points, none equal to 0, 1, or 2. At the next stage the actual background maximum is

\[
M_{r+1}=H_r=n_r^4.
\tag{28}
\]

In particular \(n_{r+1}>n_r^4\). The adjustment atom's full size is carried into the next stage, rather than incorrectly being bounded by \(n_r\).

Since both current pair atoms are below \(n_r\),

\[
0<p_r(L_r^-+L_r^+)<2n_r^{-3}\le\Delta_r/4.
\tag{29}
\]

The final inequality follows from \(n_r\ge2^{8r}\). Consequently

\[
\frac{\Delta_r}{4H_r}<a_r<\frac{\Delta_r}{2H_r},
\qquad 0<h_r<3n_r^{-4}.
\tag{30}
\]

The mean increment is *exactly*

\[
p_r(L_r^-+L_r^+)+a_rH_r=\Delta_r/2.
\tag{31}
\]

Therefore the updated mean is \(1-\Delta_r/2=1-\Delta_{r+1}\), proving the induction used in (12). Floors in (14) cause no problem because the adjustment uses a real probability at a fixed integer atom, rather than asking an integer atom size to match a prescribed real mean with fixed probability.

Because \(n_{s+1}\ge2n_s\),

\[
\sum_{s\ge r}h_s
\le3\sum_{s\ge r}n_s^{-4}
\le\frac{3n_r^{-4}}{1-2^{-4}}
<4n_r^{-4}.
\tag{32}
\]

In particular the total mass subtracted from zero is less than \(4\cdot256^{-4}<1/8\). Every finite update remains a probability distribution, and its zero mass remains above \(1/2\).

Define the single final law by

\[
\pi_1=\frac14,\quad \pi_2=\frac18,\quad
\pi_{L_r^-}=\pi_{L_r^+}=p_r,\quad
\pi_{H_r}=a_r,\quad
\pi_0=\frac58-\sum_{r\ge1}h_r,
\tag{33}
\]

and give every other integer mass zero. Equations (25)–(33), together with the finite selection rule, define one fixed law, not an \(n\)-dependent collection of offspring laws.

## 5. Exact criticality and moment properties

The base mean is \(1/2\). Summing (31) and using nonnegativity gives

\[
\mathbb E_\pi\xi
=\frac12+\sum_{r\ge1}\frac{\Delta_r}{2}
=\frac12+\sum_{r\ge1}2^{-r-1}=1.
\tag{34}
\]

Thus the law is exactly critical. For every \(\alpha>1\), (30) gives a single-term lower bound

\[
a_rH_r^\alpha>
\frac{2^{-r}}4\,n_r^{4(\alpha-1)}.
\tag{35}
\]

The support separation gives \(n_{r+1}>n_r^4\), so
\(\log n_r\ge4^{r-1}\log256\). The logarithm of the right side of (35) tends to infinity for every \(\alpha>1\). Hence \(\mathbb E\xi^\alpha=\infty\) for every such \(\alpha\). In particular \(\mathbb E\xi^2=\infty\). For \(0<\alpha\le1\), finiteness follows from \(x^\alpha\le1+x\).

The second moments of \(Q^{(r)}\) increase to infinity. Their means are bounded by one, so

\[
V_r\longrightarrow\infty,
\qquad v_r\longrightarrow q(1-q)=3/16.
\tag{36}
\]

The law has no positive exponential moment; otherwise all its positive moments would be finite. Equivalently, one can use the adjustment terms directly:
\(a_r e^{\theta H_r}\ge 2^{-r}e^{\theta n_r^4}/(4n_r^4)\to\infty\) for every \(\theta>0\). Therefore its probability generating function has radius exactly one. For simply generated weights \(w_k=\pi_k\), the canonical law is this same \(\pi\), with \(\rho=\tau=1\), \(\Phi(1)=1\), and \(\Psi(1)=1\). Positivity at 0 and 1 gives lattice span one.

## 6. Future mass does not change the rare conditional laws

Fix stage \(r\), and abbreviate \(n=n_r\), \(N=n-1\), \(Q=Q^{(r-1)}\), and \(A=\operatorname{supp}Q\). Let

\[
\tau_r=\sum_{s\ge r}h_s<4n^{-4},\qquad z_r=Q(0)>1/2.
\tag{37}
\]

On positive points of \(A\), the final law \(\pi\) equals \(Q\) exactly. At zero it equals \(Q(0)-\tau_r\). Thus for any vector \(x\in A^k\), \(k\le n\),

\[
\prod_{i=1}^k\pi_{x_i}
=\prod_{i=1}^kQ(x_i)
\left(1-\frac{\tau_r}{z_r}\right)^{\#\{i:x_i=0\}}.
\tag{38}
\]

Consequently every such product lies between \(\eta_r\prod Q(x_i)\) and \(\prod Q(x_i)\), where

\[
\eta_r:=\left(1-\frac{\tau_r}{z_r}\right)^n
\ge1-\frac{n\tau_r}{z_r}
\ge1-8n^{-3}\longrightarrow1.
\tag{39}
\]

This is a **multiplicative** bound valid for every configuration and every event on the background coordinates, however small its probability. An additive total variation estimate of order \(n\tau_r\) alone would not suffice for an exponentially small conditional denominator. Equation (38) avoids that issue completely.

After conditioning on any positive-probability background event, the reweighted law has a density with respect to the corresponding conditioned \(Q\) law between \(\eta_r\) and \(\eta_r^{-1}\). Its total variation distance is therefore at most

\[
\eta_r^{-1}-1=O(n^{-3}).
\tag{40}
\]

This handles the recursive dependence on the final zero probability; no exact knowledge of future support or probabilities was needed in the finite-stage CLT tests.

## 7. Conditioning decomposition, both branch weights, and every other rare count

Take independent variables \(\xi_1,\ldots,\xi_n\) with the final law \(\pi\), and put

\[
\mathcal C_r=\left\{\sum_{i=1}^n\xi_i=n-1\right\}.
\tag{41}
\]

The current adjustment atom is \(H_r=n_r^4>n_r\). Every future support point exceeds \(H_r\), by (27)–(28) and induction. Hence no current adjustment atom and no future atom can occur on \(\mathcal C_r\), exactly. Earlier adjustment atoms are allowed and are included in \(Q\), with maximum \(M_r\).

Let \(J_r\) be the number of current-pair atoms, namely coordinates equal to \(L_r^-\) or \(L_r^+\). On \(\mathcal C_r\), every coordinate is either in the background \(A\) or is a current-pair atom. The possibilities \(J_r=0,1,2,\ldots\) exhaust the conditioning event. Unlike the subcritical construction, multiple current-pair atoms are not declared impossible.

Write \(\beta_r^\pm\) for the joint probability of \(\mathcal C_r\) and exactly one current-pair atom, with sign \(\pm\). Put

\[
w_r:=np_r\frac{c_r}{\sqrt N}
=\frac{c_r n^{-3}}{\sqrt N}>0.
\tag{42}
\]

By (38),

\[
\eta_rnp_r\mathbb P_Q(S_N=k_r^\pm)
\le\beta_r^\pm
\le np_r\mathbb P_Q(S_N=k_r^\pm).
\tag{43}
\]

The factor \(n\) counts the position of the single current-pair atom. Using G2,

\[
\eta_r(1-\varepsilon_r)w_r
\le\beta_r^\pm\le(1+\varepsilon_r)w_r.
\tag{44}
\]

Thus both branch probabilities are asymptotic to the **same** changing quantity \(w_r\). The two Gaussian local densities agree at opposite targets, and the finite selection tests make that symmetry accurate enough; no unproved exact symmetry or recursive unequal-probability adjustment is used.

For the route \(J_r=0\), (38) gives

\[
\begin{split}
\mathbb P(\mathcal C_r,J_r=0)
&\le\mathbb P_Q(S_n=n-1)\\
&\le\exp\left\{-\frac{(n\Delta_r-1)^2}
 {2(nV_r+M_r(n\Delta_r-1)/3)}\right\}
<\varepsilon_rw_r.
\end{split}
\tag{45}
\]

The middle inequality is the usual Bernstein bound for independent bounded centered summands. Here \(0\le X\le M_r\), \(|X-\mu_r|\le M_r\), variance is exactly \(V_r\), and the required excess is \(n\Delta_r-1>0\). A direct derivation is to use

\[
\log\mathbb Ee^{t(X-\mu_r)}
\le\frac{t^2V_r}{2(1-tM_r/3)},\qquad0<t<3/M_r,
\]

which follows by expanding the exponential and using \(k!\ge2\cdot3^{k-2}\) for \(k\ge2\), then optimize with \(t=D/(nV_r+M_rD/3)\), where \(D=n\Delta_r-1\). This proves the displayed bound without another local-limit input. The last inequality is G4.

For **all** routes \(J_r\ge2\), use the unconditional factorial moment of the current-pair count. In the independent final sample, \(J_r\sim\operatorname{Bin}(n,2p_r)\). Therefore

\[
\begin{split}
\mathbb P(\mathcal C_r,J_r\ge2)
&\le\mathbb P(J_r\ge2)
\le\frac12\mathbb E[J_r(J_r-1)]\\
&=\binom n2(2p_r)^2
\le2n^2p_r^2=2n^{-6}<\varepsilon_rw_r.
\end{split}
\tag{46}
\]

The last inequality is G5. This bounds the sum of *every* possible current-pair count at least two in one step. It does not assume that the number of allowable rare atoms is uniformly bounded, and it does not factor category counts.

Combining (44)–(46) gives

\[
\mathbb P(\mathcal C_r)=2w_r(1+o(1)),
\quad
\mathbb P(J_r=1\mid\mathcal C_r)\longrightarrow1,
\quad
\mathbb P(\text{single sign}=\pm\mid\mathcal C_r)\longrightarrow\frac12.
\tag{47}
\]

For example, the total conditional probability of the bad routes is at most
\(\varepsilon_r/[\eta_r(1-\varepsilon_r)]\), which tends to zero. Even if \(c_r\) tends to zero extraordinarily quickly, (18)–(19) compare both errors directly with \(w_r\). This is the denominator comparison absent from the archival critical sketch.

## 8. Conditional count limits and centering

On a single-sign branch the other \(N=n-1\) coordinates lie in \(A\), and their sum is \(k_r^\pm\). The current atom is not one, so the total count of ones is the background count \(B_N\).

Under \(Q\), G3 gives Kolmogorov distance less than \(\varepsilon_r\) from \(\mathcal N(\mp1,v_r)\) for \((B_N-Nq)/\sqrt N\). Equation (40) changes this by at most \(O(n^{-3})\) under the true final law and the same branch conditioning. By (36), this proves

\[
\mathcal L\left(\frac{B_N-Nq}{\sqrt N}\,
\middle|\,\mathcal C_r,\text{single sign }\pm\right)
\Longrightarrow\mathcal N(\mp1,3/16).
\tag{48}
\]

The requested centering is \(nq\), not \(Nq\). The exact conversion is

\[
\frac{B_N-nq}{\sqrt n}
=\sqrt{\frac{N}{n}}\,\frac{B_N-Nq}{\sqrt N}
 -\frac q{\sqrt n}.
\tag{49}
\]

Both changes vanish in the limit. No normalization of the background one mass, and no hidden \(\sqrt n\)-order correction from future stages, is present; the one probability of every partial law is exactly \(q\), and (38) handles the final restriction multiplicatively.

Combining (47) and (48)–(49) against bounded continuous test functions yields (3) for the independent sample conditioned on its sum. Its limiting characteristic function is

\[
e^{-3t^2/32}\cos t.
\tag{50}
\]

It vanishes at \(t=\pi/2\), whereas the characteristic function of every Gaussian probability distribution is nonzero everywhere. Thus the limit is non-Gaussian.

### Why the vanishing critical covariance is not an obstruction

The background covariance is \(q\Delta_r\), which tends to zero. The target sum displacement is chosen as

\[
\frac{k_r^\pm-N\mu_r}{\sqrt N}
\simeq\mp\frac{V_r}{q\Delta_r}.
\tag{51}
\]

Its product with the regression coefficient \(q\Delta_r/V_r\) remains \(\mp1\). Equation (23), not the incorrect covariance \(q(1-q)\), is the reason for the separation in (14). At a heuristic tilt level the required parameter is \(\mp1/(q\Delta_r\sqrt n)\), but no heuristic tilt calculation is needed for the proof. The diagonal procedure ensures that every finite-stage Gaussian assertion remains sufficiently accurate at that stage's very large, fixed standardized displacement.

## 9. Transfer to conditioned Galton–Watson trees

The transfer of degree counts is exact. A vector of nonnegative integers \((x_1,\ldots,x_n)\) summing to \(n-1\) has increments \(x_i-1\) summing to \(-1\). Exactly one of its cyclic rotations has all partial sums nonnegative before the final step; that rotation is the depth-first offspring sequence of a plane rooted tree.

For completeness, let \(H_0=0\) and \(H_j=\sum_{i\le j}(x_i-1)\). The starting point is the first minimum, indexed by \(j\), among \(H_0,\ldots,H_{n-1}\). Later heights before the endpoint are at least that minimum. If the original endpoint is encountered before the final rotated step, then \(j>0\), so \(H_j<0\) and integrality gives \(H_j\le-1=H_n\). Earlier heights are strictly larger integers, making the wrapped partial sums \(-1-H_j+H_\ell\) nonnegative for \(\ell<j\). Conversely these inequalities force the first minimum. A nontrivial cyclic period is impossible because the total increment sum is \(-1\).

The conditional independent-sample weights are proportional to \(\prod_i\pi_{x_i}\) and are rotation invariant. Every orbit has \(n\) elements and exactly one tree sequence. The selected tree has weight proportional to the same product, which is precisely the conditioned Galton–Watson law. Counts of fixed degrees are invariant under the rotation. Therefore (3) transfers unchanged from the conditioned sample to \(T_{n_r}\).

The path of length \(n-1\) has probability \(\pi_1^{n-1}\pi_0>0\); all sizes are admissible. Criticality and nondegeneracy imply the unconditioned tree is finite almost surely, although only the positivity of these finite-size probabilities is needed here.

## 10. The terminating computable selector

Fix a stage and omit its subscripts: \(Q=Q^{(r-1)}\), \(\Delta=2^{-r}\), \(V=V_r\), \(M=M_r\), \(v=v_r\), \(\varepsilon=\varepsilon_r\), and \(c=c_r\). Write
\[
E_r(n)=\frac{(n\Delta-1)^2}{2(nV+M(n\Delta-1)/3)}.
\]
A literal least-passing-power rule is well-defined by Section 3, but strict comparisons of computable real numbers do not by themselves provide a terminating decision for a rejected equality case. The selector below avoids such decisions. It was supplied and independently justified in agent033.

### 10.1 Exact finite formula for the G3 distance

All probabilities in the fixed finite law \(Q\) are rational. With

\[
F(z,u)=Q(0)+qzu+\sum_{j\ge2}Q(j)z^j,
\]

define, for each chosen target \(k\),

\[
P_{k,b}=[z^ku^b]F(z,u)^N,
\quad P_k=\sum_{b=0}^N P_{k,b},
\quad C_b=\frac{\sum_{j=0}^bP_{k,j}}{P_k},\quad C_{-1}=0.
\tag{A17}
\]

These are rational and are obtained by a finite exact calculation. At a G1-passing candidate, the bounds \(L^->(1-\varepsilon)n\Delta>M\) and \(L^+\le(1+\varepsilon)n\Delta<n\) imply \(0\le k^\pm\le N\). The target is attained by \(k^\pm\) ones and \(N-k^\pm\) zeros, both of which have positive \(Q\)-mass. Thus \(P_k>0\) before any conditional probability is evaluated. Let

\[
x_b=(b-Nq)/\sqrt N,\qquad
G(x)=\Phi((x-m)/\sqrt v),\qquad m=\mp1.
\]

Then the exact Kolmogorov distance in G3 is

\[
K=\max_{0\le b\le N}
\max\{|C_b-G(x_b)|,\ |C_{b-1}-G(x_b)|\}.
\tag{A18}
\]

Between two consecutive possible count values the discrete CDF is constant and \(G\) is increasing, so its maximum absolute difference occurs at an endpoint. The two unbounded tails are covered by the first and last endpoints, their limits at infinity being zero. Formula (A18) remains valid if some count values have zero probability.

### 10.2 Uniformly computable positive margins

The finite-stage mean and variance are rational. All floor arguments in (14) are algebraic numbers; their floors and all the G1 comparisons are decidable exactly by algebraic-number arithmetic. In fact, for eligible \(n=2^\ell\) with \(\ell\ge8\), \(N=2^\ell-1\) is not a square, since it is 3 modulo 4. The nonzero rational multiple \(D\) of \(\sqrt N\) is irrational. No ambiguous floor equality arises.

For a G1-passing candidate define the six margins

\[
g_{2,\pm}=\varepsilon-
\left|\frac{\sqrt N P_{k^\pm}}{c}-1\right|,
\qquad
g_{3,\pm}=\varepsilon-K_\pm,
\]

\[
g_4=\varepsilon c n^{-3}/\sqrt N-e^{-E_r(n)},
\qquad
g_5=\varepsilon c n^{-3}/\sqrt N-2n^{-6}.
\tag{A19}
\]

These are uniformly computable real numbers from the finite stage data and candidate exponent. Rational operations, positive square roots, the exponential, and the normal CDF can all be enclosed by rational intervals of any requested error. For the last function one may use its defining Gaussian integral, Taylor approximation on a finite interval, and an elementary Gaussian tail bound; all arguments here are finite and computable. Finite maxima and absolute values preserve computability. The positive denominator \(c\) permits computable division by refinement until a positive lower bound is found.

Thus, for each candidate and precision \(j\), a terminating finite calculation produces an enclosing rational interval of width at most \(2^{-j}\) for each margin. A strictly positive lower endpoint is a sound certificate for that gate. Margins equal to zero never receive such a certificate, which is exactly appropriate for strict gates.

### 10.3 Deterministic algorithm

Fix once and for all a deterministic rational-interval evaluator for (A18)–(A19), using the explicit convention in [audit062, Section5.3](agents/062.md): rational bisection for square roots, the alternating Gregory series for the circle constant, Taylor series with the displayed rational remainder bounds for exponentials and the Gaussian integral, and increasing internal precision until all denominator intervals are positive and every final interval has the requested width. Use the written expression order and the first admissible cutoff at each stage. This is a mathematical specification; no stage computation is claimed. Fixing the evaluator removes dependence of the selected law on arbitrary enclosure choices.

At stage \(r\), let \(\ell_0\) be the least integer for which
\(2^{\ell_0}\ge\max(2^{8r},2n_{r-1})\). Enumerate pairs
\((\ell,j)\), \(\ell\ge\ell_0\), \(j\ge1\), by increasing
\((\ell-\ell_0)+j\), breaking ties by increasing \(\ell\).

For each pair:

1. Check G1 exactly. If it fails, continue to the next pair.
2. Compute the finite rational probabilities (A17), the exact formula (A18), and rational enclosures of all six margins (A19) at precision \(j\).
3. If all lower endpoints are positive, choose \(n_r=2^\ell\) and end this stage. Otherwise continue.

Each visit performs only finite work. Section 3 gives an exponent \(\ell\) with G1 and all six strict margins positive. For that exponent, sufficiently large \(j\) certifies every margin. The specified enumeration reaches that pair after finitely many visits, so the algorithm terminates. This proves termination inductively at every stage, even though no usable running-time bound is claimed.

The selected candidate satisfies the original G1–G5. Every subsequent proof uses only those gates, not minimality of the exponent. Therefore this algorithm defines a fixed law satisfying (2)–(3). It may differ from the law selected by the literal least-passing-power definition in agent028; that distinction does not change the theorem. This note adopts this certificate selector throughout.

### 10.4 Computability of the resulting infinite law

Under the certificate selector, every finite list of support points and positive masses is computable exactly, and the masses are rational. The support strictly increases past each stage maximum. To determine \(\pi_k\) for an integer \(k>0\), generate stages until a maximum \(H_R\ge k\); every later positive point exceeds \(H_R\), so membership and mass are decided by a finite list.

The only infinite sum in a mass is at zero. Since \(h_s<3n_s^{-4}\) and \(n_s\ge2^{8s}\), its omitted tail after stage \(R\) is bounded by

\[
\sum_{s>R}h_s
<\frac{3\,2^{-32(R+1)}}{1-2^{-32}}.
\tag{A20}
\]

This is an effective tail bound tending to zero. It proves that \(\pi_0\), and hence the whole law, is computable. Nothing in this argument asserts that a selected critical-stage integer has actually been computed.

## 11. Direct exclusion of stable-domain hypotheses

This is an independent check, not an appeal to the counterexample conclusion. Let

\[
U(x)=E_\pi[\xi^2\mathbf1_{\{\xi\le x\}}],\qquad
W(x)=\operatorname{Var}_\pi(\xi\mathbf1_{\{\xi\le x\}}).
\]

At \(H=H_r=n_r^4\), the interval \((H/2,H)\) contains no support point: the current pair is below \(n_r<H/2\), all earlier points are smaller still, and all future points exceed \(H\). Therefore

\[
U(H/2)=E_{Q^{(r-1)}}X^2+p_r((L_r^-)^2+(L_r^+)^2)
\le M_r+2n_r^{-2}
\le\varepsilon_r n_r\Delta_r+2n_r^{-2}.
\tag{A40}
\]

On the other hand, \(U(H)\ge a_rH_r^2>\Delta_r n_r^4/4\). Since all truncated first moments are at most \(E_\pi\xi=1\),

\[
\frac{W(H_r)}{W(H_r/2)}
\ge
\frac{\Delta_r n_r^4/4-1}
{\varepsilon_r n_r\Delta_r+2n_r^{-2}}
\longrightarrow\infty.
\tag{A41}
\]

The denominator is positive because the law has positive masses at 0 and 1. The divergence follows from \(n_r\ge2^{8r}\), \(\Delta_r=2^{-r}\), and \(\varepsilon_r=1/(r+10)\). If \(W(x)\) were regularly varying with a finite exponent \(2-\alpha\), its ratio at \(H_r\) and \(H_r/2\) would converge to \(2^{2-\alpha}\), a finite number. Thus this law fails the truncated-variance regular-variation condition for every \(\alpha\in(1,2]\), including the normal domain with infinite variance.

## 12. Original conjecture match and exact scope

[Janson's original paper](https://arxiv.org/pdf/1112.0510), Problem 20.2 on printed page 135, asks about extending its Gaussian degree-count limit to critical laws with infinite variance. [Thévenin's paper](https://arxiv.org/pdf/1812.07365), version 2 of 26 February 2020, states the corresponding unrestricted critical conjecture on printed page 23. For the degree set \(\{1\}\), the proposed centered limit is \(\mathcal N(0,3/16)\). The fixed law above has the required criticality, infinite variance, nondegeneracy and span, and (3) contradicts that limit. The original papers' proved theorems retain further tail hypotheses; Section 11 shows directly why their stable-domain hypotheses do not hold here.

Agents033 and062 independently retrieved both primary sources and checked the literal hypotheses. This is a negative example for the specified Gaussian extension, not a classification of every possible critical fluctuation law. No full-sequence limit or moment convergence of the count is asserted. Along the selected sizes, with conditional probability tending to one, the dominant rare degree has size \((1+o(1))n_r\Delta_r=o(n_r)\) and the remaining degrees are at most \(M_r\le\varepsilon_r n_r\Delta_r\).

The complete derivations, archival proposal, rejected approaches and audit details are retained in reports001, 028 and 033. The optional law selected by the original literal minimum need not be the same law as this note's certificate-selected version. Both satisfy G1–G5 and the theorem's conclusion. Computability here refers specifically to the selector in Section 10. No practical stage computation, proof-assistant verification, external referee acceptance, or worldwide priority is claimed.
