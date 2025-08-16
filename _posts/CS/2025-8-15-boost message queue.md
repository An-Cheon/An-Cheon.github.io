---
layout: post
title: boost 消息队列接收端下线后try_send阻塞
categories: [CS, C++]
tags: [c++]
---

在接收端关闭后，如果存在未被处理的信息，发送端使用try_send也会阻塞，此时判断一下消息队列中存在的消息数量，如果消息数量不为0且一段时间不变就不要再发送了，可能接收端已经下线了。

boost队列阻塞和非阻塞通信：

```cpp
send

void send(const void *buffer,     size_type buffer_size,
              unsigned int priority);
             
bool try_send(const void *buffer,  size_type buffer_size,
               unsigned int priority);

bool timed_send(const void *buffer, size_type buffer_size,
                 unsigned int priority,  const boost::posix_time::ptime& abs_time);






receive

inline void message_queue_t<VoidPointer>::receive(void *buffer,        size_type buffer_size,
                        size_type &recvd_size,   unsigned int &priority)
{  this->do_receive(blocking, buffer, buffer_size, recvd_size, priority, ptime()); }

template<class VoidPointer>
inline bool
   message_queue_t<VoidPointer>::try_receive(void *buffer,              size_type buffer_size,
                              size_type &recvd_size,   unsigned int &priority)
{  return this->do_receive(non_blocking, buffer, buffer_size, recvd_size, priority, ptime()); }

template<class VoidPointer>
inline bool
   message_queue_t<VoidPointer>::timed_receive(void *buffer,            size_type buffer_size,
                                size_type &recvd_size,   unsigned int &priority,
                                const boost::posix_time::ptime &abs_time)
{
   if(abs_time == boost::posix_time::pos_infin){
      this->receive(buffer, buffer_size, recvd_size, priority);
      return true;
   }
   return this->do_receive(timed, buffer, buffer_size, recvd_size, priority, abs_time);
}

```
