#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
def getRandomFortune():
    fortunes = [
    "I see much code in your future",
    "Consider eating more fortune cookies",
    "You may have tamed the mighty python, now you must free it onto the Great Spider's Web!"
    ]
    index = random.randint(0, 2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1> Fortune Cookies</h1>"

        fortune= getRandomFortune()
        fortune_sentence = "Your Fortue sentence: " + "<strong>" + fortune + "</strong>"
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"
        lucky_number= "<strong>" + str(random.randint(1, 100))+"</strong>"
        number_sentence = 'Your Lucky Number:' + str(lucky_number)
        number_paragraph = "<p>" + number_sentence +"</p>"

        newcookie_please = "<a href='.'><button> Another Cookie plz! </button></a>"
        content = header+fortune_paragraph + number_paragraph + newcookie_please
        self.response.write(content)
class LoginHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("Thanks for trying to Log in")


routes =[
    ('/', MainHandler),
    ('/login', LoginHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
