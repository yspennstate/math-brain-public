#include <bits/stdc++.h>
using namespace std;
struct A { int x,y,dh,c,m; long long hb,lb,rb; };
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
    vector<A> as; as.reserve(654);
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40, c=(11*x+9*y)/40, m=max(x,y);
        as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});
    }
    int sr=R-r; vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1); int stable=-1;
    for(int h=1;h<=H;h++){
        bool same=true;
        for(int k=0;k<=M;k++){
            long long br=0,bs=0;
            for(const auto&a:as){
                int kh=k+a.dh; long long HR=a.hb+(kh<=M?pr[kh]:0), HS=a.hb+(kh<=M?ps[kh]:0),LR,LS;
                if(k>=a.c){LR=a.lb+pr[k-a.c];LS=a.lb+ps[k-a.c];}
                else {int kl=a.c-k-1; long long xr=1LL*k*R+r,xs=1LL*k*R+sr; LR=a.rb-40LL*xr*Q+ps[kl]; LS=a.rb-40LL*xs*Q+pr[kl];}
                br=max(br,min(HR,LR)); bs=max(bs,min(HS,LS));
            }
            cr[k]=br; cs[k]=bs; if(cr[k]!=pr[k]||cs[k]!=ps[k]) same=false;
        }
        if(same){stable=h;break;} pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps),stable};
}
static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){
    vector<A> as; as.reserve(654);
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);
        as.push_back({x,y,dh,c,m,9LL*x*Q-10LL*P*m,-11LL*x*Q-10LL*P*m,9LL*y*Q-10LL*P*m});
    }
    vector<long long> pr(M+1),cr(M+1);
    for(int h=1;h<=H;h++){
        bool same=true;
        for(int k=0;k<=M;k++){
            long long best=0;
            for(auto&a:as){long long hi=a.hb+((k+a.dh<=M)?pr[k+a.dh]:0),lo;if(k>=a.c)lo=a.lb+pr[k-a.c];else lo=a.rb-40LL*k*Q+pr[a.c-k];best=max(best,min(hi,lo));}
            cr[k]=best; if(cr[k]!=pr[k]) same=false;
        }
        if(same)break; pr.swap(cr);
    }
    return pr;
}
int main(){
    const long long P=1007,Q=240000; const int M=20401, PAD=3840, MAXD=600;
    auto fi=integer_table(P,Q); vector<Orbit> os(5); for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);
    auto F0=[&](int J)->long long{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return fi[k]*8;if(r<=4)return os[r].r[k];return os[8-r].s[k];};
    auto RH=[&](int p){return 8LL*(45LL*p*Q-9600LL*P);};
    auto RL=[&](int p){return 8LL*(-55LL*p*Q-9600LL*P);};
    auto RR=[&](int J){return 8LL*(8640LL*Q-9600LL*P)-40LL*Q*J;};
    const long long T8=8LL*(12480LL*Q+28800LL*P);

    vector<long long> prev(M+1),cur(M+1); for(int J=0;J<=M;J++) prev[J]=F0(J);
    int firstRoot=-1, stable=-1; long long gap332=LLONG_MIN,gap333=LLONG_MIN,gap413=LLONG_MIN,gap414=LLONG_MIN;
    for(int d=1;d<=MAXD;d++){
        bool same=true;
        for(int J=0;J<=M;J++){
            long long best=LLONG_MIN;
            for(int p=0;p<=192;p++){
                int dh=9*p+2112,c=11*p+1728; int jh=J+dh,jl=abs(J-c);
                long long hi=RH(p)+(jh<=M?prev[jh]:0);
                long long lo=(J>=c?RL(p):RR(J))+(jl<=M?prev[jl]:0);
                best=max(best,min(hi,lo));
            }
            cur[J]=max(F0(J),best); if(cur[J]!=prev[J]) same=false;
        }
        prev.swap(cur); long long g=prev[3840]-T8;
        if(firstRoot<0 && g>=0) firstRoot=d;
        if(d==332)gap332=g; if(d==333)gap333=g; if(d==413)gap413=g; if(d==414)gap414=g;
        if(same){stable=d;break;}
    }
    if(stable<0) return 2;
    vector<long long> h=prev;
    bool coreEq=true, tailZero=true, f0TailZero=true; long long maxTailBell=LLONG_MIN; int maxTailJ=-1,maxTailP=-1;
    int maxnz=-1; for(int J=0;J<=M;J++)if(h[J]>0)maxnz=J;
    for(int J=0;J<=M;J++){
        long long best=LLONG_MIN;
        for(int p=0;p<=192;p++){
            int dh=9*p+2112,c=11*p+1728,jh=J+dh,jl=abs(J-c);
            long long hi=RH(p)+(jh<=M?h[jh]:0),lo=(J>=c?RL(p):RR(J))+(jl<=M?h[jl]:0);
            best=max(best,min(hi,lo));
        }
        if(max(F0(J),best)!=h[J]){coreEq=false;break;}
    }
    for(int J=M+1;J<=M+PAD;J++){
        if(F0(J)!=0) f0TailZero=false;
        long long best=LLONG_MIN; int bp=-1;
        for(int p=0;p<=192;p++){
            int dh=9*p+2112,c=11*p+1728,jl=J-c;
            long long hi=RH(p),lo=RL(p)+(jl>=0&&jl<=M?h[jl]:0),v=min(hi,lo);
            if(v>best){best=v;bp=p;}
        }
        if(best>maxTailBell){maxTailBell=best;maxTailJ=J;maxTailP=bp;}
        if(best>0){tailZero=false;break;}
    }
    auto diag=[&](int J){long long best=LLONG_MIN,hi0=0,lo0=0;int bp=-1;for(int p=0;p<=192;p++){int dh=9*p+2112,c=11*p+1728,jh=J+dh,jl=abs(J-c);long long hi=RH(p)+(jh<=M?h[jh]:0),lo=(J>=c?RL(p):RR(J))+(jl<=M?h[jl]:0),v=min(hi,lo);if(v>best){best=v;bp=p;hi0=hi;lo0=lo;}}return tuple<long long,int,long long,long long>(best,bp,hi0,lo0);};
    auto [frontBest,frontP,frontH,frontL]=diag(M); auto [rootBest,rootP,rootH,rootL]=diag(3840);
    if(!coreEq||!tailZero||!f0TailZero) return 3;
    if(maxnz!=M || stable!=414 || firstRoot!=333 || gap333!=0 || h[3840]!=T8) return 4;
    cout<<"I0130_B13_B11_B24_INFINITE_RESTRICTED_FIXED_POINT_PASS\n";
    cout<<"epsilon=1007/240000\n";
    cout<<"finite_support_max_J="<<maxnz<<"\n";
    cout<<"global_stabilization_depth="<<stable<<"\n";
    cout<<"first_root_threshold_depth="<<firstRoot<<"\n";
    cout<<"depth332_gap8="<<gap332<<" depth333_gap8="<<gap333<<"\n";
    cout<<"depth413_gap8="<<gap413<<" depth414_gap8="<<gap414<<"\n";
    cout<<"root_value="<<h[3840]<<" threshold="<<T8<<" root_action="<<rootP<<" root_hi="<<rootH<<" root_lo="<<rootL<<"\n";
    cout<<"frontier_J="<<M<<" value="<<h[M]<<" action="<<frontP<<" hi="<<frontH<<" lo="<<frontL<<"\n";
    cout<<"tail_strip_max_bellman="<<maxTailBell<<" at_J="<<maxTailJ<<" p="<<maxTailP<<"\n";
    cout<<"analytic_tail_after_J="<<(M+PAD)<<" : low immediate reward <0 for every p, hence Bellman <=0\n";
    cout<<"delta=25007/240000\n";
    cout<<"U_MIV_after=214993/240000\n";
    cout<<"L_MIV=19/30\n";
    cout<<"W_MIV_after=62993/240000\n";
    cout<<"U_MIV_before=1721/1920\n";
    cout<<"exact_improvement=11/20000\n";
    cout<<"finite_witness_max_total_goods=948\n";
}
