# Independent reconstruction: compatible-root aggregation

Verdict: HOLDS at the complete stated scope of
A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION@1, statement hash
e65558de09e5ed30b847048af90eae15a5e4da12d8651ac3f3684213c8060271,
using the explicitly established threshold Theorem A baseline. No repair.
This review does not independently reprove the threshold paper's full chain.

Read CENTRAL_PAYMENT.md and CLAIMS.json from A008's
20261023T024024Z-account03-A008-gate-label-compression run; reread original
forests.tex queue definitions/normalizer and the threshold paper's Theorem A
(Creg<8.937<9). The local threshold text is cp1252; no rewritten source is used.

I reconstructed the event sum from raw conditioned Bernoulli roots. Put
z=pi/N and D=(1+z)^N-1. Exactly root e, with all other roots absent, has
mass z/D. Its zero-child specified-subset visit has mass
prod(theta)/[2s(s+1)Z_s]. Distinct compatible prime names specify distinct
runs, so their probabilities sum BEFORE logarithms. For block degrees a,b,
the number of compatible roots is
binom(2k-a,k-a)binom(2k-b,k-b). Dividing by binom(2k,k)^2 gives exactly
binom(k,a)/binom(2k,a) times binom(k,b)/binom(2k,b). The binomial bounds in
the source yield at least(2e)^-(a+b), without choosing lambda after exposure.

For good A, theta_d>=(d/W)^(6/5), Z_d<=(6e)^d and D<=2pi give
Q_good>= (d/W)^(6d/5)/[4d(d+1)(12e^2)^d]. Since
2+log[d(d+1)]<=4d and 12e^2<128, the cost is at most
(6/5)dlog(W/d)+11d. These estimates are uniform over arbitrary fixed full
orders; they do not require the event probabilities themselves to be symmetric.

For bad A, the fixed first-half and last-half primes are DISJOINT and each
owns a nonempty subset. Their two-root, zero-child event includes z^2/D and
the TWO visit factors, giving cost<=1+13m<26d. It is an actual partition
forest even under the source's minimal-source-SCC convention. Good and bad
outputs are disjoint, as are the underlying root events. Hence Q_sel is a
subprobability of the SAME original sampler, and Q_*>=Q_sel.

For separately block-exchangeable P, the pointwise good-set rank bound is
paid by log binom(m,a)+log binom(m,b), whose expectation is the orbit part
of H(P). Adding the bad cost gives C_sel<=6H(P)/5+37E|A|. This entropy
comparison alone does NOT prove universal FEI; its coefficient exceeds one.

Independently expanding F=2h_X h_Y-1 gives sector masses
(2q^2-1)^2, q^2v_g, q^2v_g, v_g^2/4. The mean number of active block spectra
is2qv_g, so the coefficient of H(g)-h2(v_g) is2q, exactly as in the source.
Thus H(F)<=2+2qH(g)<=11I(F), using I(g)>=1, I(F)=2qI(g)>=1 and the
established H(g)<9I(g). Hence251I/5 follows with no entropy absorption.
The optional261I/5 wrapper is valid; in this family h2(v)<=1<=I even gives
the stronger full cost256I/5. These are FULL-wrapper bounds, distinct from
the unchanged NONEMPTY251I/5 source claim.

The independently written code/check.py imports no A008 helper. It checks
every physical Fourier coefficient for k=1,2,3 against tensor coefficients,
and direct character sums for k=1,2. For k=1,2 every nonempty output is
enumerated; actual prime lists, rotated fixed physical orders, outward
32-bit fifth-root intervals, raw root factors and subset normalizers certify
the good/bad event bounds and total subprobability. Exact arithmetic and
counts are in out/checks.json. The all-k proof is the reconstruction above,
not extrapolation from those cases.

Conflict disclosure: A015 supplied the motivating earlier dimension-budget
obstruction and rare-tail certificate, but neither is a dependency of A008's
central proof. I made no substantive repair and am not accepting my own
96I theorem through this review. The review covers A008's precise original
queue code and its declared established threshold dependency; no nonsymmetric
or arbitrary-prime existence statement is accepted.
