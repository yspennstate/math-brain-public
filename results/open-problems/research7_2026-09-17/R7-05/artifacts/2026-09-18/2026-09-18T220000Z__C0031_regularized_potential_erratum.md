Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# Erratum to `2026-09-18T215700Z__C0031_regularized_potential_defect.md`

Exact-SHA readback of creation commit `d6b1b93c8118721471baf21c4a7bca03de1a52b1` exposed one unfinished notation placeholder in Section 4:

`E_n(z;J) := sum_{j>=J} 2^{-j}??`

That line is **withdrawn**. It is replaced by the following exact logarithmic-coordinate formulation.

Let `eta=e^{-J}` and put

`F_{n,z}(t)=nu_{n,z}([0,t])`.

For the dangerous part `0<t<=eta`, the substitution `t=e^{-u}` in the exact defect identity

`R_{n,eta}(z)=int_0^infinity F_{n,z}(t) eta^2/[t(t^2+eta^2)]dt`

gives

`R_{n,eta}^{low}(z)
 = int_J^infinity F_{n,z}(e^{-u})/[1+e^{-2(u-J)}] du`.

Since `u>=J`, the weight lies in `[1/2,1]`, and therefore

`(1/2) int_J^infinity F_{n,z}(e^{-u})du
 <= R_{n,eta}^{low}(z)
 <= int_J^infinity F_{n,z}(e^{-u})du`.                            (E.1)

A natural dyadic/logarithmic discrete energy is consequently

`E_n(z;J) := sum_{m=ceil(J)}^infinity F_{n,z}(e^{-m})`.             (E.2)

By monotonicity of `u -> F_{n,z}(e^{-u})`, (E.2) is comparable, up to the first unit interval, with the integral in (E.1). No factor `2^{-m}` belongs here.

All other statements and proofs in the parent artifact are unchanged. In particular, the exact Tonelli identity (2.1), the Frobenius-Lipschitz smoothing lemma (3.1), and the fixed-`eta` smoothing conclusion (3.2) are unaffected.
