import os
import shutil

def makeMain():
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
def makeDirectory():
    lab= raw_input("What do you want the name of the directory to be: ")
    os.mkdir(lab)
    shutil.move("main.cpp", lab)
    shutil.move("Executive.h", lab)


makeMain()
makeDirectory()
