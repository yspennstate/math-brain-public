# Checks — fleet02/B20 20260924T020212Z

## Arithmetic

Using

`eps_0=(9*2^-18)^(1/4)=sqrt(3/2)/16`,

one has

`sqrt(2) eps_0=sqrt(3)/16=0.10825317547305482...`.

The finite-carrier off-diagonal floor is

`sqrt(3/16-1/2048)=sqrt(383/2048)=0.432448515721814...`,

hence

`gamma_0=sqrt(383/2048)-sqrt(3)/16=0.3241953402487592...`,

and the random-cut energy floor is

`c_0=gamma_0^2/4=(sqrt(766)-4sqrt(3))^2/16384
    =0.026275654659752182...`.

At `delta=1/64`, the fleet04/B20-r10 volume inequality plus pinned D5 gives

`5 sqrt(2e) [120/(delta^4 c_0^5)]^(1/10)
 =612.6967612912748...`.

If strong-top-four holds and `s_3>=1/64`,

`Delta_3 > sqrt((63/256)c_0)/4096
          =1.9632116237736183e-5`,

and

`3e Delta_3^(-1/3)=302.29203045238205...`.

The E2 floor in the `s_2>=1/64>s_3` branch is

`z_0=(1/4096)[(63/64)c_0-3/4096]
    =6.135907148606825e-6 >0`.

The rank-one reproduction map is

`F(E)=1919/8192+(63/128)E`,

with fixed point

`E_infty=1919/4160=0.461298076923...`,

and

`F(c_0)=0.24718547846534678... >c_0`.

The curvature-flip retained-arm floor is

`a_0^2=(1/2)[(63/64)c_0-3/4096]
       =0.012566337840346777...`,

so

`a_0=0.11209967814559851...`.

## Support/provenance check

In the r44 skeleton decomposition `A=S+T+R_0`, the off-diagonal support of `T` is confined to the `R-R` and `C-C` physical blocks. The support of `Off(S)+R_0` is confined to `H-H`, `H-R`, `H-C`, and `R-C`. They are disjoint matrix positions, so

`||Off(A)||_F^2=||Off(S)+R_0||_F^2+||Off(T)||_F^2`.

The only cancellation paid in the new cut theorem is therefore between the `R-C` component of `S` and the retained physical tail `R_0`; triangle inequality with `||R_0||_F<sqrt(3)/16` is sufficient.

The random two-colouring identity is exact: for any real symmetric zero-diagonal `B`, if each original coordinate is independently coloured left/right with probability `1/2`, then

`E ||B[L,R]||_F^2=(1/4)||B||_F^2`.

No random input coordinate is rotated in this argument.
