Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Erratum to `2026-09-19T011045Z__P0429_exponential_busy_projection_square_root_threshold.md`

This immutable erratum corrects an overclaim in the preceding artifact. The earlier file must be read together with this correction.

## What remains proved

The following statements in the preceding artifact are valid and retained.

1. For exponential service, with `M=sum_i N_i` and `B=sum_i 1_{N_i>0}`,

\[
E B=n\rho,
\qquad
\operatorname{Cov}(M,B)=\frac{n\rho(k+1)}2.
\]

2. By exchangeability and the geometric M/M/1 marginal,

\[
\boxed{
\operatorname{Cov}(N_i,B_j)
=\frac{\rho(k-1)}{2(n-1)}
\quad(i\ne j).
}
\]

3. Stationary association implies

\[
\boxed{
0\le \operatorname{Cov}(B_i,B_j)
\le\frac{\rho(k-1)}{2(n-1)}.
}
\]

Hence

\[
\operatorname{Var}(B)
\le n\rho(1-\rho)+\frac{n\rho(k-1)}2.
\]

4. Combining the exact covariance upper bound with the already proved fixed-pair linear response

\[
\operatorname{Cov}(B_i,B_j)
=\rho^2C_{\rho,\mu}\lambda\frac{k-1}{n-1}
+O((k/n)^2)
\]

gives the sharpened coefficient interval

\[
\boxed{
\frac{(1-\rho)^2}{2\rho^2\mu}
\le C_{\rho,\mu}
\le\frac1{2\rho^2\mu}.
}
\]

5. Conditional on the full-system busy count `B`, the tagged busy vector is hypergeometric. Coupling sampling without replacement to sampling with replacement, then applying the Hellinger bound to the resulting Bernoulli mixture, gives

\[
\boxed{
 d_{\rm TV}(P^{\rm busy}_{n,k},\operatorname{Ber}(\rho)^{\otimes k})
\le
\frac{k(k-1)}{2n}
+
\sqrt{
\frac{k[(1-\rho)+(k-1)/2]}
{n(1-\rho)}
}.
}
\]

Therefore the rigorous new theorem is

\[
\boxed{
 k^2/n\to0
\quad\Longrightarrow\quad
 d_{\rm TV}(P^{\rm busy}_{n,k},\operatorname{Ber}(\rho)^{\otimes k})\to0.
}
\]

6. The Walsh/Parseval calculation is also valid as an `L^2` diagnostic:

\[
\chi^2(P^{\rm busy}_{n,k}\|Q_k)
\ge
\binom{k}{2}
\left[
\frac{\operatorname{Cov}(B_1,B_2)}{\rho(1-\rho)}
\right]^2.
\]

Thus at `k^2/n -> tau in (0,infinity)` the pair-Walsh contribution to chi-square remains bounded away from zero. **This does not by itself imply a total-variation lower bound.**

## What is withdrawn

The claimed converse

\[
 d_{\rm TV}(P^{\rm busy}_{n,k},Q_k)\to0
\Longrightarrow k^2/n\to0
\]

is **not proved** by the preceding artifact.

The precise gap is in Section 3.1 -> 3.2. The Neumann/resolvent argument was justified only for each **fixed** selected dimension `r`. It produced bounds such as

\[
E\prod_{i\in A}(B_i-\rho)=O_r(\varepsilon^{\lceil |A|/2\rceil}),
\qquad
\varepsilon=(k-1)/(n-1),
\]

with constants allowed to depend on `r`. Section 3.2 then substituted a growing dimension

\[
m\asymp n/k,
\]

without proving that those constants remain uniform as `m\to\infty`. That step is not justified. Consequently the asserted uniform fourth-moment estimate

\[
E S_m^4=O_T(m^2)
\]

remains an **UNPROVED LEMMA**, and the truncation argument converting variance inflation into a positive TV gap is not certified.

This is exactly the kind of dimension-uniform issue that the source problem is about, so it cannot be treated as a technicality.

## Correct current exponential-service state

For the busy/idle projection we rigorously have

\[
k=o(\sqrt n)
\quad\Longrightarrow\quad
\text{TV independence},
\]

and at the square-root scale the pair-Walsh `chi^2` contribution is nonvanishing. A TV necessity theorem at that scale remains open in this R7-01 record.

For the **full workload vector**, the source-wide theorem from the earlier R7-01 artifact remains

\[
k=o(n^{1/3})\Longrightarrow\text{TV independence}
\]

under every finite-second-moment service law. No new exponential full-workload threshold is claimed here.

The frozen source metric `M_alpha` remains `1/3`; this erratum does not change it.