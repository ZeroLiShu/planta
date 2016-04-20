from .common import BeautifulSoup
from requests import Response

class BaseEflora:
    def _gen_soup(self, content):
        self.soup = BeautifulSoup(content)

    def _get_content(self):
        resp = self._session.get(self.url[:-1])
        return resp.content

    def _make_soup(self):
        if self.url and not self.soup:
            self._gen_soup(self._get_content())

    def refresh(self):
        # refresh self.soup's content
        self._gen_soup(self._get_content())