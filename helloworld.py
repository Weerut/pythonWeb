# This Python file uses the following encoding: utf-8

import webapp2

form="""
<form method="post">
What's your birthday?
<br>

<label>Month
<input type="text" name="month">
</label>

<label>Day
<input type="text" name="day">
</label>

<label>Year
<input type="text" name="year">
</label>

<br>
<br>
<input type="submit">
</form>
"""


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
	
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(form)

	def post(self):
		self.response.write("Yeah here you posted a form")

class TestHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content­Type'] = 'text/plain'
		q=self.request.get("q")
		# self.response.write(q)
		self.response.write(self.request)

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/testform', TestHandler),

], debug=True)
