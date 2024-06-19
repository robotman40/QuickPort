# QuickPort - One Codebase, Multiple Platforms
QuickPort is a simple and easy-to-use Win32 wrapper that utilizes Wine (in addition to Box64 and Box86), enabling developers to bring their applications to multiple platforms.

## Can't compatibility layers be used standalone?
That is true, but you are more likely to encounter compatibility issues, especially when developers do not officially support these solutions. With QuickPort, developers can test their applications against multiple environments, allowing for them to be distributed in a guaranteed environment while sparing them the development time that would come from directly porting their applications

## As a developer, will I have to make any changes to my program?
In many cases, you will not have to make any changes to your program as you can often expect it to work out-of-the-box given how far the projects used (i.e. Wine, DXVK, Box64) have come. If your program happens to have any bugs with those projects, please report them to their respective authors. While they are being investigated, you can apply workarounds in your projects (such as using different APIs).

## What about Mac support?
I do not have any Macs that could serve as testing machines and Apple already provides tools that make porting to Mac convenient (such as the Game Porting Toolkit), so I strongly recommend using their tools instead. I would welcome someone to port this tool to Mac, however.

# Building
It is NOT currently possible due to PyInstaller's incompatibility with pathlib. I will work to remove this project's reliance on pathlib at some point to allow PyInstaller to work, though.

# Credits
This project is possible thanks to the people listed below
### Wrapper projects that enable this:
* [Wine](https://www.winehq.org/) by the [Wine Authors](https://wiki.winehq.org/Who%27s_Who)
* [DXVK](https://github.com/doitsujin/dxvk) by [Philip Rebohle](https://github.com/doitsujin)
* [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton) by [Hans-Kristian Arntzen](https://github.com/HansKristian-Work)
* [Box64](https://github.com/ptitSeb/box64) and [Box86](https://github.com/ptitSeb/box86) by [ptitSeb](https://github.com/ptitSeb)
