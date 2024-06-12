# QuickPort - One Codebase, Multiple Platforms
QuickPort is a simple and easy-to-use program that wraps a Win32 application with Wine (and optionally Box64 and Box86), enabling developers to bring their applications to multiple platforms.

## Can't compatibility layers be used standalone?
That is true, but you are more likely to encounter compatibility issues, especially when developers do not officially support these solutions. With QuickPort, developers are able to test their applications against multiple environments, allowing for effective compatibility while sparing them the development time that would come from directly porting their applications

## As a developer, will I have to make any changes to my program?
In many cases, you will not have to make any changes to your program as you can often expect it to work out-of-the-box given how far the projects used (i.e. Wine, DXVK, Box64) have come. If your program encounters any bugs with those projects, please report them to their respective authors and while they are being investigated, you can apply workarounds in your projects (such as using different APIs).
