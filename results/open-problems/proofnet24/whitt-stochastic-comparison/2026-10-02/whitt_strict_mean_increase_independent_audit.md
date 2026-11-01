# Independent audit of the explicit strictly larger-mean witness

2 October 2026. Full mathematical and parameter-binding audit. Historical priority and external expert acceptance remain unverified.

## Verdict

The proof and exact certificate in `whitt_strict_mean_increase_proof.md` and `whitt_strict_mean_increase_exact.py` are valid. An independently implemented generator and exact rational solver reproduced the probability bounds. The target rates are correctly scaled, its mean is strictly larger, the service stop-loss comparison is strict at every finite nonnegative threshold, and the reversed waiting tail is certified at an explicit positive threshold. No continuity assumption is needed for this explicit witness.

The independent code is `whitt_strict_mean_increase_independent_check.py`, with output in `whitt_strict_mean_increase_independent_checks.json`. It imports no matrix or generator helper from the production certificate.

## Literal model binding

Both queues have two homogeneous FCFS servers and Poisson arrival rate11/10. The base law is

    S=(1/5)E with probability3/7,
      (8/5)E with probability4/7,

whereE is exponential of meanone. Its mean isone. The intermediate lawT has means1/1000 and8/5 with probabilities200/533 and333/533. Its mean is alsoone.

Setbeta=10001/10000 andU=beta*T. The actual target service means, rates, and probabilities are therefore

    mean10001/10000000, rate10000000/10001, probability200/533;
    mean10001/6250, rate6250/10001, probability333/533.

The independent implementation starts from these literal service means and derives the rates by reciprocal, rather than importing a possibly stale rate list. It checksE U=beta exactly.

As an additional binding check, it computes the unchanged target service lawT at arrival rate(11/10)*beta=110011/100000. Exact time rescaling requires its delay enclosure to equal that ofU at arrival11/10. The independently computed lower bounds, upper bounds, and slow-tail bounds agree as exact Fractions, not merely to displayed precision. This would detect an omitted service scaling or an accidental use of the original arrival rate with the unscaled target.

## Strict service comparison

The intermediate martingale coupling is correct. Keep the large base class unchanged. In the small class replace its multiplier1/5 by1/1000 with probability1400/1599 and8/5 with probability199/1599, using the sameE. The replacement's conditional mean is1/5; the resulting short probability is(3/7)*(1400/1599)=200/533. Conditional Jensen givesS<=cx T.

Scaling givesU>T almost surely. For every finite thresholdt>=0, sinceT has a positive exponential tail,

    E[(U-t)+]-E[(T-t)+]
      >=(beta-1)E[T*1{T>t}]>0.

ThusE[(U-t)+]>E[(S-t)+] for everyt>=0. Atzero the difference isbeta-1=1/10000. The increasing-convex stop-loss characterization givesS<=icx U. In the cdf orientation of Whitt's proposed strengthened condition,

    integral_t^infinity(F_S(u)-F_U(u))du
      =E[(U-t)+]-E[(S-t)+]>0,  t>=0.

All means and tail integrals are finite. The comparison genuinely includes thresholdzero and does not exploit the equal-mean endpoint equality.

## Independent generator and solver

The independent phase ordering at each busy level is the number0,1,2 of small jobs in service. The production generator instead enumerates unordered class pairs, in the opposite order. At countone the independent phases are large then small. This independent enumeration gives a direct check on physical generator binding.

At countn>=3, a small completion(ratei*mu_s) leavesi-1 small jobs and chooses a fresh small class with probabilityp or large with1-p; a large completion(rate(2-i)*mu_l) leavesi small jobs and similarly chooses the replacement. At counttwo there is no queued replacement. Below counttwo arrivals choose their service class; at higher counts arrivals retain the current service phase. The diagonal always includes the original arrival rate, including the maximum retained countN=80, where it is the killing rate. Every exact row sum equalszero belowN andarrival rate atN in the negative killed generator.

The independent solver performs block linear elimination by solving simultaneously for the outgoing-block transfer and two occupation columns. It does not reuse the production inverse routine or transformed-right-side helper. It then checks every row of the original backward equations for time rewardone and busy reward1{count>=2}; every occupation has0<busy time<total time.

## Why these finite computations enclose the infinite queue

For the killed state setA={count<=80}, the two occupation columns areh=(-Q_A)^-1*1 andg=(-Q_A)^-1*f. Stationary incoming flux from the genuine infinite queue is supported only on count80. Therefore its conditional busy probability withinA is a convex combination ofg(x)/h(x) over those entry phases. All states outsideA are busy. If their stationary mass isdelta, the total probability isrbar+delta*(1-rbar).

Both service laws are dominated job by job by their slowest exponential component using the sameE multiplier. Workload and individual start/finish-time monotonicity give count domination by the respective slow M/M/2 queue. Thusdelta is at most the exact tail

    gamma=[2rho²/(1+rho)]*rho^79,

withrho22/25 for the baseline and110011/125000 for the scaled target. Consequently the lower enclosure isming/h and the upper enclosure ismaxg/h+gamma*(1-maxg/h). This is a rigorous infinite-state enclosure; no uncontrolled truncation error is being ignored.

## Reproduced exact bounds

The independent output displays

    Base lower: .3928726193785124206366671950742728563769600690751058873
    Base upper: .3928931900472240517674819361196440707363530945657863330
    Target lower: .3904100961171857913875746396412345814989030137704568529
    Target upper: .3904309172156204546413347038758258673484982382003552460

The rigorous lower bound on the delay-probability gap is

    .002441702162891965995332491198446989028461830874750641321
       >12/5000.

The decimal strings display exact rational calculations. Only Fraction comparisons establish the inequalities.

## Explicit positive waiting threshold

When a baseline arrival is delayed, it can begin service withinh only if a service completion occurs. Each of the two busy servers has exponential rate at mostfive, so the total completion intensity is at mostten. HenceP(0<W_S<=h)<=10h. At h=1/100000,

    P(W_S>h)-P(W_U>h)
       >=P(W_S>0)-P(W_U>0)-10h
        >23/10000.

The independent exact lower bound displayed for this tail gap is

    .002341702162891965995332491198446989028461830874750641321.

This is a strict increasing-convex service comparison at every nonnegative threshold, with a strictly larger target mean and strictly positive continuous service distributions, yet a reversed waiting tail at a positive threshold. It refutes the asserted full stochastic comparison and the corresponding strict integrated-tail strengthening; it leaves the weaker mean-wait conjecture unaddressed.

## Reproduction

    python whitt_strict_mean_increase_independent_check.py

The script uses Python's standard library alone and independently checks generator rows, all exact backward equations, the physical scaled means and rates, the exact time-rescaling equality, and both rational gap assertions.
