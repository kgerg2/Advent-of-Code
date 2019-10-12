#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(){
    int i, hossz=50000, db=0, kul = 'a' - 'A', ujhossz;
    bool cserel = true;
    char s[50000];
    //ifstream be (".\\2018\\5\\input.txt");
    cin >> s;
    cout << s[0] << s[49999];
    cout << (int)s[0] << " " << (int)s[49999] << endl;
    //be.close();
    while (cserel){
        cserel = false;
        ujhossz = 0;
        for(i=0; i<hossz; i++){
            if(i < hossz-1 && abs(s[i]-s[i+1]) == kul){
                i++;
                cserel = true;
            } else{
                s[ujhossz] = s[i];
                ujhossz++;
            }
        }
        s[ujhossz] = '\0';
        hossz = ujhossz;
        cout << hossz << endl;
        //cin >> i;
    }
    cout << hossz;
    //cin >> i;
    return 0;
}