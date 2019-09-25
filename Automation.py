def main():
    m= open("main.cpp", "w+")
    m.write("""
    #include <iostream>
    #include "Executive.h"
    int main()
    {


    }
    """)
    m.close()
    e= open("Executive.h", "w+")
    e.write("""
    #ifndef EXECUTIVE_H
    #define EXECUTIVE_H

    #include <iostream>
    #include <string>

    Executive()
    {

    };
    #endif
    """)
    e.close()
main()
