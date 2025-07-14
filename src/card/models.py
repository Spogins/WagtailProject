from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField

from components.card.blocks import CardStreamBlock


class CardIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        cards = self.get_children()
        context['cards'] = cards
        return context


class CardPage(Page):
    intro = RichTextField(blank=True)

    body = StreamField(
        CardStreamBlock(),
        blank=True,
        use_json_field=True,
        help_text="Use this section to list your projects and skills.",
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel("body"),

    ]


