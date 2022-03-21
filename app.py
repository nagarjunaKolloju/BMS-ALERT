import requests
from time import sleep
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# SENDGRID_KEY = 'YORU-API-KEY-HERE'


def send_mail():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox11f72a48f8bb44ec81834fc71cbabf61.mailgun.org/messages",
		auth=("api", "110b22b11f4bb2e40e60f90ced220f1f-0677517f-15ef2a9e"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox11f72a48f8bb44ec81834fc71cbabf61.mailgun.org>",
			"to": "Nagarjuna <ninjaforyou69@gmail.com>",
			"subject": "ALERT",
			"text": "BOOKINGS ARE OPEN"})


while(True):
    res = requests.get(
        'https://in.bookmyshow.com/buytickets/radhe-shyam-tirupati/movie-tiru-ET00135230-MT/20220322')
    if(res.text.find('PGR Cinemas') != -1):
        print("BOOKINGS ARE NOW OPEN!")
        send_mail()
    elif(res.text.find('NVR Sandhya') != -1):
        print("BOOKINGS ARE NOW OPEN!")
        send_mail()
    elif(res.text.find('Padma Picture') != -1):
        print("BOOKINGS ARE NOW OPEN!")
        send_mail()
    elif(res.text.find('Pratap Theater') != -1):
        print("BOOKINGS ARE NOW OPEN!")
        send_mail()
    else:
        print("Bookings not open yet")
    sleep(60)