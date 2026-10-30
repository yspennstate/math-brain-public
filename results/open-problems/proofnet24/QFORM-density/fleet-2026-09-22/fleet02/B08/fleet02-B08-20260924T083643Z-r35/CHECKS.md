# fleet02/B08 r35 deterministic checks

All quantities below are algebraic identities or direct arithmetic checks; they are not numerical evidence for the conjecture.

- `C3=6^(4/3)=10.902723556992836...`.
- Retained benchmark `C*=197.7780678260685`, so
  `theta=C3/C*=0.05512604949999305...`.
- Row-aware cut balance: `E||G_S-I/2||_F^2<=1/64`; Markov at radius `1/5` gives failure at most `25/64`, hence balance success at least `39/64`.
- Cross-row event at threshold `Z>=R^2/6` has probability at least `2/5` from `E Z=R^2/2` and `Z<=R^2`.
- Joint probability lower bound: `39/64+2/5-1=3/320>0`.
- Balanced Gram floor: `g=3/10`; new cancellation floor
  `eta_row=g-theta=0.24487395050000695...`.
- Inherited actual row gate: `gamma=0.0006247538095703261...`; if the row gate is off-diagonal then the selected cross-star satisfies
  `||z||>gamma/sqrt(6) L=0.0002550546747178715... L`.
- After deleting the selected row,
  `g_del=3/10-1/48=67/240`, hence the selected top-three crossing still has
  `s3(B0_minus)>=sqrt((67/240)(3/10)) L=sqrt(67/800)L`
  with `c0=sqrt(67/800)=0.28939592256975566...`.
- Set `sigma=c0/2=0.14469796128487783...`. The partner exterior-algebra inequality plus the unpaid third-compound gate gives the absolute alignment tube
  `dist(z,R2(D)) < delta L`,
  `delta=theta^3/sigma^2=(3200/67)theta^3=0.008001027955285274...`,
  unless `s2(D)<sigma L`.
- If `s2(D)<sigma L`, the two-dimensional min-max argument gives
  `s2((A-A3)[S\{k},T])>=(c0-sigma)L=sigma L`.

## Walsh six-frame cancellation stress family

For `m=2^q>=1024`, choose Walsh characters `u_1,u_2,u_3` and a sign character `chi`, with the six normalized characters

`u_1,u_2,u_3,v_1=chi*u_1,v_2=chi*u_2,v_3=chi*u_3`

all distinct. They are exactly orthonormal. For the `chi=+1` / `chi=-1` half-cut:

- `U_S^T U_S=U_T^T U_T=I_3/2`.
- The selected top-three crossing has singular values exactly `(L/2,L/2,L/2)`.
- Each `v_j v_j^T` crossing is exactly the negative of the corresponding `u_j u_j^T` crossing, so the literal crossing of the six-frame sum is exactly zero.
- Adding a separate coordinate `z` with diagonal coefficient `L/2` gives spectrum exactly `{L,L,L,L,L,L,L/2,0,...}`.
- Every light-light physical `2x2` block has operator norm at most `12L/m`; every `z`-light block has least singular value `6L/m`. Thus for `m>=1024` every physical `2x2` principal block has least singular value `<L/64`.
- The rank-six frame leverage is `6/m<=1/2`, so fixed-source generalized Theorem F yields
  `||p_Q||_infinity <= [4*6/(6-2)] L^(-1)=6/L`, with a `C_0` density.

`QFORM_B08_R35_CHECK_PASS`
