# Growing controlled edit sets with one terminal data bank

Uniform Boolean signs, entropy in bits. Let k=2m>=4 and b be the paired
quadratic bent sign. Let v_1,...,v_q be distinct data vertices, q>=1,
and A_j arbitrary indicators on the SAME uniform controller cube, independent
of the data bits. Indicators can be dependent and overlap arbitrarily.
Write a_j=1-2A_j, alpha_j=EA_j, delta=2^-k and

    F(x,z)=b(x)[1-2 sum_j 1_(x=v_j) A_j(z)].           (1)

Distinct data supports make (1) an actual sign. Put c=log2(e).
The general guarded theorem, for q<=2^(m-2), is

    I_ctrl(F)=delta sum_j I(a_j),
    H(F)<=K(m,q) I_data(F)+delta sum_j H(a_j),         (2)
    K(m,q)=max(4+2c,[4m+2c+4c/e]/[m-log2(q)]).

In particular, if q^2<=2^(m-2), then K(m,q)<8 and

    H(F)<=8 I_data(F)+delta sum_j H(a_j).             (3)

Every controller entropy is retained with its exact physical/spectral weight;
(3) does not prove FEI for arbitrary controllers. Supplied controller bounds
H(a_j)<=C I(a_j) give H(F)<=max(8,C)I(F).

## Exact signed root and leaf logarithmic terms

For any bent reference (not only quadratic), the exact root coefficients are

    Fhat(S,T)=bhat(S)1_(T=empty)
             -2delta sum_j b(v_j)chi_S(v_j)Ahat_j(T). (4)

All signed pair cross terms are kept before squaring. For T!=empty,
data-label orthogonality gives the exact marginal
R_T=4delta sum_j Ahat_j(T)^2. The conditional data spectral law is the
normalized squared sum in (4), not a sum of the individual point laws.
The exact root entropy is sum_(S,T) phi(Fhat(S,T)^2), phi(u)=u log2(1/u).
The controller-empty row is included, with no sign folding or entropy reset.

Exact data edge accounting, valid for all bent references, is

Inf_i(F)=1/2+2delta sum_j alpha_j b(v_j)b(v_j xor e_i)
 -4delta sum_(j<l:v_l=v_j xor e_i) b(v_j)b(v_l)E(A_j A_l). (5)

Controller edges occur on disjoint data fibers, yielding the first identity
in (2). The last term in (5) is the actual adjacent double-flip cancellation;
independent-controller products cannot replace E(A_j A_l).

## Good access without inactive-branch fairness

Query the first coordinate of every quadratic pair, then STOP with all partner
and controller bits retained. At a node after h<m first-coordinate queries,
the reference derivative is exactly1/2. Surviving perturbations occupy at
most q*2^{-(k-h)} of the local cube. Taking their union with their coordinate
translate changes influence by at most twice that mass. Consequently

    d>=1/2-q*2^-m>=1/4                              (6)

under q<=2^(m-2). Concavity gives B<=h2(d), and h2(d)/d decreases,
so B/d<=8-3log2(3)<4. All access nodes have zero threshold-4 bad credit.
This schedule is quadratic-paired; no such schedule is asserted for every
bent reference merely because the root identities (4)-(5) hold there.

## One physical leaf, arbitrary controller dependence

A first-coordinate fiber of reach tau=2^-m contains ell<=q edited partner
vertices t_1,...,t_ell. Its actual sign is a common character times
g(t,z)=1-2 sum_j 1_(t=t_j)A_j(z), with indices local to this fiber.
Let s=sum_j alpha_j and u=sum_j alpha_j^2. Raw partner influences are at
most2tau s<=2tau q<=1/2, so the common character can only increase them;
it preserves entropy and controller influences exactly.

The exact signed leaf coefficients are

    ghat(U,T)=1_(U=empty,T=empty)-2tau sum_j chi_U(t_j)Ahat_j(T).

Its empty joint mass is (1-2tau s)^2. In the controller-empty, partner-nonempty
sector, total mass is M=4tau u-4tau^2 s^2. For T!=empty, total row mass is
R_T=4tau sum_j Ahat_j(T)^2. Define normalized conditional partner laws nu_0
on U!=empty and nu_T on all U from the ACTUAL squared signed coefficients.
Zero masses contribute zero. The complete exact entropy is

H(g)=phi((1-2tau s)^2)+phi(M)+M H(nu_0)
     +sum_(T!=empty)[phi(R_T)+R_T H(nu_T)].           (7)

This exhibits every logarithmic term the leaf must pay, including controller-
empty and joint-empty rows. Conditional laws retain all geometric interference.

## Entropy charge versus actual post-cancellation data influence

Since phi(x)<=c(1-x) on [0,1], the joint-empty term is at most4tau s c.
The next sector costs at most M log2(e*2^m/M). The function increases for
M<=2^m, and M<=4tau u<=4tau q<=1, hence this sector is at most

    8tau m u+4tau u(c-2)+4tau u log2(1/u)
    <=8tau m u+4tau u log2(1/u).                    (8)

For nonempty controller labels, phi(sum x_j)<=sum phi(x_j) and H(nu_T)<=m.
Using a_j's nonempty spectral masses4Ahat_j(T)^2 gives the upper bound

    tau sum_j H(a_j)+8tau m sum_j alpha_j(1-alpha_j). (9)

The subtracted tau phi((1-2alpha_j)^2) terms are nonnegative. The potentially
signed u log(1/u) term is bounded by

u log2(1/u)<=sum_j alpha_j^2 log2(1/alpha_j^2)
            <=(2c/e) sum_j alpha_j.

Thus all rows in (7) have the complete bound

    H(g)<=tau sum_j H(a_j)+tau s(8m+4c+8c/e).        (10)

Now at EACH fixed controller input z the actual negative partner set D_z
has cardinality r_z<=ell<=q. Cube edge isoperimetry gives
boundary(D_z)>=r_z(m-log2 r_z)>=r_z(m-log2 q).
Averaging gives

    I_data(g)>=2tau s(m-log2 q).                   (11)

This is the boundary after all collisions and adjacent cancellations, not
the sum of point boundaries. Isoperimetry can be proved by induction:
a set of r vertices spans at most(r/2)log2 r edges; splitting into sizes
a<=b uses cross edges<=a and h2(a/(a+b))>=2a/(a+b).
The empty negative set contributes zero, as do s=0 and ell=0 fibers.

Combining (10)-(11), and using the increased actual character-shifted data
influence, proves the leaf coefficient in (2).

## Absolute guard and full physical partition

If q^2<=2^(m-2), then log2 q<=(m-2)/2 and this implies q<=2^(m-2).
The leaf coefficient is at most

    [4m+2c+4c/e]/[(m+2)/2]<8,

because c<3/2, e>2 imply2c+4c/e<6<8. Also4+2c<7<8.
The controller cube is never queried. Every leaf has physical reach tau;
each edited vertex appears in exactly one leaf. The tau controller entropy
coefficient in (10) is multiplied by its physical tau reach, yielding
tau^2=delta for each controller, ONCE.

Exactly I_data(F)=I_access+E I_terminal,data and
I_ctrl(F)=E I_terminal,ctrl=delta sum_j I(a_j). The entropy telescope
H=sum pi(B+JS)+E H(leaf), with JS<=2cd, proves (2)-(3).
The scalar JS proof is supplied in A022 stage3 PROOF.md §3; no FEI assumption
or repeated terminal-data reserve occurs in this step.

## Depth-independent scoped recursive closure

Start with constants and characters. Repeatedly apply (1) satisfying the
quadratic pairing, distinct-data-vertex and q^2 guard, with a fresh data block
independent of the existing controller bits. Controllers a_j can share those
bits and can be any previously constructed signs. Induction on construction
depth, (3), and I_ctrl=delta sum I(a_j) prove H<=8I for every such finite
construction. The constant does NOT grow with depth or edit count. Sharing
controller bits is allowed because their actual root influences are the sum
over disjoint data fibers. This is a scoped grammar, not universal admission.

## Exact universal frontier

All scoped statements above are proved. The first unsupported universal line
is that arbitrary Boolean functions admit this guarded recursive representation,
or that a dense edit fiber lacking m-log2(q) slack has another paid data bank.
When q approaches2^m, (11) degenerates; character multiplication may then
lower influence and (6) can fail. Arbitrary controller entropy remains fully
inherited outside the recursively certified grammar. No constant-leaf zero-
credit completion, unguarded composition or universal FEI theorem is asserted.
