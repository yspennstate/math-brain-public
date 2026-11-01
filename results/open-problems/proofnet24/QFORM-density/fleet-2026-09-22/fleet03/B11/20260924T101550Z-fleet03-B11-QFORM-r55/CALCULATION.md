SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-24T10:15:50Z.
attacking: the general physical indefinite-pair L^3 endpoint, then spend a third original-coordinate square before taking L^infinity.

# Early calculation: a uniform L^3 theorem for every physical indefinite binary quadratic

Let X,Y be independent probability variables with densities f,g satisfying 0<=f,g<=1. Let

q(x,y)=a x^2+2txy+b y^2+alpha x+beta y+gamma

and suppose B=[[a,t],[t,b]] is indefinite. Put D=t^2-ab=|det B|>0. The calculation below gives

||p_q||_3 <= 22 D^(-1/3).

Affine terms are removed by the constant translation (x,y)->(x,y)+(1/2)B^{-1}(alpha,beta); coordinatewise translations preserve independence and density caps. Scaling B by D^{-1/2} reduces to D=1, since scaling a real random variable by sqrt(D) multiplies its density L^3 norm by D^{-1/3}. Hence assume t^2-ab=1.

## Case I: |ab| <= t^2/4

Then |t|>=2/sqrt(5). Split the physical plane into

R1={|by|<=|tx|/2},  R2=R1^c.

For fixed x on R1,

|d_y q|=2|tx+by|>=|tx|,

and y->q(x,y) is monotone on the interval R1(x). If k_x is the pushforward of g(y)1_R1(x), then

||k_x||_3^3 = int_R1(x) g(y)^3/|d_y q|^2 dy <= |tx|^{-2}.

Minkowski and the cap-one bathtub estimate give

||p_1||_3 <= |t|^{-2/3} int f(x)|x|^{-2/3}dx
            <=6*2^(-1/3)|t|^(-2/3).

On R2, |x|<2|b||y|/|t|, so |ax|<|ty|/2 by |ab|<=t^2/4. Therefore

|d_x q|=2|ax+ty|>=|ty|,

and the symmetric argument yields the same bound for p_2. Hence

||p_q||_3 <=12*2^(-1/3)|t|^(-2/3)
           <=12*(5/8)^(1/3)
           =10.2598556801... .

## Case II: |ab|>t^2/4

From t^2-ab=1, either ab>1/3 or ab<-1/5. Thus max(|a|,|b|)>1/sqrt(5). Swap X,Y if needed and assume |b|>1/sqrt(5).

For fixed x, the discriminant of b y^2+2txy+a x^2-z is

4[(t^2-ab)x^2+bz]=4(x^2+bz).

At every regular root, |tx+by|=sqrt(x^2+bz). Since g<=1 and there are at most two roots, the conditional density is at most (x^2+bz)^(-1/2) when the discriminant is positive. Consequently

p_q(z)<=F(bz),
F(u)=int f(x)|x^2+u|^(-1/2)dx.

Let h be the density of X^2. Then h(y)<=y^(-1/2), int h=1, and, with s=-u,

F(u)=int_0^infty h(y)|s-y|^(-1/2)dy=:I_{1/2}h(s).

For the centered Hardy-Littlewood maximal function Mh, a direct near/far split gives

I_{1/2}h(s)<=4 sqrt(Mh(s)).

Indeed, on |s-y|<=R, Stieltjes integration and H(r)<=2r Mh(s) give <=4 sqrt(R) Mh(s), while the complement contributes <=R^(-1/2); optimize R=1/(4Mh(s)).

The one-dimensional centered maximal operator has weak-(1,1) constant 3 by the interval Vitali covering lemma. Truncating h at level lambda/2 and integrating the weak estimate gives, for p=3/2,

int (Mh)^(3/2) <= 9*2^(3/2) int h^(3/2) <26 int h^(3/2).

Also

int h^(3/2)<=int h(y)y^(-1/4)dy=E|X|^(-1/2)<=2sqrt(2),

where the last cap-one bathtub extremizer is 1_[-1/2,1/2]. Hence

||F||_3^3 <=64*26*2sqrt(2),

and therefore

||p_q||_3 <= |b|^(-1/3)||F||_3
           < (64*26*2sqrt(2))^(1/3) 5^(1/6)
           =21.91430857... <22.

Combining the two cases and undoing the determinant normalization proves

boxed: ||p_q||_3 <=22 |det B|^(-1/3).

## Third-direction consequence

If a literal third original coordinate W is source-disjoint and contributes lambda(W-s)^2, the completed shifted-square lemma of fleet01/B05 gives

||p_{lambda(W-s)^2}||_(3/2)<=2|lambda|^(-1/3).

Young therefore gives

boxed: ||p_{q(X,Y)+lambda(W-s)^2}||_infinity
       <=44 (|det B| |lambda|)^(-1/3).

The convolution is continuous and vanishes at infinity. This is the exact functional mechanism requested by the indefinite-signature assignment: the opposite-sign rank-two logarithmic singularity is compatible with L^3, and the third square contributes the conjugate L^(3/2) smoothing needed for L^infinity.

Full QFORM remains open: this calculation does not yet cover a third coordinate that is bilinearly coupled to both pair variables, nor arbitrary shared-source third curvature or the global extraction problem.
