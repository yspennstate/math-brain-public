#include <bits/stdc++.h>
using namespace std;
struct Act { int x,y,dh,c,m; long long hb,lb,rb; };
struct Orbit { vector<long long> r,s; int stable=-1; };
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
    vector<Act> as; as.reserve(654);
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
                int kh=k+a.dh; long long HR=a.hb+(kh<=M?pr[kh]:0), HS=a.hb+(kh<=M?ps[kh]:0),LR,LS;
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
    vector<Act> as; as.reserve(654);
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
static string s128(__int128 x){
    if(x==0) return "0"; bool neg=x<0; if(neg)x=-x; string s;
    while(x){s.push_back(char('0'+x%10));x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s;
}
int main(){
    const long long P=7841,Q=1860480;
    const int M=20401, PAD=3840, MAXD=500;
    auto fi=integer_table(P,Q); vector<Orbit> os(5);
    #pragma omp parallel for schedule(static)
    for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);
    auto F0=[&](int J)->long long{
        if(J<0)J=-J; int k=J/8,r=J%8; if(k>=2600)return 0;
        if(r==0)return fi[k]*8; if(r<=4)return os[r].r[k]; return os[8-r].s[k];
    };
    auto RH=[&](int p){return 8LL*(45LL*p*Q-9600LL*P);};
    auto RL=[&](int p){return 8LL*(-55LL*p*Q-9600LL*P);};
    auto RR=[&](int J){return 8LL*(8640LL*Q-9600LL*P)-40LL*Q*J;};
    const long long T8=8LL*(12480LL*Q+28800LL*P);
    vector<long long> prev(M+1),cur(M+1); for(int J=0;J<=M;J++)prev[J]=F0(J);
    int stable=-1;
    for(int d=1;d<=MAXD;d++){
        int diff=0;
        #pragma omp parallel for schedule(static) reduction(|:diff)
        for(int J=0;J<=M;J++){
            long long best=LLONG_MIN;
            for(int p=0;p<=192;p++){
                int dh=9*p+2112,c=11*p+1728,jh=J+dh,jl=abs(J-c);
                long long hi=RH(p)+(jh<=M?prev[jh]:0);
                long long lo=(J>=c?RL(p):RR(J))+(jl<=M?prev[jl]:0);
                best=max(best,min(hi,lo));
            }
            cur[J]=max(F0(J),best); if(cur[J]!=prev[J])diff=1;
        }
        prev.swap(cur); if(!diff){stable=d;break;}
    }
    if(stable<0) return 2;
    vector<long long> h=prev;
    bool coreEq=true,tailZero=true,f0TailZero=true;
    long long maxTailBell=LLONG_MIN; int maxTailJ=-1,maxTailP=-1,maxnz=-1;
    for(int J=0;J<=M;J++) if(h[J]>0) maxnz=J;
    for(int J=0;J<=M;J++){
        long long best=LLONG_MIN;
        for(int p=0;p<=192;p++){
            int dh=9*p+2112,c=11*p+1728,jh=J+dh,jl=abs(J-c);
            long long hi=RH(p)+(jh<=M?h[jh]:0);
            long long lo=(J>=c?RL(p):RR(J))+(jl<=M?h[jl]:0);
            best=max(best,min(hi,lo));
        }
        if(max(F0(J),best)!=h[J]){coreEq=false;break;}
    }
    for(int J=M+1;J<=M+PAD;J++){
        if(F0(J)!=0) f0TailZero=false;
        long long best=LLONG_MIN; int bp=-1;
        for(int p=0;p<=192;p++){
            int c=11*p+1728,jl=J-c;
            long long hi=RH(p),lo=RL(p)+(jl>=0&&jl<=M?h[jl]:0),v=min(hi,lo);
            if(v>best){best=v;bp=p;}
        }
        if(best>maxTailBell){maxTailBell=best;maxTailJ=J;maxTailP=bp;}
        if(best>0){tailZero=false;break;}
    }
    if(!coreEq||!tailZero||!f0TailZero) return 3;
    const long long A=7193,B=11628; const int J0=3840;
    long long hi_num_state=J0*B+1728*A+2112*B;
    long long lo_num_state=J0*B-2112*A-1728*B;
    int jh=(int)((hi_num_state+B-1)/B), jl=(int)((lo_num_state+B-1)/B);
    __int128 rootHi=(__int128)B*h[jh] + (__int128)8*(8640LL*Q*A-9600LL*P*B);
    __int128 rootLo=(__int128)B*h[jl] + (__int128)8*(-10560LL*Q*A-9600LL*P*B);
    __int128 rootT=(__int128)B*T8;
    if(jh!=7021||jl!=806||rootHi!=rootT||rootLo!=rootT) return 4;
    const long long A2=871,B2=3840; const int J2=9908;
    long long hi2_num_state=J2*B2+1728*A2+2112*B2;
    long long lo2_num_state=J2*B2-2112*A2-1728*B2;
    int jh2=(int)((hi2_num_state+B2-1)/B2),jl2=(int)((lo2_num_state+B2-1)/B2);
    __int128 sepHi=(__int128)B2*h[jh2]+(__int128)8*(8640LL*Q*A2-9600LL*P*B2);
    __int128 sepLo=(__int128)B2*h[jl2]+(__int128)8*(-10560LL*Q*A2-9600LL*P*B2);
    __int128 h2=(__int128)B2*h[J2];
    __int128 sepGain=min(sepHi,sepLo)-h2;
    if(jh2!=12412||jl2!=7701||sepGain!=(__int128)B2*368375040LL||sepGain<=0) return 5;
    if((__int128)10*193889 != (__int128)Q+10*P) return 6;
    if(1860480LL-193889LL!=1666591LL) return 7;
    if((__int128)1666591*30-(__int128)19*1860480 != (__int128)488287*30) return 8;
    if((__int128)214993*1860480-(__int128)1666591*240000 != (__int128)2171*3840) return 9;
    cout<<"I0130_B19_B11_B24_CONTINUOUS_SEPARATOR_PASS\n";
    cout<<"epsilon=7841/1860480\n";
    cout<<"restricted_fixed_point_stabilization_depth="<<stable<<"\n";
    cout<<"restricted_support_max_J="<<maxnz<<"\n";
    cout<<"tail_strip_max_bellman="<<maxTailBell<<" at_J="<<maxTailJ<<" p="<<maxTailP<<"\n";
    cout<<"root_restricted_h="<<h[J0]<<" threshold="<<T8<<"\n";
    cout<<"root_continuous_action_a=7193/11628 b=1\n";
    cout<<"root_children_exact=2267760/323,780560/969 ceils="<<jh<<","<<jl<<"\n";
    cout<<"root_h_ceils="<<h[jh]<<","<<h[jl]<<"\n";
    cout<<"root_branch_lower_num_H="<<s128(rootHi)<<" L="<<s128(rootLo)<<" threshold_num="<<s128(rootT)<<"\n";
    cout<<"internal_separator_J=9908 a=871/3840 b=1\n";
    cout<<"internal_children_exact=248239/20,154019/20 ceils="<<jh2<<","<<jl2<<"\n";
    cout<<"internal_h_ceils="<<h[jh2]<<","<<h[jl2]<<" h_state="<<h[J2]<<"\n";
    cout<<"internal_branch_lower_each="<<s128(sepHi/B2)<<" strict_gain="<<s128(sepGain/B2)<<"\n";
    cout<<"delta=193889/1860480\n";
    cout<<"U_MIV_after=1666591/1860480\n";
    cout<<"L_MIV=19/30\n";
    cout<<"W_MIV_after=488287/1860480\n";
    cout<<"U_MIV_before=214993/240000\n";
    cout<<"exact_improvement=2171/116280000\n";
    cout<<"finite_witness_max_total_goods="<<(3+1+stable+612)<<"\n";
    cout<<"NOTE: continuous branch bounds use the previously proved finite-horizon nonincreasing continuation theorem: F_d(x)>=F_d(ceil x).\n";
}
