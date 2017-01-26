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
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Encrypt a Message!</h1>"
        textarea = "<textarea name='message_to_encrypt' id='message_to_encrypt'>Enter text here...</textarea>"
        text = "Number of Rotations: <input type='text' name='rot' id='rot'/>"
        submit = "<input type='submit' value='Encrypt!'/>"
        form = "<form action='/EncryptedMessage' method='get' target='_blank'>" + textarea + "<br>" + text + "<br>" + submit + "</form>"
        content = header + form
        self.response.write(content)

class EncryptedMessage(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Here is your encrypted message:</h1>"
        message = self.request.get('message_to_encrypt')
        rot = self.request.get('rot')
        encrypted_message = caesar.encrypt(message, rot)
        footer = "<input type='submit' value='Encrypt a new message?'/>"
        form = "<form action='/'>" + footer + "</form>"
        content = header + encrypted_message + form
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/EncryptedMessage', EncryptedMessage)
], debug=True)
