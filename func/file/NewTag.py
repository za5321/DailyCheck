from bs4 import BeautifulSoup


class NewTag:
    def __init__(self, data: str):
        self.data = data
        self.soup = BeautifulSoup(data, 'lxml')
        self.parent_tag, self.input_tag = "", ""

    def create(self, parent_tag: str, input_tag: str, tag_string: str = None) -> str:
        self.parent_tag, self.input_tag = parent_tag, input_tag

        new_tag = self.soup.new_tag(input_tag)
        if tag_string:
            new_tag.string = tag_string
        self.soup.find(self.parent_tag).insert(1, new_tag)
        return str(self.soup)
