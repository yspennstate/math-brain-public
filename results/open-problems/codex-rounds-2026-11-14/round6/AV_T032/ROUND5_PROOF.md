# The conditional reference law after exposure and allocation

The source is OpenAI, *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026), [Section 7](sources/groups-current.tex), Lemma 7.2. The input is the displayed thermal slab density in [Section 5](sources/slab-current.tex), equation `eq:thermal-slab-law`. The argument below verifies the conditional-law step from that density; it does not prove the estimates used to obtain certificates, routes, or condensation.

## Source statement

```tex
\begin{lemma}[Exact conditional law]\label{lem:conditional-law}
For almost every exposed datum the normalizers in
Equation~\eqref{group:reference} are positive, and the conditional law
of the unexposed trajectories is
\begin{equation}\label{group:product-law}
 \lambda_{\mathcal I}(\dd\omega_{\mathcal I})
 =\frac{1}{Z_{\mathcal I}}
   \ind_{\{\text{all pairs in $\mathcal I$ avoid each other}\}}
   \prod_{i\in\mathcal I}P_i(\dd\omega_i),
 \qquad Z_{\mathcal I}>0.
\end{equation}
All reference trajectories obey their own regularity and confinement
cutoffs.  Each label has at most $C M$ other labels in this group with
which a collision can be possible, where $C$ is a fixed geometric
constant.
\end{lemma}
```

## 1. Recheck of the preceding result

Round 4 established the single-replacement bound

\[
Q(\mathcal C_v\cap\mathcal H(c))
 \le Ctr+CrD^{3\gamma}h_0^{-1/2}
 =C\alpha(tD^{-1}+D^{-1/4})
\tag{1}
\]

for a deterministic regular opponent, fixed \(t>0\), sufficiently large \(D\), and \(K>50\). Here \(r=\alpha/D\), \(h_0=D^{-1}\), and \(\gamma=1/12\). Its full derivation is preserved in [ROUND4_PROOF.md](ROUND4_PROOF.md). The following independently recovers the terms and the dependence argument.

For a generator-\(\Delta\) bridge of duration \(H\), the covariance is
\(C_H(a,b)=2(\min(a,b)-ab/H)I\). At time \(s\), with \(L=H-s\), subtract the conditional mean from the increment:

\[
X_{s+q}=X_s+\frac qL(z-X_s)+R_q.
\]

Substitution in \(C_H\) gives
\(\operatorname{Cov}(X_s,R_q)=0\) and
\(\operatorname{Cov}(R_q,R_{q'})=2(\min(q,q')-qq'/L)I\).
Thus \(R\) is independent of \(X_s\), and represents a centered bridge restricted to an interval of length \(\tau\le r^2\). Write \(R_q=W_q-(q/L)W_L\). Brownian scaling and the maximal fourth-moment inequality give
\(\mathbb E(r^{-1}\sup_{q\le\tau}|R_q|)^3\le C\); the contribution of the second term is bounded by
\(C\tau^3/(r^3L^{3/2})\le C\).

The two endpoint windows cannot contain a collision: each path moves at most \(s_0/8\), giving separation greater than \(3s_0/4>r\). On a contributing mesh interval the oriented start therefore satisfies \(s\ge h_0/2\). If the trial is confined and collision occurs, the obstacle has a unique local lift near \(v\): its interval displacement is at most \(rD^\gamma<1\), while \(K>50\). The drift of the trial over that interval is at most \(C\tau/t\le r\), after increasing \(D\). A necessary condition for collision is that \(X_s\) lie in a ball of radius
\(r(2+A_k(c)+r^{-1}\sup|R|)\) about a deterministic center.

On the first half of either duration-\(t\) leg, the starting-position density is at most \(Cs^{-3/2}\), even after fixing its midpoint. Independence of \(R\) then gives an interval bound
\(Cr^3(1+A_k(c))^3s^{-3/2}\).
On the second half of a leg with a uniform midpoint \(U\), write
\(X_s=(1-s/t)y+(s/t)U+\beta_s\).
Conditional on the whole centered bridge \(\beta\), the position density is at most \((t/s)^3\le8\). The centered increment has bounded third maximal moment on the \(r\) scale. Integrating over \(U\) first gives the interval bound \(Cr^3(1+A_k(c))^3\). This does not assert independence between position and increment in that half.

There is a direct integral bound for the early sum. Put \(n=\lceil h_0/(2\tau)\rceil\). For \(s=j\tau\) with \(j\ge n\ge1\),

\[
s^{-3/2}\le\frac{2^{3/2}}\tau
 \int_s^{s+\tau}x^{-3/2}\,dx,
\qquad
\sum_{j\ge n}(j\tau)^{-3/2}
 \le\frac8{\tau\sqrt{h_0}}.
\]

Use \((1+A_k)^3\le8D^{3\gamma}\) and \(\tau\ge r^2/2\) to obtain the second term of (1). For the late intervals use regularity's sum bound
\(\sum_k(1+A_k)^3\le2C_{\rm reg}\lceil t/r^2\rceil\), obtaining \(Ctr\). For the ordinary duration-\(2t\) bridge, reverse the second half; the remaining duration is at least \(t\), and the Gaussian early bound applies throughout. The power is independently
\(-1+3/12+1/2=-1/4\). The preceding result holds in its stated regime.

## 2. Path spaces and the fixed-endpoint density

Work at fixed finite \(N,K\), with \(K>50\) and \(0<r<1\). Each path lies in the Polish space \(C([0,2t],\Lambda_K)\). Products of these spaces and the finite allocation space admit regular conditional probabilities. Choose the half-open starting cells once, so every initial endpoint determines one home cell.

Fix the endpoint configurations \(Y,Z\) and the purification variable \(W'\). Let \(\mathsf T_i\) be the free torus bridge from \(Y_i\) to \(Z_i\) of duration \(2t\). Disintegrating the Brownian reference \(\nu_N\) in the source equation gives the endpoint factor

\[
h(Y,Z,W')=
\frac{B_{\beta/2-t}^{\rm sym}(W',Y)
 B_{\beta/2-t}^{\rm sym}(Z,W')}{Z_N}
 \prod_i p^{\rm tor}_{2t}(Y_i,Z_i),
\]

times the path measure

\[
\mathbf1_{A(\omega)}\prod_{i=1}^N\mathsf T_i(d\omega_i),
\tag{2}
\]

where \(A\) is mutual strict avoidance. In particular, the outer symmetric kernels and the purification variable do not distinguish paths with the same endpoints. The already symmetric outer kernel does not introduce a new permutation sum into (2).

Let \(d_i(Y,Z)\in\{0,1\}\) record the endpoint displacement and separation tests in eligibility. Let \(R_i(\omega_i)\) be its own regularity and radius-ten confinement event. The eligibility indicator is exactly

\[
e_i=d_i(Y,Z)\mathbf1_{R_i(\omega_i)}.
\tag{3}
\]

No other trajectory enters (3) once endpoints are fixed. Eligibility at another home site is automatically false because the starting cells form a partition.

## 3. Allocation contributes no remaining path weight

For a full eligibility vector \(e\), let \(E_v(e)\) be the eligible labels at \(v\) and \(n_v=|E_v(e)|\). If \(n_v\ge MG_D\), a specified ordered list of length \(MG_D\) has probability

\[
\frac1{(n_v)_{MG_D}},\qquad
(n)_m=n(n-1)\cdots(n-m+1).
\tag{4}
\]

An infeasible list has probability zero. If there are too few eligible labels, the empty allocation is deterministic. Site allocations are conditionally independent. Hence the full allocation kernel \(k(a\mid e)\) is a function of \(a,e,Y,Z\) only. Recording the randomization variables as well, if desired, has the same property when their laws and selection rule depend only on this information.

Fix a feasible allocation \(a\), a group index \(g\), its selected set \(I=I(a,g)\), the entire vector \(e\), and the paths \(f=(\omega_j)_{j\notin I}\). This is a fixed exposed datum. Every selected label has \(e_i=1\), so \(d_i(Y,Z)=1\); its eligibility restriction is just \(R_i\). All restrictions on eligibility of labels outside \(I\), including zero indicators, are determined by \(f,Y,Z\). The factor (4) is constant as the paths in \(I\) vary.

Decompose avoidance into frozen-frozen, retained-frozen, and retained-retained pairs. The first is fixed and holds for almost every sampled datum. Define

\[
C_i(f)=R_i\cap
 \{\omega_i\text{ avoids every frozen path}\},\qquad
A_{II}=\{\text{every pair in }I\text{ avoids}\}.
\]

After discarding factors constant on this fixed exposed fiber, (2) becomes

\[
\mathbf1_{A_{II}}\prod_{i\in I}
 \mathbf1_{C_i(f)}\mathsf T_i(d\omega_i).
\tag{5}
\]

This derivation also proves the conditional identity directly: multiply (5) by an arbitrary bounded measurable function of the exposed datum and the retained family, insert the discarded endpoint, frozen-path, and allocation factors, and integrate. Fubini recovers the joint thermal-allocation density. Thus this is a disintegration argument, not conditioning on a point of positive endpoint probability. The fact that \(I\) itself is random is harmless: partition first by the finite allocation \(a\).

## 4. Confinement removes the winding mixture exactly

Let \(\widetilde v\) be a lift of a selected label's home center, and take the endpoint lifts \(y_i,z_i\) near it. A torus bridge is the projection of a mixture of Euclidean bridges with terminal endpoints \(z_i+Kn\), \(n\in\mathbb Z^3\), and weights

\[
w_i(n)=\frac{p^{\mathbb R^3}_{2t}(y_i,z_i+Kn)}
 {p^{\rm tor}_{2t}(Y_i,Z_i)}.
\tag{6}
\]

The torus heat kernel is the sum of the numerator over \(n\), so these weights sum to one. This identity follows as well by disintegrating Euclidean Brownian motion according to which lift of its terminal torus point it reaches.

Because \(K>20\), the inverse image of the radius-ten torus ball is a disjoint union of Euclidean radius-ten balls. A continuous path confined to that torus ball, starting at \(y_i\) in the ball about \(\widetilde v\), has its lift in that same ball throughout. It must end at \(z_i\), not \(z_i+Kn\) for \(n\ne0\). Consequently, on the confinement event, for every bounded measurable \(F\),

\[
\int F\mathbf1_{C_i(f)}\,d\mathsf T_i
 =w_i(0)\int F\mathbf1_{C_i(f)}\,dB_i,
\tag{7}
\]

where \(B_i\) is the projected Euclidean duration-\(2t\) bridge specified in the manuscript. Regularity uses lifted increments and hence is the same event in this identification. The frozen paths may wind; their collision tests are still torus tests, unchanged in (7).

Each \(w_i(0)>0\) depends on endpoints only. Applying (7) to (5), also for integrands coupling retained paths, yields the raw conditional measure

\[
\mathbf1_{A_{II}}\prod_{i\in I}
 \mathbf1_{C_i(f)}B_i(d\omega_i)
\tag{8}
\]

up to the positive constant \(\prod_i w_i(0)\). This constant cancels in normalization. This is an exact identity, with no small-winding approximation.

## 5. Positivity and the normalized product

Let the total mass of (8) be \(\widetilde Z(b)\). Integration of the original joint density over retained paths shows that the exposed marginal has a factor \(\widetilde Z(b)\), multiplied by its nonnegative fixed-fiber factors. Fibers with \(\widetilde Z(b)=0\) therefore have zero exposed probability. Since all indicators are bounded by one, \(\widetilde Z(b)\le1\); thus
\(0<\widetilde Z(b)\le1\) for almost every sampled datum.

Put \(a_i=B_i(C_i(f))\). For each \(i\in I\),

\[
0<\widetilde Z(b)\le a_i\le1,
\]

because the integrand defining \(\widetilde Z\) is at most \(\mathbf1_{C_i(f)}\). Every \(a_i\) is therefore positive on this same full-probability set. Define

\[
P_i=\mathbf1_{C_i(f)}B_i/a_i,
\qquad
Z_I=\int\mathbf1_{A_{II}}\prod_{i\in I}P_i
 =\frac{\widetilde Z(b)}{\prod_{i\in I}a_i}.
\]

Then \(0<Z_I\le1\), and normalization of (8) is precisely

\[
\lambda_I=Z_I^{-1}\mathbf1_{A_{II}}\prod_{i\in I}P_i.
\]

This establishes the claimed law and almost-everywhere positivity. It supplies no uniform lower bound on \(a_i\) or \(Z_I\). Such bounds require the later accessibility and insertion estimates. If \(I\) is empty, take the empty product and \(Z_I\) equal to one; the statement remains valid.

For completeness, all events used above are Borel. On a fixed path pair, the minimum over the compact time interval of its continuous distance is a continuous function in the uniform topology; strict avoidance is the event that this minimum exceeds \(r\). Confinement, the finitely many mesh diameters and the endpoint-window diameters are Borel as well. Lifts are determined continuously after fixing the initial lift locally. Consequently the integrals defining the conditional kernels are measurable in their parameters.

## 6. The geometric degree bound

If two retained paths with home sites \(v,w\) can collide, their confinement and the triangle inequality give
\(d_{\Lambda_K}(v,w)\le20+r<21\).
Every coordinate's periodic distance is therefore less than 21. There are at most 43 lattice coordinates in each such coordinate interval (a deliberately loose bound), hence at most \(43^3\) possible home sites. The selected group has at most \(M\) labels at a site. A label thus has at most \(43^3M-1\) other possible opponents. This is the asserted \(CM\) bound, with a numerical constant independent of volume, density and the exposed datum. For \(K>50\) and integral lattice centers, the sharper count \(41^3M-1\) is also available; it is unnecessary here.

## 7. Attempts to break the conditional identity

**Allocation bias.** Ordered sampling without replacement depends on the number of eligible labels, but that entire list is fixed by the exposed eligibility vector. Formula (4) is constant on the fiber. It may be very different on another fiber, which changes the exposed marginal, not the conditional law (8). The finite exact-arithmetic check in [audit.py](audit.py) enumerates two sites with three labels each, a nonuniform product reference on three path states, every eligibility vector permitting two ordered singleton groups at each site, and all compatible second-group allocations. It compares the conditional law from the full joint density with the proposed normalized product for every positive fiber, including retained-frozen and retained-retained collision checks.

**Additional conditioning.** The source explicitly excludes certificate events from the exposed datum. This matters: two independent fair binary variables conditioned on at least one being one have masses \(1/3\) on three states, rather than the original product masses \(1/4\). A full-sample event of that kind would add an extra factor to (8). The source's actual conditioning does not include it. Similarly, an allocation rule that inspected a retained trajectory beyond its eligibility indicator could contribute a nonconstant weight; that is not the stated rule.

**Winding.** Without confinement, the \(n\ne0\) summands in (6) are positive, so a single Euclidean bridge would not be the correct reference. With radius-ten confinement and \(K>20\), connectedness excludes those summands identically. A confinement radius at least half the torus side would invalidate this particular argument. The large-torus use satisfies the needed strict inequality.

**Mutual dependence and null fibers.** Reference paths are independent only before imposing \(A_{II}\). The final law generally has dependencies. Positivity is only an almost-everywhere claim under the actual exposed marginal, not a claim for arbitrary formally recorded endpoint, frozen-path and allocation data. These distinctions are retained throughout.

No extra eligibility, allocation, purification or winding factor remains in Lemma 7.2's conditional law under the stated exposure. Together with the preceding local audits, this removes that assumption from the earlier insertion calculation. The thermal certificate estimate and the lattice-route encounter estimate remain outside this verification.
