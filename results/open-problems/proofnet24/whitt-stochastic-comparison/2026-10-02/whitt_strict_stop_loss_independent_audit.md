# Independent audit of the strict stop-loss corollary

2 October 2026. The corollary in
`whitt_strict_stop_loss_corollary.md` passes independently. This is an
internal correctness audit, not a historical priority claim.

## Correct model and certified probability gap

The service laws are the mean-one two-component mixtures

    S=.2E with probability3/7, 1.6E with probability4/7,
    T=.001E with probability200/533, 1.6E with probability333/533.

The arrival rate is11/10 with two FCFS servers. On the short branch of
S, the coupling replaces .2E by .001E with probability1400/1599 and
1.6E with probability199/1599. Their conditional mean is .2E, and the
resulting unconditional short probability is200/533. The long branch
is unchanged. Thus E[T|S]=S and both means are exactly one.

I checked `whitt_two_phase_positive_checks.json`: its comparison law is
this H2 law, rather than the earlier three-class comparison. Its base
delay lower bound is about .3928726193785124 and its comparison delay
upper bound about .3903665339267248. The certified lower gap is about
.0025060854517876, exceeding1/400 as claimed. The earlier H3 gap is a
different number and is not being used here.

## Strictness at every positive service threshold

For each t>0, condition on the short branch and on

    t/1.6<E<t/.001.

This event has positive probability. The two possible replacement
values lie strictly on opposite sides of the kink of x->(x-t)+, and
both replacement probabilities are positive. Conditional Jensen is
therefore strict on this event, whether the conditional mean lies
above or below t. Elsewhere it is weakly unequal. Integrating yields

    E[(S-t)+]<E[(T-t)+] for every t>0.

The lower-endpoint equality at t=0 follows from the equal means, and is
correctly excluded from the strict-threshold assertion.

## Integrated-cdf signs

For any equal-mean nonnegative X,Y,

    E[(X-t)+]=m-t+integral_0^t F_X(u)du.

Consequently this comparison gives

    integral_0^t(F_S-F_T)du<0,
    integral_t^infinity(F_S-F_T)du>0,

for every t>0. The tail sign agrees with the orientation attributed to
Whitt's equation(2.6). These are complementary intervals with opposite
signs; the corollary now distinguishes them correctly.

## Strictly positive waiting threshold

The base queue has at most two active exponential services, each with
rate at most five. Hence its total service-completion counting-process
intensity is at most ten, even after new jobs begin service. If a tagged
arrival has0<W_S<=h, some completion must occur within h. The compensator
bound gives P(0<W_S<=h)<=10h. Also P(W_T>h)<=P(W_T>0). Therefore

    P(W_S>h)-P(W_T>h)
       >=P(W_S>0)-P(W_T>0)-10h.

At h=1/100000, the certified gap>1/400 yields

    P(W_S>h)-P(W_T>h)>1/400-1/10000=3/1250.

Final verdict: the strict conditional-Jensen argument, model binding,
cdf signs, and positive waiting-threshold bound are correct. The
corollary refutes the strengthened service hypothesis's usual
stochastic waiting conclusion for this explicit pair; it does not
settle a mean waiting-time conjecture.
