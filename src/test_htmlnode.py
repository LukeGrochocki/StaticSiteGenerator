import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(tag="div", value="Hello", children=None, props={"class": "my-class"})
        node2 = HTMLNode(tag="div", value="Hi!", children=None, props={"class": "my-ass"})
        node1.props_to_html()
        node2.props_to_html()
        print(node1)

if __name__ == "__main__":
    unittest.main()