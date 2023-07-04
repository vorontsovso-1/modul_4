<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page 2</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity=
            "sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <style>
        a {
            font-size: 50px;
        }
    </style>

</head>
<body>
   <form action="">
       <label for="field1">Просто текст</label>
       <input id="field1" type="text" placeholder="что-то"/>

       <label for="field2">Чек-бокс</label>
       <input id="field2" type="checkbox"/>

       <label for="field3">Пароль</label>
       <input id="field3" type="password"/>

       <input class="btn btn-success" type="button" value="Просто кнопка" />

       <label for="story">Поле многострочного ввода:</label>
       <textarea id="story" name="story" rows="5" cols="33" placeholder="напишите что-нибудь..."</textarea>

   </form>

        <a class="link-success link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover" href = "index.html">Ссылка на page1</a>
</body>
</html>
