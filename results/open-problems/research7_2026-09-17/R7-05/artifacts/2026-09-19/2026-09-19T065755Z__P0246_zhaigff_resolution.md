Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0246 source-status correction: Aldous–Fill Open Problem 7.6 follows from Zhai's GFF cover-time theorem

## 1. Purpose and status

This is an admission-side mathematical artifact for R7-05. It is **not** a new ownership claim and it does **not** assert novelty.

Canonical campaign ID: `P0246`.

Exact shard check:

```text
sum(ord(c) for c in "P0246") = 284,   284 mod 7 = 4.
```

The campaign row calls P0246 **“Universal leading cover-time upper bound under transitivity.”** The outside source is David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 7, Section 7.1.5, **Open Problem 7.6** (book PDF p. 243; current HTML section 7.1). The source asks, for every sequence of irreducible symmetric reversible `n`-state chains, whether

\[
  EC\le (1+o(1))\tau_0\log n
\]

holds without the extra hypothesis in Corollary 7.5(b). Here `EC` is the expected cover time and, by symmetry, \(\tau_0=E_\pi T_i\) is independent of `i`.

Current source URL (checked 2026-09-19):
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch7.S1.html`.

The current Aldous–Fill HTML still displays Open Problem 7.6 as open. However, the argument below shows that the requested estimate is an elementary corollary of Alex Zhai's published 2018 GFF concentration theorem for cover times on electrical networks. Because the key theorem is already in the literature and the remaining reduction is elementary, the conservative R7-05 disposition is:

```text
KNOWN / LITERATURE-IMPLIED RESOLUTION
NOVELTY: UNVERIFIED AND NOT CLAIMED
R7-05 ADMISSION: REJECT (exclude known/solved work)
```

A bounded search for the exact phrases `Open Problem 7.6`, `Aldous Fill`, `tau0 log n`, `symmetric reversible chains`, and Zhai did not locate a paper explicitly cross-referencing Zhai's theorem to Aldous–Fill 7.6. This search miss is **not** evidence of novelty.

## 2. Prior campaign attempt and why the new route is different

The earlier campaign attempt on P0246 computed the cycle baseline: for continuous-time rate-one walk on the `n`-cycle, \(\tau_0=(n^2-1)/6\) and \(EC=n(n-1)/2\), and concluded that a uniform dichotomy between cycle-like chains and chains with small mixing/hitting ratio appeared necessary.

The present route bypasses that obstruction entirely. It changes category from a direct Markov-chain/Matthews argument to an electrical-network/Gaussian-free-field argument. The only symmetry used after the change of language is enough to identify the one-point GFF variance exactly in terms of \(\tau_0\).

Methods used this run:

- **B1 CHANGE THE CATEGORY:** symmetric reversible chain \(\to\) electrical network/GFF.
- **B18 SAY IT IN ANOTHER LANGUAGE:** convert hitting times to effective resistance and recenter the GFF.
- **B3 PROVE SOMETHING STRONGER:** obtain the quantitative rate \(1+O((\log n)^{-1/2})\), stronger than the requested `1+o(1)`.

## 3. Literature input

Alex Zhai, **“Exponential concentration of cover times,”** *Electronic Journal of Probability* 23 (2018), DOI `10.1214/18-EJP149`, arXiv `1407.7617`.

Zhai proves Theorem 1.1 for general graphs and states in Remark 1.4 that the proof is actually in the more general setting of finite electrical networks. In Section 4, with

\[
 c_{\rm tot}=\sum_{x,y}c_{xy},\qquad
 M=E\max_x\eta_x,\qquad
 R=\max_{x,y}R_{\rm eff}(x,y),
\]

his proof yields universal constants `c,C>0` such that, after harmless rescaling of `lambda`,

\[
 \Pr\left(\left|\tau_{\rm cov}-\frac{c_{\rm tot}}2M^2\right|
   \ge Cc_{\rm tot}\big(\sqrt{\lambda R}\,M+\lambda R\big)\right)
 \le C e^{-c\lambda}
\tag{Z}
\]

for all sufficiently large \(\lambda\). The exact electrical-network normalization appears explicitly in the proof: Zhai replaces \(2|E|\) by \(c_{\rm tot}\), and obtains center \(c_{\rm tot}M^2/2\).

## 4. Electrical-network normalization for a symmetric reversible chain

Fix one `n`-state irreducible symmetric reversible chain with transition matrix \(P=(p_{xy})\). The Aldous–Fill symmetry assumptions imply uniform stationarity and

\[
 E_xT_y=E_yT_x \quad\text{for all }x,y,
\tag{1}
\]

and also

\[
 \tau_0=E_\pi T_x\quad\text{for every }x.
\tag{2}
\]

Realize the chain as the electrical network with conductances

\[
 c_{xy}=p_{xy}.
\]

Because \(P\) is symmetric, these are symmetric conductances. Since every row of \(P\) sums to one,

\[
 c_x=\sum_yc_{xy}=1,
 \qquad
 c_{\rm tot}=\sum_{x,y}c_{xy}=n.
\tag{3}
\]

Self-loops cause no problem: Zhai's network definition explicitly allows them. The network's discrete walk has exactly transition matrix \(P\). Its continuous-time version inserts independent mean-one exponential waiting times between embedded-chain steps.

For every embedded-chain stopping index `N` with finite expectation, if `E_1,E_2,...` are the independent `Exp(1)` holding times, then

\[
 E\left[\sum_{j=1}^{N}E_j\right]=E[N].
\tag{4}
\]

Thus expected continuous-time hitting and cover times agree with their discrete-time step-count counterparts. We may therefore use the same symbols \(E_xT_y,\tau_0,EC\).

## 5. Exact GFF variance identity

Let \(\eta\) be a pinned GFF on the network. Recenter it by its spatial average:

\[
 \zeta_x=\eta_x-\bar\eta,
 \qquad
 \bar\eta=\frac1n\sum_{v}\eta_v.
\tag{5}
\]

Then \(\sum_x\zeta_x=0\) identically, and the increments are unchanged:

\[
 E(\zeta_x-\zeta_y)^2=R_{\rm eff}(x,y).
\tag{6}
\]

The expected maximum is also unchanged because \(E\bar\eta=0\):

\[
 E\max_x\zeta_x
 =E\left(\max_x\eta_x-\bar\eta\right)
 =E\max_x\eta_x=M.
\tag{7}
\]

The chain symmetry acts transitively on the state space in the sense used by Aldous–Fill, so the law of the centered GFF is invariant under that action. Hence

\[
 \operatorname{Var}(\zeta_x)=\sigma^2
\tag{8}
\]

is independent of `x`.

Since \(n^{-1}\sum_y\zeta_y=0\) identically,

\[
 \frac1n\sum_y\operatorname{Cov}(\zeta_x,\zeta_y)=0.
\tag{9}
\]

Averaging (6) over `y` therefore gives

\[
 \frac1n\sum_yR_{\rm eff}(x,y)
 =\frac1n\sum_y\left(\sigma^2+\sigma^2
 -2\operatorname{Cov}(\zeta_x,\zeta_y)\right)
 =2\sigma^2.
\tag{10}
\]

Now use the electrical-network commute identity

\[
 E_xT_y+E_yT_x=c_{\rm tot}R_{\rm eff}(x,y)=nR_{\rm eff}(x,y).
\tag{11}
\]

By (1),

\[
 E_xT_y=\frac n2R_{\rm eff}(x,y).
\tag{12}
\]

Average (12) in `y` with the uniform stationary law. Using (2) and (10),

\[
 \boxed{\tau_0=n\sigma^2.}
\tag{13}
\]

This is the normalization that makes the sharp constant `1` emerge.

## 6. Gaussian maximum: the sharp center is at most tau0 log n

The coordinates \(\zeta_x\) need not be independent. Independence is unnecessary for the standard log-sum-exp bound. For every \(t>0\),

\[
 e^{t\max_x\zeta_x}\le\sum_xe^{t\zeta_x},
\]

so Jensen and the Gaussian mgf give

\[
 e^{tM}
 \le E e^{t\max_x\zeta_x}
 \le n e^{t^2\sigma^2/2}.
\]

Therefore

\[
 M\le \frac{\log n}{t}+\frac{t\sigma^2}{2}.
\]

Optimizing at \(t=\sqrt{2\log n}/\sigma\) gives

\[
 \boxed{M\le \sigma\sqrt{2\log n}.}
\tag{14}
\]

Combining (3), (13), and (14), Zhai's center obeys

\[
 \boxed{
 A:=\frac{c_{\rm tot}}2M^2
 =\frac n2M^2
 \le n\sigma^2\log n
 =\tau_0\log n.
 }
\tag{15}
\]

Thus the desired leading constant is already present before controlling the concentration error.

## 7. Resistance diameter and the error scale

Aldous–Fill Lemma 7.2(ii) gives

\[
 \max_{x,y}E_xT_y\le2\tau_0.
\tag{16}
\]

Using (12),

\[
 \frac n2 R
 =\max_{x,y}E_xT_y
 \le2\tau_0,
\]

so

\[
 \boxed{R\le\frac{4\tau_0}{n}=4\sigma^2.}
\tag{17}
\]

Integrating Zhai's exponential tail (Z) gives a universal constant \(C_1\) such that

\[
 E\left|\tau_{\rm cov}-A\right|
 \le C_1 n\big(\sqrt R\,M+R\big).
\tag{18}
\]

For completeness, (18) is a direct layer-cake consequence of (Z): parameterize the tail threshold by

\[
 u(\lambda)=C n(\sqrt{\lambda R}\,M+\lambda R),
\]

split the integral at the fixed lower allowed \(\lambda_0\), and substitute \(u=u(\lambda)\). Since

\[
 u'(\lambda)=Cn\left(\frac{\sqrt R M}{2\sqrt\lambda}+R\right)
\]

and \(\int_{\lambda_0}^\infty e^{-c\lambda}(\lambda^{-1/2}+1)\,d\lambda<\infty\), the claimed bound follows after absorbing the bounded initial segment.

Now (14), (17), and (13) imply

\[
 n\sqrt R\,M
 \le n(2\sigma)(\sigma\sqrt{2\log n})
 =2\sqrt2\,\tau_0\sqrt{\log n},
\tag{19}
\]

and

\[
 nR\le4\tau_0.
\tag{20}
\]

Hence, using (15) and (18),

\[
 \begin{aligned}
 EC
 &=E\tau_{\rm cov}\\
 &\le A+C_1n(\sqrt R\,M+R)\\
 &\le \tau_0\log n+C_2\tau_0(\sqrt{\log n}+1).
 \end{aligned}
\tag{21}
\]

Therefore

\[
 \boxed{
 EC\le \tau_0\log n\left(1+O\!\left(\frac1{\sqrt{\log n}}\right)\right).
 }
\tag{22}
\]

In particular,

\[
 \boxed{EC\le(1+o(1))\tau_0\log n,}
\]

which is exactly the affirmative answer requested in Aldous–Fill Open Problem 7.6, with a stronger explicit rate.

## 8. Hypothesis audit / noncircularity

No estimate of the unknown cover time is fed back into the proof. The chain inputs are only:

1. symmetric reversibility / transitivity as assumed in the source, yielding uniform stationarity and symmetric hitting times;
2. Aldous–Fill's already-proved Lemma 7.2(ii), \(\max E_xT_y\le2\tau_0\);
3. the commute identity in the electrical network;
4. Zhai's published electrical-network concentration theorem;
5. an elementary Gaussian maximum inequality.

The usual Zhai corollary written in terms of \(t_{\rm hit}/t_{\rm cov}\) is not needed, so there is no circular need to know the cover time scale first.

## 9. Prior-art disposition as of 2026-09-19

Checked primary/later sources:

- Aldous–Fill current Chapter 7 HTML still states Open Problem 7.6.
- Zhai, arXiv `1407.7617`, published in *Electronic Journal of Probability* 23 (2018), proves the needed general electrical-network concentration theorem.
- Jonathan Hermon, *A Spectral Characterization for Concentration of the Cover Time*, J. Theor. Probab. 33 (2020), gives later concentration characterizations for vertex-transitive graphs and more general chains.
- A bounded exact-phrase/citation search did not locate an explicit statement “Aldous–Fill Open Problem 7.6 is solved by Zhai”. That absence is not a novelty certificate.

Because the substantive probabilistic theorem is already published and the deduction above is short and elementary, the honest fleet status is **KNOWN / literature-implied resolution**, not a fresh `PROVED` claim by R7-05. Accordingly R7-05 must not create `operations/claims/P0246.md` under the owner rule excluding known/solved work. Coordinator reconciliation may update the shared queue/intake status; R7-05 does not edit shared `QUEUE.md`, `RESULTS.md`, or `POSTED.md`.

## 10. Reusable takeaway

For any finite symmetric reversible chain in the Aldous–Fill class, the zero-sum GFF has the exact variance identity

\[
 \operatorname{Var}(\zeta_x)=\frac{\tau_0}{n}.
\]

This makes the universal Gaussian maximum bound align exactly with the conjectured sharp cover-time constant:

\[
 \frac n2(E\max\zeta)^2\le\tau_0\log n.
\]

The old direct-Markov-chain “cycle versus rapidly mixing” dichotomy is therefore unnecessary for the upper bound once the problem is translated through the GFF.
