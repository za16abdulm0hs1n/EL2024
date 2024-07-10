#include <iostream>

int main(){
    int num = 0, sum = 0, temp = 0;
    std::cout << "Please enter an interger:" << std::endl;
    std::cin >> num;
    num = (int) num;

    temp = num;
    while (temp != 0){
        sum += temp % 10;
        temp /= 10;
    }

    std::cout << "The sum of the dighit of " << num << " is: " << sum << std::endl;
    return 0;
}