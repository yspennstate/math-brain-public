from pathlib import Path
p=Path('~/brain_workers/TRIO_1011/op/F0021')
with p.joinpath('SECOND_ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

## Proposition 12: the subadditivity shortcut is false (proved logical obstruction)
Already at time n=1, put two nonnegative reward fields on the same site (+1), of values a,b>0, with zero at (-1). At inverse temperature beta>0,

Z(a+b)=(1+exp(beta(a+b)))/2,
Z(a)Z(b)=(1+exp(beta a))(1+exp(beta b))/4,
Z(a+b)-Z(a)Z(b)=(exp(beta a)-1)(exp(beta b)-1)/4>0.

These are exact two-path partition functions. Thus a bound Z(background+tail)<=Z(background)Z(tail) is false, even when the two fields are positive and can be the cap and excess at one site. It cannot be inserted after Theorem 11.

A stronger deterministic example shows why bare-walk invisibility is insufficient. Fix kappa<1/3<rho<1, beta>0, and a>log 2/beta. At sites (i,i) for i=1,...,n-1 put the bounded reward a, at (n,n) put v_n=n^rho, and put zero at every other site. Cap above at u_n=n^kappa; for large n, a<u_n<v_n. The rare-only field in Theorem 11 is now just the terminal spike, whose bare-walk partition function is
1+2^{-n}(exp(beta v_n)-1)->1.
The original and capped partition functions instead equal

Z= C_n+exp(beta a(n-1)-n log 2+beta v_n),
Zcap=C_n+exp(beta a(n-1)-n log 2+beta u_n),
C_n=sum_{r=0}^{n-1}2^{-(r+1)} exp(beta a r).

Proof. A path has a unique initial run of r all-right steps. If r<n, it leaves the diagonal at step r+1 and can never return to a site (i,i); its reward is a r. If it takes n right steps it visits the terminal spike and receives a(n-1)+v_n (or a(n-1)+u_n). The probabilities of these events are 2^{-(r+1)} and 2^{-n}, respectively.
Since exp(beta a)/2>1, the geometric sum C_n is at most C exp((beta a-log 2)n), with C independent of n. The all-right capped term has this same exponential factor multiplied by exp(beta u_n-beta a). Hence C_n divided by that term is O(exp(-beta u_n)). Apply log(1+t)<=t to both partition functions after factoring their all-right terms to obtain

log Z-log Zcap=beta(v_n-u_n)+O(exp(-beta u_n)),

which is much larger than n^{1/3}. This is not iid disorder, so it is NOT a counterexample to F0021. It is a counterexample to a purely deterministic inference from bare-walk tail invisibility to invisibility in every capped background.

## Approach B: an explicit obstruction to a routine moment comparison
The source allows the negative side to have only a second moment. Fix alpha>5 and r in (2,3). Let Y and V be independent standard Pareto variables with tail exponents alpha and r, respectively, and define X to have mixture law Y with probability 1/2 and -V with probability 1/2. Its mean m and variance sigma^2 exist and sigma>0: moments of order p of a Pareto(s) variable exist for p<s, as follows by integrating its density s t^{-s-1}, t>=1. Normalize omega=(X-m)/sigma. Then E omega=0 and E omega^2=1, and for all sufficiently large t,

P(omega>t)=(1/2)(sigma t+m)^{-alpha}.

The quotient of this expression at ct and t tends to c^{-alpha} for c>0, so the right tail is regularly varying with exponent alpha. Yet E|omega|^3=infinity: on the negative mixture component, for all sufficiently large V, |(-V-m)/sigma|^3>=V^3/(8 sigma^3), and E V^3=infinity when r<3. This is an admissible Assumption 3 law. It shows that the third absolute moment used in the recalled elementary Lindeberg lemma is not implied by alpha>5.

For completeness, the exact cavity calculation is as follows. Delete the site's contribution and let p_0 be its visit probability under that deleted-site polymer. Then
F(w)=F(0)+log(1-p_0+p_0 exp(beta w)).
Splitting paths into visiting and nonvisiting paths proves this identity. Put p(w)=p_0 exp(beta w)/(1-p_0+p_0 exp(beta w)). Differentiation gives
F'(w)=beta p(w),
F''(w)=beta^2 p(w)(1-p(w)),
F^{(3)}(w)=beta^3 p(w)(1-p(w))(1-2p(w)).
These are bounded derivatives, but their fixed-beta uniform bound does not yield a vanishing replacement error after summing over order n^2 sites and scaling by n^{1/3}. This is a failure of that bound to establish a comparison, not a lower bound on the true error. Bounds on occupation probabilities in mixed replacement environments would be needed. An occupation sum for a SINGLE environment must not be used as though all hybrids share that environment. The infinite-third-moment example also does not refute KPZ universality; saturated derivatives or a different truncation argument could potentially handle it.

## What the selected approach has and has not achieved
Theorem 11 controls arbitrary collections of large rewards, with their actual bare-walk visit probabilities, over the entire reachable cone. It strengthens the isolated-spike result to a many-spike statement and even gives convergence of the tail-only quenched path law to the bare walk. It uses no original-polymer confinement estimate and no assumption about the negative tail.
The exact remaining gap is still the random background: prove that adding the excess (omega-u_n)_+ to min(omega,u_n) changes the centered, fixed-temperature polymer free energy by o_P(n^{1/3}), or prove an appropriate background-dependent multipoint visit bound that makes the chain expansion usable under that polymer law. Theorem 11 and Proposition 12 show that a bare-walk estimate alone cannot supply it. Even a successful perturbation estimate would leave the generic capped-model KPZ/Airy universality theorem unproved.
''')
print('Saved background obstruction and admissible infinite-third-moment construction.')
