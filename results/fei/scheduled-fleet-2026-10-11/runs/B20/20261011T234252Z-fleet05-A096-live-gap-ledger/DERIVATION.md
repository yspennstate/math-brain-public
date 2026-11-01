# Universal level-one-to-two payment: candidate proof saved immediately

For every uniform Boolean sign f, put a_S=hat f(S), epsilon_i=Inf_i(f), W2=sum_{i<j}a_{ij}^2, H2=sum_{i<j}a_{ij}^2 log2(1/a_{ij}^2), and T12=sum_{i!=j}phi(a_i^2,a_{ij}^2), phi(x,y)=x log2(1+y/x)+y log2(1+x/y) with zero terms by continuity.

1. Boolean sparse derivative: h_i=(f|x_i=+1-f|x_i=-1)/2 is 0,+1,-1; its support has probability epsilon_i. For L_i=sum_{j!=i}a_{ij} x_j, E[h_i L_i]=E L_i^2=d_i:=sum_{j!=i}a_{ij}^2. The Rademacher mgf obeys E exp(t L_i)<=exp(t^2 d_i/2), hence E exp(t|L_i|)<=2exp(t^2d_i/2). Conditional Jensen on the support gives E[|L_i||h_i!=0]<=ln(2/epsilon_i)/t+t d_i/2. Optimizing t yields d_i<=epsilon_i sqrt(2d_i ln(2/epsilon_i)), thus

    d_i<=2 epsilon_i^2 ln(2/epsilon_i).

All zero cases are handled separately. This is the exact Booleanity input; it fails for arbitrary L2-normalized real spectral vectors.

2. With I=sum epsilon_i>0, Q({i,j})=2 epsilon_i epsilon_j/I^2 is a subprobability law on pairs. Normalize the level-two masses to P=a_{ij}^2/W2 when W2>0 and apply Gibbs:

    H2<=sum_i d_i log2(1/epsilon_i)+W2 log2(I^2/(2W2)).

For t=-ln epsilon_i, the first term is at most

    K1 I, K1=8/(e^2 ln2)+2/e,

since 2 epsilon_i ln(2/epsilon_i) log2(1/epsilon_i)=2exp(-t)(t^2+t ln2)/ln2 and sup t^2exp(-t)=4/e^2, sup t exp(-t)=1/e.

3. For z>0, ln z<=2 sqrt(z)/e. Parseval gives W2<=1, so

    W2 log2(I^2/(2W2))<=sqrt(2)/(e ln2) I sqrt(W2)<=sqrt(2)/(e ln2) I.

Thus H2<=K2 I, K2=8/(e^2 ln2)+2/e+sqrt(2)/(e ln2).

4. Each parent edge has x+y<=1. Since x ln(1+y/x)<=y,

    phi(x,y)<=y log2(1/y)+y/ln2.

Every pair is counted twice, and 2W2<=I. Consequently

    T12<=2H2+2W2/ln2<=K12 I,
    K12=16/(e^2 ln2)+4/e+2sqrt(2)/(e ln2)+1/ln2<8.

The last strict rational certificate uses e>27/10 (exponential series through 1/120), ln2>69/100 (atanh series at 1/3 through cubic gives 56/81), and sqrt2<71/50. No numerical log sign is needed for this universal proof. The target is therefore paid universally, with no structural class restriction. Still unproved: the sum of edges beginning at levels at least two is <=K I with one absolute K.
