# account03/B03 r49 supplement — stress-test normalization correction

The main theorem and all constants in Sections 2–8 of `REPORT.md` are unchanged.

There is one harmless normalization typo in Section 9's interface stress test. For the stated choice

`U,C ~ Uniform[-1/2,1/2]`, independent, and `R=2UC`,

the exact density is

`p_R(r)=log(1/(4|r|))`, for `0<|r|<1/4`,

not `log(1/(2|r|))` on `0<|r|<1/2`.

Indeed

`p_R(r)=integral_{2|r|<=|c|<=1/2} (1/(2|c|)) dc
       =log(1/(4|r|)).`

The intended conclusion is identical: `p_R(r)->infinity` as `r->0`, so a conditional scalar density cap plus a bounded `(C,D)` joint density does not by itself imply an `L^infinity` bound for the quadratic/bilinear output. The half-Riesz theorem does not make that invalid inference.

`QFORM_B03_R49_STRESS_NORMALIZATION_CORRECTED`
