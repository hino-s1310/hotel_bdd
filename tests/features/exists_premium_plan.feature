Feature: プレミアム会員でログインした時、プレミアムプランが表示される

  Scenario Outline: isExists_Premium_Plan
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And email、パスワード欄に「<email>」、「<password>」と入力しログインボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And 氏名が「<name>」であることを確認する
    And 会員ランクが「<rank>」であることを確認する
    And 宿泊予約リンクを押下する
    Then ページの見出しが「宿泊プラン一覧」であることを確認する
    And ログインしたアカウントが「<rank>」の時、プレミアムプランの存在を確認する

    Examples:
    | name | email | password | rank |  
    | 山田一郎 | ichiro@example.com | password | プレミアム会員 |  
    | 松本さくら | sakura@example.com | pass1234 | 一般会員 |  
    | 林潤 | jun@example.com | pa55w0rd! | プレミアム会員 |  
    | 木村良樹 | yoshiki@example.com | pass-pass | 一般会員 |  