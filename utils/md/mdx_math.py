import markdown
from markdown.util import etree
from . import katex


class MathExtension(markdown.extensions.Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'enable_dollar_delimiter': [False, 'Enable single-dollar delimiter'],
        }
        super(MathExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        def handle_match(m):
            text = m.group(3)
            return etree.fromstring(katex.convert(text))


        inlinemathpatterns = (
            markdown.inlinepatterns.Pattern(r'(?<!\\|\$)(\$)([^\$]+)(\$)'),   #  $...$
            markdown.inlinepatterns.Pattern(r'(?<!\\)(\\\()(.+?)(\\\))')      # \(...\)
        )
        mathpatterns = (
            markdown.inlinepatterns.Pattern(r'(?<!\\)(\$\$)([^\$]+)(\$\$)'),  # $$...$$
            markdown.inlinepatterns.Pattern(r'(?<!\\)(\\\[)(.+?)(\\\])'),     # \[...\]
        )
        if not self.getConfig('enable_dollar_delimiter'):
            inlinemathpatterns = inlinemathpatterns[1:]
        for i, pattern in enumerate(inlinemathpatterns):
            pattern.handleMatch = handle_match
            md.inlinePatterns.add('math-inline-%d' % i, pattern, '<escape')
        for i, pattern in enumerate(mathpatterns):
            pattern.handleMatch = handle_match
            md.inlinePatterns.add('math-%d' % i, pattern, '<escape')


def makeExtension(*args, **kwargs):
    return MathExtension(*args, **kwargs)