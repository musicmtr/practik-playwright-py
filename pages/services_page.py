from components.services_section import ServicesSection

class ServicePage:

    def __init__(self, page):
        self.page = page

    def get_sections(self):
        sections_locator = self.page.locator("section")
        sections = []
        count = sections_locator.count()

        for i in range(count):
            section = ServicesSection(sections_locator.nth(i))
            sections.append(section)

        return sections

    def get_services_in_container(self, container_name):
        # можно искать и по id=first-category но фишка поиска карусели пропадает, если поставят новую категорию в начало
        title = self.page.get_by_role("heading", name=container_name)
        container = title.locator("xpath=../../..")
        titles = container.locator("h4")

        return [t.strip().lower() for t in titles.all_text_content]

    # def get_section_by_title(self, title):
    #     sections = self.get_sections()
    #
    #     for sect in sections:
    #         if sect.get_title() == title.lower():
    #             return sect
    #     raise Exception(f"Section '{title}' netu")
