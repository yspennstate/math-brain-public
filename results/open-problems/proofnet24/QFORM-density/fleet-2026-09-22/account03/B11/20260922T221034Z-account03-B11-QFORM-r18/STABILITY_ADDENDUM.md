# Addendum: disjoint Pluecker mass is the volume-sampled complement determinant

Retain the notation of `REPORT.md`: `R^T R=I_3`, physical rows `r_i`, and `w_B=det(R_B)^2`, so `sum_B w_B=1`. For every basis triple `B`, define the complement covariance

`S_B = sum_{j notin B} r_j r_j^T = I_3 - sum_{i in B} r_i r_i^T`.

By Cauchy--Binet applied to the row matrix with the three rows in `B` deleted,

`det S_B = sum_{T subset B^c, |T|=3} w_T`.

Therefore the ordered disjoint Pluecker mass has the exact identity

`boxed: D0 = sum_B w_B det S_B`.                                  (A.1)

Equivalently, if `B` is sampled from the rank-three volume law `P(B)=w_B`, then

`D0 = E_B det S_B`.                                                (A.2)

This supplies a quantitative stability bridge beyond the exact `D0=0` endpoint. There exists at least one basis triple `B` such that

`det S_B <= D0`.                                                    (A.3)

Since `0 <= S_B <= I_3`, its smallest eigenvalue obeys

`lambda_min(S_B) <= (det S_B)^(1/3) <= D0^(1/3)`.                  (A.4)

Let `e` be a unit eigenvector for that eigenvalue. Then

`sum_{j notin B} <r_j,e>^2 <= D0^(1/3)`,                           (A.5)

whereas Parseval gives

`sum_{i in B} <r_i,e>^2 >= 1-D0^(1/3)`.                            (A.6)

Thus small positive disjoint-basis mass forces **all but three original spectral rows to have small aggregate transverse energy to one physical two-plane**, while the selected three rows carry almost the entire missing transverse direction. At `D0=0`, (A.5) is exact and recovers the plane argument in `REPORT.md`; the indefinite null-cone intersection then collapses the complement to at most two projective null rays.

This does not by itself prove a density bound uniform as `D0 ->0`: small spectral-row transverse coefficients cannot simply be discarded because the input variables have no moment or support bound. But it replaces the vague stability problem by a precise quantitative target. A correction-safe continuation must convert (A.5)--(A.6), together with the null relation `r_i^T Lambda r_i=0`, into either an already-paid physical-pair/ridge certificate or an exact grouped-bank transducer before inversion.

The identity (A.1) is deterministic and uses no probability law for the inputs; the only probability is the auxiliary volume-sampling distribution on basis triples.
