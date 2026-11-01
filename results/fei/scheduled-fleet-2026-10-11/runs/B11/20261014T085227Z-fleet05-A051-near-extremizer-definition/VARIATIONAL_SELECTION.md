# Finite variational selection without an infinite optimizer

Finite uniform cubes; Boolean signs; all logarithms in bits. Put D_K=H-KI,
N=2^n, and a_S=fhat(S). Define the real spectral entropy potential

    G_f(x)=sum_S a_S log2(a_S^2) chi_S(x),

with 0 log(0)=0. For E subset of cube vertices let f^E flip f on E,
delta=|E|/N, and let boundary(E) consist of undirected cube edges crossing E.
Write b_K(n)=max_f D_K(f), including constants and inessential coordinates.

## 1. Admissible selection and tolerance

There are exactly 2^(2^n) truth tables, so b_K(n) is attained for every fixed
n and real K. If any K-violation exists, well-order its essential dimension,
call it n*, and choose a table maximizing D_K on the entire n*-cube. Its
deficit is positive. An inessential table could be compressed to a smaller
violator, a contradiction. Every smaller Boolean phase and every proper
physical child has nonpositive deficit. Thus ALL previous critical child
and phase banks apply, while also D_K(f^E)<=D_K(f) for every E. No optimizer
over unbounded dimension is assumed.

More generally define finite epsilon-extremality by

    b_K(n)-D_K(f)<=epsilon, epsilon>=0.

Then every vertex edit has D_K(f^E)-D_K(f)<=epsilon. This is an additive
deficit tolerance, not ratio tolerance divided by possibly tiny influence.
For a proper physical cut A the exact telescope gives

    D_K(f)=L_A-KI_A+E D_K(child).

Each child, padded if necessary, is bounded above by b_K(n-|A|). Therefore
L_A-KI_A >= D_K(f)-b_K(n-|A|). At the selected n* these finite caps are zero
(constants give zero and minimality excludes positive values). This supplies
the actual signed reserve, rather than asserting descendants remain near
maximizers. There is no claimed preservation of epsilon-extremality under
arbitrary tensor, activation or coding transformations: their exact deficit
ledgers must be used. Tensorization does give b_K(n+m)>=b_K(n)+b_K(m), by
Parseval entropy and influence additivity, so an unbounded-dimensional
deficit optimizer generally cannot be presumed once a violation exists.

## 2. A universal entropy edit inequality

Let h(t)=-t^2 log2(t^2), h(0)=0. On [-1,1], away from zero,

    h''(t)=-(2 ln(t^2)+6)/ln(2) >= -6/ln(2).

Consequently h(t)+3t^2/ln(2) is convex on [-1,1]. Its derivative extends
continuously through zero, proving convexity across zero as well. Both old
and edited Boolean Fourier coefficients lie in this interval. With
b_S=fhat^E(S)-a_S, the supporting tangent inequality implies

    H(f^E)-H(f) >= -2 sum a_S log2(a_S^2)b_S
                      -(2/ln2) sum a_S b_S -(3/ln2) sum b_S^2.

Parseval, applied to f^E-f=-2 f 1_E, gives sum a_S b_S=-2delta and
sum b_S^2=4delta. Fourier inversion identifies the first term. Hence

    H(f^E)-H(f) >= 4 E_x[1_E(x) f(x)G_f(x)] - (8/ln2)delta.       (V1)

This is valid for all Boolean tables and all E, without criticality. Zeros
in the spectrum cause no missing differentiability assumption. The constant
is a proved bound; no sharpness is claimed. Since ln2>2/3, replacing 8/ln2
by 12 gives a rationally certifiable, slightly weaker bound.

## 3. The signed cut constraint at the selected witness

Only boundary edges change their pivotal status. An edge with endpoint
product f(x)f(y) contributes change +1 when agreeing and -1 when disagreeing.
Each undirected edge contributes 2/N to influence, so exactly

    I(f^E)-I(f)=(2/N) sum_boundary(E) f(x)f(y).                   (V2)

For a finite epsilon-extremizer, combine V1, V2 and D_K(f^E)-D_K(f)<=epsilon:

    sum_(x in E) f(x)G_f(x)
        <= (K/2) sum_boundary(E) f(x)f(y)
                  +(2/ln2)|E| + N epsilon/4.                   (V3)

In particular at an exact maximizer epsilon=0, every signed vertex cut
satisfies this inequality. Let p_f(x) be the number of pivotal incident
coordinates. The singleton E={x} version is

    f(x)G_f(x)+K p_f(x) <= K n/2+2/ln2.                         (V4)

These constraints are simultaneous with every proper physical D+S bank
at the least-dimensional witness. A one-point edit is not a physical child;
finite deficit maximization is the precise reason it is allowed here.
Taking arbitrary roots to obey V3 would be false as a logical deduction;
only V1 and V2 are universal. The term N epsilon/4 also shows why a vague
near-extremizer hypothesis is insufficient for pointwise stationarity:
absolute tolerance must be o(2^-n) to make that singleton error vanish.

An exact scope guard is the three-bit parity at K=3: its spectrum is one
atom, G=0, and p_f(x)=3 at every vertex. V4 would require 9<=9/2+2/ln2,
which is false since ln2>2/3 gives the right side<15/2. This root is not
a finite deficit maximizer (its deficit is -9 while constants give zero).
Thus the new variational constraint is genuinely additional to Booleanity;
it cannot be imported into root-hardness wrappers without a selection step.

## 4. Status and next unsupported line

Finite selection and V1--V4 are proved above. They do not pay a physical
query, nor prove that G_f has a dimension-independent influence bound.
First unsupported line: use these Boolean vertex-edit inequalities together
with the complete all-block Gibbs/phase banks to select a proper block with
L_A<=K I_A on an actual positive-deficit minimal witness. Absolute collision
smallness alone does not bound G_f and cannot replace this step. The next
test should retain the signed boundary and root reserve in the same
potential-to-pair comparison; summing V4 discards the useful pointwise
information and gives only a trivial averaged inequality.
