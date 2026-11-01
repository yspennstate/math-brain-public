# One fresh control: pay occupation without an ownership tail

All logarithms are base two. Set gamma=6/5. This is a proof of a conditional
reference-transfer bound, not a proof of FEI. The accepted A007 distributed-lift
interface and its same-posterior signed ledger are the premises.

Fix ANY original actual partition forest rho for a nonempty selected data set T.
Write s=|T|, k=|V|, s_l>=1 for owned sizes, kappa_l=|R_l intersect T|.
Thus s_l<=kappa_l<=s and sum_l s_l=s. Neither private leaves nor bounded read,
equal root rarities, or bounded ownership entropy is assumed. Keep the original
posterior eta_T, original gate weights lambda, and all original root rarities pi.
Let 0<beta<=1 be one globally fixed scaling, feasible for the fresh common
control: beta sum_l lambda_l<=1. Old packing constraints remain valid after
scaling. Constants below do not depend on dimension or the number of gates.

For one selected fresh control the rank-stripped occupation sum is

    Z_rho=A sum_l t_l,
    A=prod_l (kappa_l/(kappa_l+1))^(gamma s_l),
    t_l=[(s_l+1)^(s_l+1)/(s_l^s_l (kappa_l+1))]^gamma.

Since log(1+x)<=x, -log A<=gamma log(e) sum_l s_l/kappa_l
<=gamma k log(e). Bernoulli gives
(1+1/s_l)^(s_l+1)>=1+(s_l+1)/s_l>1+1/kappa_l;
consequently t_l>=(s_l/kappa_l)^gamma. Also
sum_l s_l/kappa_l>=sum_l s_l/s=1. Power-mean convexity now gives

    sum_l t_l>=k^(1-gamma),
    -log Z_rho<=gamma k log(e)+(gamma-1)log k.                 (1)

Every denominator is positive: k>=1, s_l>=1, kappa_l>=s_l.
No probability or spectral hypothesis is used before this point; (1) is a
deterministic statement for every permitted partition record.

The exact A007 one-control root multiplier is 1 if c=1. If c>=2 it is
(c-1)! times an occupation-tilted mean of pi_a divided by prod_a pi_a.
For each a, pi_a/prod_b pi_b=1/prod_(b!=a)pi_b>=1 since 0<pi_b<=1.
Thus this root multiplier is at least one. This uses the ACTUAL tree-component
root of each gate, rather than a source-SCC surrogate. Hence the exact joint
coefficient satisfies

    -log G_rho(1)<=k log(1/beta)+gamma k log(e)
                                      +(gamma-1)log k.       (2)

The root/factorial credit stays in G; bounding it below by one deliberately
forgoes usable credit, never creates credit. In particular no independence of
root rarity and occupation is asserted.

Let v=Var(g), P_g(T)=ghat(T)^2, I_g=sum_T P_g(T)|T|, and
m_T=E_eta k. Set L0(T)=E_eta beta^k, J1(T)=E_eta G_rho(1).
Concavity of log, applied under THIS SAME eta_T, yields

    -log L0(T)<=log(1/beta)m_T,
    -log J1(T)<=[log(1/beta)+gamma log(e)+gamma-1]m_T,          (3)

where log k<=k is sufficient. Let D=prod(1+lambda_l pi_l)-1,
D'=prod(1+beta lambda_l pi_l/2)-1. The old table is nonempty with positive
weights and rarities, so D,D'>0. Expanding the finite product into nonempty
subsets proves D'<=beta D/2, since (beta/2)^j<=beta/2 for j>=1.
The complete one-control distributed correction in A007's notation is

    Psi=(v/2)log(2D'/D)
            -(1/4)sum_(T!=empty)P_g(T)[log L0(T)+log J1(T)].

Its exact normalization term is nonpositive, and can be retained more sharply:

    Psi <= (v/2)log beta
             +[log(1/beta)/2+3 log(e)/10+1/20] I_g.           (4)

Indeed m_T<=|T| pointwise; every coefficient used in replacing m_T by |T|
is nonnegative. In units of activated DATA influence I_data=I_g/2,

    Psi <= (v/2)log beta
             +[log(1/beta)+3 log(e)/5+1/10] I_data.          (5)

In particular beta=1 gives surcharge at most
(3 log(e)/5+1/10) I_data < 1 I_data: log(e)<3/2, so this coefficient<1.
For an explicit rational check of that last estimate, the exponential series
and its factorial tail give e<8/3+5/96=87/32<11/4, while (11/4)^2<8.
Thus log(e)<3/2 without a floating-point comparison.
This does not bound the whole activated residual or the original base cost.
The inherited (1/2)R_g, physical rank-payment terms, fresh-control-only sector
and all external entropy/reference overhead remain in the source transfer.
Both empty-control and nonempty-control sectors with T!=empty ARE included
in (4); the control-only sector T=empty IS NOT silently identified with Psi.

## The scale is paid only for extra used gates

The signed normalization improves the interpretation of (4). Define, under
the SAME old posterior and original unnormalized nonempty spectral masses,

    M=sum_(T!=empty)P_g(T) E_eta(k-1).

This is not conditional on a gate being activated, and no new posterior is
chosen. Since 1<=k<=|T|, 0<=M<=I_g-v.
For k=1 the whole selected T is owned by that gate, so kappa=s and Z=1
EXACTLY. Thus G=beta. For k>=2, k<=2(k-1) and log k<=k-1, giving

    -log Z <= [2 gamma log(e)+gamma-1](k-1).

Retaining the same >=1 root credit and using Jensen as before proves

    Psi <= [log(1/beta)/2+3 log(e)/5+1/20] M                  (6)
         <= [log(1/beta)/2+3 log(e)/5+1/20](I_g-v).

The two beta*k bills in the two data sectors produce (log(1/beta)/2)E k;
the SAME normalization subtracts (log(1/beta)/2)v. Their difference is
exactly the displayed extra-gate charge. There is no independent marginal
rebate and no reused influence. Bounds (4) and (6) are alternative valid
upper bounds on the same correction, so either may be used but their credits
must not be added. For beta=1 the coefficient in (6) is <19/20, by
log(e)<3/2. This is a centered-influence bound for this transfer correction,
not for the entire entropy of the Boolean function.

## What this closes and what it does not

For one control there is no need for a uniform ownership-entropy tail, even on
shared or leafless incidence: its exact joint occupation/root surcharge is
paid by (4) or (6). The sharper remaining scaling price is explicit
(log(1/beta)/2)M, with M the expected EXCESS number of used gates.
The signed normalization rebate (v/2)log beta stays visible. Feasibility
allows beta=min(1,1/sum lambda). A sum-lambda-independent estimate does not
follow; already disjoint singleton primes at lambda=1 have sum lambda=n.
One may instead choose a normalized original reference, but its inherited R_g
can then grow. This is precisely the global reference-selection tradeoff,
not a counterexample to the infimum over all representations or to FEI.

The statement applies to any Boolean gate cover for which the original
partition posterior and accepted distributed transfer are defined. No claim
about an arbitrary non-Boolean spectral law or a repeatedly renewed reference
is made. Iterating (5) for r controls without tracking the same budget produces
an r factor and is NOT an all-r or universal FEI proof.
