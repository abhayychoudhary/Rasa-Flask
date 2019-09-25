# RASA NLU Test Bot using flask Get API 

Rasa NLU and Rasa Core devs are doing an amazing job improving both of these libraries which results in code changes for one method or another.


## How to use this code

### Installation

Before you start please install the dependency library

1. ```pip install -r requirements.txt```

### To Execute the API in Flask

The code is build with Flask which can be access by the Get API

2.``` python nlu_model.py ```

### Training the NLU model

Training of the mode go to the browser and just send a get request:

2. ``` http://127.0.0.1:5000/train ```

After the completion of the training 
`Training Compleated`


## Testing the NLU model

For Testing the nlu model o to the Browser and just send a get request:

4.```http://127.0.0.1:5000/test?name=your query```








