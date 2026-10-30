# A fixed controller reserve cannot pay every seed stopping history

This corollary uses the protected-tag separation in PROOF.md. The bent
one-point-flip local obstruction is prior work (ERASURE_RIGIDITY section2
and B05); no priority is claimed for that seed alone. The application here
is an exact all-C obstruction to replacing the surviving beta V_C(h) by
one fixed controller reserve, even on an actual Boolean FEI-bounded family.

Fix ANY finite C>=0. Choose an even m>=max(2,C+6), N=2^m, delta=1/N.
On the binary m-cube let g=(-1)^(y0*y1+y2*y3+...), let h equal g with
only its origin flipped, and let f(z,y) have children g and h. All three
functions are Boolean. The Walsh transform of each two-bit factor of g
has four entries +/-2. Tensor multiplication proves, in EVERY even m,
that the raw transform of g has entries +/-sqrt(N). The origin flip
subtracts2 from every entry, so the split midpoint A=(g+h)/2 has raw
transform w_s-1 and the difference B=(g-h)/2 has constant raw transform1.
Thus ||A||^2=1-delta and ||B||^2=delta; B's normalized spectrum is uniform.

Write q for A's normalized squared spectrum. Direct expansion, using
sum_s w_s=N and w_s^2=N, gives

    sum_s(w_s-1)^2=N(N-1),
    sum_s(w_s-1)^4=N(N-1)(N+3),
    chi^2(q,Uniform)=4/(N-1).

The two moment identities hold for every even m by the displayed flat
Walsh formula, not by extrapolation from the finite validation list.
For any probability law, Jensen and ln(1+x)<=x give
D_2(q||Uniform)<=chi^2(q,Uniform)/ln2. Therefore

    H(f)=h2(delta)+(1-delta)H(q)+delta*m
        >=m+h2(delta)-4delta/ln2.

Each child has at most N Fourier atoms, so (H(g)+H(h))/2<=m. Since
h2(delta)>delta*log2(1/delta)=m delta, its selector query satisfies

    Delta_z H(f)-C Inf_z(f) > delta*(m-C-4/ln2) > 0.       (1)

Here Inf_z=delta exactly. The positive-series identity
ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3 proves4/ln2<6,
so the chosen m makes the right side positive with no floating comparison.
The series converges absolutely (ratio bounded by1/9), justifying the
positive tail; the logarithm identity follows by integrating the uniformly
convergent geometric series on[0,1/3]. Every denominator N,N-1,ln2 is positive.

This is not an FEI counterfamily. At the origin g and all its neighbors
equal1. Flipping it increases each child's data influence from1/2 to
1/2+2delta. Hence

    I(f)=m/2+(m+1)delta,
    H(f)<=m+1<=3 I(f), m>=2.

Now take t disjoint copies, f^tensor t. Query just the t selector bits,
in any fixed order, then STOP and retain the full tensor of g/h terminal
spectra. Spectral entropy and physical influence add over disjoint tensor
factors, so the total stopped signed cost is EXACTLY

    t*[Delta_z H(f)-C delta],

which tends to infinity by(1), while H(f^tensor t)<=3 I(f^tensor t).
There is no sum/integral interchange or infinite tree: for each t the
tree has depth t; the displayed divergence is a scalar positive multiple
of t. This is a reproducible actual Boolean family for every fixed C.

For ANY fixed ternary controller mask with beta=E B^2>0, use
F_t=A+B ell f^tensor t. Query the seed selectors only and stop. The
protected-tag identity multiplies their cost by beta. Thus NO finite
controller-only reserve, depending on A,B,C but independent of the seed
and t, can pay every such history after rate-C influence has been charged.
This conclusion already follows from these particular deterministic
histories; it requires neither optimizing over histories nor ignoring a
child terminal. At beta=0 it does not apply, as the seed is absent.

For A079's fixed mask, G=A+B ell has H(G)<=5 and I(G)=5/2. Its fixed
overhead also satisfies H(G)<=3I(G), so EVERY F_t above obeys H(F_t)<=3I(F_t).
The failed assertion is therefore the all-history fixed-reserve shortcut,
not FEI or a stopping theorem that retains an unused seed-dependent bank.

The correct choices are to retain beta V_C(h) as in PROOF.md, or to select
a history with a justified seed-dependent payment. An arbitrary inherited
reference and its conversion costs still require a separate proof. The
next useful collision is a chosen tag exposure with both A+Bh and A-Bh
terminals, not a demand that one constant reserve pay every seed history.
