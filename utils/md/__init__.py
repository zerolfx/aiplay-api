import markdown
import mdx_math
import mdx_downheader


def convert(text):
    md = markdown.Markdown(
        extensions=[mdx_math.makeExtension(enable_dollar_delimiter=False),
                    mdx_downheader.makeExtension(levels=3),
                    'codehilite',
                    'nl2br'
                    ],
    )
    return md.convert(text)
