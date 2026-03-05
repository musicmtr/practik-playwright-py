class ServicesSection:

    def __init__(self, locator):
        self.locator = locator

    def get_title(self):
        return self.locator.inner_text().strip().lower()

    def get_services(self):

        carousel = self.locator.locator(
            "xpath=following::div[@data-t-id='components-CardsCarousel'][1]"
        )

        titles = carousel.locator("h4")

        return [t.strip().lower() for t in titles.all_text_contents()]