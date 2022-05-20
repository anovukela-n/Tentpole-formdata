# -*- coding: utf-8 -*-
'''This is a flask server that recieves data from a html form 
it then reads the data and store it in a file and out the results to 
an html file. the inputs include a file with expenses and income which is then plotted against each other'''


from flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def index():
    title ="tentpole"
    return render_template("index.html",title)
@app.route('/',methods =['POST'])
def getValues():
    name= request.form['fname']
    lastname= request.form['lname']
    dateObirth =request.form['dateofbirth']
    filename =request.form['fupload']
    
    #inputFile = pd.read_excel("Income and Expenditure.xlsx")
    inputFile = pd.read_excel(filename)
    print(inputFile)
    plt.legend(loc='upper left')
    plt.xlabel('month')
    plt.ylabel('Amount in Rands')
    plt.style.use('ggplot') 
    plt.plot(inputFile['Month'],inputFile['Income'],inputFile['Expenses']) 
    plt.legend(loc='upper left')
    plt.xlabel('month')
    plt.ylabel('Amount in Rands')    
    plt.style.use('ggplot')  
    plt.plot(inputFile['Month'],inputFile['Income'],inputFile['Expenses'])  
    
    return render_template('result.html', name=name,surname=lastname,dateObirth=dateObirth)
    


if __name__=='__main__':
    app.run