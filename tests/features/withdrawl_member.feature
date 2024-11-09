Feature: 会員登録を行い、退会手続きを行う

  Scenario Outline: withdrawl_member
    Given HOTELPLANISPHEREのホームページにアクセスする
    When 会員登録リンクを押下する
    And ページの見出しが「会員登録」であることを確認する
    And メールアドレス欄に「<email>」を入力する
    And パスワード欄に「<password>」を入力する
    And パスワード確認欄に「<password_confirm>」を入力する
    And 氏名欄に「<name>」を入力する
    And 会員ランクラジオボタンで「<rank>」を選択する
    And 住所欄に「<address>」を入力する
    And 電話番号欄に「<phone>」を入力する
    And 性別リストダウンで「<gender>」を選択する
    And 生年月日欄に「<birthday>」を入力する
    And お知らせを<check_flag>
    And 登録ボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And 退会するボタンを押下
    Then タイトルに「HOTEL PLANISPHERE」が含まれていることを確認

    Examples:
    | name | email | password | password_confirm | rank | address | phone | gender | birthday | validate_birthday | check_flag |  
    | 森本雄介 | yusuke@example.com | pazzw0rd | pazzw0rd | プレミアム会員 | 豊島区 | 04099999999 | 男性 | 1999-01-01 | 1999年1月1日 | 受け取る |  
    