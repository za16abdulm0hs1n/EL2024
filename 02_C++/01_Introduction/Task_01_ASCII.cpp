#include<iostream>
#include<iomanip>


int main() {
    std::cout << "ASCII Code Table" << std::endl;
    std::cout << "+------+------+" << std::endl;
    std::cout << "| Char | ASCII|" << std::endl;
    std::cout << "+------+------+" << std::endl;

    for (int i = 0; i < 128; i++){
        std::cout << "|  ";
        if (i < 32 || i == 127){
            // non printable characters
            std::cout << "  ";
        } 
        else{
            std::cout << static_cast<char>(i) << " ";
        }
        std::cout << "  |  " << std::setw(3) << i << " |" << std::endl;


    }
    std::cout << "+------+------+" << std::endl;
    return 0;
}