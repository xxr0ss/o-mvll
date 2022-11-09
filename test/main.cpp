#include <iostream>

int func(int a, int b) {
    return a + b;
}

int main() {
    volatile int a = 0;
    volatile int b = 1;
    int c = func(a, b);
    std::cout << c << std::endl;
}