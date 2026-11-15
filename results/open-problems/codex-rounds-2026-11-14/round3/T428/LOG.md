# T428 work log

Task: “take the NEXT checkable step on this problem, building on that work” —
15 November 2026, approximately 03:53 +04 (Asia/Tbilisi;
first recorded local clock reading).

## Orientation and bounded literature check (approximately 03:53–03:54)

Read the previous folder's REPORT.md, PROOF.md, LOG.md, verify.py and
verification.json. The old folder is read-only. New work stays here; no git,
subagents, external messages or shared-state writes. The task's folder-only
rule precludes the usual external checklist, mesh and brain-log updates.
Read the startup memory index and compute-state JSON. State: warn,
owner_away_open, CPU saturated, 67% free memory. Only scalar checks are planned,
under nice 15, with the four numerical thread settings equal to one.

Web searches, using the web tool:

- `"2609.15832" "Conjecture"`
- `"stochastic heat flow" "signed" kernels universality November 2026`
- `"Drillick" "Hou" "Parekh" "signed"`
- `"Conjecture 1.17" "heat"`

Opened the current abstract and v1 HTML of Hindy Drillick, Jonathan Hou,
Shalin Parekh, *A universality result for the critical 2d stochastic heat
flow*, https://arxiv.org/abs/2609.15832 and
https://arxiv.org/html/2609.15832v1. The abstract lists only v1; the HTML
still states the signed exponential extension as Conjecture 1.17.

Also opened the abstract and v1 HTML of Quentin Berger, Francesco Caravenna,
Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng
Sun, Li-Cheng Tsai, Zuodi Xie, Nikos Zygouras, *The Critical 2D KPZ Process*,
https://arxiv.org/abs/2610.31614 and https://arxiv.org/html/2610.31614v1.
It concerns a renormalized Cole–Hopf construction, not a stated proof of
the signed spatial-kernel conjecture. It predates the previous report.
No later resolution was located in this search of less than five minutes.
This is not a claim that the literature was exhausted.

Inspection commands: `cat` on the five old artifacts, startup memory and
compute state; `rg --files`; `date '+%Y-%m-%d %H:%M:%S %z'`.
Clock output at the end of inspection: 2026-11-15 03:53:41 +0400.

## Independent re-derivation of the earlier claim

The main claim holds on inspection. For the gap generator Delta,
S_N(r)=(4 pi)^(-1)E_1(r^2/(4N)). Independently, splitting the time integral
at 1 and differentiating its finite renormalized limit in q=r^2/4 gives
derivative -1/q and value -gamma at q=1. Thus
S_N=L/(4 pi)+g+r_N, with g=(log 4-gamma-2 log r)/(4 pi) and
0<=r_N<=r^2/(16 pi N). Exponential weights make this an operator-norm
expansion A_N=mu P+K/L+O(1/(NL)), with mu=m/(4 pi),
P=u tensor v/m, u=sqrt(|f|), v=sgn(f)u. First-order perturbation against
left vector v and right vector u gives Lambda_N=mu+I(f)/(mL)+O(L^-2).
This uses a nonorthogonal projection; no positivity of f is needed.

The nonzero spectra of the full operator and A_N coincide by the XY/YX
factorization in the old proof. The complementary operator has norm
O(1/L), so its normalized powers are uniformly small. The cutoff proof's
constants are uniform because m_R>=m/2 eventually. No defect found.

For the old signed Gaussian example, Gaussian convolution gives
4 pi H(t)=4/(t+1)-4/(t+3/2)+1/(t+2). Integrating and subtracting log N
gives -4 log(2/3)+log(1/2)=log(81/32). A fresh scalar check will be
included with the new checks rather than running the old script, which
would write verification.json in the old folder.

## Chosen extension, recorded before implementation

Prove a locally uniform operator-norm asymptotic for the Brownian signed
pair resolvent after a macroscopic Laplace transform, retaining the same
sharp-time spectral tuning Lambda_N. The proposed limiting denominator
is log z+gamma-theta. The extra gamma comes from replacing the sharp
cutoff in time by exponential damping and must be checked independently.

Why this piece: it is the transform-side part of the previous report's
next step. The explicit heat kernel allows the difference between sharp
and exponential time cutoffs to be estimated directly, preserving signed
spatial cancellations. Pointwise time inversion and higher-particle
estimates are separate issues and will not be inferred from this limit.

## First transform calculation

For w_z(s)=exp(-zs)-1_{s<=1}, direct subtraction of the two time kernels
gives (4 pi)^(-1) integral w_z(s) exp(-r^2/(4Ns)) ds/s.
The scalar integral without the spatial exponential equals
-gamma-log z: differentiation in z gives -1/z, and integration by parts
at z=1 gives -gamma. On compact subsets of Re z>0,
|w_z(s)|<=C s for s<=1 and <=exp(-delta s) for s>1.
Using 1-exp(-q/s)<=sqrt(q/s), the spatial error is bounded by C r/sqrt(N).
Its weighted Hilbert–Schmidt norm is O(N^-1/2).

This yields the Laplace operator expansion without requiring a Bessel
function asymptotic. It also identifies the gamma shift independently of
the old heat-overlap constant. The next algebraic step is a Schur
complement relative to the nonorthogonal rank-one P.

## Proof written: transform and genuine renewal interpretation

Wrote PROOF.md. A uniform rank-one spectral perturbation gives
L^-1 B_N(z)(I-B_N(z))^-1 -> P/(log z+gamma-theta), with error
O_K(1/L+|epsilon_N|), locally uniformly on Re z>0 away from the pole.
The final proof uses the spectral projection instead of a Schur complement;
both give the same scalar denominator.

The issue of identifying the inverse as an actual renewal transform is
resolved as follows. The finite-time Volterra series is exactly
R_N(t)=alpha_N M_u exp(t(Delta+alpha_N f)) M_v. For a real
x_0>exp(theta-gamma), the signed Birman–Schwinger operator B_N(x_0)
has leading eigenvalue strictly below one. Its nonzero spectrum equals
that of the self-adjoint operator
alpha_N(q-Delta)^(-1/2) f (q-Delta)^(-1/2), q=x_0/N.
The associated quadratic-form identity puts the top of Delta+alpha_N f
strictly below q. This justifies the Laplace integral in the desired
right half-plane, without interchanging an infinite signed series and
an integral through an absolute-value bound.

This proves a transform-side pair result, not a local renewal theorem.
The next task is independent scalar checks of all normalization constants,
followed by an audit of the spectral and semigroup arguments.

## Scalar verification passed

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0. Full stdout is saved as verification.json. The script uses scalar
mpmath quadrature at 45 digits, a 120-second CPU limit, and no arrays or
workers. It completed in 0.614 seconds, with peak RSS 24,592,384 bytes.
All four thread environment variables were 1. The nice command emitted
`setpriority: Operation not permitted`, as in the previous session; a direct
libc check found inherited nice 20 with errno 0, satisfying nice>=15.

Output that matters:

- The old I(f), recomputed by finite-interval Gaussian-log quadrature,
  was 0.073904652375245286251900741971235, agreeing with
  log(81/32)/(4 pi) to the 45-digit working precision (reported error 0).
- Direct quadrature of the time-cutoff difference agreed with
  -gamma-log z for z=0.5, 1, 3, 0.6+0.8i and 2+i; maximum error
  1.76e-46. In particular at z=1 the answer is -0.57721566490153286... .
- Three direct time-integral/Bessel-kernel checks, including z=2+i,
  had maximum error below 5.48e-48.
- Nine finite-N signed Gaussian heat-overlap checks, using N=100,
  10,000 and 1,000,000, agreed between direct integration and exponential
  integrals to less than 2.81e-44. Their renormalized limits agreed with
  log(81/32)-gamma-log z. For z=2, the finite-part error decreased from
  0.0201278246141 to 0.000209127970258 to 0.00000209296623793.
- Six spatial-remainder checks, with r=0.01, 2, 50, N=1000 and
  z=0.5 or 2+i, all satisfied the explicit O(r/sqrt(N)) bound.
- All close-equality assertions used tolerance 1e-34.

These are scalar normalization and remainder checks. They do not compute
Lambda_N or verify an infinite-dimensional operator limit numerically.

## Adversarial audit

Re-derived the tuned inverse independently using the splitting
H=range(P) plus ker(P), which is a bounded direct sum even though P is
not orthogonal. For M_N=I-B_N, its diagonal block on range(P) is
(d_theta-epsilon_N)/L+O(L^-2). Its two off-diagonal blocks are O(L^-1),
and the other diagonal block is identity+O(L^-1), with bounded inverse.
The scalar Schur complement therefore changes only by O(L^-2). Its
inverse divided by L tends to 1/d_theta. This independently checks the
spectral-projection calculation, including the factors m and mu:
P K_f P=(I_f/m)P, and eta=I_f/(m mu) cancels the sharp-time tuning
correction. No orthogonality or positivity of the signed operator was used.

Rechecked the operator order in the renewal identification:
Q(t-s)Q(s)=M_u exp((t-s)Delta) M_f exp(s Delta) M_v, because
M_v M_u=M_f. Thus the potential in the Duhamel series is alpha_N f,
with R_N=alpha_N M_u exp(tH_N)M_v; there is no extra alpha_N or m.
The change t=Ns in the Laplace transform supplies exactly the N/L
in (7). Applying ell(Tu)/m sends P to 1, checking the scalar normalization.

Rechecked the signed Birman–Schwinger argument by quadratic forms.
YX=alpha_N(q-Delta)^(-1/2) f (q-Delta)^(-1/2) is self-adjoint,
even though XY=B_N is not. The XY/YX resolvent identity transfers the
entire nonzero spectrum, not a norm bound. With the one eigenvalue
below 1 and all other spectrum O(1/L), I-YX is strictly positive.
This is enough to place sup spectrum(H_N)<q. It does not require
monotonicity of B_N(z) in z for signed f.

Cases checked for failure:

- The pole z_star is excluded. Compact convergence across it would be
  false; below it the algebraic continuation is not asserted to be an
  actual Laplace transform.
- For m=0 the isolated rank-one eigenvalue is absent. The theorem
  explicitly excludes that case, and constants can diverge as m tends
  to zero. Negative total mass is likewise outside the statement.
- Even for m>0, replacing f by |f| changes the leading mass and need
  not make the critical interaction series Laplace-integrable. The
  proof uses the actual signed potential and its self-adjoint form.
- Finite-time absolute convergence of the Duhamel series alone only
  gives growth exp(alpha_N ||f||_infinity t), which is insufficient at
  damping z/N. The separate spectral form estimate is necessary.
- Uniformity in z is on compact sets only. In particular there is no
  bound as |Im z| grows, Re z tends to zero, or z approaches the pole.
  No inverse Laplace convergence is inferred.
- No assertion is made for arbitrary N-dependent f, for the paper's
  general gap processes, or for third/fourth moments. The Brownian
  generator is Delta, not Delta/2.

No counterexample to the stated theorem was found. Its novelty is not
claimed. No failed numerical run occurred; the only environment warning
was the refused additional nice increment on an inherited nice-20 process.

An additional normalization check is scaling f by a positive constant b.
Then m and mu scale by b, K_f by b, I_f by b^2, while P and eta are
unchanged. Tuning alpha_N scales by 1/b, so B_N and its limiting
denominator are unchanged. This agrees with the exact definition (4).

Read the end of the earlier PROOF.md and its full verification.json once
more during the final read-only audit. Their values and stated limitations
agree with the independent re-derivation recorded above.

## Final artifact check

Wrote REPORT.md with the required first-line PARTIAL verdict. A short
read-only Python check, run with the same four thread variables and
`nice -n 15`, confirmed all five deliverables are present and nonempty,
the first-line verdict has the required form, verification.json parses,
reported nice>=15, RSS<1 GB and all thread settings equal one. Output:
`Artifact checks passed; numerical run was not repeated.` The final
proof edit only makes the complex Bessel identity's analytic continuation
explicit; it does not change the theorem or require another numerical run.

Completed one piece: the fixed-profile Brownian signed pair-renewal
Laplace theorem, with original spectral tuning. Full Conjecture 1.17
remains open in this report.
