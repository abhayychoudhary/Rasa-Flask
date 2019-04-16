from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from flask import Flask
import json
app = Flask(__name__)
 
from flask import request

@app.route('/test')
def api_hello():
	if 'name' in request.args:
		interpreter = Interpreter.load('./models/nlu/default/weathernlu')
		test=str(interpreter.parse(request.args['name']))
		return test
		# run_nlu(request.args['name'])
	else:
		return 'Please give a correct output'

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')
	
	
# def run_nlu(question):
# 	interpreter = Interpreter.load('./models/nlu/default/weathernlu')
# 	test=str(interpreter.parse(question))
# 	return test
# if __name__ == '__main__':
# 	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
# 	run_nlu()
@app.route('/train')
def traindata():
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	return "Training Compleated"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
    
