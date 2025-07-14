from django import forms
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, IntegerBlock, BooleanBlock, ChoiceBlock
from wagtail.images.blocks import ImageBlock




class PriceBlock(StructBlock):
    notice = CharBlock(required=False)
    amount = CharBlock(required=False)


class PriceStreamBlock(StreamBlock):
    price = PriceBlock(required=False)


class CardCheckBlock(StructBlock):
    state = ChoiceBlock(required=True,
                        choices=[
                            ("perfect", "Perfect"),
                            ("good", "Good"),
                            ("garbage", "Garbage"),
                        ], widget=forms.RadioSelect())

    rarity = ChoiceBlock(required=True,
                       choices=[
                           ("rare", "Rare"),
                           ("uncommon", "Uncommon"),
                           ("common", "Common"),
                       ], widget=forms.RadioSelect())


class CardCheckStreamBlock(StreamBlock):
    card = CardCheckBlock(required=False)


class RegularCardBlock(StructBlock):
    heading = CharBlock(required=False)
    price = PriceStreamBlock(required=False, max_num=3)
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    image = ImageBlock(required=False)
    card_check = CardCheckStreamBlock(required=False, max_num=1)

    class Meta:
        icon = "folder-open-inverse"
        template = "card/regular_card_block.html"


class CardStreamBlock(StreamBlock):
    card = RegularCardBlock(group="Cards")