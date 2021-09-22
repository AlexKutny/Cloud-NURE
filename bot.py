import telebot
from telebot import types
from telegram import ParseMode
from telegram import Update

TOKEN = "2016986832:AAEp3VPmCS8n_NI57hV0cUqGft434oxc1hM"

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['start'])

def menu(message):
 
 
 #--- choice (student && academic) --- 
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    student = types.KeyboardButton('🙎‍♂️ Я студент')
    prepodovatel = types.KeyboardButton('👨‍🏫 Я преподаватель')
    markup.add (student,  prepodovatel )
    bot.send_message(message.chat.id, '👋Приветствую, {0.first_name}, я ваш виртуальный помощник, разработанный кафедрой КИУ, в мои задачи входит помощь студенту в виде предоставления расписания/списка группы, а также всех учебных материалов на учебный семестр.На данный момент я нахожусь в раннем доступе.\nНачнем же наше знакомство!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot1_message(message): 



 #--- Выбор(Студент) ---      
      
      
     #---- Выбор курса ----
       if message.text == '🙎‍♂️ Я студент':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kurse1 = types.KeyboardButton('🔘1 курс')
          back = types.KeyboardButton('⬅️ Вернуться в главное меню')
          markup.add (kurse1, back )
          bot.send_message(message.chat.id, '➡️ Выберите свой курс!'.format(message.from_user), reply_markup = markup)
       
       elif message.text == '⬅️ Вернуться в главное меню':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          student = types.KeyboardButton('🙎‍♂️ Я студент')
          prepodovatel = types.KeyboardButton('👨‍🏫 Я преподаватель')
          markup.add (student,  prepodovatel )
          bot.send_message(message.chat.id, '➡️ Вы вернулись в главное меню!'.format(message.from_user), reply_markup = markup)       
       if message.text == '⬅️ Вернуться к выбору курса':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kurse1 = types.KeyboardButton('🔘1 курс')
          back = types.KeyboardButton('⬅️ Вернуться в главное меню')
          markup.add (kurse1, back )
          bot.send_message(message.chat.id, '➡️ Выберите свой курс!'.format(message.from_user), reply_markup = markup)
      
      #---- Выбор факультета ----
       elif message.text == '🔘1 курс':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kiuki209 = types.KeyboardButton('🔘КИУ')
          back = types.KeyboardButton('⬅️ Вернуться к выбору курса')
          markup.add (kiuki209, back )
          bot.send_message(message.chat.id, '➡️ Выберите свой факультет!'.format(message.from_user), reply_markup = markup)
     
       elif message.text == '⬅️ Вернуться к выбору факультета':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kiuki209 = types.KeyboardButton('🔘КИУ')
          back = types.KeyboardButton('⬅️ Вернуться к выбору курса')
          markup.add (kiuki209, back )
          bot.send_message(message.chat.id, '➡️ Выберите свой факультет!'.format(message.from_user), reply_markup = markup) 
      
      #---- Выбор группы ----
       elif message.text == '🔘КИУ':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kiuki206 = types.KeyboardButton('🔘 КИУКИ 20-6')
          kiuki207 = types.KeyboardButton('🔘 КИУКИ 20-7')
          kiuki208 = types.KeyboardButton('🔘 КИУКИ 20-8')
          kiuki209 = types.KeyboardButton('🔘 КИУКИ 20-9')                              
#          other = types.KeyboardButton('🐵 Другая группа...')
#          freecourse = types.KeyboardButton('💸 Слитые курсы')
          back = types.KeyboardButton('⬅️ Вернуться к выбору факультета')
#          markup.add (kiuki209, other, freecourse, back )
          markup.add (kiuki206, kiuki207, kiuki208, kiuki209, back )
          bot.send_message(message.chat.id, '➡️ Выберите свою группу!'.format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️ Вернуться к выбору группы факультета КИУ':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kiuki206 = types.KeyboardButton('🔘 КИУКИ 20-6')
          kiuki207 = types.KeyboardButton('🔘 КИУКИ 20-7')
          kiuki208 = types.KeyboardButton('🔘 КИУКИ 20-8')
          kiuki209 = types.KeyboardButton('🔘 КИУКИ 20-9')                              
#          other = types.KeyboardButton('🐵 Другая группа...')
#          freecourse = types.KeyboardButton('💸 Слитые курсы')
          back = types.KeyboardButton('⬅️ Вернуться к выбору факультета')
#          markup.add (kiuki209, other, freecourse, back )
          markup.add (kiuki206, kiuki207, kiuki208, kiuki209, back )
          bot.send_message(message.chat.id, '➡️ Выберите свою группу!'.format(message.from_user), reply_markup = markup)
        
      #---- Меню КИУКИ 20-9 ----
       elif message.text == '🔘 КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          rasp209 = types.KeyboardButton('🗓️ Расписание \ КИУКИ 20-9')
          mat209 = types.KeyboardButton('📂 Материалы курса \ КИУКИ 20-9')
          listprepodov = types.KeyboardButton('📊 Личный кабинет \ КИУКИ 20-9')
          back = types.KeyboardButton('⬅️ Вернуться к выбору группы факультета КИУ')
          markup.add (rasp209, mat209, listprepodov, back )
          bot.send_message(message.chat.id, '➡️ Вы в главном меню группы КИУКИ 20-9! \n- Если хотите посмотреть расписание, то \nкнопка "🗓️ Расписание" позволит вам это сделать;\nЕсли хотите скачать материалы по предметам , то \nкнопка "📂 Материалы курса" поможет вам найти желаемые : лекции, конспекты, практические занятия, семинары, лабораторные работы;  \nЕсли вам нужна информация о группе КИУКИ 20-9, то \nкнопка "📊 Личный кабинет", поможет найти: списки группы, номер старосты и профорга, чаты. \n'.format(message.from_user), reply_markup = markup)
    
       elif message.text == '↩️ Вернуться в меню / КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          rasp209 = types.KeyboardButton('🗓️ Расписание \ КИУКИ 20-9')
          mat209 = types.KeyboardButton('📂 Материалы курса \ КИУКИ 20-9')
          listprepodov = types.KeyboardButton('📊 Личный кабинет \ КИУКИ 20-9')
          back = types.KeyboardButton('⬅️ Вернуться к выбору группы факультета КИУ')
          markup.add (rasp209, mat209, listprepodov, back )
          bot.send_message(message.chat.id, '➡️ Вы в главном меню группы КИУКИ 20-9! \n- Если хотите посмотреть расписание, то \nкнопка "🗓️ Расписание" позволит вам это сделать;\nЕсли хотите скачать материалы по предметамна , то\nкнопка "📂 Материалы курса" поможет вам найти желаемые : лекции, конспекты, практические занятия, семинары, лабораторные работы;  \nЕсли вам нужна информация о группе КИУКИ 20-9, то \nкнопка "📊 Личный кабинет", поможет найти: списки группы, номер старосты и профорга, чаты. \n'.format(message.from_user), reply_markup = markup)

      #---- Личный кабинет КИУКИ 20-9 ----      
       elif message.text == '📊 Личный кабинет \ КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          rasp209 = types.KeyboardButton('🧾 Список \ КИУКИ 20-9')
          mat209 = types.KeyboardButton('👥 Контакты \ КИУКИ 20-9')
          chat209 = types.KeyboardButton('💬 Чаты \ КИУКИ 20-9')
          back = types.KeyboardButton('↩️ Вернуться в меню \ КИУКИ 20-9')
          markup.add (rasp209, mat209, chat209, back )
          bot.send_message(message.chat.id, '➡️ В личном кабинете расписано все о группе, но некоторые вкладки не доступны для студентов!'.format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️ Вернуться в личный кабинет \ КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          rasp209 = types.KeyboardButton('🧾 Список \ КИУКИ 20-9')
          mat209 = types.KeyboardButton('👥 Контакты \ КИУКИ 20-9')
          back = types.KeyboardButton('↩️ Вернуться в меню \ КИУКИ 20-9')
          markup.add (rasp209, mat209, back )
          bot.send_message(message.chat.id, '➡️ В личном кабинете расписано все о группе, но некоторые вкладки не доступны для студентов!'.format(message.from_user), reply_markup = markup)

      #--- Контакты КИУКИ 20-9 ---         
       elif message.text == '👥 Контакты \ КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kiuki209 = types.KeyboardButton('👩 Староста \ КИУКИ 20-9')
          other = types.KeyboardButton('👱 Профорг \ КИУКИ 20-9')
          back = types.KeyboardButton('⬅️ Вернуться в личный кабинет \ КИУКИ 20-9')
          markup.add (kiuki209, other, back )
          bot.send_message(message.chat.id, '➡️ Если староста либо профорг не принимают звонок, то в ближайшие время они вам перезвонят!'.format(message.from_user), reply_markup = markup)

       elif message.text == '👱 Профорг \ КИУКИ 20-9':
           markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
           bot.send_message(message.chat.id,
           'Кузнецов Дмитрий\n'+
           '+380 95 888 95 42\n'+
           'Telegram: @Rspt2002\n', reply_markup = markup) 
           markup.add ()
       
       elif message.text == '👩 Староста \ КИУКИ 20-9':
           markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
           bot.send_message(message.chat.id,
           'Контакты старосты:\n'+
           'Гнатченко Елена Васильевна\n'+
           '+380 99 770 82 74\n'+
           'Telegram: @Peskar_lvanovich'
           , reply_markup = markup) 
           markup.add ()

#--- Чаты КИУКИ 20-9 ---
       elif message.text == '💬 Чаты \ КИУКИ 20-9':
           markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
           bot.send_message(message.chat.id,
           '❌ Информация доступно исключительно: ❌\n❌ *Администрации либо Преподователям* ❌', parse_mode=ParseMode.MARKDOWN, reply_markup = markup) 
           markup.add ()
      
      
#--- Список КИУКИ 20-9 ---      
       elif message.text == '🧾 Список \ КИУКИ 20-9':
           markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
           bot.send_message(message.chat.id,
            '1 Варава Роман Васильович	@jkRpower\n'
            '2 Гевондян Карина Гурамівна	@kariina12\n'
            '3 Герасимчук Дмитро Вікторович	@chelikqq\n'
            '4	Гнатченко Єлєна Василівна	@Peskar_lvanovich\n'
            '5	Гончар Дімітрій Андрійович	@dimitriy_gonchar\n'
            '6	Заєць Олександр Сергійович	@ogo_maesh_garnuy_xyi\n'
            '7	Заліцький В`Ячеслав Андрійович	@Alzgaymer\n'
            '8	Замощанський Максим Олексійович	@mAkSiMkaYaXD\n'
            '9	Іваницька Анастасія Максимівна	@copperfields_moon\n'
            '10 Козаков Данило Вадимович	@sseitc\n'
            '11 Кондрацький Гліб Олександрович	@jerleyn\n'
            '12 Король Микола Миколайович	@Nik0lasik\n'
            '13 Кузнєцов Дмитро Олександрович	@Rspt2002\n'
            '14 Лященко Віталій Олександрович	@Joseph8711\n'
            '15 Мальцев Олександр Богданович	@TupaSplach\n'
            '16 Маскальов Євгеній Миколайович	@exhaustedjeka\n'
            '17 Моруга Артем Ігорович	@moruga_artem\n'
            '18 Романенко Павло Олексійович	@pasha_romanenko\n'
            '19 Роскошна Дар`Я Миколаївна	@roskoahnaia\n'
            '20 Роскошний Владислав Русланович	@pplanejane\n'
            '21 Севенко Богдан Дмитрович	@Savahaker\n'
            '22 Тарануха Андрій Миколайович	@Temindiff\n'
            '23 Терещенко Роман Михайлович	@Terromio\n'
            '24 Тесленко Ангеліна Едуардівна	@Angelinatslnk'
           , reply_markup = markup) 
           markup.add ()


#--- Расписание КИУКИ 20-9 ---
       elif message.text == '🗓️ Расписание \ КИУКИ 20-9':
         keyboard = types.InlineKeyboardMarkup()
         url_button = types.InlineKeyboardButton(text="Перейти к расписанию", url="https://cist.nure.ua/ias/app/tt/f?p=778:201:3420173996977685:::201:P201_FIRST_DATE,P201_LAST_DATE,P201_GROUP,P201_POTOK:01.09.2021,31.01.2022,8476396,0:#1021257")
         keyboard.add(url_button)
         bot.send_message(message.chat.id, "➡️ Встроенинное расписанние еще в разработке!\nНо вы можете перейти на сайт и посмотреть расписание пар... ", reply_markup=keyboard)    
       
       
#--- Материалы 20-9 КИУКИ ---       
   
       elif message.text == '📂 Материалы курса \ КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kelek209 = types.KeyboardButton('⚙️ КЕлек \ КИУКИ 20-9')
          obd209 = types.KeyboardButton('🗃️ ОБД \ КИУКИ 20-9')
          fil209 = types.KeyboardButton('💡 Фил \ КИУКИ 20-9')
          klog209 = types.KeyboardButton('🗒️ КЛоГ \ КИУКИ 20-9')
          mztsoi209 = types.KeyboardButton('🛠️МЗЦОИ \ КИУКИ 20-9')
          oopro209 = types.KeyboardButton('🖥️ООПро \ КИУКИ 20-9')
          fv209 = types.KeyboardButton('🏋️‍♂️ФВ ')
          back = types.KeyboardButton('↩️ Вернуться в меню / КИУКИ 20-9')
          markup.add (obd209,kelek209,fil209,mztsoi209,klog209,oopro209,fv209,back )
          bot.send_message(message.chat.id, '➡️ Выберите предмет. \n‼️ В скором времени будут выложены все предметы! ‼️'.format(message.from_user), reply_markup = markup)  

       elif message.text == '⬅️Вернуться к выбору предмета КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          kelek209 = types.KeyboardButton('⚙️ КЕлек \ КИУКИ 20-9')
          obd209 = types.KeyboardButton('🗃️ ОБД \ КИУКИ 20-9')
          fil209 = types.KeyboardButton('💡 Фил \ КИУКИ 20-9')
          klog209 = types.KeyboardButton('🗒️ КЛоГ \ КИУКИ 20-9')
          mztsoi209 = types.KeyboardButton('🛠️МЗЦОИ \ КИУКИ 20-9')
          oopro209 = types.KeyboardButton('🖥️ООПро \ КИУКИ 20-9')
          fv209 = types.KeyboardButton('🏋️‍♂️ФВ \ КИУКИ 20-9')
          back = types.KeyboardButton('↩️ Вернуться в меню / КИУКИ 20-9')
          markup.add (obd209,kelek209,fil209,mztsoi209,klog209,oopro209,fv209,back )
          bot.send_message(message.chat.id, '➡️ Выберите предмет. \n‼️ В скором времени будут выложены все предметы! ‼️'.format(message.from_user), reply_markup = markup)

       elif message.text == '⚙️ КЕлек':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog1209 = types.KeyboardButton('Лекции / КЕлек КИУКИ 20-9')
 #         klog2209 = types.KeyboardButton('Практические занятия')
          klog3209 = types.KeyboardButton('Лабораторные работы / КЕлек КИУКИ 20-9')
          klog4209 = types.KeyboardButton('Литература / КЕлек КИУКИ 20-9')
          back = types.KeyboardButton('⬅️Вернуться к выбору предмета КИУКИ 20-9')
          markup.add (klog1209, klog3209, klog4209, back )
          bot.send_message(message.chat.id, '➡️Вы зашли в меню предмета КЕлек!'.format(message.from_user), reply_markup = markup)




       elif message.text == '⬅️Вернуться в меню предмета КЕлек 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog1209 = types.KeyboardButton('Лекции')
#          klog2209 = types.KeyboardButton('Практические занятия')
          klog3209 = types.KeyboardButton('Лабораторные работы')
          klog4209 = types.KeyboardButton('Литература')
          back = types.KeyboardButton('⬅️Вернуться к выбору предмета КИУКИ 20-9')
          markup.add (klog1209, klog3209, klog4209, back )
          bot.send_message(message.chat.id, 'Вы на 4 странице списка предметов, {0.first_name}!'.format(message.from_user), reply_markup = markup)  
       elif message.text == 'Лекции':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog209lec1 = types.KeyboardButton('🔘Лекция 1')
          klog209lec2 = types.KeyboardButton('🔘Лекция 2')
          klog209lec3 = types.KeyboardButton('🔘Лекция 3')
          klog209lec4 = types.KeyboardButton('🔘Лекция 4')
          klog209lec5 = types.KeyboardButton('🔘Лекция 5')
          klog209lec6 = types.KeyboardButton('🔘Лекция 6')
          klog209lec7 = types.KeyboardButton('🔘Лекция 7')
          klog209lec8 = types.KeyboardButton('🔘Лекция 8')
          klog209lec9 = types.KeyboardButton('🔘Лекция 9')
          klog209lec10 = types.KeyboardButton('🔘Лекция 10')
          klog209lec11 = types.KeyboardButton('🔘Лекция 11')
          klog209lec12 = types.KeyboardButton('🔘Лекция 12')
          klog209lec13 = types.KeyboardButton('🔘Лекция 13')
          klog209lec14 = types.KeyboardButton('🔘Лекция 14')
          klog209lec15 = types.KeyboardButton('🔘Лекция 15')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (klog209lec1, klog209lec2, klog209lec3, klog209lec4, klog209lec5, klog209lec6, klog209lec7, klog209lec8, klog209lec9, klog209lec10, klog209lec11, klog209lec12, klog209lec13, klog209lec14, klog209lec15, back )
          bot.send_message(message.chat.id, 'Лекции выложены на семестр вперед!'.format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️Вернуться к выбору лекций':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog209lec1 = types.KeyboardButton('🔘Лекция 1')
          klog209lec2 = types.KeyboardButton('🔘Лекция 2')
          klog209lec3 = types.KeyboardButton('🔘Лекция 3')
          klog209lec4 = types.KeyboardButton('🔘Лекция 4')
          klog209lec5 = types.KeyboardButton('🔘Лекция 5')
          klog209lec6 = types.KeyboardButton('🔘Лекция 6')
          klog209lec7 = types.KeyboardButton('🔘Лекция 7')
          klog209lec8 = types.KeyboardButton('🔘Лекция 8')
          klog209lec9 = types.KeyboardButton('🔘Лекция 9')
          klog209lec10 = types.KeyboardButton('🔘Лекция 10')
          klog209lec11 = types.KeyboardButton('🔘Лекция 11')
          klog209lec12 = types.KeyboardButton('🔘Лекция 12')
          klog209lec13 = types.KeyboardButton('🔘Лекция 13')
          klog209lec14 = types.KeyboardButton('🔘Лекция 14')
          klog209lec15 = types.KeyboardButton('🔘Лекция 15')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (klog209lec1, klog209lec2, klog209lec3, klog209lec4, klog209lec5, klog209lec6, klog209lec7, klog209lec8, klog209lec9, klog209lec10, klog209lec11, klog209lec12, klog209lec13, klog209lec14, klog209lec15, back )
          bot.send_message(message.chat.id, 'Лекции выложены на семестр вперед!'.format(message.from_user), reply_markup = markup)



# --- Sample on item message ---
       elif message.text == 'Лекия N':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("Lec1.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору предметов')
          markup.add (back )
          bot.send_message(message.chat.id, 'Вы на 2 странице списка предметов, {0.first_name}!'.format(message.from_user), reply_markup = markup)
# --- Лекции по КЕлек  ---
       elif message.text == '🔘Лекция 1':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec1.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 1.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 2':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec2.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 2.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 3':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec3.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 3.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 4':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec4.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 4.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 5':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec5.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 5.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 6':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec6.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 6.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 7':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Leс7.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 7.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 8':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec8.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 8.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec9.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 9.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 10':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec10.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 10.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 11':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec11.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 11.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 12':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec12.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 12.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 13':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec13.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 13.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 14':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec14.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 14.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 15':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lec\Lec15.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 15.'.format(message.from_user), reply_markup = markup)
       
#--- Literatura ---       
       
       elif message.text == 'Литература':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('Shuka A.A. _Elektronika')
          marchenkoosnovielectroniki = types.KeyboardButton('Марченко Основы электроники Учебное пособие для вузов')
          analogovayaicifrivaya = types.KeyboardButton('Аналоговая и цифровая электроника Опадчий Ю.Ф., Глудкин О.П., Гуров А.И. (2000)')
          guseivieelectrinika1991 = types.KeyboardButton('Гусев В.Г., Гусев Ю.М. Электроника (2-е издание, 1991)')
          jerepsovaya = types.KeyboardButton('Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989)')
          shilovlpopularnie = types.KeyboardButton('Шило В.Л. Популярные цифровые микросхемы')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, analogovayaicifrivaya, guseivieelectrinika1991, jerepsovaya , shilovlpopularnie , back )
          bot.send_message(message.chat.id, 'Вы на 4 странице списка предметов, {0.first_name}!'.format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('Shuka A.A. _Elektronika')
          marchenkoosnovielectroniki = types.KeyboardButton('Марченко Основы электроники Учебное пособие для вузов')
          analogovayaicifrivaya = types.KeyboardButton('Аналоговая и цифровая электроника Опадчий Ю.Ф., Глудкин О.П., Гуров А.И. (2000)')
          guseivieelectrinika1991 = types.KeyboardButton('Гусев В.Г., Гусев Ю.М. Электроника (2-е издание, 1991)')
          jerepsovaya = types.KeyboardButton('Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989)')
          shilovlpopularnie = types.KeyboardButton('Шило В.Л. Популярные цифровые микросхемы')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, analogovayaicifrivaya, guseivieelectrinika1991, jerepsovaya , shilovlpopularnie , back )
          bot.send_message(message.chat.id, 'Вы на 4 странице списка предметов, {0.first_name}!'.format(message.from_user), reply_markup = markup)
       

       
       elif message.text == 'Марченко Основы электроники Учебное пособие для вузов':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Марченко Основы электроники Учебное пособие для вузов.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Марченко Основы электроники Учебное пособие для вузов.'.format(message.from_user), reply_markup = markup)



       elif message.text == 'Shuka A.A. _Elektronika':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\ShukaA.A. _Elektronika.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Shuka A.A. _Elektronika.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989).pdf':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989).pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989).pdf'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Гусев В.Г., Гусев Ю.М. Электроника (2-е издание, 1991)':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Гусев В.Г., Гусев Ю.М. Электроника (2-е издание, 1991).pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Гусев В.Г., Гусев Ю.М. Электроника (2-е издание, 1991).'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Марченко Основы электроники Учебное пособие для вузов':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Марченко Основы электроники Учебное пособие для вузов.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Жеребцов И.П. И.П. Жеребцов, Основы электроники (5-е издание, 1989).'.format(message.from_user), reply_markup = markup)



       elif message.text == 'Шило В.Л. Популярные цифровые микросхемы':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Шило В.Л. Популярные цифровые микросхемы.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Шило В.Л. Популярные цифровые микросхемы.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Аналоговая и цифровая электроника Опадчий Ю.Ф., Глудкин О.П., Гуров А.И. (2000)':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\Опадчий Ю.Ф., Глудкин О.П., Гуров А.И. Аналоговая и цифровая электроника (2000).pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Аналоговая и цифровая электроника Опадчий Ю.Ф., Глудкин О.П., Гуров А.И. (2000)'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Лабораторные работы':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('ЛР КЕлек за 2021 год')
          marchenkoosnovielectroniki = types.KeyboardButton('ЛР КЕлек за 2021 год')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, back )
          bot.send_message(message.chat.id, 'Лаборатные работы!'.format(message.from_user), reply_markup = markup)


       elif message.text == '⬅️Вернуться к выбору лабораторных работ КЕлек КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('ЛР КЕлек за 2021 год')
          marchenkoosnovielectroniki = types.KeyboardButton('ЛР КЕлек за 2021 год')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, back )
          bot.send_message(message.chat.id, 'Лаборатные работы!'.format(message.from_user), reply_markup = markup)


       elif message.text == 'ЛР Келек за 2020 год':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lab\ЛабРаботыКЕ2020.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторных работ КЕлек КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Шило В.Л. Популярные цифровые микросхемы.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'ЛР КЕлек за 2021 год':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lab\ЛабРаботыКЕ2021.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'ЛабРаботыКЕ2020.'.format(message.from_user), reply_markup = markup)
#       ОБД
       elif message.text == '🗃️ ОБД':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog1209 = types.KeyboardButton('Лекции ОБД КИУКИ 20-9')
 #         klog2209 = types.KeyboardButton('Практические занятия')
          klog3209 = types.KeyboardButton('Лабораторные работы ОБД КИУКИ 20-9')
          klog4209 = types.KeyboardButton('Литература ОБД КИУКИ 20-9')
          back = types.KeyboardButton('⬅️Вернуться к выбору предмета КИУКИ 20-9')
          markup.add (klog1209, klog3209, klog4209, back )
          bot.send_message(message.chat.id, 'Вы зашли в меню предмета ОБД!'.format(message.from_user), reply_markup = markup)
       elif message.text == '⬅️Вернуться в меню ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          klog1209 = types.KeyboardButton('Лекции ОБД КИУКИ 20-9')
#          klog2209 = types.KeyboardButton('Практические занятия')
          klog3209 = types.KeyboardButton('Лабораторные работы ОБД КИУКИ 20-9')
          klog4209 = types.KeyboardButton('Литература ОБД КИУКИ 20-9')
          back = types.KeyboardButton('⬅️Вернуться к выбору предмета КИУКИ 20-9')
          markup.add (klog1209, klog3209, klog4209, back )
          bot.send_message(message.chat.id, 'Вы зашли в меню предмета ОБД!'.format(message.from_user), reply_markup = markup)  
      # Лекции 
       elif message.text == 'Лекции ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          obd209lec1 = types.KeyboardButton('🔘Лекция 1')
          obd209lec2 = types.KeyboardButton('🔘Лекция 2')
          obd209lec3 = types.KeyboardButton('🔘Лекция 3')
          obd209lec4 = types.KeyboardButton('🔘Лекция 4')
          obd209lec5 = types.KeyboardButton('🔘Лекция 5')
          obd209lec6 = types.KeyboardButton('🔘Лекция 6')
          obd209lec7 = types.KeyboardButton('🔘Лекция 7')
          obd209lec8 = types.KeyboardButton('🔘Лекция 8')
          obd209lec9 = types.KeyboardButton('🔘Лекция 9')
          obd209lec10 = types.KeyboardButton('🔘Лекция 10')
          obd209lec11 = types.KeyboardButton('🔘Лекция 11')
          obd209lec12 = types.KeyboardButton('🔘Лекция 12')
          obd209lec13 = types.KeyboardButton('🔘Лекция 13_INSERT_UPDATE_MySQL')
          obd209lec14 = types.KeyboardButton('🔘Лекция 13 new_Stored_Proc_MySQL')
          obd209lec15 = types.KeyboardButton('🔘Лекция 14_new_Репликации_в_MySQL')
          obd209lec16 = types.KeyboardButton('Лекция 14_Операторы_функции_языка_SQL_в_MySQL')
          obd209lec17 = types.KeyboardButton('🔘Лекция 15_Пользователи_Резервирование_MySQL')
          obd209lec18 = types.KeyboardButton('🔘Лекция 16_NoSQL')
          back = types.KeyboardButton('⬅️Вернуться в меню ОБД КИУКИ 20-9')
          markup.add (obd209lec1, obd209lec2, obd209lec3, obd209lec4, obd209lec5, obd209lec6, obd209lec7, obd209lec8, obd209lec9, obd209lec10, obd209lec11, obd209lec12, obd209lec13, obd209lec14, obd209lec15, obd209lec16, obd209lec17, obd209lec18, back )
          bot.send_message(message.chat.id, 'Лекции выложены на семестр вперед!'.format(message.from_user), reply_markup = markup)
       elif message.text == '⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          obd209lec1 = types.KeyboardButton('🔘Лекция 1')
          obd209lec2 = types.KeyboardButton('🔘Лекция 2')
          obd209lec3 = types.KeyboardButton('🔘Лекция 3')
          obd209lec4 = types.KeyboardButton('🔘Лекция 4')
          obd209lec5 = types.KeyboardButton('🔘Лекция 5')
          obd209lec6 = types.KeyboardButton('🔘Лекция 6')
          obd209lec7 = types.KeyboardButton('🔘Лекция 7')
          obd209lec8 = types.KeyboardButton('🔘Лекция 8')
          obd209lec9 = types.KeyboardButton('🔘Лекция 9')
          obd209lec10 = types.KeyboardButton('🔘Лекция 10')
          obd209lec11 = types.KeyboardButton('🔘Лекция 11')
          obd209lec12 = types.KeyboardButton('🔘Лекция 12')
          obd209lec13 = types.KeyboardButton('🔘Лекция 13_INSERT_UPDATE_MySQL')
          obd209lec14 = types.KeyboardButton('🔘Лекция 13 new_Stored_Proc_MySQL')
          obd209lec15 = types.KeyboardButton('🔘Лекция 14_new_Репликации_в_MySQL')
          obd209lec16 = types.KeyboardButton('Лекция 14_Операторы_функции_языка_SQL_в_MySQL')
          obd209lec17 = types.KeyboardButton('🔘Лекция 15_Пользователи_Резервирование_MySQL')
          obd209lec18 = types.KeyboardButton('🔘Лекция 16_NoSQL')
          back = types.KeyboardButton('⬅️Вернуться в меню ОБД КИУКИ 20-9')
          markup.add (obd209lec1, obd209lec2, obd209lec3, obd209lec4, obd209lec5, obd209lec6, obd209lec7, obd209lec8, obd209lec9, obd209lec10, obd209lec11, obd209lec12, obd209lec13, obd209lec14, obd209lec15, obd209lec16, obd209lec17, obd209lec18, back )
          bot.send_message(message.chat.id, 'Лекции выложены на семестр вперед!'.format(message.from_user), reply_markup = markup)
# --- Sample on item message ---
       elif message.text == 'Лекия N':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("Lec1.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору предметов')
          markup.add (back )
          bot.send_message(message.chat.id, 'Вы на 2 странице списка предметов, {0.first_name}!'.format(message.from_user), reply_markup = markup)
# --- Лекции по КЕлек  ---
       elif message.text == '🔘Лекция 1':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec1.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 1.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 2':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec2.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 2.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 3':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec3.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 3.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 4':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec4.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 4.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 5':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec5.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 5.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 6':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec6.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 6.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 7':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Leс7.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 7.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 8':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec8.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 8.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec9.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 9.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 10':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec10.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 10.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 11':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec11.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 11.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 12':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec12_MySQL.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 12.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 13_INSERT_UPDATE_MySQL':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec13_INSERT_UPDATE_MySQL.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 13_INSERT_UPDATE_MySQL'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 13 new_Stored_Proc_MySQL':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec13_new_Stored_Proc_MySQL [Автосохраненный].pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 13 new_Stored_Proc_MySQL.'.format(message.from_user), reply_markup = markup)

       elif message.text == '🔘Лекция 14_new_Репликации_в_MySQL':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec14_new_Репликации_в_MySQL .pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 14_new_Репликации_в_MySQL.'.format(message.from_user), reply_markup = markup)
       
       elif message.text == '🔘Лекция 14_Операторы_функции_языка_SQL_в_MySQL':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec14_new_Репликации_в_MySQL .pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 14_Операторы_функции_языка_SQL_в_MySQL.'.format(message.from_user), reply_markup = markup)
       elif message.text == '🔘Лекция 15_Пользователи_Резервирование_MySQL':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec15_Пользователи_Резервирование_MySQL.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция 15_Пользователи_Резервирование_MySQL.'.format(message.from_user), reply_markup = markup)
       
       elif message.text == '🔘Лекция 16_NoSQL':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\Lec16_2017_NoSQL.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лекций ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Лекция Lec16_2017_NoSQL.'.format(message.from_user), reply_markup = markup)
       
       
       
       #Template file load in TelgramAPI
       elif message.text == '':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lec\.pdf", 'rb')
          bot.send_document(chat_id, d)
          
#--- Lab ---       
       
       elif message.text == 'Лабораторные работы ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          mtdobd2017 = types.KeyboardButton('Метода_ОБД_2021')
          vopr1labkiuki209 = types.KeyboardButton('Вопросы к 1 лб ОБД КИУКИ 20-9')
          vopr2labkiuki209 = types.KeyboardButton('Вопросы к 2 лб ОБД КИУКИ 20-9')
          vopr3labkiuki209 = types.KeyboardButton('Вопросы к 3 лб ОБД КИУКИ 20-9')
          vopr4labkiuki209 = types.KeyboardButton('Вопросы к 4 лб ОБД КИУКИ 20-9')
          back = types.KeyboardButton('⬅️Вернуться в меню ОБД КИУКИ 20-9')
          markup.add (mtdobd2017, vopr1labkiuki209, vopr2labkiuki209, vopr3labkiuki209, vopr4labkiuki209, back )
          bot.send_message(message.chat.id, 'В этой вкладке вы найдете: \n-вопросы к лабораторным работам \n-методичку со всеми лабораторными работами.'.format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          mtdobd2017 = types.KeyboardButton('Метода_ОБД_2021')
          vopr1labkiuki209 = types.KeyboardButton('Вопросы к 1 лб ОБД КИУКИ 20-9')
          vopr2labkiuki209 = types.KeyboardButton('Вопросы к 2 лб ОБД КИУКИ 20-9')
          vopr3labkiuki209 = types.KeyboardButton('Вопросы к 3 лб ОБД КИУКИ 20-9')
          vopr4labkiuki209 = types.KeyboardButton('Вопросы к 4 лб ОБД КИУКИ 20-9')
          back = types.KeyboardButton('⬅️Вернуться в меню ОБД КИУКИ 20-9')
          markup.add (mtdobd2017, vopr1labkiuki209, vopr2labkiuki209, vopr3labkiuki209, vopr4labkiuki209, back )
          bot.send_message(message.chat.id, 'В этой вкладке вы найдете: \n-вопросы к лабораторным работам \n-методичку со всеми лабораторными работами.'.format(message.from_user), reply_markup = markup)
       
       elif message.text == 'Вопросы к 1 лб ОБД КИУКИ 20-9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lab\обд_1защита.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Этот документ предназначен для подготовки к первой защите лабораторных работ по ОБД.'.format(message.from_user), reply_markup = markup)



       elif message.text == 'Вопросы к 2 лб ОБД КИУКИ 20-9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lab\обд_2защита.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Этот документ предназначен для подготовки ко воторой защите лабораторных работ по ОБД.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Вопросы к 3 лб ОБД КИУКИ 20-9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lab\обд_3защита.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Этот документ предназначен для подготовки к третий защите лабораторных работ по ОБД.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Вопросы к 4 лб ОБД КИУКИ 20-9':
          chat_id = message.chat.id   
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\lit\obd\lab\обд_4защита.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Этот документ предназначен для подготовки к четвертой защите лабораторных работ по ОБД.'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Метода_ОБД_2021':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lab\Метода_ОБД_2017.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору лабораторной работы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Это актульная методичка с помощью которой вы сможете выполнить лабораторные работы'.format(message.from_user), reply_markup = markup)



       elif message.text == 'Собеседование защита за 2021 год ОБД КИУКИ 20-9':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\Собеседование\Собеседование ОБД_ответы.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться в меню предмета ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Собеседование ОБД КИУКИ 20-9'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Литература':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('SQL Крис Фиайли')
          marchenkoosnovielectroniki = types.KeyboardButton('Базы данных - Проектирование, реализация и сопровождение - Теория и практика (Томас Коннолли и Ка)')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек КИУКИ 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, back )
          bot.send_message(message.chat.id, 'Литература которую рекомендовала Лидия Анатольевна Тихонова' .format(message.from_user), reply_markup = markup)

       elif message.text == '⬅️Вернуться к выбору литературы ОБД КИУКИ 20-9':
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          shukaaa_electronica = types.KeyboardButton('SQL Крис Фиайли')
          marchenkoosnovielectroniki = types.KeyboardButton('Базы данных - Проектирование, реализация и сопровождение - Теория и практика (Томас Коннолли и Ка)')
          back = types.KeyboardButton('⬅️Вернуться в меню предмета КЕлек 20-9')
          markup.add (shukaaa_electronica, marchenkoosnovielectroniki, back )
          bot.send_message(message.chat.id, 'Лаборатные работы!'.format(message.from_user), reply_markup = markup)


       elif message.text == 'Базы данных - Проектирование, реализация и сопровождение - Теория и практика (Томас Коннолли и Ка)':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lit\Базы данных - Проектирование, реализация и сопровождение - Теория и практика (Томас Коннолли и Ка.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы ОБД КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'Шило В.Л. Популярные цифровые микросхемы.'.format(message.from_user), reply_markup = markup)



       elif message.text == 'SQL Крис Фиайли':
          chat_id = message.chat.id
          markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
          d = open("material\kiuki20-9\obd\lit\SQL Крис Фиайли.pdf", 'rb')
          bot.send_document(chat_id, d)
          back = types.KeyboardButton('⬅️Вернуться к выбору литературы КЛог КИУКИ 20-9')
          markup.add (back )
          bot.send_message(message.chat.id, 'ЛабРаботыКЕ2020.'.format(message.from_user), reply_markup = markup)


bot.polling(none_stop = True)