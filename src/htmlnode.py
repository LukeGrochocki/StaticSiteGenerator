class HTMLNode:
    def __init__(self = None, tag = None, value : str = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented for HTMLNode")

    def props_to_html(self):
        if self.props is None:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag : str = None, value : str = None, props = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag : str = None, children : list = None, props = None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")
        inner_html = ""       
        for child in self.children:
            inner_html += child.to_html()
        return f'<{self.tag}>{inner_html}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"