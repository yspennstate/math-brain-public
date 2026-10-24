TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T21:47:13.412035Z — FEI interface-C integration: q=1/q=3 Hodge companion and R16-compensation localization.

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. Full-problem change versus mechanism change

**FULL-PROBLEM CHANGE: NONE.** I do not prove a universal finite constant in
\[
H(f)\le C I(f)
\]
for every uniform-cube Boolean function.

**MECHANISM CHANGE: YES.** The last three substantive B18 reports moved, successively, through:

1. an arbitrary-product-noise mask payment;
2. an arbitrary-pair affine-subspace plaquette payment, which removed the product-noise shape restriction but still required a positive physical pair lift; and
3. restriction-kernel polarization, which replaced that lift by positive PSD source banks.

The newest exact half-band counterexample now proves that any all-Boolean **positive** current-to-`O(J)` continuation of that route is false. This run therefore leaves the diagonal positive current before trying another physical norm. It proves an exact **cross-degree, pre-square Hodge identity** between the charged `q=3` syndrome layer and the current-killed `q=1` layer, with the terminal-code failure isolated as one explicit character defect. On the actual sparse half-band obstruction family this cross term has exactly the missing `Theta(n^{-3})` size, while the authentic R16 bank and terminal endpoint are exponentially too small. Thus the compensation forced by the no-go is localized to a source-level signed cross term, not to the already-reserved R16/terminal banks.

This does not yet prove that the Hodge cross term occurs with the required sign and multiplicity in the full compiler ledger. That is the new universal obligation.

# 1. Fresh source chain actually consumed

The scientific master was refreshed during this run. The following completed other-account result is used in the proofs below, not merely cited:

- `account03/B18/20260921T212630Z-positive-contraction-no-go/REPORT.md` and its source-bound handoff. It proves for the genuine half-band four-point Boolean family that the exact central positive current obeys
  \[
  \mathcal P_{\rm cen}\sim \frac{11}{864 n^3},\qquad
  J(f)=\frac{8n}{2^D},\qquad n=D-1,
  \]
  with all charged modes `(q,k)=(3,1)`, while the function itself satisfies `H(f)<4I(f)`. It also proves that any compensating signed term in an inequality of the form `P_cen-C <= O(J)` must itself have `liminf n^3 C >= 11/864` (up to the separately stated outer averaging factor if that average is imposed).

I also consumed the newly completed `account02/B17/20260921T215432Z-selector-phase-low-plaquette/HANDOFF.md`. Its low-plaquette cut theorem is compatible with the present route: rare physical plaquette interaction can lead to approximate factorization, but the stronger global prefix remainder bound is refuted. I do not use its unfinished adaptive amortization as a payment here.

Exact compiler dependencies used below are:

- the authentic account02/B16 parent/current representation;
- account04/B16 parity-current Walsh diagonalisation, in particular the exact annihilation of `q=1` and the `q=3,k=1` saturation mode;
- the historical/source-recovered R16 common-relation reservoirs and terminal moment-saturation theorem;
- the exact account02 interactive half-band collision extension, including its bounded-independence lemma for an arbitrary dependent bounded sign multiplier.

No positive part is inserted into R32. No terminal code is replaced by a binomial model.

# 2. Exact target/checklist entering this run

The smallest honest interface-C target is now:

1. retain the actual same-syndrome signed coefficients `b_R(s)`;
2. keep the R32 `0 mod 4` debits and `2 mod 4` credits signed;
3. keep the terminal subtraction `P_0-P_1` with
   \[
   P_0=RM(1,D),\qquad P_1=RM(d,D);
   \]
4. do not replace the current by a nonnegative sink before exposing a compensating signed term;
5. preserve the exact central multiplier, in particular
   \[
   \varepsilon_{3,1}=\frac{11}{288};
   \]
6. do not spend R16 or the signed terminal endpoint twice;
7. after compensation, only then seek an `O(J)` physical or restriction payment.

The account03 no-go proves that item 4 is essential: the raw central positive current is polynomially larger than every fixed multiple of `J` on an actual half-band Boolean family.

# 3. PROVED — exact R16 scale on the half-band obstruction family

The four-point source has negative set an affine two-plane `Q` in `F_2^D`; put
\[
N=2^D,\qquad n=D-1.
\]
For the Boolean function `f=1-2 1_Q`, the squared Fourier law is independent of the orientation of `Q`:
\[
p_0=\left(1-\frac8N\right)^2,
\qquad
p_1=\frac{64}{N^2}
\]
with multiplicity
\[
m=\frac N4-1
\]
for `p_1`, and zero elsewhere. Write
\[
\delta=mp_1=1-p_0=\frac{16}{N}-\frac{64}{N^2}.
\tag{3.1}
\]
Hence the exact initial R16 common-relation reservoir is
\[
C_{0,r}=1-p_0^r-mp_1^r.
\tag{3.2}
\]

Let `d=ceil(D/2)` and let `D_{d,r}=C_{0,r}-C_{d,r}` be the half-band R16 deposit. The terminal moment-saturation theorem gives
\[
D_{d,r}=C_{0,r}\qquad(2\le r<2^d).
\tag{3.3}
\]
Define
\[
\Delta_{d,>2}
=\sum_{r=2}^{\infty}
\frac{(-1)^rD_{d,r}}{(r-1)2^{r-1}}.
\tag{3.4}
\]
If the terminal prefix were fully spent at every order, the corresponding exact series is
\[
\begin{aligned}
\Delta_\infty
&:=\sum_{r=2}^{\infty}
\frac{(-1)^rC_{0,r}}{(r-1)2^{r-1}}\\
&=\log\frac32
-p_0\log\left(1+\frac{p_0}{2}\right)
-mp_1\log\left(1+\frac{p_1}{2}\right).
\end{aligned}
\tag{3.5}
\]
This follows from
\[
\sum_{r=2}^{\infty}\frac{(-1)^r}{(r-1)2^{r-1}}=\log\frac32,
\qquad
\sum_{r=2}^{\infty}\frac{(-1)^r x^r}{(r-1)2^{r-1}}
=x\log\left(1+\frac x2\right).
\]

Because `0<=D_{d,r}<=C_{0,r}<=rJ`, (3.3) gives the explicit terminal-saturation error
\[
\boxed{
|\Delta_{d,>2}-\Delta_\infty|
\le 2^{3-2^d}J(f).
}
\tag{3.6}
\]

For this source `J(f)=8n/N`. Expanding (3.5) at large `N`, with `A=log(3/2)`, gives
\[
\boxed{
\Delta_\infty
=\frac{16(A+1/3)}N+O(N^{-2}).
}
\tag{3.7}
\]
Consequently the authentic half-band R16 bank
\[
\mathcal B_d=\kappa_2J-\Delta_{d,>2},
\qquad
\kappa_2=\frac23+\operatorname{artanh}(1/2),
\]
satisfies
\[
\boxed{
\mathcal B_d
=\frac{8\kappa_2 n-16(A+1/3)+o(1)}N
=O\!\left(\frac nN\right)
=O(J).
}
\tag{3.8}
\]

This scale is exponentially smaller than the required `Theta(n^{-3})` companion forced by the exact positive-current theorem. At `D=128`, the closed-form full-spent proxy for `B_d` is about `3.596e-36`, while `11/(864 n^3)` is about `6.215e-9`; their ratio is about `5.79e-28`. The actual half-band correction in (3.6) is vastly smaller still.

### Corollary 3.1 — R16/endpoint-only compensation is impossible on this family

The carried half-band terminal theorem has `R_d=o(J)` uniformly over noncharacters. Therefore, on the present family,
\[
\mathcal B_d+|R_d|+C_0J=o(n^{-3})
\]
for every fixed constant `C_0`, whereas any compensation of the genuine central positive current must have order at least `n^{-3}`.

Thus the missing compensation cannot be supplied solely by the already-designated R16 bank, the net terminal endpoint, or another fixed-multiple-of-`J` sink. It must occur **inside the signed source transformation before the positive current is isolated**, unless a separately proved high-ratio-core reduction excludes this family before interface C is invoked.

# 4. PROVED — affine-plane Hodge complement identity with exact terminal defect

This section exposes such a pre-square source companion.

Let `Q={q_1,q_2,q_3,q_4}` be any affine two-plane in the truth-table cube. Let `h:V->{+1,-1}` be an arbitrary fixed base phase and put
\[
\sigma_Q(h)=\prod_{x\in Q}h(x).
\tag{4.1}
\]
For a linear mask code `P` and `r in P`, set
\[
y_x=h(x)(-1)^{r(x)},
\qquad
W_r=\sum_{x\notin Q}y_x.
\]
For `R subseteq Q`, define the active Walsh coefficient in the normalization used by the current construction by
\[
 b_R^{P}(Nt;h)
 =2N\,\mathbb E_{r\in P}
 \operatorname{Re}\left[
 e^{itW_r}(i\sin t)^{|R|}(\cos t)^{4-|R|}
 \prod_{x\in R}y_x
 \right].
\tag{4.2}
\]
This is exactly the coefficient obtained by Fourier-expanding the four active truth-table toggles before any square.

Fix `i in Q` and let `T_i=Q\setminus{i}`. Since `|T_i|=3`, (4.2) gives
\[
 b_{\{i\}}^P
 =-2N\sin t\cos^3t\,
 \mathbb E_P[y_i\sin(tW_r)],
\tag{4.3}
\]
\[
 b_{T_i}^P
 =2N\sin^3t\cos t\,
 \mathbb E_P\left[\left(\prod_{x\in T_i}y_x\right)\sin(tW_r)\right].
\tag{4.4}
\]
Let
\[
\chi_Q(r)=(-1)^{\sum_{x\in Q}r(x)}.
\tag{4.5}
\]
Because
\[
\prod_{x\in Q}y_x=\sigma_Q(h)\chi_Q(r),
\]
we have
\[
\prod_{x\in T_i}y_x=\sigma_Q(h)\chi_Q(r)y_i.
\tag{4.6}
\]
Substitution into (4.3)-(4.4) proves the exact identity
\[
\boxed{
 b_{T_i}^{P}(Nt;h)
 +\sigma_Q(h)\tan^2t\,b_{\{i\}}^{P}(Nt;h)
 =2N\sigma_Q(h)\sin^3t\cos t\,
 \mathbb E_P[(\chi_Q-1)y_i\sin(tW_r)].
}
\tag{4.7}
\]

For the affine code
\[
P_0=RM(1,D),
\]
every affine function has even parity on an affine two-plane, so `chi_Q=1` identically. Hence
\[
\boxed{
 b_{T_i}^{P_0}
 =-\sigma_Q(h)\tan^2t\,b_{\{i\}}^{P_0}.
}
\tag{4.8}
\]
This is a signed Hodge complement: the `q=3` mode is paired with the complementary `q=1` mode, and the pairing sign is exactly the physical plaquette product `sigma_Q(h)`.

For the retained compiler potential
\[
b_R=b_R^{P_0}-b_R^{P_1},
\qquad P_1=RM(d,D),
\]
(4.8) leaves only the genuine terminal defect:
\[
\boxed{
H_i(Nt;h)
:=b_{T_i}(Nt;h)+\sigma_Q(h)\tan^2t\,b_{\{i\}}(Nt;h)
=-2N\sigma_Q(h)\sin^3t\cos t\,
\mathbb E_{P_1}[(\chi_Q-1)y_i\sin(tW_r)].
}
\tag{4.9}
\]
No terminal term has been dropped. If `Q in D_d=P_1^perp`, then `chi_Q=1` on `P_1` and the retained Hodge identity is exact with `H_i=0`.

Equation (4.9) is the first source-exact cross-degree interface in this chain that has the correct scale to repair the account03 positive-current obstruction. It also retains the physical orientation: `sigma_Q=-1` and `+1` are not identified.

# 5. PROVED — on the genuine half-band obstruction, the Hodge cross term supplies the missing scale

Return to the actual account03/account02 four-point half-band family. Let
\[
T=(2n)^{-1/2},\qquad S_f=NT,
\qquad
m_d=2^{d-1}-1.
\]
The bounded-independence collision lemma used in the exact half-band countertheorem applies to **any** dependent bounded multiplier `Z`. In (4.9) take
\[
Z=\frac{(\chi_Q-1)y_i}{2},
\qquad |Z|\le1.
\]
Then `|sin t|<=t`, `|cos t|<=1`, and the collision lemma give
\[
\boxed{
\int_0^{S_f}\frac{|H_i(s)|^2}{s^3}\,ds
\le
\frac{16\pi T^3}{\sqrt{m_d}}.
}
\tag{5.1}
\]
Indeed, after `s=Nt`, the square of the prefactor in (4.9) contributes at most `16t^3`, and the collision integral is at most `pi/sqrt(m_d)`.

At the half-band `d=ceil(D/2)`, and more generally whenever `2^d/n^3 -> infinity`,
\[
\frac{T^3}{\sqrt{m_d}}=o(T^6).
\tag{5.2}
\]
The exact source theorem already proves, for each of the four charged triples,
\[
\int_{40}^{S_f}\frac{|b_{T_i}(s)|^2}{s^3}\,ds
\sim \frac23T^6.
\tag{5.3}
\]
Set
\[
u_i(s)=\sigma_Q(h)\tan^2(s/N)b_{\{i\}}(s).
\]
Then `H_i=b_{T_i}+u_i`, so (5.1)-(5.3) imply in the live weighted Hilbert space
\[
\|u_i\|_2^2\sim\|b_{T_i}\|_2^2\sim\frac23T^6,
\qquad
\langle b_{T_i},u_i\rangle
\sim-\frac23T^6.
\tag{5.4}
\]
Thus the current-killed singleton layer carries an **oppositely phased companion of exactly the same polynomial scale** as the charged triple layer.

For `(q,k)=(3,1)` the authentic central multiplier is
\[
\varepsilon=\frac{11}{288}.
\]
Define the source-level Hodge companion on this four-triple packet by
\[
\boxed{
\mathcal C_H
:=-\varepsilon\sum_{i\in Q}
\langle b_{T_i},u_i\rangle_W,
\qquad W=[40,S_f].
}
\tag{5.5}
\]
The corresponding positive central current is
\[
\mathcal P_{\rm cen}
=\varepsilon\sum_{i\in Q}\|b_{T_i}\|_{2,W}^2.
\tag{5.6}
\]
Because `H_i=b_{T_i}+u_i`, there is the **exact algebraic remainder identity**
\[
\boxed{
\mathcal P_{\rm cen}-\mathcal C_H
=\varepsilon\sum_{i\in Q}
\langle b_{T_i},H_i\rangle_W.
}
\tag{5.7}
\]
Therefore Cauchy-Schwarz and (5.1) give
\[
|\mathcal P_{\rm cen}-\mathcal C_H|
\le
\varepsilon
\left(\sum_i\|b_{T_i}\|_{2,W}^2\right)^{1/2}
\left(\sum_i\|H_i\|_{2,W}^2\right)^{1/2}
=o(n^{-3}).
\tag{5.8}
\]
Using the known central-current asymptotic,
\[
\boxed{
\mathcal C_H
\sim\mathcal P_{\rm cen}
\sim\frac{11}{864n^3}.
}
\tag{5.9}
\]

This does **not** assert that `C_H` is already an authorized positive credit in the global entropy ledger. The theorem is narrower and source-exact: it proves that the polynomial compensation demanded by the positive-current no-go is present algebraically as a `q=3`/`q=1` **signed cross term of the actual retained Borel coefficients**, while the R16 bank and terminal endpoint are exponentially too small. The remaining job is to derive this cross term from the original signed compiler identity with the correct global multiplicity and no ledger reuse.

# 6. Why this is a genuine interface-C change

The positive-current Walsh-frame step diagonalizes syndrome degrees and therefore destroys the cross term in (5.5). That diagonalization is excellent for positivity but is exactly too early on the no-go family. The new evidence says the worst saturating mode `(3,1)` should instead be treated by a Hodge block
\[
\{q=1,q=3\}
\]
before translation averaging or squaring.

The physical orientation is not an abstract surrogate: `sigma_Q(h)` is the signed plaquette product on the actual affine two-plane. Thus this mechanism is compatible with the account03 signed physical-flag theorem. The only failure of the affine-code Hodge relation is the explicit terminal character `chi_Q`, which is already source-bound to `P_1=RM(d,D)`.

The newly consumed B17 low-plaquette theorem is complementary rather than a substitute. If an adaptive factorization tree eventually amortizes its `n sqrt(Q)` losses, low-plaquette sectors could be removed before this current analysis. Until that theorem exists, (4.9) gives a direct signed source mechanism that repairs the strongest known positive-current obstruction without assuming a high-ratio restriction.

# 7. Exact ledger after this run

## PROVED

- The authentic half-band R16 bank on the four-point positive-current obstruction has the exact closed form (3.5) up to the doubly-exponentially small terminal-saturation tail (3.6), and is `O(n/2^D)`.
- Therefore R16, the carried net terminal endpoint, and any fixed `O(J)` physical sink cannot supply the `Theta(n^{-3})` compensation required by the exact central positive-current lower bound.
- The affine-code `q=1/q=3` Hodge relation (4.8) is exact for every affine two-plane and arbitrary base phase.
- For the retained `P_0-P_1` source, its complete failure is the explicit terminal character defect (4.9); no other error term occurs.
- On the genuine half-band obstruction family the terminal Hodge defect is `o(n^{-3})`, and the cross-degree companion (5.5) cancels the exact central current to `o(n^{-3})`.

## CONDITIONAL / NOT YET A PAYMENT

- If the original signed R32/Shapley/compiler ledger can be rewritten so that the global sum of the Hodge cross terms (5.5) appears with its source sign and multiplicity, then the worst `q=3,k=1` positive-current sector reduces to the terminal Hodge defects plus non-saturating higher-syndrome modes. This ledger extraction is not proved here.

## OPEN

1. Prove the global source identity that exposes the `q=1/q=3` Hodge cross term **before** syndrome translation diagonalization, with no double spending of R16, negative R32 credit, or the terminal endpoint.
2. Pay the summed terminal Hodge-defect correlations in (4.9), or identify their exact cancellation with the finite-window/terminal boundary term.
3. Extend the block mechanism to `q>=5` or show the remaining two-resolvent multiplier is directly payable once the saturating `q=3` sector is removed.
4. Independently integrate the low-plaquette factorization route only after its adaptive losses are truly amortized.

## REFUTED / MUST NOT BE REVIVED

- universal positive central/full current `<= C J`;
- positive/TV parent-by-parent plaquette lift without the codimension factor;
- global rank/l1 phase payment, sign-free parity/profile payment, and strict-superset receiver-only charging;
- the claim that the R16 bank or net terminal endpoint can furnish the polynomial-scale compensation on the known half-band obstruction family.

# 8. Primary-literature applicability check

A fresh arXiv/web check this run still finds no unrestricted FEI proof. Potapov's September 18, 2026 paper proves FEI for plateaued Boolean functions (sharp constant 4 in that class) and partially bent functions (sharp constant 2), not for every Boolean function. González--MacManus--Pereyra's 2026 restriction/stopping-tree paper explicitly leaves its universal restriction inequality as the conditional step that would imply full FEI. Li--Han's information-theoretic strengthening retains the coordinate influence-profile term. No novelty/priority claim is made for the Hodge formulation above.

# 9. Next nonoverlapping proof-sized claim

B18's next exact target is no longer another positive kernel bound. It is:

> Starting from the authentic signed R32/Aumann--Shapley current **before** syndrome-translation squaring, extract the sum of affine-plane Hodge cross terms
> \[
> -\sum_{Q,i}\varepsilon_{Q,i}\,\sigma_Q\tan^2(s/N)\,b_{Q\setminus i}(s)b_{\{i\}}(s)
> \]
> with its actual orientation and multiplicity, and show that the remaining terminal-character defect is already one of the retained boundary/terminal ledger terms or is bounded by an unused `O(J)` bank.

This target is source-exact, survives the known no-go family, and does not duplicate the B17 low-cut factorization task or B13 critical-core row-defect task.
