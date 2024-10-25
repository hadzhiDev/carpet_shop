# from django.conf import settings
# from django.core.mail import send_mail
# from django.utils.html import strip_tags
# # from django_rest_passwordreset.signals import reset_password_token_created
# from rest_framework.generics import get_object_or_404
#
# from .models import
# from urllib.parse import urlencode
#
#
#
#
# class ResetPasswordManager:
#
#     def __init__(self, user):
#         self.user = user
#         print(type(self.user))
#         self.payload = UserResetPassword.objects.get_or_create(user=self.user)[0]
#         if self.payload.is_expired():
#             self.payload.delete()
#             self.payload = UserResetPassword.objects.get_or_create(user=self.user)[0]
# #
#
# import requests
#
# # Логин для доступа к платформе smspro.nikita.kg.
# login = 'login'
# # Пароль для доступа к платформе smspro.nikita.kg.
# password = 'password'
# # Уникальный идентификатор транзакции. Для каждой отправки он должен быть уникальным.
# # Используя этот ID можно получить отчет о доставке сообщения.
# transactionId = 'U4B4m1za'
# # Имя отправителя - должно быть согласовано с администратором smspro.nikita.kg
# sender = 'SMSPRO.KG'
# # Текст СМС-сообщения - текст на русском или латинице любой длины (до 800 знаков).
# # В случае необходимости платформа smspro.nikita.kg автоматически разделит текст на несколько сообщений.
# text = 'test'
# # Номер телефона получателя СМС в формате 996ххххххххх.
# # В одной транзакции отправки может быть указано и более 1го телефона.
# phone = '996550403993'
#
# xml_data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
# <message>
#     <login>{login}</login>
#     <pwd>{password}</pwd>
#     <id>{transactionId}</id>
#     <sender>{sender}</sender>
#     <text>{text}</text>
#     <phones>
#         <phone>{phone}</phone>
#     </phones>
# </message>"""
#
#
# # Отправка сообщения с указанием времени отправки в формате YYYYMMDDHHMMSS.
# # time = '20240101123000'
# # xml_data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
# # <message>
# #    <login>{login}</login>
# #    <pwd>{password}</pwd>
# #    <id>{transactionId}</id>
# #    <sender>{sender}</sender>
# #    <text>{text}</text>
# #    <time>{time}</time>
# #    <phones>
# #        <phone>{phone}</phone>
# #    </phones>
# # </message>"""
#
#
#
# # Отправка тестового сообщения, сообщение не будет отправлено фактически и не будет тарифицировано.
# # xml_data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
# # <message>
# #    <login>{login}</login>
# #    <pwd>{password}</pwd>
# #    <id>{transactionId}</id>
# #    <sender>{sender}</sender>
# #    <text>{text}</text>
# #    <phones>
# #        <phone>{phone}</phone>
# #    </phones>
# #    <test>1</test>
# # </message>"""
#
#
# url = 'https://smspro.nikita.kg/api/message'
# headers = {'Content-Type': 'application/xml'}
#
# response = requests.post(url, data=xml_data, headers=headers)
# if response.status_code == 200:
#     print('Ответ сервера:', response.text)