# P0441: exact stationary tradeoff for one server, including setup arrivals

Label: proof for a specified M/M/1 DelayedOff model, awaiting w346. It does not solve the source's many-server question.

Assume Poisson arrivals of rate lambda>0, independent exponential service of rate mu>lambda, FCFS, and a single server. After becoming empty, it remains on for a deterministic grace period g in [0,infinity], then switches off. An arrival to an off server starts a deterministic setup of duration tau>=0. Setup is not cancelled; arrivals during setup wait and are served when setup ends. Define p=exp(-lambda g) (p=0 for g=infinity), x=lambda tau, v=mu-lambda, and rho=lambda/mu.

The stationary mean queueing wait, excluding service, is

W(g)=lambda/[mu(mu-lambda)] + tau(1+lambda tau/2) p/(1+lambda tau p).

The long-run fractions of time busy, on-idle, off, and in setup are respectively

rho, (1-rho)(1-p)/(1+xp), (1-rho)p/(1+xp), (1-rho)xp/(1+xp).

If their powers are B,I,O,U, average power is

P(g)=rho B+(1-rho) I+(1-rho)[O+xU-(1+x)I] p/(1+xp).

Thus W and P lie on an affine line as g varies (power may be constant when the bracket vanishes); all later arrivals and the busy period are included.

Proof: Use iid regenerative cycles starting when a busy period ends. The next-arrival gap A is exponential(lambda). Its expected on-idle and off durations are (1-p)/lambda and p/lambda. Setup occurs with probability p and contributes tau p expected time. After setup the initial busy-period queue is K=1+Poisson(x), whereas after a hot arrival it is K=1.

For the birth-death queue killed at zero, its expected busy duration from k is k/v. Its expected area under the queue length is

F(k)=k^2/(2v)+(lambda+mu)k/(2v^2).

The generator satisfies LF(k)=-k and F(0)=0. A justification avoiding an unbounded optional-stopping assumption is as follows: embed at jump epochs, whose increments are iid with probabilities lambda/(lambda+mu) and mu/(lambda+mu). Negative drift and bounded increments give an exponential tail for the hitting time of zero from each fixed k, by a Chernoff bound on the unconstrained walk when survival forces its position to stay positive. Queue height is at most k plus the number of jumps. This tail makes the stopped quadratic boundary term vanish and the queue area integrable; apply the stopped generator identity and let the cutoff tend to infinity. The Poisson initial queue also has all moments and exponential moments sufficiently near zero, so the same formulas can be averaged over K.

E[K]=1+x, E[K^2]=1+3x+x^2 after setup, and the expected setup queue area is tau+lambda tau^2/2. Thus the expected cycle duration is

C=mu/[lambda v] (1+xp),

and its expected queue area is

A=mu/v^2 [1+mu tau p+lambda v tau^2 p/2].

Renewal reward gives E[N]=A/C. Little's law gives response time E[N]/lambda, and subtracting 1/mu yields the displayed W. Dividing each expected state duration by C yields the power fractions and their sum one. This also verifies busy fraction rho, g=0, g=infinity, and tau=0.
