import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        node3 = TextNode(
            "This is a text node",
            TextType.IMG,
            "https://storage.googleapis.com" +
            "/qvault-webapp-dynamic-assets/course_assets/qyHo5HQ.png"
        )
        node4 = TextNode( "This is a text node", TextType.IMG)

        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)


    def test_url_None(self):
        with self.assertRaises( TypeError) as context:
             TextNode("this is an image node",TextType.IMG,None)


    def test_text_None(self):
        with self.assertRaises(TypeError) as context:
            TextNode(None, TextType.BOLD)


    def test_not_texttype(self):
        with self.assertRaises(ValueError) as context:
            TextNode([], None)


    def test_repr(self):
        node = TextNode("This is a text node",
            TextType.NORMAL,
            "https://www.boot.dev"
        )

        self.assertEqual(
            f"TextNode(This is a text node, {node.text_type.value}, https://www.boot.dev)",
            repr(node)
        )



if __name__ == "__main__":
    unittest.main()
