from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMG = "![alt text](url)"



class TextNode:

    def __init__(self, text, text_type, url = 0):
        self.text = text                                  # text content of node

        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be a member of the TextType enum")
        self.text_type = text_type                        # type of text in the node

        self.url = url                                    # url of link/img if it's a link


    def __eq__(self, other):
        if isinstance(other, TextNode):
            return False

        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return (
            f"TextNode({ self.text }, " +
            f"{ self.text_type.value }, " +
            f"{ self.url })"
        )
