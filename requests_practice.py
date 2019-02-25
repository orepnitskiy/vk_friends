import requests
import json
import re


def calc_age(uid):
    """ Главная функция, которая отвечает за запросы к API VK """
	access_token = "81aa0e9281aa0e9281aa0e925881c265f3881aa81aa0e92ddfe98f711816a9f281028ce"	
	get_id = requests.get('https://api.vk.com/method/users.get', params={ 
	'v':5.71,
	'access_token':access_token,
	'user_ids':uid
	})
	id = json.loads(get_id.text)["response"][0]["id"]
	get_friends = requests.get('https://api.vk.com/method/friends.get', params={
	 'v':5.71,
	 'access_token':access_token,
	 'user_id':id,
	 'fields':'bdate'
	 })
	friends_list = json.loads(get_friends.text)['response']['items']
	return friends_sort(friends_list)
	
	
def friends_sort(friends_list:list):
    """ Функция, которая выдает друзей в нужном формате """
	friends_dict = dict()
	for x in friends_list:
		try:
			bday = int(x['bdate'].split('.')[2])
			try:
				friends_dict[str(2019-bday)] += 1
			except KeyError:
				friends_dict[str(2019-bday)]=1
		except KeyError:
			pass
		except IndexError:
			pass
	age_list = []
	for x in friends_dict.keys():
		age_list.append((int(x), friends_dict[x]))
	return sorted(age_list, key=lambda x: (-x[1], x[0]))



