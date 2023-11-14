from flask import Flask, render_template

app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ketua_portofolio/')
def ketua_portfolio():
    return render_template('portofolio.html')

@app.route('/anggota1_portofolio/')
def anggota1_portofolio():
    return render_template('portofolio2.html')

@app.route('/anggota2_portofolio/')
def anggota2_portofolio():
    return render_template('portofolio3.html')

@app.route('/anggota3_portofolio/')
def anggota3_portofolio():
    return render_template('portofolio4.html')
    
if __name__== '__main__':
	app.run()