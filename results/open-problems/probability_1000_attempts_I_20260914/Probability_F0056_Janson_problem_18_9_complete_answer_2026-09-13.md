# Janson's Problem 18.9: the sparse regime of the largest box, answered

13 September 2026. Ledger row F0056 (intake F), source Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Problem 18.9, Section 18.2, PDF page 89.

## The question

Janson's Theorem 18.7 describes the largest boxes in a random allocation of $m$ balls into $n$ boxes with weight sequence $w = (w_k)_{k \ge 0}$, $w_0 > 0$, $\omega = \infty$: the allocation $(Y_1,\dots,Y_n)$ has probability proportional to $\prod_i w_{Y_i}$ on $\{\sum_i Y_i = m\}$. Write $\Phi(t) = \sum_k w_k t^k$, $\rho$ for its radius of convergence, $\Psi(t) = t\Phi'(t)/\Phi(t)$, and $\nu = \lim_{t \uparrow \rho} \Psi(t)$. For $m/n < \nu$ let $\tau_n$ solve $\Psi(\tau_n) = m/n$ and let $\xi^{(n)}$ have the tilted law $\pi_k = w_k \tau_n^k/\Phi(\tau_n)$, so $\mathbb{E}\xi^{(n)} = m/n$ exactly. The theorem, in the version with $\xi^{(n)}$, says that when $m/n \to \lambda$ with $0 < \lambda < \nu$, the largest values $Y_{(1)} \ge Y_{(2)} \ge \dots$ of the allocation behave like the largest values of $n$ independent copies of $\xi^{(n)}$: for $N_{[h,\infty)} = |\{i : Y_i \ge h\}|$,

(i) $n\,\mathbb{P}(\xi^{(n)} \ge h(n)) \to \alpha \in [0,\infty]$ implies $N_{[h(n),\infty)} \to \mathrm{Po}(\alpha)$;
(ii) $n\,\mathbb{P}(\xi^{(n)} \ge h(n)) \to 0$ implies $Y_{(1)} < h(n)$ w.h.p.;
(iii) $n\,\mathbb{P}(\xi^{(n)} \ge h(n)) \to \infty$ implies $Y_{(j)} \ge h(n)$ w.h.p. for each fixed $j$;
(iv) $\tilde d_K(N_{[h(n),\infty)}, \bar N^{(n)}_{[h(n),\infty)}) \to 0$ for every $h(n)$, where $\bar N^{(n)}$ is the count for the independent copies;
(v) $d_K(Y_{(j)}, \xi^{(n)}_{(j)}) \to 0$ for each fixed $j$;
(vi) $d_{TV}(Y_{(1)}, \xi^{(n)}_{(1)}) \to 0$.

Problem 18.9 asks whether this remains true for $\lambda = 0 < \nu$, that is when $m/n \to 0$.

## The answer

Three facts settle it. The first two were already on the record (attempts F0056-A001 and A002 and the candidate counterexample of 9 September); what was missing was the analytic half of the counterexample and, more importantly, the positive theorem that says exactly where the counterexample stops working.

**Bounded $m$ is excluded by a triviality.** If $m$ stays bounded then at most $m$ boxes are nonempty while the independent count $\bar N_{[1,\infty)}$ is binomial with mean $n(1 - \pi_0) \to m$ along any subsequence where $m$ is constant, so part (i) with $h = 1$ fails. ($m = 1$: one nonempty box against a Poisson(1) count.) The question therefore concerns $m \to \infty$, $m/n \to 0$, and that is the reading used below.

**Theorem 1 (the answer is yes when $w_1 > 0$).** Let $w_0 > 0$, $w_1 > 0$, $\omega = \infty$, $\rho > 0$. Let $m = m(n) \to \infty$ with $m/n \to 0$. Then all six parts of Theorem 18.7 hold in the $\xi^{(n)}$ version.

**Theorem 2 (the answer is no when $w_1 = 0$).** Let $w_0 > 0$, $w_1 = 0$, $\omega = \infty$, $\rho > 0$ and $\mathrm{span}(w) = 1$. Put $a = \min\{k \ge 1 : w_k > 0\} \ge 2$ and $b = \min\{k : w_k > 0,\ a \nmid k\}$ (it exists because the span is one, and $b > a$). Let $m \to \infty$ with $m \not\equiv 0 \pmod a$ and $n \to \infty$ with $n/m^{b/(b-a)} \to \infty$. Then $Y_{(1)} \ge b$ almost surely while $\mathbb{P}(\xi^{(n)}_{(1)} \ge b) \to 0$, so parts (i), (ii), (iv), (v) and (vi) all fail, and $d_{TV}(Y_{(1)}, \xi^{(n)}_{(1)}) \to 1$.

The ledger's construction $w_0 = 1$, $w_1 = 0$, $w_k = 1$ for $k \ge 2$, $n = k^4$, $m = 2k+1$ is the case $a = 2$, $b = 3$, $n \gg m^3$ of Theorem 2. So Problem 18.9 has a negative answer as posed, for every weight sequence with $w_1 = 0$, and a positive answer under the single extra hypothesis $w_1 > 0$, which holds in every classical allocation model (equiprobable balls, uniform compositions, and every $w$ equivalent to a probability weight sequence with $\mathbb{P}(\xi = 1) > 0$). The hypothesis is not a convenience: the proof of Theorem 1 uses $w_1 > 0$ in one place, a bound on the characteristic function of $\xi^{(n)}$ away from the origin, and Theorem 2 is exactly what happens when that bound is lost.

## Proof of Theorem 2

Every allocation of positive weight has all $Y_i \in \mathrm{supp}(w)$. If every nonzero $Y_i$ were a multiple of $a$ then $m = \sum_i Y_i$ would be, so some box has a size in $\mathrm{supp}(w)$ not divisible by $a$, hence $Y_{(1)} \ge b$. (The conditioned allocation exists for large $m$: since the span is one, every large integer is a sum of elements of $\mathrm{supp}(w) \setminus \{0\}$, using at most $m \le n$ summands.)

For the independent side, as $t \to 0$, $\Phi(t) = w_0 + w_a t^a + O(t^{a+1})$ and $\Psi(t) = (a w_a/w_0)\, t^a\,(1 + O(t))$, so $\tau_n \sim (w_0 \mu_n/(a w_a))^{1/a}$ with $\mu_n = m/n$, and for $\tau_n \le \tau_0 < \rho$,
$$\mathbb{P}(\xi^{(n)} \ge b) \le \frac{1}{w_0}\sum_{k \ge b} w_k \tau_n^k \le C\,\tau_n^{\,b} = O(\mu_n^{\,b/a}).$$
Hence $n\,\mathbb{P}(\xi^{(n)} \ge b) = O(n\,\mu_n^{b/a}) = O\big(m^{b/a} n^{1-b/a}\big) \to 0$, which is the hypothesis $n/m^{b/(b-a)} \to \infty$. So $\mathbb{P}(\xi^{(n)}_{(1)} \ge b) \le n\,\mathbb{P}(\xi^{(n)} \ge b) \to 0$.

Now take $h(n) \equiv b$ in (i): $\alpha = 0$ but $N_{[b,\infty)} \ge 1$ surely. The same $h$ breaks (ii) and (iv), since $|\mathbb{P}(N_{[b,\infty)} \le 0) - \mathbb{P}(\bar N^{(n)}_{[b,\infty)} \le 0)| \to 1$. For (v) and (vi), $d_K(Y_{(1)}, \xi^{(n)}_{(1)}) \ge |\mathbb{P}(Y_{(1)} \le b-1) - \mathbb{P}(\xi^{(n)}_{(1)} \le b-1)| \to 1$, and $d_{TV} \ge d_K$. $\square$

(Part (iii) is not claimed to fail; in this regime the number of nonempty boxes tends to infinity in both models.)

## Proof of Theorem 1

Throughout, $\mu = \mu_n = m/n \to 0$, $\tau = \tau_n$, $\pi_k = w_k\tau^k/\Phi(\tau)$, and $C$ denotes constants depending on $w$ only. Fix $\tau_0 \in (0,\rho)$; for large $n$, $\tau \le \tau_0$.

*Asymptotics of the tilted law.* Since $w_1 > 0$, $\Psi(t) = (w_1/w_0)\,t\,(1 + O(t))$, so $\tau = (w_0/w_1)\,\mu\,(1 + O(\mu))$, $\pi_1 = \mu(1 + O(\mu))$, $\pi_0 = 1 - O(\mu)$, and for each fixed $r \ge 1$,
$$\sum_{k \ge 2} k^r \pi_k \le \frac{\tau^2}{w_0}\sum_{k \ge 2} k^r w_k \tau_0^{\,k-2} = O(\tau^2) = O(\mu^2).$$
Hence $\mathbb{E}(\xi^{(n)})^r = \mu\,(1 + O(\mu))$ for $r = 1,2,3$; in particular $\sigma^2 := \mathrm{Var}\,\xi^{(n)} = \mu(1 + O(\mu))$ and $\mathbb{E}(\xi^{(n)})^3 \le C\mu$. Also $\mathbb{P}(\xi^{(n)} \ge K) \le C\,(\tau/\tau_0)^K$ for every $K \ge 1$.

*Lemma A (local limit theorem in the Poisson regime).* Fix $r \ge 0$ and let $S_N = \xi_1 + \dots + \xi_N$ be a sum of $N = n - r$ independent copies of $\xi^{(n)}$, with $M_N = N\mu$ and $V_N = N\sigma^2$. Then, uniformly in $j \in \mathbb{Z}$,
$$\mathbb{P}(S_N = j) = \frac{1}{\sqrt{2\pi V_N}}\exp\Big(-\frac{(j - M_N)^2}{2V_N}\Big) + o\big(m^{-1/2}\big).$$

*Proof.* Let $\varphi(t) = \mathbb{E}e^{it\xi^{(n)}} = \Phi(\tau e^{it})/\Phi(\tau)$ and $\psi_N(t) = (e^{-i\mu t}\varphi(t))^N$, the characteristic function of $S_N - M_N$. By inversion,
$$2\pi\,\mathbb{P}(S_N = j) = \int_{-\pi}^{\pi} e^{-i(j - M_N)t}\,\psi_N(t)\,dt.$$

Away from the origin: with $\xi'$ an independent copy, $|\varphi(t)|^2 = \mathbb{E}\cos(t(\xi - \xi')) \le 1 - \mathbb{P}(|\xi - \xi'| = 1)(1 - \cos t) \le 1 - 2\pi_0\pi_1(1 - \cos t)$. This is the one place $w_1 > 0$ is used. For large $n$, $2\pi_0\pi_1 \ge \mu$, so, using $1 - \cos t \ge 2t^2/\pi^2$ on $[-\pi,\pi]$,
$$|\psi_N(t)| = |\varphi(t)|^N \le \exp\big(-\tfrac12 N\mu(1 - \cos t)\big) \le \exp\big(-M_N t^2/\pi^2\big), \qquad |t| \le \pi. \tag{1}$$

Near the origin: $|\varphi(t) - 1| \le \mu|t| \le \pi\mu \to 0$, so $\log\varphi$ is defined on $[-\pi,\pi]$ for large $n$, and expanding $\varphi(t) = 1 + i\mu t - \tfrac12\mathbb{E}\xi^2\,t^2 + R(t)$ with $|R(t)| \le \mathbb{E}\xi^3|t|^3/6 \le C\mu|t|^3$, together with $\log(1+z) = z - z^2/2 + O(|z|^3)$ and $\mathbb{E}\xi^2 = O(\mu)$, gives
$$\log\varphi(t) = i\mu t - \tfrac12\sigma^2 t^2 + O(\mu|t|^3), \qquad\text{so}\qquad \psi_N(t) = \exp\big(-\tfrac12 V_N t^2 + O(M_N|t|^3)\big). \tag{2}$$

Let $\varepsilon_n = m^{-3/8}$. For $|t| \le \varepsilon_n$, $M_N|t|^3 \le C m^{-1/8} \to 0$, so by (2), $|\psi_N(t) - e^{-V_N t^2/2}| \le C\,M_N|t|^3 e^{-V_N t^2/2}$, and
$$\int_{|t| \le \varepsilon_n}\big|\psi_N(t) - e^{-V_N t^2/2}\big|\,dt \le C M_N \int_{\mathbb{R}}|t|^3 e^{-V_N t^2/2}\,dt = O(M_N V_N^{-2}) = O(m^{-1}).$$
For $\varepsilon_n \le |t| \le \pi$, (1) gives $\int |\psi_N| \le 2\int_{\varepsilon_n}^\infty e^{-M_N t^2/\pi^2}dt \le C M_N^{-1/2} e^{-M_N\varepsilon_n^2/\pi^2} = o(m^{-1/2})$ because $M_N\varepsilon_n^2 \sim m^{1/4} \to \infty$; and $\int_{|t| > \varepsilon_n} e^{-V_N t^2/2}dt = o(m^{-1/2})$ for the same reason. Therefore
$$2\pi\,\mathbb{P}(S_N = j) = \int_{\mathbb{R}} e^{-i(j-M_N)t} e^{-V_N t^2/2}\,dt + o(m^{-1/2}) = \sqrt{\tfrac{2\pi}{V_N}}\,\exp\Big(-\tfrac{(j-M_N)^2}{2V_N}\Big) + o(m^{-1/2}),$$
uniformly in $j$. $\square$

Two consequences. Since $V_N = m(1 + o(1))$ and $M_N = m - r\mu = m + o(1)$:

(A1) *Ratio.* For fixed $r \ge 0$ and integers $0 \le K \le K_n$ with $K_n = o(\sqrt m)$,
$$\frac{\mathbb{P}(S_{n-r} = m - K)}{\mathbb{P}(S_n = m)} \to 1 \quad\text{uniformly in } K,$$
because both point probabilities are $(1 + o(1))/\sqrt{2\pi m}$ (the Gaussian factors are $\exp(-O((K+1)^2/m)) \to 1$).

(A2) *Uniform bound.* $\sup_j \mathbb{P}(S_{n-1} = j) \le (2\pi)^{-1}\int_{-\pi}^{\pi}|\varphi|^{n-1} \le (2\pi)^{-1}\int_{\mathbb{R}} e^{-M_{n-1}t^2/\pi^2}dt = O(m^{-1/2})$ by (1), while $\mathbb{P}(S_n = m) \ge c\,m^{-1/2}$ by Lemma A with $j = m$. Hence $\sup_j \mathbb{P}(S_{n-1} = j) \le C\,\mathbb{P}(S_n = m)$.

*The truncation level.* Put $B = B(n) = \lceil m^{1/4}\rceil = o(\sqrt m)$. Then $n\,\mathbb{P}(\xi^{(n)} \ge B) \to 0$: indeed $\log\big(n\,C(\tau/\tau_0)^B\big) = \log C + \log m + \log(n/m) - B\log(\tau_0/\tau)$, and since $\tau \le 2(w_0/w_1)\mu$ for large $n$, $\log(\tau_0/\tau) \ge \log(n/m) - c_1 =: L_n \to \infty$, so the expression is at most $\log C + \log m + c_1 - (B-1)L_n \to -\infty$.

*Janson's proof now runs.* The allocation law is unchanged if $w$ is replaced by the tilted probability weight sequence $(\pi_k)$ (the factor $\tau^m/\Phi(\tau)^n$ cancels), so Janson's (17.11) reads
$$\mathbb{P}(Y_1 = k) = \pi_k\,\frac{\mathbb{P}(S_{n-1} = m-k)}{\mathbb{P}(S_n = m)}, \qquad
\mathbb{P}(Y_1 = k_1,\dots,Y_\ell = k_\ell) = \pi_{k_1}\cdots\pi_{k_\ell}\,\frac{\mathbb{P}(S_{n-\ell} = m - \sum k_i)}{\mathbb{P}(S_n = m)}.$$
By (A2), $\mathbb{P}(Y_1 = k) \le C\pi_k$ for all $k$, so $\mathbb{P}(Y_{(1)} \ge B) \le n\,\mathbb{P}(Y_1 \ge B) \le Cn\,\mathbb{P}(\xi^{(n)} \ge B) \to 0$, and likewise $\xi^{(n)}_{(1)} < B$ w.h.p.; this is Janson's (18.19)-(18.20) with $B(n)$ in place of $\delta_n\sqrt n$. By (A1) with $r = \ell$ and $K = \sum k_i \le \ell B = o(\sqrt m)$, the joint probabilities equal $(1 + o(1))\prod\pi_{k_i}$ uniformly for $k_i \le B$; this is (18.21)-(18.22). From here the proof of Theorem 18.7 in the source is verbatim: the factorial moments $\mathbb{E}(N_{[h,B]})_\ell \to \alpha^\ell$ give (i) for $\alpha < \infty$, the thinning argument gives $\alpha = \infty$, (ii), (iii) are special cases, (iv) and (v) are formal consequences of (i) with the binomial Poisson approximation on the independent side, and the proof of (vi) uses only the joint Poisson limits of $(N_{A_l}, N_{B_l}, N_{A_l^c})$, which follow from the same joint factorial moments, together with (v). No step of it refers to the regime $m/n \to \lambda > 0$ except through Lemma 13.1 and Remark 13.2, which (A1) and (A2) replace. $\square$

## Remarks

1. **Why the dividing line is $w_1$.** In the Poisson regime the sum $S_n$ is essentially a count of boxes holding one ball plus a small perturbation, and its point probabilities are smooth in the lattice direction because $\mathbb{P}(\xi - \xi' = \pm 1) \asymp \mu$ with $n\mu = m \to \infty$. When $w_1 = 0$ the dominant boxes hold $a \ge 2$ balls and the sum lives, to first approximation, on $a\mathbb{Z}$; the characteristic function at $t = 2\pi j/a$ has modulus $1 - O(\pi_b)$, and $|\varphi(2\pi j/a)|^n \to 1$ exactly when $n\pi_b \to 0$, which is Theorem 2's regime. The same bound shows the obstruction disappears when $n\pi_b \gg \log m$; the range $n\pi_b \asymp 1$ to $\log m$ for $w_1 = 0$ is not settled here.

2. **What is classical.** For the equiprobable scheme $w_k = 1/k!$ the sparse regime $m/n \to 0$ is Kolchin, Sevast'yanov and Chistyakov's left domain, and statements of the type of (i)-(iii) there are old. Theorem 1 is that picture for an arbitrary weight sequence with $w_1 > 0$ and all six parts of Theorem 18.7, and Theorem 2 is the reason the hypothesis cannot be dropped. I did not find Problem 18.9 addressed in the literature; that search was not exhaustive and the usual caveat applies.

3. **Numerical check, for the record.** For $w_k \equiv 1$ (uniform weak compositions, $w_1 = 1$) the exact first two factorial moments of $N_{[2,\infty)}$ are, against the Poisson prediction $\alpha = n\,\mathbb{P}(\xi^{(n)} \ge 2) = n\tau^2$ with $\tau = m/(m+n)$:

| $m$ | $n$ | $\mathbb{E}N$ | $\alpha$ | $\mathbb{E}N(N-1)$ | $\alpha^2$ |
| --- | --- | --- | --- | --- | --- |
| 100 | $10^4$ | 0.97078 | 0.98030 | 0.90518 | 0.96098 |
| 300 | $10^5$ | 0.89167 | 0.89462 | 0.78451 | 0.80035 |
| 1000 | $10^6$ | 0.99701 | 0.99800 | 0.99005 | 0.99601 |

For the parity sequence, at $k = 10, 100, 1000$: $\tau_n k^{3/2} = 1.00073, 1.00174, 1.00023$ and $n\,\mathbb{P}(\xi^{(n)} \ge 3) = 0.327, 0.101, 0.032$, decaying like $k^{-1/2}$ as the proof says, while $\mathbb{P}(Y_{(1)} \ge 3) = 1$ exactly. Script: `f0056_check.py` (mpmath, 30 digits).

## Status

Mathematics: complete, author-checked once against the source's proof line by line. Verification word: author checked, no independent read yet. Prior art: a bounded search, not a clearance. The ledger row should move from `candidate counterexample, author stage` to `answered: no in general (Theorem 2), yes under w_1 > 0 (Theorem 1)`, with both theorems stated.
