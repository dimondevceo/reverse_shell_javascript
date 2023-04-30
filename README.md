# Description
A reverse shell in JavaScript using WebSockets
# Setup and Use
`pip install websockets asyncio`
Then, you need to change your server's IP in the file `server.py`, and in the file `client.html` and upload it to the target server. To test locally, simply open it in your browser.
To run the server, open a terminal window and type:
`python server.py`
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
