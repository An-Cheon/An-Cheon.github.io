---
layout: post
title: boost 进程间通信消息队列传递字符串
categories: [CS, C++]
tags: [c++]
---

sender:

```cpp
#include <boost/interprocess/ipc/message_queue.hpp>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
using namespace boost::interprocess;

int main()
{
try {
//Erase previous message queue
message_queue::remove("message_queue");
char MessageStr[100] = "Hello World";
//Create a message_queue.
message_queue mq
(create_only               //only create
, "message_queue"           //name
, 100                       //max message number
, sizeof(MessageStr)               //max message size
);

//Send 100 numbers
std::string sTemp;
for (int i = 0; i < 100; ++i) {
sTemp = to_string(i);
memcpy(MessageStr, to_string(i).c_str(), sizeof(to_string(i).c_str()));
mq.send(&MessageStr, sizeof(MessageStr), 0);
}


}
catch (interprocess_exception& ex) {
std::cout << ex.what() << std::endl;
return 1;
}

return 0;
}
```

receiver:

```cpp
#include <boost/interprocess/ipc/message_queue.hpp>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
using namespace boost::interprocess;

int main()
{
//std::string sTemp;

try {
//Open a message queue.
message_queue mq
(open_only        //only create
, "message_queue"  //name
);

unsigned int priority;
message_queue::size_type recvd_size;

//Receive 100 numbers
//std::string sTemp;
char MessageStr[100]="Hello World";
for (int i = 0; i < 100; ++i)
{
std::string sTemp;
mq.receive(&MessageStr, sizeof(MessageStr), recvd_size, priority);
printf("%s\n", MessageStr);
//printf("I:%d Rec:%d\n",i,number);
}
int a = 0;
int b = 1;
}
catch (interprocess_exception& ex) {
message_queue::remove("message_queue");
std::cout << ex.what() << std::endl;
return 1;
}
message_queue::remove("message_queue");
return 0;

}
```
