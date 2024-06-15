# NOTICE: This project is still currently work-in-progress. I have been making good progress however and you can expect the first version (0.0.1) to ship sometime next week

# QuickPort - One Codebase, Multiple Platforms
QuickPort is a simple and easy-to-use Win32 wrapper that utilizes Wine (and optionally Box64 and Box86), enabling developers to bring their applications to multiple platforms.

## Can't compatibility layers be used standalone?
That is true, but you are more likely to encounter compatibility issues, especially when developers do not officially support these solutions. With QuickPort, developers are able to test their applications against multiple environments, allowing for them to be distributed in a guaranteed environment while sparing them the development time that would come from directly porting their applications

## As a developer, will I have to make any changes to my program?
In many cases, you will not have to make any changes to your program as you can often expect it to work out-of-the-box given how far the projects used (i.e. Wine, DXVK, Box64) have come. If your program encounters any bugs with those projects, please report them to their respective authors and while they are being investigated, you can apply workarounds in your projects (such as using different APIs).

## What about Mac support?
I do not have any Macs that could serve as testing machines and Apple already provides tools that make porting to Mac convenient (such as the Game Porting Toolkit), so I strongly recommend using their tools instead. I would welcome someone to port this tool to Mac however.

# Building
**Prerequisites**

• Python 3.12.1 (Note that other Python versions may work, but this program is only officially tested against the stated version)

• Pyinstaller

Since this is a Python script, you can simply run `main.py` and input the appropriate parameters, but it is recommended to use a compiled build. To do so, run `install.py` in the QuickPort's directory and allow it to build and once that is done, you can get started with porting your applications!
