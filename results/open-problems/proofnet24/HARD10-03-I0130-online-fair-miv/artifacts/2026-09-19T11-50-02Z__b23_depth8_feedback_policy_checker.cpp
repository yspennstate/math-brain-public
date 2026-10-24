#define main i0130_recourse_checker_main
#include "2026-09-19T11-50-00Z__b8_b16_b23_multistage_recourse_checker.cpp"
#undef main

int main(){
    const long long P=1489, Q=554410;
    const int D=8;
    auto fi=integer_table(P,Q);
    vector<Orbit> os(5);
    for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);
    auto F0=[&](int J)->long long{
        if(J<0) J=-J;
        int k=J/8,r=J%8;
        if(k>=2600) return 0;
        if(r==0) return fi[k]*8;
        if(r<=4) return os[r].r[k];
        return os[8-r].s[k];
    };

    int Jmax=3840 + D*3840 + 3840;
    vector<vector<long long>> V(D+1, vector<long long>(Jmax+1));
    vector<vector<short>> pol(D+1, vector<short>(Jmax+1,-1));
    for(int J=0;J<=Jmax;J++) V[0][J]=F0(J);
    for(int d=1;d<=D;d++){
        for(int J=0;J<=Jmax-3840;J++){
            long long best=F0(J); int bp=-1;
            for(int p=0;p<=192;p++){
                int dh=9*p+2112,c=11*p+1728;
                long long hi=8LL*(45LL*p*Q-9600LL*P)+V[d-1][J+dh];
                int jl=abs(J-c);
                long long lo=(J>=c)?8LL*(-55LL*p*Q-9600LL*P)+V[d-1][jl]
                                     :8LL*(8640LL*Q-9600LL*P)-40LL*Q*J+V[d-1][jl];
                long long val=min(hi,lo);
                if(val>best){ best=val; bp=p; }
            }
            V[d][J]=best; pol[d][J]=bp;
        }
    }

    long long T8=8LL*(12480LL*Q+28800LL*P);
    if(V[D][3840]-T8!=0 || pol[D][3840]!=118) return 2;

    function<long long(int,int,char)> fixed=[&](int J,int d,char incoming)->long long{
        if(d==0) return F0(J);
        int p=(incoming=='R'?119:(incoming=='L'?175:73));
        int dh=9*p+2112,c=11*p+1728;
        long long hi=8LL*(45LL*p*Q-9600LL*P)+fixed(J+dh,d-1,'H');
        int jl=abs(J-c);
        long long lo=(J>=c)?8LL*(-55LL*p*Q-9600LL*P)+fixed(jl,d-1,'L')
                             :8LL*(8640LL*Q-9600LL*P)-40LL*Q*J+fixed(jl,d-1,'L');
        return min(hi,lo);
    };
    long long fixedGap=fixed(3840,D,'R')-T8;
    if(fixedGap>=0) return 3;

    cout << "I0130_B23_DEPTH8_FEEDBACK_POLICY_PASS\n";
    cout << "depth8_gap8=0 root_p=118 fixed_recursive_(119;L175,H73)_gap8=" << fixedGap << "\n";
    queue<pair<int,int>> q; q.push({D,3840});
    int shown=0;
    while(!q.empty() && shown<15){
        auto [d,J]=q.front(); q.pop();
        int p=pol[d][J];
        cout << "node d=" << d << " J=" << J << " p=" << p << "\n";
        ++shown;
        if(d>0 && p>=0){
            int dh=9*p+2112,c=11*p+1728;
            q.push({d-1,J+dh});
            q.push({d-1,abs(J-c)});
        }
    }
    return 0;
}
