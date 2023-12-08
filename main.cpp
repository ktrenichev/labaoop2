#include <iostream>
#include <vector>

int findKthPrime(int k) {
    if (k <= 0) return -1;

    int limit = 10000000; // Устанавливаем предел поиска (можно увеличить при необходимости)
    std::vector<bool> sieve(limit, true);
    sieve[0] = sieve[1] = false; // 0 и 1 - не простые числа

    // Применение решета Эратосфена
    for (int p = 2; p * p <= limit; ++p) {
        if (sieve[p]) {
            for (int i = p * p; i < limit; i += p) {
                sieve[i] = false;
            }
        }
    }

    // Поиск k-го простого числа
    int primeCount = 0;
    for (int i = 2; i < limit; ++i) {
        if (sieve[i]) {
            ++primeCount;
            if (primeCount == k) {
                return i;
            }
        }
    }

    return -1; // В случае, если k-е простое число больше установленного предела
}

int main() {
    setlocale(LC_ALL, "Russian");
    int k;
    std::cout << "Введите номер простого числа: ";
    std::cin >> k;

    int kthPrime = findKthPrime(k);
    if (kthPrime != -1) {
        std::cout << k << "-е простое число: " << kthPrime << std::endl;
    }
    else {
        std::cout << "Простое число с таким номером не найдено в пределах заданного диапазона." << std::endl;
    }

    return 0;
}
