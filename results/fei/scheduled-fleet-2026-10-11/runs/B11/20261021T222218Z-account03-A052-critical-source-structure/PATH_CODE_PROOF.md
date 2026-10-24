# Affine-minimal Boolean spectra can have an unpaid pair collision

All cubes are finite and uniform, signs are Boolean, and entropy uses bits.
This is a counterexample to an intermediate pair bound, not to FEI.

## 1. Actual Boolean construction and exact spectrum

Fix m>=3, M=2^m and r=M-2. Let P be the path with r edges e_0,...,e_(r-1)
and r+1=M-1 vertices. Let c_0=0, and let the other M-1 vectors c_y in
F_2^r be its vertex-edge incidence rows, in path order. Thus the ordered
list is

    C=(0, e_0, e_0+e_1, e_1+e_2, ..., e_(r-2)+e_(r-1), e_(r-1)).

Use any bijection from F_2^m to this displayed list, and define the actual
Boolean function f_m(x,y)=(-1)^(x dot c_y), with r data and m address bits.
For data Fourier label s and address label v, direct averaging over x gives

    fhat_m(s,v)=M^(-1)(-1)^(v dot y_s) if s=c_(y_s), and 0 otherwise.

The code vectors are distinct (the path has at least six edges), so y_s
is unique. Thus the squared spectrum is uniform on C times F_2^m,
with M^2 atoms, each of mass M^(-2). Consequently

    H(f_m)=2m,
    Inf_xi=2/M,  Inf_yj=1/2,
    I(f_m)=2r/M+m/2.

In particular H/I tends to 4, not infinity. No FEI counterfamily results.

## 2. Full affine span and minimum influence over the entire affine orbit

The incidence rows span F_2^r: if an edge vector is orthogonal to every
vertex row, its selected edge set has even degree at each path vertex.
A nonempty forest has a leaf in a nontrivial component, so this is
impossible. Since 0 belongs to C, its affine span is all F_2^r. The product
support therefore has full affine dimension r+m.

For any nonzero data parity a, the number of rows c_y satisfying a dot
c_y=1 is the number b(a) of odd-degree vertices in the nonempty selected
edge subgraph. It is even and positive; it is at most M-2 because there
are only M-1 actual vertices and their count is odd. Hence

    2/M <= min(b(a), M-b(a))/M.

Every data coordinate marginal equals 2/M. Any parity using at least one
address coordinate is fair under the product spectral law. Thus, writing
p_i=P(S_i=1) and w(v)=P(v dot S=1), the exact minimum-basis inequalities are

    p_i<=1/2,
    min(w(v),1-w(v)) >= max_(i:v_i=1) p_i,  v!=0.

A051's independently reconstructed basis argument shows that these imply
I(M_0 S+b)>=I(S) for every invertible M_0 and translation b. They do NOT
imply physical descendant criticality. This construction is an actual
Boolean full-span affine minimum, not the non-Boolean simplex relaxation.

## 3. A pair invisible to both singleton collisions

Use the original physical data coordinates i=2,j=3 (zero-based).
There are no two code vectors differing by e_i or e_j. Indeed the only
unit differences between path-incidence rows or zero have labels
0,1,r-2,r-1: zero to a leaf row, or a leaf row to its neighboring
degree-two row. All other comparisons have even size 2 or 4, or odd
size 3. Since r>=6, i,j are excluded from this list.

Exactly one unordered pair of code vectors differs by e_i+e_j: zero and
the row e_2+e_3. Two degree-two incidence rows sharing an edge differ
in two nonconsecutive edge labels; disjoint such rows differ in four
labels. The two leaf rows differ in labels 0,r-1. A leaf and a degree-two
row have an odd-size difference. This lists every possibility.

For each retained Fourier label t off i,j, write its real coefficient
quartet (a,b,c,d), q=a^2+b^2+c^2+d^2. Zero rows contribute zero. Define

    c_i(t)=4a^2 b^2/(a^2+b^2)+4c^2 d^2/(c^2+d^2),
    c_j(t)=4a^2 c^2/(a^2+c^2)+4b^2 d^2/(b^2+d^2),
    Q(t)=4[(ab+cd)^2+(ac+bd)^2+(ad+bc)^2]/q.

Every denominator-zero term has numerator zero and is defined as zero.
Let C_i,C_j,C_ij be their sums. The absent unit differences give
C_i=C_j=0. The unique pair difference creates, at each of the M address
Fourier labels, one diagonal quartet (a,0,0,d) with |a|=|d|=1/M.
It contributes 4a^2d^2/(a^2+d^2)=2/M^2. Other quartets contain at most
one nonzero coefficient and contribute zero. Therefore

    C_ij=2/M>0=2(C_i+C_j).

At m=3 this is C_23=1/4. In A052's previous exact decomposition, P_ij=2/M,
both merging refunds vanish, beta_i=beta_j=0, and O_i+O_j=4/M. The old
orientation-corrected inequality remains valid. The false new proposal
was that affine minimality could remove its additive orientation term.
This construction disproves that proposal for EVERY m>=3 and for every
finite multiplier of C_i+C_j at this pair. It does not disprove selection
of a different pair or a theorem assuming physical criticality.

## 4. Where actual descendant criticality excludes the construction

Because no original Fourier pair differs only at i, restriction x_i=0 or
1 moves every coefficient injectively to its retained label, changing at
most its sign. Each actual child has exactly the original multiset of
squared nonzero Fourier coefficients, so H(child)=2m. The influence
decomposition is exact, and either child's squared law is the same
retained projection. Hence

    I(child)=I(f_m)-2/M>0,
    H(child)/I(child)>H(f_m)/I(f_m).

Both denominators are positive: I>=m/2 and m>=3. Thus these affine minima
are not ratio-critical even under one physical query. At m=3, H=6,I=3,
and each x_2 or x_3 child has H=6,I=11/4 and ratio 24/11>2.

Set K=R=H/I and D_K(f_m)=0. The actual signed child reserve is
S_i=-E D_K(child)=-K(2/M)<0, and the exact bank reads
D_K(f_m)+S_i=L_i-K Inf_i=-K(2/M), with L_i=0. Assigning a nonnegative
child bank to this affine minimum would be the first invalid line.
For a genuinely descendant-critical source, R Inf_i<=L_i excludes this
same zero-erasure pattern whenever R>0 and Inf_i>0. No descendant is
assumed to inherit criticality.

## 5. Component pruning and the unresolved universal step

Everything above uses the complete original signed Boolean spectrum and
actual input restrictions. No component indicator or incoherent spectral
mixture replaces the parent. The historical nine-bit raw-entropy and
seven-bit maximum-component-ratio failures therefore do not contradict
the calculation; their prior physical-descendant exclusions remain as
recorded in A052 stage1. Affine minimality is a different, strictly
insufficient admission test, now with an explicit Boolean witness.

The exact remaining gap is to use physical child eligibility TOGETHER
with affine minimum-basis inequalities and the signed pair interaction
to pay a selected proper physical block from the SAME unused D+S_A bank.
The present witness has no eligible positive child bank and cannot be
substituted for a genuine high-K critical witness. A quantitative
near-zero-erasure comparison relative to D+S_A, rather than an affine-only
pair inequality, is the next unpaid implication.
