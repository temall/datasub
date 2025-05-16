from playwright.sync_api import Page

free_quote = "//*[text()='Free Quote']"
your_name = "#q_name"
your_email = "#q_email"
select_a_service = "#q_service"
service1 = "//*[@text()='Service 1']"
service2 = "//*[@text()='Service 2']"
service3 = "//*[@text()='Service 3']"
your_message = "#q_message"
button_request = "button:has-text('Request A Quote')"
quote_status = "#quoteStatus"


class Quote:

    def __init__(self, page: Page):
        self.page = page

    def fill_quote_form(self,
                        name: str,
                        email: str,
                        message: str,
                        service: str | None = None):
        self.page.locator(your_name).fill(name)
        self.page.locator(your_email).fill(email)
        if service is not None:
            self.page.locator(select_a_service).select_option(service)
        self.page.locator(your_message).fill(message)

    def submit_quote(self):
        self.page.locator(button_request).click()

    def check_quote_status(self, message: str):
        assert self.page.locator(quote_status).text_content() == message
