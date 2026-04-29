from textnode import TextNode, TextType

def main():
    text_node1 = TextNode("Hello, World!", TextType.TEXT)
    print(text_node1.text)
    print(text_node1.text_type)
    print(text_node1.url)
    print(text_node1)


if __name__ == "__main__":
    main()