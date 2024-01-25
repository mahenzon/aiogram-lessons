# Асинхронный Telegram бот на языке Python 3 с использованием библиотеки aiogram

## Текстовая серия уроков устарела технически, хоть и остаётся актуальной концептуально.
Есть [новая текстовая серия уроков](https://mastergroosha.github.io/aiogram-3-guide/) от автора, вдохновившего меня на создание этой серии уроков (вот так вот мы зациклились).

Также [на канале автора этого текстового курса](https://www.youtube.com/@SurenKhorenyan) есть [серия видеоуроков по aiogram](https://www.youtube.com/playlist?list=PLYnH8mpFQ4am8cFYqn2KsPLb-HrhcYgtC) **по новой версии aiogram 3**.

К сожалению, ресурс, на котором были расположены текстовые курсы, "закончился" и остался в законсервированном виде. Там нельзя ничего обновлять, нет админки, поэтому там не оставить никакую подсказку об изменениях.

___

Для понимания уроков необходимо хотя бы базовое знание языка Python версии 3.

Код из всех уроков доступен на [GitHub](https://github.com/surik00/aiogram-lessons).

> **Важно!** Автор не является профессионалом, в уроках от вас не требуется поступать точно так же. Данный учебник является дружеской рекомендацией, поэтому обо всех ошибках и недочетах можно и **нужно** писать в комментариях или обсуждении. Советы, как поступить было бы лучше, тоже приветствуются.

### Q&A:

**Q:** Почему [aiogram](http://aiogram.readthedocs.io/en/latest/index.html), а не, например, [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)?  
**A:** Автор сам [начинал знакомство с разработкой Телеграм ботов](https://www.gitbook.com/book/groosha/telegram-bot-lessons/details), используя pyTelegramBotAPI, однако поведение библиотеки перестало удовлетворять на больших проектах, у неё странная многопоточность, [FSM](https://en.wikipedia.org/wiki/Finite-state_machine) приходилось создавать самостоятельно \(есть даже [порт FSM из aiogram в pyTelegramBotAPI](https://github.com/Ars2014/FSMTelegramBotAPI)\), плохо реализованное логгирование, aiogram позволяет создавать middleware, например то же [логгирование](https://github.com/aiogram/aiogram/blob/master/aiogram/contrib/middlewares/logging.py), [антифлуд](https://github.com/aiogram/aiogram/blob/master/examples/middleware_and_antiflood.py), ну и просто, [почему нет](https://goo.gl/ngtT8u)?


### **Оглавление:**

* [Урок 1. Быстрый старт. Эхо-бот](https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html)
* [Урок 2. Медиа, разметка, эмоджи и щепотка логирования](http://surik00.gitbooks.io/aiogram-lessons/content/chapter2.html)
* [Урок 3. Машина состояний и то самое логгирование](http://surik00.gitbooks.io/aiogram-lessons/content/chapter3.html)
* [Урок 4. Платежи в Telegram](http://surik00.gitbooks.io/aiogram-lessons/content/chapter4.html)
* [Урок 5. Клавиатуры и кнопки](http://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html)
