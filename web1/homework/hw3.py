from flask import Flask, render_template
app = Flask(__name__)
@app.route('/user/<username>')
def users_profile(username):
    users = {
	"quy":   {
			"name": "Dinh Cong Quy",
			"age": 20
                    },
    "tuan anh" : {
			"name" : " Huynh Tuan Anh",
			"age" : 22
             }
            }

    if username in users:
        user = users[username]
        return render_template('user.html', user=user)
    else:
        return 'User not found'
if __name__ == '__main__':
    app.run( debug=True)
