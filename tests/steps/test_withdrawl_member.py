import re

from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage

from playwright.sync_api import Page,expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('withdrawl_member.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('会員登録リンクを押下する')
def step_when(home_page: HomePage):
    home_page.click_signup()

@when(parsers.parse('ページの見出しが「会員登録」であることを確認する'))
def step_when(signup_page: SignUpPage):
    expect(signup_page.signup_heading).to_contain_text("会員登録")

@when(parsers.parse('メールアドレス欄に「{email}」を入力する'))
def step_when(signup_page: SignUpPage, email):
    signup_page.fill_email(email)

@when(parsers.parse('パスワード欄に「{password}」を入力する'))
def step_when(signup_page: SignUpPage, password):
    signup_page.fill_password(password)

@when(parsers.parse('パスワード確認欄に「{password_confirm}」を入力する'))
def step_when(signup_page: SignUpPage, password_confirm):
    signup_page.fill_password_confirm(password_confirm)

@when(parsers.parse('氏名欄に「{name}」を入力する'))
def step_when(signup_page: SignUpPage, name):
    signup_page.fill_name(name)

@when(parsers.parse('会員ランクラジオボタンで「{rank}」を選択する'))
def step_when(signup_page: SignUpPage, rank):
    signup_page.select_rank(rank)

@when(parsers.parse('住所欄に「{address}」を入力する'))
def step_when(signup_page: SignUpPage, address):
    signup_page.fill_address(address)

@when(parsers.parse('電話番号欄に「{phone}」を入力する'))
def step_when(signup_page: SignUpPage, phone):
    signup_page.fill_phone(phone)

@when(parsers.parse('性別リストダウンで「{gender}」を選択する'))
def step_when(signup_page: SignUpPage, gender):
    signup_page.select_gender(gender)

@when(parsers.parse('生年月日欄に「{birthday}」を入力する'))
def step_when(signup_page: SignUpPage, birthday):
    signup_page.fill_birthday(birthday)

@when(parsers.parse('お知らせを{check_flag}'))
def step_when(signup_page: SignUpPage, check_flag):
    signup_page.check_notification(check_flag)

@when(parsers.parse('登録ボタンを押下する'))
def step_when(signup_page: SignUpPage):
    signup_page.click_signup()

@when(parsers.parse('ページの見出しが「マイページ」であることを確認する'))
def step_when(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@when(parsers.parse('退会するボタンを押下'))
def step_when(my_page: MyPage):
    my_page.withdraw_member()

@then(parsers.parse('タイトルに「HOTEL PLANISPHERE」が含まれていることを確認'))
def step_then(page: Page):
    expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))











