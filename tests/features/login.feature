Feature: HOTEL_PLANISPHEREログイン

  Scenario Outline: Login
    Given HOTELPLANISPHEREのホームページにアクセスする
    When ログインボタンを押下する
    And email、パスワード欄に「<email>」、「<password>」と入力しログインボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And メールアドレスが「<email>」であることを確認する
    And 氏名が「<name>」であることを確認する
    And 会員ランクが「<rank>」であることを確認する  

    Examples:
    | name | email | password | rank |  
    | 山田一郎 | ichiro@example.com | password | プレミアム会員 |  
    | 松本さくら | sakura@example.com | pass1234 | 一般会員 |  
    | 林潤 | jun@example.com | pa55w0rd! | プレミアム会員 |  
    | 木村良樹 | yoshiki@example.com | pass-pass | 一般会員 |  