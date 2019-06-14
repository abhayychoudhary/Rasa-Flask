# RASA NLU Test Bot using flask Get API 
Rasa NLU and Rasa Core devs are doing an amazing job improving both of these libraries which results in code changes for one method or another. In fact, since I recorded a Wetherbot tutorial,


## How to use this repo

The code is build with Flask which can be access by the Get API

1.``` python nlu_model.py ```

### Training the NLU model

Training of the mode go to the Browser and just send a get request:

2. ``` http://127.0.0.1:8080/train ```

After the completion of the training 
`Training Compleated`



### Testing the NLU model

For Testing the nlu model o to the Browser and just send a get request:

3. ```http://127.0.0.1:8080/test?name=your query```






