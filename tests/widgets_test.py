import pytest

from pages.widgets_page import WidgetsPage


class TestWidgetsPage:
    class TestAccordianPage:
        @pytest.mark.debug
        def test_accordian(self, browser):
            page = WidgetsPage(browser, 'https://demoqa.com/accordian')
            page.open()
            first_section_title, first_section_content = page.check_accordian('first')
            second_section_title, second_section_content = page.check_accordian('second')
            third_section_title, third_section_content = page.check_accordian('third')
            assert first_section_title == 'What is Lorem Ipsum?' and len(first_section_content) > 0
            assert second_section_title == 'Where does it come from?' and len(second_section_content) > 0
            assert third_section_title == 'Why do we use it?' and len(third_section_content) > 0


