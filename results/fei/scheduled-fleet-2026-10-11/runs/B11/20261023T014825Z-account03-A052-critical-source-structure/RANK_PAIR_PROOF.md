# A rank formula for usable affine release and a paid original pair

Finite uniform cubes; Boolean signs; Fourier entropy uses bits. This is
a lower-funding interface and a local paid step, not full FEI.

## 1. Exact rank formula; overlapping exchanges cannot be added

Let g be a d-bit Boolean function, p_j=Inf_j(g), and let its squared
Fourier label be S. For a nonzero parity vector v put

    w(v)=P(v dot S=1), m(v)=min(w(v),1-w(v)), c_j=m(e_j).

Let E be any collection of nonzero vectors containing every coordinate
vector. For 0<=t<=1/2 let r_E(t) be the binary rank of {v in E:m(v)<=t}
and N(t)=#{j:c_j<=t}. All integrals below are finite step-function sums:
split at the finitely many costs, with endpoint conventions irrelevant.

A basis chosen from E with cheapest centered costs has total cost

    a_E(g)=integral_0^(1/2) [d-r_E(t)] dt.                   (1)

Proof: sort E by nondecreasing cost and greedily append independent
vectors. At every cost threshold its selected vectors span all vectors
seen so far: rejecting a vector means it is already in their span.
The final selected set is a basis because E contains the coordinates.
Any basis has at most r_E(t) members of cost at most t. Integrating its
number of costs above t bounds its cost below by (1); the greedy basis
attains equality simultaneously at every threshold. No optimizer over
dimensions or infinite limiting argument is used.

Set chi(g)=sum_j(p_j-c_j)=sum_j(2p_j-1)_+. Then

    rho_E(g)=I(g)-a_E(g)
      =chi(g)+integral_0^(1/2)[r_E(t)-N(t)]dt >=0.          (2)

The integrand is nonnegative because the cheap coordinate vectors are
independent and lie in E. The chosen basis plus independent majority
centering is an actual invertible affine spectral map of g, preserving
Booleanity and H. For E equal to all nonzero parities, a_E=a(g), the
full affine influence minimum, and (2) is its exact release. For a
smaller E it supplies an executable lower bound on that full release.

More locally, any parity vectors independent modulo the span of the
cheap coordinate vectors certify a corresponding rank increment. Such
increments may be integrated to give lower funding. Separate proposed
row exchanges must not be summed unless their quotient independence
has been checked. They can all consume the same one-dimensional gain.

An actual Boolean guard has squared spectrum uniform on the even-parity
hyperplane in odd d>=3. It is realized by the parity lift of the bent
quadratic on d-1 bits:

    g(y)=(-1)^sum_(j=0)^((d-3)/2) (y_(2j)+y_(d-1))
                                      (y_(2j+1)+y_(d-1)).

All sums in this exponent are in F_2. Each p_j=1/2; every parity other
than zero and the all-ones vector has centered cost1/2, while the
all-ones vector has cost0. Thus chi=0 and (2) gives rho=1/2. Every one
of d separate coordinate-row replacements by that same all-ones vector
would individually save1/2. Summing them overcharges the actual release
by a factor d. At d=3 this is rho=1/2 versus a false proposed total3/2.
This refutes an overlapping-swap sum, not any registered source theorem.

## 2. Physical Fourier rows and the SAME child bank

For an original physical queried block A, retain all assignments u and
write g_u=f|X_A=u. Its actual Fourier coefficients are

    b_u(T)=sum_(V subset A) fhat(T union V) chi_V(u).

Use these signed coefficients before squaring to calculate w_u(v) in
(1). This keeps every interaction, including mixed entropy refunds; no
incoherent mixture replaces a child. Let rho_E,A=E_u rho_E(g_u), and
S_E,A=E_u[K a_E(g_u)-H(g_u)]. Exact restriction accounting gives

    D_K(f)+S_E,A=L_A-K(I_A+rho_E,A),                       (3)
    S_A=S_E,A+K rho_E,A.

The original complete terminal entropies remain. In a least-dimensional
positive K-witness with K>=0 every transformed proper child is smaller
and Boolean, so S_E,A>=0. For an arbitrary affine-minimal root this last
line is unavailable; the previous A052/A055 path families have negative
physical child banks. Physical ratio criticality alone does not license
the transformed children: it gives S_A>=0, while S_E,A=S_A-K*rho_E,A
may be negative. The stronger least-dimensional fixed-K selector is
used precisely to license these smaller Boolean affine images. Equation(3) itself holds without criticality.

Consequently the new functional provides actual lower release, rather
than another upper budget, but still needs a universal block selection.
It never grants a fresh bank after a chart change.

## 3. A fixed original pair with a non-character refund

Let k>=2, p=2^-k, and A_k be the event that k new control bits are zero.
On four data bits a,b,c,z define the bent Boolean quadratic

    Q(a,b,c,z)=(-1)^(ab+ac+bc+za),
    F_k=1-A_k+A_k Q.

The exponent is in F_2. Direct elimination of z shows EQ=1/4; the
nondegenerate quadratic has sixteen Fourier coefficients of magnitude
1/4, hence H(Q)=4,I(Q)=2. Its squared law is the full uniform four-cube,
so it is affine-influence minimal. The established activation parity
calculation shows F_k has full affine spectral span and is also affine
minimal. More explicitly, each data marginal is p/2, each control
marginal is3p/4; a nonzero data parity costs p/2 and any parity using a
control costs3p/4. These satisfy all minimum-basis inequalities.

Query the ORIGINAL proper pair (a,b), of total influence I_A=p.
Before activation its four actual children are

    (a,b)=00: +1;  01: chi_c;  10: chi_c chi_z;  11: -chi_z.

After activation the first remains constant and the other three are
activated characters, all with core mean zero. Each has complete entropy
E_k(0,0), where E_k is defined below. The character of weight two has
influence(k+2)p. Replacing one retained data parity row by c+z makes it
a single-coordinate character and reduces its influence to(k+1)p.
The other two already have influence(k+1)p. No control is queried or
discarded. All four terminal entropies are unchanged by these resets.

For each nonconstant child the only zero-cost data directions are the
kernel of its character; every remaining nonzero parity cost is p.
Formula(1) therefore proves these influence minima exactly. In particular

    rho_A=p/4, I_A+rho_A=5p/4.                            (4)

Character-only centering releases zero in every child: each marginal is
at most p<=1/4. The lower funding in (4) is a genuine parity-basis gain.
It is a single refund in one of the four branches, not three separate
root budgets. It persists as every influence and total influence tend
to zero when k grows.

## 4. Uniform price15/4, with every entropy term retained

Write h(t)=-t^2 log2(t^2), h(0)=0. For a Boolean G with H=H(G), mu=EG,
direct Fourier expansion of1-A_k+A_k G gives

    E_k(H,mu)=pH+h(1-p(1-mu))-p h(mu)
      +p(1-p)h(1-mu)
      +2kp[(1-mu^2)+(1-p)(1-mu)^2].

This includes the exceptional empty coefficient. All sums are finite.
Indeed, at every nonzero data label s all control labels carry amplitude
p*Ghat(s); at data label zero the nonempty control amplitudes are
-p(1-mu), and the empty one is1-p(1-mu). Summing their h-values gives
the displayed formula: the nonzero data terms contribute
p[H-h(mu)]+2kp(1-mu^2), and the nonempty control-only terms contribute
p(1-p)h(1-mu)+2kp(1-p)(1-mu)^2.
The pair decrement is exactly

    L_A=E_k(4,1/4)-(3/4)E_k(0,0)
       =(15/4)p+p(1-p)h(3/4)+(3/8)kp^2+Delta(p),          (5)
    Delta(p)=h(1-3p/4)-(3/4)h(1-p).

The factor3/4 in (5) is the three complete nonconstant terminals, with
the fourth constant terminal retained at its original reach1/4.
It is not an omitted conditional entropy or a new reference.

For0<p<=1/4, h''(t)=-(4 ln(t)+6)/ln2 on[1-p,1]. It is nonpositive
there and is at least-6/ln2. Taylor's theorem about the mean, with the
two endpoint values of weights3/4 and1/4, gives

    0<=Delta(p)<=9p^2/(16ln2)<27p^2/32.                   (6)

Here ln2>2/3 follows from the positive atanh series. Also
h(3/4)=9/4-(9/8)log2(3)<1/2 because3^9>2^14. Finally
kp<=1/2 for k>=2: the sequence k/2^k is nonincreasing for k>=1.
Divide(5) by positive p, apply(6), and use p<=1/4 to obtain

    L_A/p <15/4+1/2+3/16+27/128=595/128.

At K=15/4, equations(4)--(6) prove the ORIGINAL pair is paid:

    K(I_A+rho_A)-L_A > (600-595)p/128=5p/128.             (7)

All terms come from the SAME original influence account. In particular
the physical-only pair cost is not given the additional p/4 a second
time elsewhere. This is a local theorem, not FEI(15/4). In fact the
physical-only query is strictly unpaid at15/4: (5) has L_A>(15/4)p,
because h(3/4)>0, p(1-p)>0 and Delta>=0. The actual non-character
refund changes this SAME original pair from unpaid to paid.

## 5. Arbitrary core, nonvacuity, and the exact remaining obstruction

Tensor F_k with ANY Boolean h on disjoint variables. Query the same
displayed pair and use the same explicit reset only in the weight-two
character branch. H(h) and I(h) remain in EVERY terminal; the chosen
release is still p/4 and (5)--(7) are unchanged. No FEI assumption on h
or permission to center it is required. Its full affine optimum might
release more, but that extra resource is not used in this theorem.
If h is canonical affine-minimal/full-span, tensor closure additionally
gives those properties for the displayed source; they are not needed
for payment of this particular query.

The terminal obstruction is real even without an arbitrary h. An
optimized nonconstant terminal has entropy E_k(0,0) and influence(k+1)p.
Its ratio tends to4. For every k>=16 it VIOLATES K=15/4:

    E_k(0,0)>=2kp(2-p),
    2kp<1/4 and 4k-1/4>=(15/4)(k+1).

The first inequality discards only nonnegative h(1-p); the second uses
monotonicity of k/2^k and is strict in its first part. Thus the three
optimized terminal reserves are negative there. At a genuine minimal
15/4-witness, their nonnegativity would contradict(7); this explicit
family is excluded precisely at that hypothesis. No terminal debt or
mixed refund is declared paid by local query payment alone.

Known component-pruning failures do not apply to this construction:
the signed physical rows, original reaches and whole h persist. Neither
component indicators nor disconnected-support pruning are used.

FIRST UNSUPPORTED LINE: on every genuine critical source, select an
original proper pair whose rank-certified unused affine release covers
its signed entropy bill, with the same S_E,A and all terminals. The rank
formula solves overlapping release ownership and the example supplies
one actual non-character lower funding ray. It does not force that ray,
or any adequate rank increment, on all Boolean sources.
