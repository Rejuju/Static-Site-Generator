from textnode import *
from htmlnode import *

def main():
    dummy_text_node = TextNode("please be right", "plain", "https://pleaseberight.ca")
    dummy_html_node = HTMLNode("c", "sometext", None, None)
    print(f"{dummy_text_node}\n{dummy_html_node}")


main()
