# account02/B12 r13 early checkpoint

Status: supporting theorem in progress; full QFORM remains OPEN.

Let `M in R^(p x m)` have full column rank, `g=s_m(M)>0`, and let `N` be arbitrary. Put

`G=M^T M`, `U=M G^(-1/2)`, `Pi=UU^T`,

`K=G^(-1/2) M^T N G^(-1/2)`, `Z=(I-Pi)N`.

Then

`M+N = U(I+K)G^(1/2)+Z`, with orthogonal output ranges, so

`(M+N)^T(M+N)=G^(1/2)(I+K)^T(I+K)G^(1/2)+Z^T Z`.

For integers `r,s>=0`, `r+s<=m-1`, PSD Weyl plus the singular-value product inequality gives

`boxed: s_(m-r-s)(M+N)^2 >= g^2 s_(m-r)(I+K)^2 + s_(m-s)(Z)^2.`

This spends bad dimensions separately in the in-range relative action and the transverse action. After any coefficient tail `E` with `||E||op<=delta`, subtract only `delta` from the resulting singular-value floor.

Strict family for the five-mode branch: `m=7,p=14`,

`M=[2 I_7;0]`, `K_L=diag(-1,L,L,L,L,L,L)`, `N_L=[2K_L; I_7]`.

Then `K=K_L`, `Z=[0;I_7]`, so with `r=s=1`,

`s_5(M+N_L)>=sqrt(4(1+L)^2+1)` (in fact equality for the fifth singular value).

For `L>=1`, the account03/B12 r52 principal-angle five-mode certificate is only `2/sqrt(4L^2+1) -> 0`, because the first six canonical correlations tend to one. Thus near-alignment of packet and carrier ranges is not itself destructive when a transverse floor and non-antipodal relative action coexist.

The final report will apply the pinned `e5f71d79eff325201dd0274053d20268ce65b837` D5 theorem to the actual original-coordinate cross block after an arbitrary dense symmetric tail.
