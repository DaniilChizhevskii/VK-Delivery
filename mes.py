import vk
import json
import requests
import datetime
from data.settings import *

session = vk.Session()
api = vk.API(session, v=5.80)

def get ():
	token_number = 0
	token_quantity = tokens.__len__()
	num = int(api.messages.getDialogs(access_token=tokens[0], group_id=group_id)['count'] / 200)
	print (gettime() + ' Users in database: ' + str(num * 200))
	print (gettime() + ' Gathering database...')
	print (gettime() + ' Database progress: 0% (0 of ' + str(num * 200) + ').')
	dialogs = []
	percents = 0
	for i in range(num):
		if (token_number < token_quantity - 1):
			token_number = token_number + 1
		else:
			token_number =  0
		token = tokens[token_number]
		messages = api.messages.getDialogs(access_token=token, group_id=group_id, count=200, offset=i*200)
		for j in range(200):
			user_id = messages['items'][j]['user_id']
			if not (user_id in dialogs):
				dialogs.append(user_id)
			if (int(((i*200)+j + 1)/num/2) - 5 == percents):
				print(gettime() + ' Database progress: ' + str(int(((i*200)+j + 1)/num/2)) + '% (' + str((i*200)+j + 1) + ' of ' + str(num * 200) + ').')
				percents = int(((i*200)+j + 1)/num/2)
	print (gettime() + ' Database had gathered successfully')
	file = open ('./data/dialogs.json', 'w')
	file.write(json.dumps(dialogs))
	file.close()
	return 'ok'
def send ():
	token_number = 0
	token_quantity = tokens.__len__()
	print (gettime() + ' Starting delivery...')
	file = open ('./data/dialogs.json')
	dialogs = json.loads(file.read())
	file.close()
	percents = 0
	num = dialogs.__len__()
	print (gettime() + ' Delivery progress: 0% (0 of ' + str(dialogs.__len__()) + ').')
	for i in range (num):
		if (token_number < token_quantity - 1):
			token_number = token_number + 1
		else:
			token_number =  0
		token = tokens[token_number]
		try:
			i = i
			if (send_name == True):
				name = api.users.get(access_token=token, user_id=dialogs[i])[0]['first_name']
				api.messages.send(access_token=token, user_id=dialogs[i], message=message % name)
			else:
				api.messages.send(access_token=token, user_id=dialogs[i], message=message)
		except vk.exceptions.VkAPIError:
			continue
		if (int(((i + 1)/num) * 100) - 5 == percents):
			print(gettime() + ' Database progress: ' + str(int(((i + 1)/num) * 100)) + '% (' + str(i + 1) + ' of ' + str(num) + ').')
			percents = int(((i + 1)/num)*100)
	print (gettime() + ' Delivery had sent successfully')
	return 'ok'

def gettime ():
	time = datetime.datetime.now()
	now = time.strftime('[%d.%m.%Y %H:%M:%S]')
	return now
get ()
send ()
