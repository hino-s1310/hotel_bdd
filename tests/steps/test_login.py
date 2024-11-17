from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
import json

# ガーキンファイルの読み込み
scenarios('login.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('ログインボタンを押下する')
def step_when_login(home_page: HomePage):
    home_page.click_login()

@when(parsers.parse('ログイン画面で「{login_input}」を入力しログインボタンを押下する'))
def step_when_login(login_page:LoginPage, login_input):
    login_input_list = json.loads(login_input)
    email = login_input_list['ログイン情報']['email']
    pwd = login_input_list['ログイン情報']['password']
    login_page.submit_login(email,pwd)

@then(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_then(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

@then(parsers.parse('マイページの各項目が「{login_validate}」であることを確認する'))
def step_then(my_page:MyPage, login_validate):
    login_validate_list = json.loads(login_validate)
    email = login_validate_list['マイページ情報']['email']
    name = login_validate_list['マイページ情報']['name']
    rank = login_validate_list['マイページ情報']['rank']
    expect(my_page.email_text).to_have_text(email)
    expect(my_page.username_text).to_have_text(name)
    expect(my_page.rank_text).to_have_text(rank)

@then('マイページをログアウトする')
def step_then(my_page:MyPage):
    my_page.click_logout()





