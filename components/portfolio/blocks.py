from components.blocks.base_blocks import BaseStreamBlock, CardBlock, FeaturedPostsBlock


class PortfolioStreamBlock(BaseStreamBlock):
    card = CardBlock(group="Sections")
    featured_posts = FeaturedPostsBlock(group="Sections")