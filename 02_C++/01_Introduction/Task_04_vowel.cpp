#include <iostream>
#include <cctype>


int main() {
    char letter, realletter;

    std::cout << "Please enter a letter: ";
    std::cin>>realletter;

    letter = std::tolower(realletter);

    if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u'){
        std::cout << "The letter " <<  realletter << " is vowel." << std::endl;
    }
    else{
        std::cout << "The letter " <<  realletter << " is not vowel." << std::endl;
    }
    return 0;
}