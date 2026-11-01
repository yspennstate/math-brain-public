# PROB10-05 idea checkpoint — equicorrelation + probit-product trace envelope

Runtime request is GPT-6 / maximum. Authenticated runtime model/effort telemetry is unavailable in this scheduler context, so runtime metadata is **UNVERIFIED**; no stronger claim is made.

Target is unchanged from HARD7-05: standard centered fBM with H=1/4, I_H(t)=int_0^t B_H(u)du, continuous event sup_{0<=t<=T} I_H(t)<=1, and source exponent theta_{2,1/4}. The newest HARD7-05 certified checkpoint is the lower bound theta_{2,1/4}>103/625=0.1648, upper bound 1/4, width 213/2500=0.0852. The old H(1-H) formula is not a target and Molchan v11 reports it refuted.

## New route before any checker

Keep the existing r=7/8, s=24861/25000 softened AR(1) comparator and its already-certified degree-18 quasimode. The remaining loss is the upper bound on tr(K^4).

The exact four-cycle Gaussian representation from HARD7-05 has standardized correlations

- adjacent: a = 168557580/170952323,
- opposite: b = 167065920/170952323,

with 0<b<a<1. By Slepian, the four-negative orthant probability is at most that of the equicorrelated 4-vector with all off-diagonal correlations a. Represent the latter as

G_i = sqrt(a) Z + sqrt(1-a) E_i,

with Z,E_i iid standard normal. Conditionally on Z, put U=Phi(-cZ), c=sqrt(a/(1-a)). Then the orthant probability is M_4=E[U^4].

The useful identity is obtained from V=U(1-U): by U =_d 1-U,

M_3 = (3/2)M_2-1/4,
M_4 = 2M_2-1/2 + E[V^2],
M_2 = 1/4 + asin(a)/(2 pi).

Instead of the previous generic V^2<=V/4 bound, prove the pointwise Gaussian inequality

Phi(x)Phi(-x) <= (1/4) exp(-x^2/2).

With y=x/sqrt(2), it is equivalent to erf(y)^2 >= 1-exp(-y^2). For f(y)=erf(y)^2+exp(-y^2)-1,

f'(y)=2 exp(-y^2)[(2/sqrt(pi))erf(y)-y].

The bracket starts at 0, initially increases, and has exactly one positive zero because its derivative 4/pi exp(-y^2)-1 is strictly decreasing and crosses once. Thus f rises from 0 and then decreases back to 0, so f>=0.

Consequently

E[V^2] <= (1/16) E exp(-c^2 Z^2)
          = (1/16) sqrt((1-a)/(1+a)),

and therefore

P_eq(G_0,...,G_3<0)
 <= asin(a)/pi + (1/16)sqrt((1-a)/(1+a)).

Multiplying by the exact four-cycle factor 1/(1-r^4) should reduce the trace cap from 1.10273 to about 1.09204. The intended exact target is theta*=16517/100000=0.16517. A checker is worth building only if outward rational asin/sqrt bounds certify the trace cap 273011/250000 and the inherited Temple inequalities close.

## Three materially different attacks considered

1. **Equicorrelation/probit moment route (chosen):** covariance comparison + one-factor representation + the new pointwise probit-product inequality above. This gives an analytic trace reduction before any finite arithmetic.
2. **Exact 4D orthant evaluation (deferred):** a Plackett/Childs-style quadrivariate formula would be sharper, but would require a new validated integral/special-function enclosure. It is unnecessary if the elementary bound already moves the source metric, so no numerical quadrature is promoted to proof.
3. **Continuous-time interpolation audit (parallel):** for any mesh of [0,T] with maximum gap Delta,
   sup I_H <= max_j I_H(t_j) + Delta sup|B_H|.
   Hence {max_j I_H(t_j)<=1-eta, sup|B_H|<=eta/Delta} is contained in the continuous persistence event, while the continuous event is contained in the sampled event. The current lower-exponent route uses only the latter inclusion, so it needs no unproved interpolation step. A reverse discrete-to-continuous exponent comparison would require quantitative control of the derivative/modulus term and is not asserted here.

No code or finite certificate has yet been created for this route.