import webapp2
import httplib
import json

def listCommands():
	commands = list(COMMAND_FUNCTIONS.keys())
	s = "Commands are: "
	for i in range(len(commands)):
		s += (commands[i] + (", " * (i == len(commands)-1)))
	return s

def handleCommand(command):
	if command in COMMAND_FUNCTIONS:
		for i in COMMAND_FUNCTIONS:
			if type(COMMAND_FUNCTIONS[i]) == str:
				return COMMAND_FUNCTIONS[i]
			else:
				return COMMAND_FUNCTIONS[i]()
		return ""
		
COMMAND_FUNCTIONS = {"Kappa":"http://i.imgur.com/6CbxaPc.jpg",
                     "commands":listCommands,
					 "samjay":"Sam Jay is a successful F1 driver and an all time favorite student of Mr. Jackson",
					 "destroythehumanrace":"Working on this NOT Kappa",
					 "nicememe":"http://i.imgur.com/KsYpXaP.gif"}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
		 
	def post(self):
		h = httplib.HTTPSConnection('api.groupme.com')
		body = {"bot_id":"ca172b2058c8342d2294baf104", "text":""}
		headers = {"Content-Type":"application/json"}
		message = json.loads(self.request.body)['text']
		words = message.split(' ')
		
		if message == '!':
			body['text'] = handleCommand(words[1:])
			h.request("POST", "/v3/bots/post", json.dumps(body), headers)
			h.getresponse()
		else:
			self.response.write("Ignoring Message")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
