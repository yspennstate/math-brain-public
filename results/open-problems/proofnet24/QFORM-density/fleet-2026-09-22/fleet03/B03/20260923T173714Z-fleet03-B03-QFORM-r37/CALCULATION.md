SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T17:37:14Z.
attacking: the near-coloop collar by pivoting a second heavy physical coordinate in the strong complementary frame direction while retaining the whole-copy half-Riesz time integral.

# Early calculation — second-heavy-complement pivot

Inside the existing angular packet, let the high-leverage right-bank row r have c=v_r^2+q_r^2 in (2/3,1). Choose the spectral basis e1=(v_r,q_r)/sqrt(c), e2 perpendicular, and write the complementary physical rows as (a_j,b_j). Parseval gives

sum_{j!=r} a_j^2=1-c,   sum_{j!=r} b_j^2=1,   sum_{j!=r}a_j b_j=0.

Write the spectral vectors e_v=(1,0) and w=(beta,m) in this basis as (alpha,gamma) and (w1,w2). Then

v_r=alpha sqrt(c), h_r=w1 sqrt(c),
v_k=alpha a_k+gamma b_k, h_k=w1 a_k+w2 b_k,
|alpha w2-gamma w1|=m.

Hence for every complementary physical coordinate k,

|v_r h_k-v_k h_r|=sqrt(c)|b_k|m.                         (C1)

Condition on every original coordinate except X_r,X_k. Completing the square in X_k in

a^(-1)(Hbar+h_r X_r+h_k X_k)^2+2 sigma U(v_r X_r+v_k X_k)

leaves

Q=(h_k^2/a)[X_k+G_k]^2+R_k,
R_k=S_k+2 b U X_r,
|b|=|sigma| sqrt(c)|b_k|m/|h_k|.                         (C2)

The already-proved dependence-safe scalar-bilinear lemma therefore yields

int_R |t|^(-1/2)|phi_{R_k}(t)|^2 dt
 <=8 sqrt(pi L0 |h_k|/(|sigma| sqrt(c)|b_k|m)),            (C3)

sup_s E|R_k-s|^(-1/2)
 <=4 sqrt(2 L0 |h_k|/(|sigma| sqrt(c)|b_k|m)),             (C4)

where L0=sqrt(e) is the scalar product-projection density cap. Since X_k is a genuine original coordinate independent of the background, the square receiver gives

||p_Q||_infinity
 <=4 sqrt(2L0) sqrt(|a|/(|sigma| sqrt(c)|b_k|m|h_k|)).      (C5)

If some strong-complement coefficient satisfies b_k^2>=1/2, split on |w1|.

* If |w1|>=m/4, then |h_r|>=m sqrt(c)/4 and the preceding physical-pivot theorem gives
  ||p_Q||_infinity <=16 sqrt(e)c^(-1/2)s_3(A)^(-1)
  <16 sqrt(3e/2)s_3(A)^(-1).

* If |w1|<m/4, then |w2|>=3m/4. Since |a_k|<=sqrt(1-c)<1/sqrt(3) and |b_k|>=1/sqrt(2),
  |h_k| >= (m/4)(3/sqrt(2)-1/sqrt(3)).
  Thus |b_k h_k| >= d_* m with
  d_*=3/8-1/(4sqrt(6))=0.272937927384... .
  Inserting this into (C5) and using |a|/(|sigma|m^2)<2/s_3(A)^2 gives
  ||p_Q||_infinity
  <=8 sqrt(sqrt(e)/d_*) (3/2)^(1/4) s_3(A)^(-1)
  =21.7597788685... s_3(A)^(-1).

So the whole branch with max_{k!=r} b_k^2>=1/2 is uniformly paid by the larger constant

||p_Q||_infinity <16 sqrt(3e/2) s_3(A)^(-1)=32.3082067304... s_3(A)^(-1).   (C6)

The remaining near-coloop endpoint is thereby narrowed to the genuinely diffuse strong-complement direction max b_k^2<1/2. This calculation keeps the entire copy difference inside (C3); no X-X' / X+X' conditional independence or cap is used.
