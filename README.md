# Асинхронный Telegram бот на языке Python 3 с использованием библиотеки aiogram

Для понимания уроков необходимо хотя бы базовое знание языка Python версии 3.

### Q&A:

**Q:** Почему [aioram](http://aiogram.readthedocs.io/en/latest/index.html), а не, например, [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)?  
**A:** Автор сам [начинал знакомство с разработкой Телеграм ботов](https://www.gitbook.com/book/groosha/telegram-bot-lessons/details), используя pyTelegramBotAPI, однако поведение библиотеки перестало удовлетворять на больших проектах, у неё странная многопоточность, [FSM](https://en.wikipedia.org/wiki/Finite-state_machine) приходилось создавать самостоятельно \(есть даже [порт FSM из aiogram в pyTelegramBotAPI](https://github.com/Ars2014/FSMTelegramBotAPI)\), плохо реализованное логгирование, aiogram позволяет создавать middleware, например [антифлуд](https://github.com/aiogram/aiogram/blob/master/examples/middleware_and_antiflood.py), ну и просто, [почему нет](https://goo.gl/ngtT8u)?

### **Оглавление:**

* [Урок 1. Быстрый старт. Эхо-бот](https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html)



