---
layout: post
title: C++ 共享内存(Windows, linux)
categories: [CS, C++]
tags: [c++]
---

main_writer.cpp 

```cpp
#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#ifdef _WIN32
#include <windows.h>
#elif __linux
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#endif

using namespace std;

#ifdef _WIN32
struct MyData
{
    string name;
    int age;
    MyData(string _name, int _age) : name(_name), age(_age)
    {}
};

void writeMemory()
{
    // define shared data
    string shared_file_name = "my_shared_memory";
    unsigned long buff_size = 4096;
    char share_buffer[] = "greetings, hello world";
    //MyData share_buffer("Tom", 18);

    // create shared memory file
    HANDLE dump_file_descriptor = CreateFile(shared_file_name.c_str(),
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_ALWAYS, // open exist or create new, overwrite file
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    if (dump_file_descriptor == INVALID_HANDLE_VALUE)
        cout << "create file error" << endl;

    HANDLE shared_file_handler = CreateFileMapping(
        dump_file_descriptor, // Use paging file - shared memory
        NULL,                 // Default security attributes
        PAGE_READWRITE,       // Allow read and write access
        0,                    // High-order DWORD of file mapping max size
        buff_size,            // Low-order DWORD of file mapping max size
        shared_file_name.c_str());    // Name of the file mapping object

    if (shared_file_handler)
    {
        // map memory file view, get pointer to the shared memory
        LPVOID lp_base = MapViewOfFile(
            shared_file_handler,  // Handle of the map object
            FILE_MAP_ALL_ACCESS,  // Read and write access
            0,                    // High-order DWORD of the file offset
            0,                    // Low-order DWORD of the file offset
            buff_size);           // The number of bytes to map to view



        // copy data to shared memory
        memcpy(lp_base, &share_buffer, sizeof(share_buffer));

        FlushViewOfFile(lp_base, buff_size); // can choose save to file or not

        // process wait here for other task to read data
        cout << "already write to shared memory, wait ..." << endl;
        //cout << share_buffer << endl;
        this_thread::sleep_for(chrono::seconds(100));

        // close shared memory file
        UnmapViewOfFile(lp_base);
        CloseHandle(shared_file_handler);
        CloseHandle(dump_file_descriptor);
        //unlink(shared_file_name);
        cout << "shared memory closed" << endl;
    }
    else
        cout << "create mapping file error" << endl;
}
#elif __linux

struct MyData
{
    char name[20];
    int age;
};

void writeMemory()
{
    // specify shared file path
    char *shared_file_name = "/home/user/codetest/my_shared_memory";

    // define shared data
    //    unsigned long buff_size = 4096;
    //    char share_buffer[] = "greetings, hello world";
    //    MyData share_buffer("Tom", 18);
    MyData share_buffer = { "Tom", 18 };

    // create mmap file
    int fd = open(shared_file_name, O_CREAT | O_RDWR | O_TRUNC, 00777);
    if (fd < 0)
        cout << "create file error" << endl;

    size_t write_size = sizeof(share_buffer);

    ftruncate(fd, write_size); // extend file size

    // map memory to file
    void *p = mmap(NULL, write_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

    // copy data to shared memory
    memcpy(p, &share_buffer, write_size);

    cout << "already write to shared memory, wait ..." << endl;
    //cout << share_buffer << endl;
    this_thread::sleep_for(chrono::seconds(10));

    // unmap and close
    munmap(p, write_size);
    close(fd);

}
#endif

int main()
{
    writeMemory();

    return 0;
}
```

main_reader.cpp

```
#include <iostream>
#include <string>
#ifdef _WIN32
#include <windows.h>
#elif __linux
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#endif

using namespace std;

#ifdef _WIN32
struct MyData
{
    string name;
    int age;
    MyData(string _name, int _age) : name(_name), age(_age)
    {}
};

void readMemory()
{
    string shared_file_name = "my_shared_memory";

    // open shared memory file
    HANDLE shared_file_handler = OpenFileMapping(
        FILE_MAP_ALL_ACCESS,
        NULL,
        shared_file_name.c_str());

    if (shared_file_handler)
    {
        LPVOID lp_base = MapViewOfFile(
            shared_file_handler,
            FILE_MAP_ALL_ACCESS,
            0,
            0,
            0);

        // copy shared data from memory
        cout << "read shared data: " << endl;
        const unsigned long buff_size = 4096;
        //char share_buffer[buff_size] = { 0 };
        //strcpy(share_buffer, (char *)lp_base);
        char *share_buffer = (char *)lp_base;

        cout << share_buffer << endl;

        /*MyData *my_data = (MyData *)lp_base;
        cout << my_data->name << " " << my_data->age << endl;*/

        // close share memory file
        UnmapViewOfFile(lp_base);
        CloseHandle(shared_file_handler);
    }
    else
        cout << "open mapping file error" << endl;
}
#elif __linux
struct MyData
{
    char name[20];
    int age;
};

void readMemory()
{
    // specify shared file path
    char *shared_file_name = "/home/user/codetest/my_shared_memory";

    // open mmap file
    int fd = open(shared_file_name, O_RDONLY, 00777);
    if (fd < 0)
        cout << "open file error" << endl;

    const unsigned long buff_size = 4096;
    //    size_t read_size = buff_size;
    size_t read_size = sizeof(MyData);

    // map file to memory
    void *p = mmap(NULL, read_size, PROT_READ, MAP_SHARED, fd, 0);

    cout << "read shared data: " << endl;

    //    char *share_buffer = (char *)p;
    //    cout << share_buffer << endl;

    MyData *share_buffer = (MyData *)p;
    cout << share_buffer->name << " " << share_buffer->age << endl;

    // unmap and close
    munmap(p, read_size);
    close(fd);
}
#endif

int main()
{
    readMemory();

    getchar();

    return 0;
}

```
