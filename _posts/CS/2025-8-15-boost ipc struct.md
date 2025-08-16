---
layout: post
title: boost 进程间通信消息队列传递结构体
categories: [CS, C++]
tags: [c++]
---

sender

```cpp
#include <boost/interprocess/ipc/message_queue.hpp>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
using namespace boost::interprocess;


struct MyData
{
    string name;
    int age;
    MyData(string _name, int _age) : name(_name), age(_age)
    {}
};  

int main()
{
try {
//Erase previous message queue
//message_queue::remove("message_queue");
//message_queue::remove
char MessageStr[100] = "Hello World";
//Create a message_queue.
message_queue mq
(open_only               //open or create
, "message_queue"           //name
);

//Send 100 numbers
MyData data_temp("tom ", 0);
for (int i = 0; i < 4; ++i) {
data_temp.name = data_temp.name + to_string(i);
data_temp.age = i;
//memcpy(MessageStr, to_string(i).c_str(), sizeof(to_string(i).c_str()));
mq.send(&data_temp, sizeof(data_temp), 0);
data_temp.name = "tom ";
}


}
catch (interprocess_exception& ex) {
std::cout << ex.what() << std::endl;
return 1;
}

return 0;
}

```

receiver

```cpp
#include <boost/interprocess/ipc/message_queue.hpp>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
using namespace boost::interprocess;


struct MyData
{
    string name;
    int age;
    MyData(string _name, int _age) : name(_name), age(_age)
    {}
};  


int main()
{
//std::string sTemp;

try {
//Open a message queue.
char MessageStr[100]="Hello World";

message_queue::remove("message_queue");

std::string sTemp = "";
MyData data_temp("", 0);

message_queue mq
(open_or_create               //open or create
, "message_queue"           //name
, 100                       //max message number
, sizeof(data_temp)               //max message size
);

unsigned int priority;
message_queue::size_type recvd_size;

//Receive 100 numbers
//std::string sTemp;
//std::string sTemp;

for (int i = 0; i < 60; ++i)
{
mq.receive(&data_temp, sizeof(data_temp), recvd_size, priority);
printf("%s   %d\n",data_temp.name.c_str(), data_temp.age);
//printf("%s\n", sTemp);
//printf("I:%d Rec:%d\n",i,number);
int ac = 0;
}

}
catch (interprocess_exception& ex) {
message_queue::remove("message_queue");
std::cout << ex.what() << std::endl;
return 1;
}
//message_queue::remove("message_queue");
return 0;

}
```
