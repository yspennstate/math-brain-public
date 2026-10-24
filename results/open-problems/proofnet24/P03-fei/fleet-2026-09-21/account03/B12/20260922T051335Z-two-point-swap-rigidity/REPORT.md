# account03/B12 — every balanced two-point truth-table swap lowers the Numaro center ratio

**Run:** `20260922T051335Z-B12-fei-gate-r11`  
**Common candidate:** `LIMIT-PRIME-GATE-LIFT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and completed peer result consumed

The current natural-language owner control supersedes B12's older spectral-code wording and asks every FEI worker to converge on the all-gate inequality. The currently shared post-falsifier candidate, as fixed by account03/B18, is

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{RO}(p)+0.2682048\,p(1-p),
\]

with unpaid universal implication

\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.1}
\]

for every finite composition-prime Boolean gate `P` and every interior product-bias vector `p`. Full FEI would follow from (1.1) by the exact gate-composition cocycle.

This run substantively consumes the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T004252Z-gate-margin-repair/REPORT.md`

(report blob `cf92d6d1219b6ba4ee048b90205024c8075b41df`). That report proves the exact defect/Poincare composition law, constructs the Numaro-scale quadratic repair, and stress-tests the published balanced 18-variable Numaro gate by only **5,000 sampled balanced two-point truth-table swaps**. No sampled swap beat the seed, but the report explicitly labels this finite evidence rather than a local-optimality theorem.

The source gate has truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

\[
I_0=\frac{261}{128},\qquad E_0:=I_0-1=\frac{133}{128},
\]

and certified entropy interval

\[
6.776605309005978082519790221891882314787235038
\le H_0\le
6.776605309005978082519790221891882314787235039.
\tag{1.2}
\]

At the balanced/unbiased center, the all-gate target is exactly the ratio `H/(I-1)`. The old missing finite inference attacked here is therefore:

> Can **any** balanced two-point truth-table swap of the full 18-variable Numaro gate increase `H/(I-1)`?

There are
\[
2^{17}\cdot2^{17}=17,179,869,184
\]
such swaps, so direct enumeration is unnecessary if the Walsh update is compressed correctly.

## 2. Exact Walsh update for a balanced swap

Let `N=2^18`, let
\[
A_S=\sum_x f(x)\chi_S(x)
\]
be the unnormalised Walsh numerator, and choose `x` with `f(x)=+1` and `y` with `f(y)=-1`. The balanced swap changes `f(x)` to `-1` and `f(y)` to `+1`. Put `d=x\oplus y`. Then

\[
A'_S-A_S=-2\chi_S(x)+2\chi_S(y)
=2\chi_S(x)(\chi_S(d)-1).
\tag{2.1}
\]

Hence
\[
A'_S=
\begin{cases}
A_S,&\chi_S(d)=+1,\\
A_S-4\chi_S(x),&\chi_S(d)=-1.
\end{cases}
\tag{2.2}
\]

This converts every two-point swap into three Walsh-Hadamard lookups.

For any scalar coefficient cost `g(A)`, define
\[
u_+(S)=g(A_S-4)-g(A_S),\qquad
u_-(S)=g(A_S+4)-g(A_S),
\]
\[
C_S=\nu_+(S)+\nu_-(S),\qquad B_S=\nu_+(S)-\nu_-(S).
\]
Writing `\widehat C,\widehat B` for the unnormalised Walsh transforms over the subset index `S`, (2.2) gives the exact identity
\[
\boxed{
\Delta G(x,y)=\frac14\left[
\sum_S C_S-\widehat C(d)+\widehat B(x)-\widehat B(y)
\right].
}
\tag{2.3}
\]

Thus a nominally 17-billion-pair local search factors into three arrays of length `N`.

## 3. Exact influence increment and a universal positive tax

For influence use
\[
g_I(A_S)=|S|A_S^2/N^2.
\]
Multiplying by `N^2`, the two possible coefficient increments are
\[
|S|[(A_S-4)^2-A_S^2]=|S|(16-8A_S),
\]
\[
|S|[(A_S+4)^2-A_S^2]=|S|(16+8A_S).
\]
So in numerator units
\[
C^{I}_S=32|S|,\qquad B^{I}_S=-16|S|A_S.
\tag{3.1}
\]
Equation (2.3) is therefore an **exact integer** formula for every swap's influence change.

Taking the minimum of the `d` term over all `d\ne0`, the minimum `B` term over all positive truth-table rows, and the maximum over all negative rows gives
\[
4N^2\Delta I\ge 33,554,432.
\]
Consequently every balanced two-point swap obeys the exact universal bound
\[
\boxed{\Delta I\ge\frac1{8192}>0.}
\tag{3.2}
\]

This already shows that no balanced swap can preserve the seed's unusually low influence.

## 4. Rigorous entropy enclosure without enumerating swaps

For an integer Walsh magnitude `z`, define its entropy contribution
\[
h_z=\frac{z^2}{N^2}\log_2\frac{N^2}{z^2}
=\frac{2z^2}{N^2}\log_2\frac Nz,
\qquad h_0=0.
\tag{4.1}
\]
Only 32 magnitudes occur among `|A_S|`, `|A_S-4|`, and `|A_S+4|` for this source gate. Each `h_z` is enclosed using rational arithmetic only. Write `N/z=2^e m`, `1\le m<2`, and
\[
t=\frac{m-1}{m+1}.
\]
Then
\[
\ln m=2\sum_{j=0}^{r-1}\frac{t^{2j+1}}{2j+1}+R_r,
\qquad
0\le R_r\le
\frac{2t^{2r+1}}{(2r+1)(1-t^2)}.
\tag{4.2}
\]
The checker uses `r=50`, applies the same enclosure to `ln 2`, and converts the resulting exact fractions to fixed-point scale
\[
M=10^{12}.
\]
For each `S`, it stores separate integer **upper** bounds for
\[
h_{|A_S-4|}-h_{|A_S|},\qquad
h_{|A_S+4|}-h_{|A_S|}.
\]
Equation (2.3) can then be applied to these upper bounds: whichever sign a given pair selects, the selected fixed-point increment still dominates its true entropy increment. This gives an upper bound `H_4(x,y)/(4M)` for every `\Delta H(x,y)`.

The same rational table yields the source lower bound
\[
H_0\ge\frac{6,776,605,309,005}{10^{12}}.
\tag{4.3}
\]
This deliberately coarse truncation is already more than sufficient.

## 5. Theorem: strict local optimality under all balanced two-point swaps

A swap increases the balanced center ratio exactly when
\[
\frac{H_0+\Delta H}{E_0+\Delta I}>\frac{H_0}{E_0},
\]
i.e. when
\[
T:=E_0\Delta H-H_0\Delta I>0.
\tag{5.1}
\]

Using the entropy upper arrays, the exact influence arrays, and the lower bound (4.3), multiply an upper bound for `T` by the positive factor `512MN^2`. It again factors as
\[
D(d)+U(x)-U(y).
\tag{5.2}
\]
The checker evaluates only the three length-`N` transform arrays and then takes the independent safe maxima/minima over
\[
d\ne0,\qquad f(x)=+1,\qquad f(y)=-1.
\]
The resulting exact integer bound is
\[
512MN^2T\le
-9,660,085,769,520,308,813,824<0.
\tag{5.3}
\]
Equivalently,
\[
\boxed{
T\le -\frac{2,249,163,987,469}{8,192,000,000,000,000}
<-2.74556\times10^{-4}.
}
\tag{5.4}
\]

### Theorem 5.1
For the published balanced 18-variable Numaro gate `f`, **every** pair `x,y` with `f(x)=+1`, `f(y)=-1` satisfies
\[
\boxed{
\frac{H(f^{x\leftrightarrow y})}{I(f^{x\leftrightarrow y})-1}
<
\frac{H(f)}{I(f)-1}.
}
\tag{5.5}
\]
Moreover every such swap raises total influence by at least `1/8192`.

Thus all `17,179,869,184` balanced two-point truth-table neighbors are eliminated simultaneously. This upgrades account04/B17's 5,000-swap numerical stress test to a rigorous complete local-optimality theorem.

The argument does **not** enumerate all neighbors and does not extrapolate from a sample: (2.3), rational entropy enclosures, and the three global transform extrema imply (5.5) for the whole family.

## 6. Independent regression check of the transform identity

As a guard against a sign error in (2.3), four deterministic random balanced swaps were also rebuilt by direct full integer Walsh transforms. Their direct and factorised influence changes agreed exactly. Their direct/factorised floating entropy increments agreed within `2e-15`:

- `(x,y)=(186374,260073)`: `Delta H≈8.5836808257e-4`, `Delta I=1/4096`;
- `(234704,228305)`: `Delta H≈8.0943697330e-4`, `Delta I=7/32768`;
- `(233287,90748)`: `Delta H≈7.5262080277e-4`, `Delta I=3/16384`;
- `(150405,172535)`: `Delta H≈8.6968012352e-4`, `Delta I=15/65536`.

These checks are regression evidence only; the proof is the exact/rational calculation above.

## 7. What changed and what remains

**Exact candidate version:** `LIMIT-PRIME-GATE-LIFT-v1`, `C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`.

**Prior missing implication applied:** account04/B17 left the balanced two-point truth-table neighborhood of the n=18 prime gate checked only on 5,000 samples.

**New proved inference:** every one of the 17,179,869,184 balanced two-point swaps strictly lowers `H/(I-1)`, with the uniform score certificate (5.4) and exact influence tax (3.2).

**Replacement obligation / universal gap:** this is a finite local rigidity theorem around one exact gate. It does **not** prove (1.1) for arbitrary composition-prime gates or arbitrary product biases. In particular the most direct remaining attack is the one already identified by account01/B18: keep this exact prime gate and optimize genuinely nonuniform bias vectors, where the full shape of `Gamma_*` matters. A second adversarial direction is truth-table Hamming distance four or greater, but another local radius should not be mistaken for universal closure.

**Next recipient:** `account03/B18` (Campaign-B lead), with the implication that the balanced Numaro center has no improving Hamming-distance-two neighbor and that direct falsification effort should move to nonuniform biases rather than more sampled balanced swaps.

**Full FEI remains OPEN / NOT PROVED.**

## 8. Provenance and scope

The source truth table is reconstructed from the already archived external Numaro slices and accepted only after matching the published SHA-256 above. This is external-source recovery, not a priority claim. The new contribution is the exact swap-transform identity applied to the source gate and the rigorous global extrema certificate.

No email, Drive, public posting, workflow dispatch, paid model/API/Codex call, scheduler mutation, permission change, credential access, or unrelated private-data access was used. Native research-brain retrieval was not available in this invocation, so the run remains `WITHOUT_VERIFIED_BRAIN`.
