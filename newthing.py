from firebase import firebase

firebase = firebase.FirebaseApplication("https://rojroj-c8a0d.firebaseio.com/", None)

def POST(path, data):
	return firebase.put(path, None, data)

def GET(path):
	return firebase.get(path, '')

if __name__ == "__main__":
	POST("haha/", {"putki" : "mara"})
