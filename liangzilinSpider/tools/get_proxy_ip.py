import requests

class GetProxyIp(object):
    def check_proxy(self, url, port):
        """
        验证代理是否可用
        """
        http_url = "https://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(url, port)
    
        try:
            response = requests.get(http_url, proxies={"http": proxy_url})

            code = response.status_code
            if 200 <= code and code < 300:
                print("IP代理： {0}".format(proxy_url))
                return True
            else:
                print("失效的IP代理")
                return False
        except Exception:
            print("失效的IP代理")
            return False
    
    def get_one_ip(self):
        """
        取一个IP地址
        """
        url = "http://127.0.0.1:8111/proxy"
        response = requests.get(url).json()
        proxy_url = response[0][0]
        proxy_port = response[0][1]

        if self.check_proxy(proxy_url, proxy_port):
            return "http://{0}:{1}".format(proxy_url, proxy_port)

if __name__ == '__main__':
    get_ip = GetProxyIp()
    ip = get_ip.get_one_ip()
    print(ip)
