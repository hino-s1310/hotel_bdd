import pytest
import re


from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage

from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def my_page(page: Page) -> MyPage:
    return MyPage(page)

@pytest.fixture
def plans_page(page: Page) -> PlansPage:
    return PlansPage(page)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)