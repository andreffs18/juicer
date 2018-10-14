import bs4


class GetContentFromHtmlService:
    """
    From given HTML markup document, remove all html tags and return it's clean text.
    This Service uses BeautifulSoup to do the heavy lifting
    """

    VALID_TAGS = [u'h1', u'h2', u'h3', u'h4', u'h5', u'label', u'span', u'title', u'li', u'a', u'p', u'div']

    def __init__(self, html, extra_valid_tags=None):
        """
        Initialize service that cleans HTML document
        :param html: raw HTML document (String)
        :param extra_valid_tags: list of HTML tags to be added to list of VALID_TAGS
        """
        self.html = html
        self.valid_tags = self.VALID_TAGS

        if extra_valid_tags and isinstance(extra_valid_tags, list):
            self.valid_tags.extend(extra_valid_tags)

    @staticmethod
    def _is_visible(element):
        """
        Auxiliar method to check if soup element is visible text.
        """
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif "[if" in element or "endif]" in element:
            return False
        elif isinstance(element, bs4.element.Comment):
            return False
        return True

    def call(self):
        # Setup main soup and search for all content that is present within a "valid_tag"
        soup = bs4.BeautifulSoup(self.html, 'html.parser')
        soups = sum(map(lambda tag: soup.findAll(tag, text=True), self.valid_tags), [])
        # Filter out invisible texts
        visible_soups = filter(self._is_visible, soups)
        # Extract clean text from soups
        clean_content = map(lambda t: t.text, visible_soups)
        # Join clean content by new line character
        return u"\n".join(clean_content)
