from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('reserve_plan.feature')

@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

@when('ログインボタンを押下する')
def step_when(home_page: HomePage):
    home_page.click_login()

@when(parsers.parse('email、パスワード欄に「{email}」、「{pwd}」と入力しログインボタンを押下する'))
def step_when(login_page:LoginPage, email, pwd):
    login_page.submit_login(email,pwd)

@when(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_when(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

@when('宿泊予約リンクを押下する')
def step_when(my_page:MyPage):
    my_page.click_reserve()

@when('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_when(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_be_visible()

@when(parsers.parse("「{plan_name}」カードのこのプランで予約ボタンを押下する"))
def step_when(plans_page:PlansPage, plan_name):
    pass

@when('ページの見出しが「宿泊予約」であることを確認する')
def step_when(reserve_page:ReservePage):
    pass

@when('宿泊日欄に今日の日付を入力する')
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('宿泊数欄に「{stay_num}」を入力する'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('人数欄に「{people_num}」を入力する'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('朝食プランのチェックボックスを「{flag_morning}」にする'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('昼からチェックインプランのチェックボックスを「{flag_noon_checkin}」にする'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('お得な観光プランのチェックボックスを「{flag_reasnable_sightseeing}」にする'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('確認のご連絡リストを「{confirm_contact}」に選択する'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('合計欄が「{total_bill}」であることを確認する'))
def step_when(reserve_page:ReservePage):
    pass

@when(parsers.parse('予約内容を確認するボタンを押下する'))
def step_when(reserve_page:ReservePage):
    pass

@then(parsers.parse('ページの見出しが「宿泊予約確認」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('合計金額が「{total_bill}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('プラン名が「{plan_name}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('期間が 今日から「{stay_num}」を足した日までであることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('追加プランが「{additional_plan}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('お名前が「{name}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('確認のご連絡が「{confirm_contact}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then(parsers.parse('ご要望・ご連絡事項等が「{comment}」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    pass

@then('この内容で予約するボタンを押下する')
def step_then(confirm_page:ConfirmPage):
    pass

@then('ページの見出しが「宿泊予約確認」であることを確認する')
def step_then(plans_page:PlansPage):
    pass