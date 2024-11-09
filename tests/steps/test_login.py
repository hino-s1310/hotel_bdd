import re


from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage

from playwright.sync_api import Page,expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('login.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('ログインボタンを押下する')
def step_when_login(home_page: HomePage):
    home_page.click_login()

@when(parsers.parse('email、パスワード欄に「{email}」、「{pwd}」と入力しログインボタンを押下する'))
def step_when_login(login_page:LoginPage, email, pwd):
    login_page.submit_login(email,pwd)

@then(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_then(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

@then(parsers.parse('メールアドレスが「{email}」であることを確認する'))
def step_then(my_page:MyPage, email):
        expect(my_page.email_text).to_have_text(email)

@then(parsers.parse('氏名が「{name}」であることを確認する'))
def step_then(my_page:MyPage, name):
    expect(my_page.username_text).to_have_text(name)

@then(parsers.parse('会員ランクが「{rank}」であることを確認する'))
def step_then(my_page:MyPage, rank):
    expect(my_page.rank_text).to_have_text(rank)





