Feature: 会員登録を行い、退会手続きを行う

  Scenario Outline: withdrawl_member
    Given HOTELPLANISPHEREのホームページにアクセスする
    When 会員登録リンクを押下する
    And ページの見出しが「会員登録」であることを確認する
    And 会員登録画面で「<signup_input>」を入力する
    And 登録ボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And 退会するボタンを押下
    Then タイトルに「HOTEL PLANISPHERE」が含まれていることを確認

    Examples:
    | signup_input |  
    | {"会員情報_入力":{"name": "森本雄介", "email": "yusuke@example.com", "password":"pazzw0rd", "password_confirm":"pazzw0rd", "rank":"プレミアム会員", "address":"豊島区", "phone":"04099999999", "gender":"男性", "birthday":"1999-01-01","check_flag":"受け取る"}} |