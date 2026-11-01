#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
struct BaseAct { int x,y,dh,c,m; long long hb,lb,rb; };
struct Orbit { vector<long long> r,s; int stable=-1; };
struct RatAct { long long A,B; };
static vector<pair<int,int>> old654_points(){
    vector<pair<int,int>> ps;
    for(int i=0;i<=24;i++) for(int j=0;j<=24;j++) ps.push_back({40*i,40*j});
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:ex) ps.push_back({4*p[0],4*p[1]});
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};
    for(auto &p:cut) ps.push_back({p[0],p[1]});
    return ps;
}
static Orbit orbit_table(long long P,long long Q,int R,int r,int M=2600,int H=612){
    vector<BaseAct> as; as.reserve(654);
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);
        as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});
    }
    int sr=R-r; vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1); int stable=-1;
    for(int h=1;h<=H;h++){
        int diff=0;
        #pragma omp parallel for schedule(static) reduction(|:diff)
        for(int k=0;k<=M;k++){
            long long br=0,bs=0;
            for(const auto&a:as){
                int kh=k+a.dh;
                long long HR=a.hb+(kh<=M?pr[kh]:0), HS=a.hb+(kh<=M?ps[kh]:0),LR,LS;
                if(k>=a.c){LR=a.lb+pr[k-a.c];LS=a.lb+ps[k-a.c];}
                else {int kl=a.c-k-1; long long xr=1LL*k*R+r,xs=1LL*k*R+sr; LR=a.rb-40LL*xr*Q+ps[kl]; LS=a.rb-40LL*xs*Q+pr[kl];}
                br=max(br,min(HR,LR)); bs=max(bs,min(HS,LS));
            }
            cr[k]=br; cs[k]=bs; if(cr[k]!=pr[k]||cs[k]!=ps[k]) diff=1;
        }
        if(!diff){stable=h;break;} pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps),stable};
}
static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){
    vector<BaseAct> as; as.reserve(654);
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);
        as.push_back({x,y,dh,c,m,9LL*x*Q-10LL*P*m,-11LL*x*Q-10LL*P*m,9LL*y*Q-10LL*P*m});
    }
    vector<long long> pr(M+1),cr(M+1);
    for(int h=1;h<=H;h++){
        int diff=0;
        #pragma omp parallel for schedule(static) reduction(|:diff)
        for(int k=0;k<=M;k++){
            long long best=0;
            for(const auto&a:as){
                long long hi=a.hb+((k+a.dh<=M)?pr[k+a.dh]:0),lo;
                if(k>=a.c) lo=a.lb+pr[k-a.c];
                else lo=a.rb-40LL*k*Q+pr[a.c-k];
                best=max(best,min(hi,lo));
            }
            cr[k]=best; if(cr[k]!=pr[k]) diff=1;
        }
        if(!diff) break; pr.swap(cr);
    }
    return pr;
}
static long long gcdll(long long a,long long b){return b?gcdll(b,a%b):a;}
static long long lcmll(long long a,long long b){return a/gcdll(a,b)*b;}
static long long ceil_rat(long long num,long long den){ if(num>=0)return (num+den-1)/den; return num/den; }
static string s128(__int128 x){ if(x==0)return"0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back(char('0'+x%10));x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }
static __int128 gcd128(__int128 a,__int128 b){ if(a<0)a=-a;if(b<0)b=-b; while(b){__int128 t=a%b;a=b;b=t;} return a; }

struct ActI{
    bool base;
    int p;
    long long A,B,mul;
    int dhceil,cfloor,cceil;
    long long rh,rl;
};
struct FixRes{
    vector<long long> h;
    vector<ActI> acts;
    int stable=-1,maxnz=-1,maxC=0;
    long long scale=1;
    long long tailMax=LLONG_MIN; int tailJ=-1,tailAct=-1;
    long long minDrop=LLONG_MAX,maxDrop=LLONG_MIN; int monoBad=0,lipBad=0;
};

static FixRes fixed_augmented(long long P,long long Q,int M=25000,int MAXD=700){
    vector<RatAct> extra={{7193,11628},{871,3840}};
    long long S=1; for(auto z:extra)S=lcmll(S,z.B);
    auto fi=integer_table(P,Q); vector<Orbit> os(5);
    #pragma omp parallel for schedule(static)
    for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);
    auto F0=[&](int J)->long long{
        if(J<0)J=-J; int k=J/8,r=J%8; if(k>=2600)return 0;
        if(r==0)return fi[k]*8*S;
        if(r<=4)return os[r].r[k]*S;
        return os[8-r].s[k]*S;
    };
    vector<ActI> acts; acts.reserve(195);
    for(int p=0;p<=192;p++){
        int dh=9*p+2112,c=11*p+1728;
        acts.push_back({true,p,p,192,S,dh,c,c,8LL*(45LL*p*Q-9600LL*P)*S,8LL*(-55LL*p*Q-9600LL*P)*S});
    }
    for(auto z:extra){
        long long A=z.A,B=z.B,mul=S/B;
        long long hnum=1728*A+2112*B,cnum=2112*A+1728*B;
        int dh=(hnum+B-1)/B,cf=cnum/B,cc=(cnum+B-1)/B;
        long long rh=8LL*(8640LL*Q*A-9600LL*P*B)*mul;
        long long rl=8LL*(-10560LL*Q*A-9600LL*P*B)*mul;
        acts.push_back({false,-1,A,B,mul,dh,cf,cc,rh,rl});
    }
    int maxC=0;for(auto&a:acts)maxC=max(maxC,a.cceil);
    auto bell=[&](int J,const vector<long long>&v,int *arg)->long long{
        long long best=LLONG_MIN; int bi=-1;
        for(int ii=0;ii<(int)acts.size();ii++){
            auto&a=acts[ii]; int jh=J+a.dhceil; long long hi=a.rh+(jh<(int)v.size()?v[jh]:0),lo;
            if(a.base){int c=a.cfloor;if(J>=c)lo=a.rl+v[J-c];else{int jl=c-J; long long rr=8LL*(8640LL*Q-9600LL*P)*S-40LL*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}
            else{
                long long cnum=2112*a.A+1728*a.B;
                if((__int128)J*a.B>=cnum){int jl=J-a.cfloor;lo=a.rl+(jl<(int)v.size()?v[jl]:0);}
                else {int jl=a.cceil-J;long long rr=8LL*(8640LL*Q*a.B-9600LL*P*a.B)*a.mul-40LL*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}
            }
            long long z=min(hi,lo); if(z>best){best=z;bi=ii;}
        }
        if(arg)*arg=bi;return best;
    };
    vector<long long> prev(M+1),cur(M+1); for(int J=0;J<=M;J++)prev[J]=F0(J);
    int stable=-1;
    for(int d=1;d<=MAXD;d++){
        int diff=0;
        #pragma omp parallel for schedule(static) reduction(|:diff)
        for(int J=0;J<=M;J++){long long b=bell(J,prev,nullptr);cur[J]=max(F0(J),b);if(cur[J]!=prev[J])diff=1;}
        prev.swap(cur); if(!diff){stable=d;break;}
    }
    if(stable<0){cerr<<"no stabilization\n";exit(2);} int maxnz=-1;for(int J=0;J<=M;J++)if(prev[J]>0)maxnz=J;
    for(int J=0;J<=M;J++){long long z=max(F0(J),bell(J,prev,nullptr));if(z!=prev[J]){cerr<<"fixed mismatch "<<J<<"\n";exit(3);}}
    long long tailMax=LLONG_MIN;int tailJ=-1,tailAct=-1;
    int tailEnd=maxnz+maxC;if(tailEnd>M){cerr<<"M too small tailEnd="<<tailEnd<<"\n";exit(4);} 
    for(int J=maxnz+1;J<=tailEnd;J++){int a=-1;long long z=bell(J,prev,&a); if(F0(J)!=0){cerr<<"F0 tail nonzero "<<J<<"\n";exit(5);} if(z>tailMax){tailMax=z;tailJ=J;tailAct=a;} if(z>0){cerr<<"positive tail Bellman "<<J<<" "<<z<<"\n";exit(6);}}
    long long minDrop=LLONG_MAX,maxDrop=LLONG_MIN;int monoBad=0,lipBad=0;long long lip=40LL*Q*S;
    for(int J=0;J<M;J++){long long d=prev[J]-prev[J+1];minDrop=min(minDrop,d);maxDrop=max(maxDrop,d);if(d<0)monoBad++;if(d>lip)lipBad++;}
    if(monoBad||lipBad){cerr<<"shape failure\n";exit(7);} 
    return {move(prev),move(acts),stable,maxnz,maxC,S,tailMax,tailJ,tailAct,minDrop,maxDrop,monoBad,lipBad};
}

struct Sep{long long A=0,B=1,J=-1;__int128 valueNum=0,valueDen=1,gainNum=0,gainDen=1;};
static Sep exhaustive_b1(long long P,long long Q,const vector<long long>&h,long long S,int maxJ){
    vector<pair<long long,long long>> bp={{0,1},{1,1}};
    for(int k=1;k<1728;k++){long long g=gcdll(k,1728);bp.push_back({k/g,1728/g});}
    for(int k=1;k<2112;k++){long long g=gcdll(k,2112);bp.push_back({k/g,2112/g});}
    sort(bp.begin(),bp.end(),[](auto x,auto y){return (__int128)x.first*y.second<(__int128)y.first*x.second;});
    bp.erase(unique(bp.begin(),bp.end(),[](auto x,auto y){return (__int128)x.first*y.second==(__int128)y.first*x.second;}),bp.end());
    Sep global;global.gainNum=-((__int128)1<<120);global.gainDen=1;
    #pragma omp parallel
    {
        Sep loc;loc.gainNum=-((__int128)1<<120);loc.gainDen=1;
        auto consider=[&](int J,long long A,long long B){
            if(A<0||A>B)return;
            long long hn=J*B+1728*A+2112*B,ln=J*B-2112*A-1728*B;
            int jh=ceil_rat(hn,B),jl=ceil_rat(llabs(ln),B);
            __int128 H=(__int128)B*(jh<(int)h.size()?h[jh]:0)+(__int128)8*S*(8640LL*Q*A-9600LL*P*B);
            __int128 L;
            if(ln>=0)L=(__int128)B*(jl<(int)h.size()?h[jl]:0)+(__int128)8*S*(-10560LL*Q*A-9600LL*P*B);
            else L=(__int128)B*(jl<(int)h.size()?h[jl]:0)+(__int128)8*S*(8640LL*Q*B-9600LL*P*B)-(__int128)40*Q*J*S*B;
            __int128 v=min(H,L); __int128 g=v-(__int128)B*h[J];
            __int128 lhs=g*loc.gainDen,rhs=loc.gainNum*B; bool take=lhs>rhs;
            if(lhs==rhs){ if(loc.J<0||J<loc.J)take=true; else if(J==loc.J && (__int128)A*loc.B<(__int128)loc.A*B)take=true; }
            if(take)loc={A,B,J,v,B,g,B};
        };
        #pragma omp for schedule(dynamic,16)
        for(int J=0;J<=maxJ;J++){
            for(auto [A,B]:bp)consider(J,A,B);
            for(size_t i=0;i+1<bp.size();i++){
                auto [A1,B1]=bp[i];auto [A2,B2]=bp[i+1];
                long long Am=A1*B2+A2*B1,Bm=2*B1*B2;
                long long hn=J*Bm+1728*Am+2112*Bm,ln=J*Bm-2112*Am-1728*Bm;
                int jh=ceil_rat(hn,Bm),jl=ceil_rat(llabs(ln),Bm);
                long long HH=(jh<(int)h.size()?h[jh]:0),LL=(jl<(int)h.size()?h[jl]:0);
                __int128 n,d;
                if(ln>=0){n=(__int128)LL-HH;d=(__int128)8*S*19200LL*Q;}
                else {n=(__int128)LL-HH+(__int128)8*S*8640LL*Q-(__int128)40*Q*J*S;d=(__int128)8*S*8640LL*Q;}
                if(n<0||n>d)continue;__int128 g=gcd128(n,d);n/=g;d/=g;if(n>LLONG_MAX||d>LLONG_MAX)continue;
                long long A=(long long)n,B=(long long)d;
                if((__int128)A*B1<=(__int128)A1*B||(__int128)A*B2>=(__int128)A2*B)continue;
                consider(J,A,B);
            }
        }
        #pragma omp critical
        {__int128 lhs=loc.gainNum*global.gainDen,rhs=global.gainNum*loc.gainDen;bool take=lhs>rhs;
         if(lhs==rhs){if(global.J<0||loc.J<global.J)take=true;else if(loc.J==global.J&&(__int128)loc.A*global.B<(__int128)global.A*loc.B)take=true;}
         if(take)global=loc;}
    }
    return global;
}

int main(){
    const long long P=7860,Q=1860480; const int J0=3840;
    auto R=fixed_augmented(P,Q);
    const long long S=R.scale; const long long T8=8LL*(12480LL*Q+28800LL*P)*S;
    if(R.stable!=328||R.maxnz!=20320||S!=3720960) return 10;
    if(R.h[J0]-T8!=-443514617856000LL) return 11;
    if(R.monoBad||R.lipBad||R.maxDrop!=40LL*Q*S) return 12;

    auto E=exhaustive_b1(P,Q,R.h,S,R.maxnz+R.maxC);
    __int128 edgeGain=E.gainNum;
    if(edgeGain<=0){cerr<<"expected positive b=1 separator after only two columns\n";return 13;}

    const long long D=11162880,A=6858927,B=11100227;
    if(!((__int128)A*D<= (__int128)B*D && A>0 && B<D)) return 14;
    long long hn=J0*D+1728*A+2112*B,ln=J0*D-2112*A-1728*B;
    int jh=ceil_rat(hn,D),jl=ceil_rat(llabs(ln),D);
    if(jh!=7002||jl!=824||ln<=0) return 15;
    if((__int128)hn*2907!=(__int128)20354522*D) return 16;
    if(ln!=(long long)((__int128)824*D)) return 17;
    __int128 H=(__int128)D*R.h[jh]+(__int128)8*S*(8640LL*Q*A-9600LL*P*B);
    __int128 L=(__int128)D*R.h[jl]+(__int128)8*S*(-10560LL*Q*A-9600LL*P*B);
    __int128 TT=(__int128)D*T8;
    if(H!=L||H<=TT) return 18;
    __int128 gap=H-TT;
    if(gap!=(__int128)D*1761824870400LL) return 19;
    if((__int128)(R.h[jl]-R.h[jh])*1240320 != (__int128)762103*8*S*19200LL*Q) return 20;
    if((__int128)A*1240320!=(__int128)762103*D) return 21;
    if((__int128)B*11162880!=(__int128)11100227*D) return 22;

    if((__int128)7860*31008!=(__int128)131*1860480) return 23;
    if((__int128)10*16159*1860480 != (__int128)155040*(1860480+10*7860)) return 24;
    if(155040-16159!=138881) return 25;
    if(138881LL-19LL*(155040LL/30)!=40689LL || 40689LL!=3LL*13563LL || 155040LL!=3LL*51680LL) return 26;
    if(1666591LL-12LL*138881LL!=19LL || 1860480LL/19LL!=97920LL) return 27;

    cout<<"I0130_B19_B30_B3_COLUMN_GENERATION_PASS\n";
    cout<<"epsilon=7860/1860480=131/31008\n";
    cout<<"augmented_columns=(7193/11628,1),(871/3840,1)\n";
    cout<<"augmented_scale="<<S<<" stabilization_depth="<<R.stable<<" support_max_J="<<R.maxnz<<" max_cceil="<<R.maxC<<"\n";
    cout<<"shape_monotone_bad="<<R.monoBad<<" lipschitz_bad="<<R.lipBad<<" min_drop="<<R.minDrop<<" max_drop="<<R.maxDrop<<" lip_bound="<<(40LL*Q*S)<<"\n";
    cout<<"tail_strip_end="<<(R.maxnz+R.maxC)<<" tail_max_structural="<<R.tailMax<<" at_J="<<R.tailJ<<" action_index="<<R.tailAct<<"\n";
    cout<<"root_augmented_h="<<R.h[J0]<<" physical_threshold="<<T8<<" root_augmented_gap="<<(R.h[J0]-T8)<<"\n";
    cout<<"whole_b1_edge_best_gain_num="<<s128(E.gainNum)<<" gain_den="<<s128(E.gainDen)<<" at_J="<<E.J<<" a="<<E.A<<"/"<<E.B<<"\n";
    cout<<"root_interior_action=(762103/1240320,11100227/11162880) common_den_action=(6858927/11162880,11100227/11162880)\n";
    cout<<"root_children_exact=20354522/2907,824 ceils="<<jh<<","<<jl<<"\n";
    cout<<"root_h_ceils="<<R.h[jh]<<","<<R.h[jl]<<"\n";
    cout<<"root_branch_num_H="<<s128(H)<<" L="<<s128(L)<<" threshold_num="<<s128(TT)<<" positive_gap_num="<<s128(gap)<<" gap_per_action_den=1761824870400\n";
    cout<<"delta=16159/155040\n";
    cout<<"U_MIV_after=138881/155040\n";
    cout<<"L_MIV=19/30\n";
    cout<<"W_MIV_after=13563/51680\n";
    cout<<"U_MIV_before=1666591/1860480\n";
    cout<<"exact_improvement=1/97920\n";
    cout<<"finite_witness_max_total_goods="<<(3+1+R.stable+612)<<"\n";
    cout<<"B3_FIXED_TABLE_FINITE_BASIS: for fixed rational integer-state table h, full continuous one-step separation is finite rational polyhedral: lines 1728a+2112b=k, 2112a+1728b=k, a=b and reflection faces fix ceilings/sign/max; on each cell both branches are affine, so maxima occur at vertices or H=L edge intersections. This proves finite exact separation for fixed h, not finite termination across changing h tables.\n";
    cout<<"NOTE: recurrent non-grid columns and the source-root interior action use the proved finite-horizon nonincreasing 1-Lipschitz continuation inequality F_d(x)>=F_d(ceil x).\n";
    return 0;
}
