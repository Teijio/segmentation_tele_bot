Описание: телеграм бот, который на вход принимает картинку, а на выходе возвращает указанные объект в виде картинки, без заднего фона.

Подготовка к запуску:
- в корне проекта создать файл .env и указать в нем свой TOKEN бота
- сбилдить образ docker build -t "название образа" .
- привязать .env к контейнеру и запустить docker run -it -v /path/to/your/project/.env:/app/.env "название-конейтера"

Пример использования:
Передаем картинку ![image](https://github.com/Teijio/segmentation_tele_bot/assets/114352761/7aa516d5-38af-4880-920d-cb0928685ceb)
Выбираем найденный объект ![image](https://github.com/Teijio/segmentation_tele_bot/assets/114352761/eea4d06c-f4c3-4d0a-adf8-39d933a30363)
Получаем ![image](https://github.com/Teijio/segmentation_tele_bot/assets/114352761/bb570edf-5d6b-48c0-a243-fe879154d587)


