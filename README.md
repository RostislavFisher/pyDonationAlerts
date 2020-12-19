# pyDonationAlerts
Переделка donationalerts_api в самостоятельную версию без flask


Последовательность действий для использования:

1. Создание приложения по ссылке [Тык](https://www.donationalerts.com/application/clients)


2. После создания появится окно с существующими приложениями. Нужно скопировать полученные данные

3. Полученные данные будут использованыы для инницализации объекта:
    donationAPI = DonationAlertsAPI(client_id, client_secret, redirect_uri, scope(необязательно))
    
4. Получите ссылку на подключение бота к своему DonationAlerts - аккаунту:
    donationAPI.login()
    
    И в браузере (по полученной ссылке) подтвердите свои действия
5. DonationAlerts пошлет редирект на выбранный сайт. Можно заморочиться или просто достать из поисковой строки параметр "code".

6. Параметр код нужно использовать для получения токена.:
    token = donationAPI.getAccessToken("ПОЛУЧЕННЫЙ CODE")
7. С полученным токеном можно уже играться:
    donationAPI.getDonation(token)

8. Полученный json-файл можно анализировать.
