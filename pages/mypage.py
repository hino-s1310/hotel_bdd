from playwright.sync_api import Page

class MyPage:
    URL = "https://hotel.testplanisphere.dev/ja/mypage.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.mypage_heading = page.get_by_role("heading", name="マイページ")
        self.email_text = page.locator("id=email")
        self.username_text = page.locator("id=username")
        self.rank_text = page.locator("id=rank")
        self.logout_button = page.get_by_role("button", name="ログアウト")
        self.reserve_link = page.get_by_role("link", name="宿泊予約")

    def load(self) -> None:
        self.page.goto(self.URL)
    
    def click_reserve(self) -> None:
        self.reserve_link.click()

    def click_logout(self) -> None:
        self.logout_button.click()