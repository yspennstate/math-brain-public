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
        as.push_back({x,y,dh,c,m,
            (9LL*x*Q-10LL*P*m)*R,
            (-11LL*x*Q-10LL*P*m)*R,
            (9LL*y*Q-10LL*P*m)*R});
    }
    int sr=R-r;
    vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1);
    int stable=-1;
    for(int h=1;h<=H;h++){
        bool same=true;
        for(int k=0;k<=M;k++){
            long long br=0,bs=0;
            for(const auto &a:as){
                int kh=k+a.dh;
                long long HR=a.hb+(kh<=M?pr[kh]:0);
                long long HS=a.hb+(kh<=M?ps[kh]:0);
                long long LR,LS;
                if(k>=a.c){
                    LR=a.lb+pr[k-a.c];
                    LS=a.lb+ps[k-a.c];
                }else{
                    int kl=a.c-k-1;
                    long long xr=1LL*k*R+r, xs=1LL*k*R+sr;
                    LR=a.rb-40LL*xr*Q+ps[kl];
                    LS=a.rb-40LL*xs*Q+pr[kl];
                }
                br=max(br,min(HR,LR));
                bs=max(bs,min(HS,LS));
            }
            cr[k]=br; cs[k]=bs;
            if(cr[k]!=pr[k]||cs[k]!=ps[k]) same=false;
        }
        if(same){ stable=h; break; }
        pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps),stable};
}

static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){
    vector<A> as; as.reserve(654);
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40, c=(11*x+9*y)/40, m=max(x,y);
        as.push_back({x,y,dh,c,m,
            9LL*x*Q-10LL*P*m,
            -11LL*x*Q-10LL*P*m,
            9LL*y*Q-10LL*P*m});
    }
    vector<long long> pr(M+1),cr(M+1);
    for(int h=1;h<=H;h++){
        bool same=true;
        for(int k=0;k<=M;k++){
            long long best=0;
            for(const auto &a:as){
                long long hi=a.hb+((k+a.dh<=M)?pr[k+a.dh]:0);
                long long lo;
                if(k>=a.c) lo=a.lb+pr[k-a.c];
                else { int kk=a.c-k; lo=a.rb-40LL*k*Q+pr[kk]; }
                best=max(best,min(hi,lo));
            }
            cr[k]=best;
            if(cr[k]!=pr[k]) same=false;
        }
        if(same) break;
        pr.swap(cr);
    }
    return pr;
}

int main(int argc,char**argv){
    if(argc<4){ cerr << "usage: checker P Q recourse_depth\n"; return 1; }
    long long P=stoll(argv[1]), Q=stoll(argv[2]);
    int D=stoi(argv[3]);

    auto fi=integer_table(P,Q);
    vector<Orbit> os(5);
    for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);

    auto F0=[&](int J)->long long{
        if(J<0) J=-J;
        int k=J/8, r=J%8;
        if(k>=2600) return 0;
        if(r==0) return fi[k]*8;
        if(r<=4) return os[r].r[k];
        return os[8-r].s[k];
    };

    // G_0=old654 terminal continuation.  For d>=1,
    // G_d(J)=max{G_0(J), max_p min(high_p+G_{d-1}, low_p+G_{d-1})}.
    // The max with G_0 is the legal option to hand off immediately to old654,
    // so D means at most D extra adaptive structural actions z_p=(p/192,1).
    int Jmax=3840 + D*3840 + 3840;
    vector<long long> prev(Jmax+1),cur(Jmax+1);
    for(int J=0;J<=Jmax;J++) prev[J]=F0(J);

    long long T8=8LL*(12480LL*Q+28800LL*P);
    cout << "eps=" << P << "/" << Q << " depth0_gap=" << prev[3840]-T8 << "\n";

    for(int d=1;d<=D;d++){
        for(int J=0;J<=Jmax-3840;J++){
            long long best=LLONG_MIN;
            for(int p=0;p<=192;p++){
                int dh=9*p+2112;
                int c=11*p+1728;
                long long hi=8LL*(45LL*p*Q-9600LL*P)+prev[J+dh];
                int jl=abs(J-c);
                long long lo;
                if(J>=c) lo=8LL*(-55LL*p*Q-9600LL*P)+prev[jl];
                else lo=8LL*(8640LL*Q-9600LL*P)-40LL*Q*J+prev[jl];
                best=max(best,min(hi,lo));
            }
            cur[J]=max(F0(J),best);
        }
        prev.swap(cur);
        cout << "depth" << d << "_gap=" << prev[3840]-T8 << "\n";
    }
    return 0;
}
