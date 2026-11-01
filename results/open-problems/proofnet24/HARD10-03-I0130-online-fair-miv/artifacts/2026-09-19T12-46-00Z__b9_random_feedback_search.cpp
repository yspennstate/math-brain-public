#define main base_unused
#include "2026-09-19T11-50-00Z__b8_b16_b23_multistage_recourse_checker.cpp"
#undef main
#include <random>

int main(int argc,char**argv){
    if(argc<5){ cerr << "usage: search P Q recourse_depth samples\n"; return 1; }
    long long P=stoll(argv[1]),Q=stoll(argv[2]);
    int D=stoi(argv[3]),N=stoi(argv[4]);
    auto fi=integer_table(P,Q);
    vector<Orbit> os(5);
    for(int r=1;r<=4;r++) os[r]=orbit_table(P,Q,8,r);
    auto F0=[&](int J)->long long{
        if(J<0)J=-J;
        int k=J/8,r=J%8;
        if(k>=2600)return 0;
        if(r==0)return fi[k]*8;
        if(r<=4)return os[r].r[k];
        return os[8-r].s[k];
    };
    int Jmax=3840+D*3840+3840;
    long long T8=8LL*(12480LL*Q+28800LL*P);
    mt19937_64 rng(777);
    long long bestgap=LLONG_MIN;
    double bestA=0,bestB=0,bestC=0;
    int bestR[5]={};
    for(int it=0;it<N;it++){
        double A=130.0 + (rng()%70001)/1000.0;
        double B=0.004 + (rng()%16001)/1000000.0;
        double C=-4.0 + (rng()%8001)/1000.0;
        int roff[5]; for(int r=0;r<5;r++) roff[r]=(int)(rng()%17)-8;
        vector<long long> prev(Jmax+1),cur(Jmax+1);
        for(int J=0;J<=Jmax;J++)prev[J]=F0(J);
        for(int d=1;d<=D;d++){
            for(int J=0;J<=Jmax-3840;J++){
                int rr=J%8; if(rr>4)rr=8-rr;
                int p=(int)llround(A+C*d-B*J+roff[rr]);
                if(p<0)p=0; if(p>192)p=192;
                int dh=9*p+2112,c=11*p+1728;
                long long hi=8LL*(45LL*p*Q-9600LL*P)+prev[J+dh];
                int jl=abs(J-c);
                long long lo=(J>=c)
                    ?8LL*(-55LL*p*Q-9600LL*P)+prev[jl]
                    :8LL*(8640LL*Q-9600LL*P)-40LL*Q*J+prev[jl];
                cur[J]=max(F0(J),min(hi,lo));
            }
            prev.swap(cur);
        }
        long long gap=prev[3840]-T8;
        if(gap>bestgap){
            bestgap=gap; bestA=A; bestB=B; bestC=C;
            for(int r=0;r<5;r++)bestR[r]=roff[r];
        }
    }
    cout << "I0130_B9_RANDOM_FEEDBACK_SEARCH\n";
    cout << "seed=777 samples=" << N << " epsilon=" << P << "/" << Q << " depth=" << D << "\n";
    cout << "bestgap=" << bestgap << " A=" << setprecision(12) << bestA
         << " B=" << bestB << " C=" << bestC << " roff=";
    for(int r=0;r<5;r++) cout << bestR[r] << (r==4?'\n':',');
    cout << "DISCOVERY_ONLY_RANDOMIZATION_NOT_PART_OF_SOURCE_THEOREM\n";
    return 0;
}
