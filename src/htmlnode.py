class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise  NotImplementedError("This is a child class method")


    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for k,v in self.props.items():
            html_string += f' {k}="{v}"'
        return html_string


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def __eq__(self, other):
        return (self.tag == other.tag and self.value == other.value and self.children == other.children and  self.props == other.props)

#define a LeafNode child class of an HTMLNode
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag,value,None,props)

    #Add a to_html method
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        #if self.props is not None, account for it in the return
        if self.props is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        return f'<{self.tag}>{self.value}</{self.tag}>'
 
   
    #define leaf node representation
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)

    #implement to_html()
    def to_html(self):

        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        children_html = ""
        for child in self.children:
           children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f'ParentNode({self.tag},children: {self.children}, {self.props})'



