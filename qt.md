__int main(int argc, char *argv[])__  
    here  
        argc = number of argument count.  
        argv[] = an array of arguments. The first element of the array is name of the program. so variable `argc` has value at least 1.  

__Dot(.) operator VS Arrow(->) operator__  
    Dot(.) operator is used to access a class member.  
    `object.class_member`  
    Arrow(->) operator is used to access a class member of an object pointer.  
    `object_pointer->class_member`

__#ifdef__  
    The #ifdef directive allows for conditional compilation. The preprocessor determines if the provided macro exists before including the subsequent code in the compilation process.  
    `#ifdef macro_definition`  
    example code:  
    ```
        #ifdef Q_OS_ANDROID
            httpWin.showMaximized();
        #else
            httpWin.show();
        #endif
    ```  
    Here if Q_OS_ANDROID macro evaluates to True then `httpwin.showMaximized()` will be included in compilable codes.

    
    