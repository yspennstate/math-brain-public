# Limited fork-join: a stationary exponential-service partial candidate

Status: private author-checked partial result for P0429. No independent review or novelty certification. The general finite-second-moment service question is not solved. The basic collision and empty-start coupling method is already in Wang et al., *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, Sections 3-5, archived as `queues_limited_forkjoin_2018`. We credit that method and its $k=o(n^{1/4})$ theorem. This packet sharpens the marginal emptying-time step under an additional exponential-service assumption and restores thinned arrival rates explicitly.

## Model and candidate bound

There are $n\ge2$ FIFO servers. Jobs arrive as a Poisson process of rate $\Lambda=n\lambda/k$, independently select uniform $k$-subsets of servers, and place one task in each selected queue. Service requirements of all tasks, including different tasks of the same job, are independent and identically distributed, independent of routing and arrivals. Fix the marginal rate $0<\lambda<\mu$, with mean service $1/\mu$. Let $\pi_{n,k}$ be the stationary joint workload law at any specified $k$ servers, and let $\nu_k$ be the product of their marginal stationary workload laws. Total variation uses $\sup_A|\pi(A)-\nu(A)|$.

Write $r(T)$ for the probability that a stationary marginal M/G/1 workload has not hit zero by time $T$. The modular coupling bound is

$$d_{\rm TV}(\pi_{n,k},\nu_k)\le 2k r(T)+\frac{3\lambda T k(k-1)^2}{2(n-1)},\qquad T>0.$$

With exponential service of rate $\mu$, put $\rho=\lambda/\mu$ and $c=(\sqrt\mu-\sqrt\lambda)^2>0$. Then

$$r(T)\le(1+\sqrt\rho)e^{-cT},$$

so the candidate explicit stationary bound is

$$d_{\rm TV}(\pi_{n,k},\nu_k)\le 2k(1+\sqrt\rho)e^{-cT}+\frac{3\lambda T k(k-1)^2}{2(n-1)}.$$

Either right-hand side may also be capped at one. The constants are uniform in $n,k$ at fixed $\lambda,\mu$.

## Step 1: independent arrivals with exactly restored marginal rates

Fix the tagged set $K$ with $|K|=k$. For one job let $N$ count selected servers in $K$. Counting ordered pairs gives

$$\mathbb E[N(N-1)]=\frac{k^2(k-1)^2}{n(n-1)}.$$

Poisson marking decomposes the arrival stream into independent streams indexed by its selected tagged subset. Retain every singleton-tagged arrival, discard all arrivals hitting two or more tagged queues, and add independent Poisson arrivals to each tagged queue at the marginal rate removed from that queue. The resulting $k$ arrival processes are independent Poisson processes of rate exactly $\lambda$. Give added tasks independent service requirements with the original law, and use identical marks on shared singleton arrivals.

Over $[0,T]$, the probability of any discrepancy is bounded by the expected number of discarded job events plus the expected total number of added task events. These are bounded by

$$\Lambda T\left(\mathbb P(N\ge2)+\mathbb E[N\mathbf1_{N\ge2}]\right)\le\frac32\Lambda T\mathbb E[N(N-1)].$$

Here $1\le N(N-1)/2$ and $N\le N(N-1)$ when $N\ge2$. Substitution of $\Lambda=n\lambda/k$ yields the collision term in the stated bound. This argument is nonasymptotic and does not require $2k\le n$.

Start the original and modified queues empty. Until the first discrepancy their tagged workload paths agree, because they have identical tagged arrival times and task marks. Thus the same bound controls total variation at time $T$.

## Step 2: couple empty starts to stationary starts

For the original system, couple one copy with stationary workloads at time zero to a copy with empty workloads, using the same future routing, arrivals and service marks. The stationary workload is coordinatewise above the empty-start workload. Whenever a stationary coordinate hits zero, both copies have zero workload there and then agree forever at that coordinate.

Each stationary coordinate is a marginal M/G/1 queue with the same $\lambda$ and service law, even though coordinates are dependent. By a union bound, the probability that any of the $k$ coordinates has failed to couple by $T$ is at most $kr(T)$. The independent comparison system has the same marginal law, so its own stationary-versus-empty coupling has the same bound. The triangle inequality between these two comparisons and Step 1 proves the modular estimate. Independence of the original stationary coordinates is neither assumed nor required.

## Step 3: exponential-service emptying tail

Consider the marginal M/M/1 queue count $Q$ until its first hit $\tau_0$ of zero. For $q\ge1$, its generator applied to $h(q)=a^q$, with $a=\sqrt{\mu/\lambda}>1$, is

$$\frac{{\cal L}h(q)}{h(q)}=\lambda(a-1)+\mu(a^{-1}-1)=-(\sqrt\mu-\sqrt\lambda)^2=-c.$$

Stopping first at zero and at a finite upper count level makes the standard exponential generator martingale legitimate. Nonnegativity and Fatou's lemma upon removal of the upper stopping level give

$$\mathbb E_q\left[e^{c(T\wedge\tau_0)}a^{Q(T\wedge\tau_0)}\right]\le a^q.$$

On $\{\tau_0>T\}$ the integrand is at least $e^{cT}$, so $\mathbb P_q(\tau_0>T)\le a^qe^{-cT}$. Averaging over the stationary geometric queue count yields

$$\mathbb E[a^{Q(0)}]=\frac{1-\rho}{1-\rho a}=\frac{1-\rho}{1-\sqrt\rho}=1+\sqrt\rho.$$

A marginal workload is zero exactly when its queue count is zero. The count process here is used only to bound this marginal stopping time; the pathwise workload coupling in Step 2 remains driven by shared task marks. No erroneous identification of arbitrary coupled count and workload paths is needed.

## Consequences and limits

Taking $T=2\log n/c$ gives

$$d_{\rm TV}(\pi_{n,k},\nu_k)\le\frac{2k(1+\sqrt\rho)}{n^2}+\frac{3\lambda k(k-1)^2\log n}{c(n-1)}.$$

Hence the distance tends to zero when $k=o((n/\log n)^{1/3})$ under exponential service. This is a sufficient regime, not an optimal threshold, and says nothing at the boundary $k\asymp n^{1/3}$ by itself. Poisson arrivals see the stationary pre-arrival workload law by PASTA. The arriving job selects its uniform target set independently of that law; exchangeability makes its selected workloads have the law of the specified tagged set. Appending independent tagged-job service requirements and taking a maximum is a Markov kernel, so total variation contracts; the same error controls the job-delay distribution against the independent comparison.

More generally, if $r(T)\le C T^{-p}$ for some fixed $p>0$, the modular estimate gives an error of order $k/T^p+Tk^3/n$. Balancing at $T\asymp(n/k^2)^{1/(p+1)}$ gives the sufficient regime $k=o(n^{p/(3p+1)})$. This conclusion is conditional on the stated emptying-tail bound; no unproved implication from a service moment is used. For $p=1$, the source's finite-second-moment estimate recovers the known exponent $1/4$.

## Attempts to break the argument

The vulnerable points are the growing number of tagged queues, simultaneous multi-hit arrivals, the marginal rate after removing those arrivals, and the passage to stationarity. The proof restores lost marginal rates rather than silently comparing to lower-load queues. It uses a union bound over all $k$ queues and retains both empty-start errors. The exponential tail constant tends to zero as load approaches one, so this packet does not claim a uniform heavy-traffic result. Correlated within-job service marks are excluded. Exponential control of the stationary emptying time has not been proved here for general service laws.

The original paper already has the same broad finite-time/emptying-time proof structure and numerical experiments at larger exponents. The observation here could be a known or straightforward corollary; bounded search is not a novelty certificate. No full original open-problem solution is promoted. Arithmetic controls are in `check_forkjoin_stationary.py` and `forkjoin_stationary_checks.json`.
