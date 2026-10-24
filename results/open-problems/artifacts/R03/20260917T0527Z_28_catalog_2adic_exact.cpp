#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

struct Key { uint64_t a,b; bool operator==(Key const&o) const{return a==o.a&&b==o.b;} };
struct KH { size_t operator()(Key const&k) const { uint64_t x=k.a*0x9e3779b97f4a7c15ULL + k.b; x^=x>>30; x*=0xbf58476d1ce4e5b9ULL; x^=x>>27; x*=0x94d049bb133111ebULL; x^=x>>31; return x; }};

int invmod(int a,int p){ for(int x=1;x<p;x++) if(a*x%p==1) return x; assert(false); return 0; }
vector<int> decode(uint64_t z,int m,int p){ vector<int> v(m); for(int i=0;i<m;i++){v[i]=z%p;z/=p;}return v; }
uint64_t encode(vector<int> const&v,int p){ uint64_t z=0,mul=1; for(int x:v){z+=mul*x;mul*=p;}return z;}

vector<uint64_t> sparse_lines(int m,int p){
    vector<uint64_t> out;
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++){
        int S[3]={a,b,c};
        for(int neg=0;neg<3;neg++){
            vector<int> v(m); for(int t=0;t<3;t++)v[S[t]]=(t==neg?p-1:1);
            int first=0; while(v[first]==0)first++; int iv=invmod(v[first],p); for(int&i:v)i=i*iv%p;
            out.push_back(encode(v,p));
        }
    }
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)for(int d=c+1;d<m;d++){
        int S[4]={a,b,c,d};
        for(int q=1;q<4;q++){
            vector<int> v(m);
            for(int t=0;t<4;t++) v[S[t]]=(t==0||t==q)?1:p-1;
            out.push_back(encode(v,p));
        }
    }
    sort(out.begin(),out.end()); out.erase(unique(out.begin(),out.end()),out.end()); return out;
}
Key rref2(uint64_t av,uint64_t bv,int m,int p){
    int A[2][12]{}; auto va=decode(av,m,p), vb=decode(bv,m,p); for(int j=0;j<m;j++){A[0][j]=va[j];A[1][j]=vb[j];}
    int row=0;
    for(int col=0;col<m&&row<2;col++){
        int piv=-1; for(int r=row;r<2;r++) if(A[r][col]){piv=r;break;} if(piv<0)continue;
        if(piv!=row) for(int j=0;j<m;j++) swap(A[piv][j],A[row][j]);
        int iv=invmod(A[row][col],p); for(int j=0;j<m;j++)A[row][j]=A[row][j]*iv%p;
        for(int r=0;r<2;r++)if(r!=row && A[r][col]){int c=A[r][col];for(int j=0;j<m;j++){A[r][j]=(A[r][j]-c*A[row][j])%p;if(A[r][j]<0)A[r][j]+=p;}}
        row++;
    }
    assert(row==2); vector<int>x(m),y(m);for(int j=0;j<m;j++){x[j]=A[0][j];y[j]=A[1][j];}
    return {encode(x,p),encode(y,p)};
}

int rank_add(vector<vector<int>>&basis, vector<int> v,int p,int target){
    int m=v.size();
    for(auto &b:basis){int piv=-1;for(int j=0;j<m;j++)if(b[j]){piv=j;break;} if(piv>=0 && v[piv]){int c=v[piv];for(int j=0;j<m;j++){v[j]=(v[j]-c*b[j])%p;if(v[j]<0)v[j]+=p;}}}
    int piv=-1;for(int j=0;j<m;j++)if(v[j]){piv=j;break;}if(piv<0)return basis.size();
    int iv=invmod(v[piv],p);for(int&z:v)z=z*iv%p;
    for(auto &b:basis) if(b[piv]){int c=b[piv];for(int j=0;j<m;j++){b[j]=(b[j]-c*v[j])%p;if(b[j]<0)b[j]+=p;}}
    basis.push_back(v); sort(basis.begin(),basis.end(),[](auto const&a,auto const&b){int pa=99,pb=99;for(int j=0;j<(int)a.size();j++){if(a[j]&&pa==99)pa=j;if(b[j]&&pb==99)pb=j;}return pa<pb;});
    return basis.size();
}

vector<vector<int>> nullspace_basis(vector<vector<int>> M,int p,int m){
    int r=M.size(), row=0; vector<int> piv;
    for(int col=0;col<m && row<r;col++){
        int pr=-1; for(int i=row;i<r;i++) if(M[i][col]%p){pr=i;break;} if(pr<0) continue;
        swap(M[row],M[pr]); int iv=invmod(M[row][col]%p,p); for(int j=0;j<m;j++)M[row][j]=M[row][j]*iv%p;
        for(int i=0;i<r;i++) if(i!=row && M[i][col]){int c=M[i][col];for(int j=0;j<m;j++){M[i][j]=(M[i][j]-c*M[row][j])%p;if(M[i][j]<0)M[i][j]+=p;}}
        piv.push_back(col); row++;
    }
    vector<char> isp(m); for(int c:piv)isp[c]=1; vector<vector<int>> out;
    for(int f=0;f<m;f++) if(!isp[f]){
        vector<int>x(m);x[f]=1;
        for(int i=row-1;i>=0;i--){int pc=piv[i], sum=0;for(int j=pc+1;j<m;j++)sum=(sum+M[i][j]*x[j])%p;x[pc]=(p-sum)%p;}
        out.push_back(x);
    }
    return out;
}
int min_support_span(vector<vector<int>> const& N,int p,int m){
    int k=N.size(), best=m+1; long long total=1;for(int i=0;i<k;i++)total*=p;
    for(long long code=1;code<total;code++){long long z=code;vector<int>v(m);for(int i=0;i<k;i++){int c=z%p;z/=p;for(int j=0;j<m;j++)v[j]=(v[j]+c*N[i][j])%p;}int w=0;for(int x:v)w+=x!=0;best=min(best,w);}
    return best;
}

struct Stats {long long lines,planes; map<int,long long> minctr,hctr,rankctr,hiddenmin;};
Stats analyze(int m,int p){
    auto lines=sparse_lines(m,p);
    unordered_set<Key,KH> S; S.reserve(lines.size()*lines.size()/2);
    for(size_t i=0;i<lines.size();i++)for(size_t j=i+1;j<lines.size();j++) S.insert(rref2(lines[i],lines[j],p));
    Stats st;st.lines=lines.size();st.planes=S.size(); int d=m-2, border=1<<(d-1);
    for(auto const&k:S){
        auto a=decode(k.a,m,p), b=decode(k.b,m,p);
        int mins=m+1;
        for(int t=0;t<p;t++){int w=0;for(int j=0;j<m;j++)if((a[j]+t*b[j])%p)w++;mins=min(mins,w);}
        int wb=0;for(int j=0;j<m;j++)if(b[j])wb++;mins=min(mins,wb);st.minctr[mins]++;
        if(mins<3)continue;
        int h=0; vector<vector<int>> basis;
        for(int mask=0;mask<(1<<m);mask++){
            int da=0,db=0;for(int j=0;j<m;j++)if(mask>>j&1){da+=a[j];db+=b[j];}da%=p;db%=p;
            if(da==0&&db==0){h++; if(h<=border+5 && (int)basis.size()<d){vector<int>x(m);for(int j=0;j<m;j++)x[j]=(mask>>j)&1;rank_add(basis,x,p,d);}}
        }
        st.hctr[h]++;
        if(h==border){
            st.rankctr[(int)basis.size()]++;
            if((int)basis.size()<d){ auto N=nullspace_basis(basis,p,m); st.hiddenmin[min_support_span(N,p,m)]++; }
        }
    }
    return st;
}

cpp_int prod(vector<long long> v){cpp_int z=1;for(auto x:v)z*=x;return z;}
long double ratio_ld(cpp_int n,cpp_int d){return n.convert_to<long double>()/d.convert_to<long double>();}

pair<long long,long long> cycle_counts(int a,int b){int A=a-1,B=b-1,N=A*B; long long c0=0,c1=0; for(uint64_t mask=0;mask<(1ULL<<N);mask++){int rows[8]={},cols[8]={},wt=0;for(int i=0;i<A;i++)for(int j=0;j<B;j++){int z=(mask>>(i*B+j))&1;rows[i]^=z;cols[j]^=z;wt+=z;}int corner=0;for(int i=0;i<A;i++){wt+=rows[i];corner^=rows[i];}for(int j=0;j<B;j++)wt+=cols[j];wt+=corner; assert((wt&1)==0); ((wt/2)&1?c1:c0)++;}return {c0,c1};}

int main(){ios::sync_with_stdio(false);cout<<"R03 run28 catalog-wide exact-corank-two + 2-adic cycle-code checker\n";
    auto s9=analyze(9,7); auto s10=analyze(10,11);
    auto prmap=[](map<int,long long> const&m){string z="{";bool f=0;for(auto [a,b]:m){if(f)z+=",";f=1;z+=to_string(a)+":"+to_string(b);}return z+"}";};
    cout<<"m9 p7 lines "<<s9.lines<<" planes "<<s9.planes<<" min_support "<<prmap(s9.minctr)<<" useful_h "<<prmap(s9.hctr)<<" borderline_rank "<<prmap(s9.rankctr)<<" hidden_min "<<prmap(s9.hiddenmin)<<"\n";
    cout<<"m10 p11 lines "<<s10.lines<<" planes "<<s10.planes<<" min_support "<<prmap(s10.minctr)<<" useful_h "<<prmap(s10.hctr)<<" borderline_rank "<<prmap(s10.rankctr)<<" hidden_min "<<prmap(s10.hiddenmin)<<"\n";
    map<int,long long> eh9{{64,48384},{72,89775},{80,15750}}, er9{{6,10584},{7,37800}};
    map<int,long long> eh10{{128,103320},{144,259875},{160,34650}}, er10{{7,20160},{8,83160}};
    assert(s9.lines==630&&s9.planes==166635&&s9.hctr==eh9&&s9.rankctr==er9);
    assert(s10.lines==990&&s10.planes==420255&&s10.hctr==eh10&&s10.rankctr==er10);
    map<int,long long> hm9{{1,3024},{2,7560}}, hm10{{1,5040},{2,15120}};
    assert(s9.hiddenmin==hm9 && s10.hiddenmin==hm10);
    vector<long long> t72={71,70,68,64,56,40,8}; cpp_int B72=prod(t72),E72=B72*4032;
    vector<long long> t80={79,78,76,72,64,48,16}; cpp_int B80=prod(t80),E80=B80*5112;
    vector<long long> t64={63,62,60,56,48,32,1}; cpp_int B64=prod(t64),E64=B64*3080;
    cpp_int Enew9=cpp_int(89775-7560)*E72+cpp_int(15750)*E80+cpp_int(37800)*E64;
    cout<<"m9 B72 "<<B72<<" E72 "<<E72<<" B80 "<<B80<<" E80 "<<E80<<" B64span "<<B64<<" E64 "<<E64<<" NEW_E2 "<<Enew9<<"\n";
    assert(Enew9==cpp_int("264270941440966656000"));
    vector<long long> t144={143,142,140,136,128,112,80,16};cpp_int B144=prod(t144),E144=B144*18090;
    vector<long long> t160={159,158,156,152,144,128,96,32};cpp_int B160=prod(t160),E160=B160*22650;
    vector<long long> t128={127,126,124,120,112,96,64,1};cpp_int B128=prod(t128),E128=B128*14042;
    cpp_int Enew10=cpp_int(259875-18900)*E144+cpp_int(34650)*E160+cpp_int(83160)*E128;
    cout<<"m10 B144 "<<B144<<" E144 "<<E144<<" B160 "<<B160<<" E160 "<<E160<<" B128span "<<B128<<" E128 "<<E128<<" NEW_E2 "<<Enew10<<"\n";
    assert(Enew10==cpp_int("57590525370775562197401600"));
    cpp_int d9n("1728914888653785"),d9d("2251799813685248");
    cpp_int n9n("80980526207266000017381"),n9d("295147905179352825856");
    cpp_int d10n("60766026811068072002355"),d10d("59416962661418465755136");
    cpp_int n10n("4072170700433858852772747816165"),n10d("7787900129957441143457185792");
    cpp_int lhs9=d9n*cpp_int(50)*(cpp_int(1)<<71), rhs9=d9d*cpp_int(343)*Enew9; assert(lhs9==rhs9);
    cpp_int lhs10=d10n*cpp_int(16105)*(cpp_int(1)<<89), rhs10=d10d*cpp_int(177023)*Enew10; assert(lhs10==rhs10);
    cout<<setprecision(18)<<"n10 additional "<<d9n<<"/"<<d9d<<" = "<<ratio_ld(d9n,d9d)<<" new_r10 "<<n9n<<"/"<<n9d<<" = "<<ratio_ld(n9n,n9d)<<"\n";
    cout<<"n11 additional "<<d10n<<"/"<<d10d<<" = "<<ratio_ld(d10n,d10d)<<" new_r11 "<<n10n<<"/"<<n10d<<" = "<<ratio_ld(n10n,n10d)<<"\n";
    for(int a=3;a<=5;a++)for(int b=3;b<=5;b++){auto [c0,c1]=cycle_counts(a,b);int d=(a-1)*(b-1),u=(a-1)/2,v=(b-1)/2;long long total=1LL<<d,G=1LL<<(d-2*u*v);long long p0=(total+G)/2,p1=(total-G)/2;cout<<"cycle "<<a<<","<<b<<" "<<c0<<","<<c1<<" pred "<<p0<<","<<p1<<"\n";assert(c0==p0&&c1==p1);} 
    cout<<"SELF-CHECK PASS\n";
}
