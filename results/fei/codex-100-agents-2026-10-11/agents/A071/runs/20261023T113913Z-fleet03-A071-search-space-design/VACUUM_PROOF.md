# Universal empty-coefficient component payment

This lemma pays one entropy component; it does not bound the nonempty spectrum or settle FEI.

Let phi(t)=-t^2 log2(t^2), phi(0)=0, on[-1,1]. Its derivative is

    phi'(t)=-(2t/ln2)(ln(t^2)+1).

It extends continuously at0. For0<=t<=1, |t(ln(t^2)+1)|<=1. Above exp(-1/2), use0<=ln(t^2)+1<=1. Below that point the absolute value is-2t ln(t)-t; its maximum is2exp(-3/2)<1. Evenness handles negative t. Thus phi is globally2/ln2-Lipschitz. The positive atanh series gives ln2=2sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3, hence2/ln2<3.

For EVERY Boolean f on EVERY uniform cube, let mu=E f, and let mu_0,mu_1 be the means of its full physical-query children, at influence d. Direct coupling gives |mu_0-mu_1|<=2d. Also mu=(mu_0+mu_1)/2, so

    mean phi(mu_b)-phi(mu) <= (2/ln2)d <=3d.

Influence telescoping I(f)=d+mean I(f_b) proves that

    V(f)=phi(E f)+3I(f) >= mean V(f_b)

for every physical query. At d=0 the two functions coincide and equality holds; constants cause no exception. This is a full-universe superharmonic envelope for the EMPTY Fourier entropy term phi(E f), not for the whole FEI deficit.

The elementary inequality-u ln u<=1-u gives phi(mu)<=(1-mu²)/ln2. By Parseval, Var(f)=1-mu²<=I(f). Since ln2>2/3,

    0<=phi(mu)<=3I(f)/2,
    0<=V(f)<=9I(f)/2.

The sharper exact constants are V*=phi(mu)+(2/ln2)I and V*<=(3/ln2)I. The rational constants above avoid numerical log assumptions. Any influence owner used for this component must actually be UNUSED at the current account; this lemma does not renew previously spent stock.

On the saved seven-bit witness the empty squared coefficients are1/4096 at the parent,25/1024 and1/64 at the full children. Their entropy-term drift is

    G_empty=85/512-(25/1024)log2(5).

Subtracting this from the full candidate drift leaves

    G_nonempty=-1269/512-(567/512)log2(3)+(3087/2048)log2(7)<0,

exactly certified by7^3087<2^5076*3^2268. Hence the empty term explains ALL positive drift on this witness. The global component lemma prices that term from influence. It does NOT establish that the remaining nonempty correction is coherent or influence-priced on other functions; nonempty Fourier coefficients can also cancel.

NEXT: retain this complete empty-term payment and test the nonempty signed correction plus pivotal inner hulls near a NONEMPTY coefficient cancellation. Both full terminals, old debit labels and the same actually unused influence source must remain. A fresh root reserve would conceal the history-transfer issue.
