# E0025 — partial result, 12 October 2026

The question is whether every driftless subordinator with infinite Lévy measure satisfies (H): every semipolar set is polar. The general question is not solved here. In the source, “pure jump subordinator” explicitly means drift d=0 (PDF p. 11); merely removing the Gaussian part would permit deterministic drift and would change the question.

## Construction (initial proposal, subsequently proved below)

Set r_n=2^(-16^n), n≥1, and

ρ(x)=1_(0,1](x) x^(-5/4) + Σ_(n≥1)1_[r_n,2r_n](x) x^(-7/4).

The blocks are disjoint. Thus x^(-5/4)≤ρ(x)≤2x^(-7/4) on (0,1]. The driftless subordinator is of type-(1/4,3/4). The planned proof has two parts:

1. At z_n=r_n^(-1/2), A(z_n)=1+Re ψ(z_n) is comparable to r_n^(-1/8), whereas |Im ψ(z_n)| is comparable to r_n^(-1/4). This violates Kanda–Forst and, using monotonicity of f and the fixed geometric relation between log A(z_n), every divergent-integral Rao bound.
2. On [r_n^(-4),r_n^(-5)], B=|1+ψ|≤K A, uniformly. By choosing y_n=D r_n^(-1), the B-windows [y_n,y_n^(9/8)) are contained in those good frequency bands. The finite-energy criterion, survey Theorem 2.11, then proves (H), since Σ1/log y_n<∞.

The complete proofs and referee audit below establish these statements.

## Complete proof of the special case

All comparability constants below are positive and independent of n and z. Their values may change between displays. Only finitely many initial n are discarded. Write

ψ(z)=∫_0^1(1-e^(izx))ρ(x)dx, R=Re ψ, I=-Im ψ=∫sin(zx)ρ(x)dx,
A=1+R, B=|1+ψ|=(A²+I²)^(1/2).

### 1. Measure and elementary estimates

r_(n+1)=r_n^16 and 2r_(n+1)<r_n, so the blocks are disjoint. The stated density bounds hold with c=2 in Definition 2.28. The base has infinite mass but finite first moment ∫_0^1 x^(-1/4)dx=4/3. For a block define

M_n=∫_(r_n)^(2r_n) x^(-7/4)dx = m r_n^(-3/4), m=(4/3)(1-2^(-3/4)),
L_n=∫_(r_n)^(2r_n) x^(-3/4)dx = l r_n^(1/4), l=4(2^(1/4)-1),
Q_n=∫_(r_n)^(2r_n) x^(1/4)dx = q r_n^(5/4), q=(4/5)(2^(5/4)-1).

Since r_n≤2^(-16), every successive ratio for L_n and Q_n is at most 1/2, and M_n/M_(n+1)≤1/2. The geometric-series estimate therefore gives, for n≥2,

Σ_(k≤n) M_k≤2m r_n^(-3/4),
Σ_(k<n) M_k≤2m r_(n-1)^(-3/4)=2m r_n^(-3/64),
Σ_(k>n) L_k≤2l r_(n+1)^(1/4)=2l r_n^4,
Σ_(k>n) Q_k≤2q r_(n+1)^(5/4)=2q r_n^20.

In particular ΣL_n<∞. Hence ∫(1∧x)ρ(x)dx<∞, and this is a valid infinite Lévy measure of a driftless, unkilled subordinator. For each fixed z the exponent series converges absolutely, since |1-e^(izx)|≤|z|x.

Let ψ_0 be the base exponent. For z≥1, splitting the integral at 1/z and using |1-e^(it)|≤min(2,|t|) gives

|ψ_0(z)|≤(4/3+8)z^(1/4)=C_0 z^(1/4).

For z≥2, integrating its real part on [1/z,2/z] gives

R_0(z)≥c_0 z^(1/4), c_0=(1-cos1)∫_1^2 u^(-5/4)du>0.

Indeed 1-cos u≥1-cos1 on [1,2]. Every other real contribution is nonnegative, so R≥R_0. Negative z are handled by complex conjugation.

### 2. Large ratios at z_n=r_n^(-1/2)

The n-th block has zx∈[√r_n,2√r_n]⊂[0,1]. On this interval sin t≥t/2 and 1-cos t≤t²/2. Consequently its sine contribution is at least (l/2)r_n^(-1/4), and its real contribution is at most (q/2)r_n^(1/4). The later blocks also have phases in [0,1], so their sine contributions are nonnegative. The earlier sine contributions have absolute total at most Σ_(k<n)M_k. Even allowing the base sine contribution its worst sign,

I(z_n)≥(l/2)r_n^(-1/4)-C_0r_n^(-1/8)-2m r_n^(-3/64).

The two subtracted terms divided by r_n^(-1/4) tend to zero. Thus I(z_n)≥c r_n^(-1/4) eventually. The reverse absolute bound follows from |sin t|≤min(1,|t|), the same coarse bound, and
z_n(L_n+Σ_(k>n)L_k)≤l r_n^(-1/4)+2l r_n^(7/2).
Therefore |I(z_n)| is comparable to r_n^(-1/4).

For the real part, the earlier blocks contribute at most 2Σ_(k<n)M_k and the later blocks at most (z_n²/2)Σ_(k>n)Q_k. Hence

c_0r_n^(-1/8)≤R(z_n)≤C_0r_n^(-1/8)+4m r_n^(-3/64)+(q/2)r_n^(1/4)+q r_n^19.

Because 3/64<1/8, the right side is at most C r_n^(-1/8). In particular A_n:=A(z_n) is comparable to r_n^(-1/8), and |I(z_n)|/A_n is comparable to r_n^(-1/8) and tends to infinity. This disproves the Kanda–Forst bound for this process, not (H).

### 3. Failure of every Rao bound of Theorem 2.3

Suppose a positive increasing f satisfied B(z)≤A(z)f(A(z)) for all z. Part 2 forces f(A_n)≥B(z_n)/A_n≥c A_n eventually. Also A_n is eventually strictly increasing: its lower bound at n+1 divided by its upper bound at n tends to infinity, since r_(n+1)=r_n^16. Its growth satisfies

log(A_(n+1)/A_n)≤C log(1/r_n).

For t∈[A_n,A_(n+1)], monotonicity implies f(t)≥c A_n. Therefore

∫_(A_n)^(A_(n+1)) dt/(t f(t))≤log(A_(n+1)/A_n)/(c A_n)
≤C log(1/r_n) r_n^(1/8)=C (16^n log2) 2^(-16^n/8).

The series of these bounds converges: writing t=16^n/8, the inequality t≤2^(t/2) holds eventually, so t2^(-t)≤2^(-t/2), which is bounded by a geometric sequence in n. The intervals cover a tail of [1,∞). Thus the required divergent integral cannot hold. No choice of f from Rao's theorem works for this process.

### 4. Uniform good frequency bands

Let G_n=[r_n^(-4),r_n^(-5)]. For z∈G_n, bound the earlier and n-th blocks by twice their mass and later blocks by z times their first moments:

|ψ(z)|≤C_0 z^(1/4)+4m r_n^(-3/4)+2l z r_n^4.

The second term is at most 4m z^(1/4), because z≥r_n^(-4) and r_n^(-3/4)≤r_n^(-1)≤z^(1/4). The third term is at most 2l z^(1/4): its ratio to z^(1/4) is z^(3/4)r_n^4≤r_n^(-15/4)r_n^4=r_n^(1/4)≤1. Thus |ψ(z)|≤C_G z^(1/4) on every G_n. Since A≥c_0 z^(1/4),

B(z)≤1+|ψ(z)|≤K A(z)

for one constant K and all z with |z|∈G_n. This estimate does not require monotonicity of A or B.

### 5. Choosing B-windows without assuming monotonicity

For every 0≤z≤r_n^(-4), including z<1, the same split at n gives

|ψ(z)|≤C_0 max(1,z^(1/4))+4m r_n^(-3/4)+2l z r_n^4≤C_* r_n^(-1).

The base estimate for z<1 follows directly from its finite first moment. It follows that B(z)≤D_0 r_n^(-1) throughout this interval, for a fixed D_0. Choose D>max(D_0,1), and y_n=D r_n^(-1). Put s=9/8.

If y_n≤B(z)<y_n^s, then |z|>r_n^(-4). On the other hand B≥A≥c_0|z|^(1/4), so

|z|<(y_n^s/c_0)^4=c_0^(-4)D^(4s) r_n^(-4s).

Since 4s=9/2<5, this upper bound is ≤r_n^(-5) for all sufficiently large n. Thus the entire set {z:y_n≤B(z)<y_n^s} lies inside {|z|∈G_n}. No frequencies outside G_n with the same B-values have been ignored.

### 6. Finite-energy criterion and (H)

We invoke Hu–Sun's survey Theorem 2.11(i), PDF p. 7, which restates Hu–Sun (2016), Theorem 2.3. It assumes lower semicontinuity of all 1-excessive functions. This hypothesis holds here: R(z)≥c_0|z|^(1/4) for |z|≥2 implies |exp(-tψ(z))|≤exp(-tc_0|z|^(1/4)), integrable for every t>0. Fourier inversion gives bounded continuous transition densities. Tonelli then gives resolvent densities (possibly infinite pointwise) with respect to Lebesgue measure. The equivalence between resolvent densities and lower semicontinuity of all 1-excessive functions is Hawkes's Theorem 2.1, cited explicitly on survey p. 4. Thus every hypothesis of Theorem 2.11 is met.

Let η be any finite measure of finite 1-energy, namely

E(η)=∫_R A(z)/B(z)² |η̂(z)|² dz<∞

(the normalization constant in Fourier energy is immaterial). On the selected window B≤KA, hence

1/(B log B)≤[K/log y_n] A/B².

Integrating over the window and summing gives

Σ_(n≥N) ∫_{y_n≤B<y_n^s} |η̂(z)|²/(B log B)dz
≤K E(η) Σ_(n≥N)1/log y_n<∞,

because log y_n=log D+16^n log2 and Σ16^(-n)<∞. Discard the finitely many n<N and reindex the sequence, so its first value is >1. It is strictly increasing and tends to infinity. The same sequence works for every finite-energy η, a stronger statement than required. Theorem 2.11(i) now proves (H).

This is a complete proof of one explicit type-(1/4,3/4) special case satisfying (H) despite failing every Rao bound. It is an application of existing theorems, with no claim of novelty or of a solution in print to Question 5.

## Referee audit and remaining gap

* “Pure jump” is driftless here, not simply Gaussian-free. All processes in this construction are explicitly driftless.
* The density is bounded above by 2x^(-7/4), because the spike intervals are disjoint. Finite first moment and infinite activity were checked independently.
* Coarse phases at z_n need not be accurately computed: absolute mass bounds handle them without assuming favorable cancellation. Later sine phases are ≤1, which is needed for their sign.
* Failure of a sufficient condition is never used as failure of (H). Part 6 proves (H) separately.
* The B-window inclusion uses a global low-frequency bound and a global lower bound for R. It does not assume that the Fourier exponent is monotone.
* The theorem's resolvent-density hypothesis, the finite-energy weight, its quantifier over all finite-energy measures, and the convergence of the sum are checked explicitly.
* Lean checks only the algebraic reciprocal comparison and exponent margins, not the analytic argument or the cited theorems. Numerical tests below are supplementary.
* The earlier brain example's point-polarity heuristic is not adopted. Even polarity of all singleton sets would not establish (H) for all semipolar sets.

The remaining gap is precise: for an arbitrary driftless infinite-activity subordinator, neither resolvent densities nor a sequence of B-windows with this uniform finite-energy control has been established. The present proof relies on the prescribed wide gaps r_(n+1)=r_n^16 and the stable base lower bound. An arbitrary type-(α,β) density need not have such good bands. For the more general n-dimensional question there is no reduction here removing these obstacles. We have no proof or counterexample for either universal statement.

## Supplementary numerical checks

`check_bounds.py` runs at 100 decimal digits and saves `numerical_checks.json`. It evaluates only the n-th block by quadrature after scaling x=r_n u, u∈[1,2]. All earlier blocks are bounded by their total mass; no attempt is made to numerically resolve astronomical coarse phases. Later blocks are bounded by first and second moments. The truncated stable base differs from the full stable exponent 4Γ(3/4)(-iz)^(1/4) by at most 8 in modulus, giving supplementary brackets.

For n=2, the computed logarithms to base 10 of the lower/upper ratio brackets are 8.855998084737847 and 8.855998183967236. For n=3, the displayed logarithm is 153.350396102271291. Equal printed endpoints at later n reflect the output precision, not an exact equality. Normalized own-block sine and real terms tend to l=0.756828460010884267 and q/2=0.551365692002176853. The computed upper bounds for B/A at five positions in each good band are below 33 for n=1,…,5. These checks are numerical evidence only, not interval-arithmetic certificates; the analytic inequalities above supply the proof.

During numerical auditing, integrating the exponentially tiny own-block integrands directly made adaptive quadrature stop before obtaining relative accuracy. Dividing the sine integrand by its small phase, and the real integrand by its squared phase, before quadrature corrected this. The final saved script uses that normalization. The mathematical proof did not depend on either numerical version.

## Lean check

`Weights.lean` passed `lake env lean` from ~/lean_verify (exit code 0; see lean_check.txt). The checked statements are the real reciprocal-weight comparison used in section 6 and five exact rational inequalities used for exponent margins. No `sorry` or `native_decide` occurs. The first run needed an explicit Mathlib.Data.Real.Basic import; the second rejected a redundant ring tactic after field_simp had already closed the goal. Both were corrected in the final passing version. This check does not formalize the analytic or probabilistic theorems.

## Second attempt (12 October 2026)

The complete continuation is in SECOND_ATTEMPT.md. It records two new approaches, proves a moment-separation theorem and an arbitrary-pulse special case for every 0<alpha<beta<1, and proves obstructions to both this criterion and direct stable-reference path equivalence. The general question remains unresolved. The remaining gap and referee checklist appear at the end of that file.
