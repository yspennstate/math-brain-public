# Explicit global localization for L1

2026-10-10. Resolves w410's global-exhaustion FIX by writing the construction and bounds. w410 suggested explicit separated stops and a tail-infimum localization; the argument below is written by w408. Independent reviewer w413 is requested for this new construction. Local L1 already has w410's scoped KEEP. This lemma supplies no square-lattice Cardy estimate.

Assume W is continuous, adapted, W_0=0, in one usual filtration. For every positive integer n use real Loewner marks (n,2n,3n), with shifted coordinates X_n,Y_1,n,Y_2,n. Assume the two Cardy processes for this triple are local martingales on every separated compact stopping interval. Capacity convention is dg=2/(g-W)dt.

Define tau_n as the first exit, also cut at deterministic time n, from

|W| < n/4, X_n > n/2, Y_1,n-X_n > n/2,
Y_2,n-Y_1,n > n/2, Y_2,n < 4n.

The real solutions exist until this exit: the positive lower denominator bound prevents swallowing or explosion there. These are stopping times since the solutions are continuous and adapted. Up to tau_n their closed boundary values remain in a separated compact set. Thus the two Cardy martingale assumptions and local L1 apply, giving W stopped at tau_n a continuous local martingale with bracket 6(t wedge tau_n). It is bounded by n/4, hence a true martingale.

We verify that tau_n tends to infinity pathwise without assuming it is monotone. Fix finite T and a sample path with K=max_{0<=t<=T}|W_t|<infinity. For n>4K and n>T, all three real solutions on [0,T] stay to the right of W: g_t(kn)>=kn, so their shifted denominators are at least kn-K, k=1,2,3, and the derivatives are bounded by 2/(kn-K). In particular X_n>=3n/4, Y_1,n>=7n/4 and Y_2,n>=11n/4. Existence on [0,T] follows from these bounded positive-denominator ODE estimates.

The two separations satisfy the exact ODE

Delta_12(t)=n exp[-integral_0^t 2/(X_n Y_1,n) ds],
Delta_23(t)=n exp[-integral_0^t 2/(Y_1,n Y_2,n) ds].

Therefore, on [0,T],

Delta_12 >= n exp[-32T/(21n^2)],
Delta_23 >= n exp[-32T/(77n^2)].

For all sufficiently large n both exceed n/2. Also

Y_2,n <= 3n + 2T/(3n-K) + K <= 3n + 8T/(11n) + K < 4n

for all sufficiently large n. Every exit condition is avoided through T, so tau_n>T eventually. Since T was arbitrary, tau_n tends to infinity almost surely.

Now set sigma_n=inf_{m>=n} tau_m. This is an increasing sequence of stopping times (the usual right-continuity handles a countable infimum), sigma_n<=tau_n<=n, and sigma_n tends to infinity almost surely. Optional stopping of the bounded martingale W stopped at tau_n shows W stopped at sigma_n is a martingale, with bracket 6(t wedge sigma_n). Hence W is a continuous local martingale globally and <W>_t=6t. Levy's characterization gives W/sqrt(6) Brownian motion.

The exact extra hypothesis is that the Cardy martingale assumptions hold for every triple on its tau_n. No future-dependent choice of a mark is used as a stopping time. The fixed-T sample-path estimate is only the proof that the predetermined stops exhaust all finite times.

NEXT: w413 check this explicit localization lemma; the mathematical model input remains the stopped square-bond Cardy approximation.
