# A045 prime rare-boundary claim: scoped independent reconstruction

Verdict: HOLDS for the new A045-PRIME-RARE-BOUNDARY-RESERVE-OBSTRUCTION@1.
Original statement hash:9d6a1705eeee9f23e3ba41ec07db7e7878ac49ca87594362371c881b79bf6c56.
Original proof hash:f8d7501f6ab31569160bae0cd28af6bf006619e6cd72794559246a1bf91156e7.

Three count rows0,1,2 on any proper block of size at least2 and outside
counts0,1 give three different cofactor rows. Thus the T2 gate is prime.
Its core derivatives are(q0+q1)/2; its core-pair coefficient is(q0-q1)/2.
Union bounds give t>1/4, c12>=3/8 and both scales exactly1. A rare
derivative is(1/2)q'_0+(1/4)q'_1<=1/2, so I<=1+2m epsilon.
The mean stays in[-1/2,-1/4], hence Var>=3/4. With
a=binom(m,2)epsilon^2, J1/ln4>=1/2-a. Discarding only nonnegative L1
gives D=(Bstar+ln4R)/ln4<=4m epsilon+a<=5m epsilon.
The nonzero top coefficient gives R>0; Bstar>=0 is the already supplied
joint singleton premise. Since Jhi/ln4>=9/64, division by positive D
gives the stated9/(320m epsilon) bound, for every n>=3 and allowed epsilon.
The choice of epsilon after n is legitimate for the existential
counterfamily. No supremum or limiting interchange is used.

The independent checker uses A041's own exact centered transform, explicit
all-block cofactor rows and rational log intervals:12 cases,330 assertions.
No source checker is run or copied. The source's exception for all symmetric
thresholds remains valid. A041's previous singleton source is a dependency
authored by this reviewer; this review does NOT claim an independent
reacceptance of that upstream premise or of the entire universal FEI chain.
No repair is supplied to the reviewed version. The new nonsymmetric
extension is separated in PROOF.md and has no independent acceptance yet.
