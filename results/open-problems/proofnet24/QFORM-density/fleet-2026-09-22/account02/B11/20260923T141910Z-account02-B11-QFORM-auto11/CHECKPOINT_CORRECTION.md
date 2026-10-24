# Correction to the early checkpoint

The early checkpoint's T-heavy numerical constant `<179` was an arithmetic slip. The theorem and global `<232` claim are unchanged.

For `rho<=1/2`, a T-ray row of squared amplitude `w=b_j^2>1/4` has

`c_j=w(2-rho)`,
`|A_jj|=2 sqrt(1-rho) w`,

so

`c_j |A_jj| = 2(2-rho)sqrt(1-rho) w^2
             > 2*(3/2)*(1/sqrt(2))*(1/16)
             = 3/(16 sqrt(2)).`

Thus the scalar-pivot bound is

`||p_Q||_infinity < 128(16 sqrt(2)/3)^(1/4)
                  = 212.123312834...`,

not `<179`. The S-heavy bound `128(32/3)^(1/4)=231.322112924...` still dominates, so the stated uniform family bound `<232` remains valid.
