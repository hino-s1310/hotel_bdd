import pytest
import re

from components.header import Header
from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from pages.signup import SignUpPage
from pages.icon import IconPage

from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def header(page: Page) -> Header:
    return Header(page)

@pytest.fixture
def home_page(page: Page, header: Header) -> HomePage:
    return HomePage(page, header)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def my_page(page: Page, header: Header) -> MyPage:
    return MyPage(page, header)

@pytest.fixture
def plans_page(page: Page, header:Header) -> PlansPage:
    return PlansPage(page,header)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)

@pytest.fixture
def confirm_page(page: Page) -> ConfirmPage:
    return ConfirmPage(page)

@pytest.fixture
def signup_page(page: Page) -> SignUpPage:
    return SignUpPage(page)

@pytest.fixture
def icon_page(page: Page) -> IconPage:
    return IconPage(page)