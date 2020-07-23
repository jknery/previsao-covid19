import http.client
import mimetypes


class ExtraiDados:

    def __init__(self):
        self.conn = http.client.HTTPSConnection(
            "xx9p7hp1p7.execute-api.us-east-1.amazonaws.com")

    def load_covid_data_acumulado(self):
        payload = ""
        headers = {
            "authority": "xx9p7hp1p7.execute-api.us-east-1.amazonaws.com",
            "method": "GET",
            "path": "/prod/PortalAcumulo",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "Accept-Encoding": "zip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,ja;q=0.7",
            "origin": "https://covid.saude.gov.br",
            "referer": "https://covid.saude.gov.br/?fbclid=IwAR1mlx1mFSxaMUfPXSso-TM936HNfW5ZOYnl48taVYmGmuoZLtNN5G7B-_o",
            "sec-fetch-mode": "cors",
            "sec-fetch-size": "cross-site",
            "x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm",
        }
        self.conn.request("GET", "/prod/PortalAcumulo", payload, headers)
        res = self.conn.getresponse()
        return res.read()

    def load_covid_data_por_dia(self):
        payload = ""
        headers = {
            "authority": "xx9p7hp1p7.execute-api.us-east-1.amazonaws.com",
            "method": "GET",
            "path": "/prod/PortalDias",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "Accept-Encoding": "zip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,ja;q=0.7",
            "origin": "https://covid.saude.gov.br",
            "referer": "https://covid.saude.gov.br/?fbclid=IwAR1mlx1mFSxaMUfPXSso-TM936HNfW5ZOYnl48taVYmGmuoZLtNN5G7B-_o",
            "sec-fetch-mode": "cors",
            "sec-fetch-size": "cross-site",
            "x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm",
        }
        self.conn.request("GET", "/prod/PortalDias", payload, headers)
        res = self.conn.getresponse()
        return res.read()

    def load_covid_por_regiao(self):
        payload = ""
        headers = {
            "authority": "xx9p7hp1p7.execute-api.us-east-1.amazonaws.com",
            "method": "GET",
            "path": "/prod/PortalRegiao",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "Accept-Encoding": "zip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,ja;q=0.7",
            "origin": "https://covid.saude.gov.br",
            "referer": "https://covid.saude.gov.br/?fbclid=IwAR1mlx1mFSxaMUfPXSso-TM936HNfW5ZOYnl48taVYmGmuoZLtNN5G7B-_o",
            "sec-fetch-mode": "cors",
            "sec-fetch-size": "cross-site",
            "x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm",
        }
        self.conn.request("GET", "/prod/PortalRegiao", payload, headers)
        res = self.conn.getresponse()
        return res.read()
