SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T16:09:25.414606Z.
attacking: the heavy near-null nonzero-pivot two-sheet bridge; determine exactly why the successful null slice-Fresnel/BL argument fails when the pivot is nonzero, while retaining original-coordinate product structure.

# Early checkpoint — heavy-row leverage is the exact direct-Fresnel obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T160925Z-account02-B05-QFORM-d5159a85`.
Status: substantive partial calculation; full QFORM remains OPEN.

Take an exact-rank-three active form `A=RMR^T`, `R^TR=I_3`, with a heavy physical row `r_0=sqrt(c)e_1`, `c>1/2`. In the near-null normal form

```
M = [[eta,b,0],[b,alpha,delta],[0,delta,gamma]],
```

write the residual rows as `(u_j,v_j,w_j)`, `sum u_j^2=1-c=:rho`, and `u=sqrt(rho) xi`. With `S=sqrt(c)X_0+sqrt(rho)T`, `V=v.X`, `W=w.X`, the new term relative to the already-paid null endpoint is exactly `eta S^2`.

A direct attempt to Fresnel-linearise all three active quadratic directions has a rigid geometric obstruction. If the three linear-form coefficient columns are replaced by ANY invertible deterministic change of basis `RT`, then their Gram matrix is `G=T^T T`, and the normalised Brascamp--Lieb leverage of original row `i` is

```
(r_i T) G^{-1} (r_i T)^T = ||r_i||_2^2.
```

Thus the heavy row keeps leverage exactly `c>1/2` under every shear/completion of the active coefficient basis. The product Fourier/BL step would assign that row exponent `c`, hence would require a law-uniform bound on

```
int |fhat_0(s)|^(1/c) ds,
```

where `1/c<2`. The newest-Claude L^p theorem applies only for `p>=2`, and the sub-2 extension is in fact false for cap-one densities.

For the false extension, let

```
E_N = union_{k=1}^N [2^k, 2^k+1/N],  f_N=1_{E_N}.
```

Then `0<=f_N<=1` and `int f_N=1`. Writing

```
fhat_N(xi)=a_N(xi) D_N(xi),
a_N(xi)=int_0^(1/N) exp(-i xi x) dx,
D_N(xi)=sum_{k=1}^N exp(-i 2^k xi),
```

we have `|a_N(xi)|>=c0/N` on `|xi|<=N`. On one `2pi` period, orthogonality gives `E|D_N|^2=N`; binary uniqueness gives `E|D_N|^4=2N^2-N<=2N^2`. Paley--Zygmund applied to `|D_N|^2` gives a fixed positive fraction of each period on which `|D_N|>=sqrt(N/2)`. Therefore for every fixed `1<=p<2`,

```
int_R |fhat_N(xi)|^p dxi >= C_p N^(1-p/2) -> infinity.
```

So the heavy-row exponent is not a missing constant: it is a genuinely false Fourier norm interface. The null endpoint succeeds because the heavy active direction becomes linear and is paid as a physical hub before this absolute Fourier step. Any uniform near-null bridge must preserve that hub mechanism or exploit phase cancellation before absolute values; simply Fresnelising the new `eta S^2` curvature cannot work.

Fresh designated partner account03/B05 r27 is also compatible on a distinct packet: its theorem gives

```
||p_Q||_inf <= 128 sqrt(2) (delta_B mu m)^(-1/4).
```

Hence in its ratio-packet branch, `m>=3/20`, `mu>=1`, `delta_B>=1/16` implies the concrete exit `<581.745`; a survivor of that packet must therefore lie in the small-raw-diagonal chamber. This is a real inequality application, not a transfer to the heavy near-null bridge.

Required newest-Claude source actually used: the proved law-uniform Fourier lemma `int |fhat|^p <= 4pi/sqrt(p)` for `p>=2` and the translation-invariant geometric BL normalisation. The calculation above identifies exactly why its exponent threshold is saturated by the heavy near-null branch.

Next step in this run: sharpen the obstruction into an invariant statement for any direct three-curvature Fresnel/BL receiver, and test whether slicing in the moving hub slope can avoid the forbidden sub-2 norm without introducing a reciprocal degeneracy.