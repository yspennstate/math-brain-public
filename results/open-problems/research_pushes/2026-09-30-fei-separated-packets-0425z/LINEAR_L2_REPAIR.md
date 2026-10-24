# Approximate code-ball spectra admit a linear L2 Boolean repair

2026-09-30 UTC. Status: proved using the standard Kindler–Safra theorem. This closes degree-preserving Boolean repair for the stated exact code geometry. Entropy and influence transfer remain unpaid, so full FEI remains open.

## Theorem

Let C<=F_2^n be a binary linear code with distance D>6d, where d>=0 is an integer. Let f be Boolean and let delta be its squared Fourier mass outside the union of radius-d balls centered at C. Then there is an actual Boolean f_0 with Fourier support entirely in those same balls such that

    ||f−f_0||_2^2 <= K_d delta,                          (1)

where K_d depends only on d, independently of n and code rank. One can take K_d=2^(O(d)) for d>=1 and K_0=2. The hidden absolute constant in the exponential includes the standard Kindler–Safra constant.

Moreover f_0 admits the exact code-field decomposition of LINEAR_CODE_EXTENSION.md, whose decoded children are Boolean of real degree at most d. Existence is asserted, not an efficient reconstruction algorithm.

The zero code can be included by defining its distance as infinity; in that case this specializes to an ordinary low-degree Boolean repair statement.

## External theorem used at its precise scope

Use the unbiased Kindler–Safra theorem in the following quantitative form: there is a universal B>=1 such that any Boolean sign function s has a Boolean degree-d k satisfying

    ||s−k||_2^2 <= B^d ||s^(>d)||_2^2                   (KS)

for d>=1. The statement for all tail sizes follows from its small-tail form by a constant-function bound.

A primary source giving this formulation is Dinur–Filmus–Harsha, *Sparse juntas on the biased hypercube*, ECCC TR17-180 revision 3, Theorems 2.2–2.3, PDF pages 8–9:
https://eccc.weizmann.ac.il/report/2017/180/revision/3/download . It credits the quantitative formulation to Keller–Klein, combining their Theorem 1.4 and Proposition 5.6. Conversion from 0/1-valued functions to signs preserves the displayed tail-to-L2-error constant. The earlier fixed-d version also appears in Filmus, *A simple proof of the Kindler–Safra theorem* (2022), Theorem 3.6. These are credited inputs, not results proved anew here.

## Fiber projections and the initial repair

Let g be the Fourier projection of f onto the code balls, with decoded degree-d fields h_z. On the actual physical coset of C-perp with syndrome z, g equals h_z. The low-degree characters are orthonormal on this coset, so h_z is the orthogonal projection of f there. Define

    delta_z=E_(coset z)(f−h_z)^2
            =1−||h_z||_(2,full cube)^2,
    E_z delta_z=delta.                                  (2)

In particular 0<=delta_z<=1 and ||h_z||_2<=1.

For any polynomial of degree at most 6d, its expectation on this coset equals its full-cube expectation: a nonconstant Fourier frequency of weight at most 6d cannot be a codeword. Apply this to the moments of h_z. The proof of RANK_FREE_ROBUSTNESS.md therefore holds on each coset separately and gives

    epsilon_z:=E_(full cube)(|h_z|−1)^2
       <= R_d sqrt(delta_z),
    R_d=(5^(d/2)+1)^3.                                 (3)

Put s_z=sign(h_z), with either sign at ties. Since h_z has degree at most d,

    ||s_z^(>d)||_2^2<=||s_z−h_z||_2^2=epsilon_z.

Apply (KS) to find a Boolean degree-d k_z. The triangle inequality squared gives, with

    a_z=||h_z−k_z||_2^2,
    A_d=2(1+B^d)R_d,

that

    a_z<=A_d sqrt(delta_z).                             (4)

This is only the initial square-root estimate. The next step makes it linear.

## Discrete-value bootstrap on the genuine physical coset

On the actual syndrome-z coset, put

    v=h_z−k_z,          w=f−h_z,          r=f−k_z=v+w.

Here r takes values in {0,+2,−2}, while v is a degree-d polynomial. For every real v,w with r=v+w in that three-element set,

    v^2<=v^4+w^2.                                       (5)

Indeed, if |v|>=1 use v^2<=v^4. If |v|<1 and r=0 then w=−v. If |v|<1 and |r|=2, then |w|>1>|v|.

The moments of v of orders two and four agree on the coset and full cube. Ordinary hypercontractivity on the full cube consequently gives

    E_(coset z) v^4=E_(full cube) v^4<=9^d a_z^2.

Averaging (5) on the coset yields the exact useful inequality

    a_z<=9^d a_z^2+delta_z.                              (6)

Set

    theta_d=1/[4*9^(2d)*A_d^2].

When delta_z<=theta_d, (4) gives a_z<=1/(2*9^d), and (6) absorbs to

    a_z<=2 delta_z.

When delta_z>theta_d, use ||h_z||_2<=1 and ||k_z||_2=1 to get a_z<=4<=4 delta_z/theta_d. Thus in every fiber,

    a_z<=L_d delta_z,
    L_d=max(2,16*9^(2d)*A_d^2).                          (7)

Because B is universal and R_d is exponential in d, L_d=2^(O(d)). No ambient dimension or code rank enters this bound.

## Reassemble an actual Boolean function

Walsh-invert the family k_z in its syndrome variable:

    v_c(x)=E_z chi_c(z)k_z(x),
    f_0(x)=sum_(c in C)chi_c(x)v_c(x).

If M is a generator matrix for C, the second formula is exactly

    f_0(x)=k_(Mx)(x),

so f_0 is Boolean. Every v_c has degree at most d, giving the required code-ball support.

Unique packet labels under D>2d and Parseval in z imply

    ||g−f_0||_2^2=E_z ||h_z−k_z||_2^2=E_z a_z.

The omitted Fourier part f−g is orthogonal to f_0−g. Hence

    ||f−f_0||_2^2=delta+E_z a_z<=(1+L_d)delta.            (8)

This proves (1) with K_d=1+L_d for d>=1.

For d=0, g is the conditional expectation of f on its code syndrome. Round that conditional expectation to a sign on each coset. If the smaller Boolean value has conditional probability p<=1/2, the squared rounding error is 4p and the conditional variance is 4p(1−p), so their ratio is at most two. Averaging gives K_0=2.

## Remaining FEI gap

The repair theorem is a linear squared-distance statement. It does not bound |H(f)−H(f_0)| or |I(f)−I(f_0)| by a dimension-free multiple of delta or its tail influence. A direct influence estimate can still cost n times the disagreement probability, and ordinary spectral entropy continuity can be more expensive. Those costs must be paid before the exact code-packet FEI reduction can be used as an approximate induction.

Accordingly the previously open degree-preserving repair step is now closed at radius-dependent exponential constants. The entropy/influence transfer step and any universal useful code-ball decomposition remain open. Rare arbitrary Boolean errors around a constant prevent treating that remaining transfer as an automatic consequence of closeness.

The parent independently checked the fiber normalization, initial KS use, discrete bootstrap, and Boolean reassembly. The quantitative external theorem was checked at the primary source above. No executable code, numerical certificate, full FEI claim, or publication-priority claim is included.
