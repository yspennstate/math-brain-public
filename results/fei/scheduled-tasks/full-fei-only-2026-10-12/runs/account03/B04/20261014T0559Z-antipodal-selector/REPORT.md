# B04 GU selector — two antipodal defects and an arbitrary-phase ledger (UNVERIFIED)
Producer account03/B04; B04 A016–A020. Original private mathematical run, October 14, 2026.

## Frozen candidate, consequence, and old bound
For every m>=2, x,z in {0,1}^m, y in {0,1}, set h(x)=1 if x=0^m or x=1^m, else 0, and f_m(x,z,y)=(-1)^(x·z+y h(x)). This is a genuine sign function on a uniform 2m+1 cube; its two branches share ALL physical data variables and disagree on delta=2^(1-m) of x, tending to zero. CLAIM: G(f_m)<=(9/4)I(f_m) for EVERY m>=2, but G(f_m)>2I(f_m) for EVERY m>=8. Include empty S and zero spectral masses; handle I=0 separately for the universal implication. Previous B04 result handled ONE bottom-point defect with 9/4; this is a non-tensor two-antipodal interacting-defect extension.

The universal OPEN target is G(f)<=a I(f)+b U(f) for ALL Boolean f, ONE finite a>=0 and b<1. A proved global pair would, by U-universal NOTES Sec.5.2 and REFEREE Sec.2.6, yield U<=a/(1-b) I by restriction induction and then H<=(2+2a/(1-b))I via Theorem G. This restricted claim DOES NOT prove a global pair or FEI; the failure at (a,b)=(2,0) is not a failure of FEI.

## Exact graph law for ANY Boolean phase h (PROVED locally)
For arbitrary m>=1 and h:{0,1}^m->{0,1}, define F_h(x,z,y)=(-1)^(x·z+y h(x)). Summing the Walsh transform first in z enforces x=B; summing in y enforces Y=h(B). Thus
  Fhat_h(A,B,Y)=2^-m (-1)^(A·B) 1[Y=h(B)].
Its spectral probability law has mass 4^-m at each (A,B,h(B)), A and B independent uniform m-bit strings. Put mu=P(h(B)=1) and alpha(B)=P_{B' uniform given B'>=B}(h(B')=1). Where h(B)=1, alpha(B)>0. By factoring uniform A and computing upper-set masses in (B,Y),
  I(F_h)=m+mu,
  U(F_h)=m+Q(h), Q(h)=E_B[h(B) log2 alpha(B)]<=0,
  Delta_y U=Q(h).
So the selector drift is ALWAYS nonpositive throughout this arbitrary-phase bent-lift class. This is only the selector; it does not bound total GU.

For x_j=a, the physical restriction is a z_j character times a smaller (m-1)-lift for h_a. Characters have U=0. Hence
  Delta_xj U=1+Q(h)-[Q(h_0)+Q(h_1)]/2.
Let alpha_a(b)=P_{b'>=b}[h_a(b')=1] for the m-1 remaining B bits. Since alpha((0,b))=(alpha_0(b)+alpha_1(b))/2 and alpha((1,b))=alpha_1(b),
  Delta_xj U=1+(1/2)E_b[h_0(b)log2((alpha_0(b)+alpha_1(b))/(2alpha_0(b)))].
The last summand is 0 when h_0(b)=0, so no 0/0 is evaluated.

For z_j=a, let b=B_-j and W the retained x_j spectral bit. B_-j and A_-j remain independent uniform; conditional on b, (W,Y) is a POINT at (a,h_0(b)) if h_0(b)=h_1(b), and is UNIFORM on all FOUR pairs if they differ. This is the squared two-bit Walsh transform of (-1)^(a x_j+y h(x_j,b)), not a guessed disjoint-spectrum approximation. Writing P_a^j for this (b,W,Y) law gives
  U(F_h|z_j=a)=(m-1)/2+U(P_a^j).
These x, z and y equations are the complete physical-coordinate selector ledger for arbitrary h.

## Two-antipodal exact specialization
Set r=m-1, N=2^r, L=log2(N-1). The only h-positive Fourier B are bottom and top. At bottom alpha=1/N; at top alpha=1. Consequently:
  I=m+1/N; U=m-r/(2N); Delta_y=-r/(2N).
The two x-restriction phases are a bottom-only and a top-only defect, with Q=-r/N and Q=0. Therefore Delta_xj=1 for every j.

For either z_j, b=0^r or b=1^r produces the four-point uniform (W,Y) conditional spectrum, while all other b give (W,Y)=(a,0). Upper-cone counting (including both exceptional b and B=empty) yields
  Z0=U(F|z_j=0)=r+(11-3r)/(4N),
  Z1=U(F|z_j=1)=r+(11-3r+L)/(4N)
      +(1/N) Σ_{k=1}^{r-1} C(r,k)log2(1-2^(-(r-k+1))).
Write D_r=(Z0+Z1)/2-r. Then
  D_r=(11-3r)/(4N)+L/(8N)
      +(1/(2N)) Σ_{k=1}^{r-1} C(r,k)log2(1-2^(-(r-k+1))),
  Delta_zj=1-r/(2N)-D_r,
  G=2m-((m+1)r)/(2N)-m D_r.
All m x, m z and selector contributions are included.

## Rigorous 9/4 uniform bound
For integers t>=1, log2(1-2^(-t-1))>=-2^-t: phi(u)=log2(1-u)+2u is concave on [0,1/4] and nonnegative at endpoints (3/4 >= 1/sqrt(2)). Therefore
  D_r >= (11-3r)/(4*2^r) -(1/2)(3/4)^r.
At r=1,2,3 the RHS is 5/8, 1/32, -19/128. For r>=4, (3r-11)/(4*2^r)<=1/32, by r=4,5 bases and induction (3(r+1)-11)<=2(3r-11) for r>=5. Also (1/2)(3/4)^r<=81/512. Therefore D_r>=-97/512 > -1/4. It follows Delta_zj<=5/4; Delta_xj=1; Delta_y<=0. Hence
  G<=m*(1+5/4)=(9/4)m<=(9/4) I,
for every integer m>=2, a constant independent of dimension and the vanishing branch gap.

## Exact failure of coefficient two
For 0<u<1, log2(1-u)<=-u, and 0<=L<=r. Summing the binomial upper bound gives
  D_r <=[13-(5/2)r-(3/2)^r]/(4N).
Substitution into G-2I yields
  4N(G-2I) >= m((3/2)^r-13)+(m/2-2)r-8.
If r>=7 then (3/2)^r>17 and m=r+1>=8; RHS>4m+(m/2-2)r-8>0. Hence G>2I for every m>=8. The exact formulas also imply G/I→2 and gap→0 as m→infinity. This rejects only the particular helper (a,b)=(2,0), not a larger coefficient, not GU' with b>0, not FEI.

## Actual checks, sources, and status
Stdlib CHECKER.py: exact integer Walsh/Parseval/complete physical restrictions m=2..6; exact Fraction inequalities through r=399 as diagnostic plus analytic all-r proofs above; log2 formula evaluations m=7..14 float64 only. Actual run CHECK_OUTPUT.txt: 57,717 assertions, zero failures. No evaluation items/answer banks.
Primary pins (Git blob SHAs):
 ORDER.md 231e48480d53b8d868ecd85105e19cc3efe5b5ff;
 GU_LASER_FOCUS_20261014.md 9448198701fbfe0cceb72bda7a6837ebd59704f9;
 CASE_TARGETS.json 97e41262ebb4f09eec53630a918acae09efc9a48;
 gu/U-universal/NOTES.md 3b0636c653c7818368eeb204011c3e1ff21c234e;
 gu/U-universal/REFEREE.md 87326516f71374bb2b37d593952be7ec581ee0f1;
 2026-10-14-fei-gap-audit-0330Z/REPORT.md 675455e235986825c7243b06931c9a2d128fe7c6.
New class extension not independently novelty-certified. Prior indicator coefficient-four refutation unchanged. Full FEI=OPEN. Independent review=NOT_RUN; native ingestion=NOT_OBSERVED. B04 next: bound the exact joint x/z remainder for phase supports E growing with m, with no fresh/disjoint assumption; B20 review and propagate if accepted.