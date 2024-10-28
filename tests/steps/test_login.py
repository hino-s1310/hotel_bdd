import re


from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage

from playwright.sync_api import Page,expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('login.feature')

# HOTELPLANISPHEREのホームページにアクセスする
@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()


# ログインボタンを押下する
@when('ログインボタンを押下する')
def step_when_login(home_page: HomePage):
    home_page.click_login()


# email、パスワード欄に「ichiro@example.com」、「password」と入力しログインボタンを押下する
@when(parsers.parse('email、パスワード欄に「{email}」、「{pwd}」と入力しログインボタンを押下する'))
def step_when_login(login_page:LoginPage, email, pwd):
    login_page.submit_login(email,pwd)

# ページの見出しが「マイページ」であることを確認する
@then(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_then(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

# メールアドレスが「ichiro@example.com」であることを確認する
@then(parsers.parse('メールアドレスが「{email}」であることを確認する'))
def step_then(my_page:MyPage, email):
        expect(my_page.email_text).to_have_text(email)

# 氏名が「山田一郎」であることを確認する
@then(parsers.parse('氏名が「{name}」であることを確認する'))
def step_then(my_page:MyPage, name):
    expect(my_page.username_text).to_have_text(name)

# 会員ランクが「プレミアム会員」であることを確認する
@then(parsers.parse('会員ランクが「{rank}」であることを確認する'))
def step_then(my_page:MyPage, rank):
    expect(my_page.rank_text).to_have_text(rank)





