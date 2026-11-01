from pathlib import Path
P=Path('.')
text=r'''
## A4. Stronger counterexample: eight distinct lattice faces

The matching bound fails even if one insists that all insertions occupy distinct lattice faces. We prove this for s=1/4 using a local determinantal computation and mixing of the infinite-volume square-grid measure. This removes any concern that A1 was only an artifact of repeated evaluation within one cell.

### A4a. The needed canonical inverse-kernel facts

Use primal vertices Z^2 (the half-cell shift from the dual-corner convention is immaterial), black vertices with even coordinate sum, and the bipartite Kasteleyn matrix K(b,w)=1 on horizontal edges and i on vertical edges. Its Fourier symbol for the full off-diagonal adjacency operator is

    P(k_x,k_y)=2cos(k_x)+2i cos(k_y).

The canonical zero-slope inverse kernel is the restriction of

    G(d)= (2pi)^(-2) integral_[0,2pi]^2
                    exp(i k.d)/P(k) dk.                       (A.7)

The integrand is L1: its only singularities occur at the four points where both cosines vanish, and its modulus is O(1/|k-k0|) there; this is integrable in dimension 2. Multiplication by P gives 1 almost everywhere, so Fourier multiplication verifies that the full adjacency operator times G is the identity. A simultaneous shift of both Fourier coordinates by pi shows G vanishes on even-parity displacements; hence this inverse restricts to the bipartite K inverse. The Riemann-Lebesgue lemma gives G(d)->0 as |d|->infinity. The canonical inverse-kernel construction and dimer occupation determinant formula are the standard existing Kasteleyn/Kenyon results (also Dubedat Theorem 1 and its dimer discussion); this paragraph verifies the Fourier realization and the decay needed here, not a new construction of the Gibbs measure.

Because P is even separately in k_x and k_y, G is even separately in d_x and d_y. Taking conjugates and shifting k_y by pi gives

    conjugate(G(d_x,d_y)) = (-1)^(d_y) G(d_x,d_y).

Thus G(1,0) is real and G(2,1) is purely imaginary. Swapping the Fourier coordinates gives G(0,1)=-i G(1,0): the swapped symbol is i conjugate(P), and evenness and the preceding reality relation finish this calculation. The inverse identity at d=0 then gives 2G(1,0)+2iG(0,1)=1, so

    G(1,0)=1/4,  G(0,1)=-i/4.                                (A.8)

Set c=iG(2,1), which is real; evenness handles all signs of these displacements.

### A4b. Local fusion product and nonzero mean

Take four consecutive dual faces f_j=(j,0), j=0,1,2,3. Let N_j, j=0,1,2, be the indicators of the three vertical primal edges crossed by the horizontal dual path. The signed quarter-height increments are alternating, so summing the four face heights gives exactly

    sum_{j=0}^3 h(f_j)=4h(f_0)+1/2-3N_0+2N_1-N_2.

For s=1/4, define the four-point raw product A_f=product_{j=0}^3 exp(i(pi/2)h(f+(j,0))). When f is an even horizontal translate of 0, the residue table gives exp(2pi i h(f))=1. Therefore

    A_f = exp(i pi/4) i^(N_0) (-1)^(N_1) (-i)^(N_2).           (A.9)

This is a local function of just three dimer indicators; no unbounded height variable remains.

For those vertical edges, the occupation kernel L_{jk}=K(b_j,w_j) K^{-1}(w_j,b_k) is, by (A.7)-(A.8),

    L = [[1/4, i/4, c],
         [i/4, 1/4, i/4],
         [c,   i/4, 1/4]].

The two nonadjacent crossed edges give a joint occupation probability det L_{0,2}=1/16-c^2>=0. Hence |c|<=1/4. Joint occupation moments are principal minors of L. Expanding product_j[1+(u_j-1)N_j] consequently gives

    E product_j u_j^(N_j) = det(I+diag(u_j-1)L).

With u=(i,-1,-i), direct expansion of this 3x3 determinant yields

    D := E i^(N_0)(-1)^(N_1)(-i)^(N_2)
       = 7/16+c/2-c^2.                                      (A.10)

For explicit algebra checking, the three pair-minor contributions sum to 5/8-2c^2, the singleton plus constant contributions cancel, det L=3/64-c/8-c^2/4, and the triple coefficient (i-1)(-2)(-i-1) is -4. This gives (A.10). Since c>=-1/4 and c^2<=1/16,

    D >= 7/16-1/8-1/16 = 1/4.

Thus |E A_f|=D>=1/4. No numerical evaluation of c or pi is needed for this lower bound.

### A4c. Dimer mixing supplies the separated-cluster limit

For two fixed finite edge sets separated by an even translation T, a joint occupation probability is a determinant of a block matrix whose off-diagonal blocks consist of G entries at displacements tending to infinity. By the Riemann-Lebesgue decay just proved these blocks tend to zero. The determinant tends to the product of the two diagonal-block determinants, giving asymptotic independence of all occupation monomials. Any function of finitely many binary occupations has a finite multilinear expansion: write it as the sum over configurations v of its value at v times product_j[N_j if v_j=1 else (1-N_j)], then expand. Thus all bounded local functions also factor in expectation in the limit. Applying this to (A.9),

    E A_0 conjugate(A_{(2N,0)}) -> D^2 >=1/16.                (A.11)

This mixing argument is proved for the canonical translation-invariant measure; it does not assume uniform independence under arbitrary boundary conditioning.

Finally take epsilon=1/(2N), put four positive insertions in the four different cells at epsilon f_j near 0, and four negative insertions in the four different cells at epsilon((2N,0)+f_j) near (1,0). Cross distances are uniformly bounded below, while all eight lattice faces are distinct. Their normalized balanced correlation is

    a_s^8 epsilon^(-8s^2) E A_0 conjugate(A_{(2N,0)}),

whose modulus is asymptotic to a_s^8 D^2 epsilon^(-1/2), diverging by (A.11). The matching sum remains bounded. Each product of eight prescribed cell interiors has positive measure, so the almost-everywhere issue is again resolved. QED.

### Independent checks of A4

`distinct_fusion_checks.py` scanned 455 four-face clusters using the Fourier inverse (A.7) and finite-rank Kasteleyn perturbation determinants. For the horizontal consecutive cluster, quadrature grids 64,128,256,512 gave mean moduli 0.3986795039, 0.3986788592, 0.3986788190, 0.3986788165. This suggests c=1/4-1/pi but that evaluation is **not** assumed or claimed proved. The analytical proof only uses c^2<=1/16. The nearest inverse entries were checked against (A.8). `local_fusion_symbolic.py` independently expanded the determinant exactly with SymPy; the initial u vector there is reflected, (-i,-1,i), which has the same determinant since L is invariant under swapping indices 0 and 2. The explicit proof uses the actual vector (i,-1,-i). These quadrature computations are numerical evidence, not an error-certified inverse-kernel construction. A3x3 algebra and the positivity bound, not quadrature, establish nonvanishing.
'''
with (P/'SECOND_ATTEMPT.md').open('a',encoding='utf8') as f:f.write(text)
print('Saved stronger distinct-face counterexample with full proof.')
