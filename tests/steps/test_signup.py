import re


from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage

from playwright.sync_api import Page,expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('signup.feature')

# HOTELPLANISPHEREのホームページにアクセスする
@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()


# 会員登録リンクを押下する
@when('会員登録リンクを押下する')
def step_when(home_page: HomePage):
    home_page.click_signup()

# ページの見出しが「会員登録」であることを確認する
@when(parsers.parse('ページの見出しが「会員登録」であることを確認する'))
def step_when(signup_page: SignUpPage):
    expect(signup_page.signup_heading).to_contain_text("会員登録")

# メールアドレス欄に「<email>」を入力する
@when(parsers.parse('メールアドレス欄に「{email}」を入力する'))
def step_when(signup_page: SignUpPage, email):
    signup_page.fill_email(email)

# パスワード欄に「<password>」を入力する
@when(parsers.parse('パスワード欄に「{password}」を入力する'))
def step_when(signup_page: SignUpPage, password):
    signup_page.fill_password(password)

# パスワード確認欄に「<password_confirm>」を入力する
@when(parsers.parse('パスワード確認欄に「{password_confirm}」を入力する'))
def step_when(signup_page: SignUpPage, password_confirm):
    signup_page.fill_password_confirm(password_confirm)

# 氏名欄に「<name>」を入力する
@when(parsers.parse('氏名欄に「{name}」を入力する'))
def step_when(signup_page: SignUpPage, name):
    signup_page.fill_name(name)

# 会員ランクラジオボタンで「<rank>」を選択する
@when(parsers.parse('会員ランクラジオボタンで「{rank}」を選択する'))
def step_when(signup_page: SignUpPage, rank):
    signup_page.select_rank(rank)

# 住所欄に「<address>」を入力する
@when(parsers.parse('住所欄に「{address}」を入力する'))
def step_when(signup_page: SignUpPage, address):
    signup_page.fill_address(address)

# 電話番号欄に「<phone>」を入力する
@when(parsers.parse('電話番号欄に「{phone}」を入力する'))
def step_when(signup_page: SignUpPage, phone):
    signup_page.fill_phone(phone)

# 性別リストダウンで「<gender>」を選択する
@when(parsers.parse('性別リストダウンで「{gender}」を選択する'))
def step_when(signup_page: SignUpPage, gender):
    signup_page.select_gender(gender)

# 生年月日欄に「<birthday>」を入力する
@when(parsers.parse('生年月日欄に「{birthday}」を入力する'))
def step_when(signup_page: SignUpPage, birthday):
    signup_page.fill_birthday(birthday)

# お知らせを<check_flag>
@when(parsers.parse('お知らせを{check_flag}'))
def step_when(signup_page: SignUpPage, check_flag):
    signup_page.check_notification(check_flag)

# 登録ボタンを押下する
@when(parsers.parse('登録ボタンを押下する'))
def step_when(signup_page: SignUpPage):
    signup_page.click_signup()

# ページの見出しが「マイページ」であることを確認する
@then(parsers.parse('ページの見出しが「マイページ」であることを確認する'))
def step_then(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

# メールアドレスが「<email>」であることを確認する
@then(parsers.parse('メールアドレスが「{email}」であることを確認する'))
def step_then(my_page: MyPage, email):
    expect(my_page.email_text).to_contain_text(email)

# 氏名が「<name>」であることを確認する
@then(parsers.parse('氏名が「{name}」であることを確認する'))
def step_then(my_page: MyPage, name):
    expect(my_page.username_text).to_contain_text(name)

# 会員ランクが「<rank>」であることを確認する
@then(parsers.parse('会員ランクが「{rank}」であることを確認する'))
def step_then(my_page: MyPage, rank):
    expect(my_page.rank_text).to_contain_text(rank)

# 住所が「<address>」であることを確認する
@then(parsers.parse('住所が「{address}」であることを確認する'))
def step_then(my_page: MyPage, address):
    expect(my_page.address_text).to_contain_text(address)

# 電話番号が「<phone>」であることを確認する
@then(parsers.parse('電話番号が「{phone}」であることを確認する'))
def step_then(my_page: MyPage, phone):
    expect(my_page.phone_text).to_contain_text(phone)

# 性別が「<gender>」であることを確認する
@then(parsers.parse('性別が「{gender}」であることを確認する'))
def step_then(my_page: MyPage, gender):
    expect(my_page.gender_text).to_contain_text(gender)

# 生年月日が「<year>年<month>月<day>日」であることを確認する
@then(parsers.parse('生年月日が「{validate_birthday}」であることを確認する'))
def step_then(my_page: MyPage, validate_birthday):
    expect(my_page.birthday_text).to_contain_text(validate_birthday) 

# お知らせが「<check_flag>」であることを確認する
@then(parsers.parse('お知らせが「{check_flag}」であることを確認する'))
def step_then(my_page: MyPage, check_flag):
    expect(my_page.notification_text).to_contain_text(check_flag)






