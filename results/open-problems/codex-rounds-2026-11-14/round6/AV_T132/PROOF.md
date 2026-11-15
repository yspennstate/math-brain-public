# Vanishing comparison constants retain zero-cost local certificates

The passage considered is lines 120–129 of [bootstrap.tex](sources/bootstrap-round6.tex) in OpenAI, *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026). The result below proves the vanishing-cost transfer under explicitly stated raw-certificate hypotheses. It does not construct the local kernels or prove the planar-map convergence theorem.

## 1. The retained objects and hypotheses

For each integer \(r\geq1\), let \(\eta_r:\mathbb R\to\mathbb C\) be a continuous proper curve. Proper means that the preimage of every compact set is compact. Let \(D_r\) be a continuous length metric inducing the ordinary topology. The joint law of \((\eta_r,D_r)\), including the internal reference distances on the domains below, is independent of \(r\). No independence between these objects and the certificates is assumed.

For an integer \(T\geq2\), put \(J_T=[-T,T]\). The one-segment raw certificate space is

\[
 \mathcal S_T=J_T^2\times\mathcal H(J_T)\times[0,\infty].
 \tag{1}
\]

Here \(\mathcal H\) denotes nonempty compact subsets with Hausdorff distance, and the last factor is compactified by \(c\mapsto c/(1+c)\). A point \(z=(s,t,A,c)\) records two marked representatives, every representative in the intervening path, and an upper bound for its cost. Its endpoints and range are \(\eta_r(s),\eta_r(t),\eta_r(A)\). The complete raw array retains a closed set \(\mathcal H_{r,T}\subset\mathcal S_T\). Empty sets may be adjoined as isolated points.

Assume the following.

1. The curves and the entire countable array converge jointly in law:

   \[
   (\eta_r,(\mathcal H_{r,T})_{T\geq2})
   \ \Rightarrow\
   (\eta,(\mathcal H_T)_{T\geq2}).
   \tag{2}
   \]

   Curves have local uniform topology; closed sets in each compact space (1) have Hausdorff topology. The limits have the stated raw/spatial compatibility.

2. Full witnesses are retained. A finite-cost local certificate with spatial range in a compact \(K\), all of whose representatives lie in \([-T+1,T-1]\), belongs to \(\mathcal H_{r,T}\). In particular, on

   \[
   E_{r,T}(K)=
     \{\eta_r^{-1}(K)\subset[-T+1,T-1]\},
   \tag{3}
   \]

   every local certificate confined to \(K\) is retained in this window.

3. Let \(F_{r,V}(x,y)\) be the infimum of costs of certificates from \(x\) to \(y\) compactly in \(V\). For every bounded rational Euclidean ball \(V\), simultaneously for its rational-coordinate points \(x,y\),

   \[
        F_{r,V}(x,y)\leq\varepsilon_rD_r(x,y;V),
        \qquad \varepsilon_r\geq0,\quad\varepsilon_r\longrightarrow0.
   \tag{4}
   \]

   The numbers \(\varepsilon_r\) are deterministic. The infimum has its ordinary witness meaning: a bound within any positive tolerance has a finite-cost certificate.

4. In the limit, infimal local costs are continuous pseudometrics on connected open sets. They are monotone under enlargement and allow finite concatenation with arbitrarily small additional cost.

Hypotheses 1 and 2 concern the original raw arrays, rather than a newly sampled collection having the same marginal law. Hypothesis 4 will be used only to extend from countably many endpoint pairs to every local connection.

Then, almost surely, for every connected open \(U\subset\mathbb C\) and every \(x,y\in U\), the limiting local cost is zero. More precisely, whenever \(x,y\) are rational-coordinate points of a rational ball \(V\) with \(\overline V\subset U\), there is an actual limiting raw certificate of cost zero with these endpoints and spatial range in \(\overline V\).

## 2. Finiteness and the two cutoffs

For any connected open \(V\), the internal length distance \(D_r(x,y;V)\) is finite between every pair of its points. Here is a direct justification. The ordinary and metric topologies agree. Around any point \(z\in V\), choose a metric ball \(B_{D_r}(z,\rho)\subset V\). If \(D_r(z,w)<\rho/4\), the length-space property supplies a curve from \(z\) to \(w\) of length less than \(\rho/2\); every point on it is within \(\rho/2\) of \(z\), so it stays in \(V\). Thus equivalence classes under connection by a finite-length curve in \(V\) are open. The complement of each class is a union of the other open classes. Connectedness gives a single class. Each such curve has compact range in \(V\).

Fix \(V,x,y,U\) as in the conclusion and put \(K=\overline V\). Write

\[
       Y_r=D_r(x,y;V).
\]

These nonnegative variables have one common law, that of a finite random variable \(Y\). For every \(a>0\),

\[
 \mathbb P(\varepsilon_rY_r>a)
 \leq \mathbb P(Y>M)
 \quad\hbox{once }\varepsilon_r M\leq a.
 \tag{5}
\]

First take \(r\) large for fixed \(M\), then \(M\to\infty\). Thus \(\varepsilon_rY_r\to0\) in probability. There is no moment assumption on \(Y\).

The fixed proper-curve law gives a second, separate cutoff:

\[
 \alpha_T=\mathbb P(E_{r,T}(K)^c)
 \quad\hbox{is independent of }r,\qquad
 \alpha_T\downarrow0.
 \tag{6}
\]

Indeed, for each sample the compact set \(\eta_r^{-1}(K)\) is contained in the interiors of all sufficiently large \(J_T\). The events (3) increase to an event of probability one.

By (4), choose a certificate with cost at most \(\varepsilon_rY_r+1/r\), compactly in \(V\). Its spatial range lies in \(K\). On (3) it lies in \(\mathcal H_{r,T}\). This is an existence statement; a measurable selection of the witnesses is unnecessary.

The margin of one in (3) also explains the window-retention hypothesis for actual sewing-path approximants. Start with a certificate in any larger window and raw range inside \([-T+1,T-1]\). Its approximants eventually have all representatives strictly inside \(J_T\). Every horizontal link and first-coordinate minimum witness is then internal. For a vertical matched edge, advancing the two primal representatives by one vanishing mesh step includes its terminal-step witnesses, still inside \(J_T\). The identical approximating path is therefore allowed in \(J_T\), with identical cost. Closedness puts its certificate in \(\mathcal H_{r,T}\). This is the time-window form of the deterministic argument in [ROUND5_PROOF.md](ROUND5_PROOF.md); it uses the complete representatives and actual approximants.

## 3. Closed witness events and zero cost

For \(\delta\geq0\), let \(A_{T,\delta}\) be the event that \(\mathcal H_T\) contains \(z=(s,t,A,c)\) with

\[
       \eta(s)=x,\qquad \eta(t)=y,\qquad
       \eta(A)\subset K,\qquad c\leq\delta.
       \tag{7}
\]

Use the same notation with superscript \(r\) for the corresponding event in the \(r\)th law.

The set of joint observations satisfying (7) is closed. To prove this, take any convergent sequence of observations satisfying it and pick a witness \(z_j\) for each. The compactness of (1) gives a further subsequence \(z_j\to z\). Hausdorff convergence of the closed certificate sets puts \(z\) in the limiting set. The maps \((\eta,s)\mapsto\eta(s)\) and \((\eta,A)\mapsto\eta(A)\) are continuous for uniform and Hausdorff convergence on \(J_T\). Endpoints, closed range containment in \(K\), and \(c\leq\delta\) therefore persist. This proves closedness, including at \(\delta=0\).

For each fixed \(T\) and \(\delta>0\), the witnesses in Section 2 give

\[
 \mathbb P(A^r_{T,\delta})
 \geq 1-\alpha_T
      -\mathbb P(\varepsilon_rY_r+1/r>\delta).
 \tag{8}
\]

The last probability tends to zero by (5). Apply the closed-set half of the Portmanteau theorem to (2):

\[
 \mathbb P(A_{T,\delta})
 \geq\limsup_r\mathbb P(A^r_{T,\delta})
 \geq1-\alpha_T.
 \tag{9}
\]

Now keep \(T\) fixed and let \(\delta=1/m\downarrow0\). These events decrease, and

\[
                 \bigcap_{m\geq1}A_{T,1/m}=A_{T,0}.
                 \tag{10}
\]

For the nontrivial inclusion, choose one witness for each \(m\), extract in the same compact space (1), and apply the closed conditions in (7). The limiting cost is zero. Continuity of probability from above and (9) yield

\[
                    \mathbb P(A_{T,0})\geq1-\alpha_T.
                    \tag{11}
\]

Finally the event that some finite window contains a zero-cost witness includes \(A_{T,0}\) for every \(T\). Its probability is at least \(\sup_T(1-\alpha_T)=1\). Thus the zero-cost certificate exists almost surely in a finite raw window and is compactly in \(U\). The order of operations was fixed window, resolution limit, decreasing cost tolerances, then removal of the window cutoff.

There are countably many rational balls, larger rational balls and rational-coordinate endpoint pairs. Intersect their probability-one events. Fix any connected open \(U\), and any rational ball \(V\) with \(\overline V\subset U\). The zero-cost certificates for rational pairs in \(V\) have range in \(\overline V\), so they are also certificates in \(U\). Continuity of \(F_U\) extends zero cost from these rational pairs to all pairs of \(V\). A finite chain of such balls connects any two points of \(U\). Indeed the points reachable by finite chains form an open set with open complement, since rational balls with closure in \(U\) form a basis. Connectedness gives a single chain component. The triangle inequality now gives \(F_U(x,y)=0\). This proves the simultaneous conclusion without an uncountable intersection of probability-one events. Only the rational-pair assertion claims an attained zero-cost raw certificate; for general pairs zero infimal cost suffices.

## 4. A separate derivation with continuous tests

The direction of (9) and the decreasing-event step can also be checked without a closed-event probability argument. On \(\mathcal S_T\), define the continuous nonnegative defect

\[
\begin{aligned}
 g_\eta(s,t,A,c)
  ={}&\frac{c}{1+c}
     +\min\{1,|\eta(s)-x|\}
     +\min\{1,|\eta(t)-y|\}\\
    &+\min\{1,\max_{a\in A}\operatorname{dist}(\eta(a),K)\}.
\end{aligned}
\tag{12}
\]

The first term equals one at infinity. Put \(\Psi_T=\min_{z\in\mathcal H_T}g_\eta(z)\), assigning the value four if the certificate set is empty. This is continuous in the joint curve/closed-set observations: uniform convergence of curves gives uniform convergence of the defect on the compact witness space, and Hausdorff convergence preserves its minimum. The isolated empty set causes no continuity issue.

For a fixed positive integer \(b\), use the bounded continuous test \(\min\{1,b\Psi_T\}\). On \(E_{r,T}(K)\), the witness from Section 2 gives

\[
 \min\{1,b\Psi^r_T\}
 \leq\min\{1,b(\varepsilon_rY_r+1/r)\}.
\]

On its complement the test is at most one. The expectation of the right side tends to zero: for fixed \(M\) it is at most \(b(\varepsilon_rM+1/r)+\mathbb P(Y>M)\), and then \(M\to\infty\). Weak convergence gives

\[
            \mathbb E\min\{1,b\Psi_T\}\leq\alpha_T.
            \tag{13}
\]

Let \(b\to\infty\). Monotone convergence yields
\(\mathbb P(\Psi_T>0)\leq\alpha_T\). Compactness makes \(\Psi_T=0\) equivalent to (7) at cost zero. This recovers (11) independently and checks that no bound on \(\mathbb E Y\), nor independence, entered the argument.

For an explicit infinite-mean check, let \(\mathbb P(Y=2^j)=2^{-(j+1)}\) for \(j\geq0\). Then \(\mathbb E Y=\infty\), whereas

\[
 \mathbb E\min\{1,2^{-n}Y\}
   =n\,2^{-n-1}+2^{-n}
   =(1+n/2)\,2^{-n}\longrightarrow0.
 \tag{14}
\]

The \(n\) terms with \(j<n\) each contribute \(2^{-n-1}\); the remaining tail contributes \(2^{-n}\). The same value follows from integrating the tail over \([0,1]\). Exact rational checks of both calculations are in [audit.py](audit.py).

## 5. Application to the maximizing zooms

In the notation of [bootstrap.tex](sources/bootstrap-round6.tex), the laws before further extraction are rigid. Their local rule is \(C_rD_h\). At the deterministic maximizing index \(i_r\), put \(v_r=2^{-i_r}\). The asserted quantum-unit transport makes the reference distance \(v_r^pD_{h_r^{\rm new}}\) in the original cost units. Division by the new cost unit \(H_rv_r^p\) therefore changes

\[
       \frac{C_rv_r^pD_{h_r^{\rm new}}}{H_rv_r^p}
           =\frac{C_r}{H_r}D_{h_r^{\rm new}}.
       \tag{15}
\]

Thus (4) holds with \(\varepsilon_r=C_r/H_r\to0\). This is the same factor as in bootstrap lines 120–121; there is no residual factor depending on \(i_r\). The quantum-unit transport and fixed-law reference coupling themselves remain hypotheses.

The law topology in [coherent-background.tex](sources/coherent-background-round6.tex) explicitly retains the proper curve, the reference metric and internal reference metrics on countably many buffered rational domains. It asserts their fixed joint marginal through changing laws and fixed quantum transforms. Section 3 uses only the resulting tightness of each finite \(D_r(x,y;V)\); it does not need continuity of intrinsic distance as a function of the ambient metric or of the contour.

The raw-array compactness and actual realization assertions of Proposition tree:prop:certificate_limit supply hypotheses 1 and 2 if they hold for the maximizing-zoom extraction. Its local joining and continuity conclusions supply hypothesis 4. Under these structural inputs, Sections 2–3 justify bootstrap lines 122–129 and give the zero-local-cost input left open in round 5. Combined with that round's conditional localization and tip-modulus argument, and the round-4 moment estimate, the surviving endpoint moment \( \mathbb E\widetilde X^k\geq2^{-k}>0 \) contradicts vanishing local costs.

This verifies the transfer implication, not all its construction hypotheses. In particular, the local joining proof, construction and varying-law closure of raw/chart arrays, conditional reference experiments, quantum transport and the preceding rigidity theorem have not all been independently proved. The conclusion establishes neither a new positive-\(q\) exponent nor the full graph-metric scaling limit.

## 6. Attempts to break the transfer

Tight reference costs are necessary. On \(\mathbb R\), take \(D_r(x,y)=r|x-y|\), \(F_{r,U}(x,y)=|x-y|\) on intervals, and \(\varepsilon_r=1/r\). The upper comparison is exact, but the costs between 0 and 1 remain one. Here \(D_r(0,1;U)=r\) is not tight. Merely writing a vanishing prefactor gives no conclusion without the reference-law input.

Witness confinement is necessary too. In the noncompact witness space \((0,1]\), let the only witness at stage \(r\) be located at \(1/r\), with cost \(1/r\). In every compact subset bounded away from zero the closed witness sets are eventually empty, so local closed-set convergence loses all witnesses. There is no zero-cost limiting witness in this space. The fixed spatial buffer and the proper-curve time cutoff in Section 2 prevent this escape.

Finally, zero cost on a dense set needs a continuity input. The pseudometric
\[
  F(x,y)=|\mathbf1_{\mathbb Q}(x)-\mathbf1_{\mathbb Q}(y)|
\]
vanishes between all rational pairs, but \(F(0,\sqrt2)=1\). It is discontinuous. The local joining/continuity hypothesis is therefore still needed to reach the random interior endpoints used in the nonzero-local-cost contradiction.

The next concrete target is Proposition tree:prop:certificate_limit(2), especially the converse Brownian-fiber approximation and uniform spatial joining in certificates.tex lines 130–180. That input must work for the same jointly retained arrays under changing laws. The transfer proved here cannot replace it.
