from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "img"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(value=self.text)
        elif self.text_type == TextType.BOLD:
            return LeafNode(tag="b", children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.ITALIC:
            return LeafNode(tag="i", children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.CODE:
            return LeafNode(tag="code", children=[LeafNode(value=self.text)])
        elif self.text_type == TextType.LINK:
            return LeafNode(tag="a", children=[LeafNode(value=self.text)], props={"href": self.url})
        elif self.text_type == TextType.IMG:
            return LeafNode(tag="img", props={"src": self.url, "alt": self.text})
        else:
            raise ValueError(f"Unsupported TextType: {self.text_type}")