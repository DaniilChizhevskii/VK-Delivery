import vk
import json
import datetime

session = vk.Session()
api = vk.API(session, v=5.80)

def get (**kwargs):
	if ('tokens' not in kwargs.keys() or 'group_id' not in kwargs.keys()):
		raise KeyError ('One of the arguments is missing or invalid.')
	if ('ui' not in kwargs.keys()):
		ui = False
	else:
		ui = kwargs['ui']
	tokens = kwargs['tokens']
	group_id = kwargs['group_id']
	try:
		token_number = 0
		token_quantity = tokens.__len__()
		number = api.messages.getDialogs(access_token=tokens[0], group_id=group_id)['count']
		num = int(number / 200)
		if (ui):
			print (gettime() + ' Users in database: ' + str(number))
			print (gettime() + ' Gathering database...')
			print (gettime() + ' Database gathering progress: 0% (0 of ' + str(number) + ').')
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
				if (ui):
					if (int((((i*200) + j + 1)) / number * 100) - 5 == percents):
						print(gettime() + ' Database gathering progress: ' + str(int((((i*200) + j + 1)) / number * 100)) + '% (' + str((i*200)+j + 1) + ' of ' + str(number) + ').')
						percents = int(((i*200)+j + 1)/number*100)
		if (token_number < token_quantity - 1):
			token_number = token_number + 1
		else:
			token_number =  0
		token = tokens[token_number]
		messages = api.messages.getDialogs(access_token=token, group_id=group_id, count=number % 200, offset=num*200)
		for i in range(number % 200):
			user_id = messages['items'][i]['user_id']
			if not (user_id in dialogs):
				dialogs.append(user_id)
			if (ui):
				if (int((i + 1)/number) - 5 == percents):
					print(gettime() + ' Database progress: ' + str(int((i + 1)/number)) + '% (' + str(i + 1) + ' of ' + str(number) + ').')
					percents = int((i + 1)/number)
		if (ui):
			print (gettime() + ' Database had gathered successfully')
		return dialogs
	except vk.exceptions.VkAPIError as error:
		raise error
	except Exceptions:
		raise SystemError('One of the arguments is invalid.')

def send (**kwargs):
	if ('tokens' not in kwargs.keys() or 'group_id' not in kwargs.keys() or 'dialogs' not in kwargs.keys() or 'message' not in kwargs.keys()):
		raise KeyError ('One of the arguments is missing or invalid.')
	if ('ui' not in kwargs.keys()):
		ui = False
	else:
		ui = kwargs['ui']
	tokens = kwargs['tokens']
	group_id = kwargs['group_id']
	dialogs = kwargs['dialogs']
	message = kwargs['message']
	try:
		token_number = 0
		token_quantity = tokens.__len__()
		percents = 0
		num = dialogs.__len__()
		if (ui):
			print (gettime() + ' Starting delivery...')
			print (gettime() + ' Delivery progress: 0% (0 of ' + str(dialogs.__len__()) + ').')
		for i in range (num):
			if (token_number < token_quantity - 1):
				token_number = token_number + 1
			else:
				token_number =  0
			token = tokens[token_number]
			try:
				i = i
				api.messages.send(access_token=token, user_id=dialogs[i], message=message)
			except vk.exceptions.VkAPIError:
				continue
			if (ui):
				if (int(((i + 1)/num) * 100) - 5 == percents):
					print(gettime() + ' Database progress: ' + str(int(((i + 1)/num) * 100)) + '% (' + str(i + 1) + ' of ' + str(num) + ').')
					percents = int(((i + 1)/num)*100)
		if (ui):
			print (gettime() + ' Delivery had sent successfully')
		return True
	except vk.exceptions.VkAPIError as error:
		raise error
	except Exceptions:
		raise SystemError('One of the arguments is invalid.')

def getandsend (**kwargs):
	if ('tokens' not in kwargs.keys() or 'group_id' not in kwargs.keys() or 'message' not in kwargs.keys()):
		raise KeyError ('One of the arguments is missing or invalid.')
	if ('ui' not in kwargs.keys()):
		ui = False
	else:
		ui = kwargs['ui']
	dialogs = get(tokens = kwargs['tokens'],  group_id = kwargs['group_id'], ui = ui)
	return send (tokens = kwargs['tokens'],  group_id = kwargs['group_id'], dialogs = dialogs, message = kwargs['message'], ui = ui)
	

def gettime ():
	time = datetime.datetime.now()
	now = time.strftime('[%d.%m.%Y %H:%M:%S]')
	return now
