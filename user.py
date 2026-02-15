
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile

r = Router()

menu = [
    'IT Live haqida',
    "Kurslar",
    "Mentor",
    "Biz bilan bog`lanish",
    'Lokatsiya'
]
Menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=m)] for m in menu
    ], resize_keyboard=True
)


@r.message(F.text.in_(menu))
async def Menu_message(message: Message):
    T = message.text
    rasm = FSInputFile('./img/itlive.jpg')
    if menu[0] == T:
        await  message.answer_photo(photo=rasm,caption="""<b>IT Live Academy </b>– <i>bu IT Park rezidenti sifatida ro‘yhatdan o‘tgan ta’lim markazi, u 2022-yilda tashkil qilingan. Markaz axborot texnologiyalari bo‘yicha kurslar va xizmatlar ko‘rsatadi.
</i>
<b>🎓 Asosiy yo‘nalishlar</b>

<u>Markazda quyidagi yo‘nalishlar bo‘yicha o‘quv kurslari mavjud:</u>

🧑‍💻 Dasturlash va Web Development

Frontend: React.js, JavaScript, HTML, CSS, Bootstrap, Git, Github, Netlify

Backend: Node.js, PHP (Laravel), PostgreSQL yoki MySQL

Foundation: C++, Python, Java asoslari, objektga yo‘naltirilgan dasturlash (OOP), Data Structure

Mobile App Development: Java, Kotlin, UI/UX, Git, GitHub, JetPack Compose

🖥 Qo‘shimcha yo‘nalishlar

Kompyuter savodxonligi: MS Office (Word, Excel, PowerPoint), Windows operatsion tizimi

Buxgalteriya: 1C va soliq hisobotlari bilan ishlash kursi

Dizayn: Web dizayn va UI/UX elementlari


""")
    elif menu[1] == T:
        await  message.answer('Menu tanlang🔽',reply_markup=Kurs)
    elif menu[2] == T:
        await  message.answer("""    ('Foundation dasturlash — bu dasturchi bo‘lish uchun kerak bo‘ladigan eng asosiy bilim va ko‘nikmalar to‘plami. Ya’ni, har qanday yo‘nalishga (mobil, web, sun’iy intellekt, backend va boshqalar) kirishdan oldin o‘rganiladigan poydevor bilimlar.📚 Foundation dasturlashda nimalar o‘rganiladi?1️⃣ Algoritm va mantiqiy fikrlash1️⃣ Algoritm va mantiqiy fikrlashBlok-sxema tuzishOddiy va murakkab algoritmlar2️⃣ Dasturlash asoslari🐍 PythonJava💻 💻 C++')
""")
    elif menu[3] == T:
        await  message.answer("@Alibek032009")
    elif menu[4] == T:
        # 40.502748, 68.764835
        await message.answer("Joylashuv shu yerda lokatsiyasi")
        await  message.answer_location(latitude=40.502748,longitude= 68.764835)

kurs=[
"Mobil dasturtash",
"Foundation Dasturlash", #1
"Frontend Dasturlash", #2
"Backend Dasturlash",
"Full Stack Dasturiash",
"Kibir hafsizlik",
#6
"Robotexnikal",
"SMM", #9
"DevOps", #10
"Ardunio",
"🔙 Orqaga"
]
Kurs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=m)] for m in kurs
    ], resize_keyboard=True
)
@r.message(F.text.in_(kurs[10]))
async def Orqaga(msg: Message):
    await msg.answer('Menu tanlang🔽',reply_markup=Menu)


@r.message(F.text.in_(kurs))
async def Kurs_message(msg: Message):
    T=msg.text
    if T==kurs[0]: await msg.answer('Mobil dasturchi — bu smartfon va planshetlar uchun ilovalar yaratadigan mutaxassis. Ular asosan Android va iOS platformalari uchun dasturlar ishlab chiqadi.📌 Mobil dasturchining asosiy vazifalari📲 Mobil ilovalarni yaratish va dizayn qilish🧠 Ilova funksiyalarini dasturlash🔄 Ilovani test qilish va xatolarni tuzatish🚀 Ilovani Google Play yoki App Store ga joylash🔧 Ilovani yangilab borish')
    if T==kurs[1]: await msg.answer('Foundation dasturlash — bu dasturchi bo‘lish uchun kerak bo‘ladigan eng asosiy bilim va ko‘nikmalar to‘plami. Ya’ni, har qanday yo‘nalishga (mobil, web, sun’iy intellekt, backend va boshqalar) kirishdan oldin o‘rganiladigan poydevor bilimlar.📚 Foundation dasturlashda nimalar o‘rganiladi?1️⃣ Algoritm va mantiqiy fikrlash1️⃣ Algoritm va mantiqiy fikrlashBlok-sxema tuzishOddiy va murakkab algoritmlar2️⃣ Dasturlash asoslari🐍 PythonJava💻 💻 C++')
    if T==kurs[2]: await msg.answer("""Frontend dasturlash — bu veb-sayt yoki veb-ilovaning foydalanuvchi ko‘radigan va ishlatadigan qismini yaratish jarayoni. Ya’ni dizayn, tugmalar, menyular, animatsiyalar va interaktiv elementlar frontend orqali amalga oshiriladi.Oddiy qilib aytganda:
👉 Frontend = saytning tashqi ko‘rinishi va foydalanuvchi bilan ishlashi.1️⃣ HTML (HyperText Markup Language)Saytning tuzilmasi (skeleti)Matn, rasm, tugma, jadval va boshqa elementlarni joylashtiradi2️⃣ CSS (Cascading Style Sheets)Saytning dizayni va bezagiRang, shrift, o‘lcham, joylashuv va animatsiyalarni boshqaradi3️⃣ JavaScriptSaytga jon kiritadiTugmalar bosilganda amal bajarish, forma tekshirish, sliderlar, modal oynalar va boshqalar""")
    if T==kurs[3]: await msg.answer("""Backend dasturlash — bu veb-sayt yoki ilovaning server tomoni, ya’ni foydalanuvchi ko‘rmaydigan, lekin hamma jarayonlarni boshqaradigan qismi.👉 Frontend — tashqi ko‘rinish, Backend — ichki mantiq va ma’lumotlar bilan ishlash.Backend nima ish qiladi?🔐 Foydalanuvchini ro‘yxatdan o‘tkazish va login qilish.💾 Ma’lumotlarni bazaga saqlash.🔄 Frontend bilan API orqali ma’lumot almashish.🛡️ Xavfsizlikni ta’minlash.⚙️ Serverni boshqarish.1️⃣ ServerSayt ishlaydigan kompyuter (masalan: VPS yoki cloud server).2️⃣ Ma’lumotlar bazasi (Database).Ma’lumotlar saqlanadigan joy (masalan: MySQL, PostgreSQL, MongoDB).3️⃣ APIFrontend va backend o‘rtasidagi aloqa tizimi.""")
    if T==kurs[4]: await msg.answer("""Full Stack dasturlash nima?Full Stack dasturchi — bu frontend + backend qismlarini ham qila oladigan mutaxassis.
Ya’ni u saytning ko‘rinishini ham, server qismini ham yozadi.👉 Oddiy qilib: Full Stack = butun loyihani boshidan oxirigacha qilish.1️⃣ Frontend.HTML

CSS

.JavaScr.ipt.Frameworklar (React, Vue, Angular)2️⃣ Backend.Server tili (Node.js, Python, PHP, Java).API yaratish.Authentication.Xavfsizlik.3️⃣ Database.MySQL.PostgreSQL.MongoDB""")
    if T==kurs[5]: await msg.answer("""👉 Oddiy qilib: ma’lumotlarni va tizimlarni himoya qilish ilmi.🔐 Shaxsiy ma’lumotlar (parol, karta raqami)🖥️ Server va veb-saytlar.📡 Tarmoqlar (Wi-Fi, korporativ network).💾 Ma’lumotlar bazasi.🔑 Authentication (Autentifikatsiya) nima?Authentication — bu foydalanuvchining kimligini tekshirish jarayoni.“Sen haqiqatan ham shu akkaunt egasimisan?”1️⃣ Parol orqali (Something you know).Login + parol.Eng oddiy usul.2️⃣ Biometrik (Something you are).Barmoq izi.Yuzni aniqlash (Face ID).3️⃣ SMS yoki OTP kod (Something you have).Telefon raqamga kod keladi.2 bosqichli tekshiruv (2FA).""")
    if T==kurs[6]: await msg.answer("""Robototexnika — bu robotlarni loyihalash, yaratish va dasturlash bilan shug‘ullanadigan soha. U mexanika, elektronika va dasturlashni birlashtiradi.👉 Oddiy qilib: Robototexnika = mexanika + elektronika + dasturlash.Robot — bu oldindan berilgan dastur asosida yoki sun’iy intellekt yordamida harakat qiladigan avtomatik qurilma.🏭 Zavoddagi robot qo‘l.🤖 Odamga o‘xshash humanoid robot.🏨 Mehmonxonadagi xizmat robotlari.🎓 O‘quv robot to‘plamlari.🏥 Tibbiyot (jarrohlik robotlari).📦 Ombor va logistika.🚜 Qishloq xo‘jaligi.🛡️ Harbiy soha.🏠 Maishiy robotlar (robot changyutgich)""")
    if T==kurs[7]: await msg.answer("""SMM — Social Media Marketing degani.Bu ijtimoiy tarmoqlar orqali biznesni reklama qilish va rivojlantirish sohasi.👉 Oddiy qilib: SMM = Instagram, Facebook, TikTok orqali savdo va reklama qilish.SMM mutaxassisi nima qiladi?.✔️ Post va storislar tayyorlaydi
✔️ Kontent reja tuzadi.✔️ Target reklama sozlaydi.✔️ Savdoni ko‘paytirishga yordam beradi
✔️ Analitika qiladi (statistika tahlili).SMM tarkibiy qismlari.1️⃣ Kontent (Content).Rasmlar.Videolar.Reels.Matnlar.2️⃣ Target reklama.Pullik reklama orqali kerakli auditoriyaga chiqish.3️⃣ Analitika.Ko‘rishlar, layklar, saqlashlar, sotuv natijalari.SMM o‘rganish bosqichlari.Ijtimoiy tarmoqlar algoritmini tushunish.Kontent yaratishni o‘rganish.Dizayn (Canva, Photoshop).
Real loyihada ishlash.

""")
    if T==kurs[8]: await msg.answer("""DevOps haqida ma’lumot.DevOps — bu dasturchilar (Development) va tizim administratorlari (Operations) ishini birlashtiradigan yo‘nalish.👉 Oddiy qilib: DevOps — kod yozishdan tortib, uni serverga joylash va ishlatishgacha bo‘lgan jarayonni avtomatlashtirish.🚀 Loyihani tezroq chiqarish.🔄 Avtomatik test va deploy qilish.⚡ Server ishlashini nazorat qilish.🛡️ Barqaror va xavfsiz tizim yaratish.DevOps jarayoni (Lifecycle).1️⃣ Code yozish
.2️⃣ Test qilish.3️⃣ Build qilish.4️⃣ Deploy (serverga joylash).5️⃣ Monitoring.


""")
    if T==kurs[9]: await msg.answer("""Arduino — bu ochiq manbali (open-source) elektron platforma bo‘lib, robototexnika va turli avtomatlashtirish loyihalarini yaratishda ishlatiladi.👉 Oddiy qilib: Arduino — sensor va motorlarni boshqaradigan kichik “aqlli plata”.Asosiy xususiyatlari:ATmega328P mikrokontroller.14 ta raqamli pin (6 tasi PWM).6 ta analog pin.USB orqali kompyuterga ulanadi.5V bilan ishlaydi.Arduino nima ish qiladi?.Arduino orqali siz:✅ LED yoqib-o‘chirish
.✅ Sensorlardan ma’lumot olish
✅ Motor va servo boshqarish.✅ Motor va servo boshqarish.✅ Aqlli uy tizimi qilish
✅ Robot yasash.Arduino qanday dasturlanadi?.Arduino asosan C/C++ ga o‘xshash tilda yoziladi.
Rasmiy dasturi: Arduino IDE.Kod yoziladi → USB orqali plataga yuklanadi → Qurilma mustaqil ishlaydi.

""")

@r.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


def user(dp):
    dp.include_router(r)

