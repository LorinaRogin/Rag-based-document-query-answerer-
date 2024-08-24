
import os , requests, re , json
apiKey = "f5c0643e-35ee-4ec1-953d-6d3757e5bc11"
def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter query", "type": "text"}, {"id": "{input_2}", "label": "Upload a pdf file", "type": "file"}]
    prompt = "Answer this query {input_1} from this pdf file url {input_2}"
    filesData, textData = {}, {}
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            f = open(path, 'rb')
            filesData[inputId] = f

    textData['details'] = json.dumps({'appname': 'rag-based document query answerer','prompt': prompt,'documentId': 'no-embd-type','appId' : '66c9801a64d827b744a2a1a8' , 'memoryId' : '','apiKey': apiKey})
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']
usersInputObj = {'{input_1}' : input("Enter query "),'{input_2}' : input("Upload a pdf file (Enter file path) "),}
output = apiFunction(usersInputObj)
url_regex = r'http://localhost:7000/'
replaced_string = re.sub(url_regex,'https://apiappstore.guvi.ai/' , output)
print(replaced_string)
