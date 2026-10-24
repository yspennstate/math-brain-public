# B16 handoff — central Radon energy-distance capacity

Status: **PARTIAL / PROVED SOURCE LEMMAS / FULL FEI OPEN / WITHOUT_VERIFIED_BRAIN**.

The newest account04 central Hardy/Ward reduction asks for a dimension-free payment of a two-sided Bernoulli prefix/suffix square on the q-flip compiler. The physical source side now has an exact answer.

For one physical cut
\[
\eta_i=\frac{1-f(x)f(x+e_i)}2,
\qquad
a_i(U)=\widehat\eta_i(U)^2,
\qquad
E_i=\alpha_i(1-\alpha_i),
\]
the q-flip frustration profile
\[
p_i(w)=2E_i-2\sum_{U\ne0}a_i(U)(-1)^{U\cdot w}
\]
is conditionally negative type. For any probability laws \(\mu,\nu\),
\[
2E_{\mu,\nu}p_i-E_{\mu,\mu}p_i-E_{\nu,\nu}p_i
=
2\sum_{U\ne0}a_i(U)(\widehat\mu(U)-\widehat\nu(U))^2.
\]

For the exact central Ward pair
\[
\mu_t=\mathrm{Ber}((1-t)/2)^{\otimes m},
\qquad
\nu_t=\mathrm{Ber}((1+t)/2)^{\otimes m},
\]
only odd Walsh levels survive:
\[
\delta_i(t):=E_{\mu_t}p_i-E_{\nu_t}p_i
=
-4\sum_{|U|\text{ odd}}a_i(U)t^{|U|}.
\]
The central square satisfies the sharp source bound
\[
\boxed{
\int_0^{1/2}t(1/2-t)\delta_i(t)^2dt
\le \frac{E_i^2}{40}.
}
\]
After the minimizing-character fold,
\[
\boxed{
\sum_i\int_0^{1/2}t(1/2-t)\delta_i(t)^2dt
\le \frac{J(f)}{270}.
}
\]

More generally, if a centered translation-invariant source kernel has only odd Walsh multipliers and
\[
|\widehat K_t(U)|\le M t^{|U|},
\]
then its q-flip pairing obeys
\[
\boxed{
\sum_i\int_0^{1/2}t(1/2-t)
\langle K_t,p_i\rangle^2dt
\le \frac{M^2}{1080}J(f).
}
\]

This is the next compiler criterion. The remaining step is **not** another generic source norm: compute the exact Walsh multiplier of the fully refunded central plaquette/terminal/R16 map under the random translated/pivoted q-flip basis. If its normalized odd multiplier is \(O(1)\), the source square is paid dimension-free by the theorem above. If the refunded multiplier still diverges on an authentic Boolean family, this central Radon compiler route is dead.

The raw ordered-min kernel's old \(O(n)\) modes do not decide this, because later dummy-Ward identities prove that some raw growth is exactly refunded. Account02's new channel-density theorem also shows counting active q-flips cannot replace this signed multiplier step.

See `REPORT.md` and `check_central_radon_energy.py`. Full FEI remains open.
