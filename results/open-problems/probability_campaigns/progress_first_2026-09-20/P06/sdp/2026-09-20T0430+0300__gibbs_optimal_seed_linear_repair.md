Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated maximum-reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — optimized Gibbs seed, selected-energy asymptotics, and exact linear moment repair

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `ac069301e2058269d0fbf2072e00d50398ae1680`.  
No P07-A/P07-B canonical claim or peer report is modified. This remains a complementary SDP/moment-polytope line.

## 1. Fixed source metric and inherited state

P06 / Randomstrasse Conjecture 17 is already a **KNOWN** endpoint in later literature. Its fixed repository metric remains

`U_ER^cert = 1`.

I do not rescreen or attempt to rediscover it.

For P07 / Randomstrasse Conjecture 18, the strongest recovered primary source theorem remains

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Thus the source-level iterated-log loss is unchanged. The old TH18 handoff and the active P07-A/P07-B roles already give the exact moment-polytope / orthant / one-sided-completion equivalences. In the moment language, it is enough to build a symmetric probability law on `Z_n` whose selected cosine moments all equal `-1/sqrt(n)`; then the common moment depth satisfies `delta_D>=1/sqrt(n)`, hence the corresponding orthant/completion ratio is at most `sqrt(n)`.

The immediately preceding complementary report proved, for odd prime `n`, random `D subset H={1,...,(n-1)/2}`, and

\[
S_D(j)=\sum_{a\in D}\cos(2\pi aj/n),
\qquad
p_{D,c}(j)=\frac{e^{-cS_D(j)/\sqrt n}}{nZ_D(c)},
\]

that for fixed `c>0`,

\[
Z_D(c)=e^{c^2/32}+o_{\mathbb P}(1),
\tag{1.1}
\]

\[
\frac1{\sqrt n}\,\mathbb E_{p_{D,c}}S_D\to_{\mathbb P}-\frac c{16},
\tag{1.2}
\]

and, if

\[
\mu_a(c):=\mathbb E_{p_{D,c}}\cos(2\pi aJ/n),
\]

then the exact Parseval/collision identity gives

\[
\sum_{a\in H}\mu_a(c)^2
=\frac12\left(\frac{Z_D(2c)}{Z_D(c)^2}-1\right)
\to_{\mathbb P}\frac12\big(e^{c^2/16}-1\big).
\tag{1.3}
\]

At `c=4`, the average selected moment is exactly at `-1/sqrt(n)` asymptotically, but the inherited worst-case selected residual bound was only

\[
\|\mu_D(4)+n^{-1/2}{\bf 1}\|_2^2
\le \frac{2e-3}{4}+o_{\mathbb P}(1)
=0.6091409\ldots+o_{\mathbb P}(1).
\tag{1.4}
\]

The present run changes the correction architecture in three ways:

1. it shows that **`c=4` is not the best Newton seed** even though it matches the selected average;
2. it computes the **annealed selected Fourier energy** sharply and finds an even better mean-square seed;
3. it replaces nonlinear exponential-family Newton contraction by an **exact linear multiplicative repair lemma**. For feasibility, the essential estimate is only a one-sided centered distortion bound, not a two-sided log-density bound plus a second-order remainder estimate.

---

# 2. New high-probability theorem: optimize the Gibbs seed before correcting coordinates

Define the selected target residual

\[
r_D(c):=\mu_D(c)+\frac1{\sqrt n}{\bf 1}_D,
\qquad
R_D(c):=\|r_D(c)\|_2^2.
\tag{2.1}
\]

For every realization,

\[
\begin{aligned}
R_D(c)
&=\sum_{a\in D}\mu_a(c)^2
+\frac2{\sqrt n}\sum_{a\in D}\mu_a(c)
+\frac{|D|}{n}\\
&\le \sum_{a\in H}\mu_a(c)^2
+\frac2{\sqrt n}\mathbb E_{p_{D,c}}S_D
+\frac{|D|}{n}.
\end{aligned}
\tag{2.2}
\]

Using (1.2), (1.3), and `|D|/n -> 1/4`, we obtain the source-coupled high-probability upper envelope

\[
\boxed{
R_D(c)
\le b(c)+o_{\mathbb P}(1),
\qquad
b(c):=\frac12e^{c^2/16}-\frac14-\frac c8.
}
\tag{2.3}
\]

This is valid for every fixed `c>0` on the prime subsequence.

The function `b` is strictly convex at its unique positive minimizer. Since

\[
b'(c)=\frac{c}{16}e^{c^2/16}-\frac18,
\]

the minimizing constant `c_HP` is the unique positive root of

\[
\boxed{c_{\rm HP}e^{c_{\rm HP}^2/16}=2.}
\tag{2.4}
\]

Numerically,

\[
\boxed{c_{\rm HP}=1.6774592960\ldots}
\]

and

\[
\boxed{
b(c_{\rm HP})=0.1364572394\ldots.}
\tag{2.5}
\]

Therefore

\[
\boxed{
\|r_D(c_{\rm HP})\|_2
\le 0.369401191+o_{\mathbb P}(1).
}
\tag{2.6}
\]

This is a strict quantitative improvement over the `c=4` seed bound `0.780475...+o_P(1)` in the preceding report. The reason is important: **matching the radial/average moment exactly is not the same as minimizing the full Euclidean coordinate residual**. Once a multivariate correction is available, deliberately leaving a radial error can reduce the total correction burden substantially.

No source theorem is closed by (2.6); it is a stronger seed for the missing coordinatewise repair.

---

# 3. New annealed theorem: selected Fourier energy is asymptotically half of the total energy

The total-energy identity (1.3) does not say how much Fourier energy lies on the selected mask itself. The following calculation does.

For fixed `c>0`, put

\[
t=\frac c{\sqrt n},
\qquad
w_j=e^{-tS_D(j)},
\qquad
\nu_a=\frac1n\sum_{j\in\mathbb Z_n}c_a(j)w_j,
\tag{3.1}
\]

where `c_a(j)=cos(2 pi a j/n)`. Then

\[
\mu_a(c)=\frac{\nu_a}{Z_D(c)}.
\]

Define the unnormalized selected energy

\[
N_D(c):=\sum_{a\in H}\xi_a\nu_a^2,
\tag{3.2}
\]

where `xi_a=1_{a in D}`.

### Theorem 3.1 — annealed selected-energy limit

As `n->infinity` through odd primes,

\[
\boxed{
\mathbb E_D\sum_{a\in D}\mu_a(c)^2
\longrightarrow
\frac14\big(e^{c^2/16}-1\big).
}
\tag{3.3}
\]

Thus, in expectation, asymptotically one half of the full nonzero Fourier energy lies on the selected half-mask.

## Proof

Expanding the square in (3.2),

\[
\mathbb E N_D(c)
=\frac1{n^2}\sum_{j,k\in\mathbb Z_n}
\mathbb E_D\left[
 e^{-t(S_D(j)+S_D(k))}
 Q_D(j,k)
\right],
\tag{3.4}
\]

where

\[
Q_D(j,k):=\sum_{a\in H}\xi_a c_a(j)c_a(k).
\]

For fixed `j,k`, write

\[
u_a=c_a(j)+c_a(k),\qquad v_a=c_a(j)c_a(k).
\]

Independence of the mask bits gives the exact factorization

\[
M_{jk}:=\mathbb E_D e^{-t\sum_a\xi_a u_a}
=\prod_{a\in H}\frac{1+e^{-tu_a}}2,
\tag{3.5}
\]

and

\[
\mathbb E_D[Q_D(j,k)e^{-t\sum_a\xi_a u_a}]
=M_{jk}\sum_{a\in H}
\frac{v_a}{1+e^{tu_a}}.
\tag{3.6}
\]

We now classify the replica pairs.

### 3.1 Diagonal and anti-diagonal nonzero pairs

If `j!=0` and `k=+/-j`, then `u_a=2c_a(j)` and `v_a=c_a(j)^2`. Prime cyclic orthogonality gives

\[
\sum_{a\in H}c_a(j)=-\frac12,
\qquad
\sum_{a\in H}c_a(j)^2=\frac{n-2}{4}.
\tag{3.7}
\]

Using

\[
\log\frac{1+e^{-x}}2=-\frac x2+\frac{x^2}{8}+O(x^4)
\]

uniformly for `|x|=O(n^{-1/2})`, we get

\[
M_{j,\pm j}=e^{c^2/8+o(1)}.
\tag{3.8}
\]

Also

\[
\frac1{1+e^x}=\frac12-\frac x4+O(x^3).
\]

For primes `n>3`, `cos^3 x=(3cos x+cos3x)/4` and the same prime Fourier sum gives

\[
\sum_{a\in H}c_a(j)^3=-\frac12.
\]

Hence

\[
\sum_{a\in H}\frac{c_a(j)^2}{1+e^{2tc_a(j)}}
=\frac n8+O(1).
\tag{3.9}
\]

There are exactly `2(n-1)` such ordered nonzero pairs, so their contribution to (3.4) converges to

\[
\frac14e^{c^2/8}.
\tag{3.10}
\]

### 3.2 Generic nonzero pairs

Now let `j,k!=0` and `k!=+/-j`. Then

\[
\sum_a c_a(j)c_a(k)=-\frac12,
\]

and therefore

\[
\sum_a u_a=-1,
\qquad
\sum_a u_a^2=\frac{n-4}{2}.
\tag{3.11}
\]

Thus

\[
M_{jk}=e^{c^2/16+o(1)}.
\tag{3.12}
\]

For pairs that additionally avoid the four simple cubic resonances

\[
k=\pm2j,\qquad j=\pm2k\pmod n,
\]

product-to-sum identities give

\[
\sum_a v_a u_a=O(1).
\]

Consequently

\[
\sum_a\frac{v_a}{1+e^{tu_a}}
=-\frac14+o(1)
\tag{3.13}
\]

uniformly over all such nonresonant generic pairs. The resonant generic set has only `O(n)` ordered pairs. For it, the crude bound `sum_a v_a u_a=O(n)` makes the right side of (3.6) at most `O(sqrt(n))` after the first-order logistic expansion, so its total contribution after the `n^{-2}` normalization is `o(1)`.

There are `n^2+O(n)` generic ordered pairs. Hence their total contribution converges to

\[
-\frac14e^{c^2/16}.
\tag{3.14}
\]

### 3.3 Pairs involving the origin

If exactly one of `j,k` is zero, every selected frequency contributes `1+c_a(k)` to the exponent. Since

\[
\sum_{a\in H}(1+c_a(k))=\frac{n-2}{2},
\]

(3.5) is `exp(-c sqrt(n)/4+O_c(1))`; the extra factor from the sum in (3.6) is at most `O(n)`. There are only `O(n)` such pairs, so their normalized contribution is exponentially small. The `(0,0)` term is even smaller. Thus all origin-involving pairs contribute `o(1)`.

Combining (3.10), (3.14), and the origin estimate,

\[
\boxed{
\mathbb E N_D(c)
\to
\frac14\left(e^{c^2/8}-e^{c^2/16}\right).
}
\tag{3.15}
\]

Finally, Parseval gives the deterministic domination

\[
0\le N_D(c)
\le\sum_{a\in H}\nu_a^2
=\frac12\big(Z_D(2c)-Z_D(c)^2\big)
\le\frac12Z_D(2c).
\tag{3.16}
\]

The inherited self-averaging theorem gives bounded second moments for `Z_D(2c)`, so `N_D(c)` is uniformly integrable. Also Jensen and the exact uniform identity `n^{-1}sum_j S_D(j)=0` imply

\[
Z_D(c)\ge1
\tag{3.17}
\]

deterministically, while `Z_D(c)->e^{c^2/32}` in probability. Therefore

\[
\mathbb E\frac{N_D(c)}{Z_D(c)^2}
- e^{-c^2/16}\mathbb E N_D(c)\to0.
\]

Using (3.15) proves (3.3). ∎

---

# 4. New mean-square optimal seed

The previous aggregate theorem gives

\[
\frac1{\sqrt n}\sum_{a\in D}\mu_a(c)
=\frac1{\sqrt n}\mathbb E_{p_{D,c}}S_D
\to_{\mathbb P}-\frac c{16}.
\tag{4.1}
\]

This convergence also holds in expectation. Indeed by Cauchy,

\[
\left(\frac1{\sqrt n}\sum_{a\in D}\mu_a(c)\right)^2
\le \frac{|D|}{n}\sum_{a\in D}\mu_a(c)^2
\le\frac12\sum_{a\in D}\mu_a(c)^2,
\]

and the selected energy is uniformly integrable by (3.16)-(3.17).

Therefore, expanding the target residual exactly and applying (3.3),

\[
\boxed{
\mathbb E R_D(c)
\longrightarrow
\rho(c):=\frac14e^{c^2/16}-\frac c8.
}
\tag{4.2}
\]

At the old radial-matching choice `c=4`,

\[
\boxed{
\mathbb E R_D(4)\to\frac{e-2}{4}=0.1795704571\ldots,
}
\tag{4.3}
\]

which is already much smaller than the preceding report's pathwise upper envelope `0.60914...`.

More importantly, `rho` has a unique positive minimizer `c_MS` satisfying

\[
\boxed{c_{\rm MS}e^{c_{\rm MS}^2/16}=4.}
\tag{4.4}
\]

Numerically,

\[
\boxed{c_{\rm MS}=2.6116745617\ldots}
\]

and

\[
\boxed{
\rho(c_{\rm MS})=0.05643677821\ldots.
}
\tag{4.5}
\]

Thus

\[
\boxed{
\left(\mathbb E\|r_D(c_{\rm MS})\|_2^2\right)^{1/2}
\to 0.237564262\ldots.
}
\tag{4.6}
\]

This is a second, annealed optimization. It is stronger numerically than (2.6), but (4.6) is an **expectation** statement, not yet a high-probability concentration theorem for the selected energy. For the source expectation theorem we ultimately need a bad-event probability at least as small as `o(1/sqrt(log n))`; (4.6) alone does not provide that.

The two optimized seeds have distinct roles:

- `c_HP=1.677459...` gives a rigorous **high-probability upper envelope** `||r||_2<=0.369402+o_P(1)` from already self-averaging quantities;
- `c_MS=2.611675...` minimizes the **annealed selected mean-square residual**, with limiting RMS `0.237565...`, and motivates a selected-energy concentration attack.

---

# 5. General fixed-c covariance floor; the optimized seed also improves the bad exponent

The preceding report proved a full-dimensional covariance floor only at `c=4`. The same proof works for every fixed `c>0` and is worth recording because the optimized seed reduces the subpolynomial loss substantially.

Let

\[
\Sigma_D(c)=\operatorname{Cov}_{p_{D,c}}(\Phi_D),
\qquad
\Phi_D(j)=(c_a(j))_{a\in D}.
\]

On the binomial event `|D|<=3(n-1)/8`, the covariance under the uniform law on `Z_n\{0}` has minimum eigenvalue at least `n/[8(n-1)]`. If

\[
q_*(c):=\min_{j\ne0}n p_{D,c}(j),
\]

the same variance comparison therefore gives

\[
\lambda_{\min}\Sigma_D(c)\ge\frac18q_*(c).
\tag{5.1}
\]

The inherited Hoeffding estimate gives, with failure at most `1/n`,

\[
\max_{j\ne0}S_D(j)
\le -\frac14+\frac12\sqrt{(n-2)\log n}.
\tag{5.2}
\]

The inherited `Var Z_D(c)=O_c(1/n)` estimate gives, with failure `O_c(1/n)`,

\[
Z_D(c)\le2e^{c^2/32}
\]

for all large `n`. Hence, with failure `O_c(1/n)`,

\[
\boxed{
\lambda_{\min}\Sigma_D(c)
\ge
\frac{1+o(1)}{16e^{c^2/32}}
\exp\left[-\frac c2\sqrt{\log n}\right].
}
\tag{5.3}
\]

At the high-probability optimized seed,

\[
\boxed{
\lambda_{\min}\Sigma_D(c_{\rm HP})
\ge
(0.0572388\ldots+o(1))
 e^{-0.83872965\ldots\sqrt{\log n}}
}
\tag{5.4}
\]

with failure `O(1/n)`. Compare this with the old `c=4` exponent `e^{-2 sqrt(log n)}`. The generic floor is still far too weak to prove a bounded Newton distortion, but the optimized seed improves both the residual norm and the covariance-loss exponent.

---

# 6. New exact repair lemma: no nonlinear Newton remainder is needed

This is the main architectural change of the run.

Let `p` be **any strictly positive symmetric probability law** on `Z_n`, not necessarily Gibbs. Put

\[
\mu=\mathbb E_p\Phi_D,
\qquad
t_*=-\frac1{\sqrt n}{\bf 1}_D,
\qquad
r=\mu-t_*,
\]

and assume

\[
\Sigma=\operatorname{Cov}_p(\Phi_D)
\]

is invertible. Define the source-coupled Newton direction exactly as requested,

\[
\boxed{h_N=-\Sigma^{-1}r.}
\tag{6.1}
\]

But instead of exponentiating this direction, center it and use it as a **linear density repair**:

\[
g_N(j):=h_N\cdot(\Phi_D(j)-\mu).
\tag{6.2}
\]

Then `E_p g_N=0` and

\[
\mathbb E_p[\Phi_D g_N]
=\operatorname{Cov}_p(\Phi_D,h_N\cdot\Phi_D)
=\Sigma h_N
=-r.
\tag{6.3}
\]

### Theorem 6.1 — one-step exact moment repair

If

\[
\boxed{\min_j g_N(j)\ge-1,}
\tag{6.4}
\]

then

\[
\boxed{q(j):=p(j)(1+g_N(j))}
\tag{6.5}
\]

is a symmetric probability law and has the **exact target moments**

\[
\boxed{\mathbb E_q\Phi_D=t_*=-n^{-1/2}{\bf1}_D.}
\tag{6.6}
\]

#### Proof

Condition (6.4) gives `q(j)>=0`. Equation (6.2) gives

\[
\sum_jq(j)=1+\mathbb E_pg_N=1.
\]

Symmetry follows because `p` and every cosine feature are even. Finally,

\[
\begin{aligned}
\mathbb E_q\Phi_D
&=\mu+\mathbb E_p[\Phi_Dg_N]\\
&=\mu-r=t_*.
\end{aligned}
\]

There is no Taylor expansion and no second-order remainder. ∎

Thus the previous requested sufficient estimate

\[
\max_j|h_N\cdot\Phi_D(j)|=O(1)
\]

can be weakened substantially. The sharp one-shot condition is only the **one-sided centered** bound (6.4).

### Theorem 6.2 — damped exact contraction

Define

\[
B(p):=\max_j(-g_N(j))_+.
\]

For any

\[
0\le\alpha\le \min\{1,B(p)^{-1}\}
\]

(with `B^{-1}=+infinity` if `B=0`), the law

\[
q_\alpha(j)=p(j)(1+\alpha g_N(j))
\tag{6.7}
\]

is a probability law and its residual is **exactly**

\[
\boxed{r(q_\alpha)=(1-\alpha)r(p).}
\tag{6.8}
\]

Again there is no nonlinear error term.

This can be iterated while preserving strict positivity by choosing, for example,

\[
\alpha_k=\min\left\{\frac12,\frac1{2B(p_k)}\right\}.
\tag{6.9}
\]

If along the resulting repair path

\[
\boxed{B(p_k)\le B_0<\infty\quad\text{for every }k,}
\tag{6.10}
\]

then `alpha_k>=alpha_0:=min{1/2,1/(2B_0)}>0` and

\[
\|r(p_k)\|_2\le(1-\alpha_0)^k\|r(p_0)\|_2\to0.
\]

The probability simplex is compact, so a subsequence converges to a probability law `p_*`; continuity of the moments gives

\[
\mathbb E_{p_*}\Phi_D=t_*.
\tag{6.11}
\]

Hence a **uniform `O(1)` one-sided centered Newton-distortion bound along the damped linear-repair path is sufficient for exact feasibility**, even if the one-step bound `B<=1` is unavailable.

This is strictly more useful than controlling an exponential Newton step: the repair itself is exactly linear in the moments, and the only nontrivial issue is positivity.

---

# 7. Exact probabilistic estimate that would now close the source expectation theorem

The source-level closure target can now be stated without ambiguity.

Start from either the high-probability optimized Gibbs seed `p_{D,c_HP}` or, after proving selected-energy concentration, the mean-square optimized seed `p_{D,c_MS}`. It is sufficient to prove that outside an event of probability

\[
\boxed{q_n=o(1/\sqrt{\log n}),}
\tag{7.1}
\]

one of the following holds:

1. **one-shot version:** its centered source-coupled direction satisfies `B(p)<=1`; or
2. **damped-path version:** the strictly positive linear-repair iterates satisfy `sup_k B(p_k)<=B_0` for an absolute constant `B_0`.

Either condition produces a symmetric probability law with all selected moments exactly `-1/sqrt(n)`, so

\[
\delta_D\ge\frac1{\sqrt n}
\]

and hence the exact moment/orthant identity gives the sharp instance bound

\[
\vartheta\le1+\sqrt n
\]

on the good event.

The primary random-circulant paper supplies the fallback

\[
\vartheta\le1+4\sqrt{n\log n}
\]

outside probability at most `2/n`; on the residual fallback-failure event use the deterministic `theta<=n`. Therefore (7.1) makes the total bad-event contribution `o(sqrt(n))`, yielding

\[
\mathbb E\vartheta(G_n)\le(1+o(1))\sqrt n.
\]

Combined with the source lower bound, this would prove Conjecture 18. No such distortion theorem is claimed here.

---

# 8. What failed, what changed, and the next attack

The old plan treated `c=4` as privileged because it matches the target selected moment **on average**. Sections 2 and 4 show that this is not the right criterion for a multivariate correction:

- `c_HP=1.677459...` minimizes the currently rigorous high-probability residual envelope;
- `c_MS=2.611675...` minimizes the exact limiting **expected selected squared residual**;
- both are better Newton/repair seeds than `c=4` by the relevant metric.

The old plan also asked for a bounded exponential log-density change plus a Newton remainder theorem. Section 6 removes that unnecessary nonlinear obstacle: a centered linear multiplicative correction moves the moment vector by **exactly** `Sigma h`, so only positivity remains.

### Next mathematical attack

The next run should therefore target the scalar source-coupled quantity

\[
B_D(c)
:=
\max_{j\in\mathbb Z_n}
\left[-h_N(c)\cdot(\Phi_D(j)-\mu(c))\right]_+,
\qquad
h_N(c)=-\Sigma_D(c)^{-1}r_D(c),
\tag{8.1}
\]

rather than a generic `lambda_min` or `||h||_1` bound.

Priority order:

1. start with `c=c_HP`, because both a high-probability residual bound and the stronger covariance exponent are already proved;
2. derive a two-replica / leave-one-frequency representation for the **negative tail** of (8.1), exploiting the exact Fourier-energy identity and the selected-energy calculation above;
3. separately try to prove concentration of
   \[
   \sum_{a\in D}\mu_a(c)^2
   \]
   around its annealed limit. If successful at `c_MS`, the seed residual should concentrate near `0.0564368`, substantially reducing the correction scale;
4. do not spend another run sharpening the generic minimum-eigenvalue floor unless it enters a source-coupled bound for (8.1).

Finite SDP experiments may suggest the distribution of `B_D(c)` or which seed is superior, but they are not asymptotic evidence and cannot replace the required probability theorem.

Prime `n` remains a real restriction of the present Gibbs calculations. Removing it still requires explicit gcd/resonance bookkeeping.

---

# 9. Obligation ledger

Fixed full-source P07 metric:

\[
\sqrt n\le\mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}
\quad\text{(unchanged).}
\]

Substantive intermediate movement this run:

- **PROVED PARTIAL:** optimized high-probability Gibbs seed `c_HP=1.677459...` with `||r||_2<=0.369402+o_P(1)`;
- **PROVED PARTIAL:** annealed selected Fourier-energy limit (3.3);
- **PROVED PARTIAL:** exact expected residual curve `rho(c)=e^{c^2/16}/4-c/8` and mean-square optimum `c_MS=2.611675...`, limiting residual squared `0.0564368`;
- **PROVED PARTIAL:** general fixed-`c` covariance floor (5.3), improving the subpolynomial exponent at the optimized seed;
- **PROVED PARTIAL:** exact one-shot and damped linear moment-repair lemmas, reducing the source bottleneck to one-sided centered positivity control;
- **OPEN:** prove `B_D(c)<=1` in one shot or a uniform `B_D=O(1)` bound along the damped repair path with failure `o(1/sqrt(log n))`;
- **OPEN:** selected-energy concentration strong enough to upgrade the `c_MS` expectation advantage to the source-required high-probability regime;
- **OPEN:** remove the prime-order restriction by genuine resonance/gcd analysis.

No full-source solution or publication-level novelty claim is made.