---
layout: post
title: 在Windows下编译QScintilla
categories: [CS, C++]
tags: [c++]
---

### 1. 配置QT环境变量,

[下载链接 Riverbank Computing](https://riverbankcomputing.com/software/qscintilla/download)

本人编译时使用的是QScintilla_src-2.14.1 和 Qt 6.10.1

将qmake.exe和mingw32-make.exe两个程序所在的目录添加到windows环境变量中；

### 2. qmake qscintilla.pro 生成Makefile文件

QScintilla_src-2.14.1\src 目录中 

```cmd
qmake qscintilla.pro
```

### 3. mingw32-make 编译

QScintilla_src-2.14.1\src 目录中 

```cmd
mingw32-make
```

### 4. mingw32-make install 安装

QScintilla_src-2.14.1\src 目录中 

```cmd
mingw32-make install
```

### 5. 用演示程序验证 QScintilla 是否能运行

Qt Widgets Application

CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.19)
project(Minimal_1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets)
qt_standard_project_setup()

# 使用 Qt6 的安装路径作为基础
get_target_property(QT6_QMAKE_EXECUTABLE Qt6::qmake IMPORTED_LOCATION)
get_filename_component(QT6_BIN_DIR ${QT6_QMAKE_EXECUTABLE} DIRECTORY)
get_filename_component(QT6_INSTALL_PREFIX ${QT6_BIN_DIR} DIRECTORY)

# QScintilla 头文件和库文件路径
set(QSCINTILLA_INCLUDE_DIR ${QT6_INSTALL_PREFIX}/include)
set(QSCINTILLA_LIBRARY ${QT6_INSTALL_PREFIX}/lib/libqscintilla2_qt6.a)
set(QSCINTILLA_DLL ${QT6_INSTALL_PREFIX}/lib/qscintilla2_qt6.dll)

# 检查 QScintilla 是否存在
if(NOT EXISTS ${QSCINTILLA_LIBRARY})
    message(FATAL_ERROR "QScintilla library not found at ${QSCINTILLA_LIBRARY}")
endif()

# 添加头文件路径
include_directories(${QSCINTILLA_INCLUDE_DIR})

qt_add_executable(Minimal_1
    WIN32 MACOSX_BUNDLE
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
)

target_link_libraries(Minimal_1
    PRIVATE
        Qt::Core
        Qt::Widgets
        ${QSCINTILLA_LIBRARY}
)

include(GNUInstallDirs)
install(TARGETS Minimal_1
    BUNDLE  DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

# 安装 QScintilla DLL
if(EXISTS ${QSCINTILLA_DLL})
    install(FILES ${QSCINTILLA_DLL}
        DESTINATION ${CMAKE_INSTALL_BINDIR}
    )
endif()

qt_generate_deploy_app_script(
    TARGET Minimal_1
    OUTPUT_SCRIPT deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)
install(SCRIPT ${deploy_script})
```
mainwindow.h
```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

// 包含 QScintilla 头文件
#include <Qsci/qsciscintilla.h>
#include <Qsci/qscilexercpp.h>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QsciScintilla *textEdit;
    
    void setupEditor();
};

#endif // MAINWINDOW_H
```

mainwindow.cpp
```cpp
#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QFont>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    
    // 创建 QScintilla 编辑器
    textEdit = new QsciScintilla(this);
    setCentralWidget(textEdit);
    
    setupEditor();
    
    // 设置一些示例代码
    textEdit->setText(
        "#include <iostream>\n\n"
        "int main() {\n"
        "    std::cout << \"Hello, QScintilla!\" << std::endl;\n"
        "    return 0;\n"
        "}\n"
    );
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setupEditor()
{
    // 设置字体
    QFont font("Consolas", 10);
    textEdit->setFont(font);
    textEdit->setMarginsFont(font);
    
    // 设置 C++ 语法高亮
    QsciLexerCPP *lexer = new QsciLexerCPP(textEdit);
    lexer->setFont(font);
    textEdit->setLexer(lexer);
    
    // 显示行号
    textEdit->setMarginType(0, QsciScintilla::NumberMargin);
    textEdit->setMarginWidth(0, "00000");
    textEdit->setMarginsForegroundColor(QColor("#888888"));
    textEdit->setMarginsBackgroundColor(QColor("#f0f0f0"));
    
    // 设置当前行高亮
    textEdit->setCaretLineVisible(true);
    textEdit->setCaretLineBackgroundColor(QColor("#ffe4e4"));
    
    // 设置自动缩进
    textEdit->setAutoIndent(true);
    textEdit->setIndentationWidth(4);
    textEdit->setTabWidth(4);
    textEdit->setIndentationsUseTabs(false);
    
    // 设置括号匹配
    textEdit->setBraceMatching(QsciScintilla::SloppyBraceMatch);
    textEdit->setMatchedBraceBackgroundColor(QColor("#99ff99"));
    textEdit->setUnmatchedBraceForegroundColor(QColor("#ff0000"));
    
    // 启用代码折叠
    textEdit->setFolding(QsciScintilla::BoxedTreeFoldStyle);
    textEdit->setFoldMarginColors(QColor("#f0f0f0"), QColor("#f0f0f0"));
    
    // 设置自动完成
    textEdit->setAutoCompletionSource(QsciScintilla::AcsAll);
    textEdit->setAutoCompletionThreshold(3);
    textEdit->setAutoCompletionCaseSensitivity(false);
    textEdit->setAutoCompletionReplaceWord(true);
}
```

效果：
![](https://raw.githubusercontent.com/An-Cheon/An-Cheon.github.io/master/images/qscintilla_demo.png)  

