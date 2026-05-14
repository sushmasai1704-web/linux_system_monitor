#include <iostream>
#include <fstream>
#include <string>

void getCPUInfo() {
    std::ifstream file("/proc/cpuinfo");
    std::string line;
    while (std::getline(file, line)) {
        if (line.find("model name") != std::string::npos) {
            std::cout << "CPU: " << line.substr(line.find(":") + 2) << "\n";
            break;
        }
    }
}

void getMemInfo() {
    std::ifstream file("/proc/meminfo");
    std::string line;
    int count = 0;
    while (std::getline(file, line) && count < 3) {
        std::cout << line << "\n";
        count++;
    }
}

int main() {
    std::cout << "=== System Info from /proc ===\n";
    getCPUInfo();
    getMemInfo();
    return 0;
}
