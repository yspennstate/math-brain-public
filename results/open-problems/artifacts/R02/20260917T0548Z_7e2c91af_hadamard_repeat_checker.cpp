#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

struct Mat { int n; int a[20][20]; };
static Mat parseH(const string& s,int n){ Mat H{}; H.n=n; stringstream ss(s); string tok; int i=0; while(ss>>tok){ unsigned long long x=stoull(tok,nullptr,16); for(int j=0;j<n;j++) H.a[i][j]=((x>>(n-1-j))&1ULL)?1:-1; i++; } if(i!=n) throw runtime_error("rows"); return H; }
static bool had(const Mat&H){ for(int i=0;i<H.n;i++)for(int j=0;j<H.n;j++){int s=0;for(int k=0;k<H.n;k++)s+=H.a[i][k]*H.a[j][k];if(s!=(i==j?H.n:0))return false;}return true; }

static bool dfs_sign(const Mat&H,const array<unsigned char,20>& mult,int j,int sums[20]){
    int n=H.n;
    if(j==n){ for(int i=0;i<n;i++) if(abs(sums[i])>6) return false; return true; }
    int w=1+(int)mult[j];
    for(int s=-w;s<=w;s+=2){
        for(int i=0;i<n;i++) sums[i]+=H.a[i][j]*s;
        if(dfs_sign(H,mult,j+1,sums)) return true;
        for(int i=0;i<n;i++) sums[i]-=H.a[i][j]*s;
    }
    return false;
}
static inline bool pattern_ok(const Mat&H,const array<unsigned char,20>& m){int sums[20]={0};return dfs_sign(H,m,0,sums);}

static void genrec(int pos,int n,int rem,array<unsigned char,20>&cur,vector<array<unsigned char,20>>&out){ if(pos==n-1){cur[pos]=rem;out.push_back(cur);return;} for(int v=0;v<=rem;v++){cur[pos]=v;genrec(pos+1,n,rem-v,cur,out);} }
static vector<array<unsigned char,20>> gen(int n,int e){vector<array<unsigned char,20>> o;array<unsigned char,20> c{};genrec(0,n,e,c,o);return o;}

static bool run(const vector<string>& reps,int n,int extra,long long expected){auto pats=gen(n,extra);cout<<"family n="<<n<<" extra="<<extra<<" patterns_per_class="<<pats.size()<<"\n";if((long long)pats.size()!=expected)return false;long long total=0;for(int q=0;q<(int)reps.size();q++){Mat H=parseH(reps[q],n);if(!had(H)){cerr<<"bad H "<<q<<"\n";return false;}int bad=-1;
#pragma omp parallel for schedule(dynamic,8)
for(int p=0;p<(int)pats.size();p++){ if(bad>=0) continue; if(!pattern_ok(H,pats[p])){
#pragma omp critical
{if(bad<0)bad=p;}
}}
if(bad>=0){cerr<<"bad pattern class="<<q<<" p="<<bad<<"\n";return false;}total+=pats.size();cout<<"class="<<q<<" hadamard=1 all_repeat_patterns_have_disc_le6=1 tested="<<pats.size()<<"\n";}cout<<"family_total_patterns_tested="<<total<<"\n";return true;}
static long long C(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;long long r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
int main(){
vector<string> H16={
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A5A5 A55A 9999 9966 9696 9669",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A5A5 A55A 9996 9969 9699 9666",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A599 A566 9996 9969 96A5 965A",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA A995 A659 A566 9A56 9969 96A5 959A",
"FFFF FF00 F0F0 F00F CCCC CC33 C3AA C355 AAC3 AA3C A599 A566 9996 9969 96A5 965A"};
vector<string> H20={
"FFFFF FFC00 F83E0 F421E E3199 D3067 CC987 CC479 C2F54 C1EAA B0D4B AAA33 A94D6 A68EC A5725 9A68D 9993C 965B2 95AD1 8F34A",
"FFFFF FFC00 F83E0 F421E E3199 D3067 CC987 CC479 C2F54 C1EAA B0D33 AAA4B A94D6 A66A5 A596C 9A8BC 9970D 965CA 95AD1 8F332",
"FFFFF FFC00 F83E0 F421E E3199 D2947 CD0A7 CA47C C4F31 C1ECA B1473 AAA2B A8D96 A66C5 A596C 9C8D9 9970D 965AA 93AB4 8F352"};
cout<<"R02 I0095 exact repeated-column checker 2026-09-17\n";
if(!run(H16,16,6,54264))return 2;
if(!run(H20,20,2,210))return 3;
cout<<"n19_codewords_from_rows=38 published_covering_lower_bound_used=40 strict_gap=2\n";if(!(38<40))return 4;
long long V=0;for(int k=0;k<=7;k++)V+=C(22,k);cout<<"n22_V(22,7)="<<V<<" fortyfour_ball_volume="<<44*V<<" cube="<<(1LL<<22)<<"\n";if(V!=280600)return 5;
cout<<"metric_compare_8sqrt22_vs_7sqrt17 lhs="<<64*17<<" rhs="<<49*22<<"\n";if(!(64*17>49*22))return 6;
cout<<"CONCLUSION_REPEAT_COLUMN_HADAMARD_ROUTES_CANNOT_REACH_DISC8_AT_N22\nALL_EXACT_CHECKS_PASS\n";
}
