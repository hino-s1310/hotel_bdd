from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

# ガーキンファイルの読み込み
scenarios('exists_premium_plan.feature')

# HOTELPLANISPHEREのホームページにアクセスする
@given('HOTELPLANISPHEREのホームページにアクセスする')
def step_given(home_page: HomePage):
    home_page.load()

# ログインボタンを押下する
@when('ログインボタンを押下する')
def step_when_click_login(home_page: HomePage):
    home_page.click_login()

# email、パスワード欄に「<email>」、「<password>」と入力しログインボタンを押下する
@when(parsers.parse('email、パスワード欄に「{email}」、「{pwd}」と入力しログインボタンを押下する'))
def step_when_submit_login(login_page:LoginPage, email, pwd):
    login_page.submit_login(email,pwd)

# ぺージの見出しが「マイページ」であることを確認する
@when(parsers.parse('ページの見出しが「{heading}」であることを確認する'))
def step_when_expect_mypage(my_page:MyPage, heading):
    expect(my_page.mypage_heading).to_have_text(heading)

# 氏名が「<name>」であることを確認する
@when(parsers.parse('氏名が「{name}」であることを確認する'))
def step_when_expect_name(my_page:MyPage, name):
    expect(my_page.username_text).to_have_text(name)

# 会員ランクが「<rank>」であることを確認する
@when(parsers.parse('会員ランクが「{rank}」であることを確認する'))
def step_when_expect_rank(my_page:MyPage, rank):
    expect(my_page.rank_text).to_have_text(rank)

# 宿泊予約リンクを押下する
@when('宿泊予約リンクを押下する')
def step_when_click_reserve_plan(my_page:MyPage):
    my_page.click_reserve()
    
# ページの見出しが「宿泊プラン一覧」であることを確認する
@then('ページの見出しが「宿泊プラン一覧」であることを確認する')
def step_then_expect_planspage(plans_page:PlansPage):
    expect(plans_page.plans_heading).to_be_visible()

# ログインしたアカウントが「<rank>」の時、プレミアムプランの存在を確認する
@then(parsers.parse('ログインしたアカウントが「{rank}」の時、プレミアムプランの存在を確認する'))
def step_then_isexists_premium_plan(plans_page:PlansPage, rank):
    if rank == "プレミアム会員":
        # プレミアム会員の場合、プレミアムプランが存在していることを検証する
        expect(plans_page.premium_text).to_be_visible()
    else:
        # 一般会員の場合、プレミアムプランが存在していないことを検証する
        expect(plans_page.premium_text).not_to_be_visible()