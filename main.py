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
        "watch out for cats",
        "seek the advice of cats",
        "ye who speeks to cats be crazy",
        "use caution with web advice"
    ]

    pick = random.randint(0,3)

    return fortunes[pick]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>fortune cookie</h1>"

        fortune = "<strong>"+getRandomFortune()+ "</strong>"
        fort_sent = "Your fortune is: " + fortune
        fortune_parag = "<p>" + fort_sent + "</p>"

        luck_num = "<strong>"+str(random.randint(1,100))+ "</strong>"
        num_sentence = "your lucky number:" + str(luck_num)
        num_parag = "<p>"+ num_sentence + "</p>"

        cookie_again_button = "<a href = '.'><button>Another Fortune</button></a>"

        content = header + fortune_parag + num_parag + cookie_again_button
        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("log")

routes =[
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
