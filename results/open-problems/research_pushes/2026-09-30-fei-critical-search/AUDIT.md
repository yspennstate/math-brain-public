# Independent finite-certificate audit

30 September 2026. Full FEI remains OPEN.

An independent mathematical/computational reviewer found no mathematical error in the six finite certificates or orbit formulas (1)–(3) of REPORT.md.

- All six certificates reran sequentially in 7.24 seconds. Every mathematical JSON field matched exactly; only timings differed.
- The reviewer independently rebuilt all physical truth tables and Walsh transforms for the 15- and 16-variable candidates. Every coefficient, orbit multiplicity, restriction coefficient and coordinate influence matched.
- Child normalization is correct: normalized child coefficients are `(u+v)/2^n` and `(u-v)/2^n`. Their unnormalized `(n-1)`-variable coefficients are `(u+v)/2` and `(u-v)/2`, so using denominator `2^(2n)` for squared `(u+v)` and `(u-v)` is correct.
- The integer logarithm enclosure is sound: downward-rounded series terms, 90 rounding-error units, the rational tail ceiling and positive interval division have the correct outward directions.
- Influence is exactly `di/2^(2n)`, total influence is `n*di/2^(2n)`, and the entropy-decrement ratio correctly includes the factor one half averaging the children.
- Within-block and whole-block permutations act transitively on coordinates, making the certified coordinate ratio equal to the minimum coordinate ratio.

## Scope

This audit certifies the six explicit Boolean candidates and the stated finite arithmetic, not search optimality, floating-point candidate ordering, exploratory tower limits, publication priority or full FEI. It is executable mathematical verification, not a formal proof-assistant certificate.

The independent reviewer audited the supplied local artifacts and did not independently check remote commit identity. The coordinating researcher separately fetched all 17 prose/data files at commit `8253db1b064dfc5455577a083402866a3f694fb6` and all four code files at commit `60d3a823b0f55ab46df5916d0cbed87208c187a6`, verifying exact content equality. Code remains in draft PR [#13](https://github.com/yspennstate/math-open-problems/pull/13).
