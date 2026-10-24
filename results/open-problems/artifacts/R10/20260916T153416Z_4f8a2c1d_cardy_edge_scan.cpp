#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using boost::multiprecision::cpp_int;
using std::uint64_t;

static uint64_t enc(const std::vector<int>& a){
    uint64_t s=0; for(size_t i=0;i<a.size();++i) s|=(uint64_t(a[i])<<(4*i)); return s;
}
static std::vector<int> dec(uint64_t s,int w){
    std::vector<int>a(w); for(int i=0;i<w;++i)a[i]=int((s>>(4*i))&15ULL); return a;
}
static uint64_t canon(std::vector<int> a){
    int mp[16]; std::fill(mp,mp+16,-1); mp[0]=0; int nxt=1;
    for(int&x:a){ if(x==0)continue; if(mp[x]<0)mp[x]=nxt++; x=mp[x]; }
    return enc(a);
}
static bool replace_closed(uint64_t s,int w,int j,uint64_t& out){
    auto a=dec(s,w); int old=a[j];
    if(old==0){ bool other=false; for(int k=0;k<w;++k) if(k!=j&&a[k]==0){other=true;break;} if(!other)return false; }
    int mx=0; for(int x:a)mx=std::max(mx,x); a[j]=mx+1; out=canon(a); return true;
}
static uint64_t merge_pos(uint64_t s,int w,int i,int j){
    auto a=dec(s,w); int x=a[i],y=a[j]; if(x==y)return s;
    if(x==0||y==0){ int z=(x==0?y:x); for(int&q:a)if(q==z)q=0; }
    else { for(int&q:a)if(q==y)q=x; }
    return canon(a);
}
static cpp_int pow2i(unsigned e){ cpp_int r=1; r<<=e; return r; }
static cpp_int gcdx(cpp_int a,cpp_int b){ while(b!=0){ cpp_int r=a%b; a=b; b=r; } return a; }
struct Ans{cpp_int fav,den,rn,rd; size_t states;};

static Ans solve(int n){
    const int w=n+1;
    if(w>14) throw std::runtime_error("4-bit canonical labels support width <=14");
    std::vector<int> init(w,0);
    std::unordered_map<uint64_t,cpp_int> dp,tmp,nxt;
    dp.reserve(200000); tmp.reserve(200000); nxt.reserve(200000);
    dp[enc(init)]=1;
    for(int col=0; col<2*n; ++col){
        for(int j=0;j<w;++j){
            // Horizontal edge old_j--new_j. Open: the slot inherits its old component.
            // Closed: old_j is forgotten and new_j is a singleton. If this removes
            // the last source-connected frontier vertex, the branch can never reconnect.
            tmp.clear();
            for(const auto&kv:dp){
                tmp[kv.first]+=kv.second;
                uint64_t c; if(replace_closed(kv.first,w,j,c)) tmp[c]+=kv.second;
            }
            dp.swap(tmp);
            if(j>0){
                // Vertical edge new_{j-1}--new_j, closed/open.
                nxt.clear();
                for(const auto&kv:dp){
                    nxt[kv.first]+=kv.second;
                    nxt[merge_pos(kv.first,w,j-1,j)]+=kv.second;
                }
                dp.swap(nxt);
            }
        }
    }
    cpp_int fav=0; for(const auto&kv:dp)fav+=kv.second;
    const unsigned E=unsigned(2*n*(2*n+1));
    cpp_int den=pow2i(E), g=gcdx(fav,den);
    return {fav,den,fav/g,den/g,dp.size()};
}

int main(){
    std::cout << "R10 exact edge-scan frontier certificate\n";
    std::cout << "R=[0,2]x[0,1], delta=1/n, p=1/2, LR vertex-boundary crossing\n";
    // Historical exact values from the independent column-mask checker, n<=6.
    const char* expn[7]={"",
      "1",
      "48449",
      "5363328171",
      "20696232901811649907",
      "1321126882225579491309717801203",
      "176191897998719099783873632323748134346583099"};
    const char* expd[7]={"",
      "2",
      "131072",
      "17179869184",
      "73786976294838206464",
      "5070602400912917605986812821504",
      "713623846352979940529142984724747568191373312"};
    for(int n=1;n<=9;++n){
        Ans a=solve(n);
        if(n<=6 && (a.rn!=cpp_int(expn[n]) || a.rd!=cpp_int(expd[n]))){
            std::cerr << "historical cross-check failed at n="<<n<<"\n"; return 3;
        }
        std::cout << "n="<<n<<" E="<<2*n*(2*n+1)
                  <<" reduced="<<a.rn<<"/"<<a.rd
                  <<" final_states="<<a.states;
        if(n<=6) std::cout << " prior_column_mask_MATCH";
        std::cout << "\n";
    }
    std::cout << "PASS\n";
    return 0;
}
