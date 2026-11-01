# S1's claimed proofs — log removal (n and eps out of the logarithm) — UNVERIFIED

Status: claimed complete by S1; adversarial verification pending. Setting = paper's model (S),
canonical class A_{m,L} with rigidity, entropy (E): log N(A, ||.||_inf, u) <= C_E m d log(C_E m d(2+L)/u).
[m denotes m-bar = (K-1)m+1 throughout.]

## Theorem A (complexity with n-free, eps-free log)
For all n, m >= 1, d >= 3, L > 0, with B := C_E m d (2+L) and Lambda := log(2 e B sqrt(d)/L):
  E_{x,y} sup_{f in A_{m,L}} (1/n) | sum_i y_i clip(f(x_i)) |
     <= C [ (1+L)/sqrt(n) + L sqrt(m Lambda / n) + (1+L) m d Lambda / n ].

Proof structure:
- Lemma A1 (harmonic split; Poincare). F = clip.f = c_F + <A_F, x> + h with c_F = E F,
  A_F = d E[F x]; |c_F| <= 1; ||A_F|| <= sqrt(d/(d-1)) L; E h^2 <= L^2/(2d) (spectral:
  sum_{l>=2} lambda_l ||F_l||^2 <= E|grad_T F|^2 <= L^2, lambda_2 = 2d); sup|h| <= B_1 := 2 + sqrt(3/2) L;
  h orthogonal to {1, linear}.
- Lemma A2 (affine sector). E_y sup_{|c|<=1, ||A||<=sqrt(3/2)L} (1/n)|sum y_i (c + <A,x_i>)|
  <= (1 + sqrt(3/2) L)/sqrt(n).  [E||sum y_i x_i|| <= sqrt(n).]
- Lemma A3 (Dudley at the empirical radius). H := {F - c_F - <A_F, .>}: entropy transfers from (E)
  with the degree-<=1 projection being (1+sqrt d)-Lipschitz in L^inf (absorbed into log).
  Conditionally on x, with sigma-hat^2 := sup_H (1/n) sum_i h(x_i)^2:
  E_eps sup_H (1/n)|sum eps_i h(x_i)| <= (C sqrt(m d)/sqrt(n)) phi(sigma-hat),
  phi(s) = s sqrt(log(2 e B / s)).  [Uses int_0^r sqrt(log(B/u)) du <= 2 r sqrt(log(e B/r)).]
- Lemma A4 (radius self-bounding). E_x sigma-hat^2 <= r^2 + 8 B_1 R-tilde, r^2 := L^2/(2d),
  R-tilde := E sup_H (1/n)|sum eps h|.  [Symmetrization + Ledoux-Talagrand contraction for s^2/(2B_1).]
- Assembly: psi(s) := phi(sqrt s) concave increasing; Jensen; two-case solve:
  8 B_1 R-tilde <= r^2  =>  R-tilde <= C L sqrt(m Lambda/n);
  else R-tilde <= C B_1 m d Lambda / n.

## Theorem B (the law with n-free log)
c_0, C_0 absolute; model (S), d >= 3, eps in (0, sigma^2], Lambda-bar := log(e m d (2+1/eps)); if
  n >= C_0 [ eps^{-2} log(8/delta) + eps^{-1} m d Lambda-bar + m d^2 Lambda-bar ]
then with prob >= 1-delta every fitting f (MSE <= sigma^2 - eps) has
  Lip_S(f) >= c_0 eps sqrt( n / (m Lambda-bar) ).
Proof: L* := c_0 eps sqrt(n/(m Lambda-bar)); value bound => class membership; paper's noise
decomposition (pointwise in f) => (1/n) sum z_i f-tilde(x_i) >= eps/4 on E_1 cap E_2;
multiplier symmetrization + contraction (|z_i| <= 2) => E sup <= 8 R_tot(Theorem A at L*);
Lambda(L*) <= C Lambda-bar via eps sqrt(n) >= 1; the three sample-size terms make the three
Theorem-A terms <= eps/24 each; McDiarmid (bounded differences 4/n) finishes.
BLN corollary: Lip >= c sqrt(n/(m log(C m d))) once n >= C m d^2 log(C m d).

## Lemma D (dictionary sup — log-free)
On {||X||_op <= C(sqrt(n/d)+1)} (prob >= 1-2e^{-d}):
  E_y sup_{||u||=1, t in [0,1]} | sum_i y_i relu(<u,x_i> - t) | <= C (sqrt n + sqrt d).
Proof: increments sub-gaussian wrt rho = ||X(u-u')|| + sqrt(n)|t-t'|; product entropy of two
constant-aspect balls; Dudley integrals carry no log for constant aspect ratio.
Restricted version (t >= 1-Delta): <= C Delta sqrt(n d log(e/Delta)).

## Prop S (spiky sector — log-free)
delta_0 := 1/(m d log(e m d)). Contribution of all units with 1 - t_k <= delta_0:
  E_y sup (1/n)|sum_i y_i f_spiky(x_i)| <= C L sqrt(m/n).
Proof: dyadic shells in 1-t; rigidity |alpha| <= 2L 2^{(j+1)/2}/sqrt(delta_0) per shell;
restricted Lemma D per shell; geometric sum; choice of delta_0.
Consequence: reduces to 1 - t_k >= delta_0, i.e. |alpha_k| <= C L sqrt(m d log(e m d)).

## Prop L5 (Sudakov ceiling — no single-scale log necessity)
Entropy (E) + radius sigma-hat <~ L/sqrt(d) cap every packing-based minoration at
C L sqrt(m Lambda / n), Lambda = log(m d); log n / log(1/eps) necessity REFUTED by Theorem A;
radius-scale packings have log-cardinality Theta(m d) (constant-relative-distance codes carry
no log).

## Lower-bound landscape (constructions)
- Profile spikes: R_n(L) >= min(1, L/5) floor(m/2)/n; at m >= 2n attains conjectured form.
- Affine: >= c min(1,L)/sqrt(n).
- Bulk ellipsoid (m <= d): >= c L sqrt(m/(nd)).
- Group construction FAILS to reach L sqrt(m/n): gradient pile-up sqrt(#active), confirmed
  numerically (L-hat = sqrt(#active) to 3 digits). Best known for m << n:
  c [ min(1,L) m/n + L sqrt(m/(nd)) 1_{m<=d} + min(1,L)/sqrt(n) ].

## Missing to fully log-free (S1's localization)
- C1 (uniform fiber bound for the box-cap-ellipsoid body; visible-trace ratio-LLN
  sup tr(M^{-1} Phi^T Phi) <= C n m / d over visible configs + invisible incidence
  N_k <= C(n P_k + d log n)).
- C2 (fibered chaining body-transport at merging units; increment estimate proved:
  D <= C(sqrt(n/d)+1) sum_k |a_k| ||u_k - u_k'|| + sqrt(n) sum_k |a_k||t_k - t_k'|).
- Conditional theorem: C1 + C2 + above => R_n(L) <= C[(1+L)/sqrt n + L sqrt(m/n)] — fully
  log-free BLN for PL activations (n >= C d log n).
