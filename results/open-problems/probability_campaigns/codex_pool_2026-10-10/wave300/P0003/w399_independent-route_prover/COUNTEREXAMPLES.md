# Exact counterexamples to two shortcuts

## Multiplying obstacle avoidance without conditioning

Take a single honeycomb face, the six-cycle 0-1-2-3-4-5-0, endpoints 0 and 3. The two simple endpoint paths both have three edges, hence probability 1/2 each for every x>0, including x_c.

For A={1}, B={5}, each individual avoidance probability is 1/2, while simultaneous avoidance is zero; the product 1/4 is wrong. For A={1}, C={2}, simultaneous avoidance has probability 1/2, again different from product 1/4, now with the opposite sign. Therefore avoidance events have neither a universal independence relation nor a universal sign of association, even on a finite honeycomb subgraph.

The correct sequential identity, when its denominator is positive, is

P(avoid A union B)= [Z_(G minus A)/Z_G] [Z_(G minus (A union B))/Z_(G minus A)].

It follows by cancellation and conditions the second factor in the domain already restricted by A. On the cycle with A={1}, B={5}, the conditional second factor is zero, not 1/2.

## Hausdorff trace convergence is weaker than convergence of oriented curves

For epsilon>0 small, connect in order the vertices

(0,0), (3/4,0), (3/4,epsilon), (1/4,epsilon), (1/4,2 epsilon), (19/20,2 epsilon), (19/20,epsilon/2), (1,0).

This is a simple polygonal path in the closed strip [0,1] x [-1,1], from a=(0,0) to b=(1,0), with all intermediate points away from the strip's vertical boundary. Its trace has Hausdorff distance <=2 epsilon from the straight segment [a,b]. Its oriented curve has Fréchet distance >=1/4 from that segment for every epsilon. In fact, along the path the x-coordinate visits 3/4 and then 1/4. At uniform matching error rho a forward traversal of the segment must have coordinates s_1<=s_2 satisfying 3/4-rho<=s_1<=s_2<=1/4+rho. Consequently rho>=1/4, for every pair of increasing reparametrizations.

Parametrize the eight vertices at fixed successive times. As epsilon->0 these simple paths converge uniformly to a curve that retraces [1/4,3/4]. Its trace is the simple segment, but the curve is not injective. Therefore even a simple limiting trace does not itself establish simple-curve support or convergence in the curve metric. A probabilistic bound preventing macroscopic retracing is an additional obligation for P0003.

This is a deterministic topology obstruction, not a probabilistic counterexample to the SAW conjecture. No claim is made that these curves are typical critical SAWs.
