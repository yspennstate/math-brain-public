#include <bits/stdc++.h>
using namespace std;

struct A { int x,y,dh,c,m; long long hb,lb,rb; };

static vector<pair<int,int>> old654_points(){
    vector<pair<int,int>> ps;
    for(int i=0;i<=24;i++) for(int j=0;j<=24;j++) ps.push_back({40*i,40*j});
    const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};
    for(auto &p:ex) ps.push_back({4*p[0],4*p[1]});
    const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};
    for(auto &p:cut) ps.push_back({p[0],p[1]});
    return ps;
}

struct Orbit { vector<long long> r,s; int stable=-1; };

static Orbit orbit_table(long long P,long long Q,int R,int r,int M=2600,int H=612){
    vector<A> as;
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
        }
        if(cr==pr && cs==ps){ stable=h; break; }
        pr.swap(cr); ps.swap(cs);
    }
    return {move(pr),move(ps),stable};
}

static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){
    vector<A> as;
    for(auto [x,y]:old654_points()){
        int dh=(9*x+11*y)/40, c=(11*x+9*y)/40, m=max(x,y);
        as.push_back({x,y,dh,c,m,
            9LL*x*Q-10LL*P*m,
            -11LL*x*Q-10LL*P*m,
            9LL*y*Q-10LL*P*m});
    }
    vector<long long> pr(M+1),cr(M+1);
    for(int h=1;h<=H;h++){
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
        }
        if(cr==pr) break;
        pr.swap(cr);
    }
    return pr;
}

struct SearchResult {
    long long bestGap8=LLONG_MIN,Hgap8=0,Lgap8=0;
    int p0=-1,pL=-1,pH=-1,JL=-1,JH=-1;
};

static SearchResult depth2_search(long long P,long long Q){
    const int R=8;
    auto fi=integer_table(P,Q);
    auto o1=orbit_table(P,Q,R,1), o2=orbit_table(P,Q,R,2),
         o3=orbit_table(P,Q,R,3), o4=orbit_table(P,Q,R,4);

    auto F8=[&](int J)->long long{
        if(J<0) J=-J;
        int k=J/8, r=J%8;
        if(k>=2600) return 0;
        if(r==0) return fi[k]*8;
        if(r==1) return o1.r[k];
        if(r==7) return o1.s[k];
        if(r==2) return o2.r[k];
        if(r==6) return o2.s[k];
        if(r==3) return o3.r[k];
        if(r==5) return o3.s[k];
        return o4.r[k];
    };

    auto second_value=[&](int J,int p)->long long{
        // Physical action: (a,b)=(p/192,1). Values are in scale 8.
        int dhJ=9*p+2112;     // 8*(216a+264b)
        int cJ =11*p+1728;    // 8*(264a+216b)
        long long hi=8LL*(45LL*p*Q-9600LL*P)+F8(J+dhJ);
        long long lo;
        if(J>=cJ) lo=8LL*(-55LL*p*Q-9600LL*P)+F8(J-cJ);
        else lo=8LL*(8640LL*Q-9600LL*P)-40LL*Q*J+F8(cJ-J);
        return min(hi,lo);
    };

    long long T8=8LL*(12480LL*Q+28800LL*P);
    SearchResult R0;
    for(int p0=0;p0<=192;p0++){
        // Root state K=480 -> J=3840.
        int JL=2112-11*p0; // 8*(480-c)
        int JH=5952+9*p0;  // 8*(480+dh)
        long long GL=0,GH=0; int pL=0,pH=0;
        for(int p=0;p<=192;p++){
            long long vl=second_value(JL,p);
            long long vh=second_value(JH,p);
            if(vl>GL){GL=vl;pL=p;}
            if(vh>GH){GH=vh;pH=p;}
        }
        long long Hroot=8LL*(45LL*p0*Q-9600LL*P)+GH;
        long long Lroot=8LL*(-55LL*p0*Q-9600LL*P)+GL;
        long long gap=min(Hroot,Lroot)-T8;
        if(gap>R0.bestGap8){
            R0={gap,Hroot-T8,Lroot-T8,p0,pL,pH,JL,JH};
        }
    }
    return R0;
}

int main(){
    auto oldR=depth2_search(617,253330);
    auto newR=depth2_search(227,92430);

    if(oldR.p0!=119 || oldR.pL!=175 || oldR.pH!=73 || oldR.bestGap8<=0){
        cerr<<"unexpected old-epsilon optimizer/gap\n"; return 2;
    }
    if(newR.p0!=119 || newR.pL!=175 || newR.pH!=73 || newR.bestGap8!=0){
        cerr<<"unexpected new-epsilon restricted optimum\n"; return 3;
    }
    if(newR.JL!=803 || newR.JH!=7023){
        cerr<<"unexpected root child states\n"; return 4;
    }

    // Winning branch-specific second-stage actions:
    // low child pL=175: dhJ=3687, cJ=3653, so grandchildren J=4490 and 2850 (reflection);
    // high child pH=73: dhJ=2769, cJ=2531, so grandchildren J=9792 and 4492.
    const int low_hi=803+3687, low_lo=3653-803;
    const int high_hi=7023+2769, high_lo=7023-2531;
    if(low_hi!=4490 || low_lo!=2850 || high_hi!=9792 || high_lo!=4492){
        cerr<<"terminal-state arithmetic failure\n"; return 5;
    }

    cout<<"I0130_B14_B15_B21_DEPTH2_ADAPTIVE_PASS\n";
    cout<<"old_epsilon=617/253330 old_bestgap8="<<oldR.bestGap8
        <<" old_policy=(119/192;175/192,73/192)"
        <<" Hgap8="<<oldR.Hgap8<<" Lgap8="<<oldR.Lgap8<<"\n";
    cout<<"new_epsilon=227/92430 restricted_bestgap8="<<newR.bestGap8
        <<" optimizer=(119/192;175/192,73/192)"
        <<" Hgap8="<<newR.Hgap8<<" Lgap8="<<newR.Lgap8<<"\n";
    cout<<"root_children_J=(803,7023) corresponding_K=(803/8,7023/8)\n";
    cout<<"terminal_J=(4490,2850,9792,4492) corresponding_K=(2245/4,1425/4,1224,1123/2)\n";
    cout<<"full_Z8_reflection_orbits={0},{1,7},{2,6},{3,5},{4}; winning_tree_uses={0},{2,6},{4}\n";
    cout<<"source_delta=947/9243 U_MIV=8296/9243 W_MIV=24421/92430\n";
    cout<<"improvement_over_22738/25333=4766/234152919 total_goods_at_most=617\n";
    return 0;
}
