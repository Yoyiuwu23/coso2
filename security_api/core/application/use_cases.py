class ScanUseCase:
    def __init__(self, scanner_service):
        self.scanner_service = scanner_service

    def execute_google_scan(self, query):
        return self.scanner_service.scan_google(query)