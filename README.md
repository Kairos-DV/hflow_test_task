# Декомпозиция
1. Читаем excel файл, сохраняем данные в определенной структуре. Пусть это будет список классов.
Будет базовый класс `BaseCandidate` на тот случай, если мы заходитим расширить функционал, и будет наследник `Candidate` 

    ```
    class BaseCandidate:
        def __init__(self, .... )
            self.position = position.title()
            self.firstname = firstname.title()
            self.lastname = lastname.title()
            self.middlename = '' or middlename.title() # тут может прилететь None
            self.salary = salary  # тут может прилететь None
            self.comment = comment
            self.status = status
            self.fp = ''
    
        @property
        def lastname_firstname():
            return ' '.join([self.lastname, self.firstname])
    ```


2. По ходу написания кода, появится необходимость создания констант,   
эти константы потом вынесем в отдельный файл settings.py

3. Пусть будет структура (пока планирую использовать список) в которой хранятся пути к файлам. 
Для простоты предположим, что если совпадает фамилия и имя.
Для этих целей в предыдущем пункте, в классе используется атрибут `firstname_lastname`,
а для `self.lastname` и `self.firstname` применен метод `title`.
Не будем рассматривать ситуацию, когда есть два кандидата с одинаковыми полями `lastname`, `firstname`.

    *Так как в задании резюме рассортированы по папкам с названиями профессий, то можно,
     для уменьшения вероятности прикладывания в отправку файла однофамильца на будущее заложим привязку профессии 
    к фамаили и имени, этого можно добиться добавив в структуру поле `prof`, туда будем сохранят название папки,
    в которой лежал сам файл. 
    Но этот функционал скорее всего будет реализовываться, если останется время.*

4. Необходимо реализовать функционал добавления(прикрепления) файла к отправке
    * мы храним путь до файла в переменной `fp`
    * как мы отправляем файл? буду использовать `requests`, об этом в отдельно пункте
    * отдельная функция для сравнения(добавления пути файла в атрибут `fp`) по фамилии и имени, что то типа:
        ```for cand in cand_list:
               if cand.lastname_firstname in attachments:
                   cond.fp = attachments['cond.lastname_firstname']
        ```
        `cand_list` - список наших кандидатов, созданных на основе эксель файла   
        `attachments` - список словарей, в котором хранятся пути до файлов, фамилии,
                      в следующем формате:
                       
      ```
        {
            'Иванов Иван': ['filepath','prof'],
            'Петров Петр': ['filepath','prof'],
        }
      ```
      
5. 