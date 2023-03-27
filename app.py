from flask import Flask, render_template, request, jsonify, session, redirect
import sys
import json
from pymongo import MongoClient
import random
import certifi

app = Flask(__name__)
app.secret_key = "123124324234"

ca = certifi.where()
client = MongoClient('mongodb+srv://ksc:ksc123456@cluster0.od4zh.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.toyTodo