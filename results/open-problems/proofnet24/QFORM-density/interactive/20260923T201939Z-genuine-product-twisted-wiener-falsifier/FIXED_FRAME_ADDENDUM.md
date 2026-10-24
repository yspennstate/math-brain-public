# Fixed-frame strengthening of the genuine-product twisted Wiener falsifier

The [original report](REPORT.md) varies its orthonormal frame with the comb size \(N\). The same divergence occurs for one fixed frame, even with no source phases or attenuation.

Fix
\[
f=\frac{3-\sqrt5}{2}\in(1/3,1/2),\quad
a=\sqrt{f/2},\quad b=\sqrt{(1-f)/2},\quad
\Omega=[f(1-f)]^{-1/2},\quad D=\sqrt{2\pi/\Omega},
\]
and keep the six-dimensional frame
\[
\ell=(a,a,b,b,0,0),\qquad
p=(b,b,-a,-a,0,0),\qquad
v=(0,0,0,0,2^{-1/2},2^{-1/2}).
\]
It is orthonormal, and every row has leverage \(1/2\). The frame is now independent of \(N\).

Take \(k_r=F_r\), \(N_r=F_{r+2}\), where \(F_j\) are Fibonacci numbers, along the infinite subsequence with odd \(N_r\). Standard Fibonacci identities (or Binet's formula) give
\[
\gcd(k_r,N_r)=1,\qquad
\left|f-\frac{k_r}{N_r}\right|\le \frac{C}{N_r^2}.
\]
Because \(N_r\) is odd, \(\gcd(2k_r,N_r)=1\).

For each such \(N=N_r\), give the first four independent inputs the same normalized cap-one comb-plus-remote-filler densities as in the original report:
\[
F_{i,N}(x)=\sum_{j=0}^{N-1}
w\!\left(N\left(x-\frac{Dj}{\ell_i}\right)\right)
+g(x-N^3),
\]
with fixed narrow smooth \(w\) and smooth filler \(g\). Give the final two inputs any fixed independent smooth capped densities.

At the tooth centers, the phase is now
\[
q_m=e^{-2\pi i f m^2}
=q_m^{(N)}E_m,\qquad
q_m^{(N)}=e^{-2\pi i k_r m^2/N},\quad
E_m=e^{-2\pi i(f-k_r/N)m^2}.
\]
The local phase \(R(j,t)\), the sector lower bound on the structured \(L\)-density, and its fixed positive \(L^2\) norm are unchanged. The weighted Fourier representation becomes
\[
\widehat h_N(y)=\frac1N\sum_{m=0}^{4N-4}
q_m^{(N)}e^{iyDm}\bigl(E_mA_m(y)\bigr).
\]
The original report proved \(\sup_y\bigl[\max_m|A_m(y)|+\sum_m|A_{m+1}(y)-A_m(y)|\bigr]\le C\). The Diophantine approximation gives
\[
\sum_{m=0}^{4N-5}|E_{m+1}-E_m|
\le 2\pi\left|f-\frac{k_r}{N}\right|
\sum_{m=0}^{4N-5}(2m+1)
\le C.
\]
Therefore \(E_mA_m(y)\) still has uniformly bounded total variation in \(m\), for all \(y\).

The rational chirp \(q_m^{(N)}\) is \(N\)-periodic with flat discrete Fourier coefficients of modulus \(N^{-1/2}\), because \(N\) is odd and \(\gcd(2k_r,N)=1\). Its incomplete sums are \(O(\sqrt N\log(eN))\) uniformly in the linear frequency. Abel summation thus gives the same global estimate \(\|\widehat h_N\|_\infty\le C\log(eN)/\sqrt N\). The fixed-sector argument gives \(\|h_N\|_2^2\ge c>0\); hence
\[
\|\widehat h_N\|_1\ge c\,\frac{\sqrt N}{\log(eN)}.
\]
The smooth \(L\)-output cutoff still isolates the structured event from remote filler with uniformly bounded Fourier \(L^1\) cost. Independence of the final \(V\)-bank supplies a fixed positive \(z\)-integral. Consequently, for this **single fixed orthonormal row-leverage-\(1/2\) frame**, the genuine-product twisted integral \(J(1)\) tends to infinity along the stated input-law sequence.

As before, this is a failure of the absolute twisted Fourier estimate. The independent-\(V\)-bank half-potential theorem gives a uniform density bound for the associated canonical quadratic form.
