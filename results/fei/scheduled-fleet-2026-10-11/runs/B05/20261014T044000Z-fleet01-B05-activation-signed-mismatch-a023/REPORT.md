# B05 / A023 — fair activation falsifies the sharp signed-mismatch refund

**Run:** `20261014T044000Z-fleet01-B05-activation-signed-mismatch-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B05-A023-ACTIVATION-SMR-v1`  
**Status:** exact activation recurrence proved; `SMR_{2,1/4}` exactly refuted  
**Full FEI:** **OPEN**

## Frozen candidate and its GU implication

Write

\[
B=\sum_iB_i,\qquad M=\sum_i(K_i-\Gamma_i)=G-B,
\]

and for `c>=0`, `eta>0` put

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f).
\]

The preceding B01 reduction proves that the universal estimate
`L_{c,eta}<=0` implies

\[
G(f)\le(c+2)I(f)+(1-\eta)U(f)-2\operatorname{Var}(f).
\]

The frozen candidate was

\[
\boxed{L_{2,1/4}(f)=M(f)+\frac54U(f)-2I(f)\le0.}\tag{SMR}_{2,1/4}
\]

Had it held universally, it would have given GU `(a,b)=(4,3/4)`, then
`U<=16I` and `H<=34I` by the source-reviewed induction.  This run gives an
exact genuine-Boolean falsifier to this sufficient inequality.  It does
**not** falsify GU `(4,3/4)` or FEI.

## Exact fair-activation recurrence

For a Boolean core `q` with mean `m`, define the fresh fair activation

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

Let `p_i=hat q({i})^2`,

\[
T(a,b)=a\log_2\frac{a+b}{a}+b\log_2\frac{a+b}{b},
\]

with zero terms omitted, and use the reviewed scalar identity

\[
U(A(q))=\tfrac12U(q)+R(m).
\]

For `m_i^sigma=E(q|x_i=sigma)`, put

\[
D_R(q)=\sum_i\left[R(m)-\frac{R(m_i^+)+R(m_i^-)}2\right],
\quad J(m)=\frac{1-m}{2},
\]

\[
B_z(m)=\frac{1-m^2}{2}
+\frac14T((1+m)^2,(1-m)^2),
\]

and

\[
C_i(m,p_i)=-\frac12T(m^2,p_i)
+\frac14T((1+m)^2,p_i)+\frac14T((1-m)^2,p_i).
\]

Direct Fourier pairing proves

\[
B(A(q))=\tfrac12B(q)+B_z(m)+\sum_iC_i(m,p_i),
\]

while the exact restriction identity gives

\[
G(A(q))=\tfrac12G(q)+R(m)+D_R(q),\qquad
I(A(q))=\tfrac12I(q)+J(m).
\]

Therefore

\[
\boxed{
L_{c,\eta}(A(q))=\frac12L_{c,\eta}(q)+\mathcal A_{c,\eta}(q)
}
\]

where the complete signed activation charge is

\[
\boxed{
\mathcal A_{c,\eta}(q)=D_R(q)+(2+\eta)R(m)-B_z(m)
-\sum_iC_i(m,p_i)-cJ(m).
}\tag{A}
\]

This is the requested nonreusing node ledger: the selector entropy,
upper-set curvature, singleton orbit corrections, child residual and
physical pivotal reserve all occur exactly once.  It permits a changing
core `q`; no disjoint terminal-core cancellation is used.

## Exact falsifier

Take the four-bit Boolean sign whose `+1` truth-table positions are encoded
by mask `56242` (least-significant bit is input zero):

```text
-+--++-+++-++-++
```

equivalently the truth string is `-+--++-+++-++-++`.  It has

\[
U(q)=I(q)=2,\quad B(q)=4,\quad G(q)=\frac{11}{2},
\quad M(q)=\frac32,
\]

so `L_{2,1/4}(q)=0` exactly.  Its five-bit activation has truth string

```text
-+++-+-+++++-+++++++-+++++-+++++
```

and

\[
\begin{aligned}
U(A(q))&=1.8381083242053355\ldots,\\
I(A(q))&=\frac{11}{8},\\
B(A(q))&=3.3369990984052342\ldots,\\
G(A(q))&=3.8817072476492810\ldots,\\
M(A(q))&=0.5447081492440469\ldots.
\end{aligned}
\]

Consequently

\[
\boxed{L_{2,1/4}(A(q))=0.092343554500715\ldots>0.}
\]

The exact node pieces are

\[
m=\tfrac14,\ R(m)=0.8381083242\ldots,\ D_R=0.2935989234\ldots,
\]

\[
B_z=0.9116876070\ldots,\ J=\tfrac38,\
\sum_iC_i=0.4253114914\ldots.
\]

Thus the entire debt is created by one fair activation of an equality core;
there is no child slack to reuse at the sharp constant.

`certify_activation_falsifier.py` represents the residual as a rational
linear combination of base-two logarithms.  Multiplying by the common
coefficient denominator `256` reduces positivity to one exact integer-product
comparison over 13 rational log bases.  The positive and negative sides have
9,253 and 9,229 bits respectively, and the exact comparison is strict.  The
same routine certifies the child residual as exact equality.

The witness forces any inequality of the same form with `eta=1/4` to have

\[
c\ge\frac{M(A(q))+(5/4)U(A(q))}{I(A(q))}
=2.0671589487277937\ldots.
\]

This is only a lower bound on that proof family, not a proposed universal
constant.

## Bounded checks and scope

`check_activation_smr.py` independently reconstructs Walsh spectra and the
activation recurrence.  It checks all 278 Boolean signs in dimensions zero
through three and 1,000 deterministic random four-bit cores (seed
`2026101405`).  The largest recurrence discrepancy was below `4.5e-15`.
The exact falsifier appeared in the four-bit sample.  These finite checks are
corroborative; the recurrence and sign certificate are analytic/exact.

The earlier natural coordinate allocation was already false.  This run
advances the obstruction: the aggregate sharp candidate itself is false,
even under one fresh fair activation.  The result removes the need to study
reused physical coordinates for this particular constant; reuse cannot repair
a one-step genuine-Boolean failure.

## Remaining universal gap and next move

Universal GU remains open.  The next A023 attempt should retain formula (A)
but introduce an explicit global reserve, for example a larger `c` or a
separate terminal slack, and prove that the reserve is single-use under
changing cores.  It must be tested first on this equality-core activation and
on the four-bit tensor equality family.  Merely increasing `c` from a finite
maximum is not a proof.

No independent review has been performed.  No protected source, paid compute,
public release, scheduler mutation, or subagent was used.  Exposed model:
Codex; reasoning effort metadata: UNKNOWN.

