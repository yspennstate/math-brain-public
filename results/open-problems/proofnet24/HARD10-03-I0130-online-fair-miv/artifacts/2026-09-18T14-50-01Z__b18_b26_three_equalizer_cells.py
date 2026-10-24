from fractions import Fraction as F

# Exact local continuous-cell certificates that generated the three structural
# cuts used in the B3/B18/B26 I0130 run. Each cell is analyzed against the
# preceding finite-family robust fixed point.

def cell1():
    eps=F(1269,671810); D=F(66,240); v=F(459,240)
    phiD=F(3315511,1612344); p390=F(4708495,3224688); p391=F(23521099,16123440); pH=F(19931867,16123440)
    s=240*(p391-p390); assert s==F(-21376,67181)
    def br(u):
        m=(-9*u+11*v)/4
        H=F(99,40)*u-F(81,40)*v-eps*m+pH
        y=u-D
        L=F(-121,40)*u+F(99,40)*v-eps*m+(u-D)+p390+s*(y-F(390,240))
        return H,L
    H0,L0=br(F(0));H1,L1=br(F(1));Hu=H1-H0;Lu=L1-L0
    u=(L0-H0)/(Hu-Lu); assert u==F(98457649,51790480)
    H,L=br(u); assert H==L and F(390,240)<u-D<F(391,240) and D<u<v
    a=(11*u-9*v)/4; b=(-9*u+11*v)/4
    assert a==F(95795251,103580960) and b==F(101711691,103580960) and 0<a<b<1
    res=H-phiD; assert res==F(108250925567,10438008710640) and res>0
    Hv=-F(81,40)-F(11,4)*eps; Lv=F(99,40)-F(11,4)*eps
    lamH=-Lu/(Hu-Lu);lamL=Hu/(Hu-Lu)
    assert lamH==F(314264,647381) and lamL==F(333117,647381)
    dv=lamH*Hv+lamL*Lv; assert dv==F(12409481016,43491702961) and dv>0
    return u,a,b,res,lamH,lamL,dv

def cell2():
    eps=F(173,91570); D=F(506,240); u=F(366,240)
    scale=9600*91570
    phiD=F(1106459400,scale); pL=F(1682376800,scale); p891=F(655387000,scale); p892=F(654918600,scale)
    sh=240*(p892-p891); assert sh==F(-1171,9157)
    def br(v):
        m=(-9*u+11*v)/4
        H=F(99,40)*u-F(81,40)*v-eps*m+p891+sh*((D+v)-F(891,240))
        L=F(-121,40)*u+F(99,40)*v-eps*m+pL
        return H,L
    H0,L0=br(F(0));H1,L1=br(F(1));Hv=H1-H0;Lv=L1-L0
    v=(L0-H0)/(Hv-Lv); assert v==F(10877601,6780400)
    H,L=br(v); assert H==L and F(891,240)<D+v<F(892,240) and u<v
    a=(11*u-9*v)/4;b=(-9*u+11*v)/4
    assert a==F(15842801,27121600) and b==F(2417511,2465600) and 0<a<b<1
    res=H-phiD; assert res==F(363604111,33866248800) and res>0
    slow=F(-2940,9157)
    Hu=F(99,40)+F(9,4)*eps
    Lu=-F(121,40)+F(9,4)*eps-slow
    lamH=Lv/(Lv-Hv);lamL=-Hv/(Lv-Hv)
    assert lamH==F(4112,7705) and lamL==F(3593,7705)
    du=lamH*Hu+lamL*Lu; assert du==F(4530127,70554685) and du>0
    return v,a,b,res,lamH,lamL,du

def cell3():
    eps=F(1069,556010);D=F(770,240);v=F(358,240)
    scale=9600*556010
    phiD=F(4721978000,scale);p439=F(7342021600,scale);p440=F(7338206000,scale);p1127=F(2691555600,scale);p1128=F(2690745200,scale)
    slow=240*(p440-p439);sh=240*(p1128-p1127)
    assert slow==F(-9539,55601) and sh==F(-2026,55601)
    def br(u):
        m=(-9*u+11*v)/4
        H=F(99,40)*u-F(81,40)*v-eps*m+p1128
        y=D-u
        L=F(-121,40)*u+F(99,40)*v-eps*m+p439+slow*(y-F(439,240))
        return H,L
    H0,L0=br(F(0));H1,L1=br(F(1));Hu=H1-H0;Lu=L1-L0
    u=(L0-H0)/(Hu-Lu); assert u==F(3631259,2633480)
    H,L=br(u); assert H==L and F(439,240)<D-u<F(440,240) and u<v
    a=(11*u-9*v)/4;b=(-9*u+11*v)/4
    assert a==F(229469,526696) and b==F(1579453,1580088) and 0<a<b<1
    res=H-phiD; assert res==F(2117734643,219636182220) and res>0
    Hv=-F(81,40)-F(11,4)*eps+sh;Lv=F(99,40)-F(11,4)*eps
    lamH=-Lu/(Hu-Lu);lamL=Hu/(Hu-Lu)
    assert lamH==F(35203,65837) and lamL==F(30634,65837)
    dv=lamH*Hv+lamL*Lv; assert dv==F(161367793,3660603037) and dv>0
    return u,a,b,res,lamH,lamL,dv

for i,f in enumerate((cell1,cell2,cell3),1):
    z=f();print(f'cell{i}_PASS',*(str(x) for x in z))
print('I0130_B18_B26_THREE_EQUALIZER_CELLS_PASS')
