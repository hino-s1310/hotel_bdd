from pages.home import HomePage
from pages.signup import SignUpPage
from pages.mypage import MyPage
from pages.icon import IconPage
import datetime

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('set_icon.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('会員登録リンクを押下する')
def step_when(home_page: HomePage):
    home_page.click_signup()

@when('ページの見出しが「会員登録」であることを確認する')
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

@when('登録ボタンを押下する')
def step_when(signup_page: SignUpPage):
    signup_page.click_signup()

@when('ページの見出しが「マイページ」であることを確認する')
def step_when(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@when('アイコン設定ボタンを押下する')
def step_when(my_page: MyPage):
    my_page.click_set_icon()

@when('ページの見出しが「アイコン設定」であることを確認する')
def step_when(icon_page: IconPage):
    expect(icon_page.iconpage_heading).to_contain_text("アイコン設定")

@when(parsers.parse('「{img_path}」をアップロードする'))
def step_when(icon_page: IconPage, img_path):
    icon_page.upload_img(img_path)

@when(parsers.parse('拡大・縮小を「{slider_value}」に設定する'))
def step_when(icon_page: IconPage, slider_value):
    icon_page.set_scaling(slider_value)

@when(parsers.parse('枠線の色を「{RGB_value}」に設定する'))
def step_when(icon_page: IconPage, RGB_value):
    icon_page.fill_color(RGB_value)

@when('確定ボタンを押下する')
def step_when(icon_page: IconPage):
    icon_page.click_confirm()

@then('ページの見出しが「マイページ」であることを確認する')
def step_then(my_page: MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@then('アイコンが存在することを確認する')
def step_then(my_page: MyPage):
    expect(my_page.icon).to_be_visible()

@then(parsers.parse('アイコンの枠の色が「{validate_RGB_value}」であることを確認する'))
def step_then(my_page: MyPage, validate_RGB_value):
    expect(my_page.icon).to_have_css("background-color", validate_RGB_value)

@then(parsers.parse('アイコンのスクリーンショットを撮影し、「{screenshot_path}」に格納する'))
def step_then(my_page: MyPage, screenshot_path):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    my_page.icon.screenshot(path=screenshot_path + now + "_icon_screenshot.png")







