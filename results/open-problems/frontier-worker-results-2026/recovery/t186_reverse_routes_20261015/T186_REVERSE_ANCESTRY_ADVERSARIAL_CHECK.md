# Independent controls for the proposed reverse moment argument

These controls test the load-bearing mechanism in the route note; they do
not certify the full four-message random-graph transfer.

1. A genuinely stationary two-state control. Let the update be OR, take
c=2 log(2), and use the nonzero fixed point pi_0=pi_1=1/2. There is only
one strict pair 1->0. The forward matrix on reverse labels d=0,1 is
T=log(2) I: a response needs no other positive input, and its reverse
label equals the distinguished child's baseline label. The proposed
mu is constant1/4, so R=T. Direct reverse enumeration gives exactly one
causal ancestor iff the positive-input count is1. Conditional on baseline
output1, that probability is
Pr(Pois(log2)=1)/Pr(Pois(log2)>=1)=log2. Thus the independently described
ancestry process really has R as its mean and expected total
1/(1-log2). This verifies the orientation and the baseline conditioning
in a soluble stationary case.

2. An adversarial shared-subtree control. Consider W=1+2 B W', where
B is Bernoulli(2/5), W' is the continuation on ONE shared chain, and both
listed children use exactly the same W'. The mean offspring count is4/5,
so the total expectation is5. Treating the two children as independent
would describe a different process.

The route's convexity bound gives R_p=(4/5)3^(p-1). At p=6/5 this is
strictly below1: raising the positive inequality to power5 reduces it
to 3*4^5<5^5, namely3072<3125. Therefore its moment recurrence proves a
finite6/5 moment even for completely shared sibling continuations.

Direct calculation agrees. If L is the number of consecutive successes,
Pr(L=l)=(3/5)(2/5)^l and W=2^(l+1)-1. Its6/5 moment converges since
(2/5)2^(6/5)<1, equivalently (2/5)^5*2^6=2048/3125<1.
But every positive exponential moment is infinite: the individual terms
(3/5)(2/5)^l exp(s(2^(l+1)-1)) fail to tend to zero for every s>0.
This breaks a tempting exponential-moment strengthening and confirms
that the route's limited p>1 statement is the appropriate one.

3. History labels cannot be dropped. The displayed adjoint identity is
for R_H=diag(Q_A Q_d) B^transpose diag(Q_A Q_d)^(-1), on the FULL
compatible C022 type space. Summing away A before constructing the
conditioned reverse process would assert a lumpability property that
C022 explicitly does not have. The common-tree conditional expectation
representation must be proved with both histories retained. This is
still the independent review target; the soluble controls above do not
settle that general conditioning step.
