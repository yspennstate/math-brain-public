# fleet03/B15 — exact real-restriction packet decomposition and sharp all-bias JS payment

**Run:** `20260922T082654Z-B15-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Candidate and prior missing implication

This run keeps the B-lead's current candidate and common Shannon normalization:

`LIMIT-PRIME-GATE-LIFT-v1` with

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\]

and `B-GIBBS-KL-v1`

\[
D_{\Gamma^\dagger}(G;p)
=V_q\,R_B(G;p),
\qquad
R_B=D_{\rm KL,2}(w^+\|\nu_x^+)-\log_2{A_0\over x_q}.
\]

The exact lead source consumed is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`.

The required other-account completed result consumed and applied is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`.

I use its exact all-gate Gibbs factorization

\[
D_\Gamma(G;p)=D_{\rm KL,2}(w\|\nu_p)-\log_2 Z-\Gamma(q),
\]

not merely its finite five-input tube.

The prior missing implication is universal positivity of `B-GIBBS-KL-v1` in the B-lead's low-price region, where the scalar Bellman information is insufficient and actual Boolean packet/shape information must supply the remainder.

## 1. Exact packet decomposition under a genuine coordinate restriction

Fix one input coordinate `i` with its **actual interior bias**

\[
s:=p_i\in(0,1),
\]

while the other input biases remain arbitrary and interior. Let the two genuine Boolean restrictions be

\[
G_0=G|_{x_i=0},\qquad G_1=G|_{x_i=1}.
\]

For every Fourier index `T` on the remaining coordinates write their actual biased Fourier coefficients

\[
u_T=\widehat {G_0}(T),\qquad v_T=\widehat {G_1}(T).
\]

In the normalized biased basis for the selector coordinate, the parent pair is the orthogonal weighted transform

\[
\widehat G(T)=(1-s)u_T+s v_T,
\qquad
\widehat G(T\cup\{i\})=\sqrt{s(1-s)}(v_T-u_T).
\tag{1.1}
\]

Define the **physical pair mass**, child-posterior and parent branch probability

\[
e_T=(1-s)u_T^2+s v_T^2,
\qquad
r_T={s v_T^2\over e_T},
\qquad
q_T={s(1-s)(u_T-v_T)^2\over e_T}
\tag{1.2}
\]

when `e_T>0`. Zero-mass packets are omitted. Then

\[
\sum_Te_T=1,
\qquad
\sum_Te_Tq_T=\operatorname{It}_i(G;p).
\tag{1.3}
\]

Let

\[
U_T=u_T^2,\qquad V_T=v_T^2,
\]

so `U,V` are the two actual child spectral laws and

\[
e=(1-s)U+sV.
\]

For the common Gibbs law, write

\[
x_i=2^{-a_i},
\qquad
a_i={\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad
\theta_i={x_i\over1+x_i}.
\]

Let `nu_-` be the full product Gibbs law on the remaining spectral coordinates. The KL chain rule on the **actual parent Fourier pair** gives exactly

\[
\boxed{
D(w\|\nu)
=D(e\|\nu_-)+\sum_Te_T d_2(q_T\|\theta_i).
}
\tag{1.4}
\]

The mixture identity is also exact:

\[
\boxed{
D(e\|\nu_-)
=(1-s)D(U\|\nu_-)+sD(V\|\nu_-)-\operatorname{JS}_s(U,V),
}
\tag{1.5}
\]

where the weighted Jensen--Shannon information is

\[
\operatorname{JS}_s(U,V)
=\sum_Te_T d_2(r_T\|s).
\tag{1.6}
\]

Thus no branch cost and no conditional-information term is discarded. Equations (1.1)--(1.6) use the genuine restriction spectra. On the uniform cube these coefficients of course lie on their actual Walsh lattice, but **no projection-integrality assumption is introduced** and no non-Boolean packet law replaces the source.

## 2. Sharp all-bias theorem: weighted child JS is linearly paid by the physical branch mass

The needed scalar inequality is precisely the optimal logarithmic Sobolev inequality on the asymmetric two-point space. In the normalization used here, for Bernoulli bias `s` define

\[
\kappa(s)=
{\ln((1-s)/s)\over(1-2s)\ln2},\qquad s\ne\tfrac12,
\]

with the continuous value

\[
\kappa(1/2)={2\over\ln2}.
\tag{2.1}
\]

The ratio is positive on `(0,1)` and symmetric under `s -> 1-s`.

### Lemma 2.1 — exact two-point packet inequality

For every `r,s in (0,1)`,

\[
\boxed{
d_2(r\|s)
\le \kappa(s)
\left(\sqrt{s(1-r)}-\sqrt{(1-s)r}\right)^2.
}
\tag{2.2}
\]

The endpoint cases `r=0,1` follow by continuity. The constant `kappa(s)` is sharp.

### Proof

Let `mu_s` be Bernoulli(`s`) on `{0,1}` and put

\[
f(0)=\sqrt{{1-r\over1-s}},\qquad
f(1)=\sqrt{{r\over s}}.
\]

Then `E_{mu_s} f^2=1` and, in natural logarithms,

\[
\operatorname{Ent}_{\mu_s}(f^2)
=D_{\rm KL}(\operatorname{Bern}(r)\|\operatorname{Bern}(s)).
\]

The sharp two-point logarithmic Sobolev inequality is

\[
\operatorname{Ent}_{\mu_s}(f^2)
\le
{s(1-s)\over\Lambda(s,1-s)}[f(1)-f(0)]^2,
\]

where

\[
\Lambda(s,1-s)={1-2s\over\ln(1-s)-\ln s}
\]

is the logarithmic mean. Substituting the displayed `f`, dividing by `ln 2`, and simplifying gives (2.2). The sharpness is exactly the sharpness of the two-point inequality. `QED`.

For provenance, the exact asymmetric two-point log-Sobolev constant is classical; see P. Diaconis and L. Saloff-Coste, *Logarithmic Sobolev inequalities for finite Markov chains*, Ann. Appl. Probab. 6 (1996), 695--750, DOI 10.1214/aoap/1034968224. The source computes the asymmetric two-point constant exactly. The use below is the new source-specific inference in this report, not a novelty claim for Lemma 2.1 itself.

### Theorem 2.2 — physical restriction payment at every selector bias

For packet `T`, (1.2) gives

\[
\left(\sqrt{s(1-r_T)}-\sqrt{(1-s)r_T}\right)^2
={s(1-s)(|u_T|-|v_T|)^2\over e_T}
\le q_T.
\tag{2.3}
\]

The inequality is exactly where the physical Fourier signs are retained: opposite-sign overlap makes `(u_T-v_T)^2` larger, never smaller. Apply Lemma 2.1 packetwise, multiply by `e_T`, and sum. Using (1.3),

\[
\boxed{
\operatorname{JS}_s(U,V)
\le \kappa(s)\operatorname{It}_i(G;p).
}
\tag{2.4}
\]

This is dimension free, valid for every interior selector bias, and sign safe. At `s=1/2`,

\[
\kappa(1/2)=2/\ln2=2.8853900817779268\ldots.
\]

The scalar coefficient is sharp without further cross-packet Boolean information.

## 3. Direct insertion into `B-GIBBS-KL-v1`

Let

\[
q_b=\Pr[G_b=-1],\qquad q=(1-s)q_0+s q_1.
\]

Use the fleet02/B15 Gibbs factorization on the parent and on both children. Since the remaining input-price vector is identical for the two restrictions, (1.4)--(1.5) give the **exact** defect recursion

\[
\boxed{
D_\Gamma(G;p)
=(1-s)D_0+sD_1
+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+\sum_Te_Td_2(q_T\|\theta_i)
-\operatorname{JS}_s(U,V)
-\log_2(1+x_i).
}
\tag{3.1}
\]

Because

\[
d_2(q\|\theta_i)
=a_iq+\log_2(1+x_i)-h_2(q),
\]

put the actual physical branch entropy

\[
B_i:=\sum_Te_T h_2(q_T).
\tag{3.2}
\]

Then (3.1) is equivalently

\[
\boxed{
D_\Gamma(G;p)
=(1-s)D_0+sD_1
+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+a_i\operatorname{It}_i
-B_i-\operatorname{JS}_s(U,V).
}
\tag{3.3}
\]

Applying Theorem 2.2 gives the all-bias direct residual bound

\[
\boxed{
D_\Gamma(G;p)
\ge(1-s)D_0+sD_1
+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+[a_i-\kappa(s)]\operatorname{It}_i-B_i.
}
\tag{3.4}
\]

This is a bound on the versioned common residual itself, because the B-lead/peer identity is `D_Gamma=V_q R_B`.

For the live candidate at the symmetric selector `s=1/2`,

\[
a_i=\Gamma^\dagger(1/2)=C^\dagger=6.521851214,
\]

so (3.4) specializes to

\[
\boxed{
D_{\Gamma^\dagger}(G;p)
\ge {D_0+D_1\over2}
+{\Gamma^\dagger(q_0)+\Gamma^\dagger(q_1)\over2}-\Gamma^\dagger(q)
+3.636461132222073\,\operatorname{It}_i
-B_i.
}
\tag{3.5}
\]

Thus on every genuine coordinate restriction the entire Jensen--Shannon mixing loss is now explicitly paid at the sharp two-point rate `kappa(p_i)`. No coordinate identity, branch, sign, or negative information credit was made free.

## 4. Why this does not close FEI

The theorem removes one genuine source-dependent loss, but it does not prove a credit-free bound on `B_i`. Such a bound is known to be false: the current owner state records bent-plus-one-point-flip sources with `B_i/Inf_i` growing roughly as the dimension (measured from about `2.67` to `13.44` on the recorded range). Therefore replacing `B_i` in (3.4) by `K Inf_i` with a universal `K` is a dead route.

The replacement obligation is precise. In the B-lead's low-price Bellman region, use either

1. the **retained child defects** `(1-s)D_0+sD_1`, or
2. the exact magnitude/price packet KL from `B-GIBBS-KL-v1`,

to pay `B_i` together with the displayed potential Jensen term, without discarding the conditional information already present. A credit-free interpolation is not sufficient.

## 5. Counterexample/stress test

A separate brute-force checker enumerated every Boolean truth table through `n=4` and every coordinate at the symmetric selector. It evaluates the genuine two restriction spectra and the ratio `JS(U,V)/Inf_i`. The observed maxima were

- `n=2`: `2.0000000000000000`,
- `n=3`: `2.1951797627815943`,
- `n=4`: `2.3986718134590450`,

all below the proved symmetric constant

\[
2/\ln2=2.8853900817779268\ldots.
\]

This finite computation is a stress check only; Theorem 2.2 is analytic and all-bias.

The two-point coefficient `kappa(s)` cannot be uniformly lowered packetwise without using additional cross-packet Boolean structure, because the underlying two-point log-Sobolev inequality is sharp. This is negative information about the next attack: any improvement must be global/Boolean, not another pointwise packet inequality.

## 6. Exact handoff

- **candidate_version:** `LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1`.
- **prior_missing_implication:** prove `R_B(P;p)>=0` in the low-price Bellman region for every composition-prime Boolean source.
- **new_proved_inference:** exact genuine-restriction Gibbs packet decomposition (1.4)--(1.6), sharp all-bias two-point payment (2.2)--(2.4), and the direct common-residual bound (3.4), with the symmetric numerical specialization (3.5).
- **exact_failed_claim preserved:** a universal credit-free `B_i<=K Inf_i` payment is false; no automatic packet integrality is assumed.
- **replacement_obligation:** pay the remaining physical branch entropy `B_i` from child slack or the retained magnitude/price KL in the low-price Bellman region.
- **consumed_peer_artifact:** fleet02/B15 `20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`.
- **applied_to_claim:** the exact `B-GIBBS-KL-v1` gate defect under a genuine coordinate restriction at arbitrary interior selector bias.
- **next_recipient:** fleet03/B18 (Campaign-B lead), with fleet02/B15 as the KL-credit partner.
- **remaining_implication_to_full_FEI:** universal nonnegativity of `B-GIBBS-KL-v1` for every finite arity and every interior bias; full FEI remains OPEN.
