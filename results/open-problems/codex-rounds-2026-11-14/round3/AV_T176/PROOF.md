# Conditional-flow check for T176

Source: OpenAI, *Optimal-order mixing of the Thorp shuffle*, September 26, 2026, Sections 3–4, especially Lemma 3.2 and Proposition 4.2. The source is saved as [optimal-main.tex](optimal-main.tex). This note checks the averaged-marginal input to the Fourier transfer checked in the earlier report. It does not verify the complete mixing theorem or either companion paper.

## Statement checked

Let n = 2^d and let Pi_t be the shuffle in cyclic coordinate frame. Choose an ordered list C of k distinct initial labels uniformly, independently of the shuffle, with 1 <= k <= 7n/8. At T = 200d, the source claims

\[
\mathbb E_C\left\|\mathcal L((\Pi_T(c_1),\ldots,\Pi_T(c_k))\mid C)-U_{\mathrm{inj}}\right\|_{\mathrm{TV}}
\le \frac{n^{3/2}}2\sqrt{(31/32)^{198d}+32e^{-n/256}}
=O(n^{-5/2}).
\]

The expectation over C is essential. The statement does not assert this bound for every fixed list.

The cyclic frame is obtained by undoing the coordinate rotation R after every physical shuffle. Since R^d is the identity and T=200d, the physical and cyclic frames coincide at this endpoint; T counts physical shuffles.

## 1. Conditioning on paths

First fix C and expose the paths of its first ell labels, where 0 <= ell < k. Let F_s contain C and these paths through time s. Let B_s be their complement, m = n-ell, and define

\[
p_s(x)=\Pr(\Pi_s(c_{\ell+1})=x\mid F_s),\qquad
w_s(x)=p_s(x)-m^{-1}\mathbf1_{B_s}(x).
\]

The random array consists of independent fair coins indexed by time and matching edge. Fix any feasible exposed-path history through a terminal time T. That history specifies a set of time-edge pairs and their coin values. Conversely, these prescribed coin values force precisely those paths: induction on time shows that each exposed card sees the prescribed next coin. If two exposed cards meet an edge, feasibility makes the prescriptions agree. Hence the path event is exactly a cylinder, with no constraint on any other coin.

In particular, extending the exposed history from s to T adds constraints only on coins at times s and later (the layer from s to s+1 is indexed s). Conditional on the already fixed past, those future constraints do not restrict any earlier unvisited coin. The tagged position at time s depends only on its initial label and earlier coins. Its conditional law at s is therefore unchanged by conditioning on the full exposed history through T. This justifies using an adapted forward flow even when the eventual comparison conditions on complete exposed paths.

On an edge with two free endpoints, no exposed card visits the edge. Its coin remains fair, and the two masses average. On an edge with one free endpoint, the exposed card's next position fixes the coin, and the tagged mass moves to the other, free output. The same operations carry the uniform vector on B_s to that on B_{s+1}. Thus they act linearly on w_s. Pairwise averaging decreases squared norm and one-free transport preserves it. Initially the norm squared is 1-1/m, so, pathwise,

\[
\sum_xw_s(x)=0,\qquad \|w_s\|_2^2\le1.
\]

## 2. Exact energy identity

Let i_s be the active coordinate in layer s and let A_i average across every coordinate-i edge. Before revealing the next exposed positions, each one-free edge uses an independent fresh fair coin. Consequently

\[
w_{s+1}=A_{i_s}w_s+\xi_s,\qquad
\mathbb E(\xi_s\mid F_s)=0.
\]

If x is its free endpoint, one such edge contributes

\[
\pm\frac{w_s(x)}2(\delta_x-\delta_{x+e_{i_s}})
\]

to xi_s. Other edges contribute zero. These signs are conditionally independent across edges.

Write

\[
E_s=\mathbb E\|w_s\|_2^2,\quad
b_s=\mathbb E\sum_x w_s(x)^2\mathbf1_{\{x+e_{i_s}\notin B_s\}}.
\]

Unroll the update for d layers. Each coordinate occurs once, so the product of the coordinate averages sends a vector to its constant spatial average and kills w_{t-d}. Cross terms of noises from different times have expectation zero: condition on the past of the later noise, while all intervening A_i are deterministic. Distinct-edge cross terms at one time also vanish by the independent centered signs.

A noise generated j layers before t is averaged in j-1 other coordinates. Each of its two masses spreads over 2^{j-1} positions, with disjoint supports distinguished by the generating coordinate. Its squared norm is therefore

\[
2\,2^{j-1}\left(\frac{w_{t-j}(x)}{2^j}\right)^2
=2^{-j}w_{t-j}(x)^2.
\]

Thus, for t >= d,

\[
E_t=\sum_{j=1}^{d}2^{-j}b_{t-j}. \tag{1}
\]

As a second check on this factor, a fresh dipole has squared norm w^2/2. Each averaging in a previously unused transverse coordinate halves that norm; after j-1 such averages it is w^2/2^j. This also covers j=1 and j=d.

## 3. Independence in the lookback interval

Fix s >= d-1, put a = s-d+1, and split the cube into H_0,H_1 by coordinate i_s. The layers a,...,s-1 use exactly the other d-1 coordinates and never cross these halves. Conditional on F_a, the initial sets B_a and flow w_a are fixed. The switch arrays in opposite halves during this interval are independent.

The evolution of both B and w within a half depends only on its own initial set and flow and its own future array. No conditional independence between w_a and B_a is required. Therefore w_s(x)^2 in H_h is conditionally independent of availability at the opposite endpoint x+e_{i_s}.

A fixed starting point within a half becomes uniform on that half after these d-1 layers: each of its other coordinates is refreshed once by a coin independent and fair conditional on its previous path. Since the switch map is a permutation, indicators of distinct starting points mapping to a fixed endpoint cannot overlap. Summing their endpoint probabilities gives

\[
\Pr(y\in B_s\mid F_a)=\frac{|B_a\cap H_{1-h}|}{n/2}
\quad(y\in H_{1-h}).
\]

Set r_h = |B_a intersect H_h|/(n/2). The preceding independence proves

\[
b_s=\mathbb E\sum_{h=0}^1(1-r_{1-h})
       \mathbb E\left[\sum_{x\in H_h}w_s(x)^2\mid F_a\right]. \tag{2}
\]

In particular, this is not an assertion that flow and availability within the same half are independent.

## 4. Uniform free sets and the exceptional event

Now average over uniform C. Its first ell labels form a uniform ell-subset, so their complement is a uniform m-subset. For any fixed realization of the shuffle, applying its time-a permutation preserves that distribution. Thus B_a is unconditionally uniform among m-subsets. This argument does not condition on F_a or on the energy.

For completeness, sample its m points without replacement. If S_i counts points in one half among the first i draws, the Doob martingale for the final half-count X is

\[
M_i=S_i+(m-i)\frac{n/2-S_i}{n-i},\qquad 0\le i\le m,
\]

when m<n. The two possible values after the next draw differ by (n-m)/(n-i) at stage i, hence by at most one; each centered increment has absolute value at most one. A centered variable in [-1,1] has log moment-generating function at most theta^2/2: its second derivative is a tilted variance at most one, and its value and first derivative at zero vanish. Conditional multiplication and Markov's inequality give

\[
\Pr(X-m/2\le-u)\le\inf_{\theta>0}e^{-\theta u+m\theta^2/2}
=e^{-u^2/(2m)}.
\]

Taking u=m/4 gives P(X<m/4) <= exp(-m/32). For m=n, X=n/2 deterministically, so the same required lower-tail statement holds without a martingale formula at its final zero denominator.

The event G that both half-counts are at least m/4 belongs to F_a. Since m>=n/8, on G both densities r_h are at least

\[
\frac{m/4}{n/2}=\frac{m}{2n}\ge\frac1{16}=:\beta.
\]

Its complement has probability at most 2exp(-m/32) <= 2exp(-n/256) =: eta. By (2), on G the conditional loss is at most (1-beta) times conditional energy; off G it is at most the energy. Because the energy is pathwise at most one, even with arbitrary correlation between energy and G,

\[
b_s\le(1-\beta)E_s+\eta. \tag{3}
\]

## 5. Solving the recurrence

Put gamma=31/32 and K=eta/beta=32exp(-n/256). For t<=2d, E_t<=1<=gamma^{t-2d}+K. For t>2d, all indices t-j in (1) are at least d+1, so (3) is valid, and induction yields

\[
\begin{aligned}
E_t
&\le\sum_{j=1}^d2^{-j}\{(1-\beta)(\gamma^{t-j-2d}+K)+\eta\}\\
&\le\gamma^{t-2d}(1-\beta)\sum_{j=1}^{\infty}(2\gamma)^{-j}
      +(1-\beta)K+\eta\\
&=\gamma^{t-2d}+K.
\end{aligned}
\]

The last equality uses 2gamma-1=15/16=1-beta and (1-beta)K+eta=K. These also independently verify the decay base and the additive constant; the time shift 2d safely avoids the initial d-1 layers where (3) was not derived.

## 6. Endpoint tuples

For any distinct-position tuple, append the next coordinate first using its actual conditional law and then compare with the kernel that appends a uniform unused position. The TV cost is the expected conditional TV distance at that coordinate. Uniform extension sends a uniform prefix to a uniform longer tuple, and applying a common kernel cannot increase TV. Induction gives the sum of these costs over coordinates.

At coordinate j, conditioning further on the previous j-1 complete paths can only increase the expected cost, by convexity of TV and the tower property; its uniform comparison law depends only on the endpoint prefix. Section 1 identifies the resulting conditional distribution with p_T above. Its TV cost is ||w_T||_1/2. There are m_j=n-j+1 free positions, and Cauchy–Schwarz followed by the scalar Cauchy–Schwarz inequality gives

\[
\tfrac12\mathbb E\|w_T\|_1
\le\tfrac12\sqrt{m_j\,\mathbb E\|w_T\|_2^2}
\le\tfrac12\sqrt{n\{\gamma^{198d}+32e^{-n/256}\}}.
\]

Here expectations include C and the shuffle, as required by Section 4. Every j<=k leaves at least n/8 free positions. Sum at most n terms to obtain the stated bound.

## 7. Numerical audit and scope

Two elementary checks suffice for the claimed exponent. First,

\[
\log(32/31)=\int_{31}^{32}\frac{dx}{x}>1/32,
\qquad \log2<3/4
\]

(the latter follows from exp(3/4)>1+3/4+(3/4)^2/2>2). Thus 198log_2(32/31)>198/24>8. Independently, the first four terms of the binomial expansion give

\[
(32/31)^{22}
\ge1+22/31+231/31^2+1540/31^3
=59634/29791>2.
\]

Since 198=9*22, this even gives (31/32)^{198d}<n^{-9}, which has more margin than the n^{-8} needed here. The exponential term is O(n^{-8}), so the displayed marginal bound is O(n^{3/2}n^{-4})=O(n^{-5/2}). No novelty is claimed for the available margin in the exponent.

Attempts to break the argument included conditioning on future exposed paths, allowing both exposed cards on one edge, allowing arbitrary energy on the exceptional event, m=n, m=1 when permitted, d=1 (the lookback interval is empty), and the first induction time t=2d+1. None contradicts the identities above. In particular, m=n gives no one-free-edge noise and complete one-card averaging; m=1 gives w=0 identically. The proof still needs the random-list average: a fixed initial free set can be entirely inside one half, so Section 4 cannot be asserted for every fixed list.

This verifies the stated conditional-flow and averaged-marginal calculation in ordinary mathematics. It is a local check, not a certificate of the entire preprint, its Lean development, or any result for non-dyadic decks.
