# account04/B15 handoff — full convolution L2 energy loses the rare-event KL

**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI:** OPEN / NOT PROVED  
**Scientific artifact:** `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md` in `yspennstate/math-open-problems`, creation commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`; checker-output snapshot commit `0488e5079afbcc91cb5b2ef50e598cef0aabcfac`.

## Exact inherited remainder

Consumed account02/B15 `20260922T085941Z-suspension-kl-no-loss`.  After the exact influence I-projection, the normalized all-gate remainder is

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\|Q_r)=H_{\max}(r)-H(P).
\]

On its sparse one-point-defect suspensions `F_m=y g_m`, every positive signed valuation-depth tail is exactly zero.  The KL credit cannot be fractionally discarded and repaired by an `O(J)` bank.

Consumed account03/B15 `20260922T092409Z-complement-packet-kl-gap`, which proves a one-packet `c<1` KL gap and proposes aggregating many convolution shifts or attacking the `c=1` branch.

## New theorem

Take `p=2^(1-m)`, `g_m=1-2 1_{x=0}`, `F_m=y g_m`.  The old-coordinate I-projection is product Bernoulli(`p`).  Put the **actual Fourier signs** of `g_m` on the square roots of those product masses, call the amplitudes `b_T`, and define every nonzero XOR-shift autocorrelation

\[
C_m(U)=\sum_T b_T b_{T\triangle U},
\qquad
\mathcal B_m=\sum_{U\ne0}C_m(U)^2.
\]

Then exactly

\[
\mathcal B_m=-16(1-p)^{2m}+24(1-p)^m-8(1+p-2p^2)^m+(1+4p-4p^2)^m-1,
\]

and therefore

\[
\boxed{\mathcal B_m=4mp+O(m^2p^2),\quad \mathcal B_m/I(g_m)\to4.}
\]

By contrast the exact retained KL satisfies

\[
\boxed{K_{\rm occ}/I(g_m)=m-5+1/\ln2+o(1)\to\infty.}
\]

Hence for any finite constants `A,L,C`,

\[
B_{\rm inf}^C(F_m)+A\mathcal B_m+LJ(F_m)<0
\]

for all sufficiently large `m`, whereas the exact KL-retaining residual is

\[
B_{\rm inf}^C+K_{\rm occ}=C I(g_m)-H(g_m),
\]

which is eventually positive for every `C>4`.

## Consequence

This refutes the natural continuation “sum all signed Boolean convolution equations in unweighted L2/Parseval energy and use that as the missing dependence payment,” even after adding any fixed `O(J)` valuation reserve.  It also rules out a fixed-constant `c=1` stability estimate `K_occ <= A B + L I` for this quadratic energy.

It does **not** refute the exact KL route, FEI, nonlinear/log-weighted multi-shift statistics, or a statistic recovering `K_occ` up to additive `O(I)`.  The next Interface-D statistic must preserve the sparse rare-event logarithm; merely rescaling the full convolution L2 energy is a dead route.

**Next recipients:** account02/B15, account03/B15, account03/B18.
