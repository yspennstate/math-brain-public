# Deterministic checks — account01/B04 r25

These are finite arithmetic checks supporting REPORT.md; they are not independent proof certificates.

## Small-pair inherited scale

With `delta=1/64`, `b=3delta`, and coupling threshold `||W||_F^2<1/4`, use `u<=1/2`:

`eta=(b+sqrt(b^2+4u^2))/2 <=(3+sqrt(4105))/128`.

Hence

`s_*=(125-sqrt(4105))/128=0.4760134850112079...`.

The scaled spectral-window constant is

`288 sqrt(3e)/(13 s_*)=132.90390686367482...`.

The coupling-heavy first-compound constant at `Z_1=1/4` is

`sqrt(2)*[2^(3/4)e^(1/4)Gamma(1/4)]
 =11.07241079567981...`.

## Forced off-diagonal complement energy

Using `sqrt(J_2)>=1/12`, `|det B|<=5/4096`, `||adj B||<=3/64`, and `||W||_F^2<1/4`,

`||off C||_F > (1/12-3/256)/(5/4096)
              =176/3
              =58.6666666666667...`.

## Walsh stress family

Parameters:

`m=256`, `a=1/4`, `B_e=epsilon[[1,1],[1,-1]]`,

`L_e=1/(32epsilon^2)`,

`C_e=L_e(r1r1^T+r2r2^T-r3r3^T-r4r4^T)`,

`W=a[r5^T;r6^T]`, with orthonormal Walsh `r1,...,r6` having entries `+/-1/16`.

Then

`det B_e=-2epsilon^2`,
`kappa(B_e)=sqrt(2)epsilon`,
`||C_e||_F^2=4L_e^2`,
`diag C_e=0`,
`||W||_F^2=2a^2=1/8`.

Frobenius orthogonality of the Walsh spectral supports gives

`J_2=16epsilon^4 L_e^2 +(255/64)epsilon^2 a^4
    =1/64 +(255/64)epsilon^2/256
    >1/64>1/144`.

The seventh-character leaf split has four crossing singular values `L_e/2`, hence

`E_3=4(L_e/2)^6=L_e^6/16`.

Therefore the marginal-free third-compound theorem gives

`6^(4/3)E_3^(-1/6)
 =6^(4/3)2^(2/3)/L_e
 =553.8238349980446... epsilon^2`.

The scaled spectral-window theorem gives

`[288sqrt(3e)/13]/L_e
 =2024.4496600890511... epsilon^2`.

The account02/B04 r16 diffuse-range formula has `r=4`, `beta=1/64`, `sigma=L_e`, so

`2C_*/[(1-sqrt(1/16))L_e]
 =(8C_*/3)/L_e
 =(256C_*/3)epsilon^2
 =721.3244779117378... epsilon^2`,

with `C_*=8.4530212255281768747...`.

At `epsilon=1/128`, `L_e=512`:

- explicit cross-E3: `0.03380272430407989...`;
- account02/B04 diffuse-range: `0.04402615221629259...`;
- scaled spectral window: `0.12356260132379462...`;
- exact packet `J_2=0.015625949949026108...`;
- preceding reciprocal-pair certificate `18.82331388097627*(kappa^2 J_2)^(-1/8)=97.6425299381725...`.

Thus on this family the complement-Fourier certificate improves the local pair certificate by a factor about `2888.6` at `epsilon=1/128`, and the improvement diverges as `epsilon->0`.

STATUS=PASS
