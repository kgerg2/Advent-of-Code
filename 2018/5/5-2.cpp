#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(){
    int i, hossz=50000, db=0, ujhossz;
    bool cserel = true;
    char s[50000];
    //ifstream be (".\\2018\\5\\input.txt");
    cin >> s;
    int kul = 32;
    /* cout << kul << endl;
    cout << (int) 'a'-'A' << endl;
    for(i=0; i<100; i++){
        cout << s[i] << " " << (int)s[i] << endl;
    } */
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
    cout << s; // hossza 6136, bár a változóban más van
    cout << ujhossz;
    //cin >> i;
    return 0;
}