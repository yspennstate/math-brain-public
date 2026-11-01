# r29 check and notation clarification

The mathematics in `REPORT.md` uses the final Fourier variable `t`.  In equation (3.8), the compact strings `2tdg_0 t U` and `2tdt U g_j` contain a duplicated typography token.  The intended and used arguments are, respectively,

`2 t d g_0 U`

and

`2 t d U g_j`.

All subsequent scaling, (3.11), and constants use these corrected arguments.  No theorem statement or coefficient changes.

Deterministic checks:

1. With `theta^2=beta^2+m^2`, `h=beta v+m q`, `g=m v-beta q`, and `v perp q`, one has `h perp g`, `||h||=||g||=theta`, and `beta h+m g=theta^2 v`.
2. At `h_r=0`, `h_r^2+g_r^2=theta^2(v_r^2+q_r^2)` gives `|g_r|=theta sqrt(ell_r)`.
3. The characteristic envelope constant is
   `K=2 pi sqrt(L)/[||h|| sqrt(|A d g_0|)]`.
4. `int_R min(1,K^2/t^2)dt=4K`.
5. `int_R |t|^(-1/2)min(1,K^2/t^2)dt=(16/3)sqrt(K)`.
6. Under `L<=sqrt(e)`, `y^2>1/2`, `ell_r>1/2`, and `(rho^2/|a|)|sigma|>=s_3(A)^2`, the target-scale constants are
   - `K < 2^(7/4) pi e^(1/4)/s_3 = 13.568317125581782.../s_3`;
   - `int |phi|^2 < 54.27326850232713.../s_3`;
   - `||p||_2^2 < 8.637858959899031.../s_3`;
   - collision coefficient `<17.27571791979806.../s_3`;
   - weighted half-Riesz time coefficient `<19.64543821560657.../sqrt(s_3)`.

Check status: `QFORM_B03_R29_CHECK_PASS`.
