# Numerical correction to `SHARPENING.md`

The symbolic inequalities in `SHARPENING.md` are unchanged. Two decimal evaluations there were inadvertently rounded from a different trial threshold and are too small. They must not be used.

With

`Z_0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864`,

`delta=h/1024`,

and the sharpened physical-heavy threshold `2/7`, the exact coefficient is

`c_21=Z_0/(21*1024^2)=0.03881341390130683`.

Therefore the marginal-free E3 branch coefficient is

`C_E3 c_21^(-1/6)=18.131306618412538`,

so the valid displayed bound is

`boxed: ||p_Q||_infinity <18.131306619 h^(-1) <1.560e7.`

For the pinned e5 D' subbranch (`max row E3 marginal<=2/3`), the coefficient is

`9sqrt(3e)c_21^(-1/6)=44.169254632865744`,

so the valid displayed bound is

`boxed: ||p_Q||_infinity <44.169254633 h^(-1) <3.800e7.`

The nineteen-coordinate core coefficient in `SHARPENING.md`, `2039.875741829 h^(-1)`, and the structural conclusion

`rank R_L<=34`, `|E_L|_max<(19/512)h=4.313900492e-8`

were already correct.

This correction supersedes only the two erroneous numerical decimal bounds in `SHARPENING.md`; the exterior-algebra proof and all symbolic constants remain valid. Full QFORM remains open.
