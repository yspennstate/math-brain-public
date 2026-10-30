# fleet04/B16 — all-constraint signed Boolean projection for the live Gibbs residual

**Classification:** `ESSENTIAL_STEP_APPLIED / SIGNED_SOURCE_TO_PHYSICAL_CONTRACTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Control, exact target, and inherited signed ledgers


The current common candidate consumed is fleet03/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T092424Z-quartic-safe-cone-frontier/REPORT.md`.

It defines `LIMIT-PRIME-GATE-LIFT-Q4-v1`

\[
\Gamma_Q(u)=\Gamma^\dagger(u)+{58551\over200000}\eta_4(u),
\qquad
\eta_4(u)={1-(1-2u)^4\over8},
\]

with center `C_Q=6.558445589`, and the exact normalized residual

\[
R_Q(G;p)=D_{\rm KL,2}(w^+\Vert\nu_Q^+)-\log_2{A_0^Q\over x_q^Q},
\qquad
D_{\Gamma_Q}(G;p)=V_q R_Q(G;p).
\tag{0.1}
\]

The sole promoted universal arrow remains `R_Q>=0` for every composition-prime gate and every interior product-bias vector, plus the decomposition and boundary cases. This report does not claim that arrow is closed.

The two requested interface-C sources were freshly consumed at their exact source paths:

1. fleet02/B16, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, theorem creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`. After same-syndrome signed aggregation its authentic central parent coefficients are
   \[
   \mu_j=\sum_{R:j\ {m doubled}}{\varepsilon_{q_R,k_R}\over r_R}b_R^2,
   \qquad \sum_j\mu_j=E_{\rm cen},
   \]
   and their original-coordinate incidence is at most `11/192 W`. No R32 coefficient is positive-parted before the signed aggregate `b_R` is squared.
2. fleet03/B18, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, theorem creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`. Its genuine physical signed sink is
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \]
   with ordered-flag payments `sum E kappa <= 2J`, `sum E kappa^2 <= 4J`, and `sum E o <= J/2` in the minimizing-character gauge.

The legacy dual-code multiplicity, opposite-sign overlap bank, negative entropy/KL credits, finite Borel window, R16/moment compensation, resolvent boundary, and terminal payments are **not spent again below**. The theorem here is a new all-gate signed contraction demanded by the later owner control; it does not silently declare the historical finite-window interface-C remainder solved.

## 1. Why the previous one-translation phase credit is not enough

The previous fleet04/B16 theorem

`20260922T081206Z-signed-gibbs-phase-residual`

kept one Boolean translation equation at a time and obtained a positive KL credit. Its unconditional complement-pair version is exponentially small in arity. The exact stated next step was to retain many signed constraints simultaneously and derive a PSD/relative-entropy packet inequality before taking absolute values.

There is a direct way to do this which also survives heterogeneous biased Fourier bases. Rather than sum individual convolution equations, invert the **entire signed comparison amplitude vector** back to the physical product cube and project it onto the Boolean hypercube there. This packages all signed Boolean constraints at once.

## 2. Setup in the authentic biased Fourier basis

Let

\[
G:\{0,1\}^k\to\{-1,+1\}
\]

be nonconstant under an interior product measure `mu_p`, and let

\[
\{\psi_S^p:S\subseteq[k]\}
\]

be its orthonormal biased Fourier basis. Write

\[
a_S=\widehat G_p(S),
\qquad
m=a_\varnothing=\mathbb E_pG,
\qquad
v=1-m^2=V_q>0.
\]

Then the actual normalized nonempty spectral law is

\[
w^+(S)={a_S^2\over v},\qquad S\ne\varnothing.
\tag{2.1}
\]

Let `nu^+` be **any** probability law on the nonempty subsets. In the live application it is exactly `nu_Q^+` from (0.1), with all original-coordinate prices retained.

Keep the actual coefficient orientation and define the signed comparison amplitudes

\[
b_\varnothing:=m,
\qquad
b_S:=\operatorname{sgn}(a_S)\sqrt{v\nu^+(S)}
\quad(S\ne\varnothing),
\tag{2.2}
\]

where a zero coefficient may be assigned either sign. Define the physical comparison field

\[
\boxed{
B_{\nu,p}(x):=\sum_{S\subseteq[k]}b_S\psi_S^p(x).
}
\tag{2.3}
\]

Parseval gives

\[
\mathbb E_p B_{\nu,p}^2=m^2+v\sum_{S\ne\varnothing}\nu^+(S)=1.
\tag{2.4}
\]

Thus `B` has exactly the same `L2` normalization and constant coefficient as the actual Boolean source, but its nonempty magnitudes are the target Gibbs magnitudes while its signs are the authentic source signs.

## 3. PROVED — all-constraint Boolean projection theorem

Define the physical Booleanity defect

\[
\boxed{
\mathcal Q_{\rm bool}(\nu;G,p)
:=\mathbb E_p\bigl(|B_{\nu,p}|-1\bigr)^2
=2\bigl(1-\mathbb E_p|B_{\nu,p}|\bigr).
}
\tag{3.1}
\]

The equality follows from (2.4).

### Theorem B16-ALL-CONSTRAINT-BOOLEAN-PROJECTION

For every nonconstant Boolean gate, every interior product bias, and every probability law `nu^+` on nonempty spectral subsets,

\[
\boxed{
 v\,D_{\rm KL,2}(w^+\Vert\nu^+)
 \ge
 -2\log_2\mathbb E_p|B_{\nu,p}|
 =-2\log_2\left(1-{\mathcal Q_{\rm bool}\over2}\right)
 \ge {\mathcal Q_{\rm bool}\over\ln2}.
}
\tag{3.2}
\]

Moreover `Q_bool=0` if and only if `|B_{nu,p}(x)|=1` for every physical atom of positive product measure. Thus the positive sink vanishes exactly when the signed target amplitudes themselves invert to a Boolean function with the same constant coefficient.

### Proof

Introduce full spectral probability laws

\[
P(\varnothing)=m^2,
\quad P(S)=v w^+(S),
\]

and

\[
Q(\varnothing)=m^2,
\quad Q(S)=v\nu^+(S).
\]

Their KL divergence is exactly

\[
D_{\rm KL,2}(P\Vert Q)=vD_{\rm KL,2}(w^+\Vert\nu^+).
\tag{3.3}
\]

Because the signs in (2.2) agree with the actual Fourier coefficients, their Bhattacharyya coefficient is

\[
\operatorname{BC}(P,Q)
=m^2+v\sum_{S\ne\varnothing}\sqrt{w^+(S)\nu^+(S)}
=\sum_S a_Sb_S.
\tag{3.4}
\]

Orthonormal inversion converts the last expression to the **physical signed overlap**

\[
\operatorname{BC}(P,Q)=\mathbb E_p[G B_{\nu,p}].
\tag{3.5}
\]

Now use Booleanity only at the last legitimate step: `|G|=1` pointwise, so

\[
\operatorname{BC}(P,Q)
\le\mathbb E_p|B_{\nu,p}|.
\tag{3.6}
\]

Monotonicity of Renyi divergence from order `1/2` to order `1`, in bits, gives

\[
D_{\rm KL,2}(P\Vert Q)
\ge-2\log_2\operatorname{BC}(P,Q).
\tag{3.7}
\]

Combining (3.3), (3.6), and (3.7) proves the first equality/inequality in (3.2). Equation (3.1) gives the middle form, and `-\log(1-z)>=z` gives the final linear bound. Finally, `E|B|<=sqrt(E B^2)=1`; equality holds exactly when `|B|` is constant almost surely, and (2.4) makes that constant one. `QED`.

### Geometric interpretation

The identity

\[
\inf_{F:\,F(x)\in\{-1,+1\}}
\mathbb E_p(F-B)^2
=\mathcal Q_{\rm bool}
\tag{3.8}
\]

is pointwise: the minimizer is `F=sign(B)`. Thus (3.2) is literally a contraction from the **complete signed spectral target** to squared physical distance from the Boolean cube. No individual Fourier relation is positive-parted, no sign is forgotten, and no selected packet is charged twice.

On the uniform balanced slice, the collection of ordinary XOR-convolution equations for `G^2=1` is simply the Fourier transform of the pointwise condition `G^2=1`. Equation (3.8) therefore uses all those signed equations simultaneously rather than one complement relation. In the biased case, where the XOR form is no longer the correct multiplication table, the physical projection remains exact because it works directly in the authentic biased orthonormal basis.

## 4. Direct insertion into the live quartic Gibbs candidate

For `LIMIT-PRIME-GATE-LIFT-Q4-v1`, take `nu^+=nu_Q^+` and write the resulting physical field as `B_Q`. Equation (0.1) and Theorem 3.2 give

\[
\boxed{
D_{\Gamma_Q}(G;p)
\ge
-2\log_2\mathbb E_p|B_Q|
-v\log_2{A_0^Q\over x_q^Q}.
}
\tag{4.1}
\]

Equivalently,

\[
\boxed{
D_{\Gamma_Q}(G;p)
\ge
-2\log_2\left(1-{\mathcal Q_{\rm bool}^Q\over2}\right)
-v\log_2{A_0^Q\over x_q^Q}.
}
\tag{4.2}
\]

Hence the following is a completely source-valid sufficient certificate for the live gate inequality:

\[
\boxed{
\mathbb E_p|B_Q|
\le\left({x_q^Q\over A_0^Q}\right)^{v/2}
\Longrightarrow D_{\Gamma_Q}(G;p)\ge0.
}
\tag{4.3}
\]

or, in squared physical-distance currency,

\[
\boxed{
\mathcal Q_{\rm bool}^Q
\ge2\left[1-\left({x_q^Q\over A_0^Q}\right)^{v/2}\right]
\Longrightarrow D_{\Gamma_Q}(G;p)\ge0.
}
\tag{4.4}
\]

When `A_0^Q<=x_q^Q`, the right side of (4.4) is nonpositive and the scalar part is already safe. The hard region is therefore reduced to proving a **physical Boolean-projection gap** for the signed Gibbs comparison field exactly where the partition demand is positive.

This does not prove that every prime gate satisfies (4.4). It replaces the exponentially small single-translation phase credit by a single all-constraints physical quantity which is exact at arbitrary arity and arbitrary interior bias.

## 5. Decisive source test — 228-fold improvement over complement parity on a prime four-bit gate

To test whether the all-constraint projection is merely a repackaging of the previous complement credit, I used the exact composition-prime four-bit source quoted in fleet04/B15 `20260922T081139Z-bellman-packet-split`, with uniform Walsh numerator vector

`(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0)`

and influences

\[
(r_1,r_2,r_3,r_4)=\left({1\over4},{1\over4},{1\over4},{3\over4}\right).
\]

Use the potential-independent maximum-entropy conditional-product I-projection `Q_r` from fleet02/B15 `20260922T0829Z-influence-iprojection-kl`. The deterministic checker gives

\[
K_{\rm occ}=D(w\Vert Q_r)=0.80128793785046237\ldots,
\]

while the signed physical comparison field satisfies

\[
\mathbb E|B|=0.83850045794793693\ldots.
\]

Therefore the new theorem certifies

\[
\boxed{K_{\rm occ}\ge0.50823304633612032\ldots .}
\tag{5.1}
\]

The previously proved complement-parity payment on the **same** `Q_r` target is only

\[
0.0022229157596198677\ldots.
\]

Thus the simultaneous signed physical projection is larger by

\[
\boxed{228.6335161990\ldots}
\tag{5.2}
\]

on this genuine prime Boolean source. This is not evidence from a non-Boolean row and is not a universal constant claim; it demonstrates that keeping all signed constraints together can recover two orders of magnitude of dependence credit that a single complement equation discards.

## 6. Verification

`CHECK.py` is standard-library only. It checks the analytic inequality numerically on:

- all `270` nonconstant Boolean gates through arity three at one fixed heterogeneous bias/odds choice;
- `1,906` deterministic pseudo-random nonconstant cases through arity four with heterogeneous biases and target odds;
- the exact four-bit prime Walsh vector above and its conditional-product I-projection.

The maximum normalization/overlap identity discrepancy was `1.5543122344752192e-15`. The random minimum `KL - projection lower bound` was `1.0009579000436197e-05`; the exhaustive minimum was `-3.2e-16`, numerical zero at an equality case. The theorem itself is analytic and does not depend on these finite tests.

## 7. What changed and what remains open

**Old missing implication:** the one-translation signed phase credit decays exponentially and does not pay the live all-gate Gibbs deficit at arbitrary arity.

**New proved inference:** every authentic biased Boolean source has the all-constraint inequality (3.2), converting the entire signed target amplitude vector into one physical Boolean-distance sink before any absolute-value relaxation. For the live `Gamma_Q` candidate, (4.3)-(4.4) are exact source-valid sufficient criteria.

**Replacement obligation:** prove (4.4) for every composition-prime gate in the positive-partition-demand region, or construct a genuine prime/bias pair where the physical projection gap is too small and `R_Q<0`. A useful next attack is to combine (3.8) with the prime/decomposition condition and the exact influence I-projection corridor, rather than returning to one-translation parity credits.

**Historical interface C:** fleet02/B16's authentic parent weights and fleet03/B18's signed flag curvature remain valid at their proved scopes. This report does not reuse their finite-window, R16, terminal, dual-code, or opposite-sign ledgers and therefore does not claim the old interface-C source-to-flag map is universally closed.

**Full FEI:** `OPEN / NOT PROVED`.
