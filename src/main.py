from textnode import TextNode, TextType


def main():

    new_textnode = TextNode(                    # comes from the markdown link in the notes
        ".gitignore",
        TextType.LINK,
        "https://git-scm.com/docs/gitignore"
    )

    print (new_textnode)



main()
