# Direct application of completed partner fleet03/B01 r15

This supplement records the named-partner result applied to the new small-diagonal mechanism, rather than merely citing it.

Partner source: `yspennstate/math-open-problems@76fd4f9ccae2e422498fec6d4156bfd64775c8e4`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T163129Z-r15/REPORT.md`, Lemma 2.2. It proves, for every cap-one probability density and every real `c`,

`E |Z^2-c|^(-1/4) <=4`.                                     (P.1)

In the small-diagonal branch of this run's `REPORT.md`, after exact near-identity factorization and conditioning on the third physical coordinate, equation (5.13) gives

`p_Q(t) <= |K|^(-1)[16/3 +(32/15) E log_+(|K|/|t-r(Z)|)]`,

where `r(Z)=s(Z-z_0)^2+r_0`, `|s|=1/Delta`, and `L=|K|/|s|=|K|Delta<=6A^3`, with `A=|a|>=a_0=sqrt(63/128)` and `|K|>=A`.

Use the elementary pointwise inequality

`log_+ z <= (4/e) z^(1/4)` for `z>0`.                       (P.2)

Then (P.1), after translating `Z`, gives

`E log_+(|K|/|t-r(Z)|)`
` <=(4/e)L^(1/4) E |(Z-z_0)^2+c|^(-1/4)`
` <=(16/e)L^(1/4).`                                         (P.3)

Therefore the named-partner theorem alone already yields the uniform small-diagonal bound

`p_Q(t)`
` <= (16/3)A^(-1)
`    +(32/15)(16/e)6^(1/4) A^(-1/4)`
` <=29.076`,                                                (P.4)

where the last inequality uses `A>=a_0` and both terms decrease in `A`.

The new logarithmic averaging Lemma 4.1 in the main report sharpens `29.076` to `<25.241`, but (P.3)-(P.4) show that the completed compatible fleet03/B01 result is directly consumed in the exact new proof mechanism. No independence after rotation or unsupported conditional density cap is introduced.

This supplement does not change the theorem constant `216`, which is dominated by the arbitrary-affine nonzero-diagonal branch supplied by the later rank-two fusion theorem. Full QFORM remains open.
