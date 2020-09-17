from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about
    the quote (quote content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        content = self.parent.select_one(locator)
        return content.string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        author = self.parent.select_one(locator)
        return author.string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        tags = self.parent.select(locator)
        return [e.string for e in tags]
