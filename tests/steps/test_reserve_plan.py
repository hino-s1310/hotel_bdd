from components.header import Header
from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from playwright.sync_api import expect,Page
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

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

@when('ページの見出しが「マイページ」であることを確認する')
def step_when(my_page:MyPage):
    expect(my_page.mypage_heading).to_contain_text("マイページ")

@when('宿泊予約リンクを押下する')
def step_when(my_page:MyPage):
    my_page.click_reserve()

@when('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_when(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_contain_text("宿泊プラン一覧")

@when(parsers.parse("「{plan_name}」カードのこのプランで予約ボタンを押下する"))
def step_when(plans_page:PlansPage, plan_name):
    
    # ページハンドリング
    with plans_page.page.context.expect_page() as new_page_info:
        plans_page.click_this_reserve(plan_name),
    pytest.new_page = new_page_info.value
    plans_page.page.on("new_page", handle_page)

@when('ページの見出しが「宿泊予約」であることを確認する')
def step_when(reserve_page:ReservePage):
    reserve_page = ReservePage(pytest.new_page)
    expect(reserve_page.reserve_heading).to_contain_text("宿泊予約")

@when('宿泊日欄に明日の日付を入力する')
def step_when(reserve_page:ReservePage, page:Page):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.click_tomorrow()

@when(parsers.parse('宿泊数欄に「{stay_num}」を入力する'))
def step_when(reserve_page:ReservePage, stay_num):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.fill_term(stay_num)

@when(parsers.parse('人数欄に「{people_num}」を入力する'))
def step_when(reserve_page:ReservePage, people_num):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.fill_head_count(people_num)

@when(parsers.parse('朝食プランのチェックボックスを「{flag_morning}」にする'))
def step_when(reserve_page:ReservePage, flag_morning):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.controll_mvc_checkbox(flag_morning)

@when(parsers.parse('昼からチェックインプランのチェックボックスを「{flag_noon_checkin}」にする'))
def step_when(reserve_page:ReservePage, flag_noon_checkin):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.controll_ncc_checkbox(flag_noon_checkin)

@when(parsers.parse('お得な観光プランのチェックボックスを「{flag_reasnable_sightseeing}」にする'))
def step_when(reserve_page:ReservePage, flag_reasnable_sightseeing):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.controll_rsc_checkbox(flag_reasnable_sightseeing)

@when(parsers.parse('確認のご連絡リストを「{confirm_contact}」に選択する'))
def step_when(reserve_page:ReservePage, confirm_contact):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.select_contact(confirm_contact)

@when(parsers.parse('合計欄が「{total_bill}」であることを確認する'))
def step_when(reserve_page:ReservePage, total_bill):
    reserve_page = ReservePage(pytest.new_page)
    expect(reserve_page.total_bill).to_contain_text(total_bill)

@when(parsers.parse('予約内容を確認するボタンを押下する'))
def step_when(reserve_page:ReservePage):
    reserve_page = ReservePage(pytest.new_page)
    reserve_page.click_confirm_reserve_button()

@then(parsers.parse('ページの見出しが「宿泊予約確認」であることを確認する'))
def step_then(confirm_page:ConfirmPage):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.confirm_heading).to_contain_text("宿泊予約確認")

@then(parsers.parse('合計金額が「{total_bill}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, total_bill):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.total_bill).to_contain_text(total_bill)

@then(parsers.parse('プラン名が「{plan_name}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, plan_name):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.plan_name).to_have_text(plan_name)

@then(parsers.parse('期間が 今日から「{stay_num}」を足した日までであることを確認する'))
def step_then(confirm_page:ConfirmPage, stay_num):
    confirm_page = ConfirmPage(pytest.new_page)
    stay_term = confirm_page.calc_term(stay_num)
    expect(confirm_page.term).to_have_text(stay_term)

@then(parsers.parse('追加プランが「{additional_plan}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, additional_plan):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.plans).to_have_text(additional_plan)

@then(parsers.parse('お名前が「{name}様」であることを確認する'))
def step_then(confirm_page:ConfirmPage, name):
    confirm_page = ConfirmPage(pytest.new_page)
    validate_name = name + "様"
    expect(confirm_page.username).to_have_text(validate_name)

@then(parsers.parse('確認のご連絡が「{confirm_contact}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, confirm_contact):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.contact).to_have_text(confirm_contact)

@then(parsers.parse('ご要望・ご連絡事項等が「{comment}」であることを確認する'))
def step_then(confirm_page:ConfirmPage, comment):
    confirm_page = ConfirmPage(pytest.new_page)
    expect(confirm_page.comment).to_have_text(comment)

@then('この内容で予約するボタンを押下する')
def step_then(confirm_page:ConfirmPage):
    confirm_page = ConfirmPage(pytest.new_page)
    confirm_page.click_confirm()

@then('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_then(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_have_text("宿泊プラン一覧")

def handle_page(page):
    page.wait_for_load_state()
    print(page.title())
