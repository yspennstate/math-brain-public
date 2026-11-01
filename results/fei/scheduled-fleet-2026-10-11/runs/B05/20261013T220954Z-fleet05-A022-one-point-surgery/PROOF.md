# Paired-coordinate access with sparse terminal entropy

All cubes are uniform; signs are Boolean and entropy is in bits. Let k=2m>=2,
b(x)=(-1)^{sum_j x_(2j)x_(2j+1)}, D any set of at most four vertices,
h=b(1-2 1_D), and r>=0. The actual function F is 1 unless all r fresh
controls are zero, and on that event it is b for selector y=0 and h for y=1.
No symmetry quotient or asymptotic limit is part of the theorem.

## 1. Explicit physical stopping policy

Query the fresh controls, stopping every inactive branch. On the active branch
query x_0,x_2,...,x_(2m-2), leaving all partners and the selector unqueried.
Then query the selector and stop. A constant restriction may stop earlier.
Every access node satisfies B<=4d, so its threshold-4 bad-node credit is zero.
This assertion is about access nodes; retained leaves are not silently refined.

At a control query one child is constant. The previously derived, independently
reconstructed constant-child lemma gives B/d<=2+log2(e)/sqrt(e)<3 for d>0.
The restriction which remains active keeps its physical weight 2^-r.

At a first-coordinate query, the y=0 child retains the unqueried uniform
partner of this intact quadratic pair. Its coordinate influence is exactly
1/2. The y=1 branch has nonnegative influence. Averaging over the still fair
selector gives d>=1/4. Concavity gives B<=h2(d), and h2(d)/d decreases on
(0,1). Thus B/d<=4h2(1/4)=8-3log2(3)<4; the last strict inequality follows
from 3^3>2^4. The defects can be arbitrary here: this part does not use |D|<=4.

After all first coordinates are fixed to a, b becomes the character chi_a
on the m remaining partners. The two selector children are chi_a and
chi_a(1-2 1_E), where E is the corresponding fiber of D and |E|<=4.
Multiplication by the common character permutes residual Fourier labels
and preserves the selector B and d. The same constant-child lemma applies.

## 2. Complete sparse-leaf certificate

For every m>=0, E subset of the m-cube with |E|<=4, and every character chi_A,
H(chi_A(1-2 1_E))<=6 I(chi_A(1-2 1_E)). This includes empty/full E.
Multiplication by a character preserves H, but does not in general preserve I.

For 0<u=|E|2^-m<=1/4, every Inf_i(1-2 1_E)<=2u<=1/2.
Multiplication by chi_A complements those influences indexed by A, so it
can only increase I. Put v=4u(1-u), L=log2(1/u)>=2, s=|E|.
The empty spectral mass is 1-v. Conditioning on its complement, whose
alphabet has at most 2^m labels, gives

H <= h2(v)+vm <= v[log2(e/v)+m]
  <= 4u[2L+log2(s)+log2(e)-log2(3)],
I >= 2u L.

The last entropy bound uses 3u<=v<=4u and a positive bracket. The influence
bound is the cube edge-isoperimetric inequality. Since e<3, if
log2(s)+log2(e)-log2(3) is negative the ratio is at most 4; otherwise L>=2
gives H/I<=4+log2(s)<=6. The elementary bound e<3 follows from
e=1+1+sum_(j>=2)1/j!<2+sum_(j>=2)2^{-(j-1)}=3.

For u>1/4 and s<=4, 2^m<4s<=16, hence m<=3. Every nonconstant Boolean
function on the m-cube has I>=2m/2^m and H<=m, hence H/I<=2^(m-1)<=4.
Apply this to the character-multiplied function itself. Constants have H=0.
For m=0 or 1 the claim also follows directly (all signs are characters or constants).

For completeness, the edge-isoperimetric inequality used above is proved
by induction: a set of s vertices has at most (s/2)log2(s) internal edges.
Split it into sizes a<=b; cross edges number at most a. The inductive step is
a log2(a)+b log2(b)+2a <= (a+b)log2(a+b), equivalent to
h2(a/(a+b))>=2a/(a+b), the chord bound for concave binary entropy.
Therefore boundary>=s log2(2^m/s). To obtain the minimum nonconstant
boundary m, take the smaller sign set 1<=s<=2^(m-1). The concave function
s log2(2^m/s) is minimized at an endpoint, giving min(m,2^(m-1))=m.

## 3. One physical influence partition; no unpaid terminal entropy

Let pi_v be physical reach probability, I_removed=sum_internal pi_v d_v,
I_terminal=sum_leaves pi_leaf I(leaf). Exactly I(F)=I_removed+I_terminal.
The fair coordinate entropy identity is
H(F)=sum_internal pi_v(B_v+JS_v)+sum_leaves pi_leaf H(leaf).
The C005 scalar step can be reconstructed here without assuming FEI.
For real Fourier amplitudes a,b, set q=(a^2+b^2)/2 and
z=(a^2-b^2)/(a^2+b^2), ignoring q=0. The scalar JS in nats is
q A(z), where A(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2.
For |z|<1 its series has coefficient 1/[2j(2j-1)] at z^(2j).
The corresponding coefficient of 1-sqrt(1-z^2) is
C_j/(2j-1), C_j=binom(2j,j)/4^j. Induction using C_1=1/2 and
C_(j+1)/C_j=(2j+1)/(2j+2) gives C_j>=1/(2j).
Thus A(z)<=1-sqrt(1-z^2); continuity handles |z|=1.
Consequently JS_nats<=q-|ab|=(|a|-|b|)^2/2<=(a-b)^2/2.
Summing over residual labels, and using d=sum_T(a_T-b_T)^2/4,
gives JS_bits<=2d/ln2. This independently reconstructs the analytic
interface of A083's coefficient result; no Lean check of real logs is claimed.
Sections 1-2 now give

H(F) <= (4+2/ln2) I_removed +6 I_terminal
     <= (4+2/ln2) I(F).

This is a theorem for every even k>=2 and every r>=0, with no repeated
use of the core influence. Terminal entropy is certified directly,
rather than inferred from disappearance of access bad nodes.
The C005 analytic bound has just been supplied explicitly, including its
endpoint and signed-amplitude handling.

## 4. Exact first unsupported universal line

No line of the scoped theorem remains unsupported. The extension to every
Boolean core would require an access policy maintaining a sufficiently
influential unedited branch (or another paid reserve) and stopping leaves
with uniformly bounded complete entropy/influence. Arbitrary cores have
no guaranteed intact quadratic pair. Increasing |D| also increases the
log2|E| leaf bill in Section 2. Neither a zero-cost complete constant-leaf
tree nor the universal B05 localized odd-face bridge follows from this proof.
Overlapping controls with conditional selector bias require a new argument:
the d>=1/4 step explicitly uses the still fair selector.
