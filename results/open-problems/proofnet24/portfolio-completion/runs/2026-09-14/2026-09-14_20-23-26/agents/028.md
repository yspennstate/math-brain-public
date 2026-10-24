# Agent 028: a diagonal construction for the critical infinite-variance degree-count problem

Date: 2026-09-14. Track: Janson Problem 20.2, critical infinite variance; Thévenin's closing conjecture. Assigned by agent 011. Internal inputs read: `SESSION.md`, `repository-policy.md`, `agents/001.md`, `agents/015.md`, and the complete archival F0064 memo under `computations/001_sources/downloads_memos/`. The archival source snapshot is `8861ffde776a1dbf842e918590cc1003492ff296`, as documented in the supplied reports. No child agents, GitHub writes, shared-manuscript edits, or third-party contacts were used.

**Result in this report: a complete recursive construction and proof, awaiting independent mathematical audit.** It gives one fixed, explicitly specified critical offspring law with infinite variance for which the centered degree-one count has the subsequential limit

\[
\frac12\mathcal N(-1,3/16)+\frac12\mathcal N(1,3/16).
\tag{1}
\]

The construction uses a finite-stage diagonal selection rule. Every selection test involves an already fixed finite probability distribution and a finite coefficient calculation, together with explicit elementary or Gaussian functions. Nonemptiness of every stage's selection set is proved. Thus an unproved uniform triangular-array moderate-deviation estimate is not an input. The support sizes need not have a practical closed formula, and no practical computation of the full law is claimed.

The fixed law, exact mean, all competing rare-atom counts, dependence between degree counts and sums, future changes to the zero mass, branch odds, and final centering are treated below. Source hypotheses are checked in Section 11. This is a repair of an archived proposal and not a claim of literature priority or current open status.

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

Choose \(n_r\) to be the smallest power of two satisfying all the following tests. Every law in the tests is the already fixed law \(Q^{(r-1)}\).

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

This completely specifies the stage selection. Tests G2 and G3 are finite probability calculations, not references to an unspecified asymptotic approximation. More explicitly, if

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

This recursive minimum is a mathematically explicit definition. If an effective implementation avoiding undecidable equality comparisons is desired, use dovetailed rational interval certificates for strict versions of (15)–(19), and select the first certified candidate in a fixed enumeration of candidate/precision pairs. The proof below works unchanged with that deterministic selection. Strict certificates eventually exist because all tests hold with slack for sufficiently large candidates. No numerical efficiency is asserted.

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

For completeness, let \(H_0=0\) and \(H_j=\sum_{i\le j}(x_i-1)\). The desired starting point is the first minimum among \(H_0,\ldots,H_{n-1}\). Later heights are at least that minimum. Earlier heights are strictly larger integers, which also ensures the wrapped partial sums are nonnegative after the total decrement \(-1\). Conversely those two inequalities force the first minimum. A nontrivial cyclic period is impossible because the total increment sum is \(-1\).

The conditional independent-sample weights are proportional to \(\prod_i\pi_{x_i}\) and are rotation invariant. Every orbit has \(n\) elements and exactly one tree sequence. The selected tree has weight proportional to the same product, which is precisely the conditioned Galton–Watson law. Counts of fixed degrees are invariant under the rotation. Therefore (3) transfers unchanged from the conditioned sample to \(T_{n_r}\).

The path of length \(n-1\) has probability \(\pi_1^{n-1}\pi_0>0\); all sizes are admissible. Criticality and nondegeneracy imply the unconditioned tree is finite almost surely, although only the positivity of these finite-size probabilities is needed here.

## 10. What this repairs, and what the diagonal rule does not claim

| Obligation in the critical audit | Resolution in this report |
|---|---|
| Incorrect independence of the one count and medium total | Use the joint Fourier conditional CLT with covariance \(q\Delta_r\), Sections 2 and 8 |
| Disappearing covariance as the background approaches mean one | Enlarge the selected sum displacement by \(V_r/(q\Delta_r)\), equations (14), (22), and (23) |
| Unproved uniform local moderate deviations | Fix each finite background, prove the ordinary conditional CLT, then enforce finite-error diagonal tests G2 and G3 |
| Exact mean one with integer support | Add an integer atom \(H_r=n_r^4\) with the exactly determined positive probability (25); sum the geometric mean increments |
| Adjustment atom destroys previous maximum-support estimate | Carry the actual maximum \(M_{r+1}=n_r^4\) into every later selection and Bernstein bound |
| Future probabilities alter the bulk zero mass | Pointwise multiplicative product comparison (38)–(40), uniform even for tiny events |
| Unequal branch weights from skew or floors | Equal probabilities plus opposite finite-law Gaussian targets; G2 controls relative errors, (43)–(44) |
| Zero-current-pair route competes with the small denominator | Whole-sum Bernstein estimate compared directly with \(w_r\) in G4 |
| Two or more current-pair atoms are possible in the critical regime | One factorial-moment bound for the sum over all such counts, and G5 |
| Current adjusting or future atoms | Deterministically exceed the conditioned total |
| Infinite variance, possible additional moments | Exact first moment; every higher positive moment infinite; Section 5 |
| Final count centering | Exact identity (49), with fixed \(q\) in every partial law |
| One fixed law rather than separate examples at each size | The recursive minimum is chosen before the next stage; positive atom masses never change |

The construction is deliberately much more lacunary than the original sketch. It does not give a practical growth rate or a full-sequence limit, and it does not repair the original memo's displayed moderate-deviation theorem as a general theorem. It proves the needed existence assertion by a different, elementary diagonal route.

No moment convergence for the degree-count limit is inferred merely from weak convergence. No statement is made about a macroscopic condensate at all sizes. Along the selected sizes, (27) implies that the single current atom has degree \((1+o(1))n_r\Delta_r=o(n_r)\), while all other degrees are at most \(M_r\le\varepsilon_r n_r\Delta_r\). This optional consequence follows directly from the same event in (47), and is a mesoscopic, not a macroscopic, separation.

## 11. Primary-source hypothesis check and status limits

Primary sources inspected through the web on 2026-09-14:

1. [Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510](https://arxiv.org/pdf/1112.0510), Problem 20.2, printed page 135 in the fetched version. Its critical infinite-variance question asks whether the displayed Gaussian degree-count results extend to this regime. Equations (2)–(3) provide a negative example for degree one. They do not classify possible fluctuations or settle the other open-ended parts of the problem.

2. [Paul Thévenin, *Vertices with fixed outdegrees in large Galton–Watson trees*, arXiv:1812.07365](https://arxiv.org/pdf/1812.07365), version 2 dated 26 February 2020, Theorems 6.1–6.2 and the final conjecture on printed page 23. The final conjecture proposes the centered Gaussian count limit for arbitrary critical laws of infinite variance. Its singleton choice \(A=\{1\}\) predicts \(\mathcal N(0,\pi_1(1-\pi_1))\). Our law meets those criticality, variance, and span hypotheses, while (3) gives a different limit. The proved theorems have stable-domain hypotheses and are not contradicted by this argument.

The versioned PDF URL `https://arxiv.org/pdf/1812.07365v2` returned a fetch error during this worker's check. The unversioned PDF fetched successfully and its first-page text identifies it as v2, dated 26 February 2020; the [arXiv abstract record](https://arxiv.org/abs/1812.07365) also identifies that version. No claim of external verification is based on the failed fetch.

This source check verifies the mathematical match to the stated conjecture. It is not an exhaustive search for later literature, priority, or a present-day open-status certificate. No outside researcher has checked this proof in this worker's session. Independent audit of the diagonal selection rule and conditioning comparison should precede promotion to a manuscript or public solution announcement.

## 12. Ledger and computation limits

| Claim | Status within this report | Evidence |
|---|---|---|
| Fixed-law conditional CLT used by the construction | PROVED | Fourier proof in Section 2; agrees with agent 001's lemma |
| Every finite stage has a valid selected size | PROVED | Section 3's fixed-law limits and explicit competing-route comparisons |
| One well-defined fixed law with integer, noncolliding support | PROVED | Sections 3–4 |
| Exact mean one, positive zero and one masses, span one | PROVED | Sections 4–5 |
| Infinite variance and every \(1+\varepsilon\) moment infinite | PROVED | Equation (35) and support growth |
| Future-stage changes remain negligible after rare conditioning | PROVED | Pointwise likelihood-ratio bounds (38)–(40) |
| Zero and all multiple-current-pair routes negligible | PROVED | (45)–(46), with stage gates comparing to the exact branch scale |
| Single-current-pair route and fair limiting sign | PROVED | (43)–(47) |
| Conditional branch limits and exact count centering | PROVED | G3, (36), and (48)–(49) |
| Non-Gaussian tree degree-count subsequence limit | PROVED | (47)–(50) and the exact cyclic transfer |
| Literal critical closing-conjecture hypothesis match | VERIFIED | Primary sources in Section 11 |
| Uniform moderate-deviation theorem for arbitrary arrays | NOT CLAIMED | Bypassed by finite-stage diagonal selection |
| Practical enumeration of the entire offspring law | NOT CLAIMED | Stage sizes can be extraordinarily large |
| Novelty, present-day open status, independent proof audit | NOT CLAIMED | Outside this bounded proof construction |

The mathematical proof does not depend on numerical simulation, a finite-stage toy, or software output. **No numerical stage search was executed in this worker's session; the sequence of selected stage sizes has not been computed.** The fixed law is specified by the finite-test recursion, and existence of every selected stage is proved in Section 3. The exact initial arithmetic \(\mu_1=1/2\), \(V_1=1/2\), and \(v_1=5/32\) was checked algebraically. There is no numerical certificate being substituted for a proof, and no claim that all stages were actually enumerated.

The final internal review rechecked: the sign and scale in (22)–(23); positivity and exact mean in (25)–(31); the actual previous maximum \(M_{r+1}=n_r^4\); the future-mass product ratio even on very small conditioning events; the binomial factorial-moment bound summed over all multiple-current-pair routes; and the change from \(N=n-1\) to \(n\) in (49). No additional assumption was introduced by those checks. Agent 011 suggested the factorial-moment simplification in (46), which replaces the longer possible lower-tail sum over current rare counts.

**No remaining mathematical gate in the bounded construction is being left as an assumption.** The substantive remaining action is independent audit, especially of the use of a stage-dependent but fixed-during-selection Gaussian target, not another unproved tail or normalization estimate.
