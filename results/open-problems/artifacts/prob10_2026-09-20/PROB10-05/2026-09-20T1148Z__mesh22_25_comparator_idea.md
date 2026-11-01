Runtime request: GPT-6 / maximum. Authenticated scheduler model/effort telemetry is unavailable in this run, so runtime model/effort is **UNVERIFIED**. No scheduler setting is changed by this text.

# PROB10-05 idea checkpoint — redesign the Lamperti mesh before code

Frozen source model: centered standard fractional Brownian motion with H=1/4,
`I(t)=int_0^t B_{1/4}(u)du`, and the continuous one-sided event. The exact source target remains OPEN. Molchan arXiv:2509.10265v11 (4 July 2026) is prior art: it supplies the existence/equality framework used by this track and refutes the obsolete general formula `theta_{2,H}=H(1-H)`. No part of that refutation is claimed here.

Incoming strongest self-certified repository candidate: `theta_{2,1/4}>42971/250000=0.171884`, from the degree-56 finite-polynomial Perron quasimode report. Published/source baseline remains separately `1/8 <= theta_{2,1/4} <= 1/4`; independent validation is still absent.

This iteration deliberately changes the main mechanism rather than merely increasing polynomial degree.

## Attack A — new Lamperti mesh/comparator (main route)

Take

`r=22/25`, `c=936901/1000000`, and `s=2c/(1+r)=936901/940000`.

The exact sampled Lamperti covariance at `u=e^{-tau/4}` is

`R(u)=(-2u^10+5u^6+5u^4+2(1-u^4)^(5/2)-2)/(6u^5)`.

The numerical reconnaissance only (not theorem evidence) indicates that `R(r^2)/r` is the active lag and is just below `c`; the new mesh may improve the spectral-rate quotient enough to beat the r=7/8 certificate.

The intended all-lag proof is exact and short. For k=1,2 isolate the radical and square with sign checks. For k>=3 use Taylor with signed remainder:

`(1-z)^(5/2) <= 1-(5/2)z+(15/8)z^2`, 0<=z<=1,

which implies

`R(u) <= (5/6)u+(5/8)u^3-(1/3)u^5`.

Hence

`R(r^k)/r^(k-1) <= r[5/6+(5/8)r^(2k)-(1/3)r^(4k)]`.

For k>=3 the bracket decreases with k because its derivative in q=r^(2k) is `5/8-(2/3)q>0` on `q<=r^6`; it is therefore enough to certify the k=3 rational endpoint below c. This gives continuous-source validity through the same one-way inclusion `continuous survival subset grid survival`; no reverse interpolation is asserted.

For the operator step, first reuse the already frozen degree-56 polynomial witness but recompute its Rayleigh quotient and residual for the NEW `(r,s)`. This is a new operator, so old spectral numbers are not imported. Bound the new fourth trace directly by the exact Gaussian four-cycle/HGR argument at the new `(r,s)`, then apply a trace separation plus Kato-Temple contradiction. A fresh multimode certificate is optional, not assumed.

## Attack B — continuous reverse interpolation with a derivative margin

For an upper bound on theta one ultimately needs the reverse direction. The Lamperti process is C^1 because `I'(t)=B_{1/4}(t)` and B has continuous paths. On each mesh interval, the deterministic implication

`max endpoints <= -eta` and `sup |X'| <= eta/delta  => X<=0 on the interval`

is valid. The unresolved probabilistic step is exponential-scale control of the derivative event conditional on long grid survival. An unconditional union bound is not enough because persistence itself is exponentially small in Lamperti time. This attack will be recorded as auxiliary unless such a conditional estimate is proved.

## Attack C — new-r spectral-tail sharpening

If the trace-only separation is the bottleneck, build a new-r Hermite min-max certificate for several non-Perron modes and subtract their fourth mass before Temple. This is materially different from Attack A's geometric comparator redesign and from Attack B's continuous interpolation. It is not to be counted as source progress unless every mode and tail estimate is certified for the new operator.

Primary metric: rigorous repository candidate width with U=1/4. Incoming width is `0.078116`. Unknown endpoints remain UNKNOWN. Numerical quadrature, if used to choose constants, is discovery only; theorem decisions must be exact/outward-certified.
