# Padding energy and scope ledger

For the lift

\[
F(x,z)=g(x_i\chi_{c_i}(z):1\le i\le n),
\]

define the deterministic spectral label
`C(S)=xor_{i in S} c_i`. The complete accounting is

- preserved squared masses: `mu_F(S,T)=mu_g(S) 1[T=C(S)]`;
- preserved entropy: `H(F)=H(g)`;
- added energy: `D=E_mu_g |C(S)|`;
- coordinate cost: `I_{z_j}=Pr[C(S)_j=1]` and `D=sum_j I_{z_j}`;
- conditional label entropy: `H(T|S)=0`;
- every padding-block physical restriction preserves the complete mass
  multiset, hence `Gamma_A=0`.

This imports and sharpens the independent-padding barrier: independent
product padding, disjoint labels, repeated labels, deterministic occupied
coordinates, and arbitrary linear label collisions are all included by the
same exact formula. No auxiliary coordinate is free, and none creates new
spectral entropy. The dependence here is correlated but not genuinely new:
the entire auxiliary Fourier label is a deterministic function of the core
frequency. A route beyond this barrier must introduce a Boolean mechanism
whose child squared spectra actually mix, rather than merely attach a
deterministic codeword to each occupied core frequency.

The result does not claim that the registered non-Boolean
`FIXED_CONV_PREFIX` or `FIXED_CAP_PREFIX` examples are Boolean-realizable.
It instead proves a full-Booleanity obstruction for the explicit parity-code
family. It also does not cover nonlinear gadgets whose Fourier expansion
splits one core coefficient among several auxiliary frequencies.

## Controls

- **Parity-zero erasure:** if `C(S)=0` on occupied support, then `D=0`; the
  padding is spectrally irrelevant. The one-bit parity lift is the special
  case `c_i=1` and agrees with the existing exact coefficient map.
- **Rare sparse defects:** a rare nonzero label pays its exact probability in
  auxiliary influence. It still creates no entropy and exposes `Gamma=0`.
- **Addressing:** a coded address label remains deterministic given the core
  frequency; there is no illicit per-coordinate label payment, but there is
  also no entropy gain.
- **Near tensors:** pure character padding is a special case and decreases
  `H/I`. Coherent one-point surgery outside the form above is not ruled out.
- **Prime gates:** the transform preserves the core spectral masses and can
  only add influence, so it cannot increase a prime gate's FEI ratio.
- **Activation equivalence:** fixing a relevant padding coordinate recovers a
  child with the same entropy and smaller influence. An arbitrary hard core
  therefore cannot be hidden inside a critical padded source.

Exact verification is in `verify_linear_parity_padding.py` and `CHECK.out`.
It exhausts all Boolean cores on at most three variables and every ordered
linear code into at most two padding bits, including every nonempty physical
padding restriction and assignment. All 212,592 checks use rational Walsh
arithmetic; entropy equality is certified by exact equality of positive mass
multisets, without numerical logarithms.
