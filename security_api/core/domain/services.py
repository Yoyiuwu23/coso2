class ScannerService:
    def __init__(self, google_adapter, dns_adapter, whois_adapter, nmap_adapter):
        self.google_adapter = google_adapter
        self.dns_adapter = dns_adapter
        self.whois_adapter = whois_adapter
        self.nmap_adapter = nmap_adapter

    def scan_google(self, query):
        return self.google_adapter.search(query)