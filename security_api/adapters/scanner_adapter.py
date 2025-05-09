from scanners.google_dorks import google_dork_search

class GoogleDorksAdapter:
    def search(self, query):
        return google_dork_search(query)