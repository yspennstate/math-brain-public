# Conditional verification of the path-factor insertion step

The source is OpenAI, *Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas* (October 5, 2026), Sections 6, 7 and 9. Local source copies are [bridges.tex](sources/bridges.tex), [groups.tex](sources/groups.tex) and [comparison.tex](sources/comparison.tex).

The assertion below concerns the application of Lemma 9.3. It assumes the deterministic single-replacement estimate of Lemma 6.3 (`lem:single-hit`), the conditional reference law in Lemma 7.2 (`lem:conditional-law`), and the exposed data and simple good-site routes specified in Sections 7 and 9. It does not establish those inputs or the condensation theorem.

## Proposition

Fix such exposed data, a group index, and two simple good-site routes with the same ordered endpoint cells. Suppose there are at most M retained labels at each anchor, r<1, and K>100. For every accessible retained label i and every fixed regular, confined opponent c of a different recorded label, assume the unconditioned one-path estimate

\[
 Q(\mathcal C_i\cap\mathcal H(c))\le q_D,
 \qquad q_D=C\bigl(tr+rD^{3\gamma}h_0^{-1/2}\bigr),
\]

for both the ordinary endpoint bridge and the bridge whose midpoint is uniform on a target unit cell. Here \(\gamma=1/12\), \(h_0=D^{-1}\), and \(r=\alpha/D\). The constant is uniform over the recorded endpoints and opponents, with the fixed parameter dependence permitted in Lemma 6.3.

Then the reference and two-copy proposal systems in Section 9 satisfy all the hypotheses of Lemma 9.3 with

\[
\begin{split}
 c_t&=(2\pi t)^{-3/2}e^{-8/t},\\
 G&=\max\{2,(0.98\cdot0.9\,c_t)^{-1}\},\\
 e_D&=q_D\max\{(0.99\cdot0.9\,c_t)^{-1},
                         (0.98\cdot0.9)^{-1}\},\\
 \chi_D&=2\cdot43^3M e_D=159014M e_D,
\end{split}
\]

once D is large enough that \(\chi_D<1\). The insertion bounds continue to hold under the lemma's deletion convention. With R=30, the resulting conditional second-moment bound is

\[
 \int L_SL_T\,d(\lambda_{\mathcal I}\otimes P_*)
 \le G^{|S\cap T|}(1-\chi_D)^{-4J_{30}}.
\]

## Proof

### 1. Normalization and one-path marginals

Write v for the integer anchor of i. Its recorded endpoint lifts satisfy \(y\in v+[-1/2,1/2)^3\) and \(|z-v|\le3\). The midpoint of the generator-\(\Delta\) bridge of duration 2t has mean \(m=(y+z)/2\) and covariance \(tI\). This follows either from the Brownian bridge covariance formula or from the product of the two duration-t heat kernels, divided by the duration-2t heat kernel.

For any u in a target cell (the home cell or a face neighbor),

\[
 |u-v|\le1+\sqrt3/2,\qquad
 |m-v|\le(\sqrt3/2+3)/2.
\]

Their sum is \(5/2+3\sqrt3/4<4\). Thus the midpoint density satisfies

\[
 g_i(u)=(2\pi t)^{-3/2}
       e^{-|u-m|^2/(2t)}\ge c_t.
\]

Let F be the frozen family and \(C_i(F)\) the individual success event, including regularity, confinement and avoidance of F. Accessibility supplies a subset of every target cell of volume at least 0.99 on which \(Q_i^u(C_i(F))\ge0.9\). Therefore the ordinary-bridge success normalizer obeys

\[
 a_i=\int g_i(u)Q_i^u(C_i(F))\,du
       \ge0.99\cdot0.9\,c_t>0.
\]

The reference law is \(P_i=1_{C_i(F)}B_i/a_i\). Fix a data-measurable set \(A\subset T_i(w)\) of volume at least 0.98. The proposal \(\Pi_i^A\) chooses u uniformly in A and then a successful bridge at that u. On successful paths its density relative to \(P_i\) is

\[
 \frac{a_i1_A(u)}{|A|g_i(u)Q_i^u(C_i(F))}
       \le(0.98\cdot0.9\,c_t)^{-1}\le G.
\]

It integrates to one because \(\Pi_i^A\) is a probability law. All ingredients depend only on exposed data and route/label choices, before any unselected unexposed paths are sampled.

For a deterministic permitted opponent c, the assumed one-path estimate gives

\[
 P_i(\mathcal H(c))
 \le q_D/a_i
 \le q_D/(0.99\cdot0.9\,c_t).
\]

For the proposal, use nonnegativity to extend the midpoint integral from A to its entire target cell:

\[
\begin{split}
 \Pi_i^A(\mathcal H(c))
 &=\frac1{|A|}\int_A
   \frac{Q_i^u(C_i(F)\cap\mathcal H(c))}
        {Q_i^u(C_i(F))}\,du\\
 &\le\frac{1}{0.98\cdot0.9}
       \int_{B_w} Q_i^u(\mathcal C_i\cap\mathcal H(c))\,du
 \le\frac{q_D}{0.98\cdot0.9}.
\end{split}
\]

Both collision probabilities are at most \(e_D\). No condition of mutual avoidance among the fixed opponents was used. The only endpoint separation required is between i and each opponent: it holds because i is eligible and the recorded labels differ. Opponent accessibility is unnecessary.

### 2. The shared-midpoint factors

At an internal route vertex the two accessible labels have good-target subsets of the same unit cell, each of volume at least 0.99. Their intersection A consequently has volume at least 0.98, since the complement has volume at most 0.01+0.01.

Choose U uniformly on A and, given U, sample the two successful bridges independently. Integrating out the other bridge shows that each path marginal is precisely its own \(\Pi_i^A\). Each therefore has collision probability at most \(e_D\) against a fixed permitted opponent. The paths can be dependent through U. They belong to different copies, so there is no collision check between them.

At each endpoint there is one path and one extra point sharing a midpoint. If the primary variable is the path, its marginal is again \(\Pi_i^A\). If the primary variable is the extra point, its density against uniform measure on the target cell is \(1_A/|A|\le1/0.98\le G\). The extra point itself has no collision checks. Thus every primary marginal has the required bounded density and normalization. Disintegration of these fixed Borel probability factors supplies the auxiliary kernels of Lemma 9.3; no bounded density for the joint pair of paths is needed.

### 3. Uniform insertion and deletion

All permitted paths lie within distance 10 of their own recorded anchor. If paths anchored at v and w collide at distance at most r, the torus triangle inequality gives

\[
 d_\infty(v,w)\le d_{\rm Eucl,torus}(v,w)
       \le20+r<21.
\]

It is enough to count the larger cube of anchors at supremum distance at most 21. It contains at most \((2\cdot21+1)^3=43^3\) sites. Within one copy there are at most M labels at each anchor and each label appears at most once. Consequently any inserted path has at most \(43^3M\) potential opponents. Every checked opponent has a distinct recorded label in that copy. The proposal has at most two paths, one in each copy; the union bound bounds failure of all its incident checks by

\[
 2\cdot43^3M e_D=\chi_D.
\]

The argument uses only the marginal bounds from steps 1 and 2 and the individually permitted values of the other paths. It is therefore uniform even if some fixed opponents collide with each other. Inserting a reference path needs only one such copy, hence has failure probability at most \(43^3M e_D\le\chi_D\). All real labels in S union T are accessible because both routes select accessible labels. The independent reference extra point has no checks and succeeds with probability one.

Under the stated deletion rule, removing a factor removes its paths and incident checks. An auxiliary instance in a retained factor remains that instance. It is not replaced by the original reference path of the same label. Hence deletion creates no additional obstacle, no same-copy duplicate label and no new check. The same insertion bound survives every reduced normalizer, including reductions whose fixed opponents fail mutual checks.

Since \(3\gamma=1/4\),

\[
 rD^{3\gamma}h_0^{-1/2}
   =\alpha D^{-1+1/4+1/2}=\alpha D^{-1/4},
 \qquad tr=\alpha tD^{-1}.
\]

For fixed t, the fixed alpha window and fixed M, \(e_D=O_t(D^{-1/4})\) and \(\chi_D\to0\). Thus \(\chi_D<1\) for large D. Successive insertion of the d+1 full route factors has conditional normalization at least \((1-\chi_D)^{d+1}>0\). This only proves that the route construction is defined; the cancellation lemma is still needed to avoid paying a cost proportional to d in the final bound.

### 4. Far-factor separation

A vertex factor is centered at its target cell center. A carried path's home anchor is either that center or a face neighbor, so the path lies within Euclidean torus distance 11 of the factor center. An original reference path of a primary real label also lies within distance 11 of its factor center.

If two factor centers have periodic supremum distance greater than 30, their Euclidean torus distance is greater than 30. Two points within distance 11 of the respective centers are therefore at distance greater than \(30-22=8>r\). This excludes every proposed cross-check and every reference cross-check between the far sets required by Lemma 9.3, including checks involving auxiliary paths or opposing original reference paths.

A shared real label has the same recorded home anchor in both route assignments. Each of its factor centers is within distance one of that anchor, so the two centers are at supremum distance at most two. It is therefore near in both routes. The shared extra-point index has the same endpoint center. Consequently \(F_S\cap T=F_T\cap S=\varnothing\), as required.

### 5. Likelihoods and the encounter bound

The original conditional reference law is the product of the \(P_i\), conditioned on within-copy avoidance checks, together with the independent uniform extra point. For either route, the construction samples its complement from exactly its original marginal, then samples the changed factors conditionally on that fixed complement. Thus it preserves the complement marginal. In particular it is not one global reweighting of the complement by a route success probability.

The primary proposal configuration satisfies every reference avoidance check: these are among the checks imposed within the chosen primary copy. Checks involving only unchanged coordinates already hold under their marginal. Steps 1–4 verify the remaining hypotheses of Lemma 9.3. It gives

\[
 \int L_SL_T\,d(\lambda_{\mathcal I}\otimes P_*)
 \le G^{|S\cap T|}(1-\chi_D)^{-2(|C_S|+|C_T|)}.
\]

Let \(J_{30}\) count ordered pairs of route vertices whose centers are within periodic supremum distance 30. Each near factor of S participates in at least one such pair, hence \(|C_S|\le J_{30}\). Counting by the other endpoint gives \(|C_T|\le J_{30}\). Therefore

\[
 2(|C_S|+|C_T|)\le4J_{30}.
\]

Since \(0<1-\chi_D\le1\), replacing the exponent by the larger value \(4J_{30}\) weakens the upper bound in the correct direction. This proves the proposition.

## Boundary checks

The endpoints are always encounters because both routes have the same endpoint cells; J cannot be set to zero for these actual route pairs. The extra-point factor is included in the changed sets and carries at most one checked path. A shared label's auxiliary instance can survive deletion of its primary factor because the two instances belong to different copies; this does not create a same-copy duplicate. No bound here is conditional on a prescribed midpoint: at a midpoint chosen equal to an opponent's midpoint, collision can be certain.

The opponent count admits a smaller independent bound: periodic integer anchor distance less than 21 implies distance at most 20, so there are at most \(41^3=68921\) possible anchors, compared with \(43^3=79507\) used above. Thus \(2\cdot41^3M e_D\le159014M e_D\). Likewise, the center separation can be checked in one coordinate attaining the periodic supremum distance: subtracting at most 11 from each path leaves a coordinate gap greater than eight. These checks give the same signs and sufficient geometric margins.
