---
layout: post
title:  C++ Fundamentals
categories: [CS, C++]
tags: [c++]
---
<!-- more -->
#### 逻辑运算符（Logical operators）        

&&	逻辑与运算符。如果两个操作数都 true，则条件为 true。	(A && B) 为 false。    

||	逻辑或运算符。如果两个操作数中有任意一个 true，则条件为 true。	(A || B) 为 true。         

!	称为逻辑非运算符。用来逆转操作数的逻辑状态，如果条件为 true 则逻辑非运算符将使其为 false。	!(A && B) 为 true。

#### static

```c++
int foo(){
	static int i = 1; // note:1
	//int i = 1;  // note:2
	i += 1;
	return i;
}
```
静态变量在第一次调用进入 note:1 的时候初始化。且只初始化一次，也就是你第二次调用foo(),不会继续初始化，而会直接跳过。

#### 循环（Loop ）

```c++
for (int i = 0; i < 10; i++) {
    std::cout << i << " ";
}
```

```c++
int i = 0;
while (i < 10) {
    std::cout << i << " ";
    i++;
}
```

```c++
int i = 0;
do {
    std::cout << i << " ";
    i++;
} while (i < 10);
```

#### 条件（Conditional ）

```c++
if (20 > 18) {
  cout << "20 is greater than 18";
}
```

```c++
int time = 20;
if (time < 18) {
  cout << "Good day.";
} else {
  cout << "Good evening.";
}
```
#### 数组（Array ）
```c++
    int n[10]; // n 是一个包含 10 个整数的数组

    // 初始化数组元素          
    for (int i = 0; i < 10; i++)
    {
        n[i] = i + 100; // 设置元素 i 为 i + 100
    }                
    for (int j = 0; j < 10; j++)
    {
        cout <<n[j] << endl;
    }
```

#### 字符串（String）

```c++
	char str1[5] = { 'G', 'O', 'O', 'D', '\0' }; // C风格字符串
	char str2[] = "GOOD"; // C风格字符串
	string str3 = "GOOD"; //C++ 中的 String 类
```

#### 指针（Pointer）

指针是一个变量，其值为另一个变量的地址，即，内存位置的直接地址。就像其他变量或常量一样，您必须在使用指针存储其他变量地址之前，对其进行声明。

```c++
	int  var = 20;   // 实际变量的声明
	int *ip;        // 指针变量的声明

	ip = &var;       // 在指针变量中存储 var 的地址

	cout << "Value of var variable: ";
	cout << var << endl;

	// 输出在指针变量中存储的地址
	cout << "Address stored in ip variable: ";
	cout << ip << endl;

	// 访问指针中地址的值
	cout << "Value of *ip variable: ";
	cout << *ip << endl;
```

#### 引用（Reference）

引用变量是一个别名，也就是说，它是某个已存在变量的另一个名字。一旦把引用初始化为某个变量，就可以使用该引用名称或变量名称来指向变量。

```c++
   // 声明简单的变量
   int    i;
   double d;
 
   // 声明引用变量
   int&    r = i;
   double& s = d;
```

#### 结构体（struct）

结构体是 C++ 中一种用户自定义的可用的数据类型，它允许存储不同类型的数据项和函数。

```c++
// CPP program to initialize data member in c++
#include <iostream>
using namespace std;
struct Student {
    int roll;
    Student(int x) //constructor
    {
        roll = x;
    }
};
int main() // Driver Program
{
    struct Student s(2);
    cout << s.roll;
    return 0;
}
```

```c++

```

```c++

```

```c++

```

```c++

```

```c++

```

#### 术语（term）

注释	comment              
常量 constant      
变量	variable        
声明	declaration         
初始化	initialize         
初始值	initializer	          
运算符	operator      
表达式	expression      a+3,b=a+3       
类型	type	 
对象	object        
if 语句 if statement
